"""Scoped public-CLI observations for architecture review; no product mutation."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path.cwd()


def command(feature, *args):
    result = subprocess.run(
        [sys.executable, "-m", "ticket_harness.evidence", "--feature", str(feature), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return {"argv": result.args, "exit": result.returncode, "stdout": result.stdout, "stderr": result.stderr}


def allocate(feature, *args):
    return command(feature, "allocate", "--ticket", "25", "--purpose", "architecture probe", "--producer", "probe", *args)


def register(feature, allocation):
    return command(feature, "register", "--allocation", allocation["allocation"], "--file", "result.txt", "--source-version", "probe fixture", "--activity", "scoped CLI observation", "--result", "fixture payload")


observations = []
with tempfile.TemporaryDirectory(prefix="ticket25-architecture-") as temporary:
    repository = Path(temporary)
    subprocess.run(["git", "init", "-q", str(repository)], check=True)
    for case in ("empty-shared", "empty-milestone", "retry-prior"):
        feature = repository / ".scratch" / case
        (feature / "issues").mkdir(parents=True)
        for number in ("25", "26"):
            (feature / "issues" / f"{number}-sample.md").write_text(f"# {number}: Sample\n")
        if case == "empty-shared":
            first = allocate(feature, "--ticket", "26", "--shared", "")
            ordinary = allocate(feature)
            observations.append({"case": case, "allocation": first, "ordinary_after": ordinary,
                "ticket26_link_created": (feature / "evidence" / "ticket-26" / "evidence-review.json").exists(),
                "artifact": json.loads((feature / "evidence" / "ticket-25" / "evidence-review.json").read_text())})
        elif case == "empty-milestone":
            first = allocate(feature, "--ticket", "26", "--shared", "shared-evidence", "--milestone", "")
            second = allocate(feature, "--ticket", "26", "--shared", "shared-evidence")
            observations.append({"case": case, "allocation": first, "unscoped_after": second})
        else:
            first = json.loads(allocate(feature)["stdout"])
            second = json.loads(allocate(feature)["stdout"])
            for allocation in (first, second):
                (Path(allocation["destination"]) / "result.txt").write_text("original\n")
                result = register(feature, allocation)
                if result["exit"]:
                    raise RuntimeError(result)
            artifact = Path(first["review_artifact"])
            before = artifact.read_bytes()
            (Path(second["destination"]) / "result.txt").write_text("changed after registration\n")
            retry_first = register(feature, first)
            retry_second = register(feature, second)
            observations.append({"case": case, "retry_first": retry_first, "retry_second": retry_second,
                "authoritative_record_unchanged": artifact.read_bytes() == before})
print(json.dumps(observations, indent=2))
