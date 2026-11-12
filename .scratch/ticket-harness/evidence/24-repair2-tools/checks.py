"""Check frozen source with retained commands, exits, logs and fixture observations."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
identity=json.loads((out/'24-repair2-final-source.json').read_text())
mode=sys.argv[1]
raw=Path('/tmp/ticket24-repair2-'+mode+'-raw');raw.mkdir(exist_ok=False)
env=dict(os.environ,PYTHONPATH=f"tests:/tmp/ticket23-tools:{out/'24-repair2-tools'}",TICKET24REPAIR2_RAW=str(raw))
commands={
 'focused':[[sys.executable,'-m','pytest','-q','tests/test_milestones.py','tests/test_qa_promotion.py','tests/test_continuation.py','tests/test_transaction.py','-p','capture24repair2']],
 'final':[
 [sys.executable,'-m','pytest','-q','--durations=20','-p','capture24repair2'],
 [sys.executable,'-m','mypy'],
 [sys.executable,'-m','ruff','check','ticket_harness','tests','examples'],
 [sys.executable,'-m','ruff','format','--check','ticket_harness','tests','examples'],
 ['git','diff','--check'],
 ['git','diff','--check',identity['baseline'],'--','ticket_harness','tests','examples'],
 ]}[mode]
results=[]
def unchanged():
 assert all(hashlib.sha256(Path(n).read_bytes()).hexdigest()==d for n,d in identity['source_hashes'].items())
for i,command in enumerate(commands):
 unchanged();start=time.time();log=out/f'24-repair2-{mode}-check-{i}.log'
 with log.open('wb') as stream:result=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
 unchanged()
 results.append(dict(command=command,exit=result.returncode,seconds=time.time()-start,log=str(log),source='24-repair2-final-source.json',environment={k:env[k] for k in ('PYTHONPATH','TICKET24REPAIR2_RAW')}))
 (out/f'24-repair2-{mode}-check-results.json').write_text(json.dumps(results,indent=2)+'\n');print(i,result.returncode,flush=True)
assert all(r['exit']==0 for r in results),results
