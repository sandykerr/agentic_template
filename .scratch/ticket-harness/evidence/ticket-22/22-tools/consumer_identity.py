"""Pin final consumer source and genuine archived checkpoint restoration."""
import hashlib
import json
import tarfile
from pathlib import Path

out = Path('.scratch/ticket-harness/evidence')
source = json.loads((out / '22-final-source.json').read_text())
for name, digest in source['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, name
with tarfile.open(out / '22-checkpoint/stopped-live.tar.gz', 'r:gz') as archive:
    for name in ('run.json', 'qa-checkpoint.json'):
        member = 'ticket-harness-test-e2gc9ntm/run/' + name
        file = archive.extractfile(member)
        assert file is not None
        expected = 'stopped-run.json' if name == 'run.json' else 'stopped-checkpoint.json'
        assert file.read() == (out / '22-checkpoint' / expected).read_bytes()
identity = dict(source='../22-final-source.json', files=source['files'], archive_restore='stopped-live.tar.gz restored at original paths', artifacts={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out / '22-checkpoint').iterdir() if p.is_file() and p.name != 'final-consumer-source.json'})
(out / '22-checkpoint/final-consumer-source.json').write_text(json.dumps(identity, indent=2) + '\n')
