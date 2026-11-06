"""Harness-owned records and process artifacts."""

import hashlib
import json
import os
import subprocess
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any


class GateFailure(Exception):
    """A required gate did not pass."""


def write_json(path: Path, value: Any) -> None:
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
    """Bracket external execution; True paths are restored, False paths stay inspectable."""
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
    assignment: dict[str, Any] | None = None,
    restore_on_violation_by_path: dict[Path, bool] | None = None,
    artifact_name: str | None = None,
) -> dict[str, Any]:
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
    }
    payload = None
    if assignment is not None:
        prompt = artifacts / f"{artifact_name}.assignment.json"
        write_json(prompt, assignment)
        gate["assignment"] = str(prompt)
        payload = json.dumps(assignment)
    with (
        protect(restore_on_violation_by_path or {}, artifacts, artifact_name, gate),
        stdout.open("w") as out,
        stderr.open("w") as err,
    ):
        try:
            process = subprocess.run(
                argv,
                cwd=cwd,
                input=payload,
                text=True,
                stdout=out,
                stderr=err,
                env={**os.environ, "TICKET_HARNESS_STAGE": stage},
                check=False,
            )
            gate["exit_code"] = process.returncode
            gate["passed"] = process.returncode == 0
        except OSError as error:
            err.write(str(error))
            gate["exit_code"] = None
    return gate
