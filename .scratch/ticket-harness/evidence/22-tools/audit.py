"""Audit final source and archived raw evidence by streaming original bytes."""
import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

out = Path('.scratch/ticket-harness/evidence')
source = json.loads((out / '22-final-source.json').read_text())
producer = json.loads((out / '22-checkpoint/producer.json').read_text())
baseline = '803c6ff9a4e5e057124aefc5bb96f2c9518162dd'
assert producer['producer_head'] == baseline
for name, digest in producer['source_hashes'].items():
    blob = subprocess.check_output(['git', 'show', baseline + ':' + name])
    assert hashlib.sha256(blob).hexdigest() == digest, name
for name, digest in source['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, name
(out / '22-source-crosscheck.json').write_text(json.dumps(dict(baseline=baseline, producer_files=len(producer['source_hashes']), final_files=len(source['files']), producer_matches_baseline=True, final_matches_working_tree=True, changed_paths=subprocess.check_output(['git', 'diff', '--name-only', baseline, '--', 'ticket_harness', 'tests', 'examples', 'pyproject.toml', 'environment.yml'], text=True).splitlines()), indent=2) + '\n')
manifest = json.loads((out / '22-raw-manifest.json').read_text())
seen = set()
with tarfile.open(out / '22-final-raw.tar.gz', 'r|gz') as archive:
    for member in archive:
        if not member.isfile():
            continue
        relative = str(Path(member.name).relative_to('ticket22-final-raw'))
        stream = archive.extractfile(member)
        assert stream is not None
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        assert digest == manifest[relative], relative
        seen.add(relative)
assert seen == manifest.keys()
artifacts = [out / name for name in ('22-final-raw.tar.gz', '22-focused-raw.tar.gz', '22-raw-manifest.json', '22-observation-index.json', '22-final-source.json', '22-final-check-results.json')]
(out / '22-capture-audit.json').write_text(json.dumps(dict(raw_files_verified=len(seen), source='22-source-crosscheck.json', artifacts={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in artifacts}), indent=2) + '\n')
print(json.dumps(dict(raw_files=len(seen), final_files=len(source['files']), producer_files=len(producer['source_hashes']))))
