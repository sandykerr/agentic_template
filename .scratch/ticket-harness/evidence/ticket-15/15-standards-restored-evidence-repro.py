import json
import sys
from pathlib import Path
from types import SimpleNamespace
sys.path[:0] = [str(Path.cwd()), str(Path.cwd() / 'tests')]
from test_dependencies import graph as graph_fixture
from test_milestones import configure_plan, foreground
from test_qa_promotion import waiting

generator = graph_fixture.__wrapped__(SimpleNamespace(node=SimpleNamespace(name='standards_restored_evidence_repro', path=Path('standards_repro.py'))))
graph = next(generator)
try:
    configure_plan(graph)
    with foreground(graph) as process:
        waiting(graph, process, 'M1')
        assert graph.cli('stop', graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 2
    with foreground(graph, operation='continue') as process:
        waiting(graph, process, 'M1')
        (graph.output / 'worktrees/baseline/value.txt').write_text('external post-restore edit')
        assert graph.cli('stop', graph.output).returncode == 0
        process.wait(timeout=10)
        record = graph.record()
        baseline = [gate for gate in record['gates'] if gate['stage'] == 'baseline'][0]
        result = {'exit_code': process.returncode, 'outcome': record['outcome'], 'failure': record.get('failure'), 'baseline_gate': baseline, 'run_directory': str(graph.output)}
        Path('.scratch/ticket-harness/evidence/15-standards-restored-evidence-repro.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps(result, indent=2))
finally:
    try:
        next(generator)
    except StopIteration:
        pass
