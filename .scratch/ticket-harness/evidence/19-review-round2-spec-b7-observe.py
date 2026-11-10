from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,types
ROOT=Path('/home/ajkerr1/development/agentic_template');OUT=Path('/tmp/ticket19-review2')
REV='ce4e57d77be6dfd695f0ecb15284c5e9d5792b93';PFX='.scratch/ticket-harness/evidence/19-evaluation-g4/snapshot/cases/b7/'
commands=[]
def run(argv):
    r=subprocess.run(argv,capture_output=True,cwd=ROOT)
    commands.append({'argv':argv,'exit':r.returncode,'stdout':os.fsdecode(r.stdout),'stderr':os.fsdecode(r.stderr)})
    assert r.returncode==0,commands[-1]
    return r.stdout
def source(name):return run(['git','show',REV+':'+PFX+name])
source_bytes={name:source(name) for name in ['git_ops.py','caller.py','CONTRACT.md']}
for name in ['git_ops','caller']:
    m=types.ModuleType(name);sys.modules[name]=m;exec(compile(source_bytes[name+'.py'],PFX+name+'.py','exec'),m.__dict__)
with tempfile.TemporaryDirectory(prefix='spec-b7-tag-',dir=OUT) as td:
    repo=Path(td)/'repo';run(['git','init','--quiet','--initial-branch=main',str(repo)])
    run(['git','-C',str(repo),'-c','user.name=Spec reviewer','-c','user.email=spec@example.invalid','commit','--quiet','--allow-empty','-m','observation'])
    base=run(['git','-C',str(repo),'rev-parse','HEAD']).decode().strip()
    before=sys.modules['caller'].preflight(repo,'main',base)
    run(['git','-C',str(repo),'tag','main'])
    status=run(['git','-C',str(repo),'status','--porcelain','--untracked-files=all']).decode()
    full_ref=run(['git','-C',str(repo),'symbolic-ref','HEAD']).decode()
    short_ref=run(['git','-C',str(repo),'symbolic-ref','--short','HEAD']).decode()
    actual_branch=run(['git','-C',str(repo),'branch','--show-current']).decode()
    run(['git','-C',str(repo),'rev-parse','--verify',base+'^{commit}'])
    run(['git','-C',str(repo),'merge-base','--is-ancestor',base,'HEAD'])
    try:sys.modules['caller'].preflight(repo,'main',base)
    except ValueError as e:after={'outcome':'ValueError','message':str(e)}
    else:raise AssertionError('counterexample did not reproduce')
    assert status=='' and full_ref=='refs/heads/main\n' and short_ref=='heads/main\n' and actual_branch=='main\n'
    result={'source':REV,'source_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in source_bytes.items()},'before_tag':{'root_equal':before[0]==repo.resolve(),'branch':before[1]},'after_tag':after,'worktree_status':status,'full_HEAD':full_ref,'short_HEAD':short_ref,'actual_branch':actual_branch,'base':base,'commands':commands,'scope':'One exact-source disposable Git counterexample; source compiled from committed Git blobs; no repository mutation or production tests.'}
(OUT/'spec-b7-observation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='commands'},indent=2))
