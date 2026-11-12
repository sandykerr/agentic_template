"""Run coordination and runner-owned verification of commands and agent reports."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from uuid import uuid4

from ticket_harness import agents, inputs, qa, tickets
from ticket_harness.git import git, require_direct_branches, require_unchanged, worktree
from ticket_harness.records import (
    GateFailure,
    NonRepairableFailure,
    execute,
    protect,
    write_json,
)


class _Run:
    """Own start/continuation, scheduling, outcomes and canonical verification evidence."""

    def __init__(self, output: Path, checkpoint: dict[str, Any] | None) -> None:
        self.output = output
        self._checkpoint = checkpoint
        (output / "inputs").mkdir(exist_ok=checkpoint is not None)
        self.artifacts = output / "artifacts"
        self.artifacts.mkdir(exist_ok=checkpoint is not None)
        self.trees = output / "worktrees"
        self.trees.mkdir(exist_ok=checkpoint is not None)
        self.record: dict[str, Any] = (
            checkpoint["record"]
            if checkpoint
            else {
                "outcome": "running",
                "artifacts": str(self.artifacts),
                "inputs": {},
                "ticket": {"state": "Ready", "attempt": 0},
                "gates": [],
                "attempts": [],
            }
        )
        self.config: dict[str, Any] = {}
        self.approved_source: set[str] = set()
        self.verified: list[tuple[dict[str, Any], Path, str]] = []
        self.milestone_index = 0
        self.stage = "inputs"

    def execute(self, config_path: Path | None = None) -> tuple[dict[str, Any], int]:
        """Start from prepared inputs or continue the validated deliberate checkpoint."""
        output = self.output
        checkpoint = self._checkpoint
        record = self.record
        if checkpoint is None:
            self.save()
        try:
            if checkpoint is None:
                if config_path is None:
                    raise ValueError("Fresh execution requires a configuration path")
                prepared = inputs.load(config_path, output)
                config = prepared.execution_config()
                snapshots = prepared.snapshots
                record["inputs"] = snapshots
                for field in ("requirements", "max_repairs", "timeouts", "selected_tickets"):
                    record[field] = config[field]
                if "plan" in config:
                    record.update(
                        run_id=uuid4().hex,
                        plan=config["plan"],
                        worker_settings=config["worker_settings"],
                        feature_complete=False,
                        milestone={
                            "id": config["plan"]["milestones"][0]["id"],
                            "state": "executing",
                        },
                    )
                tickets.initialize(record, config, prepared.primary)
            else:
                config = checkpoint["config"]
                snapshots = record["inputs"]
                self.restore_checks(checkpoint)
                self.milestone_index = checkpoint["milestone_index"]
                record.pop("checkpoint_sha256", None)
                # Invalidate the stopped state before executing any continuation work.
                record["outcome"] = "awaiting_human_qa"
                self.save()
            self.config = config
            repository = Path(config["repository"])
            for snapshot in snapshots.values():
                try:
                    self.approved_source.add(str(Path(snapshot["source"]).relative_to(repository)))
                except ValueError:
                    continue
            integration = config["integration"]
            planned = "plan" in config
            if checkpoint is None:
                require_direct_branches(repository, integration)
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
                    require_direct_branches(repository, development)
                    record["development_branch"] = development
                    record["development_revision"] = git(
                        repository, "rev-parse", "--verify", f"refs/heads/{development}^{{commit}}"
                    )
                record.update(
                    base_revision=base, integration_revision=base, integration_branch=integration
                )
                self.stage = "baseline"
                with self.git_operation("baseline-worktree"):
                    baseline = worktree(repository, self.trees / "baseline", base)
                self.check("baseline", config["suite"], baseline, base)
                require_unchanged(baseline, base)
            for index in range(
                self.milestone_index, len(config["plan"]["milestones"]) if planned else 1
            ):
                self.milestone_index = index
                if planned and index and checkpoint is None:
                    group = config["plan"]["milestones"][index]
                    record["selected_tickets"] = sorted(group["tickets"], key=int)
                    record["milestone"] = {"id": group["id"], "state": "executing"}
                    record["outcome"] = "running"
                    tickets.unlock(record, config)
                    self.save()
                while (ticket := tickets.next_ready(record, config, index)) is not None:
                    record["ticket"] = record["tickets"][ticket]
                    candidate_revision = tickets._TicketExecution(
                        ticket,
                        record["integration_revision"],
                        config,
                        snapshots,
                        record["ticket"],
                        record["attempts"],
                        record["gates"],
                        self.approved_source,
                        _TicketVerification(self, ticket),
                    ).execute()
                    record["integration_revision"] = candidate_revision
                    tickets.unlock(record, config)
                    self.save()
                record["outcome"] = "preparing_milestone" if planned else "completed"
                if planned:
                    review = qa.MilestoneReview(
                        record,
                        config,
                        output,
                        index,
                        self.trees / self.artifact_name("milestone-candidate"),
                        self.artifacts / self.artifact_name("qa-request.json"),
                        self,
                    )
                    if review.execute(checkpoint) is qa.ReviewOutcome.STOPPED:
                        return record, 2
                checkpoint = None
            if planned:
                record.update(outcome="completed", feature_complete=True)
            self.save()
            return record, 0
        except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
            stage = self.stage
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
            self.save()
            return record, 1

    def save(self) -> None:
        write_json(self.output / "run.json", self.record)

    def export_checks(self) -> list[list[Any]]:
        """Return verification references in the existing JSON-safe checkpoint shape."""
        return [[item, str(source), revision] for item, source, revision in self.verified]

    def restore_checks(self, checkpoint: dict[str, Any]) -> None:
        # Only canonical gate records may be invalidated, including after JSON restoration.
        self.verified = [
            (self.record["gates"][self.record["gates"].index(item)], Path(source), revision)
            for item, source, revision in checkpoint["verified"]
        ]

    def reject_checks(self, ticket: str) -> None:
        # Prior reports remain inspectable but cannot authorize another submission.
        self.verified[:] = [entry for entry in self.verified if entry[0].get("ticket") != ticket]
        self.validate_sources()

    def artifact_name(self, stage: str, ticket: str | None = None, attempt: int = 0) -> str:
        name = stage if attempt <= 1 else f"attempt-{attempt}-{stage}"
        if attempt and len(self.record["tickets"]) > 1:
            name = f"ticket-{ticket}-{name}"
        if not attempt and self.milestone_index:
            name = f"milestone-{self.milestone_index + 1}-{name}"
        return name

    def protected_paths(self) -> dict[Path, bool]:
        protected = {
            self.output / name: True
            for name in (
                "run.json",
                "qa-request.json",
                "qa-decision.json",
                "qa-checkpoint.json",
                "stop-request.json",
            )
        }
        protected.update({path: True for path in (self.output / "checkpoints").glob("*.json")})
        for snapshot in self.record["inputs"].values():
            protected[Path(snapshot["source"])] = False
            protected[Path(snapshot["artifact"])] = True
        for tree in self.trees.iterdir():
            protected.update({tree / relative: False for relative in self.approved_source})
        return protected

    @contextmanager
    def git_operation(
        self, name: str, ticket: str | None = None, attempt: int = 0
    ) -> Iterator[None]:
        name = self.artifact_name(name, ticket, attempt)
        operation: dict[str, Any] = {
            "stage": name,
            "ticket": ticket if attempt else None,
            "attempt": attempt,
            "passed": False,
        }
        self.record.setdefault("operations", []).append(operation)
        self.save()
        try:
            with protect(self.protected_paths(), self.artifacts, name, operation):
                yield
            if operation.get("integrity"):
                raise NonRepairableFailure(operation["diagnostic"])
            operation["passed"] = True
        except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
            operation["diagnostic"] = str(error)
            if operation.get("integrity"):
                raise NonRepairableFailure(str(error)) from error
            raise
        finally:
            self.save()

    def validate_sources(self) -> None:
        failures = []
        for evidence, source, revision in self.verified:
            try:
                require_unchanged(source, revision)
            except GateFailure as error:
                evidence.update(
                    passed=False, verification_status="invalidated", diagnostic=str(error)
                )
                failures.append(str(error))
        if failures:
            self.save()
            raise GateFailure("; ".join(failures))

    def check(
        self,
        stage: str,
        argv: list[str],
        source: Path,
        revision: str,
        prompt: dict[str, Any] | None = None,
        *,
        ticket: str | None = None,
        attempt: int = 0,
        owner: tickets._Attempt | None = None,
    ) -> dict[str, Any]:
        self.stage = stage
        repairable = True
        inputs.require_approved(self.record["inputs"])
        self.validate_sources()
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
            self.artifacts,
            stage,
            revision,
            self.config["timeouts"][timeout_category],
            prompt,
            self.protected_paths(),
            self.artifact_name(stage, ticket, attempt),
        )
        result["ticket"] = ticket if attempt else None
        result["attempt"] = attempt
        result["timeout_category"] = timeout_category
        if result.get("integrity"):
            repairable = False
        self.record["gates"].append(result)
        self.save()
        try:
            if result.get("execution_error"):
                repairable = False
                self.record["environment_failure"] = True
                raise GateFailure(f"Execution environment failure: {result['execution_error']}")
            if prompt is not None and result["timed_out"]:
                result["report_status"] = "not-evaluated"
                self.save()
            if prompt is not None and not result["timed_out"]:
                observation = agents.report(Path(result["stdout"]), prompt)
                result.update(observation)
                if observation["report_status"] == "invalid":
                    self.save()
                    raise GateFailure(f"{stage} report rejected: {observation['diagnostic']}")
                report = observation["report"]
                questions = []
                if stage == "implementation" and report["result"] == "human-decision-needed":
                    questions = report["unresolved_questions"]
                elif stage in ("spec", "standards"):
                    questions = [
                        f"{finding['requirement']}: {finding['resolution']}"
                        for finding in report["findings"]
                        if finding["classification"] == "blocking"
                        and finding["human_decision_needed"]
                    ]
                if questions:
                    repairable = False
                    decision = {
                        "role": stage,
                        "attempt": attempt,
                        "revision": revision,
                        "report": report,
                        "approved_inputs": self.record["inputs"],
                        "assignment": result["assignment"],
                        "stdout": result["stdout"],
                        "stderr": result["stderr"],
                    }
                    if owner is None:
                        raise NonRepairableFailure("Human decision has no owning attempt")
                    owner.attach_human_decision(decision)
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
                    and any(
                        finding["classification"] == "blocking" for finding in report["findings"]
                    )
                ):
                    result.update(passed=False, diagnostic="blocking review finding; see report")
                self.save()
            if stage != "implementation":
                self.verified.append((result, source, revision))
            try:
                self.validate_sources()
            except GateFailure as error:
                result.update(passed=False, diagnostic=str(error))
                self.save()
                raise
            if not result["passed"]:
                raise GateFailure(
                    f"Required gate failed: {stage}; "
                    + result.get("diagnostic", f"see {result['stderr']}")
                )
        except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
            if not repairable:
                raise NonRepairableFailure(str(error)) from error
            raise
        return result


class _TicketVerification:
    """Limit a ticket to scoped verification and durable observation operations.

    The runner retains its check registry, protection policy and persistence.
    Ticket policy cannot select another ticket's evidence, mutate run state or
    access the runner through this interface.
    """

    def __init__(self, execution: _Run, ticket: str) -> None:
        self.__execution = execution
        self.__ticket = ticket

    def observe(self, stage: str) -> None:
        self.__execution.stage = stage
        self.__execution.save()

    @contextmanager
    def operation(self, name: str, attempt: int) -> Iterator[Path]:
        # Worktree/artifact naming and protected Git observations remain run-owned.
        stage = "candidate" if name == "candidate-merge" else name.removesuffix("-worktree")
        destination = self.__execution.trees / self.__execution.artifact_name(
            stage, self.__ticket, attempt
        )
        with self.__execution.git_operation(name, self.__ticket, attempt):
            yield destination

    def check(
        self,
        stage: str,
        argv: list[str],
        source: Path,
        revision: str,
        attempt: int,
        owner: tickets._Attempt,
        prompt: dict[str, Any] | None = None,
    ) -> None:
        self.__execution.check(
            stage,
            argv,
            source,
            revision,
            prompt,
            ticket=self.__ticket,
            attempt=attempt,
            owner=owner,
        )

    def validate_sources(self, *, rejected: bool = False) -> None:
        inputs.require_approved(self.__execution.record["inputs"])
        if rejected:
            self.__execution.reject_checks(self.__ticket)
        else:
            self.__execution.validate_sources()


def run(config_path: Path, output: Path) -> tuple[dict[str, Any], int]:
    # Never overwrite an existing run, including its preserved rejected work.
    output.mkdir(parents=True, exist_ok=False)
    with qa.ownership(output):
        return _Run(output, None).execute(config_path)


def continue_run(output: Path) -> tuple[dict[str, Any], int]:
    try:
        with qa.ownership(output):
            checkpoint = qa.MilestoneReview.restore_checkpoint(output)
            return _Run(output, checkpoint).execute()
    except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
        qa.reject(output, "continue", error)
        raise ValueError(str(error)) from error
