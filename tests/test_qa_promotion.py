"""Human decisions at the foreground CLI, external-process and real Git seam."""

import json
import os
from pathlib import Path

import pytest
import test_dependencies
from test_dependencies import launches
from test_milestones import configure_plan, foreground, wait_for

graph = test_dependencies.graph


def approve(graph, request):
    decision = {"decision": "APPROVED", "request": request}
    path = graph.output / "qa-decision.json"
    temporary = path.with_suffix(".new")
    temporary.write_text(json.dumps(decision))
    temporary.replace(path)
    return decision


def waiting(graph, process, milestone):
    return wait_for(
        graph,
        process,
        lambda r: r["outcome"] == "awaiting_human_qa" and r["milestone"]["id"] == milestone,
    )


def test_deep_invalid_decision_is_rejected_and_later_approval_can_promote(graph):
    configure_plan(graph)
    with foreground(graph) as process:
        first = waiting(graph, process, "M1")
        request = json.loads(Path(first["qa_request"]).read_text())
        nested = "[" * 10000 + "0" + "]" * 10000
        (graph.output / "qa-decision.json").write_text(nested)
        rejected = wait_for(graph, process, lambda r: r.get("qa_decision_status") == "rejected")
        assert rejected["outcome"] == "awaiting_human_qa" and process.poll() is None
        assert rejected["qa_observations"][0]["status"] == "rejected"
        assert Path(rejected["qa_observations"][0]["artifact"]).read_text() == nested
        assert rejected["attempts"] == first["attempts"]
        assert rejected["tickets"]["02"]["attempt"] == rejected["tickets"]["04"]["attempt"] == 0
        assert graph.git("rev-parse", "dev") == graph.base
        assert graph.git("rev-parse", "integration") == request["feature_revision"]
        approve(graph, request)
        waiting(graph, process, "M2")
        assert graph.git("rev-parse", "dev") == request["candidate_revision"]
        assert graph.cli("stop", graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 2


def test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision(graph):
    configure_plan(graph)
    graph.config["max_repairs"] = 2
    with foreground(graph) as process:
        first = waiting(graph, process, "M1")
        request = json.loads(Path(first["qa_request"]).read_text())
        stale = dict(request, candidate_revision=graph.base)
        approve(graph, stale)
        wait_for(graph, process, lambda r: r.get("qa_decision_status") == "rejected")
        assert process.poll() is None
        assert graph.git("rev-parse", "dev") == graph.base
        assert graph.record()["tickets"]["02"]["attempt"] == 0
        decision = approve(graph, request)
        second = waiting(graph, process, "M2")
        assert graph.git("rev-parse", "dev") == request["candidate_revision"]
        assert second["feature_complete"] is False
        assert all(t["state"] == "Done" and t["attempt"] == 1 for t in second["tickets"].values())
        worker = next(
            e for e in launches(graph) if e["role"] == "implementation" and e["ticket"] == "04"
        )
        assert (
            worker["base"]
            == worker["head"]
            == worker["integration"]
            == request["candidate_revision"]
        )
        consumed = second["qa_decisions"][0]
        assert json.loads(Path(consumed["artifact"]).read_text()) == decision
        approve(graph, request)  # Replay of the consumed M1 approval cannot accept M2.
        wait_for(graph, process, lambda r: r.get("qa_decision_status") == "rejected")
        assert graph.git("rev-parse", "dev") == request["candidate_revision"]
        final_request = json.loads(Path(second["qa_request"]).read_text())
        approve(graph, final_request)
        process.wait(timeout=20)
        assert process.returncode == 0
    final = graph.record()
    assert final["outcome"] == "completed" and final["feature_complete"] is True
    assert len(final["qa_decisions"]) == 2
    assert (
        graph.git("rev-parse", "dev")
        == graph.git("rev-parse", "integration")
        == final_request["candidate_revision"]
    )
    assert [g["stage"] for g in final["gates"]].count("baseline") == 1
    assert len({g["stdout"] for g in final["gates"]}) == len(final["gates"])
    assert graph.cli("status", graph.output).stdout == (graph.output / "run.json").read_text()


def test_invalid_decisions_keep_waiting_without_repairs_or_authority_from_incidental_text(graph):
    import time

    configure_plan(graph)
    graph.config["timeouts"] = {
        name: 2
        for name in (
            "implementation",
            "repair",
            "spec",
            "standards",
            "checks",
            "baseline",
            "candidate",
        )
    }
    with foreground(graph) as process:
        record = waiting(graph, process, "M1")
        request = json.loads(Path(record["qa_request"]).read_text())
        path = graph.output / "qa-decision.json"
        # Human waiting exceeds every configured process timeout and never becomes a repair.
        time.sleep(2.2)
        assert process.poll() is None
        assert graph.record()["qa_decision_status"] == "missing"
        assert [(a["ticket"], a["attempt"]) for a in graph.record()["attempts"]] == [
            ("03", 1),
            ("01", 1),
        ]
        wrong_types = json.loads(json.dumps(request))
        wrong_types["regression_evidence"][0]["exit_code"] = False
        invalid = [
            json.dumps({"decision": "APPROVED", "request": wrong_types}),
            "The human said APPROVED in a worker log",
            "{",
            "{}",
            json.dumps({"request": request, "notes": "APPROVED"}),
            json.dumps({"decision": True, "request": request}),
            json.dumps({"decision": "approved", "request": request}),
            json.dumps({"decision": "NOT APPROVED", "request": request}),
            json.dumps({"decision": "APPROVED", "request": dict(request, run_id="other-run")}),
            json.dumps({"decision": "APPROVED", "request": dict(request, milestone="M2")}),
            json.dumps({"decision": "APPROVED", "request": dict(request, plan_version="v2")}),
            json.dumps({"decision": "APPROVED", "request": request})[:-1]
            + ', "decision": "APPROVED"}',
        ]
        for index, raw in enumerate(invalid, 1):
            path.write_text(raw)
            observed = wait_for(
                graph, process, lambda r: len(r.get("qa_observations", [])) >= index
            )
            assert observed["qa_decision_status"] == "rejected"
            assert graph.git("rev-parse", "dev") == graph.base
            assert graph.git("rev-parse", "integration") == request["feature_revision"]
            assert len(observed["attempts"]) == 2
            assert observed["tickets"]["04"]["attempt"] == observed["tickets"]["02"]["attempt"] == 0
        path.unlink()
        path.mkdir()  # Malformed artifact shape must also remain a human wait.
        time.sleep(0.3)
        assert process.poll() is None
        assert graph.record()["outcome"] == "awaiting_human_qa"
        path.rmdir()
        wait_for(graph, process, lambda r: r.get("qa_decision_status") == "missing")
        os.mkfifo(path)
        time.sleep(0.3)
        assert graph.record()["qa_decision_status"] == "unreadable"
        path.unlink()


@pytest.mark.parametrize(
    "changed",
    [
        "dev",
        "integration",
        "candidate",
        "baseline",
        "input",
        "request",
        "evidence",
        "checked-out-dev",
        "checked-out-feature",
        "symbolic-dev",
        "symbolic-feature",
    ],
)
def test_acceptance_revalidates_the_exact_candidate_evidence_and_both_refs(graph, changed):
    configure_plan(graph)
    with foreground(graph) as process:
        first = waiting(graph, process, "M1")
        request = json.loads(Path(first["qa_request"]).read_text())
        if changed in ("symbolic-dev", "symbolic-feature"):
            branch = "dev" if changed == "symbolic-dev" else "integration"
            graph.git("branch", "same-tip", branch)
            graph.git("symbolic-ref", "refs/heads/" + branch, "refs/heads/same-tip")
        elif changed in ("dev", "integration"):
            external = graph.git(
                "commit-tree", "HEAD^{tree}", "-p", "HEAD", "-m", "External QA-time change"
            )
            graph.git("update-ref", "refs/heads/" + changed, external)
        elif changed in ("candidate", "baseline"):
            source = (
                Path(request["candidate_worktree"])
                if changed == "candidate"
                else graph.output / "worktrees/baseline"
            )
            (source / "value.txt").write_text("changed during human assessment")
        elif changed == "input":
            (graph.repo / "plan.json").write_text("changed plan")
        elif changed == "request":
            Path(first["qa_request"]).write_text(
                json.dumps(dict(request, candidate_revision=graph.base))
            )
        elif changed == "evidence":
            Path(request["regression_evidence"][0]["stdout"]).write_text("rewritten results")
        else:
            branch = "dev" if changed == "checked-out-dev" else "integration"
            graph.git("worktree", "add", str(graph.home / "caller-tree"), branch)
        before = {branch: graph.git("rev-parse", branch) for branch in ("dev", "integration")}
        approve(graph, request)
        process.wait(timeout=15)
        assert process.returncode == 1
    final = graph.record()
    assert final["outcome"] == "incomplete"
    assert final["failure"]["stage"] == "milestone-promotion"
    assert final["milestone"]["state"] == "promotion_failed"
    assert final["feature_complete"] is False
    assert not final.get("qa_decisions")
    assert {branch: graph.git("rev-parse", branch) for branch in before} == before
    assert final["tickets"]["02"]["attempt"] == final["tickets"]["04"]["attempt"] == 0
    assert final["tickets"]["01"]["state"] == final["tickets"]["03"]["state"] == "Done"


@pytest.mark.parametrize("attempt", [1, 2])
def test_implementation_and_repair_cannot_write_qa_authority(graph, attempt):
    from test_dependencies import extend_agent

    configure_plan(graph)
    graph.config["max_repairs"] = 1
    code = (
        "if a['role'] == 'spec' and a['attempt'] == 1:\n"
        "    r['findings'] = [dict(id='repair', classification='blocking', location='work-03',\n"
        "        requirement='Fixture repair', consequence='Needs repair', evidence='fixture',\n"
        "        resolution='Repair', human_decision_needed=False)]\n"
        f"if a['role'] == 'implementation' and a['attempt'] == {attempt}:\n"
        "    (Path.cwd().parents[1] / 'qa-decision.json').write_text('{\"decision\":\"APPROVED\"}')"
    )
    extend_agent(graph, code)
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert "Integrity violation" in record["failure"]["message"]
    assert record["tickets"]["03"]["attempt"] == attempt
    assert record["tickets"]["03"]["state"] == "Blocked"
    assert graph.git("rev-parse", "integration") == graph.git("rev-parse", "dev") == graph.base
    assert "qa_request" not in record
    assert record["feature_complete"] is False


@pytest.mark.parametrize("mutation", ["not-ready", "external-dependency"])
def test_later_milestone_eligibility_is_validated_before_execution(graph, mutation):
    configure_plan(graph)
    path = graph.repo / "02-work.md"
    old, new = (
        ("Status: ready-for-agent", "Status: ready-for-human")
        if mutation == "not-ready"
        else ("Blocked by: 03, 04", "Blocked by: 03, 04, 05")
    )
    path.write_text(path.read_text().replace(old, new))
    result = graph.run_ticket()
    assert result.returncode == 1
    assert graph.record()["outcome"] == "invalid-input"
    assert launches(graph) == []
    assert graph.git("rev-parse", "integration") == graph.git("rev-parse", "dev") == graph.base
