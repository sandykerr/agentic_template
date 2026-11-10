from pathlib import Path
import hashlib, json, subprocess, datetime, re
ROOT = Path('/home/ajkerr1/development/agentic_template')
OUT = Path('/tmp/ticket19-review')
EV = ROOT / '.scratch/ticket-harness/evidence'
CORP = EV / '19-evaluation'
BASE = 'f2929e79cfd5a68f670862775053ae85ba9582b5'
HEAD = 'e90abb64ab95c5b15cdb0949b03c6a948365339b'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
commands=[]
def git(*args):
 p=subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True)
 commands.append({'command':['git',*args], 'exit':p.returncode, 'stdout':p.stdout, 'stderr':p.stderr})
 assert p.returncode == 0
 return p.stdout.strip()
assert git('rev-parse','HEAD') == HEAD
assert not git('status','--short')
assert git('merge-base', BASE, HEAD) == BASE
changed=git('diff','--name-only',BASE+'...'+HEAD).splitlines()
git('log','--oneline',BASE+'..'+HEAD)
git('diff','--check',BASE+'...'+HEAD)
for prefix in ('ticket_harness/','tests/','examples/'):
 assert not any(p.startswith(prefix) for p in changed)
manifest=json.loads((CORP/'source-manifest.json').read_text())
actual={str(p.relative_to(CORP/'snapshot')):sha(p) for p in sorted((CORP/'snapshot').rglob('*')) if p.is_file()}
assert manifest==actual
identity=hashlib.sha256(json.dumps(actual,sort_keys=True).encode()).hexdigest()
assert identity == 'ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23'
for name in manifest:
 if name.startswith('guidance/'):
  original=subprocess.check_output(['git','show',BASE+':'+name[len('guidance/'):]],cwd=ROOT)
  assert original == (CORP/'snapshot'/name).read_bytes(), name
retained=json.loads((CORP/'review-capture.json').read_text())
for name,digest in retained['sha256'].items(): assert sha(CORP/name)==digest,name
last=json.loads((EV/'19-check-results-20261110T163455901396Z.json').read_text())
for field in ('source_identities','helpers','retained_evidence_identities'):
 for name,digest in last[field].items(): assert sha(ROOT/name)==digest,(field,name)
# Source observation without import, pycache, or mutation of the corpus.
ns={}
source=CORP/'snapshot/cases/h8/attempt.py'
exec(compile(source.read_text(),str(source),'exec'),ns)
identity_input={'value':'A'}
revision_input={'value':'r1'}
a=ns['Attempt'](identity_input)
a.submit(revision_input)
a.complete()
before=json.loads(json.dumps(a.snapshot()))
identity_input['value']='B'
revision_input['value']='r2'
after=json.loads(json.dumps(a.snapshot()))
assert after[0]['id']['value']=='B' and after[0]['revision']['value']=='r2'
snapshot=a.snapshot()
snapshot[0]['revision']['value']='r3'
after_snapshot_edit=json.loads(json.dumps(a.snapshot()))
assert after_snapshot_edit[0]['revision']['value']=='r3'
observation={'source_sha256':sha(source),'before_external_input_edits':before,'after_external_input_edits':after,'after_snapshot_edit':after_snapshot_edit,'note':'h8 transition status remains completed, but caller-owned dictionaries and returned nested values change owner state without any owner operation'}
(OUT/'spec-h8-observation.json').write_text(json.dumps(observation,indent=2)+'\n')
# Verify raw reports against only original final records, without exposing unrelated context.
child_files={'spec':'rollout-2026-11-10T11-22-35-01a1c644-ba92-7cd2-bd18-6ffce685a704.jsonl','standards':'rollout-2026-11-10T11-22-48-01a1c644-ec26-74a0-ac6a-7655f53ee9bc.jsonl'}
provenance=[]
for axis,filename in child_files.items():
 path=Path('/home/ajkerr1/.codex/sessions/2026/11/10')/filename
 finals=[]
 for line in path.read_text().splitlines():
  row=json.loads(line); p=row.get('payload',{})
  if row.get('type')=='response_item' and p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':
   finals.append('\n'.join(x['text'] for x in p.get('content',[]) if x.get('type')=='output_text'))
 assert finals and finals[0]==(CORP/f'{axis}-g1-raw.md').read_text(),axis
 rows=json.loads((CORP/f'{axis}-g1-source-records.json').read_text())
 calls=[r for r in rows if r['payload']['type']=='custom_tool_call']
 outputs=[r for r in rows if r['payload']['type']=='custom_tool_call_output']
 provenance.append({'axis':axis,'session_path':str(path),'exact_original_final_match':True,'original_final_sha256':hashlib.sha256(finals[0].encode()).hexdigest(),'retained_call_count':len(calls),'retained_output_count':len(outputs),'calls':[{'timestamp':r['timestamp'],'tool':r['payload'].get('name'),'input_sha256':hashlib.sha256(r['payload'].get('input','').encode()).hexdigest(),'input':r['payload'].get('input','') if 'apply_patch' not in r['payload'].get('input','') else '<preservation-only apply_patch omitted here; full original retained in source-records>'} for r in calls]})
result={'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':commands,'changed_files':changed,'corpus_identity':identity,'corpus_files':len(actual),'all_recorded_final_check_hashes_match_current_bytes':True,'source_provenance':provenance,'h8_observation_path':'/tmp/ticket19-review/spec-h8-observation.json','limits':'Static evidence audits prove identities, not source judgment. No historical evidence helper, builder, harness or runtime suite executed.'}
(OUT/'spec-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'identity_audit':'pass','head':HEAD,'corpus_identity':identity,'corpus_files':len(actual),'raw_finals_match_original_sessions':True,'h8_input_alias_violation_observed':True,'audit':'/tmp/ticket19-review/spec-audit.json'},indent=2))
