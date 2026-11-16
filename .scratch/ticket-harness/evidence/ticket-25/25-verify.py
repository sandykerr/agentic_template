"""Capture actual ticket25 final verification using the public development helper."""
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path.cwd()
FEATURE = ROOT / ".scratch/ticket-harness"
PYTHON = str(ROOT / ".venv/bin/python")
BASE = [PYTHON, "-m", "ticket_harness.evidence", "--feature", str(FEATURE)]
allocation = json.loads(subprocess.check_output(BASE + ["allocate", "--ticket", "25", "--purpose",
    "Final implementation verification with actual commands, source identities and results", "--producer", "verification"], text=True))
destination = Path(allocation["destination"])
print(json.dumps(allocation), flush=True)
paths = sorted([*ROOT.glob("ticket_harness/*.py"), *ROOT.glob("tests/*.py"), ROOT / "pyproject.toml",
    ROOT / "requirements-uv.txt", ROOT / "AGENTS.md", ROOT / "GLOSSARY.md",
    *ROOT.glob("docs/agents/*.md"), *ROOT.glob("docs/adr/*.md"),
    FEATURE / "spec.md", FEATURE / "evidence-policy.md", FEATURE / "milestones.md",
    FEATURE / "issues/25-guide-ticket-and-shared-evidence-creation.md",
    ROOT / ".agents/skills/custom/capture-evidence/SKILL.md",
    ROOT / ".agents/skills/custom/implement-with-checkboxes/SKILL.md",
    ROOT / ".agents/skills/custom/test-strategy/SKILL.md"])
identity = {
    "host": platform.node(), "architecture": platform.machine(), "checkout": str(ROOT),
    "head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    "dirty_status": subprocess.check_output(["git", "status", "--short"], text=True),
    "files": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    "environment": subprocess.check_output([PYTHON, "-m", "pip", "freeze"], text=True),
    "concurrency": {k: os.environ[k] for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")},
}
(destination / "source-and-instructions.json").write_text(json.dumps(identity, indent=2) + "\n")
results = []

def run(name, argv, *, env=None, cwd=ROOT):
    with (destination / f"{name}.stdout").open("xb") as out, (destination / f"{name}.stderr").open("xb") as err:
        completed = subprocess.run(argv, cwd=cwd, env=env, stdout=out, stderr=err)
    result = {"name": name, "argv": argv, "cwd": str(cwd), "returncode": completed.returncode}
    results.append(result)
    (destination / "check-results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    return completed.returncode

# Single full suite, retaining new capture CLI/JSON observations at teardown.
env = os.environ | {"TICKET_HARNESS_TEST_OBSERVATIONS": str(destination / "observations")}
run("pytest", [PYTHON, "-m", "pytest"], env=env)
run("mypy", [PYTHON, "-m", "mypy"])
run("ruff", [PYTHON, "-m", "ruff", "check", "ticket_harness", "tests", "examples"])
run("format", [PYTHON, "-m", "ruff", "format", "--check", "ticket_harness", "tests", "examples"])
run("whitespace", ["git", "diff", "--check"])
validator = "/panfs/ccds02/nobackup/people/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
run("skill-validation", [PYTHON, validator, str(ROOT / ".agents/skills/custom/capture-evidence")])
with tempfile.TemporaryDirectory(prefix="ticket25-installed-") as temp:
    wheel = Path(temp) / "wheels"
    target = Path(temp) / "installed"
    run("wheel", [PYTHON, "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "--wheel-dir", str(wheel), "."])
    wheels = list(wheel.glob("*.whl"))
    if wheels:
        run("install", [PYTHON, "-m", "pip", "install", "--no-deps", "--no-index", "--target", str(target), str(wheels[0])])
        installed_env = os.environ | {"PYTHONPATH": str(target)}
        run("installed-capture-help", [PYTHON, "-m", "ticket_harness.evidence", "--help"], env=installed_env, cwd=Path(temp))
        run("installed-harness-help", [str(target / "bin/ticket-harness"), "--help"], env=installed_env, cwd=Path(temp))
        installed = target / "ticket_harness/evidence.py"
        results.append({"name": "installed-source-identity", "returncode": 0 if installed.read_bytes() == (ROOT / "ticket_harness/evidence.py").read_bytes() else 1,
            "sha256": hashlib.sha256(installed.read_bytes()).hexdigest()})
# Bind the retained source hash set again after checks; no changing final source.
changed = [name for name, digest in identity["files"].items() if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest]
results.append({"name": "source-unchanged", "returncode": int(bool(changed)), "changed": changed})
(destination / "check-results.json").write_text(json.dumps(results, indent=2) + "\n")
files = [str(path.relative_to(destination)) for path in sorted(destination.rglob("*")) if path.is_file() and not path.is_symlink() and path.name != "allocation.json"]
args = [arg for name in files for arg in ("--file", name)]
source = "HEAD " + identity["head"] + "; source-and-instructions.json sha256:" + hashlib.sha256((destination / "source-and-instructions.json").read_bytes()).hexdigest()
status = "all passed" if all(r["returncode"] == 0 for r in results) else "failures; see check-results.json"
# Some negative fixtures intentionally retain symlinks/hardlinks; these are observed
# test fixture content, not new evidence payloads. Register standalone check files
# and the JSON scenario artifacts/transcripts; the copied alias fixtures remain
# inspectable and are described by pytest results.
safe_files = [name for name in files if (destination / name).stat().st_nlink == 1]
args = [arg for name in safe_files for arg in ("--file", name)]
registered = subprocess.run(BASE + ["register", "--allocation", allocation["allocation"], *args,
    "--source-version", source, "--activity", "25-verify.py: commands in check-results.json", "--result", status], text=True, capture_output=True)
print("registration", registered.returncode, registered.stderr, flush=True)
(destination / "registration-result.txt").write_text(str(registered.returncode) + "\n" + registered.stderr)
sys.exit(int(status != "all passed" or registered.returncode != 0))
