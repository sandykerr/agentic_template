from pathlib import Path
import ast
import datetime
import hashlib
import json
import subprocess

ROOT = Path('/home/ajkerr1/development/agentic_template')
OUT = Path('/tmp/ticket19-review')
CASE = ROOT / '.scratch/ticket-harness/evidence/19-evaluation'
BASE = 'f2929e79cfd5a68f670862775053ae85ba9582b5'
HEAD = 'e90abb64ab95c5b15cdb0949b03c6a948365339b'
def digest(data): return hashlib.sha256(data).hexdigest()
def sha(path): return digest(path.read_bytes())
def git(*args): return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()
result = {'time': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'baseline': BASE,
          'source': HEAD, 'head': git('rev-parse','HEAD'), 'status': git('status','--short')}
assert result['head'] == HEAD
assert not result['status']
names = git('diff','--name-only',BASE+'...'+HEAD).splitlines()
result['changed_paths'] = names
for name in names:
    assert name.startswith('.scratch/ticket-harness/evidence/19-') or name in [
        'docs/agents/reviewer-evaluation.md', '.agents/skills/custom/references/planning.md',
        '.agents/skills/custom/implement-with-checkboxes/SKILL.md',
        '.agents/skills/custom/create-next-agent-prompt/SKILL.md'], name
    assert (ROOT/name).read_bytes() == subprocess.check_output(['git','-C',str(ROOT),'show',HEAD+':'+name])
result['exact_changed_worktree_bytes'] = True
manifest = json.loads((CASE/'source-manifest.json').read_text())
actual = {str(p.relative_to(CASE/'snapshot')):sha(p) for p in sorted((CASE/'snapshot').rglob('*')) if p.is_file()}
assert actual == manifest
result['corpus_identity'] = digest(json.dumps(manifest,sort_keys=True).encode())
assert result['corpus_identity'] == 'ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23'
for name in manifest:
    if name.startswith('guidance/'):
        original = subprocess.check_output(['git','-C',str(ROOT),'show',BASE+':'+name.removeprefix('guidance/')])
        assert original == (CASE/'snapshot'/name).read_bytes()
        assert original == (ROOT/name.removeprefix('guidance/')).read_bytes()
result['frozen_guidance_matches_baseline_and_current'] = True
for key in ['review-capture.json','review-capture-supplement.json']:
    capture = json.loads((CASE/key).read_text())
    if key == 'review-capture.json':
        for name, expected in capture['sha256'].items(): assert sha(CASE/name) == expected, name
    else:
        for row in capture['axes'].values(): assert sha(CASE/row['source_records_path']) == row['source_records_sha256']
result['retained_capture_hashes_match'] = True
final_check = json.loads((ROOT/'.scratch/ticket-harness/evidence/19-check-results-20261110T163455901396Z.json').read_text())
for group in ['source_identities','helpers','retained_evidence_identities']:
    for name, expected in final_check[group].items(): assert sha(ROOT/name) == expected, name
result['final_check_hashes_match_current_commit'] = True
result['final_check_summary'] = {key:final_check[key] for key in ['result','recorded_at_utc','head_before_checkpoint','corpus_files','protected_baseline_paths','scope','limits']}
result['recorded_local_links'] = len(final_check['local_links'])
result['sessions'] = {}
logs = Path('/home/ajkerr1/.codex/sessions/2026/11/10')
sessions = {
 'spec-g1':'rollout-2026-11-10T11-22-35-01a1c644-ba92-7cd2-bd18-6ffce685a704.jsonl',
 'standards-g1':'rollout-2026-11-10T11-22-48-01a1c644-ec26-74a0-ac6a-7655f53ee9bc.jsonl'}
for label,name in sessions.items():
    records = json.loads((CASE/(label+'-source-records.json')).read_text())
    calls = [{'timestamp':r['timestamp'],'input':r['payload']['input']} for r in records if r['payload']['type']=='custom_tool_call']
    outputs = [r for r in records if r['payload']['type']=='custom_tool_call_output']
    observed_exits = []
    for row in outputs:
        for part in row['payload']['output']:
            if part['type']=='input_text':
                try: value=json.loads(part['text'])
                except (json.JSONDecodeError,TypeError): continue
                if isinstance(value,dict) and 'exit_code' in value: observed_exits.append(value['exit_code'])
    original = [json.loads(line) for line in (logs/name).read_text().splitlines()]
    finals = []
    for row in original:
        p = row['payload']
        if row['type']=='response_item' and p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':
            finals.append('\n'.join(x['text'] for x in p['content'] if x.get('type')=='output_text'))
    assert len(finals)==2
    assert finals[0].encode() == (CASE/(label+'-raw.md')).read_bytes()
    assert (CASE/(label+'-reviewer-preserved.md')).read_text().rstrip('\n') == finals[0].rstrip('\n')
    original_selected = [row for row in original if row['type']=='response_item' and row['payload'].get('type') in ['custom_tool_call','custom_tool_call_output','agent_message']]
    assert original_selected == records
    result['sessions'][label]={'source_log':str(logs/name),'source_log_sha256':sha(logs/name),
        'original_raw_final_matches':True,'original_source_records_match':True,'calls':calls,
        'custom_output_count':len(outputs),'parsed_shell_exit_codes':observed_exits,
        'limits':'Only selected corpus session records inspected; received task payload remains opaque; no backend enforcement inferred.'}
ns = {}
source = (CASE/'snapshot/cases/h8/attempt.py').read_text()
exec(compile(source, 'frozen-h8/attempt.py', 'exec'), ns)
Attempt = ns['Attempt']
scalar = Attempt('A'); scalar.submit('r1'); scalar.complete()
snapshot = scalar.snapshot(); snapshot[0]['status'] = 'tampered'
assert scalar.snapshot()[0]['status'] == 'completed'
identity = {'id':'A'}
revision = {'rev':'r1'}
mutable = Attempt(identity); mutable.submit(revision)
identity['id'] = 'B'; revision['rev'] = 'r2'
mutable_snapshot = mutable.snapshot()
mutable_snapshot[0]['revision']['rev'] = 'r3'
result['h8_disposable_observation'] = {'scalar_top_level_copy_isolated':True,
    'caller_owned_identity_mutation_visible':mutable.snapshot()[0]['id']['id']=='B',
    'caller_owned_revision_and_snapshot_nested_mutation_visible':mutable.snapshot()[0]['revision']['rev']=='r3',
    'conclusion_limit':'Shows shallow-copy aliasing for dictionary-valued identity/revision; whether those are domain inputs requires interpretation of the frozen contract.'}
result['standards_files_search'] = git('ls-files','*CODING_STANDARDS.md','*CONTRIBUTING.md').splitlines()
result['guide_route_search'] = subprocess.check_output(['rg','-n','reviewer-evaluation|ownership-review|architecture-checkpoints|review-records',
    '.agents/skills/custom','docs/agents','.scratch/ticket-harness/milestones.md'],cwd=ROOT,text=True).splitlines()
for path in CASE.rglob('*.py'): ast.parse(path.read_text(),filename=str(path))
for path in [ROOT/'.scratch/ticket-harness/evidence/19-check.py']: ast.parse(path.read_text(),filename=str(path))
result['evidence_python_syntax'] = 'pass; parsed without executing historical writers'
(OUT/'standards-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['sessions','changed_paths','guide_route_search']},indent=2))
for label, row in result['sessions'].items():
    print(label, 'original finals/source records match', row['parsed_shell_exit_codes'])
    for call in row['calls']: print(call['timestamp'], call['input'])
