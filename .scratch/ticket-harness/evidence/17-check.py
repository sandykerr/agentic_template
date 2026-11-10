"""Read-only document/identity audit for ticket17; writes only its result JSON."""
from pathlib import Path
import hashlib
import gzip
import json
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[3]
EVIDENCE = ROOT / '.scratch/ticket-harness/evidence'
WALK = EVIDENCE / '17-walkthroughs'
BASELINE = 'c82b15f504c29a69e8fb708e10568574150e80d3'
CHANGED_DOCS = [
    '.agents/skills/custom/create-next-agent-prompt/SKILL.md',
    '.agents/skills/custom/implement-with-checkboxes/SKILL.md',
    '.agents/skills/custom/references/planning.md',
    '.agents/skills/custom/review-architecture/SKILL.md',
    'docs/agents/ownership-review.md',
    'docs/agents/review-records.md',
    'docs/templates/reviews/report.md',
    'docs/ticket-harness.md',
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', '-C', str(cwd), *args], text=True).strip()


def main():
    result_path = EVIDENCE / '17-check-results.json'
    if not result_path.exists():
        result_path.write_text(json.dumps({'result': 'pending; audit not complete'}) + '\n')
    paths = [ROOT / p for p in CHANGED_DOCS]
    paths += [EVIDENCE / '17-implementation-report.md', WALK / 'README.md']
    paths += sorted(WALK.glob('case-*/candidate/CONTRACT.md'))
    paths += sorted(WALK.glob('case-*/baseline/CONTRACT.md'))
    paths += sorted(WALK.glob('case-*/*.md'))
    # Reuse the landed link/anchor parser, never its builder/main.
    audit = runpy.run_path(str(EVIDENCE / '16-check.py'))['links']
    observations = audit(paths)
    for path in paths:
        assert '{{' not in path.read_text() or path.name == 'report.md', path
    routing = {
        '.agents/skills/custom/grill-to-tickets/SKILL.md': ['../references/planning.md'],
        '.agents/skills/custom/references/planning.md': ['docs/agents/ownership-review.md#planning-and-implementation'],
        '.agents/skills/custom/implement-with-checkboxes/SKILL.md': ['docs/agents/ownership-review.md', 'under-400-word'],
        '.agents/skills/custom/create-next-agent-prompt/SKILL.md': ['docs/agents/ownership-review.md#repair-and-handoff'],
        '.agents/skills/custom/review-architecture/SKILL.md': ['docs/agents/ownership-review.md'],
        'docs/agents/review-records.md': ['ownership-review.md'],
        'docs/templates/reviews/report.md': ['ownership-review.md#report-substantive-reasoning'],
    }
    for name, targets in routing.items():
        for target in targets:
            assert target in (ROOT / name).read_text(), (name, target)
    tracked_changes = git('diff', '--name-only', BASELINE).splitlines()
    untracked = git('ls-files', '--others', '--exclude-standard').splitlines()
    for name in tracked_changes + untracked:
        assert name in CHANGED_DOCS or name.startswith('.scratch/ticket-harness/evidence/17-'), name
    # Every historical/approved file outside the explicit doc changes is unchanged.
    protected = git('ls-tree', '-r', '--name-only', BASELINE, '.scratch', '.agents/skills/matt-pocock', '.agents/skills/microsoft', 'ticket_harness', 'tests', 'examples', 'next_agent_prompt.md').splitlines()
    for name in protected:
        assert (ROOT / name).read_bytes() == subprocess.check_output(['git', 'show', f'{BASELINE}:{name}'], cwd=ROOT), name
    cases = json.loads((WALK / 'sources.json').read_text())
    reports = {}
    for row in cases:
        dest = WALK / row['case']
        for name, identity in row['files'].items():
            assert sha(dest / name) == identity, (row['case'], name)
        repo = Path(row['repo'])
        assert git('rev-parse', 'HEAD', cwd=repo) == row['candidate']
        assert not git('status', '--porcelain', cwd=repo)
        git('bundle', 'verify', str(dest / 'source.bundle'), cwd=repo)
        for label, revision in [('baseline', row['baseline']), ('candidate', row['candidate'])]:
            for path in (dest / label).iterdir():
                assert path.read_bytes() == subprocess.check_output(['git', 'show', f'{revision}:{path.name}'], cwd=repo), path
        assignment = json.loads((dest / 'assignment.json').read_text())
        assert assignment['fork_turns'] == 'none' and assignment['reasoning_effort'] == 'high'
        assert assignment['message'] + '\n' == (dest / 'assignment.txt').read_text()
        raw = dest / 'report.md'
        assert raw.is_file() and raw.stat().st_size > 0
        reports[row['case']] = {'display_sha256': sha(raw), 'assignment_sha256': sha(dest / 'assignment.json')}
    capture = json.loads((WALK / 'capture.json').read_text())
    for row in capture['outputs']:
        raw_path = WALK / row['retained_raw']
        raw_bytes = gzip.decompress(raw_path.read_bytes()) if row['encoding'] == 'gzip' else raw_path.read_bytes()
        assert hashlib.sha256(raw_bytes).hexdigest() == row['original_sha256'], row
        assert sha(raw_path) == row['artifact_sha256'], row
    for original, row in json.loads((WALK / 'guidance-identities.json').read_text()).items():
        snap = WALK / 'guidance' / Path(row['snapshot']).name
        assert sha(snap) == row['sha256'] == sha(ROOT / original), original
    result = {'result': 'pass', 'head': git('rev-parse', 'HEAD'), 'original_baseline': BASELINE,
              'tracked_changes': tracked_changes, 'untracked': untracked,
              'source_identities': {str(p.relative_to(ROOT)): sha(p) for p in paths + [Path(__file__).resolve(), EVIDENCE / '17-run-checks.sh']},
              'links': len(observations), 'routing': routing, 'protected_files': len(protected),
              'reports': reports, 'scope': 'standalone docs/skills; no runtime suite required'}
    (EVIDENCE / '17-check-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['result', 'links', 'protected_files', 'reports']}, indent=2))


if __name__ == '__main__':
    main()
