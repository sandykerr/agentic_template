"""Stage deadlines and descendant cleanup observed through the CLI and real processes."""

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest
from test_cli import TicketFixture
from test_repairs import repair_agent


class BoundedTicketFixture(TicketFixture):
    def cli(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "ticket_harness", *map(str, args)],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )


@pytest.fixture
def harness(request):
    fixture = BoundedTicketFixture()
    fixture.setUp()
    try:
        yield fixture
    finally:
        # Also bound failed/red tests: never leave controlled children behind.
        for path in fixture.home.glob("launched-*.json"):
            pids = json.loads(path.read_text())
            if pids["group"] != os.getpgrp():
                try:
                    os.killpg(pids["group"], signal.SIGKILL)
                except ProcessLookupError:
                    pass
        observations = os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS")
        if observations and (fixture.output / "run.json").exists():
            record = fixture.record()
            evidence = {
                "scenario": request.node.name,
                "record": record,
                "integration": fixture.git("rev-parse", "integration"),
                "caller_status": fixture.git("status", "--porcelain"),
                "outputs": {
                    path.name: path.read_text()
                    for gate in record["gates"]
                    for path in (Path(gate["stdout"]), Path(gate["stderr"]))
                },
            }
            destination = Path(observations)
            destination.mkdir(parents=True, exist_ok=True)
            (destination / (fixture.home.name + ".json")).write_text(json.dumps(evidence, indent=2))
        fixture.doCleanups()


def stall_script(harness):
    script = harness.home / "stall.py"
    script.write_text(
        "import json, os, signal, subprocess, sys, time\nfrom pathlib import Path\n"
        "signal.signal(signal.SIGTERM, signal.SIG_IGN)\n"
        "child = subprocess.Popen([sys.executable, '-c',\n"
        "    'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(20)'])\n"
        f"Path({str(harness.home)!r}, 'launched-' + str(os.getpid()) + '.json').write_text(\n"
        "    json.dumps(dict(parent=os.getpid(), child=child.pid, group=os.getpgrp())))\n"
        "print('partial stdout', flush=True)\n"
        "print('partial stderr', file=sys.stderr, flush=True)\n"
        "time.sleep(20)\n"
    )
    return script


def assert_stopped(pid):
    # An orphan may briefly remain a zombie awaiting the system reaper; it cannot execute.
    deadline = time.monotonic() + 5
    while time.monotonic() < deadline:
        try:
            state = Path(f"/proc/{pid}/stat").read_text().split(") ", 1)[1].split()[0]
        except FileNotFoundError:
            return
        if state == "Z":
            return
        time.sleep(0.05)
    pytest.fail(f"controlled process {pid} still running after timeout cleanup")


def timeout_agent(harness, role, until=1, exit_parent=False, decision=False):
    stall = stall_script(harness)
    repair_agent(
        harness,
        f"if assignment['role'] == {role!r} and assignment['attempt'] <= {until}:\n"
        + (
            "    Path('value.txt').write_text('3\\n')\n"
            "    Path('repair-note').write_text('preserve timed out work')\n"
            if role == "implementation"
            else ""
        )
        + (
            "    report.update(result='human-decision-needed', unresolved_questions=['Decide'])\n"
            if decision
            else ""
        )
        + "    print(json.dumps(report), flush=True)\n"
        + f"    child = subprocess.Popen([sys.executable, {str(stall)!r}], stdout=sys.stderr)\n"
        + ("    sys.exit(0)\n" if exit_parent else "    child.wait()\n    sys.exit(0)"),
    )


def assert_observations(harness, result, completed):
    record = harness.record()
    assert result.returncode == (0 if completed else 1), result.stderr
    assert json.loads(result.stdout) == record
    durable = (harness.output / "run.json").read_bytes()
    assert json.loads(harness.cli("status", harness.output).stdout) == record
    assert (harness.output / "run.json").read_bytes() == durable
    assert record["ticket"]["state"] == ("Done" if completed else "Blocked")
    for snapshot in record["inputs"].values():
        assert Path(snapshot["source"]).read_bytes() == Path(snapshot["artifact"]).read_bytes()
    for path in harness.home.glob("launched-*.json"):
        for pid in json.loads(path.read_text()).values():
            assert_stopped(pid)
    for attempt in record["attempts"]:
        gates = record["gates"][attempt["gate_start"] : attempt["gate_end"]]
        assert all(g["attempt"] == attempt["attempt"] for g in gates)
    return record


def test_worker_timeout_stops_children_preserves_output_and_blocks(harness):
    stall = stall_script(harness)
    harness.config["agent"] = [sys.executable, str(stall)]
    harness.config["timeouts"] = {"implementation": 1}
    result = harness.run_ticket()
    assert result.returncode == 1
    record = harness.record()
    assert record["outcome"] == "incomplete"
    assert record["ticket"]["state"] == "Blocked"
    assert len(record["attempts"]) == 1
    assert [g["stage"] for g in record["gates"]] == ["baseline", "implementation"]
    gate = record["gates"][-1]
    assert gate["timed_out"] is True
    assert gate["timeout_seconds"] == 1
    assert not gate["passed"]
    assert "partial stdout" in Path(gate["stdout"]).read_text()
    assert "partial stderr" in Path(gate["stderr"]).read_text()
    pids = json.loads(next(harness.home.glob("launched-*.json")).read_text())
    assert_stopped(pids["parent"])
    assert_stopped(pids["child"])
    assert harness.git("rev-parse", "integration") == harness.base
    assert json.loads(result.stdout) == record
    assert json.loads(harness.cli("status", harness.output).stdout) == record


@pytest.mark.parametrize(
    "value", [0, -1, True, "1", None, float("inf"), float("nan"), 10**400, 1e308]
)
def test_invalid_timeout_is_rejected_before_any_process(harness, value):
    harness.config["timeouts"] = {"implementation": value}
    result = harness.run_ticket()
    assert result.returncode == 1
    record = harness.record()
    assert record["outcome"] == "invalid-input"
    assert "timeouts.implementation" in record["failure"]["message"]
    assert record["ticket"]["attempt"] == 0
    assert record["gates"] == record["attempts"] == []
    assert not list((harness.output / "worktrees").iterdir())
    assert harness.git("rev-parse", "integration") == harness.base
    assert json.loads(harness.cli("status", harness.output).stdout) == record


@pytest.mark.parametrize("value", [None, [], {"typo": 1}, {"repair": 0}, {"checks": False}])
def test_invalid_timeout_object_or_stage_is_rejected_before_execution(harness, value):
    harness.config["timeouts"] = value
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["outcome"] == "invalid-input"
    assert "timeouts" in record["failure"]["message"]
    assert record["gates"] == record["attempts"] == []


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
def test_timed_out_assignment_repairs_current_work_with_fresh_verification(harness, role):
    harness.config["max_repairs"] = 1
    harness.config["timeouts"] = {
        "implementation": 1 if role == "implementation" else 8,
        "repair": 9,
        "spec": 1 if role == "spec" else 10,
        "standards": 1 if role == "standards" else 11,
        "checks": 12,
        "baseline": 13,
        "candidate": 14,
    }
    timeout_agent(harness, role)
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "value.txt").write_text("caller unstaged\n")
    (harness.repo / "unrelated").write_text("caller untracked")
    caller_status = harness.git("status", "--porcelain")
    record = assert_observations(harness, harness.run_ticket(), completed=True)
    assert record["outcome"] == "completed"
    assert [a["state"] for a in record["attempts"]] == ["Rejected", "Done"]
    rejected, repaired = record["attempts"]
    assert rejected["failure"]["stage"] == role
    failures = [g for g in record["gates"] if g["timed_out"]]
    assert len(failures) == 1
    failure = failures[0]
    assert failure["stage"] == role
    assert failure["report_status"] == "not-evaluated"
    assert "timed out after 1 seconds" in failure["diagnostic"]
    assert json.loads(Path(failure["stdout"]).read_text())["attempt"] == 1
    assert "partial stderr" in Path(failure["stderr"]).read_text()
    assert failure["cleanup"]["sent"] is True
    gates = [g for g in record["gates"] if g["attempt"] == 2]
    assert [g["stage"] for g in gates] == [
        "implementation",
        "check-ticket",
        "spec",
        "standards",
        "candidate",
    ]
    for gate in record["gates"]:
        category = (
            "repair"
            if gate["attempt"] == 2 and gate["stage"] == "implementation"
            else ("checks" if gate["stage"].startswith("check-") else gate["stage"])
        )
        assert gate["timeout_category"] == category
        assert gate["timeout_seconds"] == harness.config["timeouts"][category]
    worker = gates[0]
    prompt = json.loads(Path(worker["assignment"]).read_text())
    assert prompt["attempt"] == 2
    assert prompt["base_revision"] == harness.base
    assert prompt["repair_context"]["failure"] == rejected["failure"]
    assert prompt["check_results"][-1] == failure
    if role == "implementation":
        assert worker["report"]["before"] == "3\n"
        assert "submitted_revision" not in rejected
        assert harness.git("show", "integration:repair-note") == "preserve timed out work"
    else:
        assert rejected["submitted_revision"] != repaired["submitted_revision"]
        assert prompt["revision"] == rejected["submitted_revision"]
    assert all(g["passed"] for g in gates)
    assert all(g["revision"] == repaired["submitted_revision"] for g in gates[1:4])
    candidate = repaired["candidate_revision"]
    assert candidate == gates[-1]["revision"] == harness.git("rev-parse", "integration")
    assert harness.git("show", "-s", "--format=%P", candidate).split() == [
        harness.base,
        repaired["submitted_revision"],
    ]
    assert harness.git("rev-parse", candidate + "^{tree}") == harness.git(
        "rev-parse", repaired["submitted_revision"] + "^{tree}"
    )
    assert harness.git("status", "--porcelain") == caller_status
    assert harness.git("rev-parse", "HEAD") == harness.base
    assert harness.git("show", ":value.txt") == "caller staged"
    assert (harness.repo / "value.txt").read_text() == "caller unstaged\n"


@pytest.mark.parametrize("decision", [False, True], ids=["submitted", "human-decision"])
def test_exited_worker_with_child_holding_output_cannot_approve_or_request_decision(
    harness, decision
):
    harness.config["max_repairs"] = 1
    harness.config["timeouts"] = {"implementation": 1}
    timeout_agent(harness, "implementation", exit_parent=True, decision=decision)
    record = assert_observations(harness, harness.run_ticket(), completed=True)
    gate = record["gates"][1]
    assert gate["exit_code"] == 0
    assert gate["timed_out"] is True
    assert gate["passed"] is False
    assert gate["report_status"] == "not-evaluated"
    assert "human_decision" not in record["attempts"][0]
    assert "human_decision" not in record["ticket"]
    assert len(record["attempts"]) == 2
    assert json.loads(Path(gate["stdout"]).read_text())["result"] == (
        "human-decision-needed" if decision else "submitted"
    )


def test_timeout_exhaustion_uses_repair_deadline_and_preserves_all_attempts(harness):
    del harness.config["max_repairs"]
    harness.config["timeouts"] = {"implementation": 1, "repair": 1.5}
    timeout_agent(harness, "implementation", until=100)
    record = assert_observations(harness, harness.run_ticket(), completed=False)
    assert record["outcome"] == "incomplete"
    assert record["max_repairs"] == 2
    assert record["ticket"]["attempt"] == 3
    assert [a["state"] for a in record["attempts"]] == ["Rejected"] * 3
    gates = record["gates"][1:]
    assert [g["stage"] for g in gates] == ["implementation"] * 3
    assert [g["timeout_seconds"] for g in gates] == [1, 1.5, 1.5]
    assert [g["timeout_category"] for g in gates] == ["implementation", "repair", "repair"]
    assert [g["attempt"] for g in gates] == [1, 2, 3]
    assert all(g["timed_out"] and not g["passed"] for g in gates)
    assert len({g["stdout"] for g in gates}) == 3
    assert len({g["cleanup"]["process_group"] for g in gates}) == 3
    assert len(list(harness.home.glob("launched-*.json"))) == 3
    for gate in gates:
        prompt = json.loads(Path(gate["assignment"]).read_text())
        assert prompt["attempt"] == gate["attempt"]
        assert prompt["base_revision"] == gate["revision"] == harness.base
        assert "partial stderr" in Path(gate["stderr"]).read_text()
        assert (Path(gate["cwd"]) / "value.txt").read_text() == "3\n"
        assert (Path(gate["cwd"]) / "repair-note").read_text() == "preserve timed out work"
    assert harness.git("rev-parse", "integration") == harness.base
    assert "done_revision" not in record["ticket"]


def timeout_check(harness, stage, until=1):
    stall = stall_script(harness)
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    Path('attempt.txt').write_text(str(assignment['attempt']))",
    )
    script = harness.home / "check-timeout.py"
    script.write_text(
        "import os, subprocess, sys\nfrom pathlib import Path\n"
        "stage = os.environ['TICKET_HARNESS_STAGE']\n"
        f"if stage == {stage!r} and (not Path('attempt.txt').exists() or "
        f"int(Path('attempt.txt').read_text()) <= {until}):\n"
        f"    subprocess.run([sys.executable, {str(stall)!r}], check=True)\n"
        "subprocess.run([sys.executable, 'check.py', 'fixture'], check=True)\n"
    )
    harness.config["suite" if stage in ("baseline", "candidate") else "checks"] = (
        [sys.executable, str(script)]
        if stage in ("baseline", "candidate")
        else {"ticket": [sys.executable, str(script)]}
    )


@pytest.mark.parametrize("stage", ["check-ticket", "candidate"])
def test_check_timeout_can_repair_and_test_the_exact_new_candidate(harness, stage):
    harness.config["max_repairs"] = 1
    category = "checks" if stage == "check-ticket" else "candidate"
    harness.config["timeouts"] = {category: 1}
    timeout_check(harness, stage)
    record = assert_observations(harness, harness.run_ticket(), completed=True)
    assert [a["state"] for a in record["attempts"]] == ["Rejected", "Done"]
    first, second = record["attempts"]
    assert first["failure"]["stage"] == stage
    failure = next(g for g in record["gates"] if g["timed_out"])
    assert failure["stage"] == stage
    assert failure["timeout_category"] == category
    assert failure["timeout_seconds"] == 1
    assert "partial stdout" in Path(failure["stdout"]).read_text()
    assert "partial stderr" in Path(failure["stderr"]).read_text()
    gates = record["gates"][second["gate_start"] : second["gate_end"]]
    assert [g["stage"] for g in gates] == [
        "implementation",
        "check-ticket",
        "spec",
        "standards",
        "candidate",
    ]
    assert all(g["passed"] and not g["timed_out"] for g in gates)
    assert first["submitted_revision"] != second["submitted_revision"]
    assert all(g["revision"] == second["submitted_revision"] for g in gates[1:4])
    assert gates[-1]["revision"] == second["candidate_revision"]
    assert harness.git("rev-parse", "integration") == second["candidate_revision"]
    if stage == "candidate":
        assert failure["revision"] == first["candidate_revision"]
        assert first["candidate_revision"] != second["candidate_revision"]


def test_baseline_timeout_is_environment_failure_without_spending_repairs(harness):
    del harness.config["max_repairs"]
    harness.config["timeouts"] = {"baseline": 1}
    timeout_check(harness, "baseline")
    record = assert_observations(harness, harness.run_ticket(), completed=False)
    assert record["outcome"] == "environment"
    assert record["attempts"] == []
    assert record["ticket"]["attempt"] == 0
    assert [g["stage"] for g in record["gates"]] == ["baseline"]
    gate = record["gates"][0]
    assert gate["timed_out"] and not gate["passed"]
    assert gate["timeout_seconds"] == 1
    assert gate["timeout_category"] == "baseline"
    assert len(list(harness.home.glob("launched-*.json"))) == 1
    assert harness.git("rev-parse", "integration") == harness.base


def test_unavailable_shared_executable_stops_run_without_repairs(harness):
    del harness.config["max_repairs"]
    executable = harness.home / "shared-check"
    executable.write_text("#!/bin/sh\nexit 0\n")
    executable.chmod(0o755)
    harness.config["checks"] = {"ticket": [str(executable)]}
    repair_agent(
        harness,
        f"if assignment['role'] == 'implementation':\n    Path({str(executable)!r}).unlink()",
    )
    record = assert_observations(harness, harness.run_ticket(), completed=False)
    assert record["outcome"] == "environment"
    assert record["ticket"]["attempt"] == 1
    assert len(record["attempts"]) == 1
    assert [g["stage"] for g in record["gates"]] == ["baseline", "implementation", "check-ticket"]
    assert record["gates"][-1]["execution_error"]
    assert record["gates"][-1]["exit_code"] is None
    assert harness.git("rev-parse", "integration") == harness.base


def test_default_timeouts_are_normalized_and_visible_on_each_successful_gate(harness):
    record = assert_observations(harness, harness.run_ticket(), completed=True)
    assert record["timeouts"] == {
        "implementation": 1800,
        "repair": 1800,
        "spec": 900,
        "standards": 900,
        "checks": 300,
        "baseline": 1800,
        "candidate": 1800,
    }
    for gate in record["gates"]:
        assert gate["timed_out"] is False
        assert gate["timeout_seconds"] == (
            300
            if gate["stage"] == "check-ticket"
            else (900 if gate["stage"] in ("spec", "standards") else 1800)
        )


def test_timeout_cannot_hide_evidence_tampering_or_authorize_repair(harness):
    harness.config["max_repairs"] = 2
    harness.config["timeouts"] = {"implementation": 1}
    timeout_agent(harness, "implementation")
    script = Path(harness.config["agent"][1])
    original = harness.output / "artifacts/baseline.stderr"
    script.write_text(
        script.read_text().replace(
            "report.update(pid=os.getpid(), before=before)",
            "report.update(pid=os.getpid(), before=before)\n"
            f"Path({str(original)!r}).write_text('rejected evidence edit')",
        )
    )
    record = assert_observations(harness, harness.run_ticket(), completed=False)
    assert record["ticket"]["attempt"] == 1
    assert len(record["attempts"]) == 1
    gate = record["gates"][-1]
    assert gate["timed_out"] is True
    assert "integrity" in record["failure"]["message"].lower()
    violation = next(item for item in gate["integrity"] if item["path"] == str(original))
    assert Path(violation["artifact"]).read_text() == "rejected evidence edit"
    assert original.read_text() == ""
    assert harness.git("rev-parse", "integration") == harness.base
