"""Finish the interrupted verifier without replaying its completed checks.

The original script and original partial outputs remain unchanged. This adapter
reuses only recorded successful checks after checking every original input hash.
Remaining commands execute through the original verifier into a new allocation.
"""
import hashlib
import json
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
original = folder / "captures/verification-71288fc1a1da4058830978bc454711dc"
identity = json.loads((original / "source-and-instructions.json").read_text())
assert all(hashlib.sha256((root / name).read_bytes()).hexdigest() == digest
           for name, digest in identity["files"].items()), "Original inputs changed"
completed = json.loads((original / "check-results.json").read_text())
assert [item["name"] for item in completed] == ["pytest", "mypy", "ruff"]
assert all(item["returncode"] == 0 for item in completed)
script = (folder / "25-verify-repair1.py").read_text()
script = script.replace('"--producer", "verification"', '"--producer", "verification-resume"')
start = script.index('run("pytest",')
end = script.index('run("format",', start)
script = script[:start] + '''
for previous in completed:
    results.append(previous | {"reused_from": str(original.relative_to(ROOT)),
        "identity_basis": "all original source/instruction hashes match before resume"})
(destination / "reuse-provenance.json").write_text(json.dumps({
    "original_capture": str(original.relative_to(ROOT)),
    "original_identity_sha256": hashlib.sha256((original / "source-and-instructions.json").read_bytes()).hexdigest(),
    "original_results_sha256": hashlib.sha256((original / "check-results.json").read_bytes()).hexdigest(),
    "reason": "Original process and terminal ended during format; confirmed absent on Forest203. No completed check replayed.",
    "completed": completed,
}, indent=2) + "\\n")
''' + script[end:]
script = script.replace('"25-verify.py: commands in check-results.json"',
                        '"25-resume-verification.py: remaining commands; first three checks reused with exact-input provenance"')
exec(compile(script, str(folder / "25-verify-repair1.py") + " [resumed]", "exec"))
