"""Archive the required suite's retained raw records and verify a streaming readback."""
import hashlib
import json
from pathlib import Path
import tarfile

out = Path('.scratch/ticket-harness/evidence')
raw = Path('/tmp/ticket23-final-raw')
manifest = {}
index = []
for path in sorted(raw.rglob('*')):
    if path.is_file():
        manifest[str(path.relative_to(raw))] = dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(), size=path.stat().st_size)
        if path.name == 'observations.json':
            item = json.loads(path.read_text())
            index.append(dict(scenario=item['scenario'], path=str(path.relative_to(raw)), outcome=item['record']['outcome'], failure=item['record'].get('failure'), attempts=len(item['record']['attempts']), gates=len(item['record']['gates'])))
(out/'23-raw-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(out/'23-observation-index.json').write_text(json.dumps(index,indent=2)+'\n')
archive = out/'23-final-raw.tar.gz'
with tarfile.open(archive,'w:gz') as stream:
    stream.add(raw,arcname='raw')
seen = set()
with tarfile.open(archive,'r|gz') as stream:
    for member in stream:
        if member.isfile():
            name = member.name.removeprefix('raw/')
            body = stream.extractfile(member).read()
            assert len(body) == manifest[name]['size']
            assert hashlib.sha256(body).hexdigest() == manifest[name]['sha256']
            seen.add(name)
assert seen == set(manifest)
(out/'23-capture-audit.json').write_text(json.dumps(dict(files=len(seen), scenarios=len(index), archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), stream_readback='all file sizes and hashes match'),indent=2)+'\n')
print(len(index), len(seen), archive.stat().st_size)
