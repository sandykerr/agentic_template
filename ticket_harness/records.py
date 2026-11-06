"""Harness-owned records and process artifacts."""

import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Any


class GateFailure(Exception):
    """A required gate did not pass."""


def write_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def execute(
    argv: list[str],
    cwd: Path,
    artifacts: Path,
    stage: str,
    revision: str,
    assignment: dict[str, Any] | None = None,
    protected: dict[Path, bool] | None = None,
) -> dict[str, Any]:
    stdout = artifacts / f"{stage}.stdout"
    stderr = artifacts / f"{stage}.stderr"
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
        prompt = artifacts / f"{stage}.assignment.json"
        write_json(prompt, assignment)
        gate["assignment"] = str(prompt)
        payload = json.dumps(assignment)
    protected = dict(protected or {})
    # Include the prompt just written, and evidence from every earlier stage.
    protected.update({path: True for path in artifacts.iterdir() if path not in (stdout, stderr)})
    originals = {path: path.read_bytes() if path.exists() else None for path in protected}
    with stdout.open("w") as out, stderr.open("w") as err:
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
    violations: list[dict[str, Any]] = []
    for path, original in originals.items():
        try:
            observed = path.read_bytes() if path.exists() else None
        except OSError:
            observed = None
        if observed == original and not path.is_symlink():
            continue
        evidence = artifacts / f"{stage}.integrity-{len(violations)}"
        if observed is not None:
            evidence.write_bytes(observed)
        violations.append(
            {
                "path": str(path),
                "expected_sha256": hashlib.sha256(original).hexdigest()
                if original is not None
                else None,
                "observed_sha256": hashlib.sha256(observed).hexdigest()
                if observed is not None
                else None,
                "artifact": str(evidence) if observed is not None else None,
            }
        )
        if protected[path] and original is not None:
            # Keep approved snapshots and prior evidence usable; retain rejected bytes above.
            if path.is_symlink():
                path.unlink()
            path.write_bytes(original)
    if violations:
        gate.update(
            passed=False,
            integrity=violations,
            diagnostic="Integrity violation: protected files changed",
        )
    return gate
