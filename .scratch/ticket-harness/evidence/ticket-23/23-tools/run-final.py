"""Run required checks against a frozen source with retained commands, exits and raw fixtures."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

out = Path('.scratch/ticket-harness/evidence')
identity = json.loads((out / '23-final-source.json').read_text())
raw = Path('/tmp/ticket23-final-raw')
raw.mkdir(exist_ok=False)
env = dict(os.environ, PYTHONPATH=f"/tmp/ticket23-tools:{out / '23-tools'}", TICKET23_RAW=str(raw))
commands = [
    [sys.executable, '-m', 'pytest', '-q', '--durations=20', '-p', 'capture23'],
    [sys.executable, '-m', 'mypy'],
    [sys.executable, '-m', 'ruff', 'check', 'ticket_harness', 'tests', 'examples'],
    [sys.executable, '-m', 'ruff', 'format', '--check', 'ticket_harness', 'tests', 'examples'],
    ['git', 'diff', '--check'],
    ['git', 'diff', '--check', '851a855889b1ec99ae78ce415da1d66a3cf06687', '--', 'ticket_harness', 'tests', 'examples'],
]
results = []
for index, command in enumerate(commands):
    assert all(hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest for name, digest in identity['source_hashes'].items())
    start = time.time()
    log = out / f'23-final-check-{index}.log'
    with log.open('wb') as stream:
        result = subprocess.run(command, env=env, stdout=stream, stderr=subprocess.STDOUT)
    results.append(dict(command=command, exit=result.returncode, seconds=time.time()-start, log=str(log), source='23-final-source.json'))
    (out / '23-final-check-results.json').write_text(json.dumps(results, indent=2)+'\n')
    print(index, result.returncode, flush=True)
assert all(item['exit'] == 0 for item in results), results
