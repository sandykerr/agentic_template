"""Single-attempt ticket lifecycle and required gate ownership."""

from pathlib import Path
from typing import Any

from ticket_harness import agents, inputs
from ticket_harness.git import candidate, capture, git, promote, require_unchanged, worktree
from ticket_harness.records import GateFailure, execute, write_json


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

    def gate(
        stage: str,
        argv: list[str],
        source: Path,
        revision: str,
        prompt: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        result = execute(argv, source, artifacts, stage, revision, prompt)
        record["gates"].append(result)
        save()
        if not result["passed"]:
            raise GateFailure(f"Required gate failed: {stage}; see {result['stderr']}")
        return result

    stage = "inputs"
    save()
    try:
        config, snapshots, ticket = inputs.load(config_path, output)
        record["inputs"] = snapshots
        record["ticket"]["id"] = ticket
        repository = Path(config["repository"])
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
        baseline = worktree(repository, trees / "baseline", base)
        gate(stage, config["suite"], baseline, base)
        require_unchanged(baseline, base)
        stage = "implementation"
        record["ticket"].update(state="Running", attempt=1)
        save()
        source = worktree(repository, trees / "implementation", base)
        prompt = agents.assignment(stage, ticket, base, base, snapshots, record["gates"][:])
        result = gate(stage, config["agent"], source, base, prompt)
        agents.report(result, prompt)
        submitted, changed = capture(source, base, ticket)
        record["ticket"].update(
            state="Verifying", submitted_revision=submitted, changed_files=changed
        )
        save()
        for name, argv in config["checks"].items():
            if not name.replace("-", "").isalnum():
                raise GateFailure("Check names must contain letters, numbers, or hyphens")
            stage = f"check-{name}"
            gate(stage, argv, source, submitted)
            require_unchanged(source, submitted)
        for role in ("spec", "standards"):
            stage = role
            review_source = worktree(repository, trees / role, submitted)
            prompt = agents.assignment(role, ticket, base, submitted, snapshots, record["gates"][:])
            result = gate(role, config["agent"], review_source, submitted, prompt)
            result["report"] = agents.report(result, prompt)
            require_unchanged(review_source, submitted)
            save()
        stage = "candidate"
        candidate_source = trees / "candidate"
        revision = candidate(repository, candidate_source, base, submitted)
        record["ticket"]["candidate_revision"] = revision
        gate(stage, config["suite"], candidate_source, revision)
        require_unchanged(candidate_source, revision)
        stage = "integration"
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
