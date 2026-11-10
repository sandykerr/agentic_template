from pathlib import Path
import ast, datetime, difflib, gzip, hashlib, json, os, re, subprocess, sys, tempfile, types
ROOT=Path('/home/ajkerr1/development/agentic_template'); OUT=Path('/tmp/ticket19-review3'); EV=ROOT/'.scratch/ticket-harness/evidence'
BASE='f2929e79cfd5a68f670862775053ae85ba9582b5'; CURRENT='8e2c82679a2314e31ebff69accab3743f55f996d'; PREV='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT).decode().strip()
def mapping(p): return {str(f.relative_to(p)):sha(f) for f in sorted(p.rglob('*')) if f.is_file()}
assert git('rev-parse','HEAD')==CURRENT
assert git('merge-base',BASE,CURRENT)==BASE
assert git('status','--porcelain')==''
changes=git('diff','--name-only',BASE+'...'+CURRENT).splitlines()
assert not any(x.startswith(('ticket_harness/','tests/','examples/')) for x in changes)
corpora=[]; captures=[]; tool_inventory=[]; raw_finals=[]
for folder in ['19-evaluation','19-evaluation-g2','19-evaluation-g3','19-evaluation-g4','19-evaluation-g5']:
    p=EV/folder; m=json.loads((p/'source-manifest.json').read_text()); assert m==mapping(p/'snapshot')
    aggregate=hashlib.sha256(json.dumps(m,sort_keys=True).encode()).hexdigest(); assert aggregate==(p/'corpus-identity.txt').read_text().strip()
    corpora.append({'directory':folder,'manifest':m,'aggregate':aggregate})
    cap=json.loads((p/'review-capture.json').read_text())
    for name,digest in cap['sha256'].items(): assert sha(p/name)==digest,(folder,name)
    captures.append({'path':str(p/'review-capture.json'),'sha256':sha(p/'review-capture.json')})
    provenance=json.loads((p/'capture-provenance.json').read_text())
    for label,info in provenance.items():
        if not isinstance(info,dict) or 'session_path' not in info: continue
        session=Path(info['session_path']); rows=[json.loads(line) for line in session.read_text().splitlines()]
        finals=[]; calls=[]; settings=[]
        for row in rows:
            payload=row.get('payload',{})
            if row['type']=='response_item' and payload.get('type')=='message' and payload.get('role')=='assistant' and payload.get('phase')=='final_answer': finals.append('\n'.join(x['text'] for x in payload.get('content',[]) if x.get('type')=='output_text'))
            if row['type']=='turn_context': settings.append({k:payload[k] for k in ['model','effort'] if k in payload})
            if row['type']=='response_item' and payload.get('type') in ['function_call','custom_tool_call']:
                calls.append({'name':payload.get('name'),'arguments':payload.get('arguments',payload.get('input'))})
        raw=p/(label+'-raw.md')
        if raw.exists(): assert raw.read_text()==finals[0],(folder,label)
        else:
            # G1 provenance labels may use axes rather than report prefixes.
            candidates=list(p.glob(label+'*-raw.md')); assert len(candidates)==1,(label,candidates);raw=candidates[0];assert raw.read_text()==finals[0]
        raw_finals.append({'directory':folder,'label':label,'session':str(session),'original_final_count':len(finals),'report_sha256':sha(raw),'settings':settings})
        tool_inventory.append({'directory':folder,'label':label,'calls':calls})
for stage in ['c2','c3','c4']:
    p=EV/('19-evaluation-g'+stage[-1]); preserved=json.loads((EV/('19-repair-'+stage+'-preservation.json')).read_text())['sha256']; assert mapping(p)==preserved
for m in corpora:
    for name,digest in m['manifest'].items():
        if name.endswith('/CONTRACT.md') or name.startswith(('cases/a3/','cases/c2/','cases/e4/','cases/g1/')): assert digest==corpora[0]['manifest'][name]
        if name.startswith('guidance/') and m!=corpora[0]: assert digest==corpora[1]['manifest'][name]
deltas=[]
for old,new in zip(corpora,corpora[1:]): deltas.append({'from':old['directory'],'to':new['directory'],'changed':[n for n in new['manifest'] if new['manifest'][n]!=old['manifest'][n]]})
assert deltas[-1]['changed']==['cases/b7/caller.py','cases/b7/git_ops.py']
# Prior tracked files must remain identical except declared mutable current summaries.
prior=git('ls-tree','-r','--name-only',PREV).splitlines(); modified=git('diff','--name-only',PREV,CURRENT).splitlines()
allowed={'docs/agents/reviewer-evaluation.md','.scratch/ticket-harness/evidence/19-finding-history.md','.scratch/ticket-harness/reviews/ticket-19.md'}
assert set(prior)&set(modified)<=allowed
for capture in ['19-review-capture.json','19-review-round2-capture.json']:
    for name,digest in json.loads((EV/capture).read_text())['sha256'].items(): assert sha(EV/name)==digest
finalcheck=json.loads((EV/'19-repair-c5-check-results-20261110T180103445335Z.json').read_text())
for category in ['checked_document_sha256','current_evidence_sha256']:
    for name,digest in finalcheck[category].items(): assert sha(ROOT/name)==digest,(category,name)
for name,digest in finalcheck['helper_sha256'].items(): assert sha(EV/name)==digest
# Probe original record identity and distinct final skill bytes.
probe=EV/'19-repair-c5-skill-probe'; cap=json.loads((probe/'capture.json').read_text())
for name,digest in cap['sha256'].items(): assert sha(probe/name)==digest
loss=cap['lossless_record_capture']; raw=gzip.decompress((probe/loss['path']).read_bytes()); assert hashlib.sha256(raw).hexdigest()==loss['uncompressed_sha256']
probe_records=[json.loads(line) for line in raw.splitlines()]; assert probe_records
skill=ROOT/'.agents/skills/custom/evaluate-reviewers/SKILL.md'; delta=json.loads((EV/'19-repair-c5-skill-final-delta.json').read_text());assert sha(probe/'inputs/SKILL.md')==delta['tested_skill_snapshot_sha256'];assert sha(skill)==delta['final_skill_sha256']
assert ''.join(difflib.unified_diff((probe/'inputs/SKILL.md').read_text().splitlines(keepends=True),skill.read_text().splitlines(keepends=True),fromfile='probe-supplied-skill',tofile='final-authored-skill'))==delta['exact_diff']
# Full default failure is explicit; exception is only one exact frozen path.
saved='.scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md'; whites=[]
for cmd in [['git','diff','--check',BASE+'...'+CURRENT],['git','diff','--check',BASE+'...'+CURRENT,'--','.',':(exclude)'+saved],['git','-c','core.whitespace=-blank-at-eof','diff','--check',BASE+'...'+CURRENT,'--',saved]]:
    r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True);whites.append({'command':cmd,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
assert [x['exit'] for x in whites]==[2,0,0];assert whites[0]['stdout']==saved+':202: new blank line at EOF.\n';assert sha(ROOT/saved)=='75dbfbdde31879ceeb2f35bb50fb6fe0a318f09cfbb6d15fb6fb76502a40f84d';assert (ROOT/saved).read_bytes().endswith(b'\n\n') and not (ROOT/saved).read_bytes().endswith(b'\n\n\n')
validators=[]
for name in ['implement-with-checkboxes','create-next-agent-prompt','evaluate-reviewers']:
    cmd=[sys.executable,'/home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py',str(ROOT/'.agents/skills/custom'/name)];r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONPATH':'/usr/lib/python3/dist-packages'});assert r.returncode==0;validators.append({'command':cmd,'exit':r.returncode,'stdout':r.stdout})
summary={'baseline':BASE,'source':CURRENT,'commits':git('log','--oneline',BASE+'..'+CURRENT).splitlines(),'changed_paths':{n:sha(ROOT/n) for n in changes},'corpora':corpora,'deltas':deltas,'raw_final_checks':raw_finals,'captures':captures,'protected_old_paths':len(set(prior)-allowed),'recorded_final_checks':{'path':'19-repair-c5-check-results-20261110T180103445335Z.json','sha256':sha(EV/'19-repair-c5-check-results-20261110T180103445335Z.json'),'links':len(finalcheck['local_links'])},'whitespace':whites,'validators':validators,'probe_lossless_record_count':len(probe_records),'skill_delta_verified':True,'worktree_after':git('status','--porcelain')}
(OUT/'spec-tool-inventory.json').write_text(json.dumps(tool_inventory,indent=2)+'\n');(OUT/'spec-audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'audit':'pass','corpora':len(corpora),'raw_finals':len(raw_finals),'protected_old_paths':summary['protected_old_paths'],'whitespace_exits':[x['exit'] for x in whites],'validators':len(validators)}))
