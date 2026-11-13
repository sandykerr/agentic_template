"""Archive one completed resumed phase without rewriting halted evidence."""
import hashlib
import json
from pathlib import Path
import sys
import tarfile

phase = sys.argv[1]
assert phase.isascii() and all(c in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in phase)
out = Path('.scratch/ticket-harness/evidence')
raw = Path('/tmp/ticket24-repair2-' + phase + '-raw')
results = json.loads((out / f'24-repair2-{phase}-check-results.json').read_text())
assert len(results) == 6 and all(row['exit'] == 0 for row in results)
assert '559 passed' in Path(results[0]['log']).read_text()
manifest = {}
index = []
for path in sorted(raw.rglob('*')):
    if path.is_file():
        name = str(path.relative_to(raw))
        body = path.read_bytes()
        manifest[name] = dict(sha256=hashlib.sha256(body).hexdigest(), size=len(body))
        if path.name == 'observations.json':
            item = json.loads(body)
            assert item['status']['exit_code'] == 0
            assert json.loads(item['status']['stdout']) == item['record']
            index.append(dict(scenario=item['scenario'], path=name, outcome=item['record']['outcome'], failure=item['record'].get('failure'), attempts=len(item['record']['attempts']), gates=len(item['record']['gates'])))
assert len(index) == 559
assert len({row['scenario'] for row in index}) == 559
archive = out / f'24-repair2-{phase}-raw.tar.gz'
with tarfile.open(archive, 'x:gz') as stream:
    stream.add(raw, arcname='raw')
seen = set()
with tarfile.open(archive, 'r|gz') as stream:
    for member in stream:
        if member.isfile():
            name = member.name.removeprefix('raw/')
            body = stream.extractfile(member).read()
            assert name not in seen
            assert len(body) == manifest[name]['size']
            assert hashlib.sha256(body).hexdigest() == manifest[name]['sha256']
            seen.add(name)
assert seen == set(manifest)
for suffix, value in [('manifest', manifest), ('index', index), ('audit', dict(files=len(seen), scenarios=len(index), archive=str(archive), archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), stream_readback='all file sizes and hashes match; no duplicates; complete membership', checks=f'24-repair2-{phase}-check-results.json'))]:
    with (out / f'24-repair2-{phase}-{suffix}.json').open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')
print(len(index), len(seen), archive.stat().st_size)
