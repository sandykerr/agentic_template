"""Capture one scoped repair check through the public helper, preserving each state."""
import hashlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
allocation_path = folder / "25-repair1-allocation.json"
base = [str(root / ".venv/bin/python"), "-m", "ticket_harness.evidence", "--feature", str(root / ".scratch/ticket-harness")]
if allocation_path.exists():
    allocation = json.loads(allocation_path.read_text())
else:
    allocation = json.loads(subprocess.check_output(base + ["allocate", "--ticket", "25", "--purpose", "Repair1 focused red/green checks with exact per-command source states", "--producer", "repair1"], text=True))
    with allocation_path.open("x") as stream:
        json.dump(allocation, stream, indent=2)
        stream.write("\n")
destination = Path(allocation["destination"])
name = sys.argv[1]
command = sys.argv[2:]
identity = {"host": platform.node(), "architecture": platform.machine(), "checkout": str(root),
            "head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
            "argv": command, "tmpdir": os.environ.get("TMPDIR"), "source_files": {}}
for label, path in (("evidence.py", root / "ticket_harness/evidence.py"), ("test_evidence.py", root / "tests/test_evidence.py")):
    content = path.read_bytes()
    identity["source_files"][str(path.relative_to(root))] = hashlib.sha256(content).hexdigest()
    (destination / f"{name}.{label}").write_bytes(content)
with (destination / f"{name}.identity.json").open("x") as stream:
    json.dump(identity, stream, indent=2)
    stream.write("\n")
with (destination / f"{name}.stdout").open("xb") as out, (destination / f"{name}.stderr").open("xb") as err:
    result = subprocess.run(command, stdout=out, stderr=err)
summary = {"name": name, "returncode": result.returncode, "destination": str(destination), "argv": command}
with (destination / f"{name}.result.json").open("x") as stream:
    json.dump(summary, stream, indent=2)
    stream.write("\n")
print(json.dumps(summary))
raise SystemExit(result.returncode)
