"""The minimal one-ticket input contract; general preflight belongs to ticket 02."""

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from ticket_harness.records import GateFailure


def load(config_path: Path, output: Path) -> tuple[dict[str, Any], dict[str, Any], str]:
    config = json.loads(config_path.read_text())
    repository = (config_path.parent / config["repository"]).resolve()
    config["repository"] = str(repository)
    if output == repository or repository in output.parents:
        raise GateFailure("Run output must be outside the target repository")
    paths = {
        "configuration": config_path,
        "spec": repository / config["spec"],
        "ticket": repository / config["ticket"],
    }
    for index, path in enumerate(config["standards"]):
        paths[f"standards-{index}"] = repository / path
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
    ticket = Path(snapshots["ticket"]["artifact"]).read_text()
    title = re.search(r"^# (\d+): .+", ticket, re.MULTILINE)
    if not title or not re.search(r"^\*\*Status:\*\* ready-for-agent\s*$", ticket, re.MULTILINE):
        raise GateFailure("Expected '# NN: Title' and '**Status:** ready-for-agent'")
    if not re.search(r"^\*\*Blocked by:\*\* None\s*$", ticket, re.MULTILINE):
        raise GateFailure("This slice accepts only one ticket with no prerequisites")
    if not config["checks"] or not config["suite"] or not config["agent"]:
        raise GateFailure("Configure an agent, suite, and at least one ticket check")
    return config, snapshots, title.group(1)
