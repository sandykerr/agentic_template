import hashlib,json,os,subprocess,sys,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
identity=json.loads((out/'23-final-source.json').read_text())
assert all(hashlib.sha256(Path(n).read_bytes()).hexdigest()==d for n,d in identity['source_hashes'].items())
command=[sys.executable,'-m','pytest','-q','--durations=20','-p','capture23']
env=dict(os.environ,PYTHONPATH='tests:/tmp/ticket23-tools:'+str(out/'23-tools'),TICKET23_RAW='/tmp/ticket23-final-raw')
start=time.time()
with (out/'23-final-suite.log').open('wb') as stream:
    result=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
entry=dict(command=command,exit=result.returncode,seconds=time.time()-start,log=str(out/'23-final-suite.log'),source='23-final-source.json',environment={k:env[k] for k in ('PYTHONPATH','TICKET23_RAW')})
(out/'23-final-suite-result.json').write_text(json.dumps(entry,indent=2)+'\n')
assert all(hashlib.sha256(Path(n).read_bytes()).hexdigest()==d for n,d in identity['source_hashes'].items())
print(entry)
assert result.returncode==0
