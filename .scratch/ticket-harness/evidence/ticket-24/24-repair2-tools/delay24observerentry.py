"""Pin late observer entry only when the caller published approval before arming it."""
from contextlib import contextmanager
import json
from pathlib import Path
import time
import test_qa_promotion

_original = test_qa_promotion.pause_after_git

@contextmanager
def late_entry(process, arguments, **kwargs):
    output = Path(process.args[process.args.index('--output') + 1])
    if (output / 'qa-decision.json').exists():
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            record = json.loads((output / 'run.json').read_text())
            if any(m['id'] == 'M1' and m['state'] == 'promoted' for m in record.get('milestones', [])):
                break
            time.sleep(0.01)
        else:
            raise AssertionError('Diagnosis did not observe public M1-promoted record')
    with _original(process, arguments, **kwargs):
        yield

def pytest_runtest_setup(item):
    if item.name == 'test_approval_rejects_same_oid_alias_installed_after_destination_validation':
        test_qa_promotion.pause_after_git = late_entry

def pytest_runtest_teardown(item):
    test_qa_promotion.pause_after_git = _original
