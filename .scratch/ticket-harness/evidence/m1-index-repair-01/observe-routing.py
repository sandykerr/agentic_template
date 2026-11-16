"""Fresh public-CLI observations; retained historical evidence is never rewritten."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "tests"))
from test_cli import TicketFixture  # noqa: E402

DESTINATION = Path(__file__).resolve().parent / "routing-observations"
DESTINATION.mkdir(exist_ok=False)


def digest(data):
    return hashlib.sha256(data).hexdigest()


source = {
    str(path.relative_to(ROOT)): digest(path.read_bytes())
    for pattern in ("ticket_harness/*.py", "tests/test*.py", "examples/scripted/*.py")
    for path in sorted(ROOT.glob(pattern))
}
(DESTINATION / "source.json").write_text(json.dumps(source, indent=2) + "\n")
observations = []
for mode in (
    "control",
    "caller-index",
    "foreign-dir",
    "foreign-worktree",
    "foreign-common-dir",
    "foreign-objects",
    "foreign-config",
    "namespace",
):
    fixture = TicketFixture()
    fixture.setUp()
    foreign = TicketFixture()
    foreign.setUp()
    saved = DESTINATION / mode
    saved.mkdir()
    try:
        index = fixture.repo / ".git/index"
        foreign_index = foreign.repo / ".git/index"
        before = index.read_bytes()
        foreign_before = foreign_index.read_bytes()
        delta = {
            "control": {},
            "caller-index": {"GIT_INDEX_FILE": str(index)},
            "foreign-dir": {"GIT_DIR": str(foreign.repo / ".git")},
            "foreign-worktree": {"GIT_WORK_TREE": str(foreign.repo)},
            "foreign-common-dir": {"GIT_COMMON_DIR": str(foreign.repo / ".git")},
            "foreign-objects": {"GIT_OBJECT_DIRECTORY": str(foreign.repo / ".git/objects")},
            "foreign-config": {
                "GIT_CONFIG_COUNT": "1",
                "GIT_CONFIG_KEY_0": "core.worktree",
                "GIT_CONFIG_VALUE_0": str(foreign.repo),
            },
            "namespace": {"GIT_NAMESPACE": "foreign"},
        }[mode]
        fixture.config_path.write_text(json.dumps(fixture.config))
        argv = [sys.executable, "-m", "ticket_harness", "run", "--config",
                str(fixture.config_path), "--output", str(fixture.output)]
        result = subprocess.run(argv, cwd=ROOT, env={**os.environ, **delta},
                                capture_output=True, check=False, timeout=30)
        after = index.read_bytes()
        foreign_after = foreign_index.read_bytes()
        (saved / "caller-index-before.bin").write_bytes(before)
        (saved / "caller-index-after.bin").write_bytes(after)
        (saved / "cli.stdout").write_bytes(result.stdout)
        (saved / "cli.stderr").write_bytes(result.stderr)
        record = fixture.record()
        observation = {
            "mode": mode, "argv": argv, "cwd": str(ROOT), "environment_delta": delta,
            "exit": result.returncode, "outcome": record["outcome"],
            "failure": record.get("failure"),
            "caller_index_before_sha256": digest(before),
            "caller_index_after_sha256": digest(after),
            "foreign_index_before_sha256": digest(foreign_before),
            "foreign_index_after_sha256": digest(foreign_after),
            "caller_head": fixture.git("rev-parse", "HEAD"), "base": fixture.base,
            "caller_index_value": fixture.git("show", ":value.txt"),
            "caller_working_value": (fixture.repo / "value.txt").read_text(),
            "foreign_head": foreign.git("rev-parse", "HEAD"), "foreign_base": foreign.base,
            "foreign_working_value": (foreign.repo / "value.txt").read_text(),
            "integration_value": fixture.git("show", "integration:value.txt"),
            "record": record,
        }
        assert before == after and foreign_before == foreign_after
        assert observation["caller_head"] == fixture.base
        assert observation["foreign_head"] == foreign.base
        assert observation["caller_working_value"] == "1\n"
        assert observation["foreign_working_value"] == "1\n"
        assert result.returncode == 0 and record["outcome"] == "completed"
        assert observation["integration_value"] == "2"
    finally:
        fixture.doCleanups()
        foreign.doCleanups()
    observation["fixture_cleanup_completed"] = not fixture.home.exists() and not foreign.home.exists()
    (saved / "observation.json").write_text(json.dumps(observation, indent=2) + "\n")
    observations.append({"mode": mode, "exit": result.returncode, "caller_index_preserved": before == after})

assert source == {name: digest((ROOT / name).read_bytes()) for name in source}
(DESTINATION / "summary.json").write_text(json.dumps(observations, indent=2) + "\n")
print(json.dumps(observations, indent=2))
