"""Ticket readiness, complete implementation attempts, and bounded repairs."""

from pathlib import Path
from typing import TYPE_CHECKING, Any

from ticket_harness import agents
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
    from ticket_harness.runner import _TicketVerification


class _Attempt:
    """Own one assignment's observations and their current-ticket projection.

    History keeps the canonical attempt dictionary; the current ticket deliberately
    exposes only the existing public projection. No persistence or repair policy
    belongs here: callers save at their existing atomic operation boundaries.
    """

    def __init__(
        self,
        ticket: str,
        number: int,
        starting_revision: str,
        current_ticket: dict[str, Any],
        history: list[dict[str, Any]],
        gates: list[dict[str, Any]],
    ) -> None:
        """Register a Running attempt in history and reset its shared ticket projection."""
        self._ticket = current_ticket
        self._gates = gates
        self._record: dict[str, Any] = {
            "ticket": ticket,
            "attempt": number,
            "state": "Running",
            "starting_revision": starting_revision,
            "gate_start": len(gates),
        }
        history.append(self._record)
        self._ticket.clear()
        self._ticket.update(id=ticket, state="Running", attempt=number)

    def observe_source(self, source: Path) -> None:
        """Retain the implementation worktree on attempt evidence for rejection/repair."""
        # Source remains attempt evidence, not part of the public ticket projection.
        self._record["source"] = str(source)

    def submit(self, revision: str, changed_files: list[str]) -> None:
        """Record Git-derived submission facts and expose them on the current ticket."""
        self._record.update(
            state="Verifying", submitted_revision=revision, changed_files=changed_files
        )
        self._ticket.update(self._record)

    def observe_candidate(self, revision: str) -> None:
        """Attach the candidate revision to both attempt and current ticket evidence."""
        self._record["candidate_revision"] = revision
        self._ticket["candidate_revision"] = revision

    def complete(self, revision: str) -> None:
        """Mark attempt and ticket Done after integration; close the attempt gate range."""
        self._record.update(state="Done", done_revision=revision, gate_end=len(self._gates))
        self._ticket.update(state="Done", done_revision=revision)

    def reject(self, stage: str, error: Exception) -> None:
        """Close rejected attempt evidence while leaving terminal ticket policy to the run."""
        self._record.update(
            state="Rejected",
            failure={"stage": stage, "message": str(error)},
            gate_end=len(self._gates),
        )
        # Ticket state retains its last Running/Verifying observation until the
        # run classifies terminal failure as Blocked or a repair starts Running.
        # Rejected is an attempt observation, not a public ticket lifecycle state.

    def repair_start(self, previous_source: Path | None) -> tuple[str, Path | None, dict[str, str]]:
        """Describe preserved rejected work without assigning another repair."""
        return (
            self._record.get("submitted_revision", self._record["starting_revision"]),
            Path(self._record["source"]) if "source" in self._record else previous_source,
            self._record["failure"],
        )

    def attach_human_decision(self, decision: dict[str, Any]) -> None:
        """Attach a validated decision to this attempt and ticket, rejecting mismatched identity."""
        report = decision["report"]
        revision = self._record[
            "starting_revision" if decision["role"] == "implementation" else "submitted_revision"
        ]
        if (
            report["ticket"] != self._record["ticket"]
            or decision["attempt"] != self._record["attempt"]
            or report["attempt"] != self._record["attempt"]
            or decision["revision"] != revision
            or report["revision"] != revision
        ):
            raise NonRepairableFailure("Human decision does not identify its owning attempt")
        self._record["human_decision"] = decision
        self._ticket["human_decision"] = decision


def _completed(record: dict[str, Any], config: dict[str, Any]) -> set[str]:
    """Combine externally completed prerequisites with this run's Done tickets."""
    return set(config["completed_tickets"]) | {
        key for key, item in record["tickets"].items() if item["state"] == "Done"
    }


def initialize(record: dict[str, Any], config: dict[str, Any], primary: str) -> None:
    """Create Pending ticket records, unlock prerequisites, and alias the active ticket."""
    selected = config["selected_tickets"]
    record["tickets"] = {
        ticket: {"id": ticket, "state": "Pending", "attempt": 0}
        for ticket in (config["plan"]["required_tickets"] if "plan" in config else selected)
    }
    unlock(record, config)
    record["ticket"] = record["tickets"][primary]


def unlock(record: dict[str, Any], config: dict[str, Any]) -> None:
    """Move selected Pending tickets to Ready when every prerequisite is completed."""
    completed = _completed(record, config)
    for ticket in record["selected_tickets"]:
        state = record["tickets"][ticket]
        if (
            state["state"] == "Pending"
            and set(config["requirements"][ticket]["dependencies"]) <= completed
        ):
            state["state"] = "Ready"


def next_ready(record: dict[str, Any], config: dict[str, Any], index: int) -> str | None:
    """Select the next Ready ticket in milestone/numeric order, or reject stalled work."""
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


class _TicketExecution:
    """Own one fixed-base ticket cycle, including its bounded repair decisions."""

    def __init__(
        self,
        ticket: str,
        base: str,
        config: dict[str, Any],
        snapshots: dict[str, Any],
        current_ticket: dict[str, Any],
        history: list[dict[str, Any]],
        gates: list[dict[str, Any]],
        approved_source: set[str],
        verification: "_TicketVerification",
    ) -> None:
        """Bind a fixed-base ticket cycle to shared evidence and scoped verification.

        Select its approved ticket snapshot without mutating the run snapshot mapping;
        attempt records and current-ticket observations retain their shared identity.
        """
        self._ticket = ticket
        self._base = base
        self._repository = Path(config["repository"])
        self._integration = config["integration"]
        self._development = config["plan"]["development"] if "plan" in config else None
        self._max_repairs = config["max_repairs"]
        self._agent = config["agent"]
        self._suite = config["suite"]
        self._checks = {
            name: config["checks"][name] for name in config["requirements"][ticket]["checks"]
        }
        self._snapshots = dict(snapshots)
        active_input = next(
            name
            for name, snapshot in snapshots.items()
            if snapshot["source"] == config["requirements"][ticket]["source"]
            and (name == "ticket" or name.startswith("ticket-"))
        )
        self._snapshots["ticket"], self._snapshots[active_input] = (
            self._snapshots[active_input],
            self._snapshots["ticket"],
        )
        self._current_ticket = current_ticket
        self._history = history
        self._gates = gates
        self._approved_source = approved_source
        self._verification = verification
        self._current: _Attempt | None = None
        self._start_revision = base
        self._previous_source: Path | None = None
        self._repair_context: dict[str, Any] | None = None

    def _ticket_gates(self) -> list[dict[str, Any]]:
        """Select shared and current-ticket evidence without copying canonical gate records."""
        # Earlier ticket reports stay inspectable without authorizing this assignment.
        return [gate for gate in self._gates if gate["ticket"] in (None, self._ticket)]

    def execute(self) -> str:
        """Run bounded attempts through submission, checks, reviews and candidate testing.

        Return the tested revision only after expected-old integration succeeds.
        Reject failed attempts before deciding whether preserved work may be repaired;
        nonrepairable failures, integration failures and exhaustion propagate.
        """
        for attempt in range(1, self._max_repairs + 2):
            current = _Attempt(
                self._ticket,
                attempt,
                self._start_revision,
                self._current_ticket,
                self._history,
                self._gates,
            )
            self._current = current
            try:
                stage = "implementation"
                source, submitted = self._implement(attempt, current)
                for name, argv in self._checks.items():
                    stage = f"check-{name}"
                    self._verification.check(stage, argv, source, submitted, attempt, current)
                    require_unchanged(source, submitted)
                for role in ("spec", "standards"):
                    stage = role
                    with self._verification.operation(f"{role}-worktree", attempt) as destination:
                        review_source = worktree(self._repository, destination, submitted)
                    prompt = agents.assignment(
                        role,
                        self._ticket,
                        self._base,
                        submitted,
                        self._snapshots,
                        self._ticket_gates(),
                        self._checks,
                        attempt,
                    )
                    self._verification.check(
                        role, self._agent, review_source, submitted, attempt, current, prompt
                    )
                    require_unchanged(review_source, submitted)
                    self._verification.observe(stage)
                stage = "candidate"
                with self._verification.operation("candidate-merge", attempt) as candidate_source:
                    revision = candidate(self._repository, candidate_source, self._base, submitted)
                    current.observe_candidate(revision)
                self._verification.observe(stage)
                require_reviewed_candidate(candidate_source, revision, self._base, submitted)
                self._verification.check(
                    stage, self._suite, candidate_source, revision, attempt, current
                )
                require_unchanged(candidate_source, revision)
                stage = "integration"
                self._verification.observe(stage)
                self._verification.validate_sources()
                promote(
                    self._repository, self._integration, revision, self._base, self._development
                )
                current.complete(revision)
                return revision
            except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
                current.reject(stage, error)
                self._verification.observe(stage)
                if (
                    isinstance(error, NonRepairableFailure)
                    or stage == "integration"
                    or attempt > self._max_repairs
                ):
                    raise
                self._prepare_repair(current, error)
        raise AssertionError("Ticket execution requires an initial attempt")

    def _implement(self, attempt: int, current: _Attempt) -> tuple[Path, str]:
        """Prepare preserved work, run implementation and capture its submission.

        Register source/submission observations before validating approved paths,
        so rejected work remains available to the existing repair policy.
        """
        self._verification.observe("implementation")
        with self._verification.operation("implementation-worktree", attempt) as destination:
            source = worktree(self._repository, destination, self._start_revision)
            if self._previous_source is not None:
                carry_changes(self._previous_source, source)
            current.observe_source(source)
        prompt = agents.assignment(
            "implementation",
            self._ticket,
            self._base,
            self._start_revision,
            self._snapshots,
            self._ticket_gates(),
            self._checks,
            attempt,
            self._repair_context,
        )
        self._verification.check(
            "implementation", self._agent, source, self._start_revision, attempt, current, prompt
        )
        with self._verification.operation("submission", attempt):
            submitted, changed = capture(
                source,
                self._start_revision,
                self._ticket,
                self._base if attempt > 1 else None,
            )
            current.submit(submitted, changed)
        self._verification.observe("implementation")
        if self._approved_source.intersection(changed):
            raise NonRepairableFailure(
                "Submission changed approved input source; human decision required"
            )
        return source, submitted

    def _prepare_repair(self, current: _Attempt, error: Exception) -> None:
        """Invalidate rejected approvals and retain the next repair starting point.

        Refuse repair if integration or the preserved implementation HEAD moved;
        leave prior attempts and gate evidence intact for the next assignment.
        """
        self._verification.validate_sources(rejected=True)
        if git(self._repository, "rev-parse", f"refs/heads/{self._integration}") != self._base:
            raise GateFailure("Integration branch changed externally; repair stopped") from error
        self._start_revision, self._previous_source, failure = current.repair_start(
            self._previous_source
        )
        if (
            self._previous_source is not None
            and git(self._previous_source, "rev-parse", "HEAD") != self._start_revision
        ):
            raise GateFailure("Rejected implementation changed HEAD; repair stopped") from error
        self._repair_context = {
            "failure": failure,
            "rejected_revisions": [
                item[key]
                for item in self._history
                if item["ticket"] == self._ticket
                for key in ("submitted_revision", "candidate_revision")
                if key in item
            ],
        }
