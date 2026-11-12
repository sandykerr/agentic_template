"""Retain lossless diagnosis/repair trials before normalizing readable failure logs."""
import hashlib,io,json,tarfile
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
phases=['resume-diagnosis-old','resume-pinned-observer-red','resume-observer-entry-red','resume-observer-entry-green','resume-focused-green','resume-final-observer-green']
archive=out/'24-resume-trials-raw.tar.gz';manifest={};logs={};rows=[]
def add(stream,name,body):
 assert name not in manifest
 member=tarfile.TarInfo(name);member.size=len(body);stream.addfile(member,io.BytesIO(body))
 manifest[name]=dict(size=len(body),sha256=hashlib.sha256(body).hexdigest())
with tarfile.open(archive,'x:gz') as stream:
 for phase in phases:
  result_path=out/f'24-repair2-{phase}-result.json';result=json.loads(result_path.read_text());log=Path(result['log']);body=log.read_bytes()
  assert hashlib.sha256(body).hexdigest()==result['log_sha256']
  for path in [result_path,log,out/result['source']]:add(stream,phase+'/'+path.name,path.read_bytes())
  raw=Path(result['raw'])
  for path in sorted(raw.rglob('*')):
   if path.is_file():add(stream,phase+'/raw/'+str(path.relative_to(raw)),path.read_bytes())
  normalized=b'\n'.join(line.rstrip(b' \t\r') for line in body.split(b'\n')).rstrip(b'\n')+b'\n'
  logs[str(log)]=dict(original_sha256=hashlib.sha256(body).hexdigest(),display_sha256=hashlib.sha256(normalized).hexdigest(),archive_member=phase+'/'+log.name)
  rows.append(dict(phase=phase,exit=result['exit'],source=result['source'],scenarios=len(list(raw.glob('*/observations.json')))))
 for name in ('delay24resume.py','delay24observerentry.py','resume-scoped-check.py'):
  add(stream,'tools/'+name,(out/'24-repair2-tools'/name).read_bytes())
seen=set()
with tarfile.open(archive,'r|gz') as stream:
 for member in stream:
  if member.isfile():
   body=stream.extractfile(member).read();assert member.name not in seen;assert len(body)==manifest[member.name]['size'];assert hashlib.sha256(body).hexdigest()==manifest[member.name]['sha256'];seen.add(member.name)
assert seen==set(manifest)
for name in logs:
 p=Path(name);body=p.read_bytes();p.write_bytes(b'\n'.join(line.rstrip(b' \t\r') for line in body.split(b'\n')).rstrip(b'\n')+b'\n')
(out/'24-resume-trials-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(out/'24-resume-trial-provenance.json').write_text(json.dumps(dict(archive=str(archive),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),files=len(seen),stream_readback='all original regular-file sizes and hashes match; no duplicates; complete membership',phases=rows,logs=logs,rule='historical log_sha256 values refer to lossless archive members; readable copies only trim line-end whitespace and excess final blank lines'),indent=2)+'\n')
print(json.dumps(dict(files=len(seen),phases=rows)))
