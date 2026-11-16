"""Retain one baseline-rejection observation before unittest fixture cleanup."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tests'))
from test_cli import TicketCycleTests

fixture = TicketCycleTests()
fixture.setUp()
try:
    fixture.test_failed_baseline_is_environment_failure_without_an_assignment()
    record = fixture.record()
    observation = {
        'scenario': 'failed baseline without agent assignment or repair',
        'reason_for_scoped_capture': 'unittest cleans its disposable repository before the suite report hook can retain its run record',
        'record': record,
        'caller_head': fixture.git('rev-parse', 'HEAD'),
        'integration': fixture.git('rev-parse', 'integration'),
        'base': fixture.base,
        'outputs': {key: Path(record['gates'][0][key]).read_text()
                    for key in ('stdout', 'stderr')},
    }
    destination = Path(__file__).resolve().parent / 'baseline-observation.json'
    destination.write_text(json.dumps(observation, indent=2) + '\n')
    print('Observed environment outcome, zero attempts, one failed baseline gate, unchanged integration.')
finally:
    fixture.doCleanups()
