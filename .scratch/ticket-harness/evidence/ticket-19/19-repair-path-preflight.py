"""Observe exact preflight callers on filesystem path representation variants."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import types

ROOT=Path('/home/ajkerr1/development/agentic_template')
EV=ROOT/'.scratch/ticket-harness/evidence'
OLD=EV/'19-evaluation-g3/snapshot'
NEW=Path('/tmp/development-review-19-c4-candidate')
def load(path,name):
    module=types.ModuleType(name)
    sys.modules[name]=module
    exec(compile(path.read_text(),str(path),'exec'),module.__dict__)
    return module

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
result={'scope':'Evaluator preflight after C3 original reports preserved; actual original/candidate caller and owner functions, temporary real Git, no production test or extra blind trial',
        'candidate_sources':{str(p.relative_to(NEW)):sha(p) for p in sorted(NEW.rglob('*')) if p.is_file()},
        'filesystem_encoding':sys.getfilesystemencoding(),'filesystem_errors':sys.getfilesystemencodeerrors(),'paths':[]}
with tempfile.TemporaryDirectory(prefix='review-19-paths-c4-') as directory:
    parent=Path(directory)
    for label,basename in [('trailing_space','repo '),('carriage_return','repo\rname'),('trailing_newline','repo\n'),('unicode','répo'),('non_utf8',os.fsdecode(b'repo-\xff'))]:
        checkout=parent/basename
        checkout.mkdir()
        commands=[]
        for args in [['git','init','--quiet','--initial-branch=main',str(checkout)],['git','-C',str(checkout),'-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','--allow-empty','-m','path observation']]:
            process=subprocess.run(args,capture_output=True,check=False)
            commands.append({'argv':args,'exit':process.returncode,'stdout_hex':process.stdout.hex(),'stderr_hex':process.stderr.hex()})
            assert process.returncode==0,commands[-1]
        base=subprocess.run(['git','-C',str(checkout),'rev-parse','HEAD'],capture_output=True,check=True).stdout.decode('ascii').removesuffix('\n')
        values={}
        for version,snapshot in [('C3',OLD),('C4_candidate',NEW)]:
            load(snapshot/'cases/b7/git_ops.py','git_ops')
            caller=load(snapshot/'cases/b7/caller.py','b7_caller_'+version+'_'+label)
            try:
                root,branch=caller.preflight(checkout,'main',base)
                values[version]={'outcome':'returned','root':str(root),'equal':root==checkout.resolve(),'branch':branch}
            except UnicodeDecodeError as error:
                values[version]={'outcome':'UnicodeDecodeError','message':str(error)}
        assert values['C4_candidate']['equal'] is True
        result['paths'].append({'kind':label,'checkout':str(checkout),'expected_root':str(checkout.resolve()),'initialization_commands':commands,'observations':values})
assert next(v for v in result['paths'] if v['kind']=='carriage_return')['observations']['C3']['equal'] is False
assert next(v for v in result['paths'] if v['kind']=='non_utf8')['observations']['C3']['outcome']=='UnicodeDecodeError'
result['audit']='The exact caller now captures bytes and explicitly os.fsdecode converts stdout/stderr into text without universal-newline translation. CompletedProcess text result, argument vectors, capture/no-shell/check=False semantics preserved. Root/ref remove only one record newline; arbitrary valid filesystem bytes round-trip through filesystem codec with surrogateescape. Other three controls and every contract/guidance/seed unchanged from audited C3.'
result['limits']='Five representative path representations, not exhaustive filesystem or Git configuration behavior. Previous all-control audit remains exact for unchanged d9/f6/h8. Source reasoning plus actual final independent reviewers still required.'
path=EV/'19-repair-path-preflight-results.json'
assert not path.exists()
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'path':str(path),'filesystem_cases':len(result['paths']),'candidate_all_roots_equal':True,'C3_CR_changed_root':True,'C3_non_UTF8_raises':True},indent=2))
