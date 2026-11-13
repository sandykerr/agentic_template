"""Capture a bounded public-seam diagnosis/repair check on frozen bytes."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
phase=sys.argv[1];out=Path('.scratch/ticket-harness/evidence');identity=out/f'24-repair2-{phase}-source.json'
assert not identity.exists()
subprocess.run([sys.executable,str(out/'24-repair2-tools/identity.py'),phase],check=True)
frozen=json.loads(identity.read_text());raw=Path('/tmp/ticket24-repair2-'+phase+'-raw');raw.mkdir(exist_ok=False)
env=dict(os.environ,PYTHONPATH=f"tests:/tmp/ticket23-tools:{out/'24-repair2-tools'}",TICKET24REPAIR2_RAW=str(raw))
command=[sys.executable,'-m','pytest','-vv','--tb=short','-p','capture24repair2',*sys.argv[2:]]
log=out/f'24-repair2-{phase}.log';start=time.time()
with log.open('xb') as stream:r=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
for name,digest in frozen['source_hashes'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
record=dict(command=command,exit=r.returncode,seconds=time.time()-start,source=identity.name,raw=str(raw),log=str(log),log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
(out/f'24-repair2-{phase}-result.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
