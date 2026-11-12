"""Pin caller delay at the existing public-observation fixture; no production edits."""
import time
import test_qa_promotion

_original = test_qa_promotion.approve

def pytest_runtest_setup(item):
    if item.name != 'test_approval_rejects_same_oid_alias_installed_after_destination_validation':
        return
    def late_observer(graph, request):
        result = _original(graph, request)
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            record = graph.record()
            if any(m['id'] == 'M1' and m['state'] == 'promoted' for m in record.get('milestones', [])):
                return result
            time.sleep(0.01)
        raise AssertionError('Diagnosis did not observe public M1-promoted record')
    test_qa_promotion.approve = late_observer

def pytest_runtest_teardown(item):
    test_qa_promotion.approve = _original
