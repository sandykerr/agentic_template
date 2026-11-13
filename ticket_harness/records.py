"""Harness-owned records and process artifacts."""

import hashlib
import json
import os
import signal
import subprocess
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any


class GateFailure(Exception):
    """A required gate did not pass."""


class NonRepairableFailure(GateFailure):
    """A failure that another implementation attempt cannot resolve."""


def write_json(path: Path, value: Any) -> None:
    """Replace a JSON record via a sibling temporary file; propagate filesystem errors."""
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


@contextmanager
def protect(
    restore_on_violation_by_path: dict[Path, bool],
    artifacts: Path,
    stage: str,
    evidence: dict[str, Any],
) -> Iterator[None]:
    """Snapshot protected paths and existing artifacts around external execution.

    On every exit, preserve observed violations and mark evidence failed. Restore
    prior bytes for True paths (including existing artifacts); False paths remain
    inspectable. Restoration errors propagate rather than claiming intact evidence.
    """
    protected = dict(restore_on_violation_by_path)
    protected.update({path: True for path in artifacts.iterdir()})
    originals = {path: path.read_bytes() if path.exists() else None for path in protected}
    try:
        yield
    finally:
        violations: list[dict[str, Any]] = []
        for path, original in originals.items():
            try:
                observed = path.read_bytes() if path.exists() else None
            except OSError:
                observed = None
            if observed == original and not path.is_symlink():
                continue
            rejected = artifacts / f"{stage}.integrity-{len(violations)}"
            moved_directory = protected[path] and path.is_dir() and not path.is_symlink()
            if moved_directory:
                path.replace(rejected)
            if observed is not None:
                rejected.write_bytes(observed)
            violations.append(
                {
                    "path": str(path),
                    "expected_sha256": hashlib.sha256(original).hexdigest()
                    if original is not None
                    else None,
                    "observed_sha256": hashlib.sha256(observed).hexdigest()
                    if observed is not None
                    else None,
                    "artifact": str(rejected) if observed is not None or moved_directory else None,
                }
            )
            if protected[path] and original is not None:
                # Keep approved snapshots and prior evidence usable after rejection.
                if path.is_symlink():
                    path.unlink()
                path.write_bytes(original)
        if violations:
            evidence.update(
                passed=False,
                integrity=violations,
                diagnostic="Integrity violation: protected files changed",
            )


def execute(
    argv: list[str],
    cwd: Path,
    artifacts: Path,
    stage: str,
    revision: str,
    timeout_seconds: int | float,
    assignment: dict[str, Any] | None = None,
    restore_on_violation_by_path: dict[Path, bool] | None = None,
    artifact_name: str | None = None,
) -> dict[str, Any]:
    """Run one command in a new session and return its gate with captured artifacts.

    Assignments are persisted and sent as JSON stdin. Deadlines kill the process
    group; final cleanup also removes background children after successful exits.
    Spawn/communication OS errors become failed evidence, and integrity checks run
    after process cleanup before the gate is returned.
    """
    artifact_name = artifact_name or stage
    stdout = artifacts / f"{artifact_name}.stdout"
    stderr = artifacts / f"{artifact_name}.stderr"
    gate: dict[str, Any] = {
        "stage": stage,
        "revision": revision,
        "argv": argv,
        "cwd": str(cwd),
        "stdout": str(stdout),
        "stderr": str(stderr),
        "passed": False,
        "timeout_seconds": timeout_seconds,
        "timed_out": False,
    }
    payload = None
    if assignment is not None:
        prompt = artifacts / f"{artifact_name}.assignment.json"
        write_json(prompt, assignment)
        gate["assignment"] = str(prompt)
        payload = json.dumps(assignment)
    with (
        protect(restore_on_violation_by_path or {}, artifacts, artifact_name, gate),
        stdout.open("wb") as out,
        stderr.open("wb") as err,
    ):
        process = None
        try:
            process = subprocess.Popen(
                argv,
                cwd=cwd,
                stdin=subprocess.PIPE if payload is not None else subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env={**os.environ, "TICKET_HARNESS_STAGE": stage},
                start_new_session=True,
            )
            captured_out, captured_err = _communicate(
                process, payload, timeout_seconds, stage, gate
            )
            out.write(captured_out)
            err.write(captured_err)
            gate["exit_code"] = process.returncode
            gate["passed"] = process.returncode == 0 and not gate["timed_out"]
        except OSError as error:
            err.write(str(error).encode())
            gate["exit_code"] = None
            gate["execution_error"] = str(error)
        finally:
            if process is not None:
                _finish_process(process, gate)
    return gate


def _communicate(
    process: subprocess.Popen[bytes],
    payload: str | None,
    timeout_seconds: int | float,
    stage: str,
    gate: dict[str, Any],
) -> tuple[bytes, bytes]:
    """Capture output by the deadline, killing the group and bounding its final drain.

    Timeout and cleanup failures update the shared gate; partial output is retained.
    """
    try:
        captured_out, captured_err = process.communicate(
            payload.encode() if payload is not None else None, timeout=timeout_seconds
        )
    except subprocess.TimeoutExpired:
        gate.update(
            timed_out=True,
            diagnostic=f"{stage} timed out after {timeout_seconds} seconds",
        )
        stop_group(process, gate)
        try:
            # A dead leader can leave children holding the output pipes open.
            # Bound the final drain too; never wait indefinitely for EOF.
            captured_out, captured_err = process.communicate(timeout=5)
        except subprocess.TimeoutExpired as error:
            captured_out, captured_err = error.output or b"", error.stderr or b""
            gate["execution_error"] = "process cleanup/output drain did not finish"
    return captured_out, captured_err


def _finish_process(process: subprocess.Popen[bytes], gate: dict[str, Any]) -> None:
    """Stop remaining group members, bound leader reaping, and close every pipe.

    Called from execution's finally block even after normal completion; records the
    final exit code and any failure to reap after SIGKILL.
    """
    # Also stop background children of an otherwise completed command.
    stop_group(process, gate)
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        gate["execution_error"] = "process did not stop after SIGKILL"
    for stream in (process.stdin, process.stdout, process.stderr):
        if stream is not None:
            stream.close()
    gate["exit_code"] = process.returncode


def stop_group(process: subprocess.Popen[bytes], gate: dict[str, Any]) -> None:
    """Kill the entire assignment's POSIX process group, including an exited leader's children."""
    cleanup = gate.setdefault(
        "cleanup", {"process_group": process.pid, "signal": "SIGKILL", "sent": False}
    )
    try:
        os.killpg(process.pid, signal.SIGKILL)
        cleanup["sent"] = True
    except ProcessLookupError:
        pass
