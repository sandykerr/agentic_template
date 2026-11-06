"""Harness-owned records and process artifacts."""

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
    return gate
