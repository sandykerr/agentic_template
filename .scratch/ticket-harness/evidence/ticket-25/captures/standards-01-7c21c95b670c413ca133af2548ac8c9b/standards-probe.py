"""Scoped public-CLI counterexamples; run on Forest with executable TMPDIR."""

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


OUTPUT = Path(__file__).resolve().parent
ROOT = Path.cwd()
observations = []


def command(argv, cwd=ROOT):
    result = subprocess.run(argv, cwd=cwd, text=True, capture_output=True)
    observations.append({"argv": argv, "cwd": str(cwd), "returncode": result.returncode,
                         "stdout": result.stdout, "stderr": result.stderr})
    return result


def make_feature(base, name):
    repository = base / name
    repository.mkdir()
    command(["git", "init", "-q", str(repository)])
    feature = repository / ".scratch" / "sample"
    issues = feature / "issues"
    issues.mkdir(parents=True)
    for number in ("25", "26"):
        (issues / f"{number}-sample.md").write_text(f"# {number}: Sample\n")
    return feature


def cli(feature, *args):
    return command([sys.executable, "-m", "ticket_harness.evidence", "--feature", str(feature), *args])


def allocate(feature, *args):
    return cli(feature, "allocate", "--ticket", "25", "--purpose", "standards probe",
               "--producer", "standards", *args)


def register(feature, allocation):
    return cli(feature, "register", "--allocation", allocation["allocation"],
               "--file", "checks.log", "--source-version", "standards disposable source",
               "--activity", "standards public CLI probe", "--result", "observed fixture")


with tempfile.TemporaryDirectory(prefix="ticket25-standards-") as temporary:
    base = Path(temporary)
    feature = make_feature(base, "empty-shared")
    first = allocate(feature, "--ticket", "26", "--shared", "")
    assert first.returncode == 0, first.stderr
    allocation = json.loads(first.stdout)
    artifact = json.loads(Path(allocation["review_artifact"]).read_text())
    observations.append({"case": "empty-shared", "allocation": allocation,
                         "artifact": artifact,
                         "ticket26_artifact_exists": (feature / "evidence" / "ticket-26" / "evidence-review.json").exists()})
    next_ticket = allocate(feature)
    assert next_ticket.returncode != 0, next_ticket.stdout

    feature = make_feature(base, "idempotent-retry")
    allocations = []
    for text in ("first original\n", "second original\n"):
        result = allocate(feature)
        assert result.returncode == 0, result.stderr
        allocation = json.loads(result.stdout)
        (Path(allocation["destination"]) / "checks.log").write_text(text)
        result = register(feature, allocation)
        assert result.returncode == 0, result.stderr
        allocations.append(allocation)
    second = Path(allocations[1]["destination"]) / "checks.log"
    second.write_text("changed second original\n")
    retry = register(feature, allocations[0])
    observations.append({"case": "idempotent-retry", "returncode": retry.returncode,
                         "second_current_sha256": hashlib.sha256(second.read_bytes()).hexdigest(),
                         "record": json.loads(Path(allocations[0]["review_artifact"]).read_text())})
    assert retry.returncode == 0, retry.stderr

with (OUTPUT / "standards-probe-results.json").open("x") as stream:
    json.dump({"source_head": command(["git", "rev-parse", "HEAD"]).stdout.strip(),
               "host": command(["hostname", "-s"]).stdout.strip(),
               "executable": sys.executable, "tmpdir": os.environ.get("TMPDIR"),
               "observations": observations}, stream, indent=2)
    stream.write("\n")
print("Both scoped counterexamples reproduced; full observations saved.")
