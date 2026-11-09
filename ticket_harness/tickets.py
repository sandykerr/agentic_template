"""Ticket readiness, complete implementation attempts, and bounded repairs."""

from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ticket_harness import agents, inputs
from ticket_harness.git import (
    candidate,
    capture,
    carry_changes,
    git,
    promote,
    require_reviewed_candidate,
    require_unchanged,
    worktree,
)
from ticket_harness.records import GateFailure, NonRepairableFailure

if TYPE_CHECKING:
    from ticket_harness.runner import _Run


def _completed(record: dict[str, Any], config: dict[str, Any]) -> set[str]:
    return set(config["completed_tickets"]) | {
        key for key, item in record["tickets"].items() if item["state"] == "Done"
    }


def initialize(record: dict[str, Any], config: dict[str, Any], primary: str) -> None:
    selected = config["selected_tickets"]
    record["tickets"] = {
        ticket: {"id": ticket, "state": "Pending", "attempt": 0}
        for ticket in (config["plan"]["required_tickets"] if "plan" in config else selected)
    }
    unlock(record, config)
    record["ticket"] = record["tickets"][primary]


def unlock(record: dict[str, Any], config: dict[str, Any]) -> None:
    completed = _completed(record, config)
    for ticket in record["selected_tickets"]:
        state = record["tickets"][ticket]
        if (
            state["state"] == "Pending"
            and set(config["requirements"][ticket]["dependencies"]) <= completed
        ):
            state["state"] = "Ready"


def next_ready(record: dict[str, Any], config: dict[str, Any], index: int) -> str | None:
    active = record["selected_tickets"]
    if all(record["tickets"][ticket]["state"] == "Done" for ticket in active):
        return None
    order = (
        config["plan"]["milestones"][index]["tickets"]
        if "plan" in config
        else sorted(active, key=int)
    )
    for ticket in order:
        if record["tickets"][ticket]["state"] == "Ready":
            return str(ticket)
    raise GateFailure("No selected ticket has verified prerequisites")


def execute(execution: "_Run", ticket: str) -> None:
    record, config = execution.record, execution.config
    snapshots = record["inputs"]
    repository = Path(config["repository"])
    integration = config["integration"]
    record["ticket"] = record["tickets"][ticket]
    base = record["integration_revision"]
    checks = {name: config["checks"][name] for name in config["requirements"][ticket]["checks"]}
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
        check = partial(execution.check, ticket=ticket, attempt=attempt)
        operation = partial(execution.git_operation, ticket=ticket, attempt=attempt)
        name_for = partial(execution.artifact_name, ticket=ticket, attempt=attempt)
        current: dict[str, Any] = {
            "ticket": ticket,
            "attempt": attempt,
            "state": "Running",
            "starting_revision": start_revision,
            "gate_start": len(record["gates"]),
        }
        record["attempts"].append(current)
        try:
            execution.stage = "implementation"
            record["ticket"].clear()
            record["ticket"].update(id=ticket, state="Running", attempt=attempt)
            execution.save()
            with operation("implementation-worktree"):
                source = worktree(
                    repository, execution.trees / name_for("implementation"), start_revision
                )
                if previous_source is not None:
                    carry_changes(previous_source, source)
                current["source"] = str(source)
            prompt = agents.assignment(
                execution.stage,
                ticket,
                base,
                start_revision,
                assignment_snapshots,
                ticket_gates(),
                checks,
                attempt,
                repair_context,
            )
            check(execution.stage, config["agent"], source, start_revision, prompt)
            with operation("submission"):
                submitted, changed = capture(
                    source, start_revision, ticket, base if attempt > 1 else None
                )
                current.update(
                    state="Verifying",
                    submitted_revision=submitted,
                    changed_files=changed,
                )
                record["ticket"].update(current)
            execution.save()
            if execution.approved_source.intersection(changed):
                raise NonRepairableFailure(
                    "Submission changed approved input source; human decision required"
                )
            for name, argv in checks.items():
                execution.stage = f"check-{name}"
                check(execution.stage, argv, source, submitted)
                require_unchanged(source, submitted)
            for role in ("spec", "standards"):
                execution.stage = role
                with operation(f"{role}-worktree"):
                    review_source = worktree(
                        repository, execution.trees / name_for(role), submitted
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
                check(role, config["agent"], review_source, submitted, prompt)
                require_unchanged(review_source, submitted)
                execution.save()
            execution.stage = "candidate"
            candidate_source = execution.trees / name_for("candidate")
            with operation("candidate-merge"):
                revision = candidate(repository, candidate_source, base, submitted)
                record["ticket"]["candidate_revision"] = revision
                current["candidate_revision"] = revision
            execution.save()
            require_reviewed_candidate(candidate_source, revision, base, submitted)
            check(execution.stage, config["suite"], candidate_source, revision)
            require_unchanged(candidate_source, revision)
            execution.stage = "integration"
            inputs.require_approved(snapshots)
            execution.validate_sources()
            promote(repository, integration, revision, base)
            current.update(state="Done", done_revision=revision)
            record["ticket"].update(state="Done", done_revision=revision)
            current["gate_end"] = len(record["gates"])
            record["integration_revision"] = revision
            unlock(record, config)
            execution.save()
            break
        except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
            current.update(
                state="Rejected",
                failure={"stage": execution.stage, "message": str(error)},
                gate_end=len(record["gates"]),
            )
            execution.save()
            if (
                isinstance(error, NonRepairableFailure)
                or execution.stage == "integration"
                or attempt > config["max_repairs"]
            ):
                raise
            inputs.require_approved(snapshots)
            execution.reject_checks(ticket)
            if git(repository, "rev-parse", f"refs/heads/{integration}") != base:
                raise GateFailure(
                    "Integration branch changed externally; repair stopped"
                ) from error
            start_revision = current.get("submitted_revision", start_revision)
            previous_source = Path(current["source"]) if "source" in current else previous_source
            if (
                previous_source is not None
                and git(previous_source, "rev-parse", "HEAD") != start_revision
            ):
                raise GateFailure("Rejected implementation changed HEAD; repair stopped") from error
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
