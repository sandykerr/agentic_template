from pathlib import Path
import hashlib
import json
import subprocess
import tarfile

root = Path.cwd()
out = root / '.scratch/ticket-harness/evidence/m1-qa-01'
def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
source = git('rev-parse', 'HEAD')
baseline = git('rev-parse', '1a623ba')
assert git('rev-parse', 'b09e324^') == baseline
assert git('diff', 'ab08f7f', source, '--', 'ticket_harness', 'tests', 'examples', 'pyproject.toml') == ''
paths = [Path(p) for p in git('ls-files', 'ticket_harness', 'tests', 'examples', 'pyproject.toml').splitlines()]
instructions = [Path(p) for p in [
    'AGENTS.md', 'GLOSSARY.md', '.scratch/ticket-harness/spec.md',
    '.scratch/ticket-harness/milestones.md', '.scratch/ticket-harness/approval.md',
    'docs/agents/domain.md', 'docs/agents/testing.md', 'docs/agents/python-environment.md',
    'docs/agents/architecture-checkpoints.md', 'docs/agents/ownership-review.md',
    'docs/agents/review-records.md', 'docs/agents/development-efficiency.md',
    'docs/agents/reviewer-evaluation.md', 'docs/ticket-harness.md',
    'docs/adr/0001-reusable-harness-and-local-integration.md',
    'docs/adr/0002-human-qa-gates-feature-promotion.md',
    '.agents/skills/microsoft/microsoft_oop/SKILL.md',
    '.agents/skills/matt-pocock/codebase-design/SKILL.md',
    '.agents/skills/custom/test-strategy/SKILL.md',
    '.agents/skills/custom/review-architecture/SKILL.md',
    'docs/templates/reviews/report.md']]
instructions += sorted(Path('.scratch/ticket-harness/issues').glob('*.md'))[:24]
start = {
    'starting_head': source, 'cumulative_baseline': baseline,
    'baseline_parent': git('rev-parse', baseline + '^'),
    'baseline_provenance': '1a623ba introduces original harness spec/tickets, GLOSSARY and ADR-0001; contains no ticket_harness package; direct parent of first implementation b09e324. Earlier 8e28f0b contains skills. No prior milestone accepted.',
    'source_unchanged_since_final_ticket24': git('rev-parse', 'ab08f7f'),
    'source_files': {str(p): digest(p) for p in paths},
    'instructions': {str(p): digest(p) for p in instructions},
    'preexisting_dirty_status': git('status', '--porcelain=v1', '--untracked-files=all'),
    'runtime_package_files': [str(p) for p in sorted(Path('ticket_harness').glob('*.py'))],
    'authority': 'Human requested beginning QA for ticket24, closing M1. Preparation/demonstration authorized; no human milestone acceptance or promotion of development checkout inferred.',
}
with (out / 'instruction-snapshot.tar.gz').open('xb') as raw:
    with tarfile.open(fileobj=raw, mode='w:gz') as archive:
        for p in instructions:
            archive.add(p, arcname=str(p), recursive=False)
start['instruction_archive_sha256'] = digest(out / 'instruction-snapshot.tar.gz')
(out / 'start.json').write_text(json.dumps(start, indent=2) + '\n')
print(json.dumps({'starting_head': source, 'baseline': baseline, 'package_files': len(start['runtime_package_files']), 'instruction_files':len(instructions)}))
