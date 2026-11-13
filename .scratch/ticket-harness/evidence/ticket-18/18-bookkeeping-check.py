"""Read-only ticket 18 reconciliation and optional next handoff checks."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / '.scratch/ticket-harness'
EVIDENCE = FEATURE / 'evidence'
SOURCE = '816aecbaa67f79ca5fd97c78f40593cdb007c45a'
TICKET = '.scratch/ticket-harness/issues/18-gate-development-on-cumulative-architecture-review.md'
MUTABLE = {TICKET, '.scratch/ticket-harness/README.md', '.scratch/ticket-harness/reviews/README.md', 'next_agent_prompt.md'}


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def criteria(text):
    return text.split('## Acceptance criteria\n', 1)[1].split('\n## Verification', 1)[0]


def main():
    before = git('show', SOURCE + ':' + TICKET)
    after = (ROOT / TICKET).read_text()
    assert criteria(before).replace('- [ ]', '- [x]') == criteria(after)
    assert criteria(after).count('- [x]') == 6 and '- [ ]' not in criteria(after)
    assert '**Status:** completed' in after
    assert 'Previous readiness: `ready-for-agent`' in after
    assert next(x for x in before.splitlines() if x.startswith('**Blocked by:**')) == next(x for x in after.splitlines() if x.startswith('**Blocked by:**'))
    index = (FEATURE / 'README.md').read_text()
    assert '20 remaining open tickets 19–38' in index
    assert 'nine completed 10–18 and six remaining 19–24' in index
    assert 'next eligible implementation ticket is 19, backed by completed 17 and 18' in index
    assert '| 16, 17 | completed | M1 |' in index
    assert '18-completion.md' in index
    for ref in [SOURCE, '3c8d4ab', '6b8dae9', '4814eab', '91e285f']:
        subprocess.run(['git', '-C', str(ROOT), 'merge-base', '--is-ancestor', ref, 'HEAD'], check=True)
    result = json.loads((EVIDENCE / '18-check-results.json').read_text())
    for name, digest in result['source_identities'].items():
        original = subprocess.check_output(['git', '-C', str(ROOT), 'show', SOURCE + ':' + name])
        assert sha(original) == digest, name
        if name not in MUTABLE:
            assert sha((ROOT / name).read_bytes()) == digest, name
    cap = json.loads((EVIDENCE / '18-review-capture.json').read_text())
    assert cap['assessed_source'] == SOURCE
    for name, digest in cap['sha256'].items():
        assert sha((EVIDENCE / name).read_bytes()) == digest, name
    # Existing reviewed artifacts remain unchanged; new review/bookkeeping files
    # belong only to this ticket. Never rerun result-writing historical helpers.
    changes = set(git('diff', '--name-only', SOURCE).splitlines())
    changes.update(git('ls-files', '--others', '--exclude-standard').splitlines())
    for name in changes:
        assert name in MUTABLE or name.startswith('.scratch/ticket-harness/evidence/18-') or name == '.scratch/ticket-harness/reviews/ticket-18.md', name
        if name not in MUTABLE:
            assert not git('ls-tree', SOURCE, '--', name), ('changed reviewed artifact', name)
    docs = [ROOT / TICKET, FEATURE / 'README.md', FEATURE / 'reviews/README.md', FEATURE / 'reviews/ticket-18.md', EVIDENCE / '18-completion.md', EVIDENCE / '18-review-spec.md', EVIDENCE / '18-review-standards.md']
    selected = None
    handoff = ROOT / 'next_agent_prompt.md'
    if handoff.read_text().startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/19-'):
        docs.append(handoff)
        selected = 19
        assert '**Status:** ready-for-agent' in next((FEATURE / 'issues').glob('19-*.md')).read_text()
        assert 'architecture-checkpoints.md' in handoff.read_text()
        assert '19–24' in handoff.read_text()
        assert 'M1' in handoff.read_text()
    anchors = runpy.run_path(str(EVIDENCE / '16-check.py'))['anchors']
    count = 0
    for path in docs:
        content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
        content = re.sub(r'`[^`\n]+`', '', content)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', content):
            if re.match(r'[a-z]+://', href):
                continue
            name, _, fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$', '', name)
            target = (path.parent / name).resolve() if name else path
            assert target.exists(), (path, href)
            if fragment:
                assert fragment in anchors(target), (path, href)
            count += 1
    subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', SOURCE], check=True)
    print(json.dumps({'result': 'pass', 'reviewed_source': SOURCE, 'criteria': 6, 'criterion_wording_dependencies_preserved': True, 'reviewed_implementation_and_original_reports_preserved': True, 'local_links': count, 'handoff_selected': selected}, indent=2))


if __name__ == '__main__':
    main()
