"""Read-only validation of ticket-16 bookkeeping and generated handoff links."""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess

root = Path('.scratch/ticket-harness')
evidence = root / 'evidence'
helper = runpy.run_path(str(evidence / '16-check.py'))
paths = [root / 'README.md', root / 'reviews/README.md', root / 'reviews/ticket-16.md', root / 'issues/16-record-review-work-findings-and-decisions.md', evidence / '16-completion.md', evidence / '16-review-spec.md', evidence / '16-review-standards.md']
if Path('next_agent_prompt.md').read_text().startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/17-'):
    paths.append(Path('next_agent_prompt.md'))
links = helper['links']([p.resolve() for p in paths])
for name, digest in json.loads((evidence / '16-review-capture.json').read_text())['sha256'].items():
    assert hashlib.sha256((evidence / name).read_bytes()).hexdigest() == digest, name
path = str(root / 'issues/16-record-review-work-findings-and-decisions.md')
before = subprocess.check_output(['git', 'show', '3c8d4ab:' + path], text=True)
after = Path(path).read_text()
criteria_before = before.split('## Acceptance criteria\n')[1].split('\n## Verification')[0]
criteria_after = after.split('## Acceptance criteria\n')[1].split('\n## Verification')[0]
assert criteria_before.replace('- [ ]', '- [x]') == criteria_after
assert criteria_after.count('- [x]') == 6 and '**Status:** completed' in after
assert next(x for x in before.splitlines() if x.startswith('**Blocked by:**')) == next(x for x in after.splitlines() if x.startswith('**Blocked by:**'))
assert '| 10, 11 | completed | M1 |' in (root / 'README.md').read_text()
for ref in ['3c8d4ab', '70a0122', 'fe036e3', '552fcd6', 'bb982c0']:
    subprocess.run(['git', 'merge-base', '--is-ancestor', ref, 'HEAD'], check=True)
print(json.dumps({'result': 'PASS', 'local_links': len(links), 'criteria': 6, 'wording_dependencies_preserved': True, 'original_reports_digest_match': True, 'implementation_and_prerequisite_ancestry': True}, indent=2))
