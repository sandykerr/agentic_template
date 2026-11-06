"""Single-attempt ticket lifecycle and required gate ownership."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from ticket_harness import agents, inputs
from ticket_harness.git import (
    candidate,
    capture,
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
    }

    def save() -> None:
        write_json(output / "run.json", record)

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
        operation: dict[str, Any] = {"stage": name, "passed": False}
        record.setdefault("operations", []).append(operation)
        save()
        try:
            with protect(protected_paths(), artifacts, name, operation):
                yield
            if operation.get("integrity"):
                raise GateFailure(operation["diagnostic"])
            operation["passed"] = True
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
        inputs.require_approved(record["inputs"])
        validate_sources()
        result = execute(argv, source, artifacts, stage, revision, prompt, protected_paths())
        record["gates"].append(result)
        save()
        if prompt is not None:
            report = agents.report(result, prompt)
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
        stage = "implementation"
        record["ticket"].update(state="Running", attempt=1)
        save()
        with git_operation("implementation-worktree"):
            source = worktree(repository, trees / "implementation", base)
        prompt = agents.assignment(
            stage, ticket, base, base, snapshots, record["gates"][:], config["checks"]
        )
        gate(stage, config["agent"], source, base, prompt)
        with git_operation("submission"):
            submitted, changed = capture(source, base, ticket)
            record["ticket"].update(
                state="Verifying", submitted_revision=submitted, changed_files=changed
            )
        save()
        if approved_source.intersection(changed):
            raise GateFailure("Submission changed approved input source; human decision required")
        for name, argv in config["checks"].items():
            stage = f"check-{name}"
            gate(stage, argv, source, submitted)
            require_unchanged(source, submitted)
        for role in ("spec", "standards"):
            stage = role
            with git_operation(f"{role}-worktree"):
                review_source = worktree(repository, trees / role, submitted)
            prompt = agents.assignment(
                role, ticket, base, submitted, snapshots, record["gates"][:], config["checks"]
            )
            gate(role, config["agent"], review_source, submitted, prompt)
            require_unchanged(review_source, submitted)
            save()
        stage = "candidate"
        candidate_source = trees / "candidate"
        with git_operation("candidate-merge"):
            revision = candidate(repository, candidate_source, base, submitted)
            record["ticket"]["candidate_revision"] = revision
        save()
        require_reviewed_candidate(candidate_source, revision, base, submitted)
        gate(stage, config["suite"], candidate_source, revision)
        require_unchanged(candidate_source, revision)
        stage = "integration"
        inputs.require_approved(snapshots)
        validate_sources()
        promote(repository, integration, revision, previous)
        record["ticket"].update(state="Done", done_revision=revision)
        record["outcome"] = "completed"
        save()
        return record, 0
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
