"""Explicit local retirement authority; capture provenance never grants deletion."""

import hashlib
import json
import stat
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from ticket_harness.evidence import REVIEW, CaptureStore, _load, _safe, _save, _text


def proposal_digest(proposal: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(proposal, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    ).hexdigest()


class Retirement:
    """Validate a complete proposal, then record each actual filesystem transition.

    All writers use CaptureStore's evidence directory lock. Historical review fields
    remain untouched. No restoration or arbitrary crash recovery is promised.
    """

    def __init__(self, store: CaptureStore) -> None:
        self.store = store

    def path(self, relative: str, *, deletion: bool = False) -> Path:
        path = self.store.feature / relative
        if (
            not relative
            or str(Path(relative)) != relative
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
            or not path.is_relative_to(self.store.feature)
            or (deletion and not path.is_relative_to(self.store.evidence))
        ):
            raise ValueError(f"Invalid retirement path: {relative}")
        _safe(path, self.store.protected if deletion else [])
        if deletion and path.name in (REVIEW, "allocation.json"):
            raise ValueError(f"Control metadata cannot be retired: {relative}")
        return path

    def identity(self, item: dict[str, Any], *, deletion: bool = False) -> Path:
        if set(item) != {"path", "size", "sha256", "kind"} or item["kind"] != "regular":
            raise ValueError("Expected exact regular-file identity")
        path = self.path(item["path"], deletion=deletion)
        details = path.stat()
        if not stat.S_ISREG(details.st_mode) or details.st_nlink != 1:
            raise ValueError(f"Expected unaliased regular file: {path}")
        content = path.read_bytes()
        if (
            type(item["size"]) is not int
            or item["size"] != len(content)
            or item["sha256"] != hashlib.sha256(content).hexdigest()
        ):
            raise ValueError(f"Stale file identity: {path}")
        return path

    def prepare(
        self, authority: Path, selected: list[str]
    ) -> tuple[dict[str, Any], str, list[dict[str, Any]], list[dict[str, Any]]]:
        record = _load(authority)
        if (
            record.get("schema_version") != 1
            or record.get("folder") != str(authority.parent.relative_to(self.store.feature))
            or not isinstance(record.get("scope"), dict)
            or any(
                not isinstance(record.get(key), list)
                for key in (
                    "captures",
                    "shared_records",
                    "assessments",
                    "approvals",
                    "execution_results",
                )
            )
        ):
            raise ValueError("Incompatible evidence authority")
        proposal = record["retirement"]
        if (
            set(proposal) != {"schema_version", "source_identity", "protected", "groups"}
            or proposal["schema_version"] != 1
        ):
            raise ValueError("Unsupported retirement schema")
        _text(proposal["source_identity"])
        digest = proposal_digest(proposal)
        groups = proposal["groups"]
        identifiers = [group["id"] for group in groups]
        if (
            not selected
            or len(set(selected)) != len(selected)
            or len(set(identifiers)) != len(identifiers)
            or not set(selected) <= set(identifiers)
        ):
            raise ValueError("Duplicate or unknown group selection")
        survivors = list(proposal["protected"])
        # Historical decisions are protection only, never fresh deletion authority.
        historical: set[str] = set()
        for assessment in record["assessments"]:
            for group in assessment.get("groups", []):
                if group.get("proposed_action") in ("keep", "merge proposed"):
                    historical.update(item["path"] for item in group.get("files", []))
        candidates: list[dict[str, Any]] = []
        seen: set[str] = set()
        approvals = record["retirement_approvals"]
        if not isinstance(approvals, list):
            raise ValueError("Expected fresh retirement approvals")
        for approval in approvals:
            if approval.get("group") not in identifiers:
                raise ValueError("Approval names an unknown group")
            survivors.append(approval["report"])
        for group in groups:
            if set(group) != {
                "id",
                "action",
                "assessor",
                "evidence_type",
                "reason",
                "files",
                "remaining_uses",
                "conditions",
                "retained_results",
                "source",
                "replacements",
                "protected",
            }:
                raise ValueError("Unsupported retirement group schema")
            for field in ("id", "assessor", "evidence_type", "reason"):
                _text(group[field])
            if group["action"] not in ("keep", "delete", "merge") or not group["files"]:
                raise ValueError("Invalid action or empty group")
            for item in group["files"]:
                if item["path"] in seen:
                    raise ValueError("Duplicate file across proposal groups")
                seen.add(item["path"])
            survivors.extend(
                group["protected"]
                + group["retained_results"]
                + group["source"]
                + group["replacements"]
            )
            for condition in group["conditions"]:
                if set(condition) != {"id", "resolved", "evidence"}:
                    raise ValueError("Unsupported retention condition")
                survivors.extend(condition["evidence"])
            if group["id"] not in selected or group["action"] == "keep":
                survivors.extend(group["files"])
                continue
            if (
                group["evidence_type"] != "routine"
                or group["remaining_uses"] != []
                or not group["conditions"]
                or not group["retained_results"]
                or not group["source"]
            ):
                raise ValueError("Unresolved uses or missing retained results/source/conditions")
            if any(
                condition["resolved"] is not True or not condition["evidence"]
                for condition in group["conditions"]
            ):
                raise ValueError("Unresolved retention condition")
            decisions = [approval for approval in approvals if approval.get("group") == group["id"]]
            if len(decisions) != 1:
                raise ValueError("Missing or conflicting fresh reviewer approval")
            approval = decisions[0]
            if set(approval) != {
                "group",
                "proposal_sha256",
                "reviewer",
                "decision",
                "report",
                "human_merge",
            }:
                raise ValueError("Unsupported reviewer approval")
            if (
                approval["decision"] != "approve"
                or approval["proposal_sha256"] != digest
                or approval["reviewer"] == group["assessor"]
            ):
                raise ValueError("Stale or non-independent reviewer approval")
            _text(approval["reviewer"])
            survivors.append(approval["report"])
            if group["action"] == "merge":
                human = approval["human_merge"]
                if not isinstance(human, dict) or set(human) != {
                    "actor",
                    "statement",
                    "proposal_sha256",
                    "replacements",
                }:
                    raise ValueError("Missing human merge approval")
                _text(human["actor"])
                _text(human["statement"])
                if (
                    not group["replacements"]
                    or human["proposal_sha256"] != digest
                    or human["replacements"] != group["replacements"]
                ):
                    raise ValueError("Stale human merge approval")
            elif group["replacements"] or approval["human_merge"] is not None:
                raise ValueError("Replacement requires explicit merge action")
            candidates.extend({"group": group["id"], "identity": item} for item in group["files"])
        protected = {item["path"] for item in survivors} | historical
        for item in survivors:
            self.identity(item)
        if not candidates:
            raise ValueError("Selection has no eligible deletion")
        for candidate in candidates:
            item = candidate["identity"]
            if item["path"] in protected:
                raise ValueError(f"Protected retained dependency: {item['path']}")
            self.identity(item, deletion=True)
        return record, digest, candidates, survivors

    def run(self, relative: str, selected: list[str], execute: bool) -> dict[str, Any]:
        authority = self.path(relative)
        if authority.name != REVIEW or not authority.is_relative_to(self.store.evidence):
            raise ValueError("Authority must be an evidence-review.json inside evidence")
        _safe(authority, self.store.protected)
        # Opening an existing directory for flock is read-only; preview must not mkdir.
        if not self.store.evidence.is_dir():
            raise ValueError("Evidence directory must already exist")
        with self.store.ownership():
            record, digest, candidates, survivors = self.prepare(authority, selected)
            if not execute:
                return {"state": "eligible", "proposal_sha256": digest, "files": candidates}
            result: dict[str, Any] = {
                "id": uuid4().hex,
                "at": datetime.now(UTC).isoformat(),
                "proposal_sha256": digest,
                "groups": selected,
                "files": [],
                "navigation": "pending operator reconciliation",
            }
            previous_results = list(record["execution_results"])
            for candidate in candidates:
                outcome = dict(candidate)
                try:
                    # Revalidate authority and every retained dependency before every unlink.
                    if _load(authority) != record:
                        raise ValueError("Authority changed during execution")
                    for survivor in survivors:
                        self.identity(survivor)
                    path = self.identity(candidate["identity"], deletion=True)
                    path.unlink()
                    outcome["state"] = "deleted"
                except (OSError, ValueError) as error:
                    outcome.update(state="failed", error=str(error))
                result["files"].append(outcome)
                # Persist actual outcomes incrementally, preserving all capture/future fields.
                updated = dict(record)
                updated["execution_results"] = [*previous_results, result]
                try:
                    _save(authority, updated)
                except OSError as error:
                    result.update(state="partial", recording_error=str(error))
                    return result
                record = updated
            result["state"] = (
                "completed"
                if all(item["state"] == "deleted" for item in result["files"])
                else "partial"
            )
            try:
                for survivor in survivors:
                    self.identity(survivor)
                result["protected_verification"] = "unchanged"
            except (OSError, ValueError) as error:
                result.update(state="partial", protected_verification=str(error))
            try:
                _save(authority, record)
            except OSError as error:
                result.update(state="partial", recording_error=str(error))
            return result
