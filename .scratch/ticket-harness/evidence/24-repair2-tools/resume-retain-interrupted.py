"""Losslessly retain the known-failing, interrupted first resumed freeze."""
import hashlib,json,tarfile,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence');raw=Path('/tmp/ticket24-repair2-resumed-final-raw')
manifest={str(p.relative_to(raw)):dict(size=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in raw.rglob('*') if p.is_file()}
index=[]
for p in sorted(raw.glob('*/observations.json'),key=lambda p:p.stat().st_mtime):
 r=json.loads(p.read_text());index.append(dict(scenario=r['scenario'],outcome=r['record']['outcome'],path=str(p.relative_to(raw))))
archive=out/'24-resume-interrupted-failed-raw.tar.gz'
with tarfile.open(archive,'x:gz') as stream:stream.add(raw,arcname='raw')
seen=set()
with tarfile.open(archive,'r|gz') as stream:
 for member in stream:
  if member.isfile():
   name=member.name.removeprefix('raw/');body=stream.extractfile(member).read();assert len(body)==manifest[name]['size'];assert hashlib.sha256(body).hexdigest()==manifest[name]['sha256'];seen.add(name)
assert seen==set(manifest)
frozen=json.loads((out/'24-repair2-resumed-final-source.json').read_text())
for name,digest in frozen['source_hashes'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
for name,value in [('manifest',manifest),('index',index)]:
 (out/f'24-resume-interrupted-failed-{name}.json').write_text(json.dumps(value,indent=2)+'\n')
record=dict(utc=time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),source='24-repair2-resumed-final-source.json',source_unchanged=True,session=14799,exit=130,completed=False,passing_gate=False,reason='Root directed stop of known-failing freeze before bounded repair; Ctrl-C returned130',log='24-repair2-resumed-final-check-0.log',log_sha256=hashlib.sha256((out/'24-repair2-resumed-final-check-0.log').read_bytes()).hexdigest(),traceback='No traceback emitted before tool termination; partial log retains two F markers; scoped old-source investigation required',captured_scenarios=len(index),files=len(seen),archive=str(archive),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),stream_readback='every regular file size and hash matches manifest',pending='all six final-source gates; no follow-on statics ran')
(out/'24-resume-interrupted-failed-audit.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
