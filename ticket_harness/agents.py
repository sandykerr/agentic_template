"""Fresh process assignments and complete report validation; no integration authority."""

import json
from math import isfinite
from pathlib import Path
from typing import Any

from ticket_harness.records import GateFailure

INSTRUCTIONS = {
    "implementation": "Implement only the approved ticket in this worktree. Do not commit. "
    "When repair_context is present, repair the current changes using its rejected revisions, "
    "failure diagnostic, and the check_results reports and output artifacts. "
    "Return submitted or human-decision-needed; only the harness can declare Done.",
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
    checks: dict[str, Any],
    attempt: int = 1,
    repair_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "role": role,
        "ticket": ticket,
        "attempt": attempt,
        "repair_context": repair_context,
        "base_revision": base,
        "revision": revision,
        "instructions": INSTRUCTIONS[role],
        "inputs": {
            name: Path(entry["artifact"]).read_text()
            for name, entry in snapshots.items()
            if name != "configuration"
        },
        "check_results": gates,
        "required_checks": checks,
        "report_contract": {
            "identity_fields": ["role", "ticket", "attempt", "base_revision", "revision"],
            "result": ["submitted", "human-decision-needed"]
            if role == "implementation"
            else "findings list",
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
            "field_types": {
                "role": "string: copy assignment role; spec/standards is the review axis",
                "ticket": "string: copy assignment ticket, including leading zeros",
                "attempt": "integer: copy assignment attempt; booleans/floats are invalid",
                "base_revision": "string: copy assignment base_revision",
                "revision": "string: copy assignment revision (starting source for implementation)",
                "result": "string: submitted or human-decision-needed; never Done",
                "summary": "nonempty string",
                "changed_files": "list of nonempty strings; claims only, may be empty",
                "checks": "list of nonempty strings; claims only, may be empty",
                "acceptance_evidence": "list of nonempty strings; nonempty for submitted",
                "unresolved_questions": "list of nonempty strings; nonempty for human-decision-needed",
                "findings": "list of complete finding objects; may be empty",
            },
            "finding_field_types": {
                "id": "nonempty string; stable and unique within this review",
                "classification": "blocking or optional",
                "location": "nonempty string",
                "requirement": "nonempty string",
                "consequence": "nonempty string",
                "evidence": "nonempty string",
                "resolution": "nonempty string",
                "human_decision_needed": "boolean",
            },
            "instructions": "Emit one JSON object to stdout; diagnostics go to stderr. "
            "Copy assignment identity fields exactly, including their JSON types. "
            "Identity fields and fields listed in fields are required. "
            "Every finding requires finding_fields. Maximum object/array nesting: 100 levels. "
            "No duplicate keys or nonfinite "
            "numbers. Extra diagnostic metadata is allowed but has no authority.",
        },
    }


def text_list(value: Any, field: str) -> None:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise ValueError(f"{field} must be a list of nonempty strings")


def implementation(value: dict[str, Any]) -> None:
    if not isinstance(value.get("summary"), str) or not value["summary"].strip():
        raise ValueError("summary must be a nonempty string")
    for field in ("changed_files", "checks", "acceptance_evidence", "unresolved_questions"):
        text_list(value[field], field)
    if value["result"] == "submitted" and not value["acceptance_evidence"]:
        raise ValueError("acceptance_evidence must not be empty for submitted implementations")

    if value["result"] == "human-decision-needed" and not value["unresolved_questions"]:
        raise ValueError("unresolved_questions must describe the required human decision")


def review(value: dict[str, Any]) -> None:
    if not isinstance(value["findings"], list):
        raise ValueError("findings must be a list")
    identifiers = set()
    for index, finding in enumerate(value["findings"]):
        prefix = f"findings[{index}]"
        if not isinstance(finding, dict):
            raise ValueError(f"{prefix} must be an object")
        for field in ("id", "location", "requirement", "consequence", "evidence", "resolution"):
            if not isinstance(finding.get(field), str) or not finding[field].strip():
                raise ValueError(f"{prefix}.{field} must be a nonempty string")
        if finding["id"] in identifiers:
            raise ValueError(f"{prefix}.id must be unique within the review")
        identifiers.add(finding["id"])
        if finding.get("classification") not in ("blocking", "optional"):
            raise ValueError(f"{prefix}.classification must be blocking or optional")
        if type(finding.get("human_decision_needed")) is not bool:
            raise ValueError(f"{prefix}.human_decision_needed must be a boolean")


def report_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate report key {key!r}")
        value[key] = item
    return value


def invalid_constant(value: str) -> None:
    raise ValueError(f"invalid JSON constant {value}")


def finite_number(value: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"nonfinite JSON number {value}")
    return number


def require_bounded_nesting(value: Any) -> None:
    # Leave headroom for the enclosing run record and later assignment check results.
    pending = [(value, 1)]
    while pending:
        item, depth = pending.pop()
        if not isinstance(item, (dict, list)):
            continue
        if depth > 100:
            raise ValueError("report nesting exceeds 100 object/array levels; see stdout")
        children = item.values() if isinstance(item, dict) else item
        pending.extend((child, depth + 1) for child in children)


def report(gate: dict[str, Any], expected: dict[str, Any]) -> dict[str, Any]:
    try:
        value = json.loads(
            Path(gate["stdout"]).read_text(),
            object_pairs_hook=report_object,
            parse_constant=invalid_constant,
            parse_float=finite_number,
        )
        require_bounded_nesting(value)
        gate["report"] = value
        if not isinstance(value, dict):
            raise ValueError("report must be an object")
        for key in ("role", "ticket", "attempt", "base_revision", "revision"):
            if type(value[key]) is not type(expected[key]) or value[key] != expected[key]:
                raise ValueError(f"mismatched {key}")
        if expected["role"] == "implementation":
            if value["result"] not in ("submitted", "human-decision-needed"):
                raise ValueError(
                    "result must be submitted or human-decision-needed; agents cannot declare Done"
                )
            implementation(value)
        else:
            review(value)
    except (ValueError, KeyError, TypeError, RecursionError) as error:
        gate.update(passed=False, report_status="invalid", diagnostic=str(error))
        raise GateFailure(f"{gate['stage']} report rejected: {error}") from error
    gate["report_status"] = "valid"
    return value
