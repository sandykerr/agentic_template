"""Read-only checks for ticket 17 completion records and optional ticket 18 handoff."""
import gzip
import hashlib
import json
from pathlib import Path
import runpy
import subprocess

ROOT = Path.cwd()
FEATURE = ROOT / '.scratch/ticket-harness'
EVIDENCE = FEATURE / 'evidence'
SOURCE = '4814eabd4bf2f196f7fb6915667c4305b7c2d0b9'
TICKET = '.scratch/ticket-harness/issues/17-review-ownership-across-affected-modules.md'


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


before = git('show', SOURCE + ':' + TICKET)
after = (ROOT / TICKET).read_text()
def criteria(text):
    return text.split('## Acceptance criteria\n', 1)[1].split('\n## Verification', 1)[0]

assert criteria(before).replace('- [ ]', '- [x]') == criteria(after)
assert criteria(after).count('- [x]') == 6
assert '**Status:** completed' in after and 'Previous readiness: `ready-for-agent`' in after
assert next(x for x in before.splitlines() if x.startswith('**Blocked by:**')) == next(x for x in after.splitlines() if x.startswith('**Blocked by:**'))
index = (FEATURE / 'README.md').read_text()
assert '21 remaining open tickets 18–38' in index
assert 'eight completed 10–17 and seven remaining 18–24' in index
assert '| 16 | completed | M1 |' in index and 'next eligible implementation ticket is 18' in index
for ref in [SOURCE, '3c8d4ab', '6b8dae9']:
    subprocess.run(['git', 'merge-base', '--is-ancestor', ref, 'HEAD'], check=True)
for name, digest in json.loads((EVIDENCE / '17-check-results.json').read_text())['source_identities'].items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
for name, digest in json.loads((EVIDENCE / '17-review-capture.json').read_text())['sha256'].items():
    assert hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest() == digest, name
for assignment in json.loads((EVIDENCE / '17-review-capture.json').read_text())['assignments'].values():
    prompt = assignment['assignment.txt']
    raw = gzip.decompress((EVIDENCE / prompt['retained_raw']).read_bytes())
    assert hashlib.sha256(raw).hexdigest() == prompt['original_sha256']
    assert raw.rstrip(b'\n') + b'\n' == (EVIDENCE / prompt['retained']).read_bytes()
# Existing implementation/history remain byte-identical; only declared bookkeeping can change.
allowed = {TICKET, '.scratch/ticket-harness/README.md', '.scratch/ticket-harness/reviews/README.md', 'next_agent_prompt.md'}
for name in git('diff', '--name-only', SOURCE).splitlines():
    assert name in allowed or name.startswith('.scratch/ticket-harness/evidence/17-') or name == '.scratch/ticket-harness/reviews/ticket-17.md', name
    if git('ls-tree', SOURCE, '--', name) and name not in allowed:
        raise AssertionError(('changed reviewed implementation', name))
paths = [ROOT / TICKET, FEATURE / 'README.md', FEATURE / 'reviews/README.md', FEATURE / 'reviews/ticket-17.md', EVIDENCE / '17-completion.md', EVIDENCE / '17-review-spec.md', EVIDENCE / '17-review-standards.md']
handoff = ROOT / 'next_agent_prompt.md'
handoff_selected = None
if handoff.read_text().startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/18-'):
    paths.append(handoff)
    handoff_selected = 18
links = runpy.run_path(str(EVIDENCE / '16-check.py'))['links'](paths)
subprocess.run(['git', 'diff', '--check', SOURCE], check=True)
print(json.dumps({'result': 'pass', 'source': SOURCE, 'criteria': 6, 'wording_dependency_preserved': True, 'implementation_source_and_original_reports_unchanged': True, 'local_links': len(links), 'handoff_selected': handoff_selected}, indent=2))
