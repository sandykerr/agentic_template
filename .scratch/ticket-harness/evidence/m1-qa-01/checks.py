from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

out=Path(__file__).resolve().parent
start=json.loads((out/'start.json').read_text())
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in start['source_files'].items())
commands=[
 [sys.executable,'-m','pytest','-q',
  'tests/test_preflight.py::test_missing_acceptance_requirements_rejects_before_any_execution',
  'tests/test_cli.py::TicketCycleTests::test_failed_baseline_is_environment_failure_without_an_assignment',
  'tests/test_continuation.py::test_continued_run_records_invalidation_of_earlier_verified_source'],
]
env=dict(os.environ,TICKET_HARNESS_TEST_OBSERVATIONS=str(out/'current-observations'))
results=[]
for i,argv in enumerate(commands):
    before=time.monotonic()
    with (out/f'check-{i}.log').open('w') as stream:
        result=subprocess.run(argv,env=env,stdout=stream,stderr=subprocess.STDOUT)
    results.append(dict(command=argv,exit=result.returncode,seconds=time.monotonic()-before,log=f'check-{i}.log',actual_source=start['starting_head'],source_manifest='start.json'))
    print(json.dumps(results[-1]),flush=True)
    (out/'check-results.json').write_text(json.dumps(results,indent=2)+'\n')
    if result.returncode:
        sys.exit(result.returncode)
