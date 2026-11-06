"""Report acceptance through external processes, the CLI, and durable Git evidence."""

import pytest
from test_cli import TicketFixture


class ReportFixture(TicketFixture):
    def agent_report(self, role, mutation):
        wrapper = self.home / "report_agent.py"
        wrapper.write_text(
            "import json, subprocess, sys\n"
            "assignment = json.load(sys.stdin)\n"
            f"result = subprocess.run([sys.executable, {str(self.repo / 'agent.py')!r}], "
            "input=json.dumps(assignment), text=True, capture_output=True)\n"
            "report = json.loads(result.stdout)\n"
            f"if assignment['role'] == {role!r}:\n"
            + "\n".join("    " + line for line in mutation.splitlines())
            + "\nprint(json.dumps(report))\n"
        )
        self.config["agent"] = [self.config["agent"][0], str(wrapper)]


@pytest.fixture
def harness():
    fixture = ReportFixture()
    fixture.setUp()
    try:
        yield fixture
    finally:
        fixture.doCleanups()


def test_incomplete_implementation_evidence_cannot_submit(harness):
    harness.agent_report("implementation", "del report['acceptance_evidence']")
    record = harness.assert_rejected_gate("implementation")
    assert "acceptance_evidence" in record["failure"]["message"]
    assert "submitted_revision" not in record["ticket"]


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_incomplete_optional_finding_cannot_satisfy_review(harness, role):
    harness.agent_report(role, "report['findings'] = [{'classification': 'optional'}]")
    record = harness.assert_rejected_gate(role)
    assert "finding" in record["failure"]["message"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
def test_boolean_attempt_is_not_assignment_identity(harness, role):
    harness.agent_report(role, "report['attempt'] = True")
    record = harness.assert_rejected_gate(role)
    assert "attempt" in record["failure"]["message"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
def test_rejected_report_is_visible_in_status_with_diagnostics(harness, role):
    harness.agent_report(role, "report['ticket'] = '99'")
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["report"]["ticket"] == "99"
    assert gate["report_status"] == "invalid"
    assert "ticket" in gate["diagnostic"]
    assert gate["exit_code"] == 0


def test_human_decision_report_is_valid_but_cannot_submit_or_launch_reviews(harness):
    harness.agent_report(
        "implementation",
        "report.update(result='human-decision-needed', acceptance_evidence=[], "
        "unresolved_questions=['Which approved behavior should take priority?'])",
    )
    record = harness.assert_rejected_gate("implementation")
    gate = record["gates"][-1]
    assert gate["report_status"] == "valid"
    assert gate["report"]["result"] == "human-decision-needed"
    assert "human decision" in record["failure"]["message"]
    assert [gate["stage"] for gate in record["gates"]] == ["baseline", "implementation"]
    assert "submitted_revision" not in record["ticket"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
def test_nonzero_exit_rejects_even_complete_success_report(harness, role):
    harness.agent_report(role, "print(json.dumps(report)); sys.exit(7)")
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["exit_code"] == 7
    assert gate["report"]["role"] == role
    assert gate["report_status"] == "valid"
    assert "exit 7" in gate["diagnostic"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize(
    "payload",
    ["sys.stdout.write('{broken')", "sys.stdout.write('')", "print('[]')", "print('null')"],
    ids=["malformed", "missing", "array", "null"],
)
def test_invalid_document_cannot_pass_on_zero_exit(harness, role, payload):
    harness.agent_report(role, payload + "; sys.exit(0)")
    record = harness.assert_rejected_gate(role)
    assert record["gates"][-1]["exit_code"] == 0
    assert record["gates"][-1]["report_status"] == "invalid"


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize("field", ["role", "ticket", "attempt", "base_revision", "revision"])
@pytest.mark.parametrize("mutation", ["missing", "mismatch", "wrong-type"])
def test_report_identity_must_match_assignment(harness, role, field, mutation):
    change = {
        "missing": f"del report[{field!r}]",
        "mismatch": f"report[{field!r}] = " + ("2" if field == "attempt" else "'wrong'"),
        "wrong-type": f"report[{field!r}] = []",
    }[mutation]
    harness.agent_report(role, change)
    record = harness.assert_rejected_gate(role)
    assert field in record["failure"]["message"]


@pytest.mark.parametrize(
    "field", ["summary", "changed_files", "checks", "acceptance_evidence", "unresolved_questions"]
)
@pytest.mark.parametrize("mutation", ["missing", "wrong-type", "blank-item"])
def test_implementation_requires_complete_typed_evidence(harness, field, mutation):
    change = {
        "missing": f"del report[{field!r}]",
        "wrong-type": f"report[{field!r}] = {{}}",
        "blank-item": f"report[{field!r}] = " + ("'  '" if field == "summary" else "['  ']"),
    }[mutation]
    harness.agent_report("implementation", change)
    record = harness.assert_rejected_gate("implementation")
    assert field in record["failure"]["message"]


FINDING = {
    "id": "stable-finding",
    "classification": "optional",
    "location": "value.txt:1",
    "requirement": "Keep the fixture easy to read",
    "consequence": "Readers may overlook the meaning of the value",
    "evidence": "The value has no accompanying explanation",
    "resolution": "Consider documenting the value",
    "human_decision_needed": False,
}


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("field", list(FINDING))
@pytest.mark.parametrize("mutation", ["missing", "wrong-type"])
def test_findings_require_every_typed_field(harness, role, field, mutation):
    finding = {**FINDING}
    if mutation == "missing":
        del finding[field]
    else:
        finding[field] = 1
    harness.agent_report(role, f"report['findings'] = [{finding!r}]")
    record = harness.assert_rejected_gate(role)
    assert field in record["failure"]["message"]


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize(
    "findings",
    [None, {}, [None], [FINDING, FINDING]],
    ids=["null", "object", "null-finding", "duplicate-id"],
)
def test_invalid_findings_cannot_satisfy_review(harness, role, findings):
    harness.agent_report(role, f"report['findings'] = {findings!r}")
    record = harness.assert_rejected_gate(role)
    assert "findings" in record["failure"]["message"]


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_complete_optional_finding_is_accepted_and_preserved(harness, role):
    harness.agent_report(role, f"report['findings'] = [{FINDING!r}]")
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    gate = next(gate for gate in record["gates"] if gate["stage"] == role)
    assert gate["report"]["findings"] == [FINDING]
    assert gate["report_status"] == "valid"
    assert record["ticket"]["attempt"] == 1


def test_git_and_independent_checks_override_worker_claims(harness):
    harness.agent_report(
        "implementation",
        "report.update(changed_files=['imaginary.txt'], checks=['claimed pass'], "
        "submitted_revision='invented', done_revision='invented', state='Done')",
    )
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = harness.record()
    ticket = record["ticket"]
    assert ticket["changed_files"] == ["value.txt"]
    assert (
        harness.git("diff", "--name-only", harness.base, ticket["submitted_revision"])
        == "value.txt"
    )
    assert ticket["done_revision"] == harness.git("rev-parse", "integration")
    assert all(gate["passed"] for gate in record["gates"])
    assert all(
        gate["revision"] == ticket["submitted_revision"]
        for gate in record["gates"]
        if gate["stage"] in ("check-ticket", "spec", "standards")
    )
    assert record["gates"][1]["report"]["changed_files"] == ["imaginary.txt"]


@pytest.mark.parametrize("result", ["Done", "completed", True, None])
def test_worker_cannot_declare_done_or_invent_an_outcome(harness, result):
    harness.agent_report("implementation", f"report['result'] = {result!r}")
    record = harness.assert_rejected_gate("implementation")
    assert "result" in record["failure"]["message"]


@pytest.mark.parametrize(
    "result, field",
    [("submitted", "acceptance_evidence"), ("human-decision-needed", "unresolved_questions")],
)
def test_outcomes_require_their_supporting_evidence(harness, result, field):
    harness.agent_report("implementation", f"report.update(result={result!r}, {field}=[])")
    record = harness.assert_rejected_gate("implementation")
    assert field in record["failure"]["message"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize(
    "payload, diagnostic",
    [
        ("print(json.dumps(report)[:-1] + ',\"attempt\":1}')", "duplicate"),
        ("print(json.dumps(report)[:-1] + ',\"extra\":NaN}')", "constant"),
        ("print(json.dumps(report)[:-1] + ',\"extra\":1e400}')", "nonfinite"),
        ('print(json.dumps(report)[:-1] + \',"extra":{"nested":[-1e400]}}\')', "nonfinite"),
    ],
    ids=["duplicate-key", "non-finite-number", "overflowing-number", "nested-overflow"],
)
def test_ambiguous_or_non_json_reports_are_rejected(harness, role, payload, diagnostic):
    harness.agent_report(role, payload + "; sys.exit(0)")
    record = harness.assert_rejected_gate(role)
    assert diagnostic in record["failure"]["message"]


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_review_for_previous_source_revision_is_stale(harness, role):
    harness.agent_report(role, "report['revision'] = assignment['base_revision']")
    record = harness.assert_rejected_gate(role)
    assert "revision" in record["failure"]["message"]
    assert record["ticket"]["submitted_revision"] != harness.base


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_review_cannot_omit_findings(harness, role):
    harness.agent_report(role, "del report['findings']")
    record = harness.assert_rejected_gate(role)
    assert "findings" in record["failure"]["message"]


@pytest.mark.parametrize(
    "field", ["changed_files", "checks", "acceptance_evidence", "unresolved_questions"]
)
def test_implementation_evidence_elements_must_be_strings(harness, field):
    harness.agent_report("implementation", f"report[{field!r}] = [1]")
    record = harness.assert_rejected_gate("implementation")
    assert field in record["failure"]["message"]


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize(
    "field", ["id", "location", "requirement", "consequence", "evidence", "resolution"]
)
def test_finding_evidence_must_not_be_blank(harness, role, field):
    finding = {**FINDING, field: "   "}
    harness.agent_report(role, f"report['findings'] = [{finding!r}]")
    record = harness.assert_rejected_gate(role)
    assert field in record["failure"]["message"]


def test_claimed_success_cannot_override_independent_check_failure(harness):
    harness.agent_report("implementation", "report['checks'] = ['Everything passed']")
    harness.config["checks"]["ticket"].append("check-ticket")
    record = harness.assert_rejected_gate("check-ticket")
    assert record["gates"][1]["report"]["checks"] == ["Everything passed"]


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("field", ["consequence", "evidence"])
def test_incomplete_blocker_is_invalid_rather_than_a_valid_blocking_review(harness, role, field):
    finding = {**FINDING, "classification": "blocking"}
    del finding[field]
    harness.agent_report(role, f"report['findings'] = [{finding!r}]")
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["report_status"] == "invalid"
    assert field in gate["diagnostic"]
    assert gate["report"]["findings"] == [finding]


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_complete_blocker_is_valid_but_prevents_integration(harness, role):
    finding = {**FINDING, "classification": "blocking"}
    harness.agent_report(role, f"report['findings'] = [{finding!r}]")
    record = harness.assert_rejected_gate(role)
    assert record["gates"][-1]["report_status"] == "valid"
    assert "blocking" in record["gates"][-1]["diagnostic"]


def test_implementation_cannot_omit_result(harness):
    harness.agent_report("implementation", "del report['result']")
    record = harness.assert_rejected_gate("implementation")
    assert "result" in record["failure"]["message"]


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize("mismatched_ticket", [False, True])
def test_excessive_nesting_preserves_a_durable_rejection(harness, role, mismatched_ticket):
    mutation = "report['ticket'] = '99'\n" if mismatched_ticket else ""
    mutation += (
        "print(json.dumps(report)[:-1] + ',\"extra\":' + '[' * 990 + '0' + ']' * 990 + '}')\n"
        "sys.exit(0)"
    )
    harness.agent_report(role, mutation)
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["exit_code"] == 0
    assert gate["report_status"] == "invalid"
    assert "nesting" in gate["diagnostic"]
    assert "report" not in gate


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
def test_supported_diagnostic_nesting_can_complete(harness, role):
    # Report object plus 99 arrays is the documented 100-container boundary.
    harness.agent_report(
        role,
        "print(json.dumps(report)[:-1] + ',\"extra\":' + '[' * 99 + '0' + ']' * 99 + '}')\n"
        "sys.exit(0)",
    )
    result = harness.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    assert harness.record()["outcome"] == "completed"
