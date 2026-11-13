"""Retain focused public CLI trial identities, command, output and raw observations."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence');phase=sys.argv[1];old=sys.argv[2]=='old'
original=Path('ticket_harness/git.py').read_bytes()
try:
 if old:Path('ticket_harness/git.py').write_bytes(subprocess.check_output(['git','show','564c0a963cdcf39b7ed6c2254c2906552d90a465:ticket_harness/git.py']))
 source={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in json.loads((out/'24-repair1-final-source.json').read_text())['source_hashes']}
 raw=Path('/tmp/ticket24-repair2-'+phase+'-raw');raw.mkdir()
 env=dict(os.environ,PYTHONPATH=f"tests:/tmp/ticket23-tools:{out/'24-repair2-tools'}",TICKET24REPAIR2_RAW=str(raw))
 command=[sys.executable,'-m','pytest','-q',*sys.argv[3:],'-p','capture24repair2']
 log=out/f'24-repair2-{phase}.log';start=time.monotonic()
 with log.open('wb') as stream:r=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
 result=dict(command=command,exit=r.returncode,seconds=time.monotonic()-start,source_hashes=source,git_source='original rejected repair1 source' if old else 'current worktree',diff=subprocess.check_output(['git','diff','--','ticket_harness','tests'],text=True),raw=str(raw),log=str(log))
 (out/f'24-repair2-{phase}.json').write_text(json.dumps(result,indent=2)+'\n');print(r.returncode)
finally:Path('ticket_harness/git.py').write_bytes(original)
