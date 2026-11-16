"""Development evidence capture through public processes and observable files."""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def feature(tmp_path, request):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    folder = tmp_path / ".scratch" / "sample"
    issues = folder / "issues"
    issues.mkdir(parents=True)
    for number in ("25", "26"):
        (issues / f"{number}-sample.md").write_text(f"# {number}: Sample\n")
    yield folder
    if location := os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS"):
        output = Path(location) / "evidence-capture" / request.node.name
        output.mkdir(parents=True, exist_ok=False)
        shutil.copytree(folder, output / "feature", symlinks=True)
        transcript = tmp_path / "commands.jsonl"
        if transcript.exists():
            shutil.copyfile(transcript, output / "commands.jsonl")


def cli(feature, *args, ok=True):
    result = subprocess.run(
        [sys.executable, "-m", "ticket_harness.evidence", "--feature", str(feature), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS"):
        with (feature.parent.parent / "commands.jsonl").open("a") as stream:
            stream.write(
                json.dumps(
                    {
                        "argv": result.args,
                        "returncode": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr,
                    }
                )
                + "\n"
            )
    if ok:
        assert result.returncode == 0, result.stdout + result.stderr
        return json.loads(result.stdout)
    assert result.returncode != 0, result.stdout
    return result


def allocate(feature, *args):
    return cli(
        feature,
        "allocate",
        "--ticket",
        "25",
        "--purpose",
        "check results",
        "--producer",
        "worker",
        *args,
    )


def register(feature, allocation, *args, ok=True):
    return cli(
        feature,
        "register",
        "--allocation",
        allocation["allocation"],
        "--file",
        "checks.log",
        "--source-version",
        "commit:abc plus retained patch",
        "--activity",
        "python -m pytest",
        "--result",
        "exit 0; 3 passed",
        *args,
        ok=ok,
    )


def test_ticket_capture_records_actual_file_and_provenance(feature):
    allocation = allocate(feature)
    destination = Path(allocation["destination"])
    assert destination.is_relative_to(feature / "evidence" / "ticket-25")
    (destination / "checks.log").write_bytes(b"3 passed\n")
    observed = register(feature, allocation)
    artifact = json.loads(Path(allocation["review_artifact"]).read_text())
    capture = artifact["captures"][0]
    assert observed["capture"] == capture
    assert capture["source_version"] == "commit:abc plus retained patch"
    assert capture["activity"] == "python -m pytest"
    assert capture["result"] == "exit 0; 3 passed"
    assert capture["kind"] == "original"
    assert capture["files"] == [
        {
            "path": str((destination / "checks.log").relative_to(feature)),
            "size": 9,
            "sha256": hashlib.sha256(b"3 passed\n").hexdigest(),
        }
    ]
    assert artifact["assessments"] == artifact["approvals"] == artifact["execution_results"] == []
    assert (feature / "issues" / "25-sample.md").read_text() == "# 25: Sample\n"


def test_shared_milestone_has_one_record_referenced_by_each_ticket(feature):
    allocation = allocate(
        feature, "--ticket", "26", "--shared", "capture-trials", "--milestone", "EC1"
    )
    destination = Path(allocation["destination"])
    assert destination.is_relative_to(feature / "evidence" / "capture-trials" / "EC1")
    (destination / "checks.log").write_text("shared original\n")
    register(feature, allocation)
    shared_path = Path(allocation["review_artifact"])
    shared = json.loads(shared_path.read_text())
    assert [ticket["issue"] for ticket in shared["scope"]["tickets"]] == [
        "issues/25-sample.md",
        "issues/26-sample.md",
    ]
    for number in ("25", "26"):
        local = json.loads(
            (feature / "evidence" / f"ticket-{number}" / "evidence-review.json").read_text()
        )
        assert local["shared_records"] == [str(shared_path.relative_to(feature))]
        assert local["captures"] == local["approvals"] == []


def test_parallel_producers_register_without_losing_captures_or_review_decisions(feature):
    first = allocate(feature)
    artifact = Path(first["review_artifact"])
    record = json.loads(artifact.read_text())
    record["approvals"] = [{"group": "old-file", "decision": "fixture approval"}]
    record["assessments"] = [{"id": "fixture assessment"}]
    record["execution_results"] = [{"state": "not executed"}]
    artifact.write_text(json.dumps(record))
    command = [sys.executable, "-m", "ticket_harness.evidence", "--feature", str(feature)]
    processes = [
        subprocess.Popen(
            command
            + [
                "allocate",
                "--ticket",
                "25",
                "--purpose",
                "parallel checks",
                "--producer",
                "worker",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        for _ in range(3)
    ]
    allocations = [first]
    for process in processes:
        stdout, stderr = process.communicate(timeout=30)
        assert process.returncode == 0, stdout + stderr
        allocations.append(json.loads(stdout))
    assert len({item["destination"] for item in allocations}) == 4
    processes = []
    for allocation in allocations:
        (Path(allocation["destination"]) / "checks.log").write_text("parallel passing checks\n")
        processes.append(
            subprocess.Popen(
                command
                + [
                    "register",
                    "--allocation",
                    allocation["allocation"],
                    "--file",
                    "checks.log",
                    "--source-version",
                    "fixture source",
                    "--activity",
                    "parallel check",
                    "--result",
                    "exit 0",
                ],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        )
    for process in processes:
        stdout, stderr = process.communicate(timeout=30)
        assert process.returncode == 0, stdout + stderr
    result = json.loads(artifact.read_text())
    assert len(result["captures"]) == 4
    for field in ("assessments", "approvals", "execution_results"):
        assert result[field] == record[field]
    assert all("approval" not in capture for capture in result["captures"])


def test_derived_summary_preserves_original_identity_and_idempotent_registration(feature):
    original = allocate(feature)
    path = Path(original["destination"]) / "checks.log"
    path.write_text("3 passed; detailed output\n")
    register(feature, original)
    derived = allocate(feature)
    (Path(derived["destination"]) / "checks.log").write_text("3 passed\n")
    args = ["--kind", "derived", "--derived-from", str(path.relative_to(feature))]
    capture = register(feature, derived, *args)["capture"]
    assert capture["kind"] == "derived"
    assert capture["derived_from"][0]["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert register(feature, derived, *args)["capture"] == capture
    artifact = json.loads(Path(derived["review_artifact"]).read_text())
    assert len(artifact["captures"]) == 2
    assert path.read_text() == "3 passed; detailed output\n"


def test_changed_original_or_registration_metadata_cannot_be_overwritten(feature):
    allocation = allocate(feature)
    path = Path(allocation["destination"]) / "checks.log"
    path.write_text("original\n")
    register(feature, allocation)
    artifact = Path(allocation["review_artifact"])
    saved = artifact.read_bytes()
    result = register(feature, allocation, "--result", "different result", ok=False)
    assert "cannot be overwritten" in result.stderr
    path.write_text("changed\n")
    result = register(feature, allocation, ok=False)
    assert "Registered original changed" in result.stderr
    assert artifact.read_bytes() == saved


@pytest.mark.parametrize("unsafe", ["../outside.log", "/tmp/outside.log", "./allocation.json"])
def test_payload_cannot_escape_or_register_allocation_metadata(feature, unsafe):
    allocation = allocate(feature)
    destination = Path(allocation["destination"])
    (destination / "checks.log").write_text("passing\n")
    artifact = Path(allocation["review_artifact"])
    before = artifact.read_bytes()
    result = register(feature, allocation, "--file", unsafe, ok=False)
    assert result.stderr
    assert artifact.read_bytes() == before


def test_declared_frozen_subtree_does_not_prevent_unrelated_ticket_capture(feature):
    frozen = feature / "evidence" / "ticket-26"
    frozen.mkdir(parents=True)
    original = frozen / "frozen.json"
    original.write_bytes(b"approved bytes")
    allocation = cli(
        feature,
        "--protect",
        str(frozen),
        "allocate",
        "--ticket",
        "25",
        "--purpose",
        "safe checks",
        "--producer",
        "worker",
    )
    (Path(allocation["destination"]) / "checks.log").write_text("passing\n")
    register(feature, allocation)
    rejection = cli(
        feature,
        "--protect",
        str(frozen),
        "allocate",
        "--ticket",
        "26",
        "--purpose",
        "unsafe checks",
        "--producer",
        "worker",
        ok=False,
    )
    assert "Protected destination" in rejection.stderr
    assert original.read_bytes() == b"approved bytes"
    assert not (frozen / "evidence-review.json").exists()


def test_new_freeze_at_registration_blocks_metadata_write(feature):
    allocation = allocate(feature)
    (Path(allocation["destination"]) / "checks.log").write_text("passing\n")
    artifact = Path(allocation["review_artifact"])
    saved = artifact.read_bytes()
    result = cli(
        feature,
        "--protect",
        str(artifact),
        "register",
        "--allocation",
        allocation["allocation"],
        "--file",
        "checks.log",
        "--source-version",
        "fixture",
        "--activity",
        "check",
        "--result",
        "exit 0",
        ok=False,
    )
    assert "Protected destination" in result.stderr
    assert artifact.read_bytes() == saved


@pytest.mark.parametrize("alias", ["symlink", "hardlink"])
def test_capture_rejects_aliases_into_protected_originals(feature, alias):
    allocation = allocate(feature)
    protected = feature / "spec.md"
    protected.write_text("approved input\n")
    path = Path(allocation["destination"]) / "checks.log"
    if alias == "symlink":
        path.symlink_to(protected)
    else:
        path.hardlink_to(protected)
    register(feature, allocation, ok=False)
    assert protected.read_text() == "approved input\n"


def test_symlinked_evidence_root_is_rejected_without_touching_target(feature, tmp_path):
    target = tmp_path / "frozen"
    target.mkdir()
    (feature / "evidence").symlink_to(target, target_is_directory=True)
    result = cli(
        feature,
        "allocate",
        "--ticket",
        "25",
        "--purpose",
        "checks",
        "--producer",
        "worker",
        ok=False,
    )
    assert "Symlink" in result.stderr
    assert list(target.iterdir()) == []


@pytest.mark.parametrize(
    "contents", ['{"schema_version":1,"schema_version":1}', "[]", '{"schema_version":99}']
)
def test_malformed_authoritative_metadata_is_preserved(feature, contents):
    folder = feature / "evidence" / "ticket-25"
    folder.mkdir(parents=True)
    artifact = folder / "evidence-review.json"
    artifact.write_text(contents)
    cli(
        feature,
        "allocate",
        "--ticket",
        "25",
        "--purpose",
        "checks",
        "--producer",
        "worker",
        ok=False,
    )
    assert artifact.read_text() == contents
    assert not (folder / "captures").exists()


def test_derived_capture_requires_originals_and_unknown_facts_are_explicit(feature):
    allocation = allocate(feature)
    (Path(allocation["destination"]) / "checks.log").write_text("unknown historical result\n")
    register(feature, allocation, "--kind", "derived", ok=False)
    result = register(feature, allocation, "--result", "unknown")
    assert result["capture"]["result"] == "unknown"


@pytest.mark.parametrize(
    "arguments",
    [
        ["--ticket", "99"],
        ["--ticket", "25", "--ticket", "25"],
        ["--ticket", "25", "--shared", "one-ticket"],
        ["--ticket", "25", "--milestone", "EC1"],
        ["--ticket", "25", "--ticket", "26", "--shared", ""],
        ["--ticket", "25", "--ticket", "26", "--shared", "capture-trials", "--milestone", ""],
        ["--ticket", "25", "--ticket", "26", "--shared", "../escape"],
        ["--ticket", "25", "--ticket", "26", "--shared", "ticket-25"],
    ],
)
def test_ambiguous_or_unsafe_scope_never_allocates_output(feature, arguments):
    cli(feature, "allocate", "--purpose", "checks", "--producer", "worker", *arguments, ok=False)
    assert not (feature / "evidence").exists()
