from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import runpy
import subprocess

ROOT = Path('/home/ajkerr1/development/agentic_template')
BASE = '54acbaad0b101b9f1e13fd3d2e518eed1fd75fb5'
FILES = [
    'docs/agents/development-efficiency.md',
    '.agents/skills/custom/implement-with-checkboxes/SKILL.md',
    '.agents/skills/custom/create-next-agent-prompt/SKILL.md',
    '.agents/skills/custom/evaluate-reviewers/SKILL.md',
    '.agents/skills/custom/test-strategy/SKILL.md',
    '.agents/skills/custom/references/planning.md',
    'next_agent_prompt.md',
    'environment.yml',
]

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()

def main():
    changes = set(git('diff', '--name-only', BASE).splitlines())
    changes.update(git('ls-files', '--others', '--exclude-standard').splitlines())
    assert all(n in FILES or n.startswith('.scratch/workflow-efficiency/') for n in changes), changes
    old_paths = set(git('ls-tree', '-r', '--name-only', BASE).splitlines())
    assert not ((old_paths - set(FILES)) & changes), 'changed protected source'
    before = git('show', BASE + ':next_agent_prompt.md')
    current = (ROOT / 'next_agent_prompt.md').read_text().strip()
    insertion = '''Before requesting review or another repair round, apply
[efficient ticket development](docs/agents/development-efficiency.md). Finish local
checks/capture with the current worker, supply canonical evidence, and collect both
reports before a fresh repair. Investigate repeated failure causes before another
dispatch. Required fresh axes, final-source gates and human boundaries still apply;
this ordinary implementation ticket does not create calibration examples.

'''
    assert current.replace(insertion, '') == before, 'changed handoff beyond preparation pointer'
    assert current.startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/20-')
    anchors = runpy.run_path(str(ROOT / '.scratch/ticket-harness/evidence/16-check.py'))['anchors']
    links = 0
    for name in FILES:
        path = ROOT / name
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
        text = re.sub(r'`[^`\n]+`', '', text)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            if re.match(r'[a-z]+://', href):
                continue
            target, _, fragment = unquote(href).partition('#')
            target = re.sub(r':\d+$', '', target)
            resolved = (path.parent / target).resolve() if target else path
            assert resolved.exists(), (name, href)
            if fragment:
                assert fragment in anchors(resolved), (name, href)
            links += 1
    # Check routing/identity separately from independent substantive assessment.
    for name in FILES[1:-1]:
        assert 'development-efficiency.md' in (ROOT / name).read_text(), name
    subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', BASE], check=True)
    print(json.dumps({'result': 'pass', 'baseline': BASE,
                     'source_sha256': {n: hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in FILES},
                     'local_links': links, 'protected_previous_paths': len(old_paths-set(FILES)),
                     'historical_ticket19_and_runtime_unchanged': True,
                     'handoff_selection': 20, 'handoff_only_adds_preparation_routing': True,
                     'limits': 'Mechanical identity/link/protection facts; not reviewer judgment or measured speed improvement.'}, indent=2))

if __name__ == '__main__':
    main()
