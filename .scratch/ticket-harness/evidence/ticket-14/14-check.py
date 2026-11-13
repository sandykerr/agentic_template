import hashlib, json, os, subprocess, sys, time
from pathlib import Path
root = Path('/home/ajkerr1/development/agentic_template')
evidence = root / '.scratch/ticket-harness/evidence'
name = sys.argv[1]
command = sys.argv[2:]
paths = sorted([*root.glob('ticket_harness/*.py'), *root.glob('tests/*.py'), root/'docs/ticket-harness.md', root/'pyproject.toml'])
identity = {'baseline': 'd67c12d91495af00557b279d0bf0e1da518e6fcc', 'head': subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(), 'status': subprocess.check_output(['git','status','--short'],text=True), 'sha256': {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(evidence/f'14-{name}-source.json').write_text(json.dumps(identity,indent=2)+'\n')
env = dict(os.environ, PYTHONPATH='/tmp/ticket12-tools', TICKET_HARNESS_TEST_OBSERVATIONS=str(evidence/'14-observations'/name))
t = time.monotonic()
r = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env=env)
(evidence/f'14-{name}.log').write_text(r.stdout)
result = {'command':command,'exit_code':r.returncode,'seconds':round(time.monotonic()-t,3),'source_identity':f'14-{name}-source.json'}
(evidence/f'14-{name}-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(r.stdout); print(json.dumps(result))
sys.exit(r.returncode)
