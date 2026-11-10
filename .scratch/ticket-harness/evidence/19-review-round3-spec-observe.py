from pathlib import Path
from copy import deepcopy
import hashlib,json,os,subprocess,sys,tempfile,types
R=Path('/home/ajkerr1/development/agentic_template'); O=Path('/tmp/ticket19-review3');S='8e2c82679a2314e31ebff69accab3743f55f996d';P='.scratch/ticket-harness/evidence/'
def blob(name): return subprocess.check_output(['git','show',S+':'+P+name],cwd=R)
def load(name,label):
    data=blob(name);m=types.ModuleType(label);sys.modules[label]=m;exec(compile(data,name,'exec'),m.__dict__);return m,hashlib.sha256(data).hexdigest()
results={'source':S,'sources':{},'h8':[],'b7':[]}
for stage in ['19-evaluation','19-evaluation-g5']:
    m,d=load(stage+'/snapshot/cases/h8/attempt.py','attempt_'+stage.replace('-','_'));results['sources'][stage+'/h8']=d
    identity={'nested':[{'id':'A'}]};revision={'nested':[{'r':'r1'}]};a=m.Attempt(identity);before=deepcopy(a.snapshot());identity['nested'][0]['id']='mutated';ingress=a.snapshot()==before
    invalid=[]
    if stage.endswith('g5'):
        for op in [a.complete,lambda:a.submit({})]:
            before=deepcopy(a.snapshot())
            try:op()
            except ValueError:invalid.append(a.snapshot()==before)
            else:raise AssertionError('accepted invalid')
    a.submit(revision);before=deepcopy(a.snapshot());revision['nested'][0]['r']='mutated';rev=a.snapshot()==before
    a.complete();before=deepcopy(a.snapshot());returned=a.snapshot();returned[0]['id']['nested'].append('x');returned[1]['revision']['nested'].append('y');egress=a.snapshot()==before
    if stage.endswith('g5'):
        for op in [lambda:a.submit('new'),a.complete]:
            before=deepcopy(a.snapshot())
            try:op()
            except ValueError:invalid.append(a.snapshot()==before)
            else:raise AssertionError('accepted invalid')
        assert ingress and rev and egress and all(invalid)
    else:assert not ingress and not rev and not egress
    results['h8'].append({'stage':stage,'identity_isolated':ingress,'revision_isolated':rev,'snapshot_isolated':egress,'invalid_guards_unchanged':invalid})
callers={}
for stage in ['19-evaluation-g4','19-evaluation-g5']:
    owner,d=load(stage+'/snapshot/cases/b7/git_ops.py','git_ops');results['sources'][stage+'/b7-owner']=d
    caller,d=load(stage+'/snapshot/cases/b7/caller.py','caller_'+stage.replace('-','_'));results['sources'][stage+'/b7-caller']=d;callers[stage]=caller
with tempfile.TemporaryDirectory(prefix='spec19-r3-',dir=O) as tmp:
    root=Path(tmp)
    def git(repo,*args):
        r=subprocess.run(['git','-C',os.fspath(repo),*args],capture_output=True);assert r.returncode==0,(r.args,r.stderr);return os.fsdecode(r.stdout).removesuffix('\n')
    def init(name):
        repo=root/name;repo.mkdir();git(repo,'init','-q','--initial-branch=main');(repo/'tracked').write_text('same\n');git(repo,'add','tracked');git(repo,'-c','user.name=Audit','-c','user.email=audit@example.invalid','commit','-qm','initial');return repo,git(repo,'rev-parse','HEAD')
    requested,base=init('requested\rwith-newline\n-and-space ')
    git(requested,'tag','main');git(requested,'update-ref','refs/remotes/main',base)
    assert git(requested,'symbolic-ref','HEAD')=='refs/heads/main';assert git(requested,'symbolic-ref','--short','HEAD')=='heads/main';assert git(requested,'status','--porcelain')==''
    for stage,caller in callers.items():
        try:r,b=caller.preflight(requested,'main',base);out={'returned_root':os.fspath(r),'branch':b,'exact':r==requested.resolve()}
        except ValueError as e:out={'ValueError':str(e)}
        results['b7'].append({'stage':stage,'case':'branch-tag-remote-collision-and-path','outcome':out})
    assert 'ValueError' in results['b7'][0]['outcome'];assert results['b7'][1]['outcome']['exact']
    foreign,foreignbase=init('foreign');env=os.environ.copy();os.environ.update({'GIT_DIR':str(foreign/'.git'),'GIT_WORK_TREE':str(foreign)})
    try:r,b=callers['19-evaluation-g5'].preflight(requested,'main',base);assert r==requested.resolve();results['b7'].append({'case':'ambient-foreign-routing','exact_requested_root':True,'branch':b})
    finally:os.environ.clear();os.environ.update(env)
    tracked=requested/'tracked';st=tracked.stat();os.utime(tracked,ns=(st.st_atime_ns,st.st_mtime_ns+1000000000))
    def hashes():return {str(p.relative_to(requested/'.git')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (requested/'.git').rglob('*') if p.is_file()}
    before=hashes();callers['19-evaluation-g5'].preflight(requested,'main',base);after=hashes();assert before==after;results['b7'].append({'case':'read-only-after-stat-change','changed_git_files':[]})
    (requested/'tracked').write_text('dirty\n')
    try:callers['19-evaluation-g5'].preflight(requested,'main',base)
    except ValueError as e:results['b7'].append({'case':'dirty-rejection','ValueError':str(e)})
    else:raise AssertionError('dirty accepted')
results['limits']='Exact committed miniature source only; bounded ordinary Python/Git behavior, no production module tests or malicious Git/copy protocol/platform proof.'
(O/'spec-observations.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
