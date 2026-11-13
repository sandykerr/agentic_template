"""Run the six required gates on a new named source freeze; preserve halted artifacts."""
import hashlib,json,os,re,subprocess,sys,time
from pathlib import Path
phase=sys.argv[1]
if not re.fullmatch('[a-z0-9-]+',phase):raise SystemExit('Use a unique lowercase phase name')
out=Path('.scratch/ticket-harness/evidence');identity_name=f'24-repair2-{phase}-source.json';identity=json.loads((out/identity_name).read_text())
raw=Path('/tmp/ticket24-repair2-'+phase+'-raw');raw.mkdir(exist_ok=False)
env=dict(os.environ,PYTHONPATH=f"tests:/tmp/ticket23-tools:{out/'24-repair2-tools'}",TICKET24REPAIR2_RAW=str(raw))
commands=[
 [sys.executable,'-m','pytest','-q','--durations=20','-p','capture24repair2'],
 [sys.executable,'-m','mypy'],
 [sys.executable,'-m','ruff','check','ticket_harness','tests','examples'],
 [sys.executable,'-m','ruff','format','--check','ticket_harness','tests','examples'],
 ['git','diff','--check'],
 ['git','diff','--check',identity['baseline'],'--','ticket_harness','tests','examples'],
]
results=[]
for i,command in enumerate(commands):
 for n,d in identity['source_hashes'].items():assert hashlib.sha256(Path(n).read_bytes()).hexdigest()==d,n
 log=out/f'24-repair2-{phase}-check-{i}.log';start=time.time()
 with log.open('xb') as stream:r=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
 for n,d in identity['source_hashes'].items():assert hashlib.sha256(Path(n).read_bytes()).hexdigest()==d,n
 results.append(dict(command=command,exit=r.returncode,seconds=time.time()-start,log=str(log),source=identity_name,environment={k:env[k] for k in ('PYTHONPATH','TICKET24REPAIR2_RAW')}))
 (out/f'24-repair2-{phase}-check-results.json').write_text(json.dumps(results,indent=2)+'\n');print(i,r.returncode,flush=True)
assert all(r['exit']==0 for r in results),results
