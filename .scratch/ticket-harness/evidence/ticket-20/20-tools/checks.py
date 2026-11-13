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
env = dict(os.environ, PYTHONPATH=f'/tmp/ticket20-tools:{root}/tests:{out}/20-tools', TICKET20_RAW='/tmp/ticket20-final-raw')
env.pop('TICKET_HARNESS_TEST_OBSERVATIONS', None)
files = sorted(list(root.glob('ticket_harness/*.py')) + list(root.glob('tests/*.py')) + list(root.glob('examples/**/*.py')) + [root / 'pyproject.toml', root / 'environment.yml'])
identity = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(out / '20-final-source.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(), 'files':identity, 'diff':subprocess.check_output(['git','diff','--','ticket_harness','tests','examples','pyproject.toml','environment.yml'],text=True)}, indent=2) + '\n')
checks = [
    [python,'-m','pytest','-q','--durations=20','-p','capture20'],
    [python,'-m','mypy'],
    [python,'-m','ruff','check','ticket_harness','tests','examples'],
    [python,'-m','ruff','format','--check','ticket_harness','tests','examples'],
    ['git','diff','--check'],
    ['git','diff','--check','0d79d016907a03ce39d33c749523a8700e4233a4','--','ticket_harness','tests','examples'],
]
results=[]
for i, argv in enumerate(checks):
    logfile=out / f'20-final-check-{i}.log'
    started=time.monotonic()
    with logfile.open('w') as stream:
        stream.write(json.dumps({'command':argv, 'source':'20-final-source.json'})+'\n');stream.flush()
        result=subprocess.run(argv,env=env,stdout=stream,stderr=subprocess.STDOUT)
    results.append({'command':argv,'exit_code':result.returncode,'seconds':time.monotonic()-started,'log':logfile.name})
    (out / '20-final-check-results.json').write_text(json.dumps({'source':'20-final-source.json','results':results},indent=2)+'\n')
    print(json.dumps(results[-1]),flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
assert identity == {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
