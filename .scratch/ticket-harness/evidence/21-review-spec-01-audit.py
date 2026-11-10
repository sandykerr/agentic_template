"""Read-only independent Spec identity/archive audit; no production imports."""

import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parent
SOURCE = "10b7050ec1fc06767e473b90217fa0d0bd100a0f"
BASELINE = "8574c6e5fb0a55ea3539e52c7c53044f1c036583"


def digest(data):
    return hashlib.sha256(data).hexdigest()


source = json.loads((EVIDENCE / "21-final-source.json").read_text())
for name, expected in source["files"].items():
    assert digest(subprocess.check_output(["git", "show", SOURCE + ":" + name])) == expected
    assert digest(Path(name).read_bytes()) == expected

instructions = json.loads((EVIDENCE / "21-review-round1-instructions.json").read_text())
for name, expected in instructions["instructions_and_packet_sha256"].items():
    assert digest(Path(name).read_bytes()) == expected

producer = json.loads((EVIDENCE / "21-checkpoint/producer.json").read_text())
assert producer["producer_head"] == BASELINE
for name, expected in producer["source_hashes"].items():
    assert digest(subprocess.check_output(["git", "show", BASELINE + ":" + name])) == expected

manifest = json.loads((EVIDENCE / "21-raw-manifest.json").read_text())
seen = set()
observations = {}
with tarfile.open(EVIDENCE / "21-final-raw.tar.gz", "r|gz") as archive:
    for entry in archive:
        if not entry.isfile():
            continue
        relative = entry.name.removeprefix("ticket21-final-raw/")
        data = archive.extractfile(entry).read()
        assert digest(data) == manifest[relative], relative
        seen.add(relative)
        if relative.endswith("/observations.json"):
            observation = json.loads(data)
            observations[observation["scenario"]] = relative
assert seen == set(manifest)

continuation = json.loads((EVIDENCE / "21-checkpoint/continuation.json").read_text())
prior, final = producer["record"], continuation["final"]
assert prior["outcome"] == "stopped_at_qa"
assert final["attempts"][:len(prior["attempts"])] == prior["attempts"]
assert final["gates"][:len(prior["gates"])] == prior["gates"]
assert final["outcome"] == "completed" and final["feature_complete"]
assert len(final["qa_decisions"]) == 2
assert sum(gate["stage"] == "baseline" for gate in final["gates"]) == 1

print(json.dumps({
    "baseline": BASELINE,
    "source": SOURCE,
    "source_and_working_files_matched": len(source["files"]),
    "instruction_hashes_matched": len(instructions["instructions_and_packet_sha256"]),
    "producer_baseline_files_matched": len(producer["source_hashes"]),
    "archived_files_matched": len(seen),
    "archived_scenarios": len(observations),
    "prior_attempts_preserved": len(prior["attempts"]),
    "prior_gates_preserved": len(prior["gates"]),
    "checkpoint_final_outcome": final["outcome"],
    "limits": "Identity/record consistency audit, not a runtime or architecture guarantee.",
}, indent=2))
