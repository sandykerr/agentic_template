"""Exclusive run ownership and deliberate QA checkpoint persistence.

This is clean checkpoint continuation, not recovery of interrupted execution.
"""

import fcntl
import hashlib
import json
import os
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any
from uuid import uuid4

from ticket_harness import inputs
from ticket_harness.git import git, require_unchanged
from ticket_harness.records import GateFailure, write_json


def digest(path: Path) -> str:
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


def persist(
    output: Path,
    record: dict[str, Any],
    config: dict[str, Any],
    verified: list[tuple[dict[str, Any], Path, str]],
    milestone_index: int,
    evidence: dict[Path, bytes],
    request_bytes: bytes,
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
        "evidence": {str(path): hashlib.sha256(raw).hexdigest() for path, raw in evidence.items()},
        "request_sha256": hashlib.sha256(request_bytes).hexdigest(),
    }
    path = output / "qa-checkpoint.json"
    write_json(path, checkpoint)
    archive = output / "checkpoints"
    archive.mkdir(exist_ok=True)
    (archive / f"{record['checkpoint_id']}.json").write_bytes(path.read_bytes())
    record["checkpoint_sha256"] = digest(path)
    write_json(output / "run.json", record)


def restore(output: Path) -> dict[str, Any]:
    record = json.loads((output / "run.json").read_text(), object_pairs_hook=inputs.unique_object)
    if not isinstance(record, dict) or record.get("outcome") != "stopped_at_qa":
        raise GateFailure(
            "Continue requires a deliberate stopped_at_qa checkpoint; arbitrary interruption recovery is unsupported"
        )
    path = output / "qa-checkpoint.json"
    if digest(path) != record.get("checkpoint_sha256"):
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
        digest(output / "checkpoints" / f"{record['checkpoint_id']}.json")
        != record["checkpoint_sha256"]
    ):
        raise GateFailure("Archived checkpoint identity changed")
    inputs.require_approved(record["inputs"])
    if digest(output / "qa-request.json") != checkpoint["request_sha256"]:
        raise GateFailure("QA request changed")
    for name, expected in checkpoint["evidence"].items():
        if digest(Path(name)) != expected:
            raise GateFailure(f"QA evidence changed: {name}")
    for _, source, revision in checkpoint["verified"]:
        require_unchanged(Path(source), revision)
    validate_request(checkpoint["config"], json.loads((output / "qa-request.json").read_text()))
    return checkpoint


def validate_request(config: dict[str, Any], request: dict[str, Any]) -> None:
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


def evidence_files(output: Path) -> list[Path]:
    return [*(output / "artifacts").iterdir(), *(output / "checkpoints").glob("*.json")]
