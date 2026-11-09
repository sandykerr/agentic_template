"""Bounded ticket lifecycle and required gate ownership."""

import hashlib
import json
import stat
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from uuid import uuid4

from ticket_harness import agents, checkpoints, inputs
from ticket_harness.git import (
    candidate,
    capture,
    carry_changes,
    git,
    promote,
    promote_milestone,
    require_clean_milestone_candidate,
    require_reviewed_candidate,
    require_unchanged,
    worktree,
)
from ticket_harness.records import GateFailure, execute, protect, write_json


def run(config_path: Path, output: Path) -> tuple[dict[str, Any], int]:
    # Never overwrite an existing run, including its preserved rejected work.
    output.mkdir(parents=True, exist_ok=False)
    with checkpoints.ownership(output):
        return _run(config_path, output)


def continue_run(output: Path) -> tuple[dict[str, Any], int]:
    try:
        with checkpoints.ownership(output):
            checkpoint = checkpoints.restore(output)
            return _run(
                Path(checkpoint["record"]["inputs"]["configuration"]["source"]), output, checkpoint
            )
    except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
        checkpoints.reject(output, "continue", error)
        raise ValueError(str(error)) from error


def _run(
    config_path: Path, output: Path, checkpoint: dict[str, Any] | None = None
) -> tuple[dict[str, Any], int]:
    (output / "inputs").mkdir(exist_ok=checkpoint is not None)
    artifacts = output / "artifacts"
    artifacts.mkdir(exist_ok=checkpoint is not None)
    trees = output / "worktrees"
    trees.mkdir(exist_ok=checkpoint is not None)
    record: dict[str, Any] = {
        "outcome": "running",
        "artifacts": str(artifacts),
        "inputs": {},
        "ticket": {"state": "Ready", "attempt": 0},
        "gates": [],
        "attempts": [],
    }

    if checkpoint is not None:
        record = checkpoint["record"]

    def save() -> None:
        write_json(output / "run.json", record)

    attempt = 0
    repairable = False
    ticket: str | None = None

    milestone_index = 0

    def attempt_name(stage: str) -> str:
        name = stage if attempt <= 1 else f"attempt-{attempt}-{stage}"
        if attempt and len(record["tickets"]) > 1:
            name = f"ticket-{ticket}-{name}"
        if not attempt and milestone_index:
            name = f"milestone-{milestone_index + 1}-{name}"
        return name

    verified: list[tuple[dict[str, Any], Path, str]] = []

    def protected_paths() -> dict[Path, bool]:
        protected = {
            output / name: True
            for name in (
                "run.json",
                "qa-request.json",
                "qa-decision.json",
                "qa-checkpoint.json",
                "stop-request.json",
            )
        }
        protected.update({path: True for path in (output / "checkpoints").glob("*.json")})
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
    if checkpoint is None:
        save()
    try:
        if checkpoint is None:
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
        else:
            config = checkpoint["config"]
            snapshots = record["inputs"]
            planned = True
            active_tickets = record["selected_tickets"]
            completed = set(config["completed_tickets"]) | {
                key for key, item in record["tickets"].items() if item["state"] == "Done"
            }
            verified = [
                (item, Path(source), revision) for item, source, revision in checkpoint["verified"]
            ]
            milestone_index = checkpoint["milestone_index"]
            record.pop("checkpoint_sha256", None)
            # Invalidate the stopped state before executing any continuation work.
            record["outcome"] = "awaiting_human_qa"
            save()
        repository = Path(config["repository"])
        approved_source = set()
        for snapshot in snapshots.values():
            try:
                approved_source.add(str(Path(snapshot["source"]).relative_to(repository)))
            except ValueError:
                continue
        integration = config["integration"]
        if checkpoint is None:
            git(repository, "check-ref-format", f"refs/heads/{integration}")
            # Refuse to move a checked-out branch, even in another caller worktree.
            if (
                f"branch refs/heads/{integration}"
                in git(repository, "worktree", "list", "--porcelain").splitlines()
            ):
                raise GateFailure("Integration branch must not be checked out")
            base = git(repository, "rev-parse", "--verify", f"{config['base']}^{{commit}}")
            previous = git(
                repository, "rev-parse", "--verify", f"refs/heads/{integration}^{{commit}}"
            )
            if previous != base:
                raise GateFailure(
                    "This slice requires base and integration to name the same commit"
                )
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
        else:
            previous = record["integration_revision"]
            development = config["plan"]["development"]
        starting_milestone = milestone_index
        for milestone_index in range(
            starting_milestone, len(config["plan"]["milestones"]) if planned else 1
        ):
            if planned and milestone_index and checkpoint is None:
                group = config["plan"]["milestones"][milestone_index]
                active_tickets = group["tickets"]
                record["selected_tickets"] = sorted(active_tickets, key=int)
                record["milestone"] = {"id": group["id"], "state": "executing"}
                record["outcome"] = "running"
                for ticket_id in active_tickets:
                    if set(config["requirements"][ticket_id]["dependencies"]) <= completed:
                        record["tickets"][ticket_id]["state"] = "Ready"
                save()
            while any(record["tickets"][t]["state"] != "Done" for t in active_tickets):
                ready = [
                    key for key, state in record["tickets"].items() if state["state"] == "Ready"
                ]
                if not ready:
                    raise GateFailure("No selected ticket has verified prerequisites")
                ticket = (
                    next(
                        t
                        for t in config["plan"]["milestones"][milestone_index]["tickets"]
                        if t in ready
                    )
                    if planned
                    else min(ready, key=int)
                )
                record["ticket"] = record["tickets"][ticket]
                base = previous
                checks = {
                    name: config["checks"][name]
                    for name in config["requirements"][ticket]["checks"]
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
                                state="Verifying",
                                submitted_revision=submitted,
                                changed_files=changed,
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
                                and set(config["requirements"][ticket_id]["dependencies"])
                                <= completed
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
                        if (
                            not repairable
                            or stage == "integration"
                            or attempt > config["max_repairs"]
                        ):
                            raise
                        inputs.require_approved(snapshots)
                        # Rejected approvals cannot authorize the next submission. Baseline stays shared.
                        verified[:] = [
                            entry for entry in verified if entry[0].get("ticket") != ticket
                        ]
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
                if checkpoint is None:
                    milestone.update(state="preparing", feature_revision=previous)
                    development_base = git(repository, "rev-parse", f"refs/heads/{development}")
                    record.setdefault(
                        "starting_development_revision", record["development_revision"]
                    )
                    record["development_revision"] = development_base
                    milestone["development_revision"] = development_base
                    save()
                    candidate_source = trees / attempt_name("milestone-candidate")
                    try:
                        with git_operation(attempt_name("milestone-candidate-merge")):
                            revision = candidate(
                                repository, candidate_source, development_base, previous
                            )
                            milestone["candidate_revision"] = revision
                    except GateFailure as error:
                        raise GateFailure(
                            f"Milestone merge failed; renewed checks and reviews required: {error}"
                        ) from error
                    with git_operation(attempt_name("milestone-candidate-validation")):
                        require_clean_milestone_candidate(
                            repository, candidate_source, revision, development_base, previous
                        )
                    stage = "milestone-regression"
                    regression = gate(stage, config["suite"], candidate_source, revision)
                    stage = "milestone-readiness"
                    inputs.require_approved(snapshots)
                    validate_sources()
                    for branch, expected in (
                        (integration, previous),
                        (development, development_base),
                    ):
                        if git(repository, "rev-parse", f"refs/heads/{branch}") != expected:
                            raise GateFailure(
                                f"Branch {branch} changed externally; candidate invalidated"
                            )
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
                        "human_checks": config["plan"]["milestones"][milestone_index]["qa"],
                        "regression_evidence": [regression],
                    }
                    request_path = output / "qa-request.json"
                    write_json(request_path, request)
                    record["qa_request"] = str(request_path)
                    record["outcome"] = "awaiting_human_qa"
                    milestone["state"] = "awaiting_human_qa"
                    write_json(artifacts / attempt_name("qa-request.json"), request)
                    record["qa_decision"] = str(output / "qa-decision.json")
                    record["qa_decision_status"] = "missing"
                    # Freeze the actual evidence bytes while the human assesses this request.
                    evidence_bytes = {
                        path: path.read_bytes() for path in checkpoints.evidence_files(output)
                    }
                    request_bytes = request_path.read_bytes()
                    save()
                else:
                    request_path = output / "qa-request.json"
                    request_bytes = request_path.read_bytes()
                    request = json.loads(request_bytes)
                    candidate_source = Path(request["candidate_worktree"])
                    revision = request["candidate_revision"]
                    development_base = request["development_revision"]
                    evidence_bytes = {
                        Path(name): Path(name).read_bytes() for name in checkpoint["evidence"]
                    }
                    archive_path = output / "checkpoints" / f"{record['checkpoint_id']}.json"
                    evidence_bytes[archive_path] = archive_path.read_bytes()
                    checkpoint = None
                    record["outcome"] = "awaiting_human_qa"
                    save()
                stop_path = output / "stop-request.json"
                observed_decision: bytes | None = None
                while True:
                    if stop_path.exists():
                        stopping = json.loads(stop_path.read_text())
                        if stopping == {
                            "run_id": record["run_id"],
                            "request_id": request["request_id"],
                        }:
                            inputs.require_approved(snapshots)
                            validate_sources()
                            if (
                                request_path.is_symlink()
                                or request_path.read_bytes() != request_bytes
                            ):
                                raise GateFailure("QA request changed before stop")
                            for path, expected_bytes in evidence_bytes.items():
                                if path.is_symlink() or path.read_bytes() != expected_bytes:
                                    raise GateFailure(f"QA evidence changed before stop: {path}")
                            checkpoints.validate_request(config, request)
                            stop_path.unlink()
                            # Include observations made after the request was prepared.
                            frozen = {
                                path: path.read_bytes()
                                for path in checkpoints.evidence_files(output)
                            }
                            checkpoints.persist(
                                output,
                                record,
                                config,
                                verified,
                                milestone_index,
                                frozen,
                                request_bytes,
                            )
                            return record, 2
                        stop_path.unlink()
                    try:
                        decision_path = output / "qa-decision.json"
                        if decision_path.is_symlink() or not stat.S_ISREG(
                            decision_path.stat().st_mode
                        ):
                            raise OSError("QA decision must be a regular file")
                        raw = decision_path.read_bytes()
                    except OSError as error:
                        status = "missing" if isinstance(error, FileNotFoundError) else "unreadable"
                        if record["qa_decision_status"] != status:
                            record["qa_decision_status"] = status
                            record["qa_decision_diagnostic"] = str(error)
                            save()
                        observed_decision = None
                        time.sleep(0.1)
                        continue
                    if raw == observed_decision:
                        time.sleep(0.1)
                        continue
                    observed_decision = raw
                    decision_observation: dict[str, Any] = {
                        "sha256": hashlib.sha256(raw).hexdigest(),
                        "milestone": milestone["id"],
                        "request_id": request["request_id"],
                        "status": "rejected",
                    }
                    observation_path = (
                        artifacts
                        / f"qa-decision-{len(record.setdefault('qa_observations', []))}.json"
                    )
                    observation_path.write_bytes(raw)
                    evidence_bytes[observation_path] = raw
                    decision_observation["artifact"] = str(observation_path)
                    record["qa_observations"].append(decision_observation)
                    try:
                        decision = json.loads(raw, object_pairs_hook=inputs.unique_object)
                        if not isinstance(decision, dict) or set(decision) != {
                            "decision",
                            "request",
                        }:
                            raise GateFailure("Expected exactly decision and request fields")
                        if decision["decision"] != "APPROVED":
                            raise GateFailure("Expected exact decision APPROVED")
                        if json.dumps(decision["request"], sort_keys=True) != json.dumps(
                            request, sort_keys=True
                        ):
                            raise GateFailure("Decision does not match the current request")
                        if any(
                            d["request_id"] == request["request_id"]
                            for d in record.get("qa_decisions", [])
                        ):
                            raise GateFailure("Decision request was already consumed")
                    except (ValueError, GateFailure) as error:
                        decision_observation["diagnostic"] = str(error)
                        record["qa_decision_status"] = "rejected"
                        save()
                        continue
                    stage = "milestone-promotion"
                    inputs.require_approved(snapshots)
                    validate_sources()
                    if request_path.is_symlink() or request_path.read_bytes() != request_bytes:
                        raise GateFailure(
                            "QA request changed; renewed candidate acceptance required"
                        )
                    for path, expected_bytes in evidence_bytes.items():
                        if path.is_symlink() or path.read_bytes() != expected_bytes:
                            raise GateFailure(
                                f"QA evidence changed: {path}; renewed acceptance required"
                            )
                    # The ref transaction validates both expected tips and advances both together.
                    promote_milestone(
                        repository, integration, development, revision, previous, development_base
                    )
                    decision_observation["status"] = "consumed"
                    record.setdefault("qa_decisions", []).append(dict(decision_observation))
                    record["qa_decision_status"] = "consumed"
                    milestone.update(state="promoted", promoted_revision=revision)
                    record.setdefault("milestones", []).append(dict(milestone))
                    previous = revision
                    record["integration_revision"] = revision
                    record["development_revision"] = revision
                    save()
                    break
        if planned:
            record.update(outcome="completed", feature_complete=True)
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
            record["milestone"]["state"] = (
                "promotion_failed" if stage == "milestone-promotion" else "preparation_failed"
            )
        save()
        return record, 1
