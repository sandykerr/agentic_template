"""Human decisions at the public CLI/report seam with repair allowance available."""

import json
from pathlib import Path

import pytest
from test_cli import TicketFixture
from test_repairs import repair_agent

QUESTION = "May value.txt accept another value despite the approved ticket requiring 2?"
FINDING = {
    "id": "contract-conflict",
    "classification": "blocking",
    "location": "value.txt:1",
    "requirement": "Approved ticket: change value to 2; preserve the existing interface",
    "consequence": "Choosing another value changes the approved contract",
    "evidence": "The ticket requires 2; the requested extension needs another value",
    "resolution": QUESTION,
    "human_decision_needed": True,
}


@pytest.fixture
def harness():
    fixture = TicketFixture()
    fixture.setUp()
    del fixture.config["max_repairs"]
    try:
        yield fixture
    finally:
        fixture.doCleanups()


def decision_agent(harness, role, attempt=1, exit_code=0, mutation=""):
    repair_agent(
        harness,
        "if assignment['role'] == 'implementation':\n"
        "    Path('decision-work.txt').write_text('preserved current work')\n"
        "    if assignment['attempt'] == 1:\n"
        + ("        Path('value.txt').write_text('3\\n')\n" if attempt > 1 else "        pass\n")
        + f"if assignment['role'] == {role!r} and assignment['attempt'] >= {attempt}:\n"
        + (
            "    report.update(result='human-decision-needed',\n"
            "        summary='Approved ticket leaves the requested extension undecided',\n"
            "        acceptance_evidence=['value.txt and decision-work.txt remain inspectable'],\n"
            f"        unresolved_questions=[{QUESTION!r}])\n"
            if role == "implementation"
            else f"    report['findings'] = [{FINDING!r}]\n"
        )
        + "\n".join("    " + line for line in mutation.splitlines())
        + f"\n    print(json.dumps(report)); sys.exit({exit_code})",
    )


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize("attempt", [1, 2])
@pytest.mark.parametrize("exit_code", [0, 7])
def test_decision_blocks_immediately_with_contract_work_and_history(
    harness, role, attempt, exit_code
):
    decision_agent(harness, role, attempt, exit_code)
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "value.txt").write_text("caller unstaged\n")
    (harness.repo / "unrelated").write_text("caller untracked")
    caller_status = harness.git("status", "--porcelain")
    approved_paths = [harness.repo / harness.config[name] for name in ("spec", "ticket")]
    approved_paths += [harness.repo / path for path in harness.config["standards"]]
    approved = {path: path.read_bytes() for path in approved_paths}
    result = harness.run_ticket()
    assert result.returncode == 1
    record = harness.record()
    assert record["max_repairs"] == 2
    assert len(record["attempts"]) == record["ticket"]["attempt"] == attempt
    assert record["outcome"] == "incomplete"
    assert record["ticket"]["state"] == "Blocked"
    assert "done_revision" not in record["ticket"]
    decision = record["ticket"]["human_decision"]
    assert decision == record["attempts"][-1]["human_decision"]
    assert decision["role"] == role
    assert decision["attempt"] == attempt
    if role == "implementation":
        assert decision["report"]["unresolved_questions"] == [QUESTION]
        assert decision["report"]["acceptance_evidence"]
        assert "submitted_revision" not in record["ticket"]
        assert not any(
            op["attempt"] == attempt and op["stage"].endswith("submission")
            for op in record["operations"]
        )
    else:
        assert decision["report"]["findings"] == [FINDING]
        assert decision["revision"] == record["ticket"]["submitted_revision"]
    assert decision["approved_inputs"] == record["inputs"]
    assert json.loads(Path(decision["stdout"]).read_text()) == decision["report"]
    assignment = json.loads(Path(decision["assignment"]).read_text())
    assert assignment["revision"] == decision["revision"]
    assert assignment["base_revision"] == harness.base
    assert QUESTION in record["failure"]["message"]
    for snapshot in decision["approved_inputs"].values():
        assert Path(snapshot["artifact"]).read_bytes() == Path(snapshot["source"]).read_bytes()
    assert {path: path.read_bytes() for path in approved} == approved
    gates = record["gates"]
    assert gates[-1]["stage"] == role
    assert gates[-1]["report_status"] == "valid"
    assert gates[-1]["exit_code"] == exit_code
    assert not gates[-1]["passed"]
    if exit_code:
        assert "process exit 7" in gates[-1]["diagnostic"]
    stages = ["implementation", "check-ticket", "spec", "standards"]
    assert [g["stage"] for g in gates if g["attempt"] == attempt] == stages[
        : stages.index(role) + 1
    ]
    assert all(op["attempt"] <= attempt for op in record["operations"])
    assert not any("candidate" in op["stage"] for op in record["operations"])
    assert not (harness.output / f"worktrees/attempt-{attempt + 1}-implementation").exists()
    for item in record["attempts"]:
        assert item["state"] == "Rejected"
        history = gates[item["gate_start"] : item["gate_end"]]
        assert all(g["attempt"] == item["attempt"] for g in history)
        assert (Path(item["source"]) / "decision-work.txt").read_text() == "preserved current work"
        for gate in history:
            assert Path(gate["stdout"]).exists()
            assert Path(gate["stderr"]).exists()
    assert (Path(record["attempts"][-1]["source"]) / "value.txt").read_text() == "2\n"
    if attempt > 1:
        first = record["attempts"][0]
        assert first["failure"]["stage"] == "check-ticket"
        assert harness.git("show", first["submitted_revision"] + ":value.txt") == "3"
        assert (Path(first["source"]) / "value.txt").read_text() == "3\n"
        assert assignment["check_results"][:3] == gates[:3]
        worker = next(g for g in gates if g["attempt"] == attempt)
        prompt = json.loads(Path(worker["assignment"]).read_text())
        assert prompt["repair_context"]["rejected_revisions"] == [first["submitted_revision"]]
        assert worker["report"]["before"] == "3\n"
    assert harness.git("rev-parse", "integration") == harness.base
    assert harness.git("rev-parse", "HEAD") == harness.base
    assert harness.git("show", ":value.txt") == "caller staged"
    assert (harness.repo / "value.txt").read_text() == "caller unstaged\n"
    assert (harness.repo / "unrelated").read_text() == "caller untracked"
    assert harness.git("status", "--porcelain") == caller_status
    durable = (harness.output / "run.json").read_bytes()
    assert json.loads(result.stdout) == record
    assert json.loads(harness.cli("status", harness.output).stdout) == record
    assert (harness.output / "run.json").read_bytes() == durable
    assert harness.git("status", "--porcelain") == caller_status


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_decision_takes_precedence_over_repairable_findings_in_same_review(harness, role):
    findings = [
        {**FINDING, "id": "repairable", "human_decision_needed": False},
        {**FINDING, "id": "suggestion", "classification": "optional"},
        FINDING,
        {**FINDING, "id": "second-decision", "resolution": "Which interface is approved?"},
    ]
    decision_agent(harness, role, mutation=f"report['findings'] = {findings!r}")
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert len(record["attempts"]) == record["ticket"]["attempt"] == 1
    assert record["ticket"]["human_decision"]["report"]["findings"] == findings
    assert QUESTION in record["failure"]["message"]
    assert "Which interface is approved?" in record["failure"]["message"]
    assert record["gates"][-1]["stage"] == role
    assert harness.git("rev-parse", "integration") == harness.base


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_optional_decision_flag_preserves_ordinary_nonblocking_behavior(harness, role):
    suggestion = {**FINDING, "classification": "optional"}
    decision_agent(harness, role, mutation=f"report['findings'] = [{suggestion!r}]")
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    assert record["outcome"] == "completed"
    assert record["ticket"]["attempt"] == len(record["attempts"]) == 1
    assert "human_decision" not in record["ticket"]
    review = next(g for g in record["gates"] if g["stage"] == role)
    assert review["report"]["findings"] == [suggestion]
    assert review["passed"]
    assert harness.git("rev-parse", "integration") == record["ticket"]["done_revision"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize(
    "invalid",
    [
        "incomplete",
        "stale",
        "mistyped-identity",
        "mistyped-evidence",
        "duplicate",
        "overflow",
        "deep",
    ],
)
def test_invalid_decision_like_output_is_untrusted_and_uses_bounded_repairs(harness, role, invalid):
    mutation = {
        "incomplete": "del report['summary']"
        if role == "implementation"
        else "report['findings'].append({'id': 'incomplete', 'classification': 'optional'})",
        "stale": "report['revision'] = 'stale'",
        "mistyped-identity": "report['attempt'] = True",
        "mistyped-evidence": "report['unresolved_questions'] = [True]"
        if role == "implementation"
        else "report['findings'][0]['human_decision_needed'] = 'true'",
        "duplicate": 'print(json.dumps(report)[:-1] + \', \\"role\\": \\"implementation\\"}\'); sys.exit(0)',
        "overflow": "print(json.dumps(report)[:-1] + ', \\\"extra\\\": 1e1000}'); sys.exit(0)",
        "deep": "nested = []\nfor _ in range(101):\n    nested = [nested]\nreport['extra'] = nested",
    }[invalid]
    decision_agent(harness, role, mutation=mutation)
    assert harness.run_ticket().returncode == 1
    record = harness.record()
    assert record["outcome"] == "incomplete"
    assert record["ticket"]["state"] == "Blocked"
    assert record["ticket"]["attempt"] == len(record["attempts"]) == 3
    assert "human_decision" not in record["ticket"]
    assert all("human_decision" not in attempt for attempt in record["attempts"])
    reports = [g for g in record["gates"] if g["stage"] == role]
    assert len(reports) == 3
    assert all(g["report_status"] == "invalid" and not g["passed"] for g in reports)
    diagnostic = {
        "incomplete": "summary" if role == "implementation" else "findings",
        "stale": "revision",
        "mistyped-identity": "attempt",
        "mistyped-evidence": "unresolved_questions"
        if role == "implementation"
        else "human_decision_needed",
        "duplicate": "duplicate report key",
        "overflow": "nonfinite",
        "deep": "nesting",
    }[invalid]
    assert all(diagnostic in gate["diagnostic"] for gate in reports)
    assert harness.git("rev-parse", "integration") == harness.base
    assert json.loads(harness.cli("status", harness.output).stdout) == record
