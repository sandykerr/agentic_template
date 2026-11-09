"""Approved milestone boundaries at the public CLI/process/Git seam."""

import hashlib
import json
from pathlib import Path

import pytest
import test_dependencies
from test_dependencies import launches
from test_preflight import reject

graph = test_dependencies.graph


def configure_plan(graph):
    graph.git("branch", "dev")
    graph.config.pop("selected_tickets")
    graph.config["ticket"] = "01-value.md"
    graph.config["plan"] = "plan.json"
    plan = {
        "version": "v1",
        "approval": "human-approved fixture bundle v1",
        "development": "dev",
        "required_tickets": ["01", "02", "03", "04"],
        "milestones": [
            {
                "id": "M1",
                "tickets": ["03", "01"],
                "qa": {
                    "setup": "Inspect disposable feature",
                    "actions": ["Read delivered work"],
                    "pass_conditions": ["Work 01 and 03 exist"],
                },
            },
            {
                "id": "M2",
                "tickets": ["04", "02"],
                "qa": {
                    "setup": "Inspect all work",
                    "actions": ["Read all delivered work"],
                    "pass_conditions": ["All required work exists"],
                },
            },
        ],
        "final_milestone": "M2",
        "final_coverage": ["01", "02", "03", "04"],
        "roles": {
            "worker": {"model": "scripted-fixture"},
            "spec": {"model": "scripted-spec"},
            "standards": {"model": "scripted-standards"},
        },
        "worker_overrides": {"03": {"reasoning": "High", "reason": "Fixture override"}},
    }
    write_plan(graph, plan)
    return plan


def write_plan(graph, plan):
    (graph.repo / "plan.json").write_text(json.dumps(plan))


def test_two_group_plan_stops_before_preparation_without_starting_later_work(graph):
    plan = configure_plan(graph)
    (graph.repo / "value.txt").write_text("caller staged\n")
    graph.git("add", "value.txt")
    (graph.repo / "value.txt").write_text("caller unstaged\n")
    (graph.repo / "untracked").write_text("caller untracked\n")
    caller = graph.git("status", "--porcelain")
    plan_bytes = (graph.repo / "plan.json").read_bytes()
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "preparation_pending"
    assert record["feature_complete"] is False
    assert record["milestone"] == {
        "id": "M1",
        "state": "preparation_pending",
        "feature_revision": record["integration_revision"],
    }
    assert record["plan"]["version"] == "v1"
    assert record["plan"]["approval"] == plan["approval"]
    assert record["plan"]["milestones"] == plan["milestones"]
    assert record["plan"]["final_coverage"] == ["01", "02", "03", "04"]
    assert record["plan"]["roles"]["worker"]["reasoning"] == "Medium"
    assert record["plan"]["roles"]["spec"]["reasoning"] == "High"
    assert record["plan"]["roles"]["standards"]["reasoning"] == "High"
    assert record["worker_settings"]["03"] == {"model": "scripted-fixture", "reasoning": "High"}
    assert record["selected_tickets"] == ["01", "03"]
    assert {t: s["state"] for t, s in record["tickets"].items()} == {
        "01": "Done",
        "02": "Pending",
        "03": "Done",
        "04": "Pending",
    }
    assert record["tickets"]["02"]["attempt"] == record["tickets"]["04"]["attempt"] == 0
    starts = launches(graph)[::2]
    assert [(e["ticket"], e["role"]) for e in starts] == [
        (t, r) for t in ("03", "01") for r in ("implementation", "spec", "standards")
    ]
    previous = graph.base
    for ticket in ("03", "01"):
        state = record["tickets"][ticket]
        worker = next(e for e in starts if e["ticket"] == ticket and e["role"] == "implementation")
        assert worker["head"] == worker["base"] == worker["integration"] == previous
        gates = [g for g in record["gates"] if g["ticket"] == ticket]
        assert [g["stage"] for g in gates] == [
            "implementation",
            "check-other" if ticket == "03" else "check-ticket",
            "spec",
            "standards",
            "candidate",
        ]
        assert all(g["passed"] for g in gates)
        assert all(g["revision"] == state["submitted_revision"] for g in gates[1:4])
        assert gates[-1]["revision"] == state["done_revision"]
        assert graph.git("show", "-s", "--format=%P", state["done_revision"]).split() == [
            previous,
            state["submitted_revision"],
        ]
        previous = state["done_revision"]
    assert graph.git("rev-parse", "integration") == previous
    assert graph.git("rev-parse", "dev") == record["development_revision"] == graph.base
    assert graph.git("status", "--porcelain") == caller
    assert graph.git("rev-parse", "HEAD") == graph.base
    assert (graph.repo / "value.txt").read_text() == "caller unstaged\n"
    assert graph.git("show", ":value.txt") == "caller staged"
    assert graph.git("show", "integration:work-01") == "delivered 01"
    assert graph.git("show", "integration:work-03") == "delivered 03"
    assert not {"work-02", "work-04"} & set(
        graph.git("ls-tree", "--name-only", "integration").splitlines()
    )
    assert (graph.repo / "plan.json").read_bytes() == plan_bytes
    snapshot = record["inputs"]["plan"]
    assert Path(snapshot["artifact"]).read_bytes() == plan_bytes
    assert snapshot["sha256"] == hashlib.sha256(plan_bytes).hexdigest()
    for snapshot in record["inputs"].values():
        data = Path(snapshot["artifact"]).read_bytes()
        assert data == Path(snapshot["source"]).read_bytes()
        assert snapshot["sha256"] == hashlib.sha256(data).hexdigest()
    assert "candidate_revision" not in record["milestone"]
    assert "qa_request" not in record
    assert graph.cli("status", graph.output).stdout == result.stdout


@pytest.mark.parametrize(
    "mutation, diagnostic",
    [
        ("missing-member", "membership"),
        ("duplicate-member", "membership"),
        ("missing-final-coverage", "final_coverage"),
        ("later-dependency", "later milestone"),
        ("ticket-milestone-conflict", "Milestone metadata conflicts"),
        ("ticket-version-conflict", "Plan version metadata conflicts"),
        ("worker-conflict", "Worker reasoning metadata conflicts"),
        ("later-selection", "selected_tickets"),
        ("later-primary", "primary ticket"),
        ("unknown-setting", "unsupported"),
        ("missing-qa", "pass_conditions"),
        ("wrong-final", "final_milestone"),
        ("duplicate-id", "duplicate milestone"),
        ("unknown-required", "unknown ticket"),
        ("missing-model", "model"),
        ("bad-reasoning", "reasoning"),
        ("override-without-reason", "reason"),
        ("override-unknown-ticket", "override"),
        ("empty-version", "version"),
        ("empty-approval", "approval"),
        ("malformed", "object"),
        ("feature-is-dev", "differ"),
    ],
)
def test_invalid_plans_reject_before_processes_or_branch_changes(graph, mutation, diagnostic):
    plan = configure_plan(graph)
    if mutation == "missing-member":
        plan["milestones"][1]["tickets"].remove("02")
    elif mutation == "duplicate-member":
        plan["milestones"][1]["tickets"].append("01")
    elif mutation == "missing-final-coverage":
        plan["final_coverage"].remove("01")
    elif mutation == "later-dependency":
        path = graph.repo / "01-value.md"
        path.write_text(path.read_text().replace("Blocked by: None", "Blocked by: 02"))
        # Remove the reverse dependency, so this is a cross-group violation, not a cycle.
        path = graph.repo / "04-work.md"
        path.write_text(path.read_text().replace("Blocked by: 01", "Blocked by: None"))
    elif mutation.startswith("ticket-") or mutation == "worker-conflict":
        field, value = {
            "ticket-milestone-conflict": ("Milestone", "M2"),
            "ticket-version-conflict": ("Plan version", "v9"),
            "worker-conflict": ("Worker reasoning", "High"),
        }[mutation]
        path = graph.repo / "01-value.md"
        path.write_text(path.read_text().replace("Status:", f"{field}: {value}\nStatus:"))
    elif mutation == "later-selection":
        graph.config["selected_tickets"] = ["01-value.md", "02-work.md", "03-work.md", "04-work.md"]
    elif mutation == "later-primary":
        graph.config["ticket"] = "02-work.md"
    elif mutation == "unknown-setting":
        plan["roles"]["worker"]["thinking"] = "medium"
    elif mutation == "missing-qa":
        plan["milestones"][0]["qa"]["pass_conditions"] = []
    elif mutation == "wrong-final":
        plan["final_milestone"] = "M1"
    elif mutation == "duplicate-id":
        plan["milestones"][1]["id"] = "M1"
    elif mutation == "unknown-required":
        plan["required_tickets"].append("99")
    elif mutation == "missing-model":
        del plan["roles"]["spec"]["model"]
    elif mutation == "bad-reasoning":
        plan["roles"]["spec"]["reasoning"] = "guess"
    elif mutation == "override-without-reason":
        del plan["worker_overrides"]["03"]["reason"]
    elif mutation == "override-unknown-ticket":
        plan["worker_overrides"]["99"] = plan["worker_overrides"].pop("03")
    elif mutation == "empty-version":
        plan["version"] = ""
    elif mutation == "empty-approval":
        plan["approval"] = ""
    elif mutation == "malformed":
        plan = []
    elif mutation == "feature-is-dev":
        plan["development"] = "integration"
    write_plan(graph, plan)
    dev = graph.git("rev-parse", "dev")
    reject(graph, diagnostic)
    assert graph.git("rev-parse", "dev") == dev
    assert launches(graph) == []


def test_single_final_group_still_requires_preparation_and_captures_matching_metadata(graph):
    plan = configure_plan(graph)
    plan["milestones"] = [plan["milestones"][0]]
    plan["milestones"][0]["tickets"] = ["03", "01", "04", "02"]
    plan["final_milestone"] = "M1"
    plan["roles"]["worker"]["context_limit"] = 250000
    write_plan(graph, plan)
    path = graph.repo / "03-work.md"
    path.write_text(
        path.read_text().replace(
            "Status:",
            "**Plan version:** v1\n**Milestone:** M1\n**Worker reasoning:** High\nStatus:",
        )
    )
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "preparation_pending"
    assert record["feature_complete"] is False
    assert all(t["state"] == "Done" for t in record["tickets"].values())
    assert record["worker_settings"]["03"] == {
        "model": "scripted-fixture",
        "reasoning": "High",
        "context_limit": 250000,
    }
    assert record["plan"]["roles"]["spec"] == {"model": "scripted-spec", "reasoning": "High"}
    assert graph.git("rev-parse", "dev") == graph.base


def test_failed_current_candidate_never_claims_preparation_or_starts_next_group(graph):
    configure_plan(graph)
    graph.config["suite"] = [
        graph.config["agent"][0],
        "-c",
        "import os; raise SystemExit(7 if os.environ['TICKET_HARNESS_STAGE'] == 'candidate' else 0)",
    ]
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert record["outcome"] == "incomplete"
    assert record["failure"]["stage"] == "candidate"
    assert record["milestone"]["state"] == "executing"
    assert record["tickets"]["03"]["state"] == "Blocked"
    assert {record["tickets"][t]["attempt"] for t in ("01", "02", "04")} == {0}
    assert graph.git("rev-parse", "integration") == graph.git("rev-parse", "dev") == graph.base
    assert record["feature_complete"] is False


@pytest.mark.parametrize("field", ["Plan version", "Milestone", "Worker reasoning"])
def test_duplicate_milestone_metadata_rejects_without_execution(graph, field):
    configure_plan(graph)
    path = graph.repo / "03-work.md"
    path.write_text(path.read_text().replace("Status:", f"{field}: v1\n{field}: v1\nStatus:"))
    reject(graph, f"duplicate {field}")
    assert launches(graph) == []


def test_context_dependency_cannot_hide_a_later_milestone_edge(graph):
    plan = configure_plan(graph)
    for name, old, new in (
        ("01-value.md", "Blocked by: None", "Blocked by: 05"),
        ("05-context.md", "Blocked by: None", "Blocked by: 02"),
        ("04-work.md", "Blocked by: 01", "Blocked by: None"),
    ):
        path = graph.repo / name
        path.write_text(path.read_text().replace(old, new))
    write_plan(graph, plan)
    reject(graph, "later milestone")
    assert launches(graph) == []


def test_plan_mutation_stops_execution_and_preserves_the_approved_snapshot(graph):
    configure_plan(graph)
    from test_dependencies import extend_agent

    approved = (graph.repo / "plan.json").read_bytes()
    extend_agent(
        graph,
        "if a['role'] == 'implementation':\n"
        f"    Path({str(graph.repo / 'plan.json')!r}).write_text('rewritten approval')\n"
        "    p = Path.cwd().parents[1] / 'inputs' / 'plan.json'\n"
        "    p.write_text('rewritten snapshot')",
    )
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert record["outcome"] == "incomplete"
    assert "Integrity violation" in record["failure"]["message"]
    # Caller-owned source stays inspectable; harness-owned approved bytes are restored.
    assert (graph.repo / "plan.json").read_text() == "rewritten approval"
    assert record["inputs"]["plan"]["sha256"] == hashlib.sha256(approved).hexdigest()
    assert any(
        item["path"] == str(graph.repo / "plan.json") for item in record["gates"][-1]["integrity"]
    )
    assert Path(record["inputs"]["plan"]["artifact"]).read_bytes() == approved
    assert graph.git("rev-parse", "integration") == graph.git("rev-parse", "dev") == graph.base
    assert all(t["attempt"] == 0 for k, t in record["tickets"].items() if k != "03")
