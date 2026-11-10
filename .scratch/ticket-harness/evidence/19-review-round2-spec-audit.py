from pathlib import Path
from copy import deepcopy
import ast, datetime, hashlib, json, os, re, subprocess, sys, tempfile, types
ROOT=Path('/home/ajkerr1/development/agentic_template')
OUT=Path('/tmp/ticket19-review2')
BASE='f2929e79cfd5a68f670862775053ae85ba9582b5'
SOURCE='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93'
EV='.scratch/ticket-harness/evidence/'
commands=[]
def run(args,**kwargs):
    p=subprocess.run(args,cwd=ROOT,capture_output=True,**kwargs)
    commands.append({'argv':args,'exit':p.returncode,'stdout':os.fsdecode(p.stdout),'stderr':os.fsdecode(p.stderr)})
    return p
def blob(path,rev=SOURCE):
    p=run(['git','show',rev+':'+path]); assert p.returncode==0
    return p.stdout
def sha(data): return hashlib.sha256(data).hexdigest()
def load(path,name):
    m=types.ModuleType(name);sys.modules[name]=m
    exec(compile(blob(path),path,'exec'),m.__dict__);return m
identity={}
for args in [['git','rev-parse','HEAD'],['git','status','--porcelain'],['git','merge-base',BASE,SOURCE],['git','log',BASE+'..'+SOURCE,'--oneline'],['git','diff','--stat',BASE+'...'+SOURCE]]:run(args)
assert commands[0]['stdout'].strip()==SOURCE and commands[1]['stdout']=='' and commands[2]['stdout'].strip()==BASE
paths=run(['git','diff','--name-only',BASE+'...'+SOURCE]).stdout.decode().splitlines()
for path in paths:identity[path]=sha(blob(path))
assert not any(p.startswith(('ticket_harness/','tests/')) or p in ['pyproject.toml','environment.yml'] for p in paths)
corpora={}; previous=None
for stage,label in [('19-evaluation','C1_G1'),('19-evaluation-g2','C2_G2'),('19-evaluation-g3','C3_G2'),('19-evaluation-g4','C4_G2')]:
    prefix=EV+stage+'/'
    manifest=json.loads(blob(prefix+'source-manifest.json'))
    assert len(manifest)==36
    aggregate=sha(json.dumps(manifest,sort_keys=True).encode())
    assert aggregate==blob(prefix+'corpus-identity.txt').decode().strip()
    for path,digest in manifest.items():assert sha(blob(prefix+'snapshot/'+path))==digest
    capture=json.loads(blob(prefix+'declaration-capture.json'))
    assert sha(blob(prefix+'declaration.md'))==capture['declaration_sha256']
    assert sha(blob(prefix+'source-manifest.json'))==capture['source_manifest_sha256']
    review_capture=json.loads(blob(prefix+'review-capture.json'))
    for path,digest in review_capture['sha256'].items():assert sha(blob(prefix+path))==digest
    assignments=json.loads(blob(prefix+'assignments.json'))['assignments']
    corpora[label]={'aggregate':aggregate,'count':len(manifest),'delta_from_previous':[] if previous is None else [p for p in manifest if previous[p]!=manifest[p]],'declaration':capture,'assignments':assignments}
    previous=manifest
    if stage!='19-evaluation':
        for row in assignments:
            assert row['settings']=={'fork_turns':'none','model':'gpt-6.1-sol','reasoning_effort':'high'}
            assert capture['declared_at_utc']<row['timestamp']
            for key,digest in [('dispatch_path','dispatch_sha256'),('known_readable_prompt_path','known_readable_prompt_sha256')]:assert sha(blob(prefix+row[key]))==row[digest]
for label in ['c2','c3']:
    stage='19-evaluation-g'+label[-1]
    preservation=json.loads(blob(EV+'19-repair-'+label+'-preservation.json'))['sha256']
    for path,digest in preservation.items():assert sha(blob(EV+stage+'/'+path))==digest
oldpaths=run(['git','ls-tree','-r','--name-only','e90abb64ab95c5b15cdb0949b03c6a948365339b']).stdout.decode().splitlines()
modified_original=[]
for p in oldpaths:
    if sha(blob(p,'e90abb64ab95c5b15cdb0949b03c6a948365339b'))!=sha(blob(p)):
        modified_original.append(p)
assert modified_original==['docs/agents/ownership-review.md','docs/agents/reviewer-evaluation.md']
# Raw tool audit extracts actual configured turns and every tool input for inspection.
tools_audit={}
for stage in ['19-evaluation','19-evaluation-g2','19-evaluation-g3','19-evaluation-g4']:
    pfx=EV+stage+'/'
    names=run(['git','ls-tree','-r','--name-only',SOURCE,'--',pfx]).stdout.decode().splitlines()
    selected={}
    for name in names:
        if name.endswith('-source-records.json'):
            rows=json.loads(blob(name)); inputs=[];settings=[];messages=[]
            for row in rows:
                p=row.get('payload',{})
                if row.get('type')=='observed_turn_settings':settings.append(row)
                if p.get('type') in ['function_call','custom_tool_call']:inputs.append({'timestamp':row.get('timestamp'),'name':p.get('name'),'input':p.get('input',p.get('arguments'))})
                if p.get('type')=='agent_message':messages.append({'author':p.get('author'),'recipient':p.get('recipient'),'timestamp':row.get('timestamp')})
            selected[name]={'settings':settings,'tool_inputs':inputs,'received_message_routes':messages}
    tools_audit[stage]=selected
(OUT/'spec-tool-audit.json').write_text(json.dumps(tools_audit,indent=2)+'\n')
# Exact fixture code is compiled from git objects; no imports/bytecode touch repository.
fixture=EV+'19-evaluation-g4/snapshot/cases/'
observations={}
h8=load(fixture+'h8/attempt.py','audit_h8')
i={'id':['A',{'nested':[1]}]};r={'revision':['R',{'nested':[2]}]};a=h8.Attempt(i)
initial=deepcopy(a.snapshot());i['id'][1]['nested'].append(3);assert a.snapshot()==initial
checks=[]
def rejected(op):
    before=deepcopy(a.snapshot())
    try:op()
    except ValueError:pass
    else:raise AssertionError('accepted invalid operation')
    assert a.snapshot()==before
    checks.append(True)
rejected(a.complete);rejected(lambda:a.submit({}));a.submit(r)
submitted=deepcopy(a.snapshot());r['revision'][1]['nested'].append(3);assert a.snapshot()==submitted
rejected(lambda:a.submit({'new':1}))
x,y=a.snapshot();x['id']['id'][1]['nested'].append(7);y['revision']['revision'][1]['nested'].append(8);assert a.snapshot()==submitted
a.complete();completed=deepcopy(a.snapshot());assert completed[0]==completed[1] and completed[0]['status']=='completed'
rejected(a.complete);rejected(lambda:a.submit('later'))
observations['h8']={'source':sha(blob(fixture+'h8/attempt.py')),'dictionary_and_list_input_isolation':True,'nested_snapshot_isolation_both_views':True,'mirrors_equal_each_phase':initial[0]==initial[1] and submitted[0]==submitted[1] and completed[0]==completed[1],'invalid_operations_unchanged':len(checks)}
d9=load(fixture+'d9/plan.py','audit_d9');n=2000
chain=','.join(f'T{x}:T{x+1}' for x in range(n-1))+f',T{n-1}:';assert len(d9.parse(chain))==n
bad=['a:+','a:b+,b:','a:missing','a:b,b:a','a:,a:']
for value in bad:
    try:d9.parse(value)
    except ValueError:pass
    else:raise AssertionError(value)
v=d9.parse(' a : b+c+b , b : c , c : ');assert tuple(x.id for x in v)==('a','b','c') and v[0].dependencies==('b','c','b')
observations['d9']={'long_chain':n,'reject_inputs':bad,'shared_and_repeated_dependencies_ordered':True}
f6=load(fixture+'f6/io_ops.py','audit_f6')
with tempfile.TemporaryDirectory(dir=OUT,prefix='spec-io-') as td:
    p=Path(td);f=p/'destination';f.write_text('old');before=set(p.iterdir())
    try:f6.atomic_write(f,'\ud800')
    except UnicodeEncodeError:pass
    else:raise AssertionError('encoding accepted')
    assert f.read_text()=='old' and set(p.iterdir())==before
    f6.atomic_write(f,'new');assert f.read_text()=='new' and set(p.iterdir())==before
    for timeout in [None,float('inf'),float('nan')]:
        try:f6.invoke(['/not-a-real-command'],p,timeout)
        except ValueError:pass
        else:raise AssertionError('bad timeout accepted')
    assert f6.invoke([sys.executable,'-c','raise SystemExit(7)'],p,1).returncode==7
    try:f6.invoke([sys.executable,'-c','import time;time.sleep(2)'],p,.01)
    except subprocess.TimeoutExpired:pass
    else:raise AssertionError('no timeout')
observations['f6']={'encoding_failure_preserves_old_content_and_cleans_temp':True,'complete_replace':True,'nonfinite_guard_before_launch':True,'nonzero_exit_returned':7,'TimeoutExpired_propagates':True}
load(fixture+'b7/git_ops.py','git_ops');caller=load(fixture+'b7/caller.py','audit_b7')
with tempfile.TemporaryDirectory(dir=OUT,prefix='spec-git-') as td:
    rows=[]
    for kind,name in [('space','repo '),('CR','repo\rname'),('LF','repo\n'),('nonutf8',os.fsdecode(b'repo\xff'))]:
        p=Path(td)/name;p.mkdir()
        for argv in [['git','init','-q','-b','main',os.fspath(p)],['git','-C',os.fspath(p),'-c','user.name=Spec audit','-c','user.email=spec@example.invalid','commit','-q','--allow-empty','-m','initial']]:assert run(argv).returncode==0
        base=run(['git','-C',os.fspath(p),'rev-parse','HEAD']).stdout.decode().strip()
        root,branch=caller.preflight(p,'main',base);assert root==p.resolve() and branch=='main'
        rows.append({'kind':kind,'root_equal':True})
        for expected,b in [('other',base),('main','missing-base')]:
            try:caller.preflight(p,expected,b)
            except ValueError:pass
            else:raise AssertionError('bad preflight accepted')
    # Ordinary branch/tag name ambiguity is an exploratory accepted-state observation.
    assert run(['git','-C',os.fspath(p),'tag','main']).returncode==0
    try: result=caller.preflight(p,'main',base);ambiguity={'outcome':'returned','branch':result[1]}
    except ValueError as error:ambiguity={'outcome':'ValueError','message':str(error),'symbolic_ref':os.fsdecode(run(['git','-C',os.fspath(p),'symbolic-ref','--short','HEAD']).stdout)}
observations['b7']={'paths':rows,'wrong_branch_and_missing_base_reject':True,'branch_tag_same_name':ambiguity}
ws=EV+'19-evaluation-g3/spec-c3-reviewer-saved.md'
for args in [['git','diff','--check',BASE+'...'+SOURCE],['git','diff','--check',BASE+'...'+SOURCE,'--','.',':(exclude)'+ws],['git','-c','core.whitespace=-blank-at-eof','diff','--check',BASE+'...'+SOURCE,'--',ws]]:run(args)
frozen=blob(ws);assert len(frozen)-len(frozen.rstrip(b'\n'))==2
observations['whitespace']={'path':ws,'sha256':sha(frozen),'trailing_LF':2,'last_three_checks':commands[-4:-1] if False else [c for c in commands if '--check' in c['argv']]}
(OUT/'spec-observations.json').write_text(json.dumps(observations,indent=2)+'\n')
instructions=['AGENTS.md','GLOSSARY.md','docs/agents/domain.md','docs/agents/issue-tracker.md','docs/agents/python-environment.md','docs/agents/testing.md','docs/agents/ownership-review.md','docs/agents/review-records.md','docs/agents/architecture-checkpoints.md','docs/templates/reviews/report.md','docs/adr/0001-reusable-harness-and-local-integration.md','docs/adr/0002-human-qa-gates-feature-promotion.md','.scratch/ticket-harness/spec.md','.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md','.agents/skills/custom/test-strategy/SKILL.md','.agents/skills/matt-pocock/code-review/SKILL.md']
for path in instructions:identity[path]=sha(blob(path))
external={str(p):sha(p.read_bytes()) for p in [OUT/'spec-assignment.txt',OUT/'common.txt',OUT/'spec-audit.py',OUT/'spec-observations.json',OUT/'spec-tool-audit.json']}
report={'review':'review-ticket-19','report':'spec-02','baseline':BASE,'source':SOURCE,'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'settings':{'requested_model':'gpt-6.1-sol','reasoning':'high','fresh_fork':'none','context_target_advisory':250000,'backend_enforcement_usage_telemetry':'unavailable'},'instruction_paths':instructions,'source_identities':identity,'external_identities':external,'corpora':corpora,'modified_rejected_paths':modified_original,'commands':commands,'limits':'Mechanical identity and observed examples do not establish judgment; report supplies substantive source assessment. No runtime suite, result-writing helper, package/private-module test or sibling current-round report used.'}
(OUT/'spec-identities.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'audit':'completed','observations':observations,'identities':str(OUT/'spec-identities.json')},indent=2))
