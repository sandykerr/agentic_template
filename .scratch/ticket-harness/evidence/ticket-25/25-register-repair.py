"""Register immutable focused repair observations and the original worker report."""
import json
import shutil
import subprocess
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
allocation = json.loads((folder / "25-repair1-allocation.json").read_text())
destination = Path(allocation["destination"])
for source, target in ((folder / "25-repair1-report.md", destination / "report.md"),
                       (folder / "25-repair-check.py", destination / "check-driver.py")):
    with target.open("xb") as stream:
        stream.write(source.read_bytes())
files = [path.name for path in sorted(destination.iterdir()) if path.is_file() and path.name != "allocation.json"]
command = [str(root / ".venv/bin/python"), "-m", "ticket_harness.evidence", "--feature", str(root / ".scratch/ticket-harness"),
           "register", "--allocation", allocation["allocation"],
           *[arg for name in files for arg in ("--file", name)],
           "--source-version", "Multiple states retained in per-check identity JSON/source snapshots; final evidence.py SHA256 8040d512b43380678f4c6baae419ab37763c468c0190ac08dd7be3b1f04d7187; test SHA256 3aa908b3c9c50ef5f490196d9a69f1fb5e54d8e0822a9de79a6c898acd5545ac",
           "--activity", "/root/repair25_1 Medium repair; parent actual Forest203 red/green/static commands",
           "--result", "Scope red2fail/6pass; scope green10pass; retry red1fail; complete capture green26pass; mypy/lint/format/whitespace exit0; final full/independent gates pending"]
result = subprocess.run(command, text=True, capture_output=True)
print(json.dumps({"returncode": result.returncode, "stderr": result.stderr, "file_count": len(files), "destination": str(destination)}, indent=2))
raise SystemExit(result.returncode)
