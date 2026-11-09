"""Verify ticket-12 bookkeeping without changing implementation or running runtime work."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[3]
evidence = root / '.scratch/ticket-harness/evidence'
baseline = '2e15004338b45d61719656de113c2cbfdea56345'
implementation = '14cafef40726eba80d8648d98d9c263fde3a5d0b'
ticket = root / '.scratch/ticket-harness/issues/12-execute-only-the-current-qa-milestone.md'
relative = str(ticket.relative_to(root))
original = subprocess.check_output(['git', 'show', f'{baseline}:{relative}'], cwd=root, text=True)
current = ticket.read_text()
def criteria(text):
    return text.split('## Acceptance criteria', 1)[1].split('\n## ', 1)[0].strip()
assert criteria(original).replace('- [ ]', '- [x]') == criteria(current)
assert criteria(current).count('- [x]') == 5 and '- [ ]' not in criteria(current)
assert '**Status:** completed' in current and 'Previous readiness: `ready-for-agent`' in current
assert next(x for x in original.splitlines() if x.startswith('**Blocked by:**')) == next(x for x in current.splitlines() if x.startswith('**Blocked by:**'))
assert '## Comments' in current and implementation in current
index = (root / '.scratch/ticket-harness/README.md').read_text()
assert '**16 open tickets (13–28)**' in index and 'next eligible ticket is **13**' in index
assert '[12: Execute only the first eligible milestone — completed](evidence/12-completion.md)' in index
assert 'M1 has not been accepted.' in index
identity = json.loads((evidence / '12-final-source-identity.json').read_text())
for name, expected in identity['sha256'].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected
    assert hashlib.sha256(subprocess.check_output(['git', 'show', f'{implementation}:{name}'], cwd=root)).hexdigest() == expected
observations = json.loads((evidence / '12-fixture-observations.json').read_text())
assert observations['implementation_commit'] == implementation
assert observations['review_baseline'] == baseline
assert observations['scenario_count'] == len(observations['scenarios']) == 78
assert all(c['exit_code'] == 0 for c in observations['final_check_results'])
for axis in ('spec', 'standards'):
    report = (evidence / f'12-review-{axis}.md').read_text()
    assert implementation in report and baseline in report
assert hashlib.sha256((root / 'docs/agents/issue-tracker.md').read_bytes()).hexdigest() == '3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce'
assert (root / '.scratch/ticket-harness/milestones.md').read_bytes() == subprocess.check_output(['git', 'show', f'{baseline}:.scratch/ticket-harness/milestones.md'], cwd=root)
files = [ticket, root / '.scratch/ticket-harness/README.md', evidence / '12-completion.md', evidence / '12-coverage-map.md', evidence / '12-review-spec.md', evidence / '12-review-standards.md']
if '--handoff' in __import__('sys').argv:
    files.append(root / 'next_agent_prompt.md')
links = 0
for file in files:
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', file.read_text()):
        if '://' in target or target.startswith('mailto:'):
            continue
        path, _, anchor = target.partition('#')
        resolved = (file.parent / path).resolve() if path else file
        assert resolved.exists(), (file, target)
        if anchor:
            headings = re.findall(r'^#{1,6}\s+(.+)$', resolved.read_text(), re.M)
            slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
            assert anchor in slugs, (file, target, slugs)
        links += 1
subprocess.run(['git', 'diff', '--check'], cwd=root, check=True)
print(f'PASS: five exact criteria; completed/prior readiness/dependency/comment/index agreement; 20 committed/current hashes; 78 final scenarios; separate reviews; unchanged milestone and tracker; {links} local links/anchors; whitespace')
