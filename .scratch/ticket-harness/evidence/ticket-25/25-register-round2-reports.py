"""Preserve external identities and register three independent original reports."""
import hashlib
import json
import subprocess
from pathlib import Path

root = Path.cwd()
folder = root / ".scratch/ticket-harness/evidence/ticket-25"
base = [str(root / ".venv/bin/python"), "-m", "ticket_harness.evidence",
        "--feature", str(root / ".scratch/ticket-harness")]
revision = "febd86321851e2acec994237f9d1a1adea824c55"
records = []
for role, producer in [
    ("Spec", "spec-02-5900732a47de41b589f24b1257f5be7b"),
    ("Standards", "standards-02-fb83db1963cc4831bb95ec2576576f03"),
    ("Broader architecture Standards", "architecture-02-4332dc4df4614538b4444cf6a932e3db"),
]:
    destination = folder / "captures" / producer
    report = destination / "report.md"
    content = report.read_bytes()
    assert revision in content.decode(), f"Missing assessed revision: {report}"
    records.append({"role": role, "report": str(report.relative_to(root)),
                    "sha256": hashlib.sha256(content).hexdigest()})
with (folder / "25-review-round2-digests.sha256").open("x") as output:
    output.writelines(f"{record['sha256']}  {record['report']}\n" for record in records)
for record in records:
    report = root / record["report"]
    result = subprocess.run(base + ["register", "--allocation", str(report.parent / "allocation.json"),
        "--file", "report.md", "--source-version", revision,
        "--activity", f"Fresh independent {record['role']} source review from original ticket baseline 2c01fe9fe04c78fa10a2dac11e94826876467562",
        "--result", "Completed; zero new blocking/optional findings; original relevant full finding keys independently verified corrected at assessed revision. Original report contains substantive reasoning and evidence limits."],
        capture_output=True, text=True)
    record.update(returncode=result.returncode, stdout=result.stdout, stderr=result.stderr)
    assert result.returncode == 0, result.stderr
with (folder / "25-review-round2-registration.json").open("x") as output:
    json.dump(records, output, indent=2)
print(json.dumps([{key: value for key, value in record.items() if key != "stdout"} for record in records]))
