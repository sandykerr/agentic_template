"""Retain selected public CLI/Git observations during the required suite run."""
import hashlib
import json
from pathlib import Path

import pytest


OUT = Path(__file__).resolve().parent / 'completion-suite-observations'
SELECTED = {
    'test_missing_acceptance_requirements_rejects_before_any_execution',
    'test_failed_baseline_is_environment_failure_without_an_assignment',
    'test_continued_run_records_invalidation_of_earlier_verified_source',
    'test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision',
}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    name = item.originalname or item.name
    if report.when != 'call' or not (name in SELECTED or name.startswith('test_inherited_')):
        return
    fixture = next((item.funcargs[key] for key in ('graph', 'harness', 'case')
                    if key in item.funcargs), getattr(item, 'instance', None))
    if fixture is None or not hasattr(fixture, 'output'):
        return
    record_path = fixture.output / 'run.json'
    if not record_path.exists():
        return
    record = json.loads(record_path.read_text())
    value = {'nodeid': item.nodeid, 'result': report.outcome, 'record': record,
             'caller_head': fixture.git('rev-parse', 'HEAD'),
             'integration': fixture.git('rev-parse', 'integration'),
             'caller_status': fixture.git('status', '--porcelain'),
             'caller_index_sha256': hashlib.sha256((fixture.repo / '.git/index').read_bytes()).hexdigest(),
             'qa_artifacts': {str(p.resolve().relative_to(fixture.output.resolve())): p.read_text()
                              for p in fixture.output.rglob('qa-*.json') if p.is_file()},
             'gate_outputs': {str(p.resolve().relative_to(fixture.output.resolve())): p.read_text(errors='replace')
                              for g in record.get('gates', [])
                              for key in ('stdout', 'stderr') if key in g
                              for p in [Path(g[key])] if p.is_file()}}
    if 'plan' in fixture.config:
        value['development'] = fixture.git('rev-parse', 'dev')
    OUT.mkdir(exist_ok=True)
    safe = item.name.replace('/', '_')
    (OUT / (safe + '.json')).write_text(json.dumps(value, indent=2) + '\n')
