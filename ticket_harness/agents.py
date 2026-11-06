"""Fresh scripted process assignments and the initial report contract."""

import json
from pathlib import Path
from typing import Any

from ticket_harness.records import GateFailure

INSTRUCTIONS = {
    "implementation": "Implement only the approved ticket in this worktree. Do not commit. "
    "Return a submitted report; only the harness can declare Done.",
    "spec": "Review the exact revision against the approved ticket/spec and actual check results. "
    "Do not edit source. Return findings classified as blocking or optional.",
    "standards": "Review the exact revision against the supplied project standards and instructions. "
    "Do not edit source. Return findings classified as blocking or optional.",
}


def assignment(
    role: str,
    ticket: str,
    base: str,
    revision: str,
    snapshots: dict[str, Any],
    gates: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "role": role,
        "ticket": ticket,
        "attempt": 1,
        "base_revision": base,
        "revision": revision,
        "instructions": INSTRUCTIONS[role],
        "inputs": {
            name: Path(entry["artifact"]).read_text()
            for name, entry in snapshots.items()
            if name != "configuration"
        },
        "check_results": gates,
        "required_checks": json.loads(Path(snapshots["configuration"]["artifact"]).read_text())[
            "checks"
        ],
        "report_contract": {
            "identity_fields": ["role", "ticket", "attempt", "base_revision", "revision"],
            "result": "submitted" if role == "implementation" else "findings list",
            "fields": [
                "result",
                "summary",
                "changed_files",
                "checks",
                "acceptance_evidence",
                "unresolved_questions",
            ]
            if role == "implementation"
            else ["findings"],
            "finding_fields": [
                "id",
                "classification",
                "location",
                "requirement",
                "consequence",
                "evidence",
                "resolution",
                "human_decision_needed",
            ],
            "instructions": "Emit one JSON object to stdout; diagnostics go to stderr. "
            "Copy assignment identity fields exactly.",
        },
    }


def report(gate: dict[str, Any], expected: dict[str, Any]) -> dict[str, Any]:
    try:
        value = json.loads(Path(gate["stdout"]).read_text())
        if not isinstance(value, dict):
            raise ValueError("report must be an object")
        for key in ("role", "ticket", "attempt", "base_revision", "revision"):
            if value[key] != expected[key]:
                raise ValueError(f"mismatched {key}")
        if expected["role"] == "implementation":
            if value["result"] != "submitted":
                raise ValueError("implementation did not submit")
        else:
            if not isinstance(value["findings"], list):
                raise ValueError("findings must be a list")
            for finding in value["findings"]:
                if finding["classification"] != "optional":
                    raise ValueError("blocking or invalid review finding")
    except (ValueError, KeyError, TypeError) as error:
        gate["passed"] = False
        raise GateFailure(f"{gate['stage']} report rejected: {error}") from error
    return value
