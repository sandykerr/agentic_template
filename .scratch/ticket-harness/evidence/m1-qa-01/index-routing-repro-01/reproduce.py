"""Bounded public-CLI observation; never imports production private owners."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile

from test_cli import ROOT, TicketFixture

DESTINATION = Path(__file__).resolve().parent
SOURCE = "d02e61ea27de4febd17e337bd51529d07861226b"


def digest(data):
    return hashlib.sha256(data).hexdigest()


observations = []
for mode in ("control", "caller-index"):
    saved = DESTINATION / mode
    saved.mkdir(exist_ok=False)
    fixture = TicketFixture()
    fixture.setUp()
    try:
        index = fixture.repo / ".git/index"
        before = index.read_bytes()
        (saved / "caller-index-before.bin").write_bytes(before)
        before_status = fixture.git("status", "--porcelain")
        fixture.config_path.write_text(json.dumps(fixture.config))
        environment = dict(os.environ)
        if mode == "caller-index":
            environment["GIT_INDEX_FILE"] = str(index)
        argv = [sys.executable, "-m", "ticket_harness", "run", "--config",
                str(fixture.config_path), "--output", str(fixture.output)]
        result = subprocess.run(argv, cwd=ROOT, env=environment,
                                capture_output=True, timeout=30, check=False)
        after = index.read_bytes()
        (saved / "caller-index-after.bin").write_bytes(after)
        (saved / "cli.stdout").write_bytes(result.stdout)
        (saved / "cli.stderr").write_bytes(result.stderr)
        (saved / "configuration.json").write_bytes(fixture.config_path.read_bytes())
        (saved / "run.json").write_bytes((fixture.output / "run.json").read_bytes())
        record = fixture.record()
        observation = {
            "mode": mode, "source": SOURCE, "argv": argv, "cwd": str(ROOT),
            "fixture_home": str(fixture.home),
            "environment_delta": {"GIT_INDEX_FILE": str(index)} if mode == "caller-index" else {},
            "qa_request": "not applicable: existing legacy single-ticket public CLI fixture",
            "exit": result.returncode, "outcome": record["outcome"],
            "failure": record.get("failure"),
            "before_index_sha256": digest(before), "after_index_sha256": digest(after),
            "before_caller_status": before_status,
            "after_caller_status": fixture.git("status", "--porcelain"),
            "after_index_value": fixture.git("show", ":value.txt"),
            "after_working_value": (fixture.repo / "value.txt").read_text(),
            "caller_head": fixture.git("rev-parse", "HEAD"), "initial_base": fixture.base,
            "integration_unchanged": fixture.git("rev-parse", "integration") == fixture.base,
            "gates": [{"stage": gate["stage"], "passed": gate["passed"],
                       "verification_status": gate.get("verification_status")}
                      for gate in record["gates"]],
            "cleanup": "pending; fixture-owned /tmp repository and run only",
        }
        with tarfile.open(saved / "raw-fixture.tar.gz", "w:gz") as archive:
            archive.add(fixture.home, arcname="fixture", recursive=True)
    finally:
        fixture.doCleanups()
    observation["cleanup"] = "completed; fixture.doCleanups removed isolated /tmp home"
    observation["fixture_home_exists_after_cleanup"] = fixture.home.exists()
    (saved / "observation.json").write_text(json.dumps(observation, indent=2) + "\n")
    observations.append(observation)

manifest = {}
for path in sorted(DESTINATION.rglob("*")):
    if path.is_file():
        manifest[str(path.relative_to(DESTINATION))] = digest(path.read_bytes())
(DESTINATION / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps(observations, indent=2))
