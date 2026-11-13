import hashlib
import json
import shutil
import subprocess
from pathlib import Path

root = Path('/home/ajkerr1/development/agentic_template')
evidence = root / '.scratch/ticket-harness/evidence'
names = ['suite', 'mypy', 'lint', 'format', 'whitespace']
results = [json.loads((evidence / f'13-renewed-final-{name}-result.json').read_text()) for name in names]
assert all(result['exit_code'] == 0 for result in results)
identity = json.loads((evidence / '13-renewed-final-suite-source.json').read_text())
for name in names:
    other = json.loads((evidence / f'13-renewed-final-{name}-source.json').read_text())
    assert identity['sha256'] == other['sha256'], name
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
for path, digest in identity['sha256'].items():
    assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest, path
    committed = subprocess.check_output(['git', 'show', f'{head}:{path}'], cwd=root)
    assert hashlib.sha256(committed).hexdigest() == digest, path
source = evidence / '13-observations/renewed-final-suite'
archive = Path('/tmp/ticket13-checks/archived-observations/renewed-final-suite')
assert not archive.exists()
scenarios = []
for path in sorted(source.glob('*.json')):
    scenario = json.loads(path.read_text())
    scenario['retained_file'] = str(archive / path.name)
    scenarios.append(scenario)
assert len({item['scenario'] for item in scenarios}) == len(scenarios)
checks_log = ['Ticket 13 final verification; implementation checkpoint ' + head,
              'Source: 13-renewed-final-suite-source.json; command-local PYTHONPATH=/tmp/ticket12-tools.']
for name, result in zip(names, results):
    checks_log.extend(['', 'Command: ' + json.dumps(result['command']),
        'Exit: ' + str(result['exit_code']) + '; elapsed seconds: ' + str(result['seconds']),
        'Source: ' + result['source_identity'],
        'Observations: .scratch/ticket-harness/evidence/13-observations/renewed-final-' + name,
        (evidence / f'13-renewed-final-{name}.log').read_text().rstrip()])
(evidence / '13-checks.log').write_text('\n'.join(checks_log).rstrip() + '\n')
(evidence / '13-check-results.json').write_text(json.dumps(results, indent=2) + '\n')
shutil.copyfile(evidence / '13-renewed-final-suite-source.json', evidence / '13-final-source-identity.json')
manifest = {
    'review_baseline': identity['baseline'],
    'implementation_commit': head,
    'tested_source_identity': identity,
    'committed_source_matches_tested_hashes': True,
    'final_check_results': results,
    'check_log': '.scratch/ticket-harness/evidence/13-checks.log',
    'coverage_map': '.scratch/ticket-harness/evidence/13-coverage-map.md',
    'scenario_count': len(scenarios),
    'scenarios': scenarios,
    'provenance': 'Only the renewed final full-suite execution supplies these observations. All final command captures have identical source/test hashes, matched to the implementation checkpoint and current bytes. Temporary fixture repositories were cleaned after retaining actual CLI, record, Git, assignment, output and applicable QA request/candidate observations. Raw scenario files are archived at each retained_file path and were compared byte-for-structure with the consolidated copy excluding retained_file. Development/focused/interrupted runs remain distinct and superseded.'
}
(evidence / '13-fixture-observations.json').write_text(json.dumps(manifest, indent=2) + '\n')
shutil.move(str(source), str(archive))
for item in scenarios:
    expected = json.loads(Path(item['retained_file']).read_text())
    assert expected == {k:v for k,v in item.items() if k != 'retained_file'}
print(json.dumps({'head': head, 'hashes_verified': len(identity['sha256']), 'scenarios': len(scenarios), 'checks': len(results)}))
