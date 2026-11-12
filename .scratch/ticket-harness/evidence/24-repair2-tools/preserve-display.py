import hashlib,json,subprocess,tarfile,io
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence'); baseline='ed017ae0c2b96769f31c710cfb4ff4708989b446'
r=subprocess.run(['git','diff','--check',baseline,'--',str(out)],capture_output=True,text=True)
names=sorted({line.split(':')[0] for line in r.stdout.splitlines() if line.startswith(str(out))})
archive=out/'24-resume-immutable-originals.tar.gz'; records={}
with tarfile.open(archive,'x:gz') as tar:
 for name in names:
  p=Path(name); body=p.read_bytes(); normalized=b'\n'.join(line.rstrip(b' \t\r') for line in body.split(b'\n')).rstrip(b'\n')+b'\n'
  member=tarfile.TarInfo(p.name);member.size=len(body);tar.addfile(member,io.BytesIO(body))
  records[name]={'original_sha256':hashlib.sha256(body).hexdigest(),'display_sha256':hashlib.sha256(normalized).hexdigest(),'archive_member':p.name,'original_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}
with tarfile.open(archive,'r:gz') as tar:
 for name,row in records.items():
  assert hashlib.sha256(tar.extractfile(row['archive_member']).read()).hexdigest()==row['original_sha256']
for name,row in records.items():
 p=Path(name);body=p.read_bytes();p.write_bytes(b'\n'.join(line.rstrip(b' \t\r') for line in body.split(b'\n')).rstrip(b'\n')+b'\n')
(out/'24-resume-display-provenance.json').write_text(json.dumps({'archive':str(archive),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'readback':'every original matched its SHA256 before display normalization','rule':'trim end-of-line spaces/tabs/CR and excess final blank lines only; historical original digests resolve to archived bytes, never display copies','files':records},indent=2)+'\n')
print(len(records),'original files preserved and displays normalized')
