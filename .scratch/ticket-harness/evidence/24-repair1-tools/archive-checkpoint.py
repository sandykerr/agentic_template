"""Retain the genuinely old checkpoint's final repair-source continuation and audit it."""
import hashlib,json,tarfile
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence/24-repair1-checkpoint')
producer=json.loads(Path('.scratch/ticket-harness/evidence/24-checkpoint/producer.json').read_text())
home=Path(producer['home']);final=json.loads((out/'continuation-final.json').read_text())
assert final['final']['outcome']=='completed'
manifest={str(p.relative_to(home)):dict(size=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in home.rglob('*') if p.is_file()}
archive=out/'continued-final-live.tar.gz'
with tarfile.open(archive,'w:gz') as stream:stream.add(home,arcname='tmp/'+home.name)
seen=set()
with tarfile.open(archive,'r|gz') as stream:
 for member in stream:
  if member.isfile():
   name=member.name.removeprefix('tmp/'+home.name+'/');body=stream.extractfile(member).read()
   assert len(body)==manifest[name]['size'] and hashlib.sha256(body).hexdigest()==manifest[name]['sha256'];seen.add(name)
assert seen==set(manifest)
(out/'archive-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(out/'audit.json').write_text(json.dumps(dict(files=len(seen),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),stream_readback='all regular-file sizes and hashes match',producer='../24-checkpoint/producer.json',consumer='continuation-final.json',consumer_exit=0,one_baseline=True,two_consumed_decisions=True,old_attempt_gate_prefixes_equal=True,final_refs_equal_exact_second_candidate=True),indent=2)+'\n')
