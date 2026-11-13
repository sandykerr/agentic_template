"""Bounded evaluator preflight of all four controls before C3 declaration."""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import types

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT/'.scratch/ticket-harness/evidence'
OLD = EV/'19-evaluation-g2/snapshot'
NEW = Path('/tmp/development-review-19-c3-candidate')
def load(path,name):
    module=types.ModuleType(name)
    sys.modules[name]=module
    exec(compile(path.read_text(),str(path),'exec'),module.__dict__)
    return module

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
result={'scope':'Evaluator source/contract preflight before C3 declaration; no additional blinded trial or production tests',
        'guidance_version':'G2 unchanged', 'sources':{str(p.relative_to(NEW)):sha(p) for p in sorted(NEW.rglob('*')) if p.is_file()}}
with tempfile.TemporaryDirectory(prefix='review-19-control-audit-') as directory:
    parent=Path(directory)
    checkout=parent/'repo '
    checkout.mkdir()
    commands=[]
    def command(args):
        value=subprocess.run(args,text=True,capture_output=True,check=False)
        commands.append({'argv':args,'exit':value.returncode,'stdout':value.stdout,'stderr':value.stderr})
        assert value.returncode == 0,commands[-1]
        return value.stdout
    command(['git','init','--quiet','--initial-branch=main',str(checkout)])
    command(['git','-C',str(checkout),'-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','--allow-empty','-m','control observation'])
    base=command(['git','-C',str(checkout),'rev-parse','HEAD']).removesuffix('\n')
    def git(args):
        value=subprocess.run(['git','-C',str(checkout),*args],capture_output=True,text=True,check=False)
        commands.append({'argv':['git','-C',str(checkout),*args],'exit':value.returncode,'stdout':value.stdout,'stderr':value.stderr})
        return value
    roots={}
    for label,snapshot in [('C2',OLD),('C3_candidate',NEW)]:
        owner=load(snapshot/'cases/b7/git_ops.py','b7_'+label)
        root,branch=owner.validate(git,'main',base)
        roots[label]={'returned_root':str(root),'expected_root':str(checkout.resolve()),'equal':root==checkout.resolve(),'branch':branch}
    assert roots['C2']['equal'] is False and roots['C3_candidate']['equal'] is True
    result['b7']={'observations':roots,'commands':commands,
        'audit':'Checked command status remains owner policy; root/ref remove one record newline, pathname whitespace preserved; status remains raw truthiness. Detached/unexpected/dirty/missing-base/ancestry checks retained; no new path restriction.'}
    parse={}
    length=1200
    text=','.join(f'T{i}:T{i+1}' for i in range(length-1))+f',T{length-1}:'
    for label,snapshot in [('C2',OLD),('C3_candidate',NEW)]:
        owner=load(snapshot/'cases/d9/plan.py','d9_'+label)
        row={}
        try:
            value=owner.parse(text)
            row['forward_chain']={'outcome':'returned','count':len(value),'first':value[0].id,'last':value[-1].id}
        except RecursionError as error:
            row['forward_chain']={'outcome':'RecursionError','message':str(error)}
        for source in ['a:+','a:,b:a+','a:,b:a','a:b,b:a','a:missing','a:,a:']:
            try:
                value=owner.parse(source)
                row[source]={'outcome':'returned','value':[{'id':v.id,'dependencies':v.dependencies} for v in value]}
            except ValueError as error:
                row[source]={'outcome':'ValueError','message':str(error)}
        parse[label]=row
    assert parse['C2']['forward_chain']['outcome']=='RecursionError'
    assert parse['C3_candidate']['forward_chain']['count']==length
    for source in ['a:+','a:,b:a+']:
        assert parse['C2'][source]['outcome']=='returned'
        assert parse['C3_candidate'][source]['outcome']=='ValueError'
    result['d9']={'chain_nodes':length,'recursion_limit':sys.getrecursionlimit(),'observations':parse,
        'audit':'Nonempty dependency operands enforce existing grammar; whole empty RHS remains valid. Explicit DFS enter/leave stack replaces interpreter recursion, preserves output order/frozen values and local graph checks. Duplicate dependency mentions remain permitted; no graph-depth input restriction.'}
    io=load(NEW/'cases/f6/io_ops.py','f6_c3')
    destination=parent/'content.txt'
    destination.write_text('original',encoding='utf-8')
    before=set(parent.iterdir())
    try:
        io.atomic_write(destination,'\ud800')
    except UnicodeEncodeError as error:
        write_failure=type(error).__name__
    assert destination.read_text()=='original' and set(parent.iterdir())==before
    io.atomic_write(destination,'complete text')
    assert destination.read_text()=='complete text' and set(parent.iterdir())==before
    nonzero=io.invoke([sys.executable,'-c','raise SystemExit(7)'],parent,1)
    assert nonzero.returncode==7
    timeout=[]
    for value in [None,float('inf'),float('nan')]:
        try:
            io.invoke(['/nonexistent/review-control-command'],parent,value)
        except ValueError as error:
            timeout.append({'input':repr(value),'outcome':type(error).__name__,'message':str(error)})
    assert len(timeout)==3
    finite=[]
    for value in [0,-1,0.01]:
        try:
            process=io.invoke([sys.executable,'-c','import time; time.sleep(1)'],parent,value)
            finite.append({'timeout':value,'outcome':'returned','exit':process.returncode})
        except subprocess.TimeoutExpired:
            finite.append({'timeout':value,'outcome':'TimeoutExpired'})
    assert all(v['outcome']=='TimeoutExpired' for v in finite)
    result['f6']={'encoding_failure':write_failure,'old_content_survived':True,'temporary_cleanup':True,'complete_replacement':True,'nonzero_exit':nonzero.returncode,'invalid_timeouts':timeout,'finite_timeouts':finite,
        'audit':'C3 enforces finite timeout before child creation without positive-only policy. argv/cwd/capture/check=False/TimeoutExpired unchanged. Same-directory temporary closes before replace; ordinary encoding failure cleans temporary and preserves old destination. Existing directory is explicit precondition; no fsync/metadata/concurrency/crash durability or impossible successful unlink under OS refusal asserted.'}
    owner=load(NEW/'cases/h8/attempt.py','h8_c3')
    identity,revision={'id':['A']},{'rev':['r1']}
    attempt=owner.Attempt(identity)
    before=deepcopy(attempt.snapshot())
    try:
        attempt.complete()
    except ValueError:
        pass
    assert attempt.snapshot()==before
    try:
        attempt.submit({})
    except ValueError:
        pass
    assert attempt.snapshot()==before
    attempt.submit(revision)
    attempt.complete()
    before=deepcopy(attempt.snapshot())
    identity['id'].append('external')
    revision['rev'].append('external')
    a,b=attempt.snapshot()
    a['id']['id'].append('observation')
    b['revision']['rev'].append('observation')
    assert attempt.snapshot()==before
    result['h8']={'premature_completion_unchanged':True,'empty_submission_unchanged':True,'nested_input_and_snapshot_isolation':True,'audit':'Unchanged corrected h8 deep-copies inputs/proposed transition pair/outputs. One owner and guard-before-mutation; dictionary/list aliases isolated without scalar restriction. No persistence/concurrency; no arbitrary malicious copy protocol behavior assessed.'}
path=EV/'19-repair-control-preflight-results.json'
assert not path.exists()
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'preflight':str(path),'candidate_files':len(result['sources']),'b7_whitespace_fixed':True,'d9_chain_nodes':length,'d9_empty_operands_reject':True,'f6_finite_timeout_guard':True,'h8_isolated':True},indent=2))
