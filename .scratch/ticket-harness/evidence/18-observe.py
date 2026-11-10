"""Collect isolated source observations; does not implement runtime review gates."""
from pathlib import Path
import json
import subprocess
import sys

walk = Path(__file__).resolve().parent / '18-walkthrough'
results = []
for name in ['ticket-a', 'ticket-b', 'risk', 'clean']:
    source = walk / name
    command = [sys.executable, '-B', str(source / 'observe.py')]
    run = subprocess.run(command, cwd=source, text=True, capture_output=True)
    results.append({'scenario': name + '-local-checks', 'command': command, 'exit': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
    assert run.returncode == 0
    if name in ['risk', 'clean']:
        command = [sys.executable, '-B', str(walk / 'observe-risk.py')]
        run = subprocess.run(command, cwd=source, env={'PYTHONPATH': str(source)}, text=True, capture_output=True)
        results.append({'scenario': name + '-cumulative-revocation', 'command': command, 'PYTHONPATH': str(source), 'exit': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
        assert run.returncode == (1 if name == 'risk' else 0), run.stderr
(walk / 'command-observations.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
