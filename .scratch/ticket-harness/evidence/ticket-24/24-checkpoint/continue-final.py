"""Continue a genuine baseline-produced checkpoint using final working source."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / 'tests'))
from test_dependencies import DependencyFixture
from test_milestones import foreground
from test_qa_promotion import approve, waiting

out = Path('.scratch/ticket-harness/evidence/24-checkpoint')
producer = json.loads((out / 'producer.json').read_text())
for name, digest in producer['source_hashes'].items():
    original = subprocess.check_output(['git', 'show', 'ed017ae0c2b96769f31c710cfb4ff4708989b446:' + name])
    assert hashlib.sha256(original).hexdigest() == digest, name
fixture = DependencyFixture()
fixture.home = Path(producer['home'])
fixture.repo = fixture.home / 'target'
fixture.output = fixture.home / 'run'
fixture.config_path = fixture.home / 'project.json'
fixture.cli_observations = []
prior = fixture.record()
assert prior == producer['record']
assert prior['outcome'] == 'stopped_at_qa'
request = json.loads((fixture.output / 'qa-request.json').read_text())
approve(fixture, request)
with foreground(fixture, operation='continue') as process:
    later = waiting(fixture, process, 'M2')
    assert len(later['qa_decisions']) == 1
    assert later['attempts'][:len(prior['attempts'])] == prior['attempts']
    assert later['gates'][:len(prior['gates'])] == prior['gates']
    second_request = json.loads((fixture.output / 'qa-request.json').read_text())
    approve(fixture, second_request)
    process.wait(timeout=20)
    assert process.returncode == 0
final = fixture.record()
assert final['outcome'] == 'completed' and final['feature_complete'] is True
assert len(final['qa_decisions']) == 2
assert [g['stage'] for g in final['gates']].count('baseline') == 1
assert [(a['ticket'], a['attempt']) for a in final['attempts']] == [('03', 1), ('01', 1), ('04', 1), ('02', 1)]
assert fixture.git('rev-parse', 'integration') == fixture.git('rev-parse', 'dev') == second_request['candidate_revision']
status = fixture.cli('status', fixture.output)
assert status.returncode == 0 and json.loads(status.stdout) == final
consumer_hashes = {name: hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in producer['source_hashes']}
assert consumer_hashes == {name: digest for name, digest in json.loads((out.parent / '24-final-source.json').read_text())['source_hashes'].items() if name in consumer_hashes}
observations = dict(consumer_hashes=consumer_hashes, producer_source='producer.json', consumer_source='../24-final-source.json', final=final, foreground=fixture.foreground_observations, cli=fixture.cli_observations, refs=fixture.git('show-ref'), caller_status=fixture.git('status', '--porcelain'), history=fixture.git('log', '--all', '--format=%H %P %s'))
(out / 'continuation-final.json').write_text(json.dumps(observations, indent=2) + '\n')
print(json.dumps({'continued':str(fixture.output), 'exit':process.returncode, 'outcome':final['outcome'], 'attempts':len(final['attempts'])}))
