"""Independent Spec evidence audit; reads renewed final captures only."""
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

root = Path.cwd()
evidence = root / '.scratch/ticket-harness/evidence'
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
baseline = '90255aaf6faf9aedce18f7159093f5dbfde294b7'
assert head == 'd11f0bc60a2c11c40683e58581dffa10e36a91be'
def sha(raw):
    return hashlib.sha256(raw).hexdigest()
def read(name):
    return json.loads((evidence / name).read_text())
def gitbytes(ref, path):
    return subprocess.check_output(['git', 'show', f'{ref}:{path}'])
identity = read('15-repair1-final-source-identity.json')
for name, expected in identity['sha256'].items():
    assert sha((root / name).read_bytes()) == expected
    assert sha(gitbytes(head, name)) == expected
checks = read('15-repair1-check-results.json')['checks']
for name, result in checks.items():
    assert result['exit_code'] == 0
    assert sha((evidence / result['log']).read_bytes()) == result['log_sha256']
    capture = read(result['source_identity'])
    assert capture['sha256'] == identity['sha256']
    standalone = read(result['source_identity'].replace('-source.json', '-result.json'))
    assert standalone['command'] == result['command']
    assert standalone['exit_code'] == result['exit_code']
assert '544 passed in 910.17s' in (evidence / checks['suite']['log']).read_text()
raw_hashes = read('15-repair1-raw-artifact-hashes.json')
for name, expected in raw_hashes.items():
    assert sha((evidence / name).read_bytes()) == expected, name
summary = read('15-repair1-fixture-observations.json')
assert summary['scenario_count'] == len(summary['observations']) == 123
raws = []
for item in summary['observations']:
    path = evidence / item['raw_file']
    raw = json.loads(path.read_text())
    assert sha(path.read_bytes()) == item['raw_sha256']
    assert raw['scenario'] == item['scenario']
    assert raw['record']['outcome'] == item['outcome']
    assert raw['record'].get('feature_complete') == item['feature_complete']
    assert raw['integration'] == item['integration']
    assert raw.get('development') == item['development']
    assert len(raw['record'].get('qa_decisions', [])) == item['consumed_decisions']
    if item['retained_run_files']:
        retained = evidence / item['retained_run_files']
        assert json.loads((retained / 'run.json').read_text()) == raw['record']
        for name, text in raw['outputs'].items():
            assert (retained / 'artifacts' / name).read_text() == text
        for name, text in raw['qa_artifacts'].items():
            assert (retained / name).read_text() == text
    raws.append(raw)
clean = next(r for r in raws if r['scenario'] == 'test_clean_qa_stop_continues_in_new_process_without_replaying_done_work')
r = clean['record']
assert [o['exit_code'] for o in clean['foreground_observations']] == [2, 0]
assert r['outcome'] == 'completed' and r['feature_complete'] is True
assert len(r['qa_decisions']) == 2
assert len(r['attempts']) == 4
assert sum(g['stage'] == 'baseline' for g in r['gates']) == 1
assert clean['integration'] == clean['development'] == r['milestones'][-1]['promoted_revision']
for d in r['qa_decisions']:
    raw = (evidence / next(item['retained_run_files'] for item in summary['observations'] if item['scenario'] == clean['scenario']) / 'artifacts' / Path(d['artifact']).name).read_bytes()
    assert sha(raw) == d['sha256']
    decision = json.loads(raw)
    assert decision['decision'] == 'APPROVED' and decision['request']['request_id'] == d['request_id']
next_worker = next(o for o in clean['launches'] if o['role'] == 'implementation' and o['event'] == 'start' and o['ticket'] == '04')
assert next_worker['head'] == next_worker['base'] == next_worker['integration'] == r['milestones'][0]['promoted_revision']
invalidated = next(r for r in raws if r['scenario'] == 'test_continued_run_records_invalidation_of_earlier_verified_source')
baseline_gate = next(g for g in invalidated['record']['gates'] if g['stage'] == 'baseline')
assert baseline_gate['passed'] is False and baseline_gate['verification_status'] == 'invalidated'
assert invalidated['development'] == invalidated['record']['base_revision']
assert not invalidated['record'].get('qa_decisions')
rejections = [r for r in raws if r['scenario'].startswith('test_continuation_rejects_changed_checkpoint_without_overwriting_prior_state')]
assert len(rejections) == 15
for raw in rejections:
    assert raw['cli_observations'][-1]['exit_code'] == 1
    assert raw['record']['outcome'] == 'stopped_at_qa'
    assert len(raw['record'].get('qa_decisions', [])) == (1 if raw['scenario'].endswith('[observation]') else 0)
manifest = read('15-repair1-package-manifest.json')
for path, expected in manifest['wheel_and_backend_sha256'].items():
    assert sha(Path(path).read_bytes()) == expected
wheel_path = next(path for path in manifest['wheel_and_backend_sha256'] if 'ticket_harness-' in path)
with zipfile.ZipFile(wheel_path) as wheel:
    for filename, expected in manifest['installed_source_sha256'].items():
        assert expected == identity['sha256']['ticket_harness/' + filename]
        assert sha(wheel.read('ticket_harness/' + filename)) == expected
        assert sha((Path('/tmp/ticket15-repair1-installed/ticket_harness') / filename).read_bytes()) == expected
installed = read('15-repair1-installed-observations.json')
assert installed['import_path'].startswith('/tmp/ticket15-repair1-installed/')
assert installed['final_record']['outcome'] == 'completed'
assert len(installed['final_record']['qa_decisions']) == 2
assert installed['feature'] == installed['development']
installed_bad = read('15-repair1-installed-invalidation.json')
bad_gate = next(g for g in installed_bad['final_record']['gates'] if g['stage'] == 'baseline')
assert not bad_gate['passed'] and bad_gate['verification_status'] == 'invalidated'
assert installed_bad['final_record']['outcome'] == 'incomplete'
assert installed_bad['development'] == installed_bad['final_record']['base_revision']
prereq = read('14-final-source-identity.json')
for ref in ['29fb5569cf53c75bd351d6bd176bb29889c42a65', '875c8f4ba8fa6c33e627c58cba6a8d118cebe12c']:
    subprocess.run(['git', 'merge-base', '--is-ancestor', ref, baseline], check=True)
changed = []
for path, expected in prereq['sha256'].items():
    assert sha(gitbytes('29fb5569cf53c75bd351d6bd176bb29889c42a65', path)) == expected
    assert sha(gitbytes(baseline, path)) == expected
    if sha((root / path).read_bytes()) != expected:
        changed.append(path)
for result in read('14-check-results.json'):
    assert result['exit_code'] == 0
    assert read(result['source_identity'])['sha256'] == prereq['sha256']
old_observations = read('14-fixture-observations.json')
for item in old_observations['scenarios']:
    raw = json.loads((root / item['retained_file']).read_text())
    assert {k:v for k,v in item.items() if k != 'retained_file'} == raw
assert len(old_observations['scenarios']) == 103
assert sha((root / 'docs/agents/issue-tracker.md').read_bytes()) == '3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce'
subprocess.run(['git', 'diff', '--check', baseline, head], check=True)
result = {'baseline': baseline, 'reviewed_head': head, 'independent_axis': 'Spec', 'source_hashes': len(identity['sha256']), 'final_gates': len(checks), 'raw_artifact_hashes': len(raw_hashes), 'final_scenarios': len(raws), 'checkpoint_rejection_scenarios': len(rejections), 'continuation_completion_decisions': len(r['qa_decisions']), 'post_restore_baseline_invalidation': True, 'installed_success_and_invalidation': True, 'prerequisite_source_hashes': len(prereq['sha256']), 'prerequisite_raw_scenarios': 103, 'prerequisite_source_changes_reviewed': changed, 'whitespace_exit_code': 0, 'unrelated_tracker_preserved': True}
(evidence / '15-spec-final-audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
