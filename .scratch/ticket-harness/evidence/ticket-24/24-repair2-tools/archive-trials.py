"""Preserve raw developmental observations and the intentionally incomplete replay."""
import hashlib,json,tarfile
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
for phase in ('red-captured','green-captured','focused'):
 raw=Path('/tmp/ticket24-repair2-'+phase+'-raw')
 manifest={str(p.relative_to(raw)):dict(size=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in raw.rglob('*') if p.is_file()}
 archive=out/f'24-repair2-{phase}-raw.tar.gz'
 with tarfile.open(archive,'w:gz') as s:s.add(raw,arcname='raw')
 seen=set()
 with tarfile.open(archive,'r|gz') as s:
  for member in s:
   if member.isfile():
    name=member.name.removeprefix('raw/');body=s.extractfile(member).read();assert len(body)==manifest[name]['size'] and hashlib.sha256(body).hexdigest()==manifest[name]['sha256'];seen.add(name)
 assert seen==set(manifest)
 r=dict(phase=phase,files=manifest,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),readback='all regular-file sizes and hashes match')
 if phase=='focused':r.update(command_scope='optional affected-file replay; interrupted via session control after root directed proceed to required full suite',exit=130,completed=False,passing_gate=False,source='24-repair2-final-source.json',log='24-repair2-focused-check-0.log')
 (out/f'24-repair2-{phase}-raw-audit.json').write_text(json.dumps(r,indent=2)+'\n')
 print(phase,len(seen),archive.stat().st_size)
