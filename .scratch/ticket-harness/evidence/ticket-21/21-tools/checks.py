"""Retain exact source, commands, output, exit and timing for required checks."""
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

root = Path.cwd()
out = root / '.scratch/ticket-harness/evidence'
python = str(root / '.micromamba/envs/dev/bin/python')
env = dict(os.environ, PYTHONPATH=f'/tmp/ticket20-tools:{root}/tests:{out}/21-tools', TICKET21_RAW='/tmp/ticket21-final-raw')
env.pop('TICKET_HARNESS_TEST_OBSERVATIONS', None)
files = sorted(list(root.glob('ticket_harness/*.py')) + list(root.glob('tests/*.py')) + list(root.glob('examples/**/*.py')) + [root / 'pyproject.toml', root / 'environment.yml'])
identity = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(out / '21-final-source.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(), 'files':identity, 'environment': {'PYTHONPATH': env['PYTHONPATH'], 'TICKET21_RAW': env['TICKET21_RAW'], 'python':subprocess.check_output([python,'--version'],env=env,text=True).strip(), 'mypy':subprocess.check_output([python,'-m','mypy','--version'],env=env,text=True).strip(), 'ruff':subprocess.check_output([python,'-m','ruff','--version'],env=env,text=True).strip()}, 'diff':subprocess.check_output(['git','diff','--','ticket_harness','tests','examples','pyproject.toml','environment.yml'],text=True)}, indent=2) + '\n')
checks = [
    [python,'-m','pytest','-q','--durations=20','-p','capture21'],
    [python,'-m','mypy'],
    [python,'-m','ruff','check','ticket_harness','tests','examples'],
    [python,'-m','ruff','format','--check','ticket_harness','tests','examples'],
    ['git','diff','--check'],
    ['git','diff','--check','8574c6e5fb0a55ea3539e52c7c53044f1c036583','--','ticket_harness','tests','examples'],
]
results=[]
for i, argv in enumerate(checks):
    logfile=out / f'21-final-check-{i}.log'
    started=time.monotonic()
    with logfile.open('w') as stream:
        stream.write(json.dumps({'command':argv, 'source':'21-final-source.json'})+'\n');stream.flush()
        result=subprocess.run(argv,env=env,stdout=stream,stderr=subprocess.STDOUT)
    results.append({'command':argv,'exit_code':result.returncode,'seconds':time.monotonic()-started,'log':logfile.name})
    (out / '21-final-check-results.json').write_text(json.dumps({'source':'21-final-source.json','results':results},indent=2)+'\n')
    print(json.dumps(results[-1]),flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
assert identity == {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
