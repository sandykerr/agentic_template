"""Audit immutable full-suite artifacts and exact tested runtime/test source."""
import hashlib
import json
import tarfile
from pathlib import Path

out = Path('.scratch/ticket-harness/evidence')
manifest = json.loads((out / '21-raw-manifest.json').read_text())
source = json.loads((out / '21-final-source.json').read_text())
results = json.loads((out / '21-final-check-results.json').read_text())
assert len(results['results']) == 6 and all(item['exit_code'] == 0 for item in results['results'])
for name, digest in source['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, name
archive = out / '21-final-raw.tar.gz'
matched = set()
with tarfile.open(archive, mode='r|gz') as saved:
    for member in saved:
        if not member.isfile():
            continue
        name = member.name.removeprefix('ticket21-final-raw/')
        assert name in manifest and name not in matched, name
        assert hashlib.sha256(saved.extractfile(member).read()).hexdigest() == manifest[name], name
        matched.add(name)
assert matched == set(manifest)
index = json.loads((out / '21-observation-index.json').read_text())
assert index['scenario_count'] == 544
result = {
    'source_files_matched': len(source['files']),
    'raw_files_matched': len(manifest),
    'scenario_count': index['scenario_count'],
    'checks_passed': len(results['results']),
    'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
    'source_manifest_sha256': hashlib.sha256((out / '21-final-source.json').read_bytes()).hexdigest(),
    'raw_manifest_sha256': hashlib.sha256((out / '21-raw-manifest.json').read_bytes()).hexdigest(),
    'scope': 'Working runtime/test bytes and archived raw files match their recorded exact identities. Independent source assessment and eventual commit blob crosscheck remain separate.'
}
(out / '21-capture-audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
