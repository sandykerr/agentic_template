"""Bounded repairs observed through CLI, scripted processes, and real Git state."""

import json
from pathlib import Path

import pytest
from test_cli import TicketFixture


@pytest.fixture
def harness():
    fixture = TicketFixture()
    fixture.setUp()
    del fixture.config["max_repairs"]
    yield fixture
    fixture.doCleanups()


def repair_agent(harness, action):
    script = harness.home / "repair-agent.py"
    script.write_text(
        "import json, os, subprocess, sys\nfrom pathlib import Path\n"
        "assignment = json.load(sys.stdin)\n"
        "before = Path('value.txt').read_text()\n"
        f"process = subprocess.run([sys.executable, {str(harness.repo / 'agent.py')!r}], "
        "input=json.dumps(assignment), capture_output=True, text=True)\n"
        "report = json.loads(process.stdout)\n"
        "report.update(pid=os.getpid(), before=before)\n" + action + "\nprint(json.dumps(report))\n"
    )
    harness.config["agent"] = [harness.config["agent"][0], str(script)]


def test_failed_check_repairs_current_changes_and_renews_all_gates(harness):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation' and assignment['attempt'] == 1:\n"
        "    Path('value.txt').write_text('3\\n')",
    )
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    assert record["max_repairs"] == 2
    assert record["ticket"]["attempt"] == 2
    assert record["ticket"]["state"] == "Done"
    attempts = record["attempts"]
    assert [a["state"] for a in attempts] == ["Rejected", "Done"]
    rejected, repaired = [a["submitted_revision"] for a in attempts]
    assert rejected != repaired
    assert harness.git("show", rejected + ":value.txt") == "3"
    assert harness.git("show", repaired + ":value.txt") == "2"
    gates = record["gates"]
    assert [(g["attempt"], g["stage"]) for g in gates] == [
        (0, "baseline"),
        (1, "implementation"),
        (1, "check-ticket"),
        (2, "implementation"),
        (2, "check-ticket"),
        (2, "spec"),
        (2, "standards"),
        (2, "candidate"),
    ]
    workers = [g for g in gates if g["stage"] == "implementation"]
    assert workers[1]["report"]["before"] == "3\n"
    assert workers[0]["report"]["pid"] != workers[1]["report"]["pid"]
    prompt = json.loads(Path(workers[1]["assignment"]).read_text())
    assert prompt["attempt"] == 2
    assert prompt["revision"] == rejected
    assert prompt["repair_context"]["rejected_revisions"] == [rejected]
    assert prompt["repair_context"]["failure"]["stage"] == "check-ticket"
    failure = prompt["check_results"][-1]
    assert not failure["passed"]
    assert "AssertionError" in Path(failure["stderr"]).read_text()
    for gate in gates[4:7]:
        assert gate["revision"] == repaired
        assert gate["passed"]
    for gate in gates[5:7]:
        assert gate["report"]["attempt"] == 2
    candidate = record["ticket"]["done_revision"]
    assert gates[-1]["revision"] == candidate
    assert harness.git("rev-parse", "integration") == candidate
    assert harness.git("show", candidate + ":value.txt") == "2"
    assert len({g["stdout"] for g in gates}) == len(gates)
    assert json.loads(harness.cli("status", harness.output).stdout) == record


def test_failed_git_operations_have_per_attempt_diagnostics(harness):
    reject_until(harness, "merge", 100)
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    failures = [op for op in record["operations"] if not op["passed"]]
    assert [op["attempt"] for op in failures] == [1, 2, 3]
    assert all("controlled merge rejection" in op["diagnostic"] for op in failures)


def test_invalid_worker_report_preserves_uncommitted_changes_for_fresh_repair(harness):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    if assignment['attempt'] == 1:\n"
        "        Path('value.txt').write_text('3\\n')\n"
        "        Path('repair-note').write_text('keep this work')\n"
        "        del report['acceptance_evidence']\n"
        "    else:\n"
        "        assert before == '3\\n'\n"
        "        assert Path('repair-note').read_text() == 'keep this work'",
    )
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    assert record["ticket"]["attempt"] == 2
    first = record["attempts"][0]
    assert "submitted_revision" not in first
    assert (Path(first["source"]) / "value.txt").read_text() == "3\n"
    assert record["gates"][1]["report_status"] == "invalid"
    assert harness.git("show", "integration:repair-note") == "keep this work"


def reject_until(harness, stage, until):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    Path('attempt.txt').write_text(str(assignment['attempt']))\n"
        f"elif assignment['role'] == {stage!r} and assignment['attempt'] <= {until}:\n"
        "    report['findings'] = [dict(id='fix-value', classification='blocking',\n"
        "        location='value.txt:1', requirement='Controlled fixture requirement',\n"
        "        consequence='Cannot accept rejected value', evidence='Concrete review failure',\n"
        "        resolution='Repair this value', human_decision_needed=False)]",
    )
    if stage == "merge":
        hook = harness.repo / ".git/hooks/pre-merge-commit"
        hook.write_text(
            f'#!/bin/sh\nif [ "$(cat attempt.txt)" -le {until} ]; then\n'
            "echo 'controlled merge rejection' >&2\nexit 1\nfi\n"
        )
        hook.chmod(0o755)
    if stage in ("check-ticket", "candidate"):
        script = harness.home / "reject-check.py"
        script.write_text(
            "import os, subprocess, sys\nfrom pathlib import Path\n"
            "stage = os.environ['TICKET_HARNESS_STAGE']\n"
            "print(subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True))\n"
            f"if stage == {stage!r} and int(Path('attempt.txt').read_text()) <= {until}:\n"
            "    sys.exit('concrete check failure: repair the value')\n"
            "subprocess.run([sys.executable, 'check.py', 'fixture'], check=True)\n"
        )
        command = [harness.config["agent"][0], str(script)]
        if stage == "candidate":
            harness.config["suite"] = command
        else:
            harness.config["checks"]["ticket"] = command


@pytest.mark.parametrize("stage", ["check-ticket", "spec", "standards", "candidate", "merge"])
def test_each_rejection_can_repair_with_fresh_revision_bound_verification(harness, stage):
    reject_until(harness, stage, 1)
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    assert [a["state"] for a in record["attempts"]] == ["Rejected", "Done"]
    rejected, repaired = record["attempts"]
    assert rejected["failure"]["stage"] == ("candidate" if stage == "merge" else stage)
    assert rejected["submitted_revision"] != repaired["submitted_revision"]
    gates = [g for g in record["gates"] if g["attempt"] == 2]
    assert [g["stage"] for g in gates] == [
        "implementation",
        "check-ticket",
        "spec",
        "standards",
        "candidate",
    ]
    assert all(g["passed"] for g in gates)
    assert all(g["revision"] == repaired["submitted_revision"] for g in gates[1:4])
    for gate in gates[2:4]:
        assert gate["report"]["attempt"] == 2
    assignment = json.loads(Path(gates[0]["assignment"]).read_text())
    assert assignment["repair_context"]["failure"] == rejected["failure"]
    assert rejected["submitted_revision"] in assignment["repair_context"]["rejected_revisions"]
    if stage in ("spec", "standards"):
        failure = next(g for g in assignment["check_results"] if g["stage"] == stage)
        assert failure["report"]["findings"][0]["evidence"] == "Concrete review failure"
    if stage == "candidate":
        assert rejected["candidate_revision"] in assignment["repair_context"]["rejected_revisions"]
    candidate = repaired["candidate_revision"]
    assert harness.git("rev-parse", "integration") == candidate == gates[-1]["revision"]
    assert harness.git("show", "-s", "--format=%P", candidate).split() == [
        harness.base,
        repaired["submitted_revision"],
    ]
    assert harness.git("rev-parse", candidate + "^{tree}") == harness.git(
        "rev-parse", repaired["submitted_revision"] + "^{tree}"
    )
    assert (Path(rejected["source"]) / "attempt.txt").read_text() == "1"


@pytest.mark.parametrize("stage", ["check-ticket", "spec", "standards", "candidate", "merge"])
@pytest.mark.parametrize("allowance", [0, 1, 2])
def test_exhaustion_is_bounded_and_preserves_complete_attempt_history(harness, stage, allowance):
    harness.config["max_repairs"] = allowance
    reject_until(harness, stage, 100)
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "value.txt").write_text("caller unstaged\n")
    (harness.repo / "unrelated").write_text("caller untracked")
    before = harness.git("status", "--porcelain")
    result = harness.run_ticket()
    assert result.returncode == 1
    record = harness.record()
    assert record["outcome"] == "incomplete"
    assert record["ticket"]["state"] == "Blocked"
    assert record["ticket"]["attempt"] == allowance + 1
    assert "done_revision" not in record["ticket"]
    attempts = record["attempts"]
    assert [a["attempt"] for a in attempts] == list(range(1, allowance + 2))
    assert all(a["state"] == "Rejected" for a in attempts)
    assert len({a["submitted_revision"] for a in attempts}) == allowance + 1
    for attempt in attempts:
        number = attempt["attempt"]
        assert (Path(attempt["source"]) / "attempt.txt").read_text() == str(number)
        assert harness.git("show", attempt["submitted_revision"] + ":attempt.txt") == str(number)
        gates = record["gates"][attempt["gate_start"] : attempt["gate_end"]]
        assert all(g["attempt"] == number for g in gates)
        if stage != "merge":
            assert not gates[-1]["passed"]
        if stage == "candidate":
            assert gates[-1]["revision"] == attempt["candidate_revision"]
        for gate in gates:
            assert Path(gate["stdout"]).is_file()
            assert Path(gate["stderr"]).is_file()
    assert len({g["stdout"] for g in record["gates"]}) == len(record["gates"])
    assert harness.git("rev-parse", "integration") == harness.base
    assert harness.git("rev-parse", "HEAD") == harness.base
    assert harness.git("status", "--porcelain") == before
    assert harness.git("show", ":value.txt") == "caller staged"
    assert (harness.repo / "value.txt").read_text() == "caller unstaged\n"
    assert json.loads(harness.cli("status", harness.output).stdout) == record


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize(
    "mutation",
    [
        "sys.stdout.write(''); sys.exit(0)",
        "print('{broken'); sys.exit(0)",
        "print(json.dumps(report)); sys.exit(7)",
        "report['attempt'] = 1",
        "report['attempt'] = True",
        "print(json.dumps(report)[:-1] + ', \\\"extra\\\": 1e1000}'); sys.exit(0)",
    ],
    ids=["missing", "malformed", "nonzero", "stale", "mistyped", "overflow"],
)
def test_report_and_process_failures_share_the_repair_allowance(harness, role, mutation):
    # Reject attempt 1 concretely, then test failed repair reports at the same seam.
    reject_until(harness, "check-ticket" if role == "implementation" else role, 1)
    script = Path(harness.config["agent"][1])
    code = script.read_text()
    code = code.replace(
        "print(json.dumps(report))\n",
        f"if assignment['role'] == {role!r} and assignment['attempt'] > 1:\n"
        + "\n".join("    " + line for line in mutation.splitlines())
        + "\nprint(json.dumps(report))\n",
    )
    script.write_text(code)
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["outcome"] == "incomplete"
    assert record["ticket"]["state"] == "Blocked"
    assert record["ticket"]["attempt"] == 3
    assert len(record["attempts"]) == 3
    failures = [g for g in record["gates"] if g["stage"] == role and g["attempt"] > 1]
    assert [g["attempt"] for g in failures] == [2, 3]
    assert all(not g["passed"] for g in failures)
    if "exit(7)" in mutation:
        assert all(g["exit_code"] == 7 and g["report_status"] == "valid" for g in failures)
    else:
        assert all(g["report_status"] == "invalid" for g in failures)
    assert len({g["stdout"] for g in record["gates"]}) == len(record["gates"])
    assert harness.git("rev-parse", "integration") == harness.base
    assert "done_revision" not in record["ticket"]
    assert json.loads(harness.cli("status", harness.output).stdout) == record


@pytest.mark.parametrize("exit_code", [0, 7])
def test_valid_human_decision_stops_without_capture_or_repair(harness, exit_code):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    report.update(result='human-decision-needed', acceptance_evidence=[],\n"
        "        unresolved_questions=['Which requirement should take priority?'])\n"
        f"    print(json.dumps(report)); sys.exit({exit_code})",
    )
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["ticket"]["attempt"] == 1
    assert len(record["attempts"]) == 1
    assert [g["stage"] for g in record["gates"]] == ["baseline", "implementation"]
    assert record["gates"][-1]["report_status"] == "valid"
    assert (
        "human decision" in record["failure"]["message"] or "exit 7" in record["failure"]["message"]
    )
    assert "submitted_revision" not in record["ticket"]


@pytest.mark.parametrize("value", [-1, True, 2.0, "2", None, [], {}])
def test_invalid_allowance_is_rejected_before_any_process(harness, value):
    harness.config["max_repairs"] = value
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["outcome"] == "invalid-input"
    assert "max_repairs" in record["failure"]["message"]
    assert record["ticket"]["attempt"] == 0
    assert record["gates"] == record["attempts"] == []
    assert not list((harness.output / "worktrees").iterdir())


def test_failed_shared_baseline_consumes_no_repairs(harness):
    harness.config["suite"].append("baseline")
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["outcome"] == "environment"
    assert record["attempts"] == []
    assert record["ticket"]["attempt"] == 0
    assert [g["stage"] for g in record["gates"]] == ["baseline"]


def test_worker_internal_edit_iterations_are_one_attempt(harness):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    for value in ['3\\n', '4\\n', '2\\n']:\n"
        "        Path('value.txt').write_text(value)\n"
        "    subprocess.run([sys.executable, 'check.py', 'ticket'], check=True, "
        "stdout=sys.stderr, env={**os.environ, 'TICKET_HARNESS_STAGE': 'check-ticket'})",
    )
    assert harness.run_ticket().returncode == 0
    record = harness.record()
    assert record["ticket"]["attempt"] == 1
    assert len(record["attempts"]) == 1


def test_final_default_repair_gets_all_rejected_revision_and_gate_history(harness):
    reject_until(harness, "candidate", 2)
    assert harness.run_ticket().returncode == 0
    record = harness.record()
    assert record["ticket"]["attempt"] == 3
    assert [a["state"] for a in record["attempts"]] == ["Rejected", "Rejected", "Done"]
    worker = next(g for g in record["gates"] if g["attempt"] == 3)
    prompt = json.loads(Path(worker["assignment"]).read_text())
    expected = [
        a[key]
        for a in record["attempts"][:2]
        for key in ("submitted_revision", "candidate_revision")
    ]
    assert prompt["repair_context"]["rejected_revisions"] == expected
    assert [(g["attempt"], g["stage"]) for g in prompt["check_results"]] == [
        (0, "baseline"),
        (1, "implementation"),
        (1, "check-ticket"),
        (1, "spec"),
        (1, "standards"),
        (1, "candidate"),
        (2, "implementation"),
        (2, "check-ticket"),
        (2, "spec"),
        (2, "standards"),
        (2, "candidate"),
    ]


def test_repair_source_mutation_invalidates_approval_before_another_full_verification(harness):
    reject_until(harness, "spec", 1)
    script = Path(harness.config["agent"][1])
    script.write_text(
        script.read_text().replace(
            "print(json.dumps(report))\n",
            "if assignment['attempt'] == 2 and assignment['role'] == 'standards':\n"
            "    (Path.cwd().parent / 'attempt-2-spec/value.txt').write_text('unreviewed')\n"
            "print(json.dumps(report))\n",
        )
    )
    assert harness.run_ticket().returncode == 0
    record = harness.record()
    assert record["ticket"]["attempt"] == 3
    spec = next(g for g in record["gates"] if g["attempt"] == 2 and g["stage"] == "spec")
    assert not spec["passed"]
    assert spec["verification_status"] == "invalidated"
    assert (harness.output / "worktrees/attempt-2-spec/value.txt").read_text() == "unreviewed"
    assert [g["stage"] for g in record["gates"] if g["attempt"] == 3] == [
        "implementation",
        "check-ticket",
        "spec",
        "standards",
        "candidate",
    ]


def test_external_integration_change_after_rejection_does_not_authorize_repair(harness):
    reject_until(harness, "spec", 1)
    script = Path(harness.config["agent"][1])
    script.write_text(
        script.read_text().replace(
            "print(json.dumps(report))\n",
            "if assignment['role'] == 'spec':\n"
            "    external = subprocess.check_output(['git', 'commit-tree', 'HEAD^{tree}',\n"
            "        '-p', 'HEAD', '-m', 'External movement'], text=True).strip()\n"
            "    subprocess.run(['git', 'update-ref', 'refs/heads/integration', external], check=True)\n"
            "print(json.dumps(report))\n",
        )
    )
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["ticket"]["attempt"] == 1
    assert "changed externally" in record["failure"]["message"]
    assert harness.git("show", "-s", "--format=%s", "integration") == "External movement"


def test_repair_cannot_overwrite_earlier_attempt_evidence(harness):
    reject_until(harness, "spec", 1)
    script = Path(harness.config["agent"][1])
    target = harness.output / "artifacts/spec.stdout"
    script.write_text(
        script.read_text().replace(
            "print(json.dumps(report))\n",
            "if assignment['attempt'] == 2 and assignment['role'] == 'implementation':\n"
            f"    Path({str(target)!r}).write_text('overwritten')\n"
            "print(json.dumps(report))\n",
        )
    )
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["ticket"]["attempt"] == 2
    failure = record["gates"][-1]
    violation = next(item for item in failure["integrity"] if item["path"] == str(target))
    assert Path(violation["artifact"]).read_text() == "overwritten"
    assert json.loads(target.read_text())["findings"][0]["classification"] == "blocking"
    assert "integrity" in record["failure"]["message"].lower()


def test_numbered_check_names_cannot_collide_with_repair_artifacts(harness):
    reject_until(harness, "candidate", 1)
    harness.config["checks"]["ticket-2"] = harness.config["checks"]["ticket"]
    assert harness.run_ticket().returncode == 0
    record = harness.record()
    paths = [g["stdout"] for g in record["gates"]]
    assert len(set(paths)) == len(paths)
    for gate in record["gates"]:
        if gate["stage"].startswith("check-"):
            assert gate["revision"] in Path(gate["stdout"]).read_text()


def test_invalidated_shared_baseline_stops_before_starting_repairs(harness):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    (Path.cwd().parent / 'baseline/value.txt').write_text('changed baseline')",
    )
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["ticket"]["attempt"] == 1
    assert len(record["attempts"]) == 1
    assert record["gates"][0]["verification_status"] == "invalidated"
    assert not (harness.output / "worktrees/attempt-2-implementation").exists()
