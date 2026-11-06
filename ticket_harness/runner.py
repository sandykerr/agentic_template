"""Bounded ticket lifecycle and required gate ownership."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

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

    def attempt_name(stage: str) -> str:
        return stage if attempt <= 1 else f"attempt-{attempt}-{stage}"

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
        operation: dict[str, Any] = {"stage": name, "attempt": attempt, "passed": False}
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
        result = execute(
            argv, source, artifacts, stage, revision, prompt, protected_paths(), attempt_name(stage)
        )
        result["attempt"] = attempt
        if result.get("integrity"):
            repairable = False
        record["gates"].append(result)
        save()
        if prompt is not None:
            report = agents.report(result, prompt)
            if stage == "implementation" and report["result"] == "human-decision-needed":
                repairable = False
            if result["exit_code"] != 0:
                result.update(
                    passed=False,
                    diagnostic=f"process exit {result['exit_code']}; see {result['stderr']}",
                )
            elif stage == "implementation" and report["result"] == "human-decision-needed":
                result.update(
                    passed=False,
                    diagnostic="human decision needed: "
                    + "; ".join(report["unresolved_questions"]),
                )
            elif stage in ("spec", "standards") and any(
                finding["classification"] == "blocking" for finding in report["findings"]
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
        record["ticket"]["id"] = ticket
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
        record["base_revision"] = base
        record["integration_branch"] = integration
        stage = "baseline"
        with git_operation("baseline-worktree"):
            baseline = worktree(repository, trees / "baseline", base)
        gate(stage, config["suite"], baseline, base)
        require_unchanged(baseline, base)
        start_revision = base
        repair_context = None
        previous_source = None
        for attempt in range(1, config["max_repairs"] + 2):
            repairable = True
            current: dict[str, Any] = {
                "attempt": attempt,
                "state": "Running",
                "starting_revision": start_revision,
                "gate_start": len(record["gates"]),
            }
            record["attempts"].append(current)
            try:
                stage = "implementation"
                record["ticket"] = {"id": ticket, "state": "Running", "attempt": attempt}
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
                    snapshots,
                    record["gates"][:],
                    config["checks"],
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
                for name, argv in config["checks"].items():
                    stage = f"check-{name}"
                    gate(stage, argv, source, submitted)
                    require_unchanged(source, submitted)
                for role in ("spec", "standards"):
                    stage = role
                    with git_operation(attempt_name(f"{role}-worktree")):
                        review_source = worktree(repository, trees / attempt_name(role), submitted)
                    prompt = agents.assignment(
                        role,
                        ticket,
                        base,
                        submitted,
                        snapshots,
                        record["gates"][:],
                        config["checks"],
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
                record["outcome"] = "completed"
                save()
                return record, 0
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
                verified[:] = [entry for entry in verified if entry[0]["stage"] == "baseline"]
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
                        for key in ("submitted_revision", "candidate_revision")
                        if key in item
                    ],
                }
        raise GateFailure("Repair allowance exhausted")
    except (GateFailure, OSError, ValueError, KeyError, TypeError) as error:
        outcome = (
            "invalid-input"
            if stage == "inputs"
            else "environment"
            if stage == "baseline"
            else "incomplete"
        )
        record.update(outcome=outcome, failure={"stage": stage, "message": str(error)})
        record["ticket"]["state"] = "Blocked"
        save()
        return record, 1
