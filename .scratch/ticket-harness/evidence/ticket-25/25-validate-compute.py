"""Validate the explicitly requested persistent compute-session skill update."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

root = Path.cwd()
folder = root / ".agents/skills/custom/adapt-compute"
files = [folder / "SKILL.md", folder / "references/forest.md", folder / "references/slurm.md"]
results = []
for file in files:
    content = file.read_text()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        path = (file.parent / target.partition("#")[0]).resolve()
        results.append({"source": str(file.relative_to(root)), "link": target, "ok": path.exists()})
    for index, script in enumerate(re.findall(r"```bash\n(.*?)```", content, re.S), 1):
        run = subprocess.run(["bash", "-n"], input=script, text=True, capture_output=True)
        results.append({"source": str(file.relative_to(root)), "bash_block": index,
                        "returncode": run.returncode, "stderr": run.stderr, "ok": run.returncode == 0})
validator = "/panfs/ccds02/nobackup/people/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
run = subprocess.run([sys.executable, validator, str(folder)], text=True, capture_output=True)
results.append({"activity": "quick_validate.py", "returncode": run.returncode,
                "stdout": run.stdout, "stderr": run.stderr, "ok": run.returncode == 0})
result = {"source": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
          "results": results, "ok": all(item["ok"] for item in results),
          "actual_session_example": "Forest203 persistent SSH session 10089; repeated commands confirmed host/checkout/architecture/capacity",
          "limits": "Documentation/skill validation and actual Forest session reuse; no Slurm job requested or runtime allocation test claimed"}
print(json.dumps(result, indent=2))
raise SystemExit(not result["ok"])
