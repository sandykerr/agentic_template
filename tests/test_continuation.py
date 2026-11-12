"""Deliberate QA continuation at the public CLI/Git/process seam."""

import json

import pytest
import test_dependencies
from test_dependencies import launches
from test_milestones import configure_plan, foreground
from test_qa_promotion import approve, waiting

graph = test_dependencies.graph


def test_clean_qa_stop_continues_in_new_process_without_replaying_done_work(graph):
    configure_plan(graph)
    with foreground(graph) as process:
        first = waiting(graph, process, "M1")
        request = json.loads((graph.output / "qa-request.json").read_text())
        assert graph.cli("stop", graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 2
    stopped = graph.record()
    assert stopped["outcome"] == "stopped_at_qa"
    assert stopped["tickets"] == first["tickets"]
    approve(graph, request)
    # The continuation itself remains foreground; own and bound its process.
    with foreground(graph, operation="continue") as process:
        second = waiting(graph, process, "M2")
        assert len(second["qa_decisions"]) == 1
        duplicate = graph.cli("continue", graph.output)
        assert duplicate.returncode == 1 and "active owner" in duplicate.stderr
        assert graph.git("rev-parse", "dev") == request["candidate_revision"]
        assert second["attempts"][:2] == first["attempts"]
        approve(graph, request)
        from test_milestones import wait_for

        wait_for(graph, process, lambda r: r.get("qa_decision_status") == "rejected")
        approve(graph, json.loads((graph.output / "qa-request.json").read_text()))
        process.wait(timeout=20)
        assert process.returncode == 0
    final = graph.record()
    assert final["feature_complete"] is True
    assert len(final["qa_decisions"]) == 2
    assert [g["stage"] for g in final["gates"]].count("baseline") == 1
    assert (
        len([e for e in launches(graph) if e["role"] == "implementation" and e["event"] == "start"])
        == 4
    )
    assert graph.cli("continue", graph.output).returncode == 1


def test_new_qa_observation_cannot_be_rewritten_before_clean_stop(graph):
    from pathlib import Path

    from test_milestones import wait_for

    configure_plan(graph)
    with foreground(graph) as process:
        waiting(graph, process, "M1")
        approve(graph, {"stale": True})
        observed = wait_for(graph, process, lambda r: r.get("qa_decision_status") == "rejected")
        Path(observed["qa_observations"][0]["artifact"]).write_text("rewritten observation")
        graph.cli("stop", graph.output)
        process.wait(timeout=10)
        assert process.returncode == 1
    assert graph.record()["outcome"] == "incomplete"
    assert not (graph.output / "qa-checkpoint.json").exists()


def stop_at_qa(graph):
    with foreground(graph) as process:
        waiting(graph, process, "M1")
        assert graph.cli("stop", graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 2


def test_clean_stop_rejects_symbolic_destination_with_unchanged_tip(graph):
    configure_plan(graph)
    with foreground(graph) as process:
        waiting(graph, process, "M1")
        graph.git("branch", "same-tip", "dev")
        graph.git("symbolic-ref", "refs/heads/dev", "refs/heads/same-tip")
        refs = graph.git("show-ref")
        assert graph.cli("stop", graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 1
    assert graph.record()["outcome"] == "incomplete"
    assert not (graph.output / "qa-checkpoint.json").exists()
    assert graph.git("show-ref") == refs


def test_continued_run_records_invalidation_of_earlier_verified_source(graph):
    configure_plan(graph)
    stop_at_qa(graph)
    with foreground(graph, operation="continue") as process:
        waiting(graph, process, "M1")
        (graph.output / "worktrees/baseline/value.txt").write_text("external post-restore edit")
        assert graph.cli("stop", graph.output).returncode == 0
        process.wait(timeout=10)
        assert process.returncode == 1
    record = graph.record()
    assert record["outcome"] == "incomplete"
    baseline = next(gate for gate in record["gates"] if gate["stage"] == "baseline")
    assert baseline["passed"] is False
    assert baseline["verification_status"] == "invalidated"
    assert "Verified source changed" in baseline["diagnostic"]
    assert graph.git("rev-parse", "dev") == graph.base
    assert not record.get("qa_decisions")


@pytest.mark.parametrize(
    "changed",
    [
        "plan",
        "snapshot",
        "record",
        "record-type",
        "malformed-record",
        "checkpoint",
        "archive",
        "request",
        "evidence",
        "observation",
        "baseline",
        "candidate",
        "dev",
        "integration",
        "checked-out",
        "symbolic-dev",
        "symbolic-feature",
    ],
)
def test_continuation_rejects_changed_checkpoint_without_overwriting_prior_state(graph, changed):
    from pathlib import Path

    configure_plan(graph)
    stop_at_qa(graph)
    record = graph.record()
    request = json.loads((graph.output / "qa-request.json").read_text())
    if changed in ("symbolic-dev", "symbolic-feature"):
        branch = "dev" if changed == "symbolic-dev" else "integration"
        graph.git("branch", "same-tip", branch)
        graph.git("symbolic-ref", "refs/heads/" + branch, "refs/heads/same-tip")
    elif changed == "plan":
        (graph.repo / "plan.json").write_text("changed approved plan")
    elif changed == "snapshot":
        Path(record["inputs"]["plan"]["artifact"]).write_text("changed snapshot")
    elif changed == "malformed-record":
        (graph.output / "run.json").write_text("[]")
    elif changed == "record-type":
        record["tickets"]["03"]["attempt"] = True
        (graph.output / "run.json").write_text(json.dumps(record))
    elif changed == "record":
        record["tickets"]["02"]["state"] = "Done"
        (graph.output / "run.json").write_text(json.dumps(record))
    elif changed == "archive":
        next((graph.output / "checkpoints").glob("*.json")).write_text("changed archive")
    elif changed in ("checkpoint", "request"):
        path = graph.output / (
            "qa-checkpoint.json" if changed == "checkpoint" else "qa-request.json"
        )
        path.write_text("{}")
    elif changed == "evidence":
        Path(request["regression_evidence"][0]["stdout"]).write_text("rewritten")
    elif changed == "observation":
        # There are no decisions at this checkpoint; fabricated consumption must not unlock work.
        record["qa_decisions"] = [{"request_id": request["request_id"]}]
        (graph.output / "run.json").write_text(json.dumps(record))
    elif changed in ("baseline", "candidate"):
        tree = (
            graph.output / "worktrees/baseline"
            if changed == "baseline"
            else Path(request["candidate_worktree"])
        )
        (tree / "value.txt").write_text("changed verified source")
    elif changed == "checked-out":
        graph.git("worktree", "add", str(graph.home / "caller-tree"), "dev")
    else:
        revision = graph.git("commit-tree", "HEAD^{tree}", "-p", "HEAD", "-m", "External")
        graph.git("update-ref", "refs/heads/" + changed, revision)
    before = {
        p: p.read_bytes()
        for p in graph.output.rglob("*")
        if p.is_file() and "/worktrees/" not in str(p)
    }
    refs = {branch: graph.git("rev-parse", branch) for branch in ("dev", "integration")}
    if changed in ("symbolic-dev", "symbolic-feature"):
        with foreground(graph, operation="continue") as process:
            process.wait(timeout=10)
            assert process.returncode == 1
        assert graph.foreground_observations[-1]["stderr"].strip()
    else:
        result = graph.cli("continue", graph.output)
        assert result.returncode == 1
        assert result.stderr.strip()
    assert all(path.read_bytes() == raw for path, raw in before.items())
    assert {branch: graph.git("rev-parse", branch) for branch in refs} == refs
    assert list((graph.output / "rejections").glob("*.json"))
    if changed == "malformed-record":
        (graph.output / "malformed-record.json").write_bytes(before[graph.output / "run.json"])
        (graph.output / "run.json").write_text(json.dumps(record))


def test_active_owner_and_arbitrary_interruption_cannot_be_continued(graph):
    configure_plan(graph)
    with foreground(graph) as process:
        waiting(graph, process, "M1")
        before = (graph.output / "run.json").read_bytes()
        result = graph.cli("continue", graph.output)
        assert result.returncode == 1 and "active owner" in result.stderr
        assert (graph.output / "run.json").read_bytes() == before
    # Termination by the fixture did not create a clean checkpoint.
    result = graph.cli("continue", graph.output)
    assert result.returncode == 1 and "deliberate" in result.stderr
    assert graph.cli("stop", graph.output).returncode == 1


def test_repeated_stops_retain_previous_decisions_and_checkpoint_lineage(graph):
    configure_plan(graph)
    stop_at_qa(graph)
    first_checkpoint = (graph.output / "qa-checkpoint.json").read_bytes()
    request = json.loads((graph.output / "qa-request.json").read_text())
    approve(graph, request)
    with foreground(graph, operation="continue") as process:
        second = waiting(graph, process, "M2")
        graph.cli("stop", graph.output)
        process.wait(timeout=10)
        assert process.returncode == 2
    assert first_checkpoint in [
        p.read_bytes() for p in (graph.output / "checkpoints").glob("*.json")
    ]
    assert len(second["qa_decisions"]) == len(graph.record()["qa_decisions"]) == 1
    with foreground(graph, operation="continue") as process:
        waiting(graph, process, "M2")
        approve(graph, json.loads((graph.output / "qa-request.json").read_text()))
        process.wait(timeout=15)
        assert process.returncode == 0
    assert len(graph.record()["attempts"]) == 4
