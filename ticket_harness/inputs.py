"""Normalize approved requirements and reject ineligible inputs before execution."""

import hashlib
import json
import os.path
import re
import shutil
from dataclasses import dataclass
from math import isfinite
from pathlib import Path
from typing import Any

from ticket_harness.git import git
from ticket_harness.records import GateFailure

DEFAULT_TIMEOUTS: dict[str, int | float] = {
    "implementation": 1800,
    "repair": 1800,
    "spec": 900,
    "standards": 900,
    "checks": 300,
    "baseline": 1800,
    "candidate": 1800,
}
# Keep each value within the platform's bounded pipe-wait range (one week).
MAX_TIMEOUT_SECONDS = 604800


def timeouts(value: Any) -> dict[str, int | float]:
    if not isinstance(value, dict):
        raise GateFailure("configuration.timeouts: expected an object of stage seconds")
    for name, seconds in value.items():
        if name not in DEFAULT_TIMEOUTS:
            raise GateFailure(f"configuration.timeouts.{name}: unsupported timeout stage")
        try:
            valid = (
                type(seconds) in (int, float)
                and isfinite(seconds)
                and 0 < seconds <= MAX_TIMEOUT_SECONDS
            )
        except OverflowError:
            valid = False
        if not valid:
            raise GateFailure(
                f"configuration.timeouts.{name}: expected positive finite seconds <= "
                f"{MAX_TIMEOUT_SECONDS}"
            )
    return DEFAULT_TIMEOUTS | value


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise GateFailure(f"duplicate JSON key {key!r}; keep one authoritative value")
        value[key] = item
    return value


def identifier(value: str) -> str:
    if not re.fullmatch(r"[0-9]+", value) or int(value) < 1:
        raise GateFailure(f"Invalid ticket ID {value!r}; use a positive numeric identifier")
    return str(int(value)).zfill(2)


def command(value: Any, field: str, repository: Path, base: str) -> None:
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(arg, str) or not arg.strip() or "\0" in arg for arg in value)
    ):
        raise GateFailure(f"{field}: expected a nonempty argument array of nonempty strings")
    if "/" in value[0] and not Path(value[0]).is_absolute():
        if ".." in Path(value[0]).parts or value[0].endswith(("/", "/.")):
            raise GateFailure(
                f"{field}: relative executable path must not contain '..' or end with '/' or '/.'"
            )
        relative = os.path.normpath(value[0])
        entry = git(repository, "--literal-pathspecs", "ls-tree", "-z", base, "--", relative)
        if not entry.startswith("100755 blob "):
            raise GateFailure(
                f"{field}: relative executable unavailable or not executable at base: {value[0]!r}"
            )
    else:
        resolved = shutil.which(value[0])
        if not resolved:
            raise GateFailure(f"{field}: executable unavailable: {value[0]!r}")
        if not Path(resolved).is_absolute():
            raise GateFailure(
                f"{field}: executable resolved through a relative PATH entry; use an absolute path"
            )


def configuration(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise GateFailure("configuration: expected a JSON object")
    required = {
        "repository",
        "base",
        "integration",
        "spec",
        "ticket",
        "standards",
        "agent",
        "suite",
        "checks",
    }
    for field in sorted(required):
        if field not in value:
            raise GateFailure(f"configuration: missing required field {field!r}")
    for field in sorted(
        value.keys()
        - required
        - {"tickets", "selected_tickets", "completed_runs", "max_repairs", "timeouts", "plan"}
    ):
        raise GateFailure(f"configuration: unsupported field {field!r}; see the input contract")
    value["timeouts"] = timeouts(value.get("timeouts", {}))
    allowance = value.setdefault("max_repairs", 2)
    if type(allowance) is not int or allowance < 0:
        raise GateFailure("configuration.max_repairs: expected a nonnegative integer")
    for field in ("repository", "base", "integration", "spec", "ticket", "plan"):
        if field not in value:
            continue
        if not isinstance(value[field], str) or not value[field].strip() or "\0" in value[field]:
            raise GateFailure(f"configuration.{field}: expected a nonempty string")
    for field in ("standards", "tickets", "selected_tickets", "completed_runs"):
        if field not in value:
            continue
        if not isinstance(value[field], list) or any(
            not isinstance(path, str) or not path.strip() or "\0" in path for path in value[field]
        ):
            raise GateFailure(f"configuration.{field}: expected an array of nonempty paths")
    if not isinstance(value["checks"], dict) or not value["checks"]:
        raise GateFailure("configuration.checks: expected a nonempty mapping of names to commands")
    return value


@dataclass(frozen=True)
class Dependency:
    id: str
    title: str | None
    path: Path | None


def requirement_text(text: str) -> str:
    """Ignore fenced examples and the tracker's appended comment history."""
    lines = []
    fence = ""
    length = 0
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (
                marker
                and marker[1][0] == fence
                and len(marker[1]) >= length
                and not marker[2].strip()
            ):
                fence = ""
        elif marker:
            fence, length = marker[1][0], len(marker[1])
        elif line.strip() == "## Comments":
            break
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


def normalize_ticket(
    text: str, path: Path, checks: dict[str, Any]
) -> tuple[dict[str, Any], list[Dependency]]:
    if text.lstrip().startswith("---\n"):
        raise GateFailure(
            f"{path}: YAML front matter is unsupported; use the Markdown metadata contract"
        )
    text = requirement_text(text)
    header = re.split(r"^## ", text, maxsplit=1, flags=re.M)[0]
    if len(re.findall(r"^# ", text, re.M)) != 1:
        raise GateFailure(f"{path}: expected exactly one ticket heading '# NN: Title'")
    title = re.search(r"^# ([0-9]+): (\S.*?)\s*$", header, re.M)
    if not title:
        raise GateFailure(f"{path}: expected '# NN: Title'")
    ticket_id = identifier(title[1])
    filename = re.match(r"([0-9]+)-", path.name)
    if filename and identifier(filename[1]) != ticket_id:
        raise GateFailure(
            f"{path}: filename ID {identifier(filename[1])} conflicts with heading ID {ticket_id}"
        )
    metadata: dict[str, str] = {}
    for key, value in re.findall(r"^(?:\*\*)?([A-Za-z ]+):(?:\*\*)?[ \t]*([^\n]*)", header, re.M):
        if key in metadata:
            raise GateFailure(f"{path}: duplicate {key} metadata; keep one authoritative value")
        metadata[key] = value.strip()
    for key, expected in (("ID", ticket_id), ("Title", title[2])):
        if key in metadata:
            actual = identifier(metadata[key]) if key == "ID" else metadata[key]
            if actual != expected:
                raise GateFailure(f"{path}: {key} metadata conflicts with heading")
    readiness = metadata.get("Status", "")
    if readiness not in {
        "needs-triage",
        "needs-info",
        "ready-for-agent",
        "ready-for-human",
        "wontfix",
    }:
        raise GateFailure(f"{path}: Status must be a triage readiness label; found {readiness!r}")
    declaration = metadata.get("Blocked by", "")
    dependencies = []
    dependency_references = []
    if not re.fullmatch(r"None(?: \(can start immediately\))?\.?", declaration):
        for reference in declaration.split(","):
            reference = reference.strip()
            link = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", reference)
            label = link[1] if link else reference
            match = re.fullmatch(r"([0-9]+)(?:: (\S.*))?", label)
            if not match:
                raise GateFailure(f"{path}: invalid Blocked by reference {reference!r}")
            dependency_id = identifier(match[1])
            dependencies.append(dependency_id)
            dependency_references.append(
                Dependency(
                    dependency_id,
                    match[2],
                    (path.parent / link[2]).resolve() if link else None,
                )
            )
    if len(re.findall(r"^## Acceptance criteria[ \t]*$", text, re.M)) > 1:
        raise GateFailure(f"{path}: duplicate Acceptance criteria section")
    acceptance = re.search(r"^## Acceptance criteria[ \t]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if acceptance and re.search(r"^[-*] \[[ xX]\][ \t]*$", acceptance[1], re.M):
        raise GateFailure(f"{path}: empty acceptance requirement; supply concrete content")
    requirements = (
        re.findall(r"^[-*] \[[ xX]\] (\S.*?)\s*$", acceptance[1], re.M) if acceptance else []
    )
    if not requirements:
        raise GateFailure(f"{path}: Acceptance criteria needs nonempty checklist items")
    references = (
        [name.strip() for name in metadata["Checks"].split(",")]
        if "Checks" in metadata
        else list(checks)
    )
    for name in references:
        if name not in checks:
            raise GateFailure(f"{path}: unknown check reference {name!r}; configure it in checks")
    if len(set(references)) != len(references):
        raise GateFailure(f"{path}: duplicate check reference; list each check once")
    plan_metadata = {
        key: metadata[key]
        for key in ("Plan version", "Milestone", "Worker reasoning")
        if key in metadata
    }
    return {
        "id": ticket_id,
        "title": title[2],
        "readiness": readiness,
        "dependencies": dependencies,
        "acceptance": requirements,
        "checks": references,
        "source": str(path),
        **({"plan_metadata": plan_metadata} if plan_metadata else {}),
    }, dependency_references


def validate_graph(requirements: dict[str, Any], references: dict[str, list[Dependency]]) -> None:
    for item in requirements.values():
        for dependency in item["dependencies"]:
            if dependency not in requirements:
                raise GateFailure(
                    f"ticket {item['id']}: missing dependency {dependency} in tickets bundle"
                )
        for reference in references[item["id"]]:
            target = requirements[reference.id]
            if reference.title and reference.title != target["title"]:
                raise GateFailure(
                    f"ticket {item['id']}: dependency {reference.id} title conflicts with {target['title']!r}"
                )
            if reference.path and reference.path != Path(target["source"]):
                raise GateFailure(
                    f"ticket {item['id']}: dependency {reference.id} link conflicts with {target['source']}"
                )
    finished: set[str] = set()
    for ticket_id in requirements:
        path: list[str] = []
        stack = [(ticket_id, False)]
        while stack:
            current, exiting = stack.pop()
            if exiting:
                path.pop()
                finished.add(current)
            elif current in path:
                cycle = path[path.index(current) :] + [current]
                raise GateFailure(f"dependency cycle: {' -> '.join(cycle)}")
            elif current not in finished:
                path.append(current)
                stack.append((current, True))
                stack.extend(
                    (dependency, False)
                    for dependency in reversed(requirements[current]["dependencies"])
                )


def completed_tickets(
    snapshots: dict[str, Any], requirements: dict[str, Any], repository: Path, base: str
) -> set[str]:
    completed: set[str] = set()
    for name, snapshot in snapshots.items():
        if not name.startswith("completed-run-"):
            continue
        record = json.loads(Path(snapshot["artifact"]).read_text(), object_pairs_hook=unique_object)
        try:
            if not isinstance(record, dict):
                raise ValueError("expected a completed run object")
            if not isinstance(record.get("inputs"), dict):
                raise ValueError("expected approved input snapshots")
            entries = record.get("tickets", {record["ticket"]["id"]: record["ticket"]})
            if not isinstance(entries, dict) or not entries or record["outcome"] != "completed":
                raise ValueError("expected a completed run with Done tickets")
            for key, ticket in entries.items():
                ticket_id = identifier(ticket["id"])
                if "tickets" in record and key != ticket_id:
                    raise ValueError("completion ticket key conflicts with its ID")
                revision = ticket["done_revision"]
                source = Path(requirements[ticket_id]["source"])
                approved = [
                    item
                    for name, item in record["inputs"].items()
                    if (name == "ticket" or name.startswith("ticket-"))
                    and Path(item["source"]).resolve() == source
                ]
                if (
                    ticket["state"] != "Done"
                    or not isinstance(revision, str)
                    or not re.fullmatch(r"[0-9a-f]{40,64}", revision)
                    or len(approved) != 1
                    or approved[0]["sha256"] != hashlib.sha256(source.read_bytes()).hexdigest()
                ):
                    raise ValueError("expected Done for the current approved ticket")
                git(repository, "merge-base", "--is-ancestor", revision, base)
                if ticket_id in completed:
                    raise ValueError(f"duplicate completion evidence for ticket {ticket_id}")
                completed.add(ticket_id)
        except (KeyError, TypeError, ValueError, GateFailure) as error:
            raise GateFailure(
                f"{snapshot['source']}: invalid prerequisite completion evidence: {error}"
            ) from error
    return completed


def require_approved(snapshots: dict[str, Any]) -> None:
    for snapshot in snapshots.values():
        for field in ("source", "artifact"):
            path = Path(snapshot[field])
            if hashlib.sha256(path.read_bytes()).hexdigest() != snapshot["sha256"]:
                raise GateFailure(f"Approved input changed: {path}")


def load(config_path: Path, output: Path) -> tuple[dict[str, Any], dict[str, Any], str]:
    config = configuration(json.loads(config_path.read_text(), object_pairs_hook=unique_object))
    repository = (config_path.parent / config["repository"]).resolve()
    for name in config["checks"]:
        if not re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", name):
            raise GateFailure(f"checks.{name}: invalid check name; use letters, numbers, hyphens")
        command(config["checks"][name], f"checks.{name}", repository, config["base"])
    command(config["agent"], "agent", repository, config["base"])
    command(config["suite"], "suite", repository, config["base"])
    config["repository"] = str(repository)
    if output == repository or repository in output.parents:
        raise GateFailure("Run output must be outside the target repository")
    paths = {
        "configuration": config_path,
        "spec": repository / config["spec"],
        "ticket": repository / config["ticket"],
    }
    if "plan" in config:
        paths["plan"] = repository / config["plan"]
    selected_path = paths["ticket"].resolve()
    bundle = [(repository / path).resolve() for path in config.get("tickets", [config["ticket"]])]
    if selected_path not in bundle:
        raise GateFailure("configuration.tickets must include the selected ticket path")
    if len(set(bundle)) != len(bundle):
        raise GateFailure("configuration.tickets contains duplicate ticket paths")
    selection = [
        (repository / path).resolve() for path in config.get("selected_tickets", [config["ticket"]])
    ]
    if not selection or selected_path not in selection:
        raise GateFailure("configuration.selected_tickets must be nonempty and include ticket")
    if len(set(selection)) != len(selection):
        raise GateFailure("configuration.selected_tickets contains duplicate ticket paths")
    if any(path not in bundle for path in selection):
        raise GateFailure("configuration.selected_tickets must be a subset of tickets")
    for index, path in enumerate(bundle):
        if path != selected_path:
            paths[f"ticket-{index}"] = path
    for index, path in enumerate(config["standards"]):
        paths[f"standards-{index}"] = repository / path
    for index, path in enumerate(config.get("completed_runs", [])):
        paths[f"completed-run-{index}"] = config_path.parent / path
    snapshots: dict[str, Any] = {}
    for name, path in paths.items():
        path = path.resolve()
        if path == output or output in path.parents:
            raise GateFailure("Run output must be separate from approved inputs")
        data = path.read_bytes()
        artifact = output / "inputs" / f"{name}{path.suffix}"
        artifact.write_bytes(data)
        snapshots[name] = {
            "source": str(path),
            "artifact": str(artifact),
            "sha256": hashlib.sha256(data).hexdigest(),
        }
    requirements: dict[str, Any] = {}
    references: dict[str, list[Dependency]] = {}
    for name, snapshot in snapshots.items():
        if name == "ticket" or name.startswith("ticket-"):
            normalized, dependencies = normalize_ticket(
                Path(snapshot["artifact"]).read_text(), Path(snapshot["source"]), config["checks"]
            )
            if normalized["id"] in requirements:
                raise GateFailure(
                    f"{snapshot['source']}: duplicate ticket ID {normalized['id']}; "
                    f"also declared by {requirements[normalized['id']]['source']}"
                )
            requirements[normalized["id"]] = normalized
            references[normalized["id"]] = dependencies
            if name == "ticket":
                ticket = normalized
    config["requirements"] = requirements
    if "plan" in snapshots:
        plan = json.loads(
            Path(snapshots["plan"]["artifact"]).read_text(), object_pairs_hook=unique_object
        )
        from ticket_harness import plans

        config["plan"], config["worker_settings"] = plans.validate(
            plan, requirements, config, ticket["id"]
        )
        selection = [Path(requirements[t]["source"]) for t in plan["milestones"][0]["tickets"]]
    validate_graph(requirements, references)
    selected = sorted(
        (item["id"] for item in requirements.values() if Path(item["source"]) in selection),
        key=int,
    )
    completed = completed_tickets(snapshots, requirements, repository, config["base"])
    # A selected prerequisite must be verified again by this run before it can unlock work.
    executable = config["plan"]["required_tickets"] if "plan" in config else selected
    completed.difference_update(executable)
    for ticket_id in executable:
        item = requirements[ticket_id]
        if item["readiness"] != "ready-for-agent":
            raise GateFailure(
                f"ticket {ticket_id}: selected Status must be ready-for-agent; "
                f"found {item['readiness']!r}"
            )
        missing = [
            dependency
            for dependency in item["dependencies"]
            if dependency not in completed and dependency not in executable
        ]
        if missing:
            raise GateFailure(
                f"ticket {ticket_id}: unsatisfied prerequisites {missing}; "
                "select prerequisites or supply completed_runs with integrated Done evidence"
            )
    config["selected_tickets"] = selected
    config["completed_tickets"] = sorted(completed, key=int)
    return config, snapshots, ticket["id"]
