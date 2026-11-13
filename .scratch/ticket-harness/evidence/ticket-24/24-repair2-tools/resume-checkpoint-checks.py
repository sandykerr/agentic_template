"""Renew genuine old-checkpoint continuation on the repaired test/source freeze."""
import hashlib,json,subprocess,sys,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence');frozen=json.loads((out/'24-repair2-resumed-repaired-final-source.json').read_text());rows=[]
for name in ('resume-restore-old.py','resume-continue-old.py','resume-archive-checkpoint.py'):
 for path,digest in frozen['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
 command=[sys.executable,str(out/'24-repair2-tools'/name)];log=out/('24-resume-'+name.removesuffix('.py')+'.log');start=time.time()
 with log.open('xb') as stream:r=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT)
 for path,digest in frozen['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,path
 rows.append(dict(command=command,exit=r.returncode,seconds=time.time()-start,log=str(log),tool_sha256=hashlib.sha256((out/'24-repair2-tools'/name).read_bytes()).hexdigest(),source='24-repair2-resumed-repaired-final-source.json'))
 (out/'24-resume-checkpoint-checks.json').write_text(json.dumps(rows,indent=2)+'\n');print(name,r.returncode,flush=True)
 assert r.returncode==0
