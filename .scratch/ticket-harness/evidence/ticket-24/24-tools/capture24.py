"""Lossless observation capture before existing fixture-owned cleanup, no test changes."""
import hashlib
import json
import os
import shutil
from pathlib import Path

import pytest

_current = "unknown"


def pytest_runtest_setup(item):
    global _current
    _current = item.nodeid


def pytest_configure(config):
    from test_cli import TicketFixture

    original = TicketFixture.doCleanups
    original_cli = TicketFixture.cli

    def cli(self, *args):
        result = original_cli(self, *args)
        if not hasattr(self, "_evidence_cli"):
            self._evidence_cli = []
        self._evidence_cli.append({
            "command": result.args,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        })
        return result

    TicketFixture.cli = cli

    def capture(self):
        try:
            record_path = self.output / "run.json"
            if record_path.exists():
                target = Path(os.environ["TICKET24_RAW"]) / self.home.name
                if not target.exists():
                    target.mkdir(parents=True)
                    record = self.record()
                    status = self.cli("status", self.output)
                    assert status.returncode == 0
                    assert json.loads(status.stdout) == record
                    observations = {
                        "scenario": _current,
                        "record": record,
                        "status": {"exit_code": status.returncode, "stdout": status.stdout, "stderr": status.stderr},
                        "cli": getattr(self, "cli_observations", []),
                        "public_cli_results": getattr(self, "_evidence_cli", []),
                        "foreground": getattr(self, "foreground_observations", []),
                        "caller_status": self.git("status", "--porcelain"),
                        "refs": self.git("show-ref"),
                        "history": self.git("log", "--all", "--format=%H %P %s"),
                    }
                    for name in ("artifacts", "inputs", "checkpoints", "rejections"):
                        path = self.output / name
                        if path.exists():
                            shutil.copytree(path, target / name)
                    for path in self.output.glob("*.json"):
                        shutil.copyfile(path, target / path.name)
                    (target / "observations.json").write_text(json.dumps(observations, indent=2) + "\n")
        finally:
            original(self)

    TicketFixture.doCleanups = capture
