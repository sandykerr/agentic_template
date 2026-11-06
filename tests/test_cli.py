"""Acceptance tests at the public CLI, Git, and recorded-artifact seam."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TicketFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ticket-harness-test-")
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.repo = self.home / "target"
        shutil.copytree(ROOT / "examples" / "scripted", self.repo)
        self.git("init", "-b", "main")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Fixture")
        self.git("add", ".")
        self.git("commit", "-m", "Fixture baseline")
        self.base = self.git("rev-parse", "HEAD")
        self.git("branch", "integration")
        self.output = self.home / "run"
        self.config = json.loads((self.repo / "project.json").read_text())
        # These prerequisite scenarios exercise rejection with repair disabled.
        self.config["max_repairs"] = 0
        self.config["repository"] = str(self.repo)
        self.config["agent"] = [sys.executable, str(self.repo / "agent.py")]
        self.config["suite"] = [sys.executable, "check.py", "suite"]
        self.config["checks"] = {"ticket": [sys.executable, "check.py", "ticket"]}
        self.config_path = self.home / "project.json"

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args], text=True).strip()

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "ticket_harness", *map(str, args)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def run_ticket(self):
        self.config_path.write_text(json.dumps(self.config))
        return self.cli("run", "--config", self.config_path, "--output", self.output)

    def record(self):
        return json.loads((self.output / "run.json").read_text())

    def assert_rejected_gate(self, stage, outcome="incomplete", attempt=1):
        before = self.git("status", "--porcelain=v1")
        result = self.run_ticket()
        self.assertNotEqual(result.returncode, 0)
        record = self.record()
        self.assertEqual(record["outcome"], outcome)
        self.assertEqual(record["failure"]["stage"], stage)
        self.assertEqual(record["ticket"]["state"], "Blocked")
        self.assertEqual(record["ticket"]["attempt"], attempt)
        self.assertNotIn("done_revision", record["ticket"])
        self.assertEqual(self.git("rev-parse", "integration"), self.base)
        self.assertEqual(self.git("status", "--porcelain=v1"), before)
        gate = record["gates"][-1]
        self.assertEqual(gate["stage"], stage)
        self.assertFalse(gate["passed"])
        self.assertTrue(Path(gate["stdout"]).is_file())
        self.assertTrue(Path(gate["stderr"]).is_file())
        self.assertEqual(json.loads(self.cli("status", self.output).stdout), record)
        return record


class TicketCycleTests(TicketFixture):
    def test_one_ticket_passes_every_gate_and_status_reads_its_exact_revision(self):
        # Caller work, including staged changes, must survive the whole cycle.
        (self.repo / "value.txt").write_text("caller edit\n")
        self.git("add", "value.txt")
        (self.repo / "unrelated.txt").write_text("keep me\n")
        before = self.git("status", "--porcelain=v1")
        result = self.run_ticket()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        record = self.record()
        self.assertEqual(record["outcome"], "completed")
        self.assertEqual(record["ticket"]["state"], "Done")
        self.assertEqual(record["base_revision"], self.base)
        candidate = record["ticket"]["candidate_revision"]
        self.assertEqual(self.git("rev-parse", "integration"), candidate)
        self.assertEqual(record["ticket"]["done_revision"], candidate)
        self.assertEqual(self.git("show", f"{candidate}:value.txt"), "2")
        self.assertEqual(
            self.git("rev-list", "--parents", "-n", "1", candidate).split()[1:],
            [self.base, record["ticket"]["submitted_revision"]],
        )
        self.assertEqual(record["ticket"]["changed_files"], ["value.txt"])
        gates = record["gates"]
        self.assertEqual(
            [g["stage"] for g in gates],
            ["baseline", "implementation", "check-ticket", "spec", "standards", "candidate"],
        )
        self.assertTrue(all(g["passed"] for g in gates))
        self.assertEqual(gates[0]["revision"], self.base)
        self.assertEqual(gates[-1]["revision"], candidate)
        for gate in gates[2:5]:
            self.assertEqual(gate["revision"], record["ticket"]["submitted_revision"])
        pids = []
        for gate in gates:
            self.assertTrue(Path(gate["stdout"]).is_file())
            self.assertTrue(Path(gate["stderr"]).is_file())
            if "assignment" in gate:
                assignment = json.loads(Path(gate["assignment"]).read_text())
                report = json.loads(Path(gate["stdout"]).read_text())
                pids.append(report["pid"])
                self.assertEqual(assignment["ticket"], "01")
                self.assertEqual(assignment["attempt"], 1)
                self.assertIn("Change value", assignment["inputs"]["ticket"])
                self.assertIn("fixture standard", assignment["inputs"]["standards-0"])
                self.assertTrue(assignment["instructions"])
                self.assertEqual(assignment["required_checks"], self.config["checks"])
                self.assertIn("revision", assignment["report_contract"]["identity_fields"])
        self.assertEqual(len(set(pids)), 3)
        for name, snapshot in record["inputs"].items():
            self.assertEqual(
                Path(snapshot["artifact"]).read_bytes(), Path(snapshot["source"]).read_bytes(), name
            )
            self.assertEqual(len(snapshot["sha256"]), 64)
        self.assertEqual(self.git("status", "--porcelain=v1"), before)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.base)
        # Status remains usable after removing the executable agent.
        (self.repo / "agent.py").unlink()
        recorded_bytes = (self.output / "run.json").read_bytes()
        status_before = self.git("status", "--porcelain=v1")
        status = self.cli("status", self.output)
        self.assertEqual(status.returncode, 0, status.stderr)
        self.assertEqual(json.loads(status.stdout), record)
        self.assertEqual(self.git("status", "--porcelain=v1"), status_before)
        self.assertEqual((self.output / "run.json").read_bytes(), recorded_bytes)

    def test_blocking_spec_review_preserves_submission_without_integrating(self):
        self.config["agent"] += ["--reject", "spec"]
        result = self.run_ticket()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        record = self.record()
        self.assertEqual(record["outcome"], "incomplete")
        self.assertEqual(record["ticket"]["state"], "Blocked")
        self.assertEqual(record["failure"]["stage"], "spec")
        self.assertEqual(self.git("rev-parse", "integration"), self.base)
        self.assertNotIn("done_revision", record["ticket"])
        submitted = record["ticket"]["submitted_revision"]
        self.assertEqual(self.git("show", f"{submitted}:value.txt"), "2")
        self.assertFalse(record["gates"][-1]["passed"])
        self.assertIn("blocking", record["failure"]["message"])
        self.assertEqual(json.loads(self.cli("status", self.output).stdout), record)

    def test_failed_baseline_is_environment_failure_without_an_assignment(self):
        self.config["suite"].append("baseline")
        record = self.assert_rejected_gate("baseline", outcome="environment", attempt=0)
        self.assertEqual(len(record["gates"]), 1)
        self.assertIn("scripted gate rejection", Path(record["gates"][0]["stderr"]).read_text())

    def test_failed_lightweight_check_preserves_submission_and_stops_reviews(self):
        self.config["checks"]["ticket"].append("check-ticket")
        record = self.assert_rejected_gate("check-ticket")
        self.assertEqual(len(record["gates"]), 3)
        self.assertEqual(
            self.git("show", record["ticket"]["submitted_revision"] + ":value.txt"), "2"
        )

    def test_blocking_standards_review_cannot_integrate(self):
        self.config["agent"] += ["--reject", "standards"]
        self.assert_rejected_gate("standards")

    def test_failed_candidate_suite_preserves_tested_candidate_without_integrating(self):
        self.config["suite"].append("candidate")
        record = self.assert_rejected_gate("candidate")
        candidate = record["ticket"]["candidate_revision"]
        self.assertNotEqual(candidate, self.base)
        self.assertEqual(record["gates"][-1]["revision"], candidate)
        self.assertEqual(self.git("show", candidate + ":value.txt"), "2")

    def test_nonzero_implementation_exit_cannot_produce_done(self):
        # An external process failure is not a submission, even if stdout is JSON.
        self.config["agent"] = [sys.executable, "-c", "print('{}'); raise SystemExit(7)"]
        record = self.assert_rejected_gate("implementation")
        self.assertEqual(record["gates"][-1]["exit_code"], 7)

    def test_existing_run_is_never_overwritten(self):
        self.assertEqual(self.run_ticket().returncode, 0)
        before = (self.output / "run.json").read_bytes()
        result = self.run_ticket()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.output / "run.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
