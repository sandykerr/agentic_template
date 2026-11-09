"""Bounded ticket lifecycle and required gate ownership."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from uuid import uuid4

from ticket_harness import agents, inputs
from ticket_harness.git import (
    candidate,
    capture,
    carry_changes,
    git,
    promote,
    require_clean_milestone_candidate,
    require_reviewed_candidate,
    require_unchanged,
    worktree,
)
from ticket_harness.records import GateFailure, execute, protect, write_json


def run(config_path: Path, output: Path) -> tuple[dict[str, Any], int]:
    # Never overwrite an existing run, including its preserved rejected work.
    output.mkdir(parents=True, exist_ok=False)
    (output / "inputs").mkdir()
    artifacts = output / "artifacts"
    artifacts.mkdir()
    trees = output / "worktrees"
    trees.mkdir()
    record: dict[str, Any] = {
        "outcome": "running",
        "artifacts": str(artifacts),
        "inputs": {},
        "ticket": {"state": "Ready", "attempt": 0},
        "gates": [],
        "attempts": [],
    }

    def save() -> None:
        write_json(output / "run.json", record)

    attempt = 0
    repairable = False
    ticket: str | None = None

    def attempt_name(stage: str) -> str:
        name = stage if attempt <= 1 else f"attempt-{attempt}-{stage}"
        if attempt and len(config["selected_tickets"]) > 1:
            name = f"ticket-{ticket}-{name}"
        return name

    verified: list[tuple[dict[str, Any], Path, str]] = []

    def protected_paths() -> dict[Path, bool]:
        protected = {output / "run.json": True}
        for snapshot in record["inputs"].values():
            protected[Path(snapshot["source"])] = False
            protected[Path(snapshot["artifact"])] = True
        for tree in trees.iterdir():
            protected.update({tree / relative: False for relative in approved_source})
        return protected

    @contextmanager
    def git_operation(name: str) -> Iterator[None]:
        nonlocal repairable
        operation: dict[str, Any] = {
            "stage": name,
            "ticket": ticket if attempt else None,
            "attempt": attempt,
            "passed": False,
        }
        record.setdefault("operations", []).append(operation)
        save()
        try:
            with protect(protected_paths(), artifacts, name, operation):
                yield
            if operation.get("integrity"):
                repairable = False
                raise GateFailure(operation["diagnostic"])
            operation["passed"] = True
        except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
            operation["diagnostic"] = str(error)
            if operation.get("integrity"):
                repairable = False
            raise
        finally:
            save()

    def validate_sources() -> None:
        failures = []
        for evidence, source, revision in verified:
            try:
                require_unchanged(source, revision)
            except GateFailure as error:
                evidence.update(
                    passed=False, verification_status="invalidated", diagnostic=str(error)
                )
                failures.append(str(error))
        if failures:
            save()
            raise GateFailure("; ".join(failures))

    def gate(
        stage: str,
        argv: list[str],
        source: Path,
        revision: str,
        prompt: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        nonlocal repairable
        inputs.require_approved(record["inputs"])
        validate_sources()
        timeout_category = (
            "repair"
            if stage == "implementation" and attempt > 1
            else "candidate"
            if stage == "milestone-regression"
            else "checks"
            if stage.startswith("check-")
            else stage
        )
        result = execute(
            argv,
            source,
            artifacts,
            stage,
            revision,
            config["timeouts"][timeout_category],
            prompt,
            protected_paths(),
            attempt_name(stage),
        )
        result["ticket"] = ticket if attempt else None
        result["attempt"] = attempt
        result["timeout_category"] = timeout_category
        if result.get("integrity"):
            repairable = False
        record["gates"].append(result)
        save()
        if result.get("execution_error"):
            repairable = False
            record["environment_failure"] = True
            raise GateFailure(f"Execution environment failure: {result['execution_error']}")
        if prompt is not None and result["timed_out"]:
            result["report_status"] = "not-evaluated"
            save()
        if prompt is not None and not result["timed_out"]:
            report = agents.report(result, prompt)
            questions = []
            if stage == "implementation" and report["result"] == "human-decision-needed":
                questions = report["unresolved_questions"]
            elif stage in ("spec", "standards"):
                questions = [
                    f"{finding['requirement']}: {finding['resolution']}"
                    for finding in report["findings"]
                    if finding["classification"] == "blocking" and finding["human_decision_needed"]
                ]
            if questions:
                repairable = False
                decision = {
                    "role": stage,
                    "attempt": attempt,
                    "revision": revision,
                    "report": report,
                    "approved_inputs": record["inputs"],
                    "assignment": result["assignment"],
                    "stdout": result["stdout"],
                    "stderr": result["stderr"],
                }
                record["ticket"]["human_decision"] = decision
                record["attempts"][-1]["human_decision"] = decision
            if result["exit_code"] != 0:
                result.update(
                    passed=False,
                    diagnostic=f"process exit {result['exit_code']}; see {result['stderr']}",
                )
            if questions:
                result.update(
                    passed=False,
                    diagnostic="human decision needed: "
                    + "; ".join(questions)
                    + (f"; {result['diagnostic']}" if result["exit_code"] != 0 else ""),
                )
            elif (
                result["exit_code"] == 0
                and stage in ("spec", "standards")
                and any(finding["classification"] == "blocking" for finding in report["findings"])
            ):
                result.update(passed=False, diagnostic="blocking review finding; see report")
            save()
        if stage != "implementation":
            verified.append((result, source, revision))
        try:
            validate_sources()
        except GateFailure as error:
            result.update(passed=False, diagnostic=str(error))
            save()
            raise
        if not result["passed"]:
            raise GateFailure(
                f"Required gate failed: {stage}; "
                + result.get("diagnostic", f"see {result['stderr']}")
            )
        return result

    stage = "inputs"
    save()
    try:
        config, snapshots, ticket = inputs.load(config_path, output)
        record["inputs"] = snapshots
        record["requirements"] = config["requirements"]
        record["max_repairs"] = config["max_repairs"]
        record["timeouts"] = config["timeouts"]
        record["selected_tickets"] = config["selected_tickets"]
        active_tickets = config["selected_tickets"]
        planned = "plan" in config
        if planned:
            record["run_id"] = uuid4().hex
            record["plan"] = config["plan"]
            record["worker_settings"] = config["worker_settings"]
            record["feature_complete"] = False
            record["milestone"] = {
                "id": config["plan"]["milestones"][0]["id"],
                "state": "executing",
            }
        completed = set(config["completed_tickets"])
        record["tickets"] = {
            ticket_id: {
                "id": ticket_id,
                "state": "Ready"
                if ticket_id in active_tickets
                and set(config["requirements"][ticket_id]["dependencies"]) <= completed
                else "Pending",
                "attempt": 0,
            }
            for ticket_id in (config["plan"]["required_tickets"] if planned else active_tickets)
        }
        record["ticket"] = record["tickets"][ticket]
        repository = Path(config["repository"])
        approved_source = set()
        for snapshot in snapshots.values():
            try:
                approved_source.add(str(Path(snapshot["source"]).relative_to(repository)))
            except ValueError:
                continue
        integration = config["integration"]
        git(repository, "check-ref-format", f"refs/heads/{integration}")
        # Refuse to move a checked-out branch, even in another caller worktree.
        if (
            f"branch refs/heads/{integration}"
            in git(repository, "worktree", "list", "--porcelain").splitlines()
        ):
            raise GateFailure("Integration branch must not be checked out")
        base = git(repository, "rev-parse", "--verify", f"{config['base']}^{{commit}}")
        previous = git(repository, "rev-parse", "--verify", f"refs/heads/{integration}^{{commit}}")
        if previous != base:
            raise GateFailure("This slice requires base and integration to name the same commit")
        if planned:
            development = config["plan"]["development"]
            git(repository, "check-ref-format", f"refs/heads/{development}")
            record["development_branch"] = development
            record["development_revision"] = git(
                repository, "rev-parse", "--verify", f"refs/heads/{development}^{{commit}}"
            )
        record["base_revision"] = base
        record["integration_revision"] = base
        record["integration_branch"] = integration
        stage = "baseline"
        with git_operation("baseline-worktree"):
            baseline = worktree(repository, trees / "baseline", base)
        gate(stage, config["suite"], baseline, base)
        require_unchanged(baseline, base)
        while any(record["tickets"][t]["state"] != "Done" for t in active_tickets):
            ready = [key for key, state in record["tickets"].items() if state["state"] == "Ready"]
            if not ready:
                raise GateFailure("No selected ticket has verified prerequisites")
            ticket = (
                next(t for t in config["plan"]["milestones"][0]["tickets"] if t in ready)
                if planned
                else min(ready, key=int)
            )
            record["ticket"] = record["tickets"][ticket]
            base = previous
            checks = {
                name: config["checks"][name] for name in config["requirements"][ticket]["checks"]
            }
            assignment_snapshots = dict(snapshots)
            active_input = next(
                name
                for name, snapshot in snapshots.items()
                if snapshot["source"] == config["requirements"][ticket]["source"]
                and (name == "ticket" or name.startswith("ticket-"))
            )
            assignment_snapshots["ticket"], assignment_snapshots[active_input] = (
                assignment_snapshots[active_input],
                assignment_snapshots["ticket"],
            )

            def ticket_gates() -> list[dict[str, Any]]:
                # Earlier ticket reports stay inspectable without authorizing this assignment.
                return [g for g in record["gates"] if g["ticket"] in (None, ticket)]

            start_revision = base
            repair_context = None
            previous_source = None
            for attempt in range(1, config["max_repairs"] + 2):
                repairable = True
                current: dict[str, Any] = {
                    "ticket": ticket,
                    "attempt": attempt,
                    "state": "Running",
                    "starting_revision": start_revision,
                    "gate_start": len(record["gates"]),
                }
                record["attempts"].append(current)
                try:
                    stage = "implementation"
                    record["ticket"].clear()
                    record["ticket"].update(id=ticket, state="Running", attempt=attempt)
                    save()
                    with git_operation(attempt_name("implementation-worktree")):
                        source = worktree(
                            repository, trees / attempt_name("implementation"), start_revision
                        )
                        if previous_source is not None:
                            carry_changes(previous_source, source)
                        current["source"] = str(source)
                    prompt = agents.assignment(
                        stage,
                        ticket,
                        base,
                        start_revision,
                        assignment_snapshots,
                        ticket_gates(),
                        checks,
                        attempt,
                        repair_context,
                    )
                    gate(stage, config["agent"], source, start_revision, prompt)
                    with git_operation(attempt_name("submission")):
                        submitted, changed = capture(
                            source, start_revision, ticket, base if attempt > 1 else None
                        )
                        current.update(
                            state="Verifying", submitted_revision=submitted, changed_files=changed
                        )
                        record["ticket"].update(current)
                    save()
                    if approved_source.intersection(changed):
                        repairable = False
                        raise GateFailure(
                            "Submission changed approved input source; human decision required"
                        )
                    for name, argv in checks.items():
                        stage = f"check-{name}"
                        gate(stage, argv, source, submitted)
                        require_unchanged(source, submitted)
                    for role in ("spec", "standards"):
                        stage = role
                        with git_operation(attempt_name(f"{role}-worktree")):
                            review_source = worktree(
                                repository, trees / attempt_name(role), submitted
                            )
                        prompt = agents.assignment(
                            role,
                            ticket,
                            base,
                            submitted,
                            assignment_snapshots,
                            ticket_gates(),
                            checks,
                            attempt,
                        )
                        gate(role, config["agent"], review_source, submitted, prompt)
                        require_unchanged(review_source, submitted)
                        save()
                    stage = "candidate"
                    candidate_source = trees / attempt_name("candidate")
                    with git_operation(attempt_name("candidate-merge")):
                        revision = candidate(repository, candidate_source, base, submitted)
                        record["ticket"]["candidate_revision"] = revision
                        current["candidate_revision"] = revision
                    save()
                    require_reviewed_candidate(candidate_source, revision, base, submitted)
                    gate(stage, config["suite"], candidate_source, revision)
                    require_unchanged(candidate_source, revision)
                    stage = "integration"
                    inputs.require_approved(snapshots)
                    validate_sources()
                    promote(repository, integration, revision, previous)
                    current.update(state="Done", done_revision=revision)
                    record["ticket"].update(state="Done", done_revision=revision)
                    current["gate_end"] = len(record["gates"])
                    previous = revision
                    record["integration_revision"] = revision
                    completed.add(ticket)
                    for ticket_id, state in record["tickets"].items():
                        if (
                            state["state"] == "Pending"
                            and ticket_id in active_tickets
                            and set(config["requirements"][ticket_id]["dependencies"]) <= completed
                        ):
                            state["state"] = "Ready"
                    save()
                    break
                except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
                    current.update(
                        state="Rejected",
                        failure={"stage": stage, "message": str(error)},
                        gate_end=len(record["gates"]),
                    )
                    save()
                    if not repairable or stage == "integration" or attempt > config["max_repairs"]:
                        raise
                    inputs.require_approved(snapshots)
                    # Rejected approvals cannot authorize the next submission. Baseline stays shared.
                    verified[:] = [entry for entry in verified if entry[0].get("ticket") != ticket]
                    validate_sources()
                    if git(repository, "rev-parse", f"refs/heads/{integration}") != previous:
                        raise GateFailure(
                            "Integration branch changed externally; repair stopped"
                        ) from error
                    start_revision = current.get("submitted_revision", start_revision)
                    previous_source = (
                        Path(current["source"]) if "source" in current else previous_source
                    )
                    if (
                        previous_source is not None
                        and git(previous_source, "rev-parse", "HEAD") != start_revision
                    ):
                        raise GateFailure(
                            "Rejected implementation changed HEAD; repair stopped"
                        ) from error
                    repair_context = {
                        "failure": current["failure"],
                        "rejected_revisions": [
                            item[key]
                            for item in record["attempts"]
                            if item["ticket"] == ticket
                            for key in ("submitted_revision", "candidate_revision")
                            if key in item
                        ],
                    }
        record["outcome"] = "preparing_milestone" if planned else "completed"
        if planned:
            # Milestone preparation has no ticket repair budget and never changes refs.
            ticket = None
            attempt = 0
            repairable = False
            stage = "milestone-candidate"
            milestone = record["milestone"]
            milestone.update(state="preparing", feature_revision=previous)
            development_base = git(repository, "rev-parse", f"refs/heads/{development}")
            record["starting_development_revision"] = record["development_revision"]
            record["development_revision"] = development_base
            milestone["development_revision"] = development_base
            save()
            candidate_source = trees / "milestone-candidate"
            try:
                with git_operation("milestone-candidate-merge"):
                    revision = candidate(repository, candidate_source, development_base, previous)
                    milestone["candidate_revision"] = revision
            except GateFailure as error:
                raise GateFailure(
                    f"Milestone merge failed; renewed checks and reviews required: {error}"
                ) from error
            with git_operation("milestone-candidate-validation"):
                require_clean_milestone_candidate(
                    repository, candidate_source, revision, development_base, previous
                )
            stage = "milestone-regression"
            regression = gate(stage, config["suite"], candidate_source, revision)
            stage = "milestone-readiness"
            inputs.require_approved(snapshots)
            validate_sources()
            for branch, expected in ((integration, previous), (development, development_base)):
                if git(repository, "rev-parse", f"refs/heads/{branch}") != expected:
                    raise GateFailure(f"Branch {branch} changed externally; candidate invalidated")
            request = {
                "request_id": uuid4().hex,
                "run_id": record["run_id"],
                "run_directory": str(output),
                "plan_version": config["plan"]["version"],
                "plan_approval": config["plan"]["approval"],
                "plan_input": snapshots["plan"],
                "milestone": milestone["id"],
                "feature_branch": integration,
                "feature_revision": previous,
                "development_branch": development,
                "development_revision": development_base,
                "candidate_revision": revision,
                "candidate_worktree": str(candidate_source),
                "human_checks": config["plan"]["milestones"][0]["qa"],
                "regression_evidence": [regression],
            }
            request_path = output / "qa-request.json"
            write_json(request_path, request)
            record["qa_request"] = str(request_path)
            record["outcome"] = "awaiting_human_qa"
            milestone["state"] = "awaiting_human_qa"
        save()
        return record, 0
    except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
        outcome = (
            "invalid-input"
            if stage == "inputs"
            else "environment"
            if stage == "baseline" or record.get("environment_failure")
            else "incomplete"
        )
        record.update(outcome=outcome, failure={"stage": stage, "message": str(error)})
        if record["ticket"]["state"] != "Done":
            record["ticket"]["state"] = "Blocked"
        if stage.startswith("milestone-") and "milestone" in record:
            record["milestone"]["state"] = "preparation_failed"
        save()
        return record, 1
