"""Development-only evidence routing and registration; no review/deletion authority.

Public interface: ``python -m ticket_harness.evidence --help``. Producers own
allocated payloads; this helper owns capture metadata under a directory flock.
Review tools must acquire that same lock before updating review namespaces.
"""

import argparse
import fcntl
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterator
from uuid import uuid4

from ticket_harness.inputs import identifier, unique_object
from ticket_harness.records import GateFailure

REVIEW = "evidence-review.json"


def _text(value: str) -> str:
    if not value.strip():
        raise ValueError("Expected nonempty text")
    return value


def _slug(value: str) -> str:
    if not re.fullmatch(r"[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*", value):
        raise ValueError(f"Expected a descriptive hyphenated name: {value!r}")
    return value


def _safe(path: Path, protected: list[Path]) -> None:
    """Reject path aliases and writes overlapping operator-declared frozen roots."""
    for part in [*reversed(path.parents), path]:
        if part.is_symlink():
            raise ValueError(f"Symlink path is not a capture destination: {part}")
    if path.exists() and path.is_file() and path.stat().st_nlink != 1:
        raise ValueError(f"Hard-linked file is not a capture destination: {path}")
    if any(path == root or root in path.parents for root in protected):
        raise ValueError(f"Protected destination: {path}")


def _load(path: Path) -> dict[str, Any]:
    _safe(path, [])
    value = json.loads(path.read_text(), object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def _save(path: Path, value: dict[str, Any]) -> None:
    """Atomically replace helper metadata while the caller holds evidence ownership."""
    _safe(path, [])
    descriptor, temporary = tempfile.mkstemp(prefix=".capture-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w") as stream:
            json.dump(value, stream, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


class CaptureStore:
    """Own all capture state transitions within one development feature's evidence."""

    def __init__(self, feature: Path, protected: list[Path]) -> None:
        # Resolve the checkout prefix (ADAPT /panfs aliases /explore), then reject
        # aliases inside the checkout. No arbitrary output destination is accepted.
        repository = subprocess.run(
            ["git", "-C", str(feature), "rev-parse", "--show-toplevel"],
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()
        self.repository = Path(repository).resolve()
        self.feature = self.repository / ".scratch" / feature.name
        if feature.resolve() != self.feature or not (self.feature / "issues").is_dir():
            raise ValueError("Feature must be .scratch/<feature> with an issues directory")
        self.protected = [path.absolute().resolve() for path in protected]
        self.evidence = self.feature / "evidence"
        _safe(self.evidence, self.protected)

    @contextmanager
    def ownership(self) -> Iterator[None]:
        """Serialize capture and later review writers on the evidence directory itself."""
        self.evidence.mkdir(exist_ok=True)
        descriptor = os.open(self.evidence, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            _safe(self.evidence, self.protected)
            yield
        finally:
            os.close(descriptor)

    def _ticket(self, number: str) -> dict[str, str]:
        number = identifier(number)
        matches = [
            path
            for path in (self.feature / "issues").glob("*.md")
            if re.match(r"[0-9]+-", path.name) and identifier(path.name.split("-", 1)[0]) == number
        ]
        if len(matches) != 1:
            raise ValueError(f"Expected exactly one issue for ticket {number}")
        return {"id": number, "issue": str(matches[0].relative_to(self.feature))}

    def _record(self, folder: Path, scope: dict[str, Any]) -> dict[str, Any]:
        path = folder / REVIEW
        _safe(path, self.protected)
        if not path.exists():
            return {
                "schema_version": 1,
                "folder": str(folder.relative_to(self.feature)),
                "scope": scope,
                "captures": [],
                "shared_records": [],
                "assessments": [],
                "approvals": [],
                "execution_results": [],
            }
        value = _load(path)
        if (
            value.get("schema_version") != 1
            or value.get("scope") != scope
            or value.get("folder") != str(folder.relative_to(self.feature))
        ):
            raise ValueError(f"Incompatible evidence record: {path}")
        for field in (
            "captures",
            "shared_records",
            "assessments",
            "approvals",
            "execution_results",
        ):
            if not isinstance(value.get(field), list):
                raise ValueError(f"Invalid evidence record field {field}: {path}")
        return value

    def allocate(
        self,
        tickets: list[str],
        shared: str | None,
        milestone: str | None,
        purpose: str,
        producer: str,
    ) -> dict[str, str]:
        """Create a unique producer destination and idempotent shared references."""
        selected = sorted((self._ticket(number) for number in tickets), key=lambda t: t["id"])
        if len({ticket["id"] for ticket in selected}) != len(selected):
            raise ValueError("Duplicate ticket selection")
        if (shared is None and (len(selected) != 1 or milestone is not None)) or (
            shared is not None and len(selected) < 2
        ):
            raise ValueError(
                "Use one ticket, or --shared with at least two tickets; milestones are shared"
            )
        purpose, producer = _text(purpose), _slug(producer)
        if shared is not None:
            # Reserve ticket-* for actual ticket folders.
            if _slug(shared).lower().startswith("ticket-"):
                raise ValueError("Shared name cannot use the ticket- prefix")
            folder = self.evidence / shared
            if milestone is not None:
                folder /= _slug(milestone)
        else:
            folder = self.evidence / f"ticket-{selected[0]['id']}"
        scope = {"tickets": selected, "shared": shared, "milestone": milestone}
        with self.ownership():
            # Validate every destination before the first metadata write.
            record = self._record(folder, scope)
            linked: list[tuple[Path, dict[str, Any]]] = []
            if shared is not None:
                for ticket in selected:
                    target = self.evidence / f"ticket-{ticket['id']}"
                    local = self._record(
                        target,
                        {
                            "tickets": [ticket],
                            "shared": None,
                            "milestone": None,
                        },
                    )
                    reference = str((folder / REVIEW).relative_to(self.feature))
                    if reference not in local["shared_records"]:
                        local["shared_records"].append(reference)
                    linked.append((target, local))
            capture_id = uuid4().hex
            destination = folder / "captures" / f"{producer}-{capture_id}"
            _safe(destination, self.protected)
            destination.mkdir(parents=True, exist_ok=False)
            allocation = {
                "schema_version": 1,
                "id": capture_id,
                "scope": scope,
                "folder": str(folder.relative_to(self.feature)),
                "destination": str(destination.relative_to(self.feature)),
                "purpose": purpose,
                "producer": producer,
                "protected": [str(path) for path in self.protected],
                "created_at": datetime.now(UTC).isoformat(),
            }
            receipt = destination / "allocation.json"
            _save(receipt, allocation)
            _save(folder / REVIEW, record)
            for target, local in linked:
                target.mkdir(parents=True, exist_ok=True)
                _save(target / REVIEW, local)
        return {
            "allocation": str(receipt),
            "destination": str(destination),
            "review_artifact": str(folder / REVIEW),
        }

    def _within(self, relative: str, root: Path) -> Path:
        path = self.feature / relative
        if (
            Path(relative).is_absolute()
            or ".." in Path(relative).parts
            or not path.is_relative_to(root)
        ):
            raise ValueError(f"Path escapes capture destination: {relative}")
        _safe(path, self.protected)
        return path

    def _identity(self, path: Path) -> dict[str, Any]:
        _safe(path, self.protected)
        if not stat.S_ISREG(path.stat().st_mode):
            raise ValueError(f"Expected regular capture file: {path}")
        content = path.read_bytes()
        return {
            "path": str(path.relative_to(self.feature)),
            "size": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        }

    def register(
        self,
        receipt: Path,
        files: list[str],
        source: str,
        activity: str,
        result: str,
        kind: str,
        derived_from: list[str],
    ) -> dict[str, Any]:
        """Append observed file identities; reject mutation of any registered originals."""
        receipt = receipt.absolute()
        if not receipt.is_relative_to(self.evidence):
            raise ValueError("Allocation must be inside this feature's evidence")
        allocation = _load(receipt)
        self.protected.extend(Path(path) for path in allocation["protected"])
        _safe(self.evidence, self.protected)
        destination = self._within(allocation["destination"], self.evidence)
        folder = self._within(allocation["folder"], self.evidence)
        if (
            receipt != destination / "allocation.json"
            or destination.parent != folder / "captures"
            or not destination.name.endswith("-" + allocation["id"])
        ):
            raise ValueError("Allocation identity does not match its location")
        if (kind == "derived") != bool(derived_from):
            raise ValueError(
                "Derived captures require --derived-from; originals cannot declare derivation"
            )
        for value in (source, activity, result):
            _text(value)
        with self.ownership():
            record = self._record(folder, allocation["scope"])
            identities = []
            for name in files:
                path = self._within(str(destination.relative_to(self.feature) / name), destination)
                if path == receipt:
                    raise ValueError("Allocation metadata is not a capture payload")
                identities.append(self._identity(path))
            if len({item["path"] for item in identities}) != len(identities):
                raise ValueError("Duplicate capture file")
            originals = [self._identity(self._within(name, self.evidence)) for name in derived_from]
            capture = {
                "id": allocation["id"],
                "purpose": allocation["purpose"],
                "producer": allocation["producer"],
                "source_version": source,
                "activity": activity,
                "result": result,
                "kind": kind,
                "derived_from": originals,
                "files": identities,
            }
            for prior in record["captures"]:
                for item in prior["files"]:
                    if self._identity(self._within(item["path"], self.evidence)) != item:
                        raise ValueError(f"Registered original changed: {item['path']}")
            for prior in record["captures"]:
                if prior["id"] == capture["id"]:
                    if prior != capture:
                        raise ValueError(
                            "Existing capture cannot be overwritten; allocate a new destination"
                        )
                    return {"review_artifact": str(folder / REVIEW), "capture": prior}
            record["captures"].append(capture)
            _save(folder / REVIEW, record)
        return {"review_artifact": str(folder / REVIEW), "capture": capture}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feature", required=True, type=Path)
    parser.add_argument(
        "--protect",
        action="append",
        default=[],
        type=Path,
        help="Active approved-input/frozen path or subtree; repeat as needed",
    )
    commands = parser.add_subparsers(dest="operation", required=True)
    allocate = commands.add_parser(
        "allocate", help="Select and reserve a unique producer destination"
    )
    allocate.add_argument("--ticket", action="append", required=True)
    allocate.add_argument("--shared")
    allocate.add_argument("--milestone")
    allocate.add_argument("--purpose", required=True)
    allocate.add_argument("--producer", required=True)
    register = commands.add_parser(
        "register", help="Register existing payload bytes and observed facts"
    )
    register.add_argument("--allocation", required=True, type=Path)
    register.add_argument(
        "--file", action="append", required=True, help="Relative to allocated destination"
    )
    register.add_argument("--source-version", required=True)
    register.add_argument("--activity", required=True)
    register.add_argument("--result", required=True)
    register.add_argument("--kind", choices=("original", "derived"), default="original")
    register.add_argument(
        "--derived-from", action="append", default=[], help="Original path relative to feature"
    )
    args = parser.parse_args()
    try:
        store = CaptureStore(args.feature, args.protect)
        if args.operation == "allocate":
            output = store.allocate(
                args.ticket, args.shared, args.milestone, args.purpose, args.producer
            )
        else:
            output = store.register(
                args.allocation,
                args.file,
                args.source_version,
                args.activity,
                args.result,
                args.kind,
                args.derived_from,
            )
        print(json.dumps(output, indent=2))
        return 0
    except (
        GateFailure,
        OSError,
        ValueError,
        KeyError,
        TypeError,
        subprocess.CalledProcessError,
    ) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
