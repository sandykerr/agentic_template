"""Preserve each pytest phase outcome and failure trace as it happens."""
import json
import os
from pathlib import Path


def pytest_runtest_logreport(report):
    row = dict(nodeid=report.nodeid, when=report.when, outcome=report.outcome,
               duration=report.duration, longrepr=report.longreprtext if report.failed else None)
    with Path(os.environ['TICKET24RESUME_REPORTS']).open('a') as stream:
        stream.write(json.dumps(row) + '\n')
    if report.failed:
        print('\nRetained failure: ' + report.nodeid + '\n' + report.longreprtext, flush=True)
