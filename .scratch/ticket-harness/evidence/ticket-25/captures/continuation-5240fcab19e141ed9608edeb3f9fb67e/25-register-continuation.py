"""Register actual interrupted check evidence and continuation identities."""
import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
base = [str(root / ".venv/bin/python"), "-m", "ticket_harness.evidence",
        "--feature", str(root / ".scratch/ticket-harness")]
original = folder / "captures/verification-71288fc1a1da4058830978bc454711dc"
with tarfile.open(original / "observations.tar.gz", "x:gz") as archive:
    archive.add(original / "observations", arcname="observations")
files = [p.name for p in sorted(original.iterdir())
         if p.is_file() and p.name != "allocation.json" and p.stat().st_nlink == 1]
result = subprocess.run(base + ["register", "--allocation", str(original / "allocation.json"),
    *[arg for name in files for arg in ("--file", name)],
    "--source-version", "febd86321851e2acec994237f9d1a1adea824c55; original source-and-instructions.json hashes match committed product and supplied instruction inputs",
    "--activity", "25-verify-repair1.py: completed pytest/mypy/lint before process ended during formatting",
    "--result", "589 passed in 813.40s; mypy/lint exit0. Formatting interrupted with no recorded exit; remaining gates not run here. Completed in separate exact-input resume capture."],
    capture_output=True, text=True)
with (folder / "25-interrupted-verification-registration.json").open("x") as output:
    json.dump({"returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}, output, indent=2)
assert result.returncode == 0, result.stderr
allocation = json.loads(subprocess.check_output(base + ["allocate", "--ticket", "25",
    "--purpose", "Continuation verification recovery scripts and committed source binding",
    "--producer", "continuation"], text=True))
destination = Path(allocation["destination"])
names = ["25-resume-verification.py", "25-bind-repair1-source.py",
         "25-repair1-committed-source-binding.json", "25-register-continuation.py",
         "25-review-round2-context.md", "25-resume-driver.log",
         "25-interrupted-verification-registration.json"]
for name in names:
    with (destination / name).open("xb") as output:
        output.write((folder / name).read_bytes())
manifest = {name: hashlib.sha256((destination / name).read_bytes()).hexdigest() for name in names}
with (destination / "manifest.json").open("x") as output:
    json.dump(manifest, output, indent=2)
result = subprocess.run(base + ["register", "--allocation", allocation["allocation"],
    *[arg for name in [*names, "manifest.json"] for arg in ("--file", name)],
    "--source-version", "febd86321851e2acec994237f9d1a1adea824c55; 25-repair1-committed-source-binding.json distinguishes supplied instructions",
    "--activity", "25-register-continuation.py: preserve recovery adapters, original registration and exact-input binding",
    "--result", "All final checks passed using recorded exact-input pytest/mypy/lint plus remaining checks in separate resumed capture; original interruption retained"],
    capture_output=True, text=True)
with (folder / "25-continuation-registration.json").open("x") as output:
    json.dump({"allocation": allocation, "returncode": result.returncode,
               "stdout": result.stdout, "stderr": result.stderr}, output, indent=2)
assert result.returncode == 0, result.stderr
print(json.dumps({"allocation": allocation, "returncode": result.returncode}))
