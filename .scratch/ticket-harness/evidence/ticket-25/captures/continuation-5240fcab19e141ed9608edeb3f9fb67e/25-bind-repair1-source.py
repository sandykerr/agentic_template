"""Bind actual verification file hashes to the committed implementation."""
import hashlib
import json
import subprocess
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
capture = folder / "captures/verification-resume-44c46221b60444d4b2ff2512e4603e48"
identity = json.loads((capture / "source-and-instructions.json").read_text())
revision = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
committed = {}
supplied = {}
for name, digest in identity["files"].items():
    result = subprocess.run(["git", "show", f"{revision}:{name}"], capture_output=True)
    current = hashlib.sha256((root / name).read_bytes()).hexdigest()
    entry = {"tested_sha256": digest, "current_sha256": current, "worktree_matches": digest == current}
    if result.returncode == 0 and hashlib.sha256(result.stdout).hexdigest() == digest:
        committed[name] = entry | {"commit_matches": True}
    else:
        supplied[name] = entry | {"reason": "preexisting supplied uncommitted instructions/planning input; preserved snapshots or starting patch"}
checks = json.loads((capture / "check-results.json").read_text())
result = {"baseline": "2c01fe9fe04c78fa10a2dac11e94826876467562", "implementation_revision": revision,
          "tested_parent_head": identity["head"], "committed": committed, "supplied_inputs": supplied,
          "checks": checks, "all_source_matches": all(item["worktree_matches"] for item in [*committed.values(), *supplied.values()]),
          "all_checks_passed": all(item["returncode"] == 0 for item in checks)}
print(json.dumps(result, indent=2))
raise SystemExit(not (result["all_source_matches"] and result["all_checks_passed"]))
