"""Produce a genuine deliberate checkpoint using unchanged public CLI fixtures."""
import hashlib
import json
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path.cwd() / 'tests'))
from test_dependencies import graph
from test_milestones import configure_plan, foreground
from test_qa_promotion import waiting

out = Path('.scratch/ticket-harness/evidence/20-checkpoint')
fixture_generator = graph.__wrapped__(SimpleNamespace(node=SimpleNamespace(name='ticket20_pre_refactor', path=Path('capture.py'))))
fixture = next(fixture_generator)
fixture.temp._finalizer.detach()  # Retain the real repository/worktrees across producer exit.
configure_plan(fixture)
with foreground(fixture) as process:
    waiting(fixture, process, 'M1')
    stopped = fixture.cli('stop', fixture.output)
    assert stopped.returncode == 0
    process.wait(timeout=10)
    assert process.returncode == 2
record = fixture.record()
assert record['outcome'] == 'stopped_at_qa'
paths = list(Path('ticket_harness').glob('*.py')) + list(Path('tests').glob('*.py'))
identity = dict(producer_head=fixture.git('-C', str(Path.cwd()), 'rev-parse', 'HEAD'), home=str(fixture.home), record=record, foreground=fixture.foreground_observations, cli=fixture.cli_observations, source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(out / 'producer.json').write_text(json.dumps(identity, indent=2) + '\n')
(out / 'stopped-run.json').write_bytes((fixture.output / 'run.json').read_bytes())
(out / 'stopped-checkpoint.json').write_bytes((fixture.output / 'qa-checkpoint.json').read_bytes())
print(json.dumps({'home':str(fixture.home), 'outcome':record['outcome'], 'owner_exit':process.returncode}))
# Explicit cleanup would erase the checkpoint. Generator remains live until interpreter exit;
# its teardown has no external output destination and the detached temp finalizer preserves files.
