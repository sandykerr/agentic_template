"""Bind repair gates and raw observations to the actual repair commit."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/home/ajkerr1/development/agentic_template')
EVIDENCE = ROOT / '.scratch/ticket-harness/evidence'
BASELINE = '90255aaf6faf9aedce18f7159093f5dbfde294b7'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, value):
    (EVIDENCE / name).write_text(json.dumps(value, indent=2) + '\n')

head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
source = json.loads((EVIDENCE / '15-repair1-final-suite-source.json').read_text())
for name, expected in source['sha256'].items():
    assert sha(ROOT / name) == expected, name
    committed = subprocess.check_output(['git', 'show', f'{head}:{name}'], cwd=ROOT)
    assert hashlib.sha256(committed).hexdigest() == expected, name
checks = {}
for label in ('suite', 'mypy', 'lint', 'format', 'whitespace', 'actual-staged-whitespace', 'committed-whitespace', 'wheel', 'install', 'installed'):
    name = f'15-repair1-final-{label}'
    capture = json.loads((EVIDENCE / f'{name}-source.json').read_text())
    result = json.loads((EVIDENCE / f'{name}-result.json').read_text())
    assert capture['sha256'] == source['sha256'], name
    assert result['exit_code'] == 0, name
    checks[label] = dict(result, log=f'{name}.log', log_sha256=sha(EVIDENCE / f'{name}.log'))
write('15-repair1-check-results.json', dict(baseline=BASELINE, implementation=head, all_final_gate_source_hashes_match_committed=True, checks=checks, historical_note='Initial 15-final-* and root audits remain initial-implementation history; only repair1-final captures verify this repair.'))
tracker = sha(ROOT / 'docs/agents/issue-tracker.md')
assert tracker == '3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce'
write('15-repair1-final-source-identity.json', dict(baseline=BASELINE, head=head, sha256=source['sha256'], tested_source_capture='15-repair1-final-suite-source.json', committed_sources_match_final_suite=True, unrelated_tracker_sha256=tracker))
observations = []
for path in sorted((EVIDENCE / '15-observations/repair1-final-suite').glob('*.json')):
    value = json.loads(path.read_text())
    record = value['record']
    retained = path.with_name(path.stem + '-files')
    observations.append(dict(scenario=value['scenario'], raw_file=str(path.relative_to(EVIDENCE)), raw_sha256=sha(path), retained_run_files=str(retained.relative_to(EVIDENCE)) if retained.exists() else None, outcome=record['outcome'], feature_complete=record.get('feature_complete'), integration=value['integration'], development=value.get('development'), consumed_decisions=len(record.get('qa_decisions', [])), checkpoint_archives=sorted(p.name for p in (retained / 'checkpoints').glob('*.json'))))
write('15-repair1-fixture-observations.json', dict(implementation=head, source_capture='15-repair1-final-suite-source.json', scenario_count=len(observations), observations=observations))
(EVIDENCE / '15-repair1-checks.log').write_text(''.join(f'{label}: command={json.dumps(result["command"])} exit={result["exit_code"]} seconds={result["seconds"]} log={result["log"]}\n' for label, result in checks.items()))
print(json.dumps(dict(implementation=head, gates=len(checks), source_hashes=len(source['sha256']), retained_scenarios=len(observations))))
