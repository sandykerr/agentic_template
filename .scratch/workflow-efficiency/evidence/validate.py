from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

root = Path('/home/ajkerr1/development/agentic_template')
out = root / '.scratch/workflow-efficiency/evidence'
validator = Path('/home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py')
commands = [[sys.executable, str(validator), str(root / '.agents/skills/custom' / name)]
            for name in ('implement-with-checkboxes', 'create-next-agent-prompt',
                         'evaluate-reviewers', 'test-strategy')]
commands += [[sys.executable, str(out / 'check.py')]]
commands += [['git', 'diff', '--check', '54acbaad0b101b9f1e13fd3d2e518eed1fd75fb5']]
results = []
attempt = sys.argv[1]
for i, command in enumerate(commands, 1):
    env = dict(os.environ)
    env.pop('PYTHONPATH', None)
    result = subprocess.run(command, cwd=root, capture_output=True, env=env)
    stem = f'validation-{attempt}-{i:02}'
    (out / f'{stem}.stdout').write_bytes(result.stdout)
    (out / f'{stem}.stderr').write_bytes(result.stderr)
    results.append({'command': command, 'cwd': str(root), 'exit': result.returncode,
                    'PYTHONPATH': env.get('PYTHONPATH'),
                    'stdout': f'{stem}.stdout', 'stderr': f'{stem}.stderr'})
    print(json.dumps({'command': command, 'exit': result.returncode,
                      'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}))
manifest = {'baseline': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
            'state': subprocess.check_output(['git', 'status', '--short'], cwd=root, text=True),
            'validator': {'path': str(validator), 'sha256': hashlib.sha256(validator.read_bytes()).hexdigest()},
            'commands': results,
            'limits': 'Document/skill checks only; no runtime or general decision-quality claim.'}
(out / f'validation-{attempt}.json').write_text(json.dumps(manifest, indent=2) + '\n')
sys.exit(int(any(r['exit'] for r in results)))
