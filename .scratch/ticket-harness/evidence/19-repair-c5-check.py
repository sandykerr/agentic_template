"""Audit C5 identity/preservation/navigation; reviewer judgment stays independent."""
from pathlib import Path
from urllib.parse import unquote
import ast, datetime, difflib, gzip, hashlib, json, re, runpy, subprocess
ROOT=Path(__file__).resolve().parents[3]
EV=ROOT/'.scratch/ticket-harness/evidence';CASE=EV/'19-evaluation-g5'
BASE='f2929e79cfd5a68f670862775053ae85ba9582b5';PREVIOUS='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args],text=True).strip()
def mapping(directory):return {str(p.relative_to(directory)):sha(p) for p in sorted(directory.rglob('*')) if p.is_file()}
def verify_capture(case):
    for name,digest in json.loads((case/'review-capture.json').read_text())['sha256'].items():assert sha(case/name)==digest,(case,name)
def main():
    current_owners={'docs/agents/reviewer-evaluation.md','.scratch/ticket-harness/evidence/19-finding-history.md','.scratch/ticket-harness/reviews/ticket-19.md'}
    modified=set(git('diff','--name-only',PREVIOUS).splitlines())
    previous=set(git('ls-tree','-r','--name-only',PREVIOUS).splitlines())
    assert modified & previous <= current_owners,sorted((modified & previous)-current_owners)
    additions=(modified-previous)|set(git('ls-files','--others','--exclude-standard').splitlines())
    for name in additions:
        assert name.startswith(('.scratch/ticket-harness/evidence/19-evaluation-g5/','.scratch/ticket-harness/evidence/19-repair-c5-','.scratch/ticket-harness/evidence/19-review-round2-')) or name in ['.agents/skills/custom/evaluate-reviewers/SKILL.md','.scratch/ticket-harness/evidence/19-repair-c4-preservation.json','.scratch/ticket-harness/evidence/19-review-spec-02.md','.scratch/ticket-harness/evidence/19-review-standards-02.md'],name
    root_context=json.loads((EV/'19-repair-c5-root-context.json').read_text())['sha256']
    for name,digest in root_context.items():assert sha(ROOT/name)==digest,name
    assert (EV/'19-finding-history.md').read_bytes().startswith(subprocess.check_output(['git','show',PREVIOUS+':.scratch/ticket-harness/evidence/19-finding-history.md'],cwd=ROOT))
    for name in ['19-review-capture.json','19-review-round2-capture.json']:
        for filename,digest in json.loads((EV/name).read_text())['sha256'].items():assert sha(EV/filename)==digest,(name,filename)
    corpus_dirs=['19-evaluation','19-evaluation-g2','19-evaluation-g3','19-evaluation-g4','19-evaluation-g5']
    corpora={};manifests=[]
    for folder in corpus_dirs:
        case=EV/folder;manifest=json.loads((case/'source-manifest.json').read_text());manifests.append(manifest)
        assert manifest==mapping(case/'snapshot'),folder
        identity=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest();assert identity==(case/'corpus-identity.txt').read_text().strip()
        corpora[folder]=identity
        verify_capture(case)
    old,new=manifests[-2:];assert set(old)==set(new) and len(new)==36
    delta={name for name in new if old[name]!=new[name]};assert delta=={'cases/b7/git_ops.py','cases/b7/caller.py'}
    for label,folder in [('c2','19-evaluation-g2'),('c3','19-evaluation-g3'),('c4','19-evaluation-g4')]:
        preserved=json.loads((EV/f'19-repair-{label}-preservation.json').read_text())['sha256'];assert preserved==mapping(EV/folder),(label,'preserved stage altered')
    for name,digest in new.items():
        supplied=Path('/tmp/development-review-19-c5')/name
        assert sha(supplied)==digest and not supplied.stat().st_mode & 0o222,name
        if name.startswith('guidance/'):
            assert all(item[name]==digest for item in manifests[1:]),name
            assert sha(ROOT/name.removeprefix('guidance/'))==digest,name
        if name.endswith('/CONTRACT.md') or name.startswith(('cases/a3/','cases/c2/','cases/e4/','cases/g1/')):
            assert all(item[name]==digest for item in manifests),name
    declared=json.loads((CASE/'declaration-capture.json').read_text())
    assert declared['guidance_version']=='G2' and declared['corpus_version']=='C5'
    assert declared['C4_preservation_sha256']==sha(EV/'19-repair-c4-preservation.json')
    assert declared['declaration_sha256']==sha(CASE/'declaration.md') and declared['source_manifest_sha256']==sha(CASE/'source-manifest.json')
    assignments=json.loads((CASE/'assignments.json').read_text())['assignments'];assert len(assignments)==2
    for row in assignments:
        assert row['settings']=={'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'}
        assert datetime.datetime.fromisoformat(declared['declared_at_utc'])<datetime.datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'))
        assert sha(CASE/row['dispatch_path'])==row['dispatch_sha256']
        assert sha(CASE/row['known_readable_prompt_path'])==row['known_readable_prompt_sha256']
        axis=row['label'].removesuffix('-c5');assert declared['known_prompt_sha256'][axis]==row['known_readable_prompt_sha256']
        prompt=(CASE/row['known_readable_prompt_path']).read_text();assert declared['corpus_sha256'] in prompt and '/tmp/development-review-19-c5' in prompt
        records=json.loads((CASE/(row['label']+'-source-records.json')).read_text());observed=[r['settings'] for r in records if r.get('type')=='observed_turn_settings']
        assert observed and all(r['model']=='gpt-6.1-sol' and r['effort']=='high' for r in observed),axis
    for row in json.loads((CASE/'artifact-capture.json').read_text())['mapping']:
        assert sha(CASE/row['retained'])==row['sha256'],row
    probe=EV/'19-repair-c5-skill-probe'
    probe_capture=json.loads((probe/'capture.json').read_text())
    for name,digest in probe_capture['sha256'].items():assert sha(probe/name)==digest,name
    raw=gzip.decompress((probe/probe_capture['lossless_record_capture']['path']).read_bytes())
    assert hashlib.sha256(raw).hexdigest()==probe_capture['lossless_record_capture']['uncompressed_sha256']
    probe_declaration=json.loads((EV/'19-repair-c5-skill-preflight-declaration.json').read_text())
    for name,digest in probe_declaration['input_sha256'].items():assert sha(probe/name)==digest,name
    probe_dispatch=json.loads((probe/'dispatch.json').read_text())
    assert datetime.datetime.fromisoformat(probe_declaration['declared_before_assignment_utc'])<datetime.datetime.fromisoformat(probe_dispatch['timestamp'].replace('Z','+00:00'))
    final_skill=ROOT/'.agents/skills/custom/evaluate-reviewers/SKILL.md'
    skill_delta=json.loads((EV/'19-repair-c5-skill-final-delta.json').read_text())
    assert sha(probe/'inputs/SKILL.md')==probe_declaration['authoring_skill_sha256']==skill_delta['tested_skill_snapshot_sha256']
    assert sha(final_skill)==skill_delta['final_skill_sha256']
    actual_diff=''.join(difflib.unified_diff((probe/'inputs/SKILL.md').read_text().splitlines(keepends=True),final_skill.read_text().splitlines(keepends=True),fromfile='probe-supplied-skill',tofile='final-authored-skill'))
    assert actual_diff==skill_delta['exact_diff']
    probe_records=json.loads((probe/'source-records.json').read_text())
    probe_settings=[r['settings'] for r in probe_records if r.get('type')=='observed_turn_settings']
    assert probe_settings and all(r['model']=='gpt-6.1-sol' and r['effort']=='medium' for r in probe_settings)
    assert not [r for r in probe_records if r.get('payload',{}).get('type')=='function_call' and r['payload'].get('name')=='spawn_agent']
    preflights={}
    for name in ['19-repair-c5-branch-preflight-results.json','19-repair-c5-adapter-preflight-results.json']:
        data=json.loads((EV/name).read_text());assert data['candidate_sources']==new and data['old_sources']==old,name
        assert datetime.datetime.fromisoformat(data['recorded_at_utc'])<datetime.datetime.fromisoformat(declared['declared_at_utc'])
        preflights[name]=sha(EV/name)
    # Earlier source observations remain exact for unchanged controls, never relabeled C5 runs.
    earlier=json.loads((EV/'19-repair-control-preflight-results.json').read_text())['sources']
    assert all(earlier[name]==new[name] for name in new if name.startswith(('cases/d9/','cases/f6/','cases/h8/')))
    saved=EV/'19-evaluation-g3/spec-c3-reviewer-saved.md';frozen=json.loads((EV/'19-repair-c3-preservation.json').read_text())['sha256'][saved.name]
    assert sha(saved)==frozen and len(saved.read_bytes())-len(saved.read_bytes().rstrip(b'\n'))==2
    anchors=runpy.run_path(str(EV/'16-check.py'))['anchors'];links=[]
    routes=['.agents/skills/custom/references/planning.md','.agents/skills/custom/implement-with-checkboxes/SKILL.md','.agents/skills/custom/create-next-agent-prompt/SKILL.md']
    docs=[ROOT/'.agents/skills/custom/evaluate-reviewers/SKILL.md',ROOT/'docs/agents/reviewer-evaluation.md',EV/'19-repair-c5-report.md',EV/'19-repair-c5-skill-observation.md',EV/'19-finding-history.md',ROOT/'.scratch/ticket-harness/reviews/ticket-19.md']+[ROOT/name for name in routes]
    docs += [p for p in CASE.glob('*.md') if not p.name.endswith(('-raw.md','-reviewer-saved.md'))]
    for path in docs:
        text=re.sub(r'^```[^\n]*\n.*?^```\s*$','',path.read_text(),flags=re.M|re.S);text=re.sub(r'`[^`\n]+`','',text)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',text):
            if re.match(r'[a-z]+://',href):continue
            name,_,fragment=unquote(href).partition('#');name=re.sub(r':\d+$','',name);target=(path.parent/name).resolve() if name else path
            assert target.exists(),(path,href)
            if fragment:assert fragment in anchors(target),(path,href)
            links.append({'from':str(path.relative_to(ROOT)),'href':href})
    assert '19-evaluation-g5' in (ROOT/'docs/agents/reviewer-evaluation.md').read_text()
    for name in routes:assert 'reviewer-evaluation.md' in (ROOT/name).read_text(),name
    syntax=list(EV.glob('19-repair-c5-*.py'))+list(CASE.glob('*.py'))+list((CASE/'snapshot/cases').rglob('*.py'))+list(probe.rglob('*.py'))
    for path in syntax:ast.parse(path.read_text(),filename=str(path))
    result={'result':'pass','recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':BASE,'previous_source':PREVIOUS,'head_before_checkpoint':git('rev-parse','HEAD'),'scope':'C5 standalone source/guidance/evaluation repair audit, no production runtime/tests or judgment scoring','protected_previous_paths':len(previous-current_owners),'changed_previous_owners':sorted(modified & previous),'corpora':corpora,'C5_source_delta':sorted(delta),'corpus_files_each':36,'root_context_sha256':sha(EV/'19-repair-c5-root-context.json'),'preflight_sha256':preflights,'checked_document_sha256':{str(p.relative_to(ROOT)):sha(p) for p in docs},'local_links':links,'authoring_skill_final_sha256':sha(final_skill),'authoring_probe_capture_sha256':sha(probe/'capture.json'),'authoring_probe_tested_skill_sha256':skill_delta['tested_skill_snapshot_sha256'],'python_syntax_files':len(syntax),'current_evidence_sha256':{str(p.relative_to(ROOT)):sha(p) for p in sorted(CASE.rglob('*')) if p.is_file()},'helper_sha256':{p.name:sha(p) for p in syntax if p.parent==EV},'immutable_whitespace_exception':{'path':str(saved.relative_to(ROOT)),'sha256':frozen,'trailing_LF_bytes':2,'scope':'Only blank-at-EOF allowance on this exact frozen report; every other whitespace rule/path checked normally; full default failure retained separately'},'limits':'Mechanical identity/link/syntax/protection checks establish their facts, not reviewer judgment. Full independent originals and manual per-case adjudication remain separate.'}
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');target=EV/f'19-repair-c5-check-results-{stamp}.json';assert not target.exists();target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'result':'pass','result_path':str(target.relative_to(ROOT)),'protected_paths':result['protected_previous_paths'],'local_links':len(links),'corpus':declared['corpus_sha256']},indent=2))
if __name__=='__main__':main()
