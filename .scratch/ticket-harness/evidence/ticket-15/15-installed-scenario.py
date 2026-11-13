"""Retained installed console-script observation; uses only the approved CLI/Git seam."""
import contextlib
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
from types import SimpleNamespace

ROOT = Path('/home/ajkerr1/development/agentic_template')
EVIDENCE = ROOT / '.scratch/ticket-harness/evidence'
sys.path.insert(0, str(ROOT / 'tests'))
import test_dependencies
from test_milestones import configure_plan, wait_for
from test_qa_promotion import approve, waiting

INSTALLED = Path('/tmp/ticket15-installed')
ENV = dict(os.environ, PYTHONPATH=str(INSTALLED))
COMMAND = [str(INSTALLED / 'bin/ticket-harness')]
commands = []


def cli(*args):
    command = COMMAND + list(map(str, args))
    result = subprocess.run(command, cwd='/tmp', env=ENV, capture_output=True, text=True, timeout=20)
    commands.append(dict(command=command, cwd='/tmp', exit_code=result.returncode, stdout=result.stdout, stderr=result.stderr))
    return result


@contextlib.contextmanager
def owner(graph, *args):
    command = COMMAND + list(map(str, args))
    out_path, err_path = graph.home / 'foreground.stdout', graph.home / 'foreground.stderr'
    with out_path.open('w') as out, err_path.open('w') as err:
        process = subprocess.Popen(command, cwd='/tmp', env=ENV, stdout=out, stderr=err, start_new_session=True)
    try:
        yield process
    finally:
        terminated = process.poll() is None
        if terminated:
            owned, pending = {process.pid}, [process.pid]
            while pending:
                parent = pending.pop()
                try:
                    found = {int(pid) for pid in Path(f'/proc/{parent}/task/{parent}/children').read_text().split()} - owned
                except FileNotFoundError:
                    found = set()
                owned.update(found); pending.extend(found)
            for pid in owned:
                try:
                    group = os.getpgid(pid)
                    if group in owned:
                        os.killpg(group, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        process.wait(timeout=10)
        observation = dict(command=command, cwd='/tmp', exit_code=process.returncode, terminated_by_fixture=terminated, stdout=out_path.read_text(), stderr=err_path.read_text())
        commands.append(observation)
        graph.foreground_observations = getattr(graph, 'foreground_observations', []) + [observation]


os.environ['TICKET_HARNESS_TEST_OBSERVATIONS'] = str(EVIDENCE / '15-observations/installed')
request = SimpleNamespace(node=SimpleNamespace(name='installed_two_group_stop_continue', path=Path('test_continuation.py')))
fixture = test_dependencies.graph.__wrapped__(request)
graph = next(fixture)
try:
    configure_plan(graph)
    graph.config_path.write_text(json.dumps(graph.config))
    with owner(graph, 'run', '--config', graph.config_path, '--output', graph.output) as process:
        first = waiting(graph, process, 'M1')
        qa1 = json.loads((graph.output/'qa-request.json').read_text())
        assert cli('continue', graph.output).returncode == 1
        assert cli('stop', graph.output).returncode == 0
        process.wait(timeout=15)
        assert process.returncode == 2
    stopped = graph.record()
    raw_plan = (graph.repo/'plan.json').read_bytes()
    (graph.repo/'plan.json').write_text('changed plan')
    assert cli('continue', graph.output).returncode == 1
    assert graph.record() == stopped
    (graph.repo/'plan.json').write_bytes(raw_plan)
    approve(graph, qa1)
    with owner(graph, 'continue', graph.output) as process:
        second = waiting(graph, process, 'M2')
        assert second['attempts'][:2] == first['attempts']
        assert len(second['qa_decisions']) == 1
        assert graph.git('rev-parse','dev') == qa1['candidate_revision']
        approve(graph, qa1)
        wait_for(graph, process, lambda r:r.get('qa_decision_status') == 'rejected')
        assert cli('stop', graph.output).returncode == 0
        process.wait(timeout=15)
        assert process.returncode == 2
    with owner(graph, 'continue', graph.output) as process:
        waiting(graph, process, 'M2')
        approve(graph, json.loads((graph.output/'qa-request.json').read_text()))
        process.wait(timeout=20)
        assert process.returncode == 0
    final = graph.record()
    assert final['feature_complete'] is True and len(final['qa_decisions']) == 2
    assert len([e for e in test_dependencies.launches(graph) if e['role']=='implementation' and e['event']=='start']) == 4
    assert [g['stage'] for g in final['gates']].count('baseline') == 1
    assert cli('status', graph.output).stdout == (graph.output/'run.json').read_text()
    assert cli('continue', graph.output).returncode == 1
    resolved = subprocess.check_output([sys.executable, '-c', 'import ticket_harness;print(ticket_harness.__file__)'], cwd='/tmp', env=ENV, text=True).strip()
    assert resolved.startswith(str(INSTALLED))
    result = dict(import_path=resolved, commands=commands, final_record=final, feature=graph.git('rev-parse','integration'), development=graph.git('rev-parse','dev'), installed_sha256={str(p.relative_to(INSTALLED)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (INSTALLED/'ticket_harness').glob('*.py')})
    (EVIDENCE/'15-installed-observations.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(import_path=resolved, feature_complete=final['feature_complete'], decisions=len(final['qa_decisions']), operations=len(commands))))
finally:
    try:
        next(fixture)
    except StopIteration:
        pass
