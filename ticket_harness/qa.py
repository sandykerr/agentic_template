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
from contextlib import AbstractContextManager, contextmanager
from enum import Enum
from pathlib import Path
from typing import Any, Protocol
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


class ReviewOutcome(Enum):
    """The two successful milestone-review outcomes understood by the run."""

    STOPPED = "stopped"
    PROMOTED = "promoted"


class ReviewVerification(Protocol):
    """Run-owned operations available to review; no scheduling or gate registry access."""

    stage: str

    def save(self) -> None: ...

    def git_operation(self, name: str) -> AbstractContextManager[None]: ...

    def check(self, stage: str, argv: list[str], source: Path, revision: str) -> dict[str, Any]: ...

    def validate_sources(self) -> None: ...

    def export_checks(self) -> list[list[Any]]: ...


class MilestoneReview:
    """Own one exact candidate, request, evidence and decision through stop or promotion.

    The durable record is shared only for existing JSON persistence. All review
    mutations stay here; verification and source invalidation remain run-owned.
    """

    def __init__(
        self,
        record: dict[str, Any],
        config: dict[str, Any],
        output: Path,
        milestone_index: int,
        candidate_source: Path,
        request_artifact: Path,
        verification: ReviewVerification,
    ) -> None:
        self._record = record
        self._config = config
        self._output = output
        self._milestone_index = milestone_index
        self._candidate_source = candidate_source
        self._request_artifact = request_artifact
        self._verification = verification
        self._repository = Path(config["repository"])
        self._artifacts = output / "artifacts"
        self._integration = config["integration"]
        self._development = config["plan"]["development"]
        self._previous = record["integration_revision"]
        self._snapshots = record["inputs"]
        self._milestone = record["milestone"]
        self._request: dict[str, Any] = {}
        self._request_sha256 = ""
        self._evidence: dict[Path, str] = {}
        self._observed_decision: bytes | None = None

    def execute(self, checkpoint: dict[str, Any] | None) -> ReviewOutcome:
        self._prepare(checkpoint)
        return self._await_decision()

    def _prepare(self, checkpoint: dict[str, Any] | None) -> None:
        # Milestone preparation has no ticket repair budget and never changes refs.
        self._verification.stage = "milestone-candidate"
        if checkpoint is None:
            self._milestone.update(state="preparing", feature_revision=self._previous)
            self._development_base = git(
                self._repository, "rev-parse", f"refs/heads/{self._development}"
            )
            self._record.setdefault(
                "starting_development_revision", self._record["development_revision"]
            )
            self._record["development_revision"] = self._development_base
            self._milestone["development_revision"] = self._development_base
            self._verification.save()
            try:
                with self._verification.git_operation("milestone-candidate-merge"):
                    self._revision = candidate(
                        self._repository,
                        self._candidate_source,
                        self._development_base,
                        self._previous,
                    )
                    self._milestone["candidate_revision"] = self._revision
            except GateFailure as error:
                raise GateFailure(
                    f"Milestone merge failed; renewed checks and reviews required: {error}"
                ) from error
            with self._verification.git_operation("milestone-candidate-validation"):
                require_clean_milestone_candidate(
                    self._repository,
                    self._candidate_source,
                    self._revision,
                    self._development_base,
                    self._previous,
                )
            self._verification.stage = "milestone-regression"
            regression = self._verification.check(
                self._verification.stage,
                self._config["suite"],
                self._candidate_source,
                self._revision,
            )
            self._verification.stage = "milestone-readiness"
            inputs.require_approved(self._snapshots)
            self._verification.validate_sources()
            for branch, expected in (
                (self._integration, self._previous),
                (self._development, self._development_base),
            ):
                if git(self._repository, "rev-parse", f"refs/heads/{branch}") != expected:
                    raise GateFailure(f"Branch {branch} changed externally; candidate invalidated")
            self._request = {
                "request_id": uuid4().hex,
                "run_id": self._record["run_id"],
                "run_directory": str(self._output),
                "plan_version": self._config["plan"]["version"],
                "plan_approval": self._config["plan"]["approval"],
                "plan_input": self._snapshots["plan"],
                "milestone": self._milestone["id"],
                "feature_branch": self._integration,
                "feature_revision": self._previous,
                "development_branch": self._development,
                "development_revision": self._development_base,
                "candidate_revision": self._revision,
                "candidate_worktree": str(self._candidate_source),
                "human_checks": self._config["plan"]["milestones"][self._milestone_index]["qa"],
                "regression_evidence": [regression],
            }
            request_path = self._output / "qa-request.json"
            write_json(request_path, self._request)
            self._record["qa_request"] = str(request_path)
            self._record["outcome"] = "awaiting_human_qa"
            self._milestone["state"] = "awaiting_human_qa"
            write_json(self._request_artifact, self._request)
            self._record["qa_decision"] = str(self._output / "qa-decision.json")
            self._record["qa_decision_status"] = "missing"
            # Freeze content identities while the human assesses this request.
            self._evidence = {path: _digest(path) for path in _evidence_files(self._output)}
            self._request_sha256 = _digest(request_path)
            self._verification.save()
        else:
            request_path = self._output / "qa-request.json"
            self._request_sha256 = _digest(request_path)
            self._request = json.loads(request_path.read_bytes())
            self._candidate_source = Path(self._request["candidate_worktree"])
            self._revision = self._request["candidate_revision"]
            self._development_base = self._request["development_revision"]
            self._evidence = {
                Path(name): expected for name, expected in checkpoint["evidence"].items()
            }
            archive_path = self._output / "checkpoints" / f"{self._record['checkpoint_id']}.json"
            self._evidence[archive_path] = _digest(archive_path)
            self._record["outcome"] = "awaiting_human_qa"
            self._verification.save()

    def _await_decision(self) -> ReviewOutcome:
        while True:
            if self._stop_if_requested():
                return ReviewOutcome.STOPPED
            raw = self._read_decision()
            if raw is None or raw == self._observed_decision:
                time.sleep(0.1)
                continue
            self._observed_decision = raw
            if self._consider_decision(raw):
                return ReviewOutcome.PROMOTED

    def _stop_if_requested(self) -> bool:
        stop_path = self._output / "stop-request.json"
        if stop_path.exists():
            stopping = json.loads(stop_path.read_text())
            if stopping == {
                "run_id": self._record["run_id"],
                "request_id": self._request["request_id"],
            }:
                self._require_current(before_stop=True)
                stop_path.unlink()
                # Include observations made after the request was prepared.
                self._evidence = {path: _digest(path) for path in _evidence_files(self._output)}
                self._persist()
                return True
            stop_path.unlink()
        return False

    def _read_decision(self) -> bytes | None:
        try:
            decision_path = self._output / "qa-decision.json"
            if decision_path.is_symlink() or not stat.S_ISREG(decision_path.stat().st_mode):
                raise OSError("QA decision must be a regular file")
            raw = decision_path.read_bytes()
        except OSError as error:
            status = "missing" if isinstance(error, FileNotFoundError) else "unreadable"
            if self._record["qa_decision_status"] != status:
                self._record["qa_decision_status"] = status
                self._record["qa_decision_diagnostic"] = str(error)
                self._verification.save()
            self._observed_decision = None
            return None
        return raw

    def _consider_decision(self, raw: bytes) -> bool:
        decision_observation: dict[str, Any] = {
            "sha256": hashlib.sha256(raw).hexdigest(),
            "milestone": self._milestone["id"],
            "request_id": self._request["request_id"],
            "status": "rejected",
        }
        observation_path = (
            self._artifacts
            / f"qa-decision-{len(self._record.setdefault('qa_observations', []))}.json"
        )
        observation_path.write_bytes(raw)
        self._evidence[observation_path] = hashlib.sha256(raw).hexdigest()
        decision_observation["artifact"] = str(observation_path)
        self._record["qa_observations"].append(decision_observation)
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
                self._request, sort_keys=True
            ):
                raise GateFailure("Decision does not match the current request")
            if any(
                d["request_id"] == self._request["request_id"]
                for d in self._record.get("qa_decisions", [])
            ):
                raise GateFailure("Decision request was already consumed")
        except (ValueError, GateFailure) as error:
            decision_observation["diagnostic"] = str(error)
            self._record["qa_decision_status"] = "rejected"
            self._verification.save()
            return False
        self._verification.stage = "milestone-promotion"
        self._require_current()
        # The ref transaction validates both expected tips and advances both together.
        promote_milestone(
            self._repository,
            self._integration,
            self._development,
            self._revision,
            self._previous,
            self._development_base,
        )
        decision_observation["status"] = "consumed"
        self._record.setdefault("qa_decisions", []).append(dict(decision_observation))
        self._record["qa_decision_status"] = "consumed"
        self._milestone.update(state="promoted", promoted_revision=self._revision)
        self._record.setdefault("milestones", []).append(dict(self._milestone))
        self._record["integration_revision"] = self._revision
        self._record["development_revision"] = self._revision
        self._verification.save()
        return True

    def _require_current(self, *, before_stop: bool = False) -> None:
        inputs.require_approved(self._snapshots)
        self._verification.validate_sources()
        _require_frozen(self._output, self._request_sha256, self._evidence, before_stop=before_stop)
        if before_stop:
            _validate_request(self._config, self._request)

    def _persist(self) -> None:
        self._record["outcome"] = "stopped_at_qa"
        self._record["checkpoint_id"] = uuid4().hex
        checkpoint = {
            "version": 1,
            "run_directory": str(self._output),
            "config": self._config,
            "record": self._record,
            "milestone_index": self._milestone_index,
            "verified": self._verification.export_checks(),
            "evidence": {str(path): expected for path, expected in self._evidence.items()},
            "request_sha256": self._request_sha256,
        }
        path = self._output / "qa-checkpoint.json"
        write_json(path, checkpoint)
        archive = self._output / "checkpoints"
        archive.mkdir(exist_ok=True)
        (archive / f"{self._record['checkpoint_id']}.json").write_bytes(path.read_bytes())
        self._record["checkpoint_sha256"] = _digest(path)
        write_json(self._output / "run.json", self._record)

    @staticmethod
    def restore_checkpoint(output: Path) -> dict[str, Any]:
        record = json.loads(
            (output / "run.json").read_text(), object_pairs_hook=inputs.unique_object
        )
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
        _validate_request(
            checkpoint["config"], json.loads((output / "qa-request.json").read_text())
        )
        return checkpoint
