"""Validate resumed evidence and optionally bind it to committed source bytes."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import re

out = Path('.scratch/ticket-harness/evidence')
phase = sys.argv[1]
def read(name):
    return json.loads((out / name).read_text())
def sha(body):
    return hashlib.sha256(body).hexdigest()
freeze = read(f'24-repair2-{phase}-source.json')
assert freeze['baseline'] == 'ed017ae0c2b96769f31c710cfb4ff4708989b446'
assert freeze['head'] == '306cadedf6af3ec178db653992b257f3d4e27545'
prior = read('24-repair2-final-source.json')['source_hashes']
changed_source = {name for name, digest in freeze['source_hashes'].items() if prior[name] != digest}
assert changed_source == {'tests/test_milestones.py', 'tests/test_qa_promotion.py'}
commit = subprocess.check_output(['git', 'rev-parse', sys.argv[2]], text=True).strip() if len(sys.argv) > 2 else None
for name, digest in freeze['source_hashes'].items():
    assert sha(Path(name).read_bytes()) == digest, name
    if commit is not None:
        assert sha(subprocess.check_output(['git', 'show', commit + ':' + name])) == digest, name
capture_tools = {}
for name in ('identity.py', 'resume-checks.py', 'capture24repair2.py'):
    path = out / '24-repair2-tools' / name
    digest = sha(path.read_bytes())
    assert sha(subprocess.check_output(['git', 'show', freeze['head'] + ':' + str(path)])) == digest
    capture_tools[str(path)] = digest
for name, digest in read(f'24-repair2-{phase}-capture-tools.json').items():
    assert sha(Path(name).read_bytes()) == digest, name
    capture_tools[name] = digest
results = read(f'24-repair2-{phase}-check-results.json')
assert len(results) == 6 and all(row['exit'] == 0 for row in results)
assert '559 passed' in Path(results[0]['log']).read_text()
suite_archive = read(f'24-repair2-{phase}-audit.json')
assert suite_archive['scenarios'] == 559
assert sha(Path(suite_archive['archive']).read_bytes()) == suite_archive['archive_sha256']
reports = [json.loads(line) for line in (out / f'24-repair2-{phase}-pytest-reports.jsonl').read_text().splitlines()]
calls = [row for row in reports if row['when'] == 'call']
assert len(reports) == 1677 and len(calls) == 559
assert len({row['nodeid'] for row in calls}) == 559
assert all(row['outcome'] == 'passed' for row in reports)
for phase_name in ('resume-focused-green', 'resume-final-observer-green'):
    assert read(f'24-repair2-{phase_name}-source.json')['source_hashes'] == freeze['source_hashes']
trials = read('24-resume-trial-provenance.json')
trial_manifest = read('24-resume-trials-manifest.json')
assert sha(Path(trials['archive']).read_bytes()) == trials['archive_sha256']
trial_seen = set()
with tarfile.open(trials['archive'], 'r|gz') as stream:
    for member in stream:
        if member.isfile():
            body = stream.extractfile(member).read()
            assert len(body) == trial_manifest[member.name]['size']
            assert sha(body) == trial_manifest[member.name]['sha256']
            assert member.name not in trial_seen
            trial_seen.add(member.name)
assert trial_seen == set(trial_manifest)
for name, row in trials['logs'].items():
    assert sha(Path(name).read_bytes()) == row['display_sha256']
    assert trial_manifest[row['archive_member']]['sha256'] == row['original_sha256']
for number in (1, 2):
    for name, digest in read(f'24-review-round{number}-capture.json')['artifacts'].items():
        assert sha((out / name).read_bytes()) == digest, name
preserved = read('24-resume-display-provenance.json')
assert sha(Path(preserved['archive']).read_bytes()) == preserved['archive_sha256']
with tarfile.open(preserved['archive'], 'r:gz') as stream:
    for name, row in preserved['files'].items():
        assert sha(stream.extractfile(row['archive_member']).read()) == row['original_sha256'], name
        assert sha(Path(name).read_bytes()) == row['display_sha256'], name
        assert sha(subprocess.check_output(['git', 'show', freeze['head'] + ':' + name])) == row['original_sha256'], name
instructions = read('24-review-round1-instructions.json')['axis_additions']['standards'][0]
assert preserved['files'][instructions['path']]['original_sha256'] == instructions['sha256']
producer = read('24-checkpoint/producer.json')
consumer = read('24-resume-checkpoint/continuation-final.json')
producer_path = out / '24-checkpoint/producer.json'
assert sha(producer_path.read_bytes()) == sha(subprocess.check_output(['git', 'show', freeze['head'] + ':' + str(producer_path)]))
stopped_archive = out / '24-checkpoint/stopped-live.tar.gz'
assert sha(stopped_archive.read_bytes()) == read('24-checkpoint/audit.json')['archives']['stopped-live.tar.gz']['sha256']
assert read('24-resume-checkpoint/restore.json')['archive_sha256'] == sha(stopped_archive.read_bytes())
for name, digest in producer['source_hashes'].items():
    assert sha(subprocess.check_output(['git', 'show', freeze['baseline'] + ':' + name])) == digest, name
for name, digest in consumer['consumer_hashes'].items():
    assert freeze['source_hashes'][name] == digest, name
assert consumer['final']['outcome'] == 'completed'
assert consumer['final']['attempts'][:len(producer['record']['attempts'])] == producer['record']['attempts']
assert consumer['final']['gates'][:len(producer['record']['gates'])] == producer['record']['gates']
assert sum(gate['stage'] == 'baseline' for gate in consumer['final']['gates']) == 1
assert len(consumer['final']['qa_decisions']) == 2
assert all(row['exit'] == 0 for row in read('24-resume-checkpoint-checks.json'))
manifest = read('24-resume-checkpoint/archive-manifest.json')
checkpoint_archive = out / '24-resume-checkpoint/continued-final-live.tar.gz'
seen = set()
with tarfile.open(checkpoint_archive, 'r|gz') as stream:
    for member in stream:
        if member.isfile():
            # The original archive uses the single live fixture home as its root.
            name = member.name.split('/', 2)[2]
            body = stream.extractfile(member).read()
            assert name not in seen
            assert len(body) == manifest[name]['size'], name
            assert sha(body) == manifest[name]['sha256'], name
            seen.add(name)
assert seen == set(manifest)
assert sha(checkpoint_archive.read_bytes()) == read('24-resume-checkpoint/audit.json')['archive_sha256']
start = read('24-resume-start-audit.json')
for name, digest in (start['unrelated_tracked_changes'] | start['unrelated_archive_files']).items():
    assert (sha(Path(name).read_bytes()) if Path(name).exists() else None) == digest, name
assert read('24-repair2-interruption.json')['required_final']['exit'] == 130
assert read('24-repair2-focused-raw-audit.json')['exit'] == 130
for document in ('24-resume-diagnosis.md', '24-resume-review-packet.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', (out / document).read_text()):
        if not target.startswith(('http:', 'https:', '#')):
            assert (out / target.split('#')[0]).exists(), (document, target)
for path in (out / '24-repair2-tools').glob('*.py'):
    ast.parse(path.read_text(), filename=str(path))
summary = dict(commit=commit, commit_binding_pending=commit is None, fixed_baseline=freeze['baseline'], starting_head=freeze['head'], source_identities=len(freeze['source_hashes']), source_matches_worktree=True, source_matches_commit=commit is not None, changed_source_since_pause=sorted(changed_source), capture_tool_identities=capture_tools, six_required_gates_pass=True, raw_archive_scenarios=559, pytest_phase_reports=len(reports), old_producer_identities=len(producer['source_hashes']), consumer_identities=len(consumer['consumer_hashes']), compatibility_archive_readback_files=len(seen), original_reports_unchanged=True, immutable_original_display_files=len(preserved['files']), original_instruction_digest_preserved=True, unrelated_tracked_changes=len(start['unrelated_tracked_changes']), unrelated_archive_files=len(start['unrelated_archive_files']), full_suite_log_sha256=sha(Path(results[0]['log']).read_bytes()), checks=f'24-repair2-{phase}-check-results.json', scope='mechanical preparation only; no independent source review, finding closure or ticket/milestone acceptance')
name = f'24-repair2-{phase}-committed-source.json' if len(sys.argv) > 2 else f'24-repair2-{phase}-validation.json'
(out / name).write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
