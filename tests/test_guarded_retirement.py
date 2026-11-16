"""Guarded local retirement exercised through the evidence command line."""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def identity(feature, relative, content):
    path = feature / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return {
        "path": relative,
        "size": len(content.encode()),
        "sha256": hashlib.sha256(content.encode()).hexdigest(),
        "kind": "regular",
    }


@pytest.fixture
def sample(tmp_path, request):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    feature = tmp_path / ".scratch" / "sample"
    (feature / "issues").mkdir(parents=True)
    (feature / "issues" / "01-sample.md").write_text("sample")
    output = subprocess.run(
        [
            sys.executable,
            "-m",
            "ticket_harness.evidence",
            "--feature",
            str(feature),
            "allocate",
            "--ticket",
            "01",
            "--purpose",
            "retirement trial",
            "--producer",
            "worker",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    allocation = json.loads(output.stdout)
    authority = Path(allocation["review_artifact"])
    destination = Path(allocation["destination"])
    (destination / "retained.log").write_text("retained original capture\n")
    registered = subprocess.run(
        [
            sys.executable,
            "-m",
            "ticket_harness.evidence",
            "--feature",
            str(feature),
            "register",
            "--allocation",
            allocation["allocation"],
            "--file",
            "retained.log",
            "--source-version",
            "fixture-source",
            "--activity",
            "fixture passing check",
            "--result",
            "exit 0",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    for observation in (output, registered):
        observe(feature, observation)
    raw = identity(feature, "evidence/ticket-01/raw.log", "routine passing output\n")
    result = identity(feature, "evidence/ticket-01/result.md", "exit 0; exact source retained\n")
    source = identity(feature, "evidence/ticket-01/source.patch", "exact source version\n")
    report = identity(
        feature, "evidence/ticket-01/review.md", "independent content/uses/replacement review\n"
    )
    proposal = {
        "schema_version": 1,
        "source_identity": "commit:fixture + source.patch",
        "protected": [report],
        "groups": [
            {
                "id": "routine",
                "action": "delete",
                "assessor": "assessor",
                "evidence_type": "routine",
                "reason": "required checks passed; no remaining use",
                "files": [raw],
                "remaining_uses": [],
                "conditions": [
                    {
                        "id": "required checks/reviews completed",
                        "resolved": True,
                        "evidence": [result],
                    }
                ],
                "retained_results": [result],
                "source": [source],
                "replacements": [],
                "protected": [],
            }
        ],
    }
    value = json.loads(authority.read_text())
    value["retirement"] = proposal
    value["retirement_approvals"] = [
        {
            "group": "routine",
            "proposal_sha256": digest(proposal),
            "reviewer": "fresh-reviewer",
            "decision": "approve",
            "report": report,
            "human_merge": None,
        }
    ]
    authority.write_text(json.dumps(value))
    yield feature, authority, value
    if location := os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS"):
        retained = Path(location) / "evidence-retirement" / request.node.name
        retained.mkdir(parents=True, exist_ok=False)
        shutil.copytree(feature, retained / "feature", symlinks=True)
        shutil.copyfile(tmp_path / "commands.jsonl", retained / "commands.jsonl")


def observe(feature, output):
    if os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS"):
        with (feature.parent.parent / "commands.jsonl").open("a") as stream:
            stream.write(
                json.dumps(
                    {
                        "argv": output.args,
                        "returncode": output.returncode,
                        "stdout": output.stdout,
                        "stderr": output.stderr,
                    }
                )
                + "\n"
            )


def command(sample, operation, *extra):
    feature, authority, _ = sample
    output = subprocess.run(
        [
            sys.executable,
            "-m",
            "ticket_harness.evidence",
            "--feature",
            str(feature),
            *extra,
            operation,
            "--authority",
            str(authority.relative_to(feature)),
            "--group",
            "routine",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    observe(feature, output)
    return output


def test_preview_is_read_only_and_execution_records_actual_deletion(sample):
    feature, authority, original = sample
    before = authority.read_bytes()
    preview = command(sample, "preview")
    assert preview.returncode == 0, preview.stderr
    assert json.loads(preview.stdout)["state"] == "eligible"
    assert authority.read_bytes() == before
    assert (feature / "evidence/ticket-01/raw.log").exists()
    executed = command(sample, "execute")
    assert executed.returncode == 0, executed.stderr
    assert not (feature / "evidence/ticket-01/raw.log").exists()
    record = json.loads(authority.read_text())
    assert record["captures"] == original["captures"]
    assert record["retirement_approvals"] == original["retirement_approvals"]
    assert record["execution_results"][-1]["files"][0]["state"] == "deleted"
    assert (feature / "evidence/ticket-01/review.md").exists()


@pytest.mark.parametrize(
    "change",
    [
        "missing-review",
        "stale-original",
        "stale-result",
        "protected",
        "unresolved",
        "duplicate",
        "historical-keep",
        "symlink",
        "hardlink",
        "control",
    ],
)
def test_preflight_failure_never_deletes_or_mutates_authority(sample, change):
    feature, authority, value = sample
    group = value["retirement"]["groups"][0]
    extra = []
    if change == "missing-review":
        value["retirement_approvals"] = []
    elif change == "stale-original":
        (feature / group["files"][0]["path"]).write_text("changed")
    elif change == "stale-result":
        (feature / group["retained_results"][0]["path"]).write_text("changed result")
    elif change == "protected":
        extra = ["--protect", str(feature / group["files"][0]["path"])]
    elif change == "unresolved":
        group["conditions"][0]["resolved"] = False
        value["retirement_approvals"][0]["proposal_sha256"] = digest(value["retirement"])
    elif change == "duplicate":
        value["retirement_approvals"].append(value["retirement_approvals"][0])
    elif change == "historical-keep":
        value["assessments"] = [{"groups": [{"proposed_action": "keep", "files": group["files"]}]}]
    elif change == "symlink":
        path = feature / group["files"][0]["path"]
        path.unlink()
        path.symlink_to("result.md")
    elif change == "hardlink":
        os.link(feature / group["files"][0]["path"], feature / "evidence/ticket-01/alias.log")
    elif change == "control":
        group["files"] = [identity(feature, "evidence/ticket-01/allocation.json", "control")]
        value["retirement_approvals"][0]["proposal_sha256"] = digest(value["retirement"])
    authority.write_text(json.dumps(value))
    before = authority.read_bytes()
    output = command(sample, "execute", *extra)
    assert output.returncode != 0
    assert authority.read_bytes() == before
    assert (feature / "evidence/ticket-01/raw.log").exists()


@pytest.mark.parametrize("change", ["missing-human", "changed-replacement", "success"])
def test_merge_requires_exact_reviewed_replacement_and_human_approval(sample, change):
    feature, authority, value = sample
    group = value["retirement"]["groups"][0]
    group["action"] = "merge"
    group["replacements"] = [
        identity(
            feature,
            "evidence/ticket-01/merged.md",
            "reviewed lossy summary; source and limitations retained",
        )
    ]
    approval = value["retirement_approvals"][0]
    approval["proposal_sha256"] = digest(value["retirement"])
    approval["human_merge"] = (
        None
        if change == "missing-human"
        else {
            "actor": "human",
            "statement": "approve this exact replacement",
            "proposal_sha256": approval["proposal_sha256"],
            "replacements": group["replacements"],
        }
    )
    authority.write_text(json.dumps(value))
    if change == "changed-replacement":
        (feature / group["replacements"][0]["path"]).write_text("different summary")
    output = command(sample, "execute")
    assert (output.returncode == 0) == (change == "success"), output.stderr
    assert (feature / "evidence/ticket-01/raw.log").exists() == (change != "success")
    assert (feature / "evidence/ticket-01/merged.md").exists()


def test_partial_filesystem_failure_records_actual_results_separately(sample):
    feature, authority, value = sample
    group = value["retirement"]["groups"][0]
    second = identity(feature, "evidence/ticket-01/read-only/second.log", "routine output")
    group["files"].append(second)
    value["retirement_approvals"][0]["proposal_sha256"] = digest(value["retirement"])
    authority.write_text(json.dumps(value))
    parent = (feature / second["path"]).parent
    parent.chmod(0o500)
    try:
        output = command(sample, "execute")
        assert output.returncode != 0
        results = json.loads(output.stdout)
        assert results["state"] == "partial"
        assert [item["state"] for item in results["files"]] == ["deleted", "failed"]
        stored = json.loads(authority.read_text())
        assert stored["retirement_approvals"] == value["retirement_approvals"]
        assert stored["execution_results"][-1] == results
        assert (feature / second["path"]).exists()
        assert not (feature / "evidence/ticket-01/raw.log").exists()
    finally:
        parent.chmod(0o700)


def test_review_report_from_another_group_cannot_be_deleted(sample):
    feature, authority, value = sample
    report = identity(
        feature, "evidence/ticket-01/other-review.md", "another durable original review"
    )
    value["retirement"]["groups"][0]["files"] = [report]
    value["retirement_approvals"][0]["proposal_sha256"] = digest(value["retirement"])
    value["retirement_approvals"].append({"group": "other-group", "report": report})
    authority.write_text(json.dumps(value))
    output = command(sample, "execute")
    assert output.returncode != 0
    assert (feature / report["path"]).exists()


def test_recording_failure_returns_successful_unlink_and_stops_further_work(sample):
    feature, authority, value = sample
    group = value["retirement"]["groups"][0]
    first = identity(feature, "evidence/ticket-01/writable/first.log", "routine first")
    second = identity(feature, "evidence/ticket-01/writable/second.log", "routine second")
    group["files"] = [first, second]
    value["retirement_approvals"][0]["proposal_sha256"] = digest(value["retirement"])
    authority.write_text(json.dumps(value))
    authority.parent.chmod(0o500)
    try:
        output = command(sample, "execute")
        assert output.returncode != 0
        result = json.loads(output.stdout)
        assert result["state"] == "partial"
        assert result["files"][0]["state"] == "deleted"
        assert result["recording_error"]
        assert not (feature / first["path"]).exists()
        assert (feature / second["path"]).exists()
        assert json.loads(authority.read_text())["execution_results"] == []
    finally:
        authority.parent.chmod(0o700)
