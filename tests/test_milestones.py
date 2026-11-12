"""Approved milestone boundaries at the public CLI/process/Git seam."""

import hashlib
import json
import os
import signal
import subprocess
import sys
import time
from contextlib import contextmanager
from pathlib import Path

import pytest
import test_dependencies
from test_dependencies import launches
from test_preflight import reject

graph = test_dependencies.graph


@pytest.mark.parametrize("alias", ["development", "feature", "feature-chain"])
def test_symbolic_milestone_destinations_are_rejected_before_ticket_work(graph, alias):
    configure_plan(graph)
    if alias == "development":
        graph.git("symbolic-ref", "refs/heads/dev", "refs/heads/integration")
    else:
        target = "dev"
        if alias == "feature-chain":
            graph.git("symbolic-ref", "refs/heads/bridge", "refs/heads/dev")
            target = "bridge"
        graph.git("symbolic-ref", "refs/heads/integration", "refs/heads/" + target)
    refs = graph.git("show-ref")
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert "symbolic" in record["failure"]["message"].lower()
    assert record["attempts"] == [] and record["gates"] == []
    assert graph.git("show-ref") == refs
    assert graph.git("rev-parse", "dev") == graph.base
    assert not (graph.output / "qa-request.json").exists()


@pytest.mark.parametrize("branch,target", [("dev", "integration"), ("integration", "dev")])
def test_ticket_integration_rejects_destinations_aliased_during_work(graph, branch, target):
    from test_dependencies import extend_agent

    configure_plan(graph)
    extend_agent(
        graph,
        "if a['role'] == 'standards' and a['ticket'] == '03':\n"
        f"    subprocess.run(['git', 'symbolic-ref', 'refs/heads/{branch}', "
        f"'refs/heads/{target}'], check=True)",
    )
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "integration"
    assert "symbolic" in record["failure"]["message"].lower()
    assert record["tickets"]["03"]["state"] == "Blocked"
    assert graph.git("rev-parse", "dev") == graph.git("rev-parse", "integration") == graph.base
    assert graph.git("symbolic-ref", "refs/heads/" + branch) == "refs/heads/" + target


@contextmanager
def foreground(graph, operation="run"):
    """Own a real foreground runner; bound fixture waits and always reap it."""
    if operation == "run":
        graph.config_path.write_text(json.dumps(graph.config))
    command = [
        sys.executable,
        "-m",
        "ticket_harness",
        operation,
        "--config",
        str(graph.config_path),
        "--output",
        str(graph.output),
    ]
    if operation != "run":
        command = command[:4] + [str(graph.output)]
    stdout_path, stderr_path = graph.home / "foreground.stdout", graph.home / "foreground.stderr"
    with stdout_path.open("w") as stdout, stderr_path.open("w") as stderr:
        process = subprocess.Popen(
            command, stdout=stdout, stderr=stderr, text=True, start_new_session=True
        )
    try:
        yield process
    finally:
        terminated = process.poll() is None
        if terminated:
            # Capture descendants before terminating their parent. Agents/checks own
            # separate sessions, so killing only the runner would leak active work.
            owned = {process.pid}
            pending = [process.pid]
            while pending:
                parent = pending.pop()
                children = Path(f"/proc/{parent}/task/{parent}/children")
                try:
                    found = {int(pid) for pid in children.read_text().split()} - owned
                except FileNotFoundError:
                    found = set()
                owned.update(found)
                pending.extend(found)
            for pid in owned:
                try:
                    group = os.getpgid(pid)
                    if group in owned:
                        os.killpg(group, signal.SIGKILL if group != process.pid else signal.SIGTERM)
                except ProcessLookupError:
                    pass
        process.wait(timeout=10)
        stdout, stderr = stdout_path.read_text(), stderr_path.read_text()
        graph.foreground_observations = getattr(graph, "foreground_observations", []) + [
            dict(
                command=command,
                exit_code=process.returncode,
                terminated_by_fixture=terminated,
                stdout=stdout,
                stderr=stderr,
            )
        ]


def wait_for(graph, process, predicate):
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        if (graph.output / "run.json").exists():
            record = graph.record()
            if predicate(record):
                return record
        if process.poll() is not None:
            raise AssertionError(
                f"runner exited {process.returncode}: "
                + (graph.home / "foreground.stderr").read_text()
            )
        time.sleep(0.025)
    raise AssertionError("fixture deadline exceeded")


def run_until_wait(graph):
    # Preparation scenarios inspect an active wait through the actual status CLI.
    # A status exit of zero is not an assertion that the terminated run completed.
    with foreground(graph) as process:
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            if (graph.output / "run.json").exists():
                if graph.record()["outcome"] == "awaiting_human_qa":
                    return graph.cli("status", graph.output)
            if process.poll() is not None:
                stdout = (graph.home / "foreground.stdout").read_text()
                stderr = (graph.home / "foreground.stderr").read_text()
                return subprocess.CompletedProcess(process.args, process.returncode, stdout, stderr)
            time.sleep(0.025)
        raise AssertionError("fixture deadline exceeded")


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


def test_two_group_plan_presents_tested_qa_without_starting_later_work(graph):
    plan = configure_plan(graph)
    (graph.repo / "value.txt").write_text("caller staged\n")
    graph.git("add", "value.txt")
    (graph.repo / "value.txt").write_text("caller unstaged\n")
    (graph.repo / "untracked").write_text("caller untracked\n")
    caller = graph.git("status", "--porcelain")
    plan_bytes = (graph.repo / "plan.json").read_bytes()
    result = run_until_wait(graph)
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "awaiting_human_qa"
    assert record["feature_complete"] is False
    assert record["milestone"]["id"] == "M1"
    assert record["milestone"]["state"] == "awaiting_human_qa"
    assert record["milestone"]["feature_revision"] == record["integration_revision"]
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
    assert record["milestone"]["candidate_revision"]
    assert Path(record["qa_request"]).exists()
    assert graph.cli("status", graph.output).stdout == result.stdout

    milestone = record["milestone"]
    candidate = milestone["candidate_revision"]
    assert milestone["state"] == "awaiting_human_qa"
    request = json.loads(Path(record["qa_request"]).read_text())
    assert request["request_id"] and request["request_id"] != request["run_id"]
    assert request["run_id"] == record["run_id"]
    assert request["plan_input"] == record["inputs"]["plan"]
    assert request["candidate_worktree"] == str(graph.output / "worktrees/milestone-candidate")
    assert request["run_directory"] == str(graph.output)
    assert request["plan_version"] == "v1"
    assert request["plan_approval"] == plan["approval"]
    assert request["milestone"] == "M1"
    assert request["feature_branch"] == "integration"
    assert request["feature_revision"] == graph.git("rev-parse", "integration")
    assert request["development_branch"] == "dev"
    assert request["development_revision"] == graph.git("rev-parse", "dev") == graph.base
    assert request["candidate_revision"] == candidate
    assert request["human_checks"] == plan["milestones"][0]["qa"]
    assert graph.git("show", "-s", "--format=%P", candidate).split() == [
        graph.base,
        request["feature_revision"],
    ]
    assert graph.git("show", candidate + ":work-01") == "delivered 01"
    assert graph.git("show", candidate + ":work-03") == "delivered 03"
    regression = record["gates"][-1]
    assert regression["stage"] == "milestone-regression"
    assert regression["revision"] == candidate
    assert regression["ticket"] is None
    assert regression["passed"]
    assert request["regression_evidence"] == [regression]
    assert Path(regression["stdout"]).read_text() == f"milestone-regression {candidate}\n"
    assert len([g for g in record["gates"] if g["stage"] == "candidate"]) == 2
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))
    assert all(record["tickets"][t]["attempt"] == 0 for t in ("02", "04"))
    assert record["feature_complete"] is False
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


def test_single_final_group_still_requires_human_qa_and_captures_matching_metadata(graph):
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
    result = run_until_wait(graph)
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "awaiting_human_qa"
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
    result = run_until_wait(graph)
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
    result = run_until_wait(graph)
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


def test_milestone_merge_hook_cannot_present_changed_source_without_renewed_reviews(graph):
    configure_plan(graph)
    hook = graph.repo / ".git/hooks/post-merge"
    hook.write_text(
        "#!/bin/sh\n"
        'if [ "$(basename "$PWD")" = milestone-candidate ]; then\n'
        "  printf 'unreviewed resolution\\n' > value.txt\n"
        "  git add value.txt\n"
        "  git commit --no-edit >/dev/null\n"
        "fi\n"
    )
    hook.chmod(0o755)
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-candidate"
    assert "renewed checks and reviews required" in record["failure"]["message"]
    assert record["milestone"]["state"] == "preparation_failed"
    assert "qa_request" not in record
    assert not (graph.output / "qa-request.json").exists()
    assert graph.git("rev-parse", "dev") == graph.base
    assert graph.git("rev-parse", "integration") == record["milestone"]["feature_revision"]
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))
    assert (
        graph.output / "worktrees/milestone-candidate/value.txt"
    ).read_text() == "unreviewed resolution\n"


def test_failed_milestone_regression_retains_done_tickets_without_a_qa_request(graph):
    configure_plan(graph)
    graph.config["suite"] = [
        graph.config["agent"][0],
        "-c",
        "import os; print('actual regression output'); "
        "raise SystemExit(7 if os.environ['TICKET_HARNESS_STAGE'] == 'milestone-regression' else 0)",
    ]
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-regression"
    assert record["milestone"]["state"] == "preparation_failed"
    assert record["outcome"] == "incomplete"
    assert "qa_request" not in record
    assert not (graph.output / "qa-request.json").exists()
    regression = record["gates"][-1]
    assert regression["stage"] == "milestone-regression"
    assert regression["exit_code"] == 7
    assert not regression["passed"]
    assert regression["revision"] == record["milestone"]["candidate_revision"]
    assert Path(regression["stdout"]).read_text() == "actual regression output\n"
    assert all(g["passed"] for g in record["gates"] if g["stage"] == "candidate")
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))
    assert all(record["tickets"][t]["attempt"] == 0 for t in ("02", "04"))
    assert graph.git("rev-parse", "integration") == record["milestone"]["feature_revision"]
    assert graph.git("rev-parse", "dev") == graph.base
    assert record["feature_complete"] is False
    assert graph.cli("status", graph.output).stdout == result.stdout


def milestone_suite(graph, action):
    script = graph.home / "milestone-suite.py"
    script.write_text(
        "import os, subprocess\nfrom pathlib import Path\n"
        "if os.environ['TICKET_HARNESS_STAGE'] == 'milestone-regression':\n"
        + "\n".join("    " + line for line in action.splitlines())
        + "\n"
    )
    graph.config["suite"] = [graph.config["agent"][0], str(script)]


def test_regression_cannot_present_qa_after_symbolic_destination_replacement(graph):
    configure_plan(graph)
    milestone_suite(
        graph,
        "subprocess.run(['git', 'branch', 'same-tip', 'dev'], check=True)\n"
        "subprocess.run(['git', 'symbolic-ref', 'refs/heads/dev', 'refs/heads/same-tip'], check=True)",
    )
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-readiness"
    assert "symbolic" in record["failure"]["message"].lower()
    assert "qa_request" not in record
    assert graph.git("rev-parse", "dev") == graph.base
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))


@pytest.mark.parametrize("branch", ["dev", "integration"])
def test_external_milestone_input_movement_preserves_refs_and_rejects_readiness(graph, branch):
    configure_plan(graph)
    milestone_suite(
        graph,
        "external = subprocess.check_output(['git', 'commit-tree', 'HEAD^{tree}', '-p', 'HEAD', "
        "'-m', 'External movement'], text=True).strip()\n"
        f"subprocess.run(['git', 'update-ref', 'refs/heads/{branch}', external], check=True)",
    )
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-readiness"
    assert f"Branch {branch} changed externally" in record["failure"]["message"]
    assert record["milestone"]["state"] == "preparation_failed"
    assert "qa_request" not in record
    assert not (graph.output / "qa-request.json").exists()
    external = graph.git("rev-parse", branch)
    assert graph.git("show", "-s", "--format=%s", external) == "External movement"
    assert external not in (record["milestone"]["candidate_revision"], graph.base)
    assert graph.git("rev-parse", "dev" if branch == "integration" else "integration") == (
        graph.base if branch == "integration" else record["milestone"]["feature_revision"]
    )
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))
    assert record["gates"][-1]["passed"]
    assert graph.cli("status", graph.output).stdout == result.stdout


@pytest.mark.parametrize("target", ["milestone-candidate", "baseline"])
def test_milestone_regression_source_mutation_invalidates_evidence_and_stops_qa(graph, target):
    configure_plan(graph)
    milestone_suite(
        graph, f"(Path.cwd().parent / {target!r} / 'value.txt').write_text('invalidated source')"
    )
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-regression"
    assert record["milestone"]["state"] == "preparation_failed"
    assert "qa_request" not in record
    invalidated = [g for g in record["gates"] if g.get("verification_status") == "invalidated"]
    assert invalidated and all(not g["passed"] for g in invalidated)
    assert (graph.output / "worktrees" / target / "value.txt").read_text() == "invalidated source"
    assert graph.git("rev-parse", "dev") == graph.base
    assert graph.git("rev-parse", "integration") == record["milestone"]["feature_revision"]


def test_changed_development_base_is_combined_with_feature_using_a_clean_same_file_merge(graph):
    from test_dependencies import extend_agent

    original = "one\ntwo\nthree\nfour\nfive\nsix\n"
    (graph.repo / "value.txt").write_text(original)
    graph.git("add", "value.txt")
    graph.git("commit", "-m", "Shared source")
    graph.base = graph.git("rev-parse", "HEAD")
    graph.git("update-ref", "refs/heads/integration", graph.base)
    configure_plan(graph)
    # Development changes while ticket work is underway; preparation must use its
    # current tip rather than the starting development identity.
    external_tree = graph.home / "development"
    graph.git("worktree", "add", "--detach", str(external_tree), graph.base)
    (external_tree / "value.txt").write_text(original.replace("six", "development six"))
    import subprocess

    subprocess.run(
        ["git", "-C", str(external_tree), "commit", "-am", "Development change"],
        check=True,
        capture_output=True,
    )
    external = graph.git("-C", str(external_tree), "rev-parse", "HEAD")
    extend_agent(
        graph,
        "if a['role'] == 'implementation' and a['ticket'] == '01':\n"
        "    Path('value.txt').write_text(Path('value.txt').read_text().replace('one', 'feature one'))\n"
        f"    git('update-ref', 'refs/heads/dev', {external!r})",
    )
    result = run_until_wait(graph)
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["starting_development_revision"] == graph.base
    assert record["development_revision"] == graph.git("rev-parse", "dev") == external
    candidate = record["milestone"]["candidate_revision"]
    assert graph.git("show", "-s", "--format=%P", candidate).split() == [
        external,
        record["milestone"]["feature_revision"],
    ]
    assert (
        graph.git("show", candidate + ":value.txt")
        == "feature one\ntwo\nthree\nfour\nfive\ndevelopment six"
    )
    request = json.loads(Path(record["qa_request"]).read_text())
    assert request["development_revision"] == external
    assert request["candidate_revision"] == candidate
    assert all(record["tickets"][t]["attempt"] == 0 for t in ("02", "04"))


@pytest.mark.parametrize("resolved", [False, True])
def test_conflicting_development_preserves_resolution_and_requires_renewed_reviews(graph, resolved):
    import subprocess

    from test_dependencies import extend_agent

    configure_plan(graph)
    external_tree = graph.home / "development"
    graph.git("worktree", "add", "--detach", str(external_tree), graph.base)
    (external_tree / "value.txt").write_text("development conflict\n")
    subprocess.run(
        ["git", "-C", str(external_tree), "commit", "-am", "Conflicting development"],
        check=True,
        capture_output=True,
    )
    external = graph.git("-C", str(external_tree), "rev-parse", "HEAD")
    graph.git("update-ref", "refs/heads/dev", external)
    extend_agent(
        graph,
        "if a['role'] == 'implementation' and a['ticket'] == '01':\n"
        "    Path('value.txt').write_text('feature conflict\\n')",
    )
    if resolved:
        # Real target configuration resolves the conflict; the independent plain
        # merge must still detect that this source has no applicable approvals.
        (graph.repo / ".git/info/attributes").write_text("value.txt merge=fixture\n")
        graph.git("config", "merge.fixture.driver", "printf 'unreviewed resolution\\n' > %A")
    result = run_until_wait(graph)
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "milestone-candidate"
    assert record["milestone"]["state"] == "preparation_failed"
    assert "qa_request" not in record
    assert not (graph.output / "qa-request.json").exists()
    assert graph.git("rev-parse", "dev") == external
    assert graph.git("rev-parse", "integration") == record["milestone"]["feature_revision"]
    assert all(record["tickets"][t]["state"] == "Done" for t in ("01", "03"))
    assert all(record["tickets"][t]["attempt"] == 0 for t in ("02", "04"))
    source = graph.output / "worktrees/milestone-candidate/value.txt"
    if resolved:
        assert source.read_text() == "unreviewed resolution\n"
        assert "renewed checks and reviews required" in record["failure"]["message"]
        assert "CONFLICT" in record["failure"]["message"]
        assert record["milestone"]["candidate_revision"]
    else:
        assert "<<<<<<<" in source.read_text()
        assert "CONFLICT" in record["failure"]["message"]
    assert record["gates"][-1]["stage"] == "candidate"


def test_development_already_containing_the_feature_still_runs_exact_milestone_regression(graph):
    configure_plan(graph)
    script = graph.home / "suite.py"
    script.write_text(
        "import json, os, subprocess\nfrom pathlib import Path\n"
        "if os.environ['TICKET_HARNESS_STAGE'] == 'milestone-regression':\n"
        "    record = json.loads((Path.cwd().parents[1] / 'run.json').read_text())\n"
        "    assert record['outcome'] == 'preparing_milestone', record['outcome']\n"
        "    assert record['milestone']['state'] == 'preparing'\n"
        "if os.environ['TICKET_HARNESS_STAGE'] == 'candidate' and Path('last-ticket').read_text() == '01':\n"
        "    subprocess.run(['git', 'update-ref', 'refs/heads/dev', 'HEAD'], check=True)\n"
    )
    graph.config["suite"] = [graph.config["agent"][0], str(script)]
    result = run_until_wait(graph)
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    feature = record["milestone"]["feature_revision"]
    assert record["milestone"]["candidate_revision"] == record["development_revision"] == feature
    assert graph.git("rev-parse", "dev") == graph.git("rev-parse", "integration") == feature
    assert record["gates"][-1]["stage"] == "milestone-regression"
    assert record["gates"][-1]["revision"] == feature
    assert record["gates"][-1]["passed"]
    assert json.loads(Path(record["qa_request"]).read_text())["candidate_revision"] == feature
    assert record["feature_complete"] is False
