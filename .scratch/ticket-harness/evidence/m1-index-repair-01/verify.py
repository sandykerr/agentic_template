"""Capture exact-source commands without replaying historical evidence writers."""
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/panfs/ccds02/nobackup/people/ajkerr1/agentic_template/agentic_template')
OUT = ROOT / '.scratch/ticket-harness/evidence/m1-index-repair-01'
OUT.mkdir(parents=True, exist_ok=True)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def snapshot(name):
    paths = [*ROOT.glob('ticket_harness/*.py'), *ROOT.glob('tests/*.py'),
             *ROOT.glob('examples/**/*.py'), ROOT / 'pyproject.toml', ROOT / 'environment.yml',
             ROOT / 'requirements-uv.in', ROOT / 'requirements-uv.txt']
    instructions = [ROOT / 'AGENTS.md', ROOT / 'GLOSSARY.md',
                    *ROOT.glob('docs/agents/*.md'), *ROOT.glob('docs/adr/*.md'),
                    *ROOT.glob('docs/ticket-harness/*.md'), ROOT / 'docs/ticket-harness.md',
                    *ROOT.glob('.agents/**/SKILL.md'),
                    ROOT / '.scratch/ticket-harness/spec.md',
                    ROOT / '.scratch/ticket-harness/approval.md',
                    ROOT / '.scratch/ticket-harness/milestones.md',
                    ROOT / '.scratch/ticket-harness/handoff-m1-caller-index-repair-and-final-verification.md']
    value = {'head': git('rev-parse', 'HEAD'), 'status': git('status', '--short'),
             'python': sys.version, 'executable': sys.executable,
             'packages': {n: importlib.metadata.version(n) for n in ('pytest', 'mypy', 'ruff', 'PyYAML')},
             'source_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted(paths)},
             'instruction_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                    for p in sorted(set(instructions))}}
    (OUT / f'{name}.json').write_text(json.dumps(value, indent=2) + '\n')
    (OUT / f'{name}.patch').write_bytes(subprocess.check_output(['git', 'diff', 'HEAD', '--',
        'ticket_harness', 'tests', 'examples', 'pyproject.toml', 'environment.yml'], cwd=ROOT))
    return value


if sys.argv[1] == 'snapshot':
    snapshot(sys.argv[2])
else:
    label = sys.argv[1]
    command = sys.argv[2:]
    before = snapshot(label + '-source')
    environment = dict(os.environ)
    environment['PYTHONPATH'] = os.pathsep.join((str(ROOT), str(OUT)))
    started = time.monotonic()
    interrupted = False
    with (OUT / f'{label}.log').open('wb') as log:
        try:
            result = subprocess.run(command, cwd=ROOT, env=environment, stdout=log, stderr=subprocess.STDOUT)
            exit_code = result.returncode
        except KeyboardInterrupt:
            interrupted = True
            exit_code = 130
    after = snapshot(label + '-after')
    record = {'command': command, 'exit': exit_code, 'interrupted': interrupted,
              'seconds': time.monotonic() - started, 'source': label + '-source.json',
              'source_unchanged': before['source_sha256'] == after['source_sha256'],
              'log': label + '.log', 'PYTHONPATH': environment['PYTHONPATH'],
              'TMPDIR': environment.get('TMPDIR')}
    (OUT / f'{label}-result.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record), flush=True)
    print((OUT / f'{label}.log').read_text()[-12000:], flush=True)
    sys.exit(exit_code)
