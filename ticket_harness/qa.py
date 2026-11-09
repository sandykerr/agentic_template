"""Milestone human QA, exact approval, and deliberate checkpoint continuation.

This is clean checkpoint continuation, not recovery of interrupted execution.
"""

import fcntl
import hashlib
import json
import os
import stat
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Any
from uuid import uuid4

from ticket_harness import inputs
from ticket_harness.git import (
    candidate,
    git,
    promote_milestone,
    require_clean_milestone_candidate,
    require_unchanged,
)
from ticket_harness.records import GateFailure, write_json

if TYPE_CHECKING:
    from ticket_harness.runner import _Run


def _digest(path: Path) -> str:
    if path.is_symlink() or not path.is_file():
        raise GateFailure(f"Expected regular checkpoint evidence: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


@contextmanager
def ownership(output: Path) -> Iterator[None]:
    # Lock the directory inode: no removable lock-file race or stale PID takeover.
    descriptor = os.open(output, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise GateFailure("Run already has an active owner") from error
        yield
    finally:
        os.close(descriptor)


def reject(output: Path, operation: str, error: Exception) -> None:
    """Keep diagnostics separate from immutable prior run/evidence/checkpoints."""
    directory = output / "rejections"
    directory.mkdir(exist_ok=True)
    write_json(
        directory / f"{uuid4().hex}.json", {"operation": operation, "diagnostic": str(error)}
    )


def stop(output: Path) -> dict[str, Any]:
    active = False
    try:
        with ownership(output):
            pass
    except GateFailure:
        active = True
    if not active:
        raise GateFailure("Stop requires an active QA owner; interruption recovery is unsupported")
    record: dict[str, Any] = json.loads((output / "run.json").read_text())
    if record["outcome"] != "awaiting_human_qa":
        raise GateFailure("Stop is supported only at an active planned QA wait")
    request = json.loads((output / "qa-request.json").read_text())
    write_json(
        output / "stop-request.json",
        {"run_id": record["run_id"], "request_id": request["request_id"]},
    )
    return {"outcome": "stop_requested", "run_id": record["run_id"]}


def _persist(
    output: Path,
    record: dict[str, Any],
    config: dict[str, Any],
    verified: list[tuple[dict[str, Any], Path, str]],
    milestone_index: int,
    evidence: dict[Path, str],
    request_sha256: str,
) -> None:
    record["outcome"] = "stopped_at_qa"
    record["checkpoint_id"] = uuid4().hex
    checkpoint = {
        "version": 1,
        "run_directory": str(output),
        "config": config,
        "record": record,
        "milestone_index": milestone_index,
        "verified": [[item, str(source), revision] for item, source, revision in verified],
        "evidence": {str(path): expected for path, expected in evidence.items()},
        "request_sha256": request_sha256,
    }
    path = output / "qa-checkpoint.json"
    write_json(path, checkpoint)
    archive = output / "checkpoints"
    archive.mkdir(exist_ok=True)
    (archive / f"{record['checkpoint_id']}.json").write_bytes(path.read_bytes())
    record["checkpoint_sha256"] = _digest(path)
    write_json(output / "run.json", record)


def restore(output: Path) -> dict[str, Any]:
    record = json.loads((output / "run.json").read_text(), object_pairs_hook=inputs.unique_object)
    if not isinstance(record, dict) or record.get("outcome") != "stopped_at_qa":
        raise GateFailure(
            "Continue requires a deliberate stopped_at_qa checkpoint; arbitrary interruption recovery is unsupported"
        )
    path = output / "qa-checkpoint.json"
    if _digest(path) != record.get("checkpoint_sha256"):
        raise GateFailure("QA checkpoint identity changed")
    checkpoint: dict[str, Any] = json.loads(
        path.read_text(), object_pairs_hook=inputs.unique_object
    )
    expected_record = dict(record)
    del expected_record["checkpoint_sha256"]
    if (
        checkpoint["version"] != 1
        or checkpoint["run_directory"] != str(output)
        or json.dumps(checkpoint["record"], sort_keys=True)
        != json.dumps(expected_record, sort_keys=True)
    ):
        raise GateFailure("Checkpoint run record or directory changed")
    if (
        _digest(output / "checkpoints" / f"{record['checkpoint_id']}.json")
        != record["checkpoint_sha256"]
    ):
        raise GateFailure("Archived checkpoint identity changed")
    inputs.require_approved(record["inputs"])
    _require_frozen(
        output,
        checkpoint["request_sha256"],
        {Path(name): expected for name, expected in checkpoint["evidence"].items()},
    )
    for _, source, revision in checkpoint["verified"]:
        require_unchanged(Path(source), revision)
    _validate_request(checkpoint["config"], json.loads((output / "qa-request.json").read_text()))
    return checkpoint


def _validate_request(config: dict[str, Any], request: dict[str, Any]) -> None:
    """Validate both refs at clean stop/restoration as well as at promotion."""
    repository = Path(config["repository"])
    for branch_key, revision_key in (
        ("feature_branch", "feature_revision"),
        ("development_branch", "development_revision"),
    ):
        branch = request[branch_key]
        if git(repository, "rev-parse", f"refs/heads/{branch}") != request[revision_key]:
            raise GateFailure(f"Branch {branch} changed externally")
        if (
            f"branch refs/heads/{branch}"
            in git(repository, "worktree", "list", "--porcelain").splitlines()
        ):
            raise GateFailure(f"Branch {branch} must not be checked out")


def _evidence_files(output: Path) -> list[Path]:
    return [*(output / "artifacts").iterdir(), *(output / "checkpoints").glob("*.json")]


def _require_frozen(
    output: Path, request_sha256: str, evidence: dict[Path, str], *, before_stop: bool = False
) -> None:
    """Apply the same request/evidence rules at stop, restore, and promotion."""

    def unchanged(path: Path, expected: str) -> bool:
        try:
            return _digest(path) == expected
        except (GateFailure, OSError):
            return False

    if not unchanged(output / "qa-request.json", request_sha256):
        suffix = " before stop" if before_stop else "; renewed candidate acceptance required"
        raise GateFailure(f"QA request changed{suffix}")
    for path, expected in evidence.items():
        if not unchanged(path, expected):
            message = (
                f"QA evidence changed before stop: {path}"
                if before_stop
                else (f"QA evidence changed: {path}; renewed acceptance required")
            )
            raise GateFailure(message)


def review(execution: "_Run", checkpoint: dict[str, Any] | None) -> bool:
    """Prepare and assess one milestone; return True only for a deliberate QA stop."""
    record, config = execution.record, execution.config
    output, artifacts, trees = execution.output, execution.artifacts, execution.trees
    repository = Path(config["repository"])
    integration, development = config["integration"], config["plan"]["development"]
    previous = record["integration_revision"]
    snapshots = record["inputs"]
    milestone_index = execution.milestone_index
    # Milestone preparation has no ticket repair budget and never changes refs.
    execution.stage = "milestone-candidate"
    milestone = record["milestone"]
    if checkpoint is None:
        milestone.update(state="preparing", feature_revision=previous)
        development_base = git(repository, "rev-parse", f"refs/heads/{development}")
        record.setdefault("starting_development_revision", record["development_revision"])
        record["development_revision"] = development_base
        milestone["development_revision"] = development_base
        execution.save()
        candidate_source = trees / execution.artifact_name("milestone-candidate")
        try:
            with execution.git_operation("milestone-candidate-merge"):
                revision = candidate(repository, candidate_source, development_base, previous)
                milestone["candidate_revision"] = revision
        except GateFailure as error:
            raise GateFailure(
                f"Milestone merge failed; renewed checks and reviews required: {error}"
            ) from error
        with execution.git_operation("milestone-candidate-validation"):
            require_clean_milestone_candidate(
                repository, candidate_source, revision, development_base, previous
            )
        execution.stage = "milestone-regression"
        regression = execution.check(execution.stage, config["suite"], candidate_source, revision)
        execution.stage = "milestone-readiness"
        inputs.require_approved(snapshots)
        execution.validate_sources()
        for branch, expected in (
            (integration, previous),
            (development, development_base),
        ):
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
            "human_checks": config["plan"]["milestones"][milestone_index]["qa"],
            "regression_evidence": [regression],
        }
        request_path = output / "qa-request.json"
        write_json(request_path, request)
        record["qa_request"] = str(request_path)
        record["outcome"] = "awaiting_human_qa"
        milestone["state"] = "awaiting_human_qa"
        write_json(artifacts / execution.artifact_name("qa-request.json"), request)
        record["qa_decision"] = str(output / "qa-decision.json")
        record["qa_decision_status"] = "missing"
        # Freeze content identities while the human assesses this request.
        evidence = {path: _digest(path) for path in _evidence_files(output)}
        request_sha256 = _digest(request_path)
        execution.save()
    else:
        request_path = output / "qa-request.json"
        request_sha256 = _digest(request_path)
        request = json.loads(request_path.read_bytes())
        candidate_source = Path(request["candidate_worktree"])
        revision = request["candidate_revision"]
        development_base = request["development_revision"]
        evidence = {Path(name): expected for name, expected in checkpoint["evidence"].items()}
        archive_path = output / "checkpoints" / f"{record['checkpoint_id']}.json"
        evidence[archive_path] = _digest(archive_path)
        checkpoint = None
        record["outcome"] = "awaiting_human_qa"
        execution.save()
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
                execution.validate_sources()
                _require_frozen(output, request_sha256, evidence, before_stop=True)
                _validate_request(config, request)
                stop_path.unlink()
                # Include observations made after the request was prepared.
                frozen = {path: _digest(path) for path in _evidence_files(output)}
                _persist(
                    output,
                    record,
                    config,
                    execution.verified,
                    milestone_index,
                    frozen,
                    request_sha256,
                )
                return True
            stop_path.unlink()
        try:
            decision_path = output / "qa-decision.json"
            if decision_path.is_symlink() or not stat.S_ISREG(decision_path.stat().st_mode):
                raise OSError("QA decision must be a regular file")
            raw = decision_path.read_bytes()
        except OSError as error:
            status = "missing" if isinstance(error, FileNotFoundError) else "unreadable"
            if record["qa_decision_status"] != status:
                record["qa_decision_status"] = status
                record["qa_decision_diagnostic"] = str(error)
                execution.save()
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
            artifacts / f"qa-decision-{len(record.setdefault('qa_observations', []))}.json"
        )
        observation_path.write_bytes(raw)
        evidence[observation_path] = hashlib.sha256(raw).hexdigest()
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
                d["request_id"] == request["request_id"] for d in record.get("qa_decisions", [])
            ):
                raise GateFailure("Decision request was already consumed")
        except (ValueError, GateFailure) as error:
            decision_observation["diagnostic"] = str(error)
            record["qa_decision_status"] = "rejected"
            execution.save()
            continue
        execution.stage = "milestone-promotion"
        inputs.require_approved(snapshots)
        execution.validate_sources()
        _require_frozen(output, request_sha256, evidence)
        # The ref transaction validates both expected tips and advances both together.
        promote_milestone(
            repository, integration, development, revision, previous, development_base
        )
        decision_observation["status"] = "consumed"
        record.setdefault("qa_decisions", []).append(dict(decision_observation))
        record["qa_decision_status"] = "consumed"
        milestone.update(state="promoted", promoted_revision=revision)
        record.setdefault("milestones", []).append(dict(milestone))
        record["integration_revision"] = revision
        record["development_revision"] = revision
        execution.save()
        break
    return False
