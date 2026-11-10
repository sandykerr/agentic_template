"""Retain focused preflight/dependency/milestone development observations."""
import hashlib
import json
import os
import subprocess
from pathlib import Path

root = Path.cwd()
out = root / '.scratch/ticket-harness/evidence'
python = str(root / '.micromamba/envs/dev/bin/python')
argv = [python, '-m', 'pytest', '-q', 'tests/test_preflight.py', 'tests/test_dependencies.py', 'tests/test_milestones.py', '-p', 'capture22']
env = dict(os.environ, PYTHONPATH=f'/tmp/ticket20-tools:{root}/tests:{out}/22-tools', TICKET22_RAW='/tmp/ticket22-focused-raw')
identity = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('ticket_harness', 'tests') for p in sorted(Path(folder).glob('*.py'))}
record = {'command': argv, 'source_hashes': identity, 'raw': '/tmp/ticket22-focused-raw'}
(out / '22-focused.json').write_text(json.dumps(record, indent=2) + '\n')
with (out / '22-focused.log').open('w') as stream:
    result = subprocess.run(argv, env=env, stdout=stream, stderr=subprocess.STDOUT)
record['exit_code'] = result.returncode
(out / '22-focused.json').write_text(json.dumps(record, indent=2) + '\n')
raise SystemExit(result.returncode)
