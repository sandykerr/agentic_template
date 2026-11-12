"""Run final gates with immediate failure traces and a separately controlled pytest child."""
import hashlib,json,os,re,signal,subprocess,sys,time
from pathlib import Path
phase=sys.argv[1]
assert re.fullmatch('[a-z0-9-]+',phase)
out=Path('.scratch/ticket-harness/evidence');identity_name=f'24-repair2-{phase}-source.json'
identity=json.loads((out/identity_name).read_text());raw=Path('/tmp/ticket24-repair2-'+phase+'-raw');raw.mkdir(exist_ok=False)
reports=out/f'24-repair2-{phase}-pytest-reports.jsonl';assert not reports.exists()
env=dict(os.environ,PYTHONPATH=f"tests:/tmp/ticket23-tools:{out/'24-repair2-tools'}",TICKET24REPAIR2_RAW=str(raw),TICKET24RESUME_REPORTS=str(reports))
commands=[
 [sys.executable,'-m','pytest','-q','--durations=20','--maxfail=1','-p','capture24repair2','-p','result24resume'],
 [sys.executable,'-m','mypy'],
 [sys.executable,'-m','ruff','check','ticket_harness','tests','examples'],
 [sys.executable,'-m','ruff','format','--check','ticket_harness','tests','examples'],
 ['git','diff','--check'],
 ['git','diff','--check',identity['baseline'],'--','ticket_harness','tests','examples'],
]
tools={str(out/'24-repair2-tools'/n):hashlib.sha256((out/'24-repair2-tools'/n).read_bytes()).hexdigest() for n in ('identity.py','resume-final-checks.py','capture24repair2.py','result24resume.py')}
(out/f'24-repair2-{phase}-capture-tools.json').write_text(json.dumps(tools,indent=2)+'\n')
results=[]
for i,command in enumerate(commands):
 for n,d in identity['source_hashes'].items():assert hashlib.sha256(Path(n).read_bytes()).hexdigest()==d,n
 log=out/f'24-repair2-{phase}-check-{i}.log';start=time.time();interrupted=False
 with log.open('xb') as stream:
  process=subprocess.Popen(command,env=env,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
  try:
   code=process.wait()
  except KeyboardInterrupt:
   interrupted=True;process.send_signal(signal.SIGINT)
   try:code=process.wait(timeout=45)
   except subprocess.TimeoutExpired:
    os.killpg(process.pid,signal.SIGKILL);code=process.wait()
 for n,d in identity['source_hashes'].items():assert hashlib.sha256(Path(n).read_bytes()).hexdigest()==d,n
 for n,d in tools.items():assert hashlib.sha256(Path(n).read_bytes()).hexdigest()==d,n
 results.append(dict(command=command,exit=code,seconds=time.time()-start,log=str(log),source=identity_name,interrupted=interrupted,environment={k:env[k] for k in ('PYTHONPATH','TICKET24REPAIR2_RAW','TICKET24RESUME_REPORTS')}))
 (out/f'24-repair2-{phase}-check-results.json').write_text(json.dumps(results,indent=2)+'\n');print(i,code,flush=True)
 if interrupted:raise SystemExit(130)
assert all(r['exit']==0 for r in results),results
