"""Audit ticket18 guidance/evidence; never rebuild or alter retained fixtures."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import runpy
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / '.scratch/ticket-harness/evidence'
WALK = EVIDENCE / '18-walkthrough'
BASE = '02d76205a1c40e45c607ef2a5d11ec282393edcd'
DOCS = [
    'docs/agents/architecture-checkpoints.md',
    'docs/agents/ownership-review.md',
    'docs/agents/review-records.md',
    'docs/agents/issue-tracker.md',
    'docs/templates/reviews/assessment.md',
    'docs/ticket-harness.md',
    '.agents/skills/custom/implement-with-checkboxes/SKILL.md',
    '.agents/skills/custom/create-next-agent-prompt/SKILL.md',
    '.agents/skills/custom/references/planning.md',
    '.scratch/ticket-harness/README.md',
    '.scratch/ticket-harness/milestones.md',
    '.scratch/ticket-harness/reviews/README.md',
]


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', '-C', str(cwd), *args], text=True).strip()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    anchors = runpy.run_path(str(EVIDENCE / '16-check.py'))['anchors']
    docs = [ROOT / p for p in DOCS] + sorted(WALK.rglob('*.md')) + [EVIDENCE / '18-implementation-report.md']
    links = []
    for p in docs:
        text = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', p.read_text(), flags=re.M | re.S)
        text = re.sub(r'`[^`\n]+`', '', text)
        for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
            if re.match(r'[a-z]+://', href):
                continue
            name, _, fragment = unquote(href).partition('#')
            name = re.sub(r':\d+$', '', name)
            target = (p.parent / name).resolve() if name else p
            assert target.exists(), (p, href)
            if fragment:
                assert fragment in anchors(target), (p, href)
            links.append({'from': str(p.relative_to(ROOT)), 'href': href})
    changes = git('diff', '--name-only', BASE).splitlines() + git('ls-files', '--others', '--exclude-standard').splitlines()
    for name in changes:
        assert name in DOCS or name.startswith('.scratch/ticket-harness/evidence/18-'), name
    # No upstream/runtime/approved ticket/frozen evidence change is permitted.
    protected = git('ls-tree', '-r', '--name-only', BASE, '.scratch', '.agents/skills/matt-pocock', '.agents/skills/microsoft', 'ticket_harness', 'tests', 'examples', 'next_agent_prompt.md').splitlines()
    assert not (set(protected) - set(DOCS)) & set(changes)
    routing = {}
    for name in DOCS:
        if name == 'docs/agents/architecture-checkpoints.md':
            continue
        content = (ROOT / name).read_text()
        assert 'architecture-checkpoints.md' in content, name
        routing[name] = 'shared checkpoint contract'
    sources = json.loads((WALK / 'sources.json').read_text())
    with tempfile.TemporaryDirectory(prefix='18-source-audit-') as temp:
        git('clone', '--quiet', '--no-checkout', str(WALK / 'source.bundle'), temp)
        for label, row in sources.items():
            git('cat-file', '-e', row['source'] + '^{commit}', cwd=Path(temp))
            inventory = git('ls-tree', '-r', '--name-only', row['source'], cwd=Path(temp)).splitlines()
            assert set(inventory) == set(row['files'])
            for name, digest in row['files'].items():
                p = WALK / label / name
                assert sha(p) == digest
                assert p.read_bytes() == subprocess.check_output(['git', '-C', temp, 'show', row['source'] + ':' + name])
        assert git('rev-parse', 'refs/remotes/origin/integration', cwd=Path(temp)) == sources['ticket-b']['source']
        assert len([p for p in sources['risk']['files'] if p.startswith('ticket_harness/') and p.endswith('.py')]) == 5
    reports = json.loads((WALK / 'capture.json').read_text())
    for name, digest in reports['sha256'].items():
        assert sha(WALK / name) == digest, name
    prefix = json.loads((WALK / 'history-prefix.json').read_text())
    assert hashlib.sha256((WALK / 'finding-history.md').read_bytes()[:prefix['bytes']]).hexdigest() == prefix['sha256']
    assignments = json.loads((WALK / 'assignments.json').read_text())['assignments']
    assert len(assignments) == 6
    for row in assignments:
        assert row['fork_turns'] == 'none' and row['reasoning_effort_argument'] == 'high'
        assert sha(WALK / row['prompt_snapshot']) == row['prompt_snapshot_sha256']
    for name, digest in json.loads((WALK / 'guidance-identities.json').read_text()).items():
        assert sha(Path(name)) == digest, name
    observations = json.loads((WALK / 'command-observations.json').read_text())
    assert [row['exit'] for row in observations] == [0, 0, 0, 1, 0, 0]
    # Explicit modeled guidance decisions remain separate from real runtime enforcement.
    outcomes = json.loads((WALK / 'readiness-observations.json').read_text())
    assert len(outcomes) >= 7 and all(row['kind'] == 'manual guidance walkthrough' for row in outcomes)
    assert any(row['outcome'] == 'blocked: stale assessed source' for row in outcomes)
    assert any(row['outcome'] == 'checkpoint clean; QA acceptance absent' for row in outcomes)
    real = json.loads((WALK / 'real-package-inventory.json').read_text())
    assert set(real['files']) == {str(p.relative_to(ROOT)) for p in (ROOT / 'ticket_harness').glob('*.py')}
    for name, digest in real['files'].items():
        assert sha(ROOT / name) == digest
    result = {'result': 'pass', 'baseline': BASE, 'head': git('rev-parse', 'HEAD'),
              'source_identities': {str(p.relative_to(ROOT)): sha(p) for p in [ROOT / n for n in DOCS] + [EVIDENCE / '18-implementation-report.md', Path(__file__).resolve(), EVIDENCE / '18-run-checks.sh']},
              'links': links, 'routing': routing, 'protected_files': len(set(protected) - set(DOCS)),
              'reports': reports, 'scope': 'standalone guidance; no runtime suite replay',
              'observations': len(observations), 'readiness_observations': len(outcomes)}
    (EVIDENCE / '18-check-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['result', 'protected_files', 'observations', 'readiness_observations']}, indent=2))
    print('Validated local links:', len(links))


if __name__ == '__main__':
    main()
