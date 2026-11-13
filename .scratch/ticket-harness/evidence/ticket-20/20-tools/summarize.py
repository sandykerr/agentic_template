"""Index retained public observations without changing their original records."""
import hashlib
import json
from collections import Counter
from pathlib import Path

raw = Path('/tmp/ticket20-final-raw')
out = Path('.scratch/ticket-harness/evidence')
scenarios = []
counts = Counter()
for path in sorted(raw.glob('*/observations.json')):
    observation = json.loads(path.read_text())
    record = observation['record']
    entry = {'scenario':observation['scenario'], 'path':str(path.relative_to(raw)), 'outcome':record.get('outcome'), 'attempts':len(record.get('attempts',[])), 'gates':len(record.get('gates',[]))}
    assert observation['status']['exit_code'] == 0
    assert json.loads(observation['status']['stdout']) == record
    for attempt in record.get('attempts',[]):
        if 'gate_end' in attempt:
            gates=record['gates'][attempt['gate_start']:attempt['gate_end']]
            assert all(g['ticket'] == attempt['ticket'] and g['attempt'] == attempt['attempt'] for g in gates), entry
        if 'human_decision' in attempt:
            decision=attempt['human_decision']
            assert decision['attempt'] == attempt['attempt']
            assert decision['report']['ticket'] == attempt['ticket']
            if record.get('ticket',{}).get('attempt') == attempt['attempt'] and record.get('ticket',{}).get('id') == attempt['ticket']:
                assert record['ticket']['human_decision'] == decision
            counts['decisions_' + decision['role']] += 1
    for gate in record.get('gates',[]):
        counts['report_' + gate.get('report_status', 'none')] += 1
    counts['outcome_' + str(record.get('outcome'))] += 1
    scenarios.append(entry)
files = {str(p.relative_to(raw)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(raw.rglob('*')) if p.is_file()}
(out / '20-observation-index.json').write_text(json.dumps({'raw_archive':'20-final-raw.tar.gz', 'scenario_count':len(scenarios), 'counts':dict(counts), 'scenarios':scenarios},indent=2)+'\n')
(out / '20-raw-manifest.json').write_text(json.dumps(files,indent=2)+'\n')
print(json.dumps({'scenarios':len(scenarios),'raw_files':len(files),'counts':dict(counts)}))
