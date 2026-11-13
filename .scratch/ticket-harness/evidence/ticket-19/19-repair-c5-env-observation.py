from pathlib import Path
import json, os, subprocess, tempfile, types, sys
snapshot=Path('/home/ajkerr1/development/agentic_template/.scratch/ticket-harness/evidence/19-evaluation-g4/snapshot')
owner=types.ModuleType('git_ops');exec(compile((snapshot/'cases/b7/git_ops.py').read_text(),'<owner>','exec'),owner.__dict__);sys.modules['git_ops']=owner
caller=types.ModuleType('caller');exec(compile((snapshot/'cases/b7/caller.py').read_text(),'<caller>','exec'),caller.__dict__)
records=[]
with tempfile.TemporaryDirectory(prefix='review19-ambient-') as tmp:
    requested,ambient=[Path(tmp)/x for x in ['requested','ambient']]
    for path in [requested,ambient]:
        subprocess.run(['git','init','--quiet','--initial-branch=main',str(path)],check=True)
        subprocess.run(['git','-C',str(path),'-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','--allow-empty','-m','initial'],check=True)
    base=subprocess.check_output(['git','-C',str(requested),'rev-parse','HEAD'],text=True).strip()
    # Both have identical initial commits; ensure an ambient root cannot fail solely due to missing base.
    for envvars in [{'GIT_DIR':str(ambient/'.git')},{'GIT_DIR':str(ambient/'.git'),'GIT_WORK_TREE':str(ambient)},{'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'core.worktree','GIT_CONFIG_VALUE_0':str(ambient)}]:
        saved=os.environ.copy()
        try:
            os.environ.update(envvars)
            root,branch=caller.preflight(requested,'main',base)
            records.append({'environment':envvars,'requested':str(requested),'returned_root':str(root),'matches':root==requested,'branch':branch})
        except ValueError as e: records.append({'environment':envvars,'error':str(e)})
        finally: os.environ.clear();os.environ.update(saved)
Path('/tmp/repair19-c5-env-observation.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
