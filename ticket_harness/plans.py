"""Validate fixed approved milestone boundaries before any execution begins."""

from pathlib import Path
from typing import Any

from ticket_harness.inputs import identifier
from ticket_harness.records import GateFailure


def object_fields(value: Any, required: set[str], optional: set[str], field: str) -> None:
    """Require an object with exactly the declared fields; raise GateFailure on mismatch."""
    if not isinstance(value, dict):
        raise GateFailure(f"{field}: expected an object")
    if missing := required - value.keys():
        raise GateFailure(f"{field}: missing required fields {sorted(missing)}")
    if extra := value.keys() - required - optional:
        raise GateFailure(f"{field}: unsupported fields {sorted(extra)}")


def text(value: Any, field: str) -> None:
    """Require nonblank, NUL-free string content; raise field-attributed GateFailure."""
    if not isinstance(value, str) or not value.strip() or "\0" in value:
        raise GateFailure(f"{field}: expected a nonempty string")


def strings(value: Any, field: str) -> None:
    """Validate a nonempty string array without mutation, raising GateFailure on failure."""
    if not isinstance(value, list) or not value:
        raise GateFailure(f"{field}: expected a nonempty array")
    for item in value:
        text(item, field)


def ticket_ids(value: Any, field: str) -> list[str]:
    """Return normalized IDs in declared order, rejecting invalid or duplicate membership."""
    strings(value, field)
    result = [identifier(item) for item in value]
    if len(set(result)) != len(result):
        raise GateFailure(f"{field}: duplicate ticket membership")
    return result


def settings(value: Any, field: str, override: bool = False) -> None:
    """Validate a role profile or reason-bearing override without inserting defaults.

    Raise GateFailure for unsupported fields, invalid targets or empty overrides;
    role default inheritance is applied later by plan validation.
    """
    object_fields(
        value,
        {"reason"} if override else {"model"},
        {"model", "reasoning", "context_limit"} if override else {"reasoning", "context_limit"},
        field,
    )
    for name in ("model", "reason"):
        if name in value:
            text(value[name], f"{field}.{name}")
    if "reasoning" in value and value["reasoning"] not in ("Low", "Medium", "High"):
        raise GateFailure(f"{field}.reasoning: expected Low, Medium, or High")
    if "context_limit" in value and (
        type(value["context_limit"]) is not int or value["context_limit"] <= 0
    ):
        raise GateFailure(f"{field}.context_limit: expected a positive integer target")
    if override and not ({"model", "reasoning", "context_limit"} & value.keys()):
        raise GateFailure(f"{field}: override must change worker settings")


def _milestone_membership(milestones: Any) -> dict[str, int]:
    """Validate QA groups, normalize ticket lists in place, and return their indexes.

    Raises GateFailure at the first malformed group or repeated membership.
    """
    if not isinstance(milestones, list) or not milestones:
        raise GateFailure("plan.milestones: expected a nonempty array")
    membership: dict[str, int] = {}
    milestone_ids = set()
    for index, milestone in enumerate(milestones):
        field = f"plan.milestones[{index}]"
        object_fields(milestone, {"id", "tickets", "qa"}, set(), field)
        text(milestone["id"], f"{field}.id")
        if milestone["id"] in milestone_ids:
            raise GateFailure(f"{field}: duplicate milestone ID")
        milestone_ids.add(milestone["id"])
        milestone["tickets"] = ticket_ids(milestone["tickets"], f"{field}.tickets membership")
        for ticket in milestone["tickets"]:
            if ticket in membership:
                raise GateFailure(f"{field}: duplicate ticket membership {ticket}")
            membership[ticket] = index
        qa = milestone["qa"]
        object_fields(qa, {"setup", "actions", "pass_conditions"}, set(), f"{field}.qa")
        text(qa["setup"], f"{field}.qa.setup")
        for name in ("actions", "pass_conditions"):
            strings(qa[name], f"{field}.qa.{name}")
    return membership


def _validate_dependency_order(membership: dict[str, int], requirements: dict[str, Any]) -> None:
    """Reject transitive prerequisites assigned after their dependent milestone.

    Traversal tolerates cycles here; input preparation separately rejects them.
    """
    for ticket, index in membership.items():
        pending = list(requirements[ticket]["dependencies"])
        visited = set()
        while pending:
            dependency = pending.pop()
            if dependency in visited:
                continue
            visited.add(dependency)
            if dependency in membership and membership[dependency] > index:
                raise GateFailure(
                    f"ticket {ticket}: dependency {dependency} belongs to a later milestone"
                )
            if dependency in requirements:
                pending.extend(requirements[dependency]["dependencies"])


def _worker_settings(
    value: dict[str, Any], membership: dict[str, int], required: list[str]
) -> dict[str, Any]:
    """Normalize role defaults/overrides in place and return per-ticket profiles.

    Validate profiles in declaration order, raising GateFailure on invalid settings.
    """
    roles = value["roles"]
    object_fields(roles, {"worker", "spec", "standards"}, set(), "plan.roles")
    for role, profile in roles.items():
        settings(profile, f"plan.roles.{role}")
        profile.setdefault("reasoning", "Medium" if role == "worker" else "High")
    overrides = value.setdefault("worker_overrides", {})
    if not isinstance(overrides, dict):
        raise GateFailure("plan.worker_overrides: expected an object")
    normalized_overrides = {}
    for ticket, profile in overrides.items():
        ticket = identifier(ticket)
        if ticket not in membership or ticket in normalized_overrides:
            raise GateFailure(
                f"plan.worker_overrides: unknown or duplicate ticket override {ticket}"
            )
        settings(profile, f"plan.worker_overrides.{ticket}", override=True)
        normalized_overrides[ticket] = profile
    value["worker_overrides"] = normalized_overrides
    return {
        ticket: roles["worker"]
        | {k: v for k, v in normalized_overrides.get(ticket, {}).items() if k != "reason"}
        for ticket in required
    }


def validate(
    value: Any, requirements: dict[str, Any], config: dict[str, Any], primary: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Validate a plan against prepared tickets and return it with worker settings.

    Mutates membership, role defaults and overrides in the supplied plan. Checks
    run in contract order and raise GateFailure on the first conflict. Call before
    execution; the returned plan conveys no candidate or human QA acceptance.
    """
    object_fields(
        value,
        {
            "version",
            "approval",
            "development",
            "required_tickets",
            "milestones",
            "final_milestone",
            "final_coverage",
            "roles",
        },
        {"worker_overrides"},
        "plan",
    )
    for field in ("version", "approval", "development", "final_milestone"):
        text(value[field], f"plan.{field}")
    if value["development"] == config["integration"]:
        raise GateFailure("Plan development branch must differ from feature integration")
    required = ticket_ids(value["required_tickets"], "plan.required_tickets")
    if unknown := set(required) - requirements.keys():
        raise GateFailure(f"plan.required_tickets: unknown ticket IDs {sorted(unknown)}")
    milestones = value["milestones"]
    membership = _milestone_membership(milestones)
    if set(membership) != set(required):
        raise GateFailure(
            "plan: milestone membership must assign every required ticket exactly once"
        )
    if value["final_milestone"] != milestones[-1]["id"]:
        raise GateFailure("plan.final_milestone: must identify the last milestone")
    coverage = ticket_ids(value["final_coverage"], "plan.final_coverage")
    if set(coverage) != set(required):
        raise GateFailure("plan.final_coverage: must cover every required ticket cumulatively")
    _validate_dependency_order(membership, requirements)
    workers = _worker_settings(value, membership, required)
    for ticket, index in membership.items():
        metadata = requirements[ticket].get("plan_metadata", {})
        for field, expected in (
            ("Plan version", value["version"]),
            ("Milestone", milestones[index]["id"]),
            ("Worker reasoning", workers[ticket]["reasoning"]),
        ):
            if field in metadata and metadata[field] != expected:
                raise GateFailure(f"ticket {ticket}: {field} metadata conflicts with plan")
    current = milestones[0]["tickets"]
    if primary not in current:
        raise GateFailure("plan: primary ticket must belong to the first milestone")
    if "selected_tickets" in config:
        selected_paths = {
            (Path(config["repository"]) / p).resolve() for p in config["selected_tickets"]
        }
        if selected_paths != {Path(requirements[t]["source"]) for t in current}:
            raise GateFailure("plan: selected_tickets must equal the first milestone membership")
    value["required_tickets"] = required
    value["final_coverage"] = coverage
    return value, workers
