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
    """Return timeout defaults merged with validated stage seconds.

    Reject unknown stages and nonpositive, nonfinite or oversized values with
    GateFailure; leave the supplied mapping unchanged.
    """
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
    """Build one JSON object, rejecting duplicate keys with GateFailure.

    Used as object_pairs_hook so duplicates cannot silently overwrite approval data.
    """
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise GateFailure(f"duplicate JSON key {key!r}; keep one authoritative value")
        value[key] = item
    return value


def identifier(value: str) -> str:
    """Normalize a positive numeric string to an ID padded to at least two digits.

    Raise GateFailure for invalid numeric text; preserve IDs wider than two digits.
    """
    if not re.fullmatch(r"[0-9]+", value) or int(value) < 1:
        raise GateFailure(f"Invalid ticket ID {value!r}; use a positive numeric identifier")
    return str(int(value)).zfill(2)


def command(value: Any, field: str, repository: Path, base: str) -> None:
    """Validate argv and executable availability without launching the command.

    Relative executable paths must be executable blobs at base in repository;
    other commands must resolve absolutely on PATH. Raise GateFailure on rejection.
    """
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
    """Validate raw configuration and return that mapping with timeout/repair defaults.

    Mutates defaults in place; executable and filesystem checks belong to load.
    Raise GateFailure on the first invalid field in contract validation order.
    """
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
    """Declared prerequisite identity plus optional title/link for later graph checks."""

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


def _ticket_dependencies(declaration: str, path: Path) -> tuple[list[str], list[Dependency]]:
    """Parse Blocked by labels/links, retaining order and duplicate references.

    Resolve links relative to the ticket; reject malformed labels with GateFailure.
    """
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
    return dependencies, dependency_references


def _ticket_acceptance(
    text: str, metadata: dict[str, str], path: Path, checks: dict[str, Any]
) -> tuple[list[str], list[str]]:
    """Return checklist content and ordered check names, validating each declaration.

    Missing Checks metadata selects all configured checks. Raises GateFailure for
    malformed acceptance content or unknown/duplicate check references.
    """
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
    return requirements, references


def normalize_ticket(
    text: str, path: Path, checks: dict[str, Any]
) -> tuple[dict[str, Any], list[Dependency]]:
    """Return normalized Markdown requirements and unresolved dependency references.

    Ignore examples/comments, then validate heading, metadata, dependencies and
    acceptance/check declarations in that order. Source text and checks remain
    unchanged; GateFailure identifies invalid or conflicting declarations. Graph
    consistency and execution eligibility are checked later by load.
    """
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
    dependencies, dependency_references = _ticket_dependencies(metadata.get("Blocked by", ""), path)
    requirements, references = _ticket_acceptance(text, metadata, path, checks)
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
    """Reject missing/mismatched references and cycles across the entire bundle.

    Read requirements and resolved link references without mutation. Validate
    reference identity before iterative cycle detection, raising GateFailure.
    """
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


def _collect_completed(
    record: Any,
    requirements: dict[str, Any],
    repository: Path,
    base: str,
    completed: set[str],
) -> None:
    """Add evidence-backed Done IDs after checking approval hashes and ancestry.

    Mutates completed in record order, rejecting duplicates across records. Errors
    propagate to completed_tickets for source attribution; prior additions remain
    local to that preparation operation when a later entry fails.
    """
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


def completed_tickets(
    snapshots: dict[str, Any], requirements: dict[str, Any], repository: Path, base: str
) -> set[str]:
    """Return prerequisite IDs backed by captured completed runs integrated at base.

    Read saved records and current ticket bytes; validate approval hashes, Done
    revisions and Git ancestry before accepting each ID. Evidence errors become
    source-attributed GateFailure; JSON decoding and filesystem errors propagate.
    The caller subsequently removes tickets that this run must verify again.
    """
    completed: set[str] = set()
    for name, snapshot in snapshots.items():
        if not name.startswith("completed-run-"):
            continue
        record = json.loads(Path(snapshot["artifact"]).read_text(), object_pairs_hook=unique_object)
        try:
            _collect_completed(record, requirements, repository, base, completed)
        except (KeyError, TypeError, ValueError, GateFailure) as error:
            raise GateFailure(
                f"{snapshot['source']}: invalid prerequisite completion evidence: {error}"
            ) from error
    return completed


def require_approved(snapshots: dict[str, Any]) -> None:
    """Recheck source and captured bytes against every recorded approval hash.

    Raise GateFailure on the first changed input; filesystem errors propagate.
    Neither the input records nor files are modified.
    """
    for snapshot in snapshots.values():
        for field in ("source", "artifact"):
            path = Path(snapshot[field])
            if hashlib.sha256(path.read_bytes()).hexdigest() != snapshot["sha256"]:
                raise GateFailure(f"Approved input changed: {path}")


@dataclass(frozen=True)
class PreparedInputs:
    """Validated settings and derived execution inputs from one preparation operation.

    Settings retain configuration paths/selections; normalized values live in their
    own fields. The frozen carrier retains mutable nested values; load alone
    initializes them, and consumers must preserve their checked invariants.
    The execution mapping preserves the existing durable checkpoint
    shape without enriching the settings or serializing this in-memory carrier.
    """

    settings: dict[str, Any]
    snapshots: dict[str, Any]
    requirements: dict[str, Any]
    primary: str
    selected: list[str]
    completed: list[str]
    plan: dict[str, Any] | None
    worker_settings: dict[str, Any] | None

    def execution_config(self) -> dict[str, Any]:
        """Return the existing JSON-safe execution/checkpoint mapping.

        Create a new outer mapping without enriching raw settings. Nested prepared
        values retain their identities; this conversion does not copy or revalidate them.
        """
        config = self.settings | {
            "requirements": self.requirements,
            "selected_tickets": self.selected,
            "completed_tickets": self.completed,
        }
        if self.plan is not None:
            config.update(plan=self.plan, worker_settings=self.worker_settings)
        return config


def _input_paths(
    config: dict[str, Any], config_path: Path, repository: Path
) -> tuple[dict[str, Path], list[Path]]:
    """Resolve bundle/selection membership and name all approved input sources.

    Retain declaration order and artifact names; reject invalid selection before
    any snapshot is copied. Completed-run paths are relative to configuration.
    """
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
    return paths, selection


def _capture_inputs(paths: dict[str, Path], output: Path) -> dict[str, Any]:
    """Copy approved bytes to an existing inputs directory and return hash records.

    Reject source/output overlap before each copy. Filesystem errors propagate;
    earlier copies can remain when a later source fails. Never write source files.
    """
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
    return snapshots


def _ticket_requirements(
    snapshots: dict[str, Any], checks: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, list[Dependency]], str]:
    """Normalize captured ticket bytes and return requirements, links and primary ID.

    Requires the primary ticket snapshot. Reject duplicate normalized IDs before
    graph/plan validation; only newly created requirement mappings are populated.
    """
    requirements: dict[str, Any] = {}
    references: dict[str, list[Dependency]] = {}
    for name, snapshot in snapshots.items():
        if name == "ticket" or name.startswith("ticket-"):
            normalized, dependencies = normalize_ticket(
                Path(snapshot["artifact"]).read_text(), Path(snapshot["source"]), checks
            )
            if normalized["id"] in requirements:
                raise GateFailure(
                    f"{snapshot['source']}: duplicate ticket ID {normalized['id']}; "
                    f"also declared by {requirements[normalized['id']]['source']}"
                )
            requirements[normalized["id"]] = normalized
            references[normalized["id"]] = dependencies
            if name == "ticket":
                primary = normalized["id"]
    return requirements, references, primary


def _require_executable(
    requirements: dict[str, Any], executable: list[str], completed: set[str]
) -> None:
    """Require agent readiness and satisfied prerequisites for every executable ID.

    Read prepared values without mutation. A plan supplies all required tickets,
    including later milestones; legacy runs supply only their selected tickets.
    Raise GateFailure on the first readiness or missing-prerequisite failure.
    """
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


def load(config_path: Path, output: Path) -> PreparedInputs:
    """Prepare inputs before execution, copying approved bytes into output/inputs.

    The caller must create output/inputs first. Output must be outside the target
    repository and separate from every approved input; violations reject before
    any worker/check execution or ref advancement. Source files are never written.
    Return a complete PreparedInputs only after plan, graph, completion and
    eligibility checks. GateFailure rejects invalid contracts; JSON/filesystem
    errors propagate, and partial captures can remain if preparation fails.
    """
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
    paths, selection = _input_paths(config, config_path, repository)
    snapshots = _capture_inputs(paths, output)
    requirements, references, primary = _ticket_requirements(snapshots, config["checks"])
    checked_plan = None
    worker_settings = None
    if "plan" in snapshots:
        plan = json.loads(
            Path(snapshots["plan"]["artifact"]).read_text(), object_pairs_hook=unique_object
        )
        from ticket_harness import plans

        checked_plan, worker_settings = plans.validate(plan, requirements, config, primary)
        selection = [
            Path(requirements[t]["source"]) for t in checked_plan["milestones"][0]["tickets"]
        ]
    validate_graph(requirements, references)
    selected = sorted(
        (item["id"] for item in requirements.values() if Path(item["source"]) in selection),
        key=int,
    )
    completed = completed_tickets(snapshots, requirements, repository, config["base"])
    # A selected prerequisite must be verified again by this run before it can unlock work.
    executable = checked_plan["required_tickets"] if checked_plan is not None else selected
    completed.difference_update(executable)
    _require_executable(requirements, executable, completed)
    return PreparedInputs(
        config,
        snapshots,
        requirements,
        primary,
        selected,
        sorted(completed, key=int),
        checked_plan,
        worker_settings,
    )
