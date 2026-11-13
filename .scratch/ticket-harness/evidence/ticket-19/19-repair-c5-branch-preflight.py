"""Bounded evaluator b7 contract audit; standalone miniature source, no runtime tests."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys, tempfile, types
ROOT=Path('/home/ajkerr1/development/agentic_template')
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g4/snapshot'
NEW=Path('/tmp/development-review-19-c5-candidate')
OUT=EV/'19-repair-c5-branch-preflight-results.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(snapshot,label):
    owner=types.ModuleType('git_ops')
    exec(compile((snapshot/'cases/b7/git_ops.py').read_text(),str(snapshot/'cases/b7/git_ops.py'),'exec'),owner.__dict__)
    sys.modules['git_ops']=owner
    caller=types.ModuleType('b7_'+label)
    exec(compile((snapshot/'cases/b7/caller.py').read_text(),str(snapshot/'cases/b7/caller.py'),'exec'),caller.__dict__)
    return owner,caller
versions={label:load(snapshot,label) for label,snapshot in [('C4',OLD),('C5_candidate',NEW)]}
rows=[]
with tempfile.TemporaryDirectory(prefix='review19-c5-b7-') as directory:
    parent=Path(directory)
    def observe(label, branch='main', collision=False, setup=None, expected='main', accepted=True, pathname='repo'):
        checkout=parent/(str(len(rows))+'-'+pathname)
        commands=[]
        def git(*args,ok=True):
            p=subprocess.run(['git','-C',os.fspath(checkout),*args],capture_output=True,check=False)
            commands.append({'argv':p.args,'exit':p.returncode,'stdout':os.fsdecode(p.stdout),'stderr':os.fsdecode(p.stderr)})
            if ok: assert p.returncode==0, commands[-1]
            return os.fsdecode(p.stdout).removesuffix('\n')
        checkout.mkdir()
        git('init','--quiet','--initial-branch='+branch)
        (checkout/'tracked').write_text('original\n')
        git('add','tracked')
        git('-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','-m','initial')
        base=git('rev-parse','HEAD')
        if collision:
            git('tag',branch)
            git('update-ref','refs/remotes/'+branch,base)
        if setup: base=setup(checkout,git,base)
        short=git('symbolic-ref','--short','HEAD',ok=False)
        full=git('symbolic-ref','HEAD',ok=False)
        outcomes={}
        for version,(_,caller) in versions.items():
            try:
                root,found=caller.preflight(checkout,expected,base)
                outcomes[version]={'outcome':'returned','root':os.fspath(root),'branch':found,'exact_root':root==checkout.resolve()}
            except ValueError as e:
                outcomes[version]={'outcome':'ValueError','message':str(e)}
        new=outcomes['C5_candidate']
        assert (new['outcome']=='returned') == accepted,(label,outcomes)
        if accepted: assert new['exact_root'] and new['branch']==expected,(label,new)
        rows.append({'case':label,'expected_accept':accepted,'expected_branch':expected,'base':base,'short_symbolic_ref':short,'full_symbolic_ref':full,'outcomes':outcomes,'setup_commands':commands})
    observe('ordinary-clean')
    observe('branch-tag-remote-same-name',collision=True)
    assert rows[-1]['outcomes']['C4']['outcome']=='ValueError'
    for branch in ['heads/main','tags/main','feature/nested','unicodé/枝']:
        observe('namespace-shaped-'+branch,branch=branch,collision=True,expected=branch)
    for path in ['trailing-space ','carriage\rreturn','trailing-newline\n','unicodé-枝','nonutf8-\udcff']:
        observe('path-'+repr(path),collision=True,pathname=path)
    observe('unexpected-branch',expected='other',accepted=False)
    def detached(checkout,git,base): git('checkout','--quiet','--detach',base); return base
    observe('detached-HEAD',setup=detached,accepted=False)
    def nonlocal_head(checkout,git,base): git('tag','outside'); git('symbolic-ref','HEAD','refs/tags/outside'); return base
    observe('nonlocal-symbolic-HEAD',setup=nonlocal_head,expected='outside',accepted=False)
    def dirty(checkout,git,base): (checkout/'tracked').write_text('changed\n'); return base
    observe('tracked-dirty',setup=dirty,accepted=False)
    def untracked(checkout,git,base): (checkout/'untracked').write_text('new\n'); return base
    observe('untracked-dirty',setup=untracked,accepted=False)
    def staged(checkout,git,base): (checkout/'tracked').write_text('changed\n'); git('add','tracked'); return base
    observe('staged-dirty',setup=staged,accepted=False)
    observe('missing-base',setup=lambda c,g,b:'absent-revision',accepted=False)
    def nonancestor(checkout,git,base): return git('-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit-tree',git('rev-parse','HEAD^{tree}'),'-m','unrelated')
    observe('nonancestor-base',setup=nonancestor,accepted=False)
    def ancestor(checkout,git,base): git('-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','--allow-empty','-m','next'); return base
    observe('ancestor-base',setup=ancestor,collision=True)
    def tagbase(checkout,git,base): git('tag','base-tag'); return 'base-tag'
    observe('tag-base',setup=tagbase)
    # Each Git failure is rejected by the sole owner, with argument-list/text adapter.
    _,caller=versions['C5_candidate']
    failing=[]
    owner=versions['C5_candidate'][0]
    values={('rev-parse','--show-toplevel'):str(parent)+'\n',('symbolic-ref','HEAD'):'refs/heads/main\n',('status','--porcelain','--untracked-files=all'):'',('rev-parse','--verify','base^{commit}'):'a'*40+'\n',('merge-base','--is-ancestor','base','HEAD'):''}
    for failed in values:
        calls=[]
        def fake(args):
            calls.append(args)
            return subprocess.CompletedProcess(args,1 if tuple(args)==failed else 0,values[tuple(args)],'failed' if tuple(args)==failed else '')
        try: owner.validate(fake,'main','base')
        except ValueError as e: failing.append({'failed_argv':list(failed),'calls':calls,'outcome':'ValueError','message':str(e)})
        else: raise AssertionError(failed)
result={'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Bounded evaluator Git namespace/policy/path audit, not reviewer judgment, exhaustive Git/platform guarantee, production test or harness run','guidance_version':'G2 unchanged','old_sources':{str(p.relative_to(OLD)):sha(p) for p in sorted(OLD.rglob('*')) if p.is_file()},'candidate_sources':{str(p.relative_to(NEW)):sha(p) for p in sorted(NEW.rglob('*')) if p.is_file()},'observations':rows,'owner_git_failure_cases':failing,'audit':'Full symbolic HEAD validates the local-branch namespace before returning the exact branch suffix; tags/remotes cannot change identity. Caller and all failure/dirty/base/ancestry/path policies remain unchanged. Representative branches, allowed filesystem paths and each decision are observed; no narrower accepted-input contract introduced.'}
assert not OUT.exists()
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result_path':str(OUT),'real_git_cases':len(rows),'git_failure_cases':len(failing),'result':'pass'},indent=2))
