"""Audit preserved producer/consumer source identity and complete archived file streams."""
import hashlib
import json
from pathlib import Path
import subprocess
import tarfile

out = Path('.scratch/ticket-harness/evidence')
base = out / '24-checkpoint'
producer = json.loads((base / 'producer.json').read_text())
consumer = json.loads((base / 'continuation-final.json').read_text())
frozen = json.loads((out / '24-final-source.json').read_text())
baseline = 'ed017ae0c2b96769f31c710cfb4ff4708989b446'
assert producer['producer_head'] == baseline
for name, digest in producer['source_hashes'].items():
    assert hashlib.sha256(subprocess.check_output(['git', 'show', baseline + ':' + name])).hexdigest() == digest
assert all(consumer['consumer_hashes'][name] == frozen['source_hashes'][name] for name in consumer['consumer_hashes'])
assert consumer['final']['outcome'] == 'completed'
assert producer['record'] == json.loads((base / 'stopped-run.json').read_text())
summary = {}
for archive, record_file, expected in (
    ('stopped-live.tar.gz', 'stopped-run.json', producer['record']),
    ('continued-final-live.tar.gz', None, consumer['final']),
):
    count = 0
    seen = set()
    home = producer['home'].lstrip('/')
    with tarfile.open(base / archive, 'r|gz') as stream:
        for member in stream:
            assert member.name not in seen
            seen.add(member.name)
            if member.isfile():
                body = stream.extractfile(member).read()
                assert len(body) == member.size
                count += 1
                if member.name == home + '/run/run.json':
                    assert json.loads(body) == expected
                    if record_file:
                        assert body == (base / record_file).read_bytes()
                if archive == 'stopped-live.tar.gz' and member.name == home + '/run/qa-checkpoint.json':
                    assert body == (base / 'stopped-checkpoint.json').read_bytes()
    assert home + '/run/run.json' in seen
    assert home + '/target/.git/HEAD' in seen
    summary[archive] = dict(files_read=count, sha256=hashlib.sha256((base / archive).read_bytes()).hexdigest())
result = dict(producer_baseline=baseline, producer_source_files=len(producer['source_hashes']), consumer_source_files=len(consumer['consumer_hashes']), frozen_source_files=len(frozen['source_hashes']), producer_matches_baseline=True,consumer_matches_frozen=True,archives=summary, scope='Streaming read of every regular archived file; retained run records/checkpoint match observations. Archive content identity is separate from behavioral/design conclusions.')
(base / 'audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
