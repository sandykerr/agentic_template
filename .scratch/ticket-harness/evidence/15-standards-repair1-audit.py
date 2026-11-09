"""Independent Standards audit of retained repaired-source verification."""

import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path.cwd()
EVIDENCE = ROOT / ".scratch/ticket-harness/evidence"
BASELINE = "90255aaf6faf9aedce18f7159093f5dbfde294b7"
HEAD = "d11f0bc60a2c11c40683e58581dffa10e36a91be"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((EVIDENCE / name).read_text())


assert subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip() == HEAD
identity = read("15-repair1-final-source-identity.json")["sha256"]
assert len(identity) == 23
for name, expected in identity.items():
    assert sha(ROOT / name) == expected, name
    committed = subprocess.check_output(["git", "show", f"{HEAD}:{name}"])
    assert hashlib.sha256(committed).hexdigest() == expected, name

checks = read("15-repair1-check-results.json")["checks"]
assert len(checks) == 10
for name, check in checks.items():
    assert check["exit_code"] == 0, name
    capture = read(check["source_identity"])
    assert capture["sha256"] == identity, name
    result_name = check["source_identity"].replace("-source.json", "-result.json")
    result = read(result_name)
    assert result["exit_code"] == 0 and result["command"] == check["command"], name
    assert sha(EVIDENCE / check["log"]) == check["log_sha256"], name
staged = read(checks["actual-staged-whitespace"]["source_identity"])["status"]
assert "M  tests/test_continuation.py\n" in staged
assert "M  ticket_harness/runner.py\n" in staged
assert "544 passed in 910.17s" in (EVIDENCE / checks["suite"]["log"]).read_text()
assert "Success: no issues found" in (EVIDENCE / checks["mypy"]["log"]).read_text()
assert "strict = true" in (ROOT / "pyproject.toml").read_text()

rows = read("15-repair1-fixture-observations.json")["observations"]
assert len(rows) == 123
for row in rows:
    assert sha(EVIDENCE / row["raw_file"]) == row["raw_sha256"], row["scenario"]
    raw = read(row["raw_file"])
    assert row["scenario"] == raw["scenario"]
    assert row["outcome"] == raw["record"]["outcome"]
raw_hashes = read("15-repair1-raw-artifact-hashes.json")
for name, expected in raw_hashes.items():
    assert sha(EVIDENCE / name) == expected, name

archives = 0
verified_links = 0
decisions = 0
for row in rows:
    scenario = row["scenario"]
    if scenario not in {
        "test_clean_qa_stop_continues_in_new_process_without_replaying_done_work",
        "test_repeated_stops_retain_previous_decisions_and_checkpoint_lineage",
        "test_continued_run_records_invalidation_of_earlier_verified_source",
    }:
        continue
    raw = read(row["raw_file"])
    record = raw["record"]
    retained = EVIDENCE / row["retained_run_files"]
    original_output = Path(record["artifacts"]).parent
    for path in (retained / "checkpoints").glob("*.json"):
        checkpoint = json.loads(path.read_text())
        assert path.stem == checkpoint["record"]["checkpoint_id"]
        for name, expected in checkpoint["evidence"].items():
            assert sha(retained / Path(name).relative_to(original_output)) == expected
        assert any(
            sha(request) == checkpoint["request_sha256"]
            for request in (retained / "artifacts").glob("*qa-request.json")
        )
        for item, _, _ in checkpoint["verified"]:
            matches = [gate for gate in checkpoint["record"]["gates"] if gate == item]
            assert len(matches) == 1
            verified_links += 1
        archives += 1
    for decision in record.get("qa_decisions", []):
        assert sha(retained / Path(decision["artifact"]).relative_to(original_output)) == decision["sha256"]
        decisions += 1
    if scenario == "test_continued_run_records_invalidation_of_earlier_verified_source":
        gate = next(gate for gate in record["gates"] if gate["stage"] == "baseline")
        assert gate["passed"] is False and gate["verification_status"] == "invalidated"
        assert "Verified source changed" in gate["diagnostic"]
        assert not record.get("qa_decisions") and raw["development"] == record["base_revision"]
    else:
        assert raw["integration"] == raw["development"] == record["integration_revision"]
        assert len(record["qa_decisions"]) == 2
        assert sum(gate["stage"] == "baseline" for gate in record["gates"]) == 1
        assert sum(item["role"] == "implementation" and item["event"] == "start" for item in raw["launches"]) == 4

manifest = read("15-repair1-package-manifest.json")
for name, expected in manifest["installed_source_sha256"].items():
    assert sha(ROOT / "ticket_harness" / name) == expected
    assert sha(Path("/tmp/ticket15-repair1-installed/ticket_harness") / name) == expected
for name, expected in manifest["wheel_and_backend_sha256"].items():
    assert sha(Path(name)) == expected
wheel = EVIDENCE / "15-repair1-package/ticket_harness-0.1.0-py3-none-any.whl"
assert sha(wheel) == manifest["wheel_and_backend_sha256"]["/tmp/ticket15-repair1-wheel/ticket_harness-0.1.0-py3-none-any.whl"]
with zipfile.ZipFile(wheel) as archive:
    for name, expected in manifest["installed_source_sha256"].items():
        assert hashlib.sha256(archive.read("ticket_harness/" + name)).hexdigest() == expected
assert sha(EVIDENCE / "15-repair1-installed-scenario.py") == manifest["installed_script_sha256"]
assert "from ticket_harness.__main__ import main" in Path("/tmp/ticket15-repair1-installed/bin/ticket-harness").read_text()
installed = read("15-repair1-installed-observations.json")
assert installed["import_path"].startswith("/tmp/ticket15-repair1-installed/")
assert installed["final_record"]["feature_complete"] is True
assert installed["feature"] == installed["development"] == installed["final_record"]["integration_revision"]
invalidation = read("15-repair1-installed-invalidation.json")["final_record"]
gate = next(gate for gate in invalidation["gates"] if gate["stage"] == "baseline")
assert gate["passed"] is False and gate["verification_status"] == "invalidated"
assert not invalidation.get("qa_decisions")

tracker = sha(ROOT / "docs/agents/issue-tracker.md")
assert tracker == "3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce"
focused_files = list((EVIDENCE / "15-observations/standards-repair1-recheck").glob("*.json"))
assert len(focused_files) == 1
focused = json.loads(focused_files[0].read_text())
focused_gate = next(gate for gate in focused["record"]["gates"] if gate["stage"] == "baseline")
assert focused_gate["passed"] is False and focused_gate["verification_status"] == "invalidated"
assert "1 passed in 2.76s" in (EVIDENCE / "15-standards-repair1-recheck.log").read_text()
report = {
    "baseline": BASELINE,
    "head": HEAD,
    "source_and_committed_hashes_verified": len(identity),
    "final_gate_commands_exits_source_maps_and_log_hashes_verified": len(checks),
    "actual_staged_repair_paths_verified": True,
    "raw_final_observation_hashes_and_outcomes_verified": len(rows),
    "raw_artifact_hashes_verified": len(raw_hashes),
    "successful_and_invalidation_checkpoint_archives_verified": archives,
    "unique_canonical_verified_gate_matches": verified_links,
    "consumed_decision_hashes_verified": decisions,
    "installed_source_and_wheel_member_hashes_verified": len(manifest["installed_source_sha256"]),
    "package_and_backend_hashes_verified": len(manifest["wheel_and_backend_sha256"]),
    "installed_continuation_and_invalidation_records_verified": True,
    "independent_focused_check": {
        "command": ["/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python", "-m", "pytest", "-q", "tests/test_continuation.py::test_continued_run_records_invalidation_of_earlier_verified_source"],
        "environment": {"TICKET_HARNESS_TEST_OBSERVATIONS": ".scratch/ticket-harness/evidence/15-observations/standards-repair1-recheck"},
        "exit_code": 0,
        "result": "1 passed in 2.76s",
        "log": "15-standards-repair1-recheck.log",
        "log_sha256": sha(EVIDENCE / "15-standards-repair1-recheck.log"),
        "raw_observation": str(focused_files[0].relative_to(EVIDENCE)),
        "raw_observation_sha256": sha(focused_files[0]),
        "reviewed_source_identity": "15-repair1-final-source-identity.json",
    },
    "unrelated_tracker_sha256": tracker,
    "full_suite_repeated": False,
    "audit_script": "15-standards-repair1-audit.py",
}
(EVIDENCE / "15-standards-repair1-audit.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
