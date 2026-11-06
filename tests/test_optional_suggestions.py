"""Optional suggestions through the public CLI, revision reports, and real Git."""

import json
from pathlib import Path

import pytest
from test_cli import TicketFixture
from test_human_decisions import FINDING
from test_repairs import repair_agent

SUGGESTION = {
    "id": "value-style",
    "classification": "optional",
    "location": "value.txt:1",
    "requirement": "Optional readability preference; the approved value is already correct",
    "consequence": "No acceptance behavior is affected",
    "evidence": "value.txt contains the required value 2",
    "resolution": "Consider adding a comment in a future change",
    "human_decision_needed": False,
}
BLOCKER = {**FINDING, "human_decision_needed": False}


@pytest.fixture
def harness():
    fixture = TicketFixture()
    fixture.setUp()
    del fixture.config["max_repairs"]
    try:
        yield fixture
    finally:
        fixture.doCleanups()


def suggestions_agent(harness, reports, mutation=""):
    repair_agent(
        harness,
        "if assignment['role'] != 'implementation':\n"
        f"    reports = {reports!r}\n"
        "    report['findings'] = reports.get(assignment['attempt'], {}).get(assignment['role'], [])\n"
        + mutation,
    )


def assert_result(harness, result, completed):
    record = harness.record()
    assert result.returncode == (0 if completed else 1), result.stdout + result.stderr
    assert record["outcome"] == ("completed" if completed else "incomplete")
    assert record["ticket"]["state"] == ("Done" if completed else "Blocked")
    assert record["max_repairs"] == 2
    assert json.loads(result.stdout) == record
    durable = (harness.output / "run.json").read_bytes()
    status = harness.cli("status", harness.output)
    assert status.returncode == 0, status.stderr
    assert json.loads(status.stdout) == record
    assert (harness.output / "run.json").read_bytes() == durable
    for snapshot in record["inputs"].values():
        assert Path(snapshot["source"]).read_bytes() == Path(snapshot["artifact"]).read_bytes()
    for attempt in record["attempts"]:
        gates = record["gates"][attempt["gate_start"] : attempt["gate_end"]]
        assert all(g["attempt"] == attempt["attempt"] for g in gates)
        for gate in gates:
            assert Path(gate["stdout"]).is_file()
            assert Path(gate["stderr"]).is_file()
            if gate["stage"] in ("spec", "standards"):
                assert gate["revision"] == attempt["submitted_revision"]
                report = gate["report"]
                prompt = json.loads(Path(gate["assignment"]).read_text())
                assert prompt["revision"] == gate["revision"]
                if gate["report_status"] == "valid":
                    assert report["revision"] == gate["revision"]
                    assert report["base_revision"] == harness.base
                    assert report["attempt"] == attempt["attempt"]
                    assert report["role"] == gate["stage"]
                    assert report["ticket"] == "01"
                assert json.loads(Path(gate["stdout"]).read_text()) == report
    if completed:
        submitted = record["ticket"]["submitted_revision"]
        candidate = record["ticket"]["done_revision"]
        assert harness.git("rev-parse", "integration") == candidate
        assert record["gates"][-1]["revision"] == candidate
        assert record["gates"][-1]["passed"]
        assert harness.git("show", "-s", "--format=%P", candidate).split() == [
            harness.base,
            submitted,
        ]
        assert harness.git("rev-parse", candidate + "^{tree}") == harness.git(
            "rev-parse", submitted + "^{tree}"
        )
        assert harness.git("show", candidate + ":value.txt") == "2"
    else:
        assert harness.git("rev-parse", "integration") == harness.base
        assert "done_revision" not in record["ticket"]
    return record


@pytest.mark.parametrize("roles", [("spec",), ("standards",), ("spec", "standards")])
@pytest.mark.parametrize("decision_flag", [False, True])
def test_optional_only_integrates_without_spending_available_repairs(harness, roles, decision_flag):
    suggestion = {**SUGGESTION, "human_decision_needed": decision_flag}
    suggestions_agent(harness, {1: {role: [suggestion] for role in roles}})
    # Preserve distinct staged/unstaged bytes and untracked caller work.
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "value.txt").write_text("caller unstaged\n")
    (harness.repo / "unrelated").write_text("caller untracked")
    caller_status = harness.git("status", "--porcelain")
    record = assert_result(harness, harness.run_ticket(), completed=True)
    assert len(record["attempts"]) == record["ticket"]["attempt"] == 1
    assert "human_decision" not in record["ticket"]
    assert [(g["attempt"], g["stage"]) for g in record["gates"]] == [
        (0, "baseline"),
        (1, "implementation"),
        (1, "check-ticket"),
        (1, "spec"),
        (1, "standards"),
        (1, "candidate"),
    ]
    assert all(g["passed"] for g in record["gates"])
    for role in ("spec", "standards"):
        gate = next(g for g in record["gates"] if g["stage"] == role)
        assert gate["report"]["findings"] == ([suggestion] if role in roles else [])
        assert gate["report_status"] == "valid"
    assert not (harness.output / "worktrees/attempt-2-implementation").exists()
    assert not any(op["attempt"] > 1 for op in record["operations"])
    assert harness.git("rev-parse", "HEAD") == harness.base
    assert harness.git("status", "--porcelain") == caller_status
    assert harness.git("show", ":value.txt") == "caller staged"
    assert (harness.repo / "value.txt").read_text() == "caller unstaged\n"
    assert (harness.repo / "unrelated").read_text() == "caller untracked"


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("exhausted", [False, True])
def test_mixed_findings_repair_only_blockers_and_keep_optional_evidence(harness, role, exhausted):
    findings = [SUGGESTION, BLOCKER]
    suggestions_agent(
        harness,
        {
            1: {role: findings},
            2: {role: findings if exhausted else [SUGGESTION]},
            3: {role: findings},
        },
    )
    record = assert_result(harness, harness.run_ticket(), completed=not exhausted)
    expected_attempts = 3 if exhausted else 2
    assert len(record["attempts"]) == record["ticket"]["attempt"] == expected_attempts
    assert "human_decision" not in record["ticket"]
    submissions = [a["submitted_revision"] for a in record["attempts"]]
    assert len(set(submissions)) == expected_attempts
    workers = [g for g in record["gates"] if g["stage"] == "implementation"]
    assert len({g["report"]["pid"] for g in workers}) == expected_attempts
    assert len({g["cwd"] for g in workers}) == expected_attempts
    for attempt in record["attempts"]:
        number = attempt["attempt"]
        gates = record["gates"][attempt["gate_start"] : attempt["gate_end"]]
        rejected = exhausted or number == 1
        expected_stages = ["implementation", "check-ticket", "spec", "standards", "candidate"]
        if rejected:
            expected_stages = expected_stages[: expected_stages.index(role) + 1]
            assert attempt["failure"]["stage"] == role
            assert "blocking review finding" in attempt["failure"]["message"]
            assert SUGGESTION["resolution"] not in attempt["failure"]["message"]
        assert [g["stage"] for g in gates] == expected_stages
        review = next(g for g in gates if g["stage"] == role)
        assert review["report_status"] == "valid"
        assert review["passed"] == (not rejected)
        assert review["report"]["findings"] == (findings if rejected else [SUGGESTION])
        if number > 1:
            prompt = json.loads(Path(gates[0]["assignment"]).read_text())
            assert prompt["revision"] == submissions[number - 2]
            assert prompt["repair_context"] == {
                "failure": record["attempts"][number - 2]["failure"],
                "rejected_revisions": submissions[: number - 1],
            }
            assert prompt["check_results"] == record["gates"][: attempt["gate_start"]]
            previous = next(
                g
                for g in prompt["check_results"]
                if g["attempt"] == number - 1 and g["stage"] == role
            )
            assert previous["report"]["findings"] == findings
            assert previous["revision"] == submissions[number - 2]
    # The optional comment was never implemented, yet all required gates can pass.
    assert harness.git("show", submissions[-1] + ":value.txt") == "2"
    assert not (
        harness.output / f"worktrees/attempt-{expected_attempts + 1}-implementation"
    ).exists()


def test_suggestions_appear_and_disappear_without_transferring_approval_between_revisions(harness):
    first = {**SUGGESTION, "evidence": "First submitted revision's optional style observation"}
    second = {**SUGGESTION, "evidence": "Second submitted revision's different observation"}
    third = {**SUGGESTION, "evidence": "Third submitted revision's new style observation"}
    reports = {
        1: {"spec": [first], "standards": [first]},
        2: {"standards": [second]},
        3: {"spec": [third]},
    }
    suggestions_agent(
        harness,
        reports,
        "if assignment['role'] == 'implementation':\n"
        "    Path('attempt.txt').write_text(str(assignment['attempt']))",
    )
    suite = harness.home / "candidate-check.py"
    suite.write_text(
        "import os, subprocess, sys\nfrom pathlib import Path\n"
        "subprocess.run([sys.executable, 'check.py', 'suite'], check=True)\n"
        "if os.environ['TICKET_HARNESS_STAGE'] == 'candidate':\n"
        "    assert int(Path('attempt.txt').read_text()) == 3, 'controlled candidate rejection'\n"
    )
    harness.config["suite"] = [harness.config["agent"][0], str(suite)]
    record = assert_result(harness, harness.run_ticket(), completed=True)
    assert record["ticket"]["attempt"] == len(record["attempts"]) == 3
    assert [a["state"] for a in record["attempts"]] == ["Rejected", "Rejected", "Done"]
    submissions = [a["submitted_revision"] for a in record["attempts"]]
    assert len(set(submissions)) == 3
    assert len({a["candidate_revision"] for a in record["attempts"]}) == 3
    for attempt in record["attempts"]:
        number = attempt["attempt"]
        gates = record["gates"][attempt["gate_start"] : attempt["gate_end"]]
        assert [g["stage"] for g in gates] == [
            "implementation",
            "check-ticket",
            "spec",
            "standards",
            "candidate",
        ]
        assert all(g["passed"] for g in gates[:-1])
        assert gates[-1]["passed"] == (number == 3)
        assert gates[-1]["revision"] == attempt["candidate_revision"]
        for gate in gates[2:4]:
            assert gate["report"]["findings"] == reports[number].get(gate["stage"], [])
            assert gate["revision"] == submissions[number - 1]
        prompt = json.loads(Path(gates[0]["assignment"]).read_text())
        assert prompt["check_results"] == record["gates"][: attempt["gate_start"]]
        if number > 1:
            assert prompt["revision"] == submissions[number - 2]
            assert prompt["repair_context"]["failure"]["stage"] == "candidate"
        assert (Path(attempt["source"]) / "attempt.txt").read_text() == str(number)
    assert harness.git("show", "integration:attempt.txt") == "3"


def test_optional_spec_findings_survive_a_later_standards_rejection(harness):
    suggestions_agent(
        harness,
        {1: {"spec": [SUGGESTION], "standards": [BLOCKER]}, 2: {"standards": [SUGGESTION]}},
    )
    record = assert_result(harness, harness.run_ticket(), completed=True)
    assert len(record["attempts"]) == record["ticket"]["attempt"] == 2
    first, second = record["attempts"]
    assert first["failure"]["stage"] == "standards"
    assert first["submitted_revision"] != second["submitted_revision"]
    reviews = [g for g in record["gates"] if g["stage"] in ("spec", "standards")]
    assert [(g["attempt"], g["stage"], g["passed"]) for g in reviews] == [
        (1, "spec", True),
        (1, "standards", False),
        (2, "spec", True),
        (2, "standards", True),
    ]
    assert [g["report"]["findings"] for g in reviews] == [[SUGGESTION], [BLOCKER], [], [SUGGESTION]]
    worker = next(
        g for g in record["gates"] if g["stage"] == "implementation" and g["attempt"] == 2
    )
    prompt = json.loads(Path(worker["assignment"]).read_text())
    assert prompt["check_results"] == record["gates"][: second["gate_start"]]
    assert prompt["repair_context"]["failure"] == first["failure"]


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("failure", ["incomplete", "stale", "nonzero"])
def test_optional_evidence_never_hides_invalid_reports_or_process_failures(harness, role, failure):
    findings = [SUGGESTION]
    if failure == "incomplete":
        # A complete blocker before malformed optional evidence cannot short-circuit validation.
        findings += [BLOCKER, {"id": "broken-optional", "classification": "optional"}]
    mutation = {
        "incomplete": "",
        "stale": f"if assignment['role'] == {role!r}:\n"
        "    report['revision'] = assignment['base_revision']",
        "nonzero": f"if assignment['role'] == {role!r}:\n"
        "    print(json.dumps(report)); sys.exit(7)",
    }[failure]
    suggestions_agent(harness, {n: {role: findings} for n in (1, 2, 3)}, mutation)
    record = assert_result(harness, harness.run_ticket(), completed=False)
    assert record["ticket"]["attempt"] == len(record["attempts"]) == 3
    assert "human_decision" not in record["ticket"]
    reviews = [g for g in record["gates"] if g["stage"] == role]
    assert len(reviews) == 3
    assert all(not g["passed"] for g in reviews)
    for review in reviews:
        assert review["report_status"] == ("valid" if failure == "nonzero" else "invalid")
        if failure == "nonzero":
            assert review["exit_code"] == 7
        elif failure == "stale":
            assert "mismatched revision" in review["diagnostic"]
        else:
            assert "findings[2]" in review["diagnostic"]
    assert not any(g["stage"] == "candidate" for g in record["gates"])


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("exit_code", [0, 7])
def test_optional_suggestions_do_not_delay_a_blocking_human_decision(harness, role, exit_code):
    findings = [SUGGESTION, BLOCKER, FINDING]
    # Distinct IDs are required even when multiple findings describe the same contract.
    findings[1] = {**BLOCKER, "id": "ordinary-blocker"}
    suggestions_agent(
        harness,
        {1: {role: findings}},
        f"if assignment['role'] == {role!r}:\n    print(json.dumps(report)); sys.exit({exit_code})",
    )
    record = assert_result(harness, harness.run_ticket(), completed=False)
    assert record["ticket"]["attempt"] == len(record["attempts"]) == 1
    assert record["ticket"]["human_decision"] == record["attempts"][0]["human_decision"]
    assert record["ticket"]["human_decision"]["report"]["findings"] == findings
    assert record["gates"][-1]["stage"] == role
    assert record["gates"][-1]["exit_code"] == exit_code
    assert record["gates"][-1]["report_status"] == "valid"
    assert not (harness.output / "worktrees/attempt-2-implementation").exists()
    assert not any("candidate" in op["stage"] for op in record["operations"])
