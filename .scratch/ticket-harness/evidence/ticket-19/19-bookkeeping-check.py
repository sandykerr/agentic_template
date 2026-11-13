"""Read-only reconciliation of ticket 19; never rerun historical evidence writers."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import runpy
import subprocess

ROOT = Path('/home/ajkerr1/development/agentic_template')
FEATURE = ROOT / '.scratch/ticket-harness'
EV = FEATURE / 'evidence'
SOURCE = '8e2c82679a2314e31ebff69accab3743f55f996d'
TICKET = '.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md'
MUTABLE = {TICKET, '.scratch/ticket-harness/README.md', '.scratch/ticket-harness/reviews/README.md', 'next_agent_prompt.md', '.scratch/ticket-harness/reviews/ticket-19.md', '.scratch/ticket-harness/evidence/19-finding-history.md'}

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
    assert '19 remaining open tickets 20–38' in index
    assert 'ten completed 10–19 and five remaining 20–24' in index
    assert 'next eligible implementation ticket is 20, backed by completed 05, 06 and 19' in index
    assert '| 17, 18 | completed | M1 |' in index
    assert '19-completion.md' in index
    for commit in (SOURCE, '34a49b7', '2a454df', 'dc1018e', '4ed073d'):
        subprocess.run(['git', '-C', str(ROOT), 'merge-base', '--is-ancestor', commit, 'HEAD'], check=True)
    result = json.loads((EV / '19-repair-c5-check-results-20261110T180103445335Z.json').read_text())
    identities = {}
    for group in ('checked_document_sha256', 'current_evidence_sha256'):
        identities.update(result[group])
    for group in ('helper_sha256',):
        identities.update({'.scratch/ticket-harness/evidence/' + k: v for k, v in result[group].items()})
    for name, digest in identities.items():
        original = subprocess.check_output(['git', '-C', str(ROOT), 'show', SOURCE + ':' + name])
        assert sha(original) == digest, name
        if name not in MUTABLE:
            assert sha((ROOT / name).read_bytes()) == digest, ('reviewed artifact changed', name)
    capture_maps = []
    for filename in ('19-review-capture.json', '19-review-round2-capture.json', '19-review-round3-capture.json'):
        capture = json.loads((EV / filename).read_text())
        if filename == '19-review-round3-capture.json':
            assert capture['assessed_source'] == SOURCE
        for name, digest in capture['sha256'].items():
            assert sha((EV / name).read_bytes()) == digest, name
        capture_maps.extend(capture['capture_mapping'])
    original_history = subprocess.check_output(['git', '-C', str(ROOT), 'show', SOURCE + ':.scratch/ticket-harness/evidence/19-finding-history.md'], text=True)
    assert (EV / '19-finding-history.md').read_text().startswith(original_history)
    original_assessment = subprocess.check_output(['git', '-C', str(ROOT), 'show', SOURCE + ':.scratch/ticket-harness/reviews/ticket-19.md'], text=True)
    assert original_assessment.split('## Assessment history\n', 1)[1] in (FEATURE / 'reviews/ticket-19.md').read_text()
    changes = set(git('diff', '--name-only', SOURCE).splitlines())
    changes.update(git('ls-files', '--others', '--exclude-standard').splitlines())
    for name in changes:
        assert name in MUTABLE or name.startswith('.scratch/ticket-harness/evidence/19-') or name == '.scratch/ticket-harness/reviews/ticket-19.md', name
        if name not in MUTABLE:
            assert not git('ls-tree', SOURCE, '--', name), ('changed reviewed source', name)
    docs = [ROOT / TICKET, FEATURE / 'README.md', FEATURE / 'reviews/README.md', FEATURE / 'reviews/ticket-19.md', EV / '19-completion.md', EV / '19-finding-history.md', EV / '19-review-navigation.md', EV / '19-review-spec-03.md', EV / '19-review-standards-03.md']
    selected = None
    handoff = ROOT / 'next_agent_prompt.md'
    if handoff.read_text().startswith('Use $implement-with-checkboxes to implement only:\n`.scratch/ticket-harness/issues/20-'):
        selected = 20
        docs.append(handoff)
        selected_text = next((FEATURE / 'issues').glob('20-*.md')).read_text()
        assert '**Status:** ready-for-agent' in selected_text
        for required in ('reviewer-evaluation.md', 'architecture-checkpoints.md', 'G2', 'C5', '20–24', 'M1'):
            assert required in handoff.read_text(), required
        for number in ('05', '06', '19'):
            assert f'{number}-completion.md' in handoff.read_text(), number
    anchors = runpy.run_path(str(EV / '16-check.py'))['anchors']
    count = 0
    by_original = {row['original_path']: EV / row['retained_path'] for row in capture_maps}
    by_retained = {str(EV / row['retained_path']): Path(row['original_path']) for row in capture_maps}
    for path in docs:
        content = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', path.read_text(), flags=re.M | re.S)
        content = re.sub(r'`[^`\n]+`', '', content)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', content):
            if re.match(r'[a-z]+://', href):
                continue
            name, _, fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$', '', name)
            target = (path.parent / name).resolve() if name else path
            if str(path) in by_retained:
                origin = by_retained[str(path)]
                original_target = (origin.parent / name).resolve() if name else origin
                target = by_original.get(str(original_target), target)
            assert target.exists(), (path, href)
            if fragment:
                assert fragment in anchors(target), (path, href)
            count += 1
    subprocess.run(['git', '-C', str(ROOT), 'diff', '--check', SOURCE], check=True)
    print(json.dumps({'result': 'pass', 'reviewed_source': SOURCE, 'criteria': 6, 'criterion_wording_dependencies_preserved': True, 'reviewed_identities': len(identities), 'reviewed_implementation_and_original_reports_preserved': True, 'local_links': count, 'handoff_selected': selected}, indent=2))

if __name__ == '__main__':
    main()
