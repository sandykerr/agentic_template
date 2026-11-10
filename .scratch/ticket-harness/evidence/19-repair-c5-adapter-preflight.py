"""Evaluator exact-caller routing/read-only audit; no production tests or harness."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys, tempfile, types
ROOT=Path('/home/ajkerr1/development/agentic_template')
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g4/snapshot'
NEW=Path('/tmp/development-review-19-c5-candidate')
OUT=EV/'19-repair-c5-adapter-preflight-results.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(snapshot,label):
    m=types.ModuleType('git_ops');exec(compile((snapshot/'cases/b7/git_ops.py').read_text(),str(snapshot/'cases/b7/git_ops.py'),'exec'),m.__dict__);sys.modules['git_ops']=m
    c=types.ModuleType('caller_'+label);exec(compile((snapshot/'cases/b7/caller.py').read_text(),str(snapshot/'cases/b7/caller.py'),'exec'),c.__dict__);return c
callers={label:load(snapshot,label) for label,snapshot in [('C4',OLD),('C5_candidate',NEW)]}
commands=[];rows=[]
with tempfile.TemporaryDirectory(prefix='review19-c5-adapter-') as tmp:
    parent=Path(tmp)
    def git(path,*args):
        p=subprocess.run(['git','-C',str(path),*args],capture_output=True,check=False)
        commands.append({'argv':p.args,'exit':p.returncode,'stdout':os.fsdecode(p.stdout),'stderr':os.fsdecode(p.stderr)})
        assert p.returncode==0,commands[-1]
        return os.fsdecode(p.stdout).removesuffix('\n')
    def init(name,branch='main'):
        path=parent/name;path.mkdir();git(path,'init','--quiet','--initial-branch='+branch)
        (path/'tracked').write_text('original\n');git(path,'add','tracked');git(path,'-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','-m','initial');return path
    requested=init('requested');foreign=init('foreign','foreign')
    base=git(requested,'rev-parse','HEAD')
    # Foreign repo also contains requested's base so wrong-root acceptance remains possible.
    git(foreign,'fetch','--quiet',str(requested),'main');git(foreign,'branch','main','FETCH_HEAD')
    def observe(label,environment,accepted=True,checkout=requested,expected='main'):
        saved=os.environ.copy();values={}
        try:
            os.environ.update(environment)
            for version,caller in callers.items():
                try:
                    root,branch=caller.preflight(checkout,expected,base)
                    values[version]={'outcome':'returned','root':str(root),'branch':branch,'exact_root':root==checkout.resolve()}
                except ValueError as e:values[version]={'outcome':'ValueError','message':str(e)}
        finally:os.environ.clear();os.environ.update(saved)
        candidate=values['C5_candidate']
        assert (candidate['outcome']=='returned')==accepted,(label,values)
        if accepted:assert candidate['exact_root'] and candidate['branch']==expected,(label,values)
        rows.append({'case':label,'environment':environment,'expected_accept':accepted,'expected_branch':expected,'requested':str(checkout),'outcomes':values})
    observe('foreign-git-dir',{'GIT_DIR':str(foreign/'.git')})
    assert rows[-1]['outcomes']['C4']['outcome']=='ValueError'
    git(foreign,'checkout','--quiet','main')
    observe('foreign-dir-and-worktree',{'GIT_DIR':str(foreign/'.git'),'GIT_WORK_TREE':str(foreign)})
    assert not rows[-1]['outcomes']['C4']['exact_root']
    (requested/'tracked').write_text('dirty requested checkout\n')
    observe('foreign-clean-cannot-hide-requested-dirty',{'GIT_DIR':str(foreign/'.git'),'GIT_WORK_TREE':str(foreign)},accepted=False)
    assert rows[-1]['outcomes']['C4']['outcome']=='returned'
    (requested/'tracked').write_text('original\n')
    (foreign/'other').write_text('foreign tracked file\n');git(foreign,'add','other')
    observe('foreign-index',{'GIT_INDEX_FILE':str(foreign/'.git/index')})
    assert rows[-1]['outcomes']['C4']['outcome']=='ValueError'
    observe('foreign-common-dir',{'GIT_COMMON_DIR':str(foreign/'.git')})
    observe('absent-object-dir',{'GIT_OBJECT_DIRECTORY':str(parent/'absent-objects')})
    observe('absent-index',{'GIT_INDEX_FILE':str(parent/'absent-index')})
    observe('invalid-config-count',{'GIT_CONFIG_COUNT':'invalid'})
    observe('environment-config-worktree',{'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'core.worktree','GIT_CONFIG_VALUE_0':str(foreign)})
    linked=parent/'linked';git(requested,'worktree','add','--quiet','-b','linked',str(linked))
    observe('linked-worktree',{},checkout=linked,expected='linked')
    observe('linked-with-foreign-routing',{'GIT_DIR':str(foreign/'.git'),'GIT_WORK_TREE':str(foreign),'GIT_COMMON_DIR':str(foreign/'.git'),'GIT_INDEX_FILE':str(foreign/'.git/index')},checkout=linked,expected='linked')
    read_only=[]
    for version,caller in callers.items():
        tracked=requested/'tracked';stat=tracked.stat();os.utime(tracked,ns=(stat.st_atime_ns,stat.st_mtime_ns+1000000000))
        before={str(p.relative_to(requested/'.git')):sha(p) for p in (requested/'.git').rglob('*') if p.is_file()}
        root,branch=caller.preflight(requested,'main',base)
        after={str(p.relative_to(requested/'.git')):sha(p) for p in (requested/'.git').rglob('*') if p.is_file()}
        changed=sorted(k for k in set(before)|set(after) if before.get(k)!=after.get(k))
        read_only.append({'version':version,'returned_root':str(root),'branch':branch,'before_git_files':before,'after_git_files':after,'changed_files':changed})
    assert read_only[0]['changed_files']==['index'],read_only
    assert read_only[1]['changed_files']==[],read_only
    local_env=git(requested,'rev-parse','--local-env-vars').splitlines()
result={'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Bounded evaluator actual Git/caller audit before declaration, no additional blind trial, production test or harness run','guidance_version':'G2 unchanged','old_sources':{str(p.relative_to(OLD)):sha(p) for p in sorted(OLD.rglob('*')) if p.is_file()},'candidate_sources':{str(p.relative_to(NEW)):sha(p) for p in sorted(NEW.rglob('*')) if p.is_file()},'observations':rows,'read_only_observations':read_only,'setup_commands':commands,'installed_git_local_env_vars':local_env,'primary_source':'https://git-scm.com/docs/githooks#_description','audit':'Git documents clearing rev-parse --local-env-vars when operating in a foreign repository. Candidate removes exactly installed Git local environment names from a copied env and disables optional locks for all requested-checkout commands. It preserves byte capture and filesystem decoding. Repository policies remain in validate. Environment/path/read-only cases are finite observed examples, not exhaustive platform or malicious-environment guarantees.'}
assert not OUT.exists();OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result':'pass','result_path':str(OUT),'routing_cases':len(rows),'read_only_comparisons':len(read_only)},indent=2))
