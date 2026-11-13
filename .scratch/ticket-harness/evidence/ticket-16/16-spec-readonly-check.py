import gzip
import hashlib
import json
from pathlib import Path
import tarfile

root = Path.cwd()
evidence = root / '.scratch/ticket-harness/evidence'
helper = evidence / '16-check.py'
namespace = {'__name__': 'readonly_ticket16_spec_review', '__file__': str(helper)}
exec(compile(helper.read_text(), str(helper), 'exec'), namespace)
observations = namespace['check_saved']()
print('saved_artifact_checks=pass; links=' + str(len(observations['resolved_links'])))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for filename in ('16-build-results.json', '16-check-results.json'):
    data = json.loads((evidence / filename).read_text())
    source_mismatches = [p for p, h in data['source_sha256'].items() if sha(root / p) != h]
    fixture_mismatches = [p for p, h in data['fixture_sha256'].items() if sha(evidence / '16-miniature' / p) != h]
    assert not fixture_mismatches
    assert source_mismatches == (['.scratch/ticket-harness/evidence/16-run-checks.sh', '.scratch/ticket-harness/evidence/16-implementation-report.md'] if filename == '16-build-results.json' else [])
    print(json.dumps({'record': filename, 'retained_result': data['result'], 'fixture_hashes': len(data['fixture_sha256']), 'source_mismatches': source_mismatches}))
    if filename == '16-build-results.json':
        assert data['generated']['immutable_before'] == data['generated']['immutable_after']
        assert len(data['generated']['events']) == 9
        assert all(c['exit'] == 0 for c in data['commands'])
        print('build_history_events=9; original_snapshot_hashes_preserved=true; recorded_commands_all_exit_zero=true')
for filename in ('16-initial-fixture.tar.gz', '16-pre-final-fixture.tar.gz', '16-link-audit-fixture.tar.gz'):
    with tarfile.open(evidence / filename) as archive:
        print(filename, 'retained_members=', len(archive.getmembers()))
for filename in ('16-original-command-log.gz', '16-initial-staged-whitespace.log.gz'):
    raw = gzip.decompress((evidence / filename).read_bytes()).decode()
    print(filename, 'retained_raw_lines=', len(raw.splitlines()))
print('readonly_review_checks=pass')
