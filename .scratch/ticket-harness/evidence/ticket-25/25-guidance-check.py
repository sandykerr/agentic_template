"""Actual scoped link/routing checks plus shared capture for the EC1 handoff."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

root = Path.cwd()
feature = root / ".scratch/ticket-harness"
python = str(root / ".venv/bin/python")
base = [python, "-m", "ticket_harness.evidence", "--feature", str(feature)]
allocation = json.loads(subprocess.check_output(base + ["allocate", "--ticket", "25", "--ticket", "26", "--shared", "evidence-capture-workflow", "--milestone", "EC1", "--purpose", "Shared capture guidance validation and provenance for EC1 tickets 25 and 26", "--producer", "guidance"], text=True))
destination = Path(allocation["destination"])
files = [root / ".agents/skills/custom/capture-evidence/SKILL.md", root / "docs/agents/evidence-capture.md",
         root / "docs/agents/testing.md", root / "docs/agents/review-records.md", root / ".agents/skills/custom/implement-with-checkboxes/SKILL.md"]
checked = []
failures = []
for source in files:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text()):
        if "://" in target:
            continue
        path, _, anchor = target.partition("#")
        resolved = (source.parent / path).resolve() if path else source
        exists = resolved.exists()
        checked.append({"source": str(source.relative_to(root)), "target": target, "exists": exists})
        if not exists:
            failures.append(checked[-1])
        if anchor and exists and resolved.suffix == ".md":
            headings = [re.sub(r"[^\w\s-]", "", line.lstrip("# ").lower()).replace(" ", "-") for line in resolved.read_text().splitlines() if line.startswith("#")]
            if anchor not in headings:
                failures.append({"source": str(source), "target": target, "reason": "missing anchor"})
for source in files[2:]:
    if "capture-evidence/SKILL.md" not in source.read_text():
        failures.append({"routing": str(source), "reason": "capture skill not reachable"})
identity = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
result = {"activity": "25-guidance-check.py", "link_count": len(checked), "links": checked,
          "routing": "implementation, testing, review guidance reach capture-evidence",
          "source_files": identity, "failures": failures, "result": "passed" if not failures else "failed",
          "limits": "Scoped path/anchor/routing validation; not independent behavior review or EC1 acceptance"}
(destination / "guidance-validation.json").write_text(json.dumps(result, indent=2) + "\n")
args = base + ["register", "--allocation", allocation["allocation"], "--file", "guidance-validation.json", "--source-version", "HEAD " + subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip() + "; source_files hashes in capture", "--activity", "25-guidance-check.py: scoped path/anchor/routing validation", "--result", result["result"]]
registered = subprocess.run(args, text=True, capture_output=True)
print(json.dumps({"allocation": allocation, "link_count": len(checked), "failures": failures, "registration_returncode": registered.returncode, "stderr": registered.stderr}), flush=True)
raise SystemExit(bool(failures) or registered.returncode)
