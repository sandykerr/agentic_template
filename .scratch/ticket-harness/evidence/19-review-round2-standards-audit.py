from pathlib import Path
from copy import deepcopy
import ast, dataclasses, datetime, hashlib, json, os, re, subprocess, sys, tempfile, types

ROOT=Path('/home/ajkerr1/development/agentic_template')
OUT=Path('/tmp/ticket19-review2')
EV=ROOT/'.scratch/ticket-harness/evidence'
BASE='f2929e79cfd5a68f670862775053ae85ba9582b5'
SOURCE='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93'
REJECTED='e90abb64ab95c5b15cdb0949b03c6a948365339b'
commands=[]
def command(args,expected=0):
    p=subprocess.run(args,cwd=ROOT,capture_output=True)
    row={'argv':list(map(str,args)),'exit':p.returncode,'stdout':os.fsdecode(p.stdout),'stderr':os.fsdecode(p.stderr)}
    commands.append(row)
    assert p.returncode==expected,row
    return p.stdout
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(commit,path): return command(['git','show',commit+':'+path])
def read_json(p):return json.loads(p.read_text())
def load(path,name):
    mod=types.ModuleType(name);sys.modules[name]=mod
    exec(compile(path.read_bytes(),str(path),'exec'),mod.__dict__)
    return mod

result={'assessment':'review-ticket-19','report':'standards-02','baseline':BASE,'source':SOURCE,'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'limits':'Independent standards source/evidence review; config is not backend enforcement, context telemetry unavailable; only /tmp observations, no production suite or historical writer execution.'}
assert command(['git','rev-parse','HEAD']).decode().strip()==SOURCE
assert command(['git','status','--porcelain'])==b''
assert command(['git','merge-base',BASE,SOURCE]).decode().strip()==BASE
result['commits']=command(['git','log',BASE+'..'+SOURCE,'--oneline']).decode().splitlines()
changed=command(['git','diff','--name-only',BASE+'...'+SOURCE]).decode().splitlines()
result['changed_sources']={p:sha(ROOT/p) for p in changed}
for p in changed:assert (ROOT/p).read_bytes()==blob(SOURCE,p),p
old_paths=command(['git','ls-tree','-r','--name-only',REJECTED]).decode().splitlines()
changed_old=command(['git','diff','--name-only',REJECTED,SOURCE]).decode().splitlines()
assert set(changed_old)&set(old_paths)=={'docs/agents/ownership-review.md','docs/agents/reviewer-evaluation.md'}
result['changed_existing_paths']=sorted(set(changed_old)&set(old_paths))
result['preserved_rejected_paths']=len(old_paths)-2
assert not any(p.startswith(('ticket_harness/','tests/','examples/')) for p in changed)
paths=['AGENTS.md','GLOSSARY.md','docs/agents/domain.md','docs/agents/testing.md','docs/agents/python-environment.md','docs/agents/issue-tracker.md','docs/agents/triage-labels.md','docs/agents/ownership-review.md','docs/agents/review-records.md','docs/agents/architecture-checkpoints.md','docs/templates/reviews/report.md','.scratch/ticket-harness/spec.md','.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md','.scratch/ticket-harness/README.md','.scratch/ticket-harness/reviews/ticket-17.md','.scratch/ticket-harness/reviews/ticket-18.md','.agents/skills/custom/grill-to-tickets/SKILL.md','.agents/skills/custom/references/planning.md','.agents/skills/custom/implement-with-checkboxes/SKILL.md','.agents/skills/custom/create-next-agent-prompt/SKILL.md','.agents/skills/matt-pocock/code-review/SKILL.md','.agents/skills/matt-pocock/implement/SKILL.md','.agents/skills/custom/test-strategy/SKILL.md','.agents/skills/matt-pocock/codebase-design/SKILL.md','.agents/skills/matt-pocock/writing-for-agents/SKILL.md']
paths+=['docs/adr/'+p.name for p in (ROOT/'docs/adr').glob('*.md')]
result['instructions_collaborators']={p:sha(ROOT/p) for p in paths}
result['external_instructions']={str(p):sha(p) for p in [OUT/'standards-assignment.txt',OUT/'common.txt',Path('/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md')]}
corpora=[];manifests=[];tool_inventory=[]
for directory,temp,label in [('19-evaluation','/tmp/development-review-19-g1','g1'),('19-evaluation-g2','/tmp/development-review-19-g2','g2'),('19-evaluation-g3','/tmp/development-review-19-c3','c3'),('19-evaluation-g4','/tmp/development-review-19-c4','c4')]:
    case=EV/directory;snapshot=case/'snapshot'
    manifest=read_json(case/'source-manifest.json');manifests.append(manifest)
    assert set(manifest)=={str(p.relative_to(snapshot)) for p in snapshot.rglob('*') if p.is_file()}
    for p,digest in manifest.items():
        assert sha(snapshot/p)==digest
        assert sha(Path(temp)/p)==digest
        assert not (Path(temp)/p).stat().st_mode&0o222
    aggregate=hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
    assert aggregate==(case/'corpus-identity.txt').read_text().strip()
    capture=read_json(case/'declaration-capture.json')
    assert sha(case/'declaration.md')==capture['declaration_sha256']
    assert sha(case/'source-manifest.json')==capture['source_manifest_sha256']
    assignments=read_json(case/'assignments.json')['assignments'];assert len(assignments)==2
    for row in assignments:
        assert row['settings']=={'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'}
        assert datetime.datetime.fromisoformat(capture['declared_at_utc'])<datetime.datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'))
        pathkey='dispatch_path' if 'dispatch_path' in row else 'prompt_path'
        hashkey='dispatch_sha256' if 'dispatch_sha256' in row else 'prompt_sha256'
        assert sha(case/row[pathkey])==row[hashkey]
        if 'known_readable_prompt_path' in row:assert sha(case/row['known_readable_prompt_path'])==row['known_readable_prompt_sha256']
    for p,digest in read_json(case/'review-capture.json')['sha256'].items(): assert sha(case/p)==digest,(directory,p)
    sessions=read_json(case/'capture-provenance.json')
    for axis in ['spec','standards']:
        key=axis+'-'+label
        if label=='g1':
            filename={'spec':'rollout-2026-11-10T11-22-35-01a1c644-ba92-7cd2-bd18-6ffce685a704.jsonl','standards':'rollout-2026-11-10T11-22-48-01a1c644-ec26-74a0-ac6a-7655f53ee9bc.jsonl'}[axis]
            session=Path('/home/ajkerr1/.codex/sessions/2026/11/10')/filename
        else:session=Path(sessions[key]['session_path'])
        rows=[json.loads(line) for line in session.read_text().splitlines()]
        finals=[];selected=[];settings=[];calls=[]
        for row in rows:
            p=row['payload']
            if row['type']=='session_meta':
                source=p.get('source',{});assert source['subagent']['thread_spawn']['agent_path'].endswith('/corpus_'+axis+'_'+label)
                selected.append({'timestamp':row['timestamp'],'type':'session_identity','id':p['id'],'cwd':p['cwd'],'source':source,'model_provider':p.get('model_provider')})
            elif row['type']=='turn_context':
                s={k:p[k] for k in ['model','effort','reasoning_effort','model_provider','cwd'] if k in p};settings.append(s)
                selected.append({'timestamp':row['timestamp'],'type':'observed_turn_settings','settings':s})
            elif row['type']=='response_item':
                if p.get('type')=='message' and p.get('role')=='assistant' and p.get('phase')=='final_answer':finals.append('\n'.join(v['text'] for v in p.get('content',[]) if v.get('type')=='output_text'))
                if p.get('type') in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output','agent_message']:selected.append(row)
                if p.get('type') in ['function_call','custom_tool_call']: calls.append({'name':p.get('name'),'arguments':p.get('arguments',p.get('input'))})
        assert len(finals)==(2 if label=='g1' else 1)
        assert (case/(key+'-raw.md')).read_text()==finals[0]
        if label!='g1':assert read_json(case/(key+'-source-records.json'))==selected
        assert all(s.get('model')=='gpt-6.1-sol' for s in settings)
        assert all(s.get('effort',s.get('reasoning_effort'))=='high' for s in settings)
        tool_inventory.append({'corpus':label,'axis':axis,'session':str(session),'settings':settings,'final_count':len(finals),'calls':calls})
    corpora.append({'directory':directory,'aggregate':aggregate,'files':len(manifest),'assignments':assignments,'declaration':capture,'session_originals_match':True})
result['corpora']=corpora
result['version_deltas']=[[p for p in manifests[i] if manifests[i][p]!=manifests[i-1][p]] for i in range(1,4)]
assert result['version_deltas']==[['cases/h8/attempt.py','guidance/docs/agents/ownership-review.md'],['cases/b7/git_ops.py','cases/d9/plan.py','cases/f6/io_ops.py'],['cases/b7/caller.py']]
for manifest in manifests[1:]:
    for p,digest in manifest.items():
        if p.startswith('guidance/'):assert sha(ROOT/p.removeprefix('guidance/'))==digest
for version in ['c2','c3']:
    case=EV/('19-evaluation-g2' if version=='c2' else '19-evaluation-g3')
    preservation=read_json(EV/f'19-repair-{version}-preservation.json')['sha256']
    assert set(preservation)=={str(p.relative_to(case)) for p in case.rglob('*') if p.is_file()}
    for p,digest in preservation.items():assert sha(case/p)==digest
final_checks=read_json(EV/'19-repair-check-results-20261110T172627119721Z.json')
checked=0
for group in ['checked_sources','retained_new_evidence','repair_evidence_identities','repair_helpers']:
    for p,digest in final_checks[group].items():
        path=ROOT/p if group in ['checked_sources','retained_new_evidence'] else EV/p
        assert sha(path)==digest,(group,p);checked+=1
result['final_check_identities_matched']=checked
saved=EV/'19-evaluation-g3/spec-c3-reviewer-saved.md'
assert len(saved.read_bytes())-len(saved.read_bytes().rstrip(b'\n'))==2
command(['git','diff','--check',BASE,SOURCE],expected=2)
command(['git','diff','--check',BASE,SOURCE,'--','.',':(exclude).scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md'])
command(['git','-c','core.whitespace=-blank-at-eof','diff','--check',BASE,SOURCE,'--','.scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md'])
result['whitespace_exception']={'path':str(saved.relative_to(ROOT)),'sha256':sha(saved),'trailing_LF':2,'default_full_exit':2,'default_every_other_path_exit':0,'only_saved_report_blank_at_EOF_ignored_exit':0}
command(['bash','-n',str(EV/'19-repair-run-checks.sh')])
for name in ['implement-with-checkboxes','create-next-agent-prompt']:
    command(['env','PYTHONPATH=/usr/lib/python3/dist-packages',sys.executable,'/home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py','.agents/skills/custom/'+name])
pyfiles=[ROOT/p for p in changed if p.endswith('.py')]
for path in pyfiles:ast.parse(path.read_bytes(),filename=str(path))
result['python_AST_files']=len(pyfiles)
for route in ['.agents/skills/custom/references/planning.md','.agents/skills/custom/implement-with-checkboxes/SKILL.md','.agents/skills/custom/create-next-agent-prompt/SKILL.md']:
    assert 'reviewer-evaluation.md' in (ROOT/route).read_text()

# Disposable behavior observations execute exact source in memory, never importing repository modules.
observations={}
for label,directory in [('C1','19-evaluation'),('C4','19-evaluation-g4')]:
    h=load(EV/directory/'snapshot/cases/h8/attempt.py','standards_h8_'+label)
    identity={'nested':['A']};revision={'nested':['r1']};a=h.Attempt(identity)
    before=deepcopy(a.snapshot())
    for op in [a.complete,lambda:a.submit({}),lambda:a.submit('')]:
        try:op();raise AssertionError('accepted invalid op')
        except ValueError:pass
        assert a.snapshot()==before
    a.submit(revision); submitted=deepcopy(a.snapshot());identity['nested'].append('ingress');revision['nested'].append('ingress')
    detached=a.snapshot()==submitted
    a.complete();completed=deepcopy(a.snapshot());x,y=a.snapshot();x['id']['nested'].append('output');y['revision']['nested'].append('output')
    isolated=a.snapshot()==completed
    before=deepcopy(a.snapshot())
    for op in [a.complete,lambda:a.submit({'x':1})]:
        try:op();raise AssertionError('accepted invalid terminal op')
        except ValueError:pass
        assert a.snapshot()==before
    observations[label]={'input_isolated':detached,'snapshot_isolated':isolated,'mirrored':a.snapshot()[0]==a.snapshot()[1],'invalid_operations_unchanged':True,'source_sha256':sha(EV/directory/'snapshot/cases/h8/attempt.py')}
assert not observations['C1']['input_isolated'] and not observations['C1']['snapshot_isolated']
assert observations['C4']['input_isolated'] and observations['C4']['snapshot_isolated'] and observations['C4']['mirrored']
with tempfile.TemporaryDirectory(prefix='standards19-',dir=OUT) as temp:
    parent=Path(temp); roots=[]
    for kind,name in [('space','repo '),('CR','repo\rname'),('LF','repo\n'),('Unicode','répo'),('nonUTF8',os.fsdecode(b'repo-\xff'))]:
        checkout=parent/name;checkout.mkdir()
        command(['git','init','--quiet','--initial-branch=main',str(checkout)])
        command(['git','-C',str(checkout),'-c','user.name=Standards review','-c','user.email=review@example.invalid','commit','--quiet','--allow-empty','-m','observation'])
        base=command(['git','-C',str(checkout),'rev-parse','HEAD']).decode().strip()
        row={'kind':kind}
        for version,directory in [('C3','19-evaluation-g3'),('C4','19-evaluation-g4')]:
            load(EV/directory/'snapshot/cases/b7/git_ops.py','git_ops')
            caller=load(EV/directory/'snapshot/cases/b7/caller.py','standards_b7_'+kind+version)
            try:
                root,branch=caller.preflight(checkout,'main',base);row[version]={'equal':root==checkout.resolve(),'branch':branch}
            except UnicodeDecodeError:row[version]={'UnicodeDecodeError':True}
        assert row['C4']['equal'];roots.append(row)
    assert next(r for r in roots if r['kind']=='CR')['C3']['equal'] is False
    assert next(r for r in roots if r['kind']=='nonUTF8')['C3']['UnicodeDecodeError']
    observations['b7_paths']=roots
    parser=load(EV/'19-evaluation-g4/snapshot/cases/d9/plan.py','standards_plan')
    parsed=parser.parse(' z: x+y, x:,y:x+x ')
    assert [(t.id,t.dependencies) for t in parsed]==[('z',('x','y')),('x',()),('y',('x','x'))]
    invalid=['a:+','a:,b:a+','a:missing','a:b,b:a','a:,a:',' :']
    for value in invalid:
        try:parser.parse(value);raise AssertionError(value)
        except ValueError:pass
    chain=','.join(f'N{i}:N{i+1}' for i in range(1499))+',N1499:'
    assert len(parser.parse(chain))==1500
    observations['d9']={'invalid_rejections':invalid,'ordered_shared_repeated_dependencies':True,'valid_chain_nodes':1500}
    io=load(EV/'19-evaluation-g4/snapshot/cases/f6/io_ops.py','standards_io')
    destination=parent/'text';destination.write_text('old');before=set(parent.iterdir())
    try:io.atomic_write(destination,'\ud800');raise AssertionError('encoding accepted')
    except UnicodeEncodeError:pass
    assert destination.read_text()=='old' and set(parent.iterdir())==before
    io.atomic_write(destination,'new');assert destination.read_text()=='new' and set(parent.iterdir())==before
    for t in [None,float('inf'),float('nan')]:
        try:io.invoke(['/nonexistent'],parent,t);raise AssertionError('unbounded accepted')
        except ValueError:pass
    p=io.invoke([sys.executable,'-c','import sys;print("out");sys.exit(7)'],parent,2)
    assert p.returncode==7 and p.stdout=='out\n'
    for t in [0,-1,0.01]:
        try:io.invoke([sys.executable,'-c','import time;time.sleep(1)'],parent,t);raise AssertionError('timeout not raised')
        except subprocess.TimeoutExpired:pass
    observations['f6']={'encoding_failure_preserves_old_and_cleans':True,'complete_write':True,'nonfinite_rejected_before_process':True,'nonzero_captured':True,'finite_timeouts_propagate':[0,-1,0.01]}
result['observations']=observations
(OUT/'standards-source-tool-inventory.json').write_text(json.dumps(tool_inventory,indent=2)+'\n')
result['commands']=commands
result['audit_sha256']=sha(Path(__file__))
result['source_tool_inventory_sha256']=sha(OUT/'standards-source-tool-inventory.json')
(OUT/'standards-identities.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result':'pass','changed_files':len(changed),'corpora':[r['aggregate'] for r in corpora],'original_corpus_reports_matched':8,'final_check_identities':checked,'whitespace':result['whitespace_exception'],'h8':{k:observations[k] for k in ['C1','C4']},'artifact':str(OUT/'standards-identities.json')},indent=2))
