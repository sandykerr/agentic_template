"""Public CLI observation for unpadded plan IDs and worker override inheritance."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path.cwd() / 'tests'))
from test_dependencies import graph
from test_milestones import configure_plan, foreground, write_plan
from test_qa_promotion import waiting

out = Path('.scratch/ticket-harness/evidence')
generator = graph.__wrapped__(SimpleNamespace(node=SimpleNamespace(name='ticket22_normalized_final', path=Path('normalized.py'))))
fixture = next(generator)
try:
    plan = configure_plan(fixture)
    plan['required_tickets'] = ['1', '2', '3', '4']
    plan['final_coverage'] = ['1', '2', '3', '4']
    plan['milestones'][0]['tickets'] = ['3', '1']
    plan['milestones'][1]['tickets'] = ['4', '2']
    plan['worker_overrides'] = {'3': plan['worker_overrides']['03']}
    write_plan(fixture, plan)
    fixture.config_path.write_text(json.dumps(fixture.config))
    config_bytes = fixture.config_path.read_bytes()
    plan_bytes = (fixture.repo / 'plan.json').read_bytes()
    with foreground(fixture) as process:
        record = waiting(fixture, process, 'M1')
        assert record['selected_tickets'] == ['01', '03']
        assert record['plan']['milestones'][0]['tickets'] == ['03', '01']
        assert record['plan']['required_tickets'] == ['01', '02', '03', '04']
        assert record['plan']['roles']['worker']['reasoning'] == 'Medium'
        assert record['worker_settings']['03']['reasoning'] == 'High'
        assert record['worker_settings']['01']['reasoning'] == 'Medium'
        assert fixture.config_path.read_bytes() == config_bytes
        assert (fixture.repo / 'plan.json').read_bytes() == plan_bytes
        result = fixture.cli('stop', fixture.output)
        assert result.returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 2
    (out / '22-normalized-final-observation.json').write_text(json.dumps(dict(record=fixture.record(), foreground=fixture.foreground_observations, cli=fixture.cli_observations, refs=fixture.git('show-ref')), indent=2) + '\n')
finally:
    generator.close()
