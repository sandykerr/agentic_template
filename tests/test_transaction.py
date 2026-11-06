"""Transaction invariants observed through real CLI processes and Git repositories."""

import json
from pathlib import Path

import pytest
from test_reports import ReportFixture


@pytest.fixture
def harness():
    fixture = ReportFixture()
    fixture.setUp()
    yield fixture
    fixture.doCleanups()


def test_worker_cannot_rewrite_approved_ticket_in_its_source(harness):
    harness.agent_report(
        "implementation",
        "from pathlib import Path\nPath('01-value.md').write_text('Redefined success')",
    )
    record = harness.assert_rejected_gate("implementation")
    assert "integrity" in record["failure"]["message"].lower()
    assert "submitted_revision" not in record["ticket"]
    assert (
        harness.output / "worktrees/implementation/01-value.md"
    ).read_text() == "Redefined success"


def test_later_review_editing_earlier_review_source_invalidates_approval(harness):
    harness.agent_report(
        "standards",
        "from pathlib import Path\n"
        "(Path.cwd().parent / 'spec/value.txt').write_text('unreviewed edit')",
    )
    record = harness.assert_rejected_gate("standards")
    spec = next(g for g in record["gates"] if g["stage"] == "spec")
    assert not spec["passed"]
    assert spec["verification_status"] == "invalidated"
    assert spec["report_status"] == "valid"
    assert "changed" in spec["diagnostic"]
    assert (harness.output / "worktrees/spec/value.txt").read_text() == "unreviewed edit"


@pytest.mark.parametrize("role", ["implementation", "spec", "standards"])
@pytest.mark.parametrize("target", ["snapshot", "record", "assignment", "prior-output", "original"])
def test_assignment_tampering_is_rejected_and_preserved(harness, role, target):
    paths = {
        "snapshot": harness.output / "inputs/ticket.md",
        "record": harness.output / "run.json",
        "assignment": harness.output / f"artifacts/{role}.assignment.json",
        "prior-output": harness.output / "artifacts/baseline.stdout",
        "original": harness.home / "approved-spec.md",
    }
    # Put this approved input outside caller source so preservation is independently observable.
    original = paths["original"]
    original.write_text((harness.repo / "spec.md").read_text())
    harness.config["spec"] = str(original)
    path = paths[target]
    harness.agent_report(
        role, f"from pathlib import Path\nPath({str(path)!r}).write_text('tampered')"
    )
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["report_status"] == "valid"
    violation = next(item for item in gate["integrity"] if item["path"] == str(path))
    assert violation["expected_sha256"] != violation["observed_sha256"]
    assert Path(violation["artifact"]).read_text() == "tampered"
    if target != "original":
        assert path.read_text() != "tampered"
    ticket_snapshot = record["inputs"]["ticket"]
    assert (
        Path(ticket_snapshot["artifact"]).read_bytes()
        == Path(ticket_snapshot["source"]).read_bytes()
    )


@pytest.mark.parametrize("role", ["spec", "standards"])
@pytest.mark.parametrize("change", ["dirty", "commit", "head"])
def test_review_source_changes_cannot_approve_another_revision(harness, role, change):
    mutation = "from pathlib import Path\nimport subprocess\nPath('value.txt').write_text('3\\n')"
    if change == "commit":
        mutation += "\nsubprocess.run(['git', 'add', 'value.txt'], check=True)"
        mutation += "\nsubprocess.run(['git', 'commit', '-m', 'Unapproved revision'], check=True, stdout=sys.stderr)"
    if change == "head":
        mutation += "\nsubprocess.run(['git', 'reset', '--hard', assignment['base_revision']], check=True, stdout=sys.stderr)"
    harness.agent_report(role, mutation)
    record = harness.assert_rejected_gate(role)
    gate = record["gates"][-1]
    assert gate["report_status"] == "valid"
    assert gate["verification_status"] == "invalidated"
    assert "changed" in gate["diagnostic"]


@pytest.mark.parametrize("role", ["spec", "standards"])
def test_review_editing_checked_submission_invalidates_check_evidence(harness, role):
    harness.agent_report(
        role,
        "from pathlib import Path\n"
        "(Path.cwd().parent / 'implementation/value.txt').write_text('3\\n')",
    )
    record = harness.assert_rejected_gate(role)
    check = next(g for g in record["gates"] if g["stage"] == "check-ticket")
    assert not check["passed"]
    assert check["verification_status"] == "invalidated"
    assert check["revision"] == record["ticket"]["submitted_revision"]


def suite_script(harness, action):
    script = harness.home / "suite.py"
    script.write_text(
        "import os, subprocess\nfrom pathlib import Path\n"
        "if os.environ['TICKET_HARNESS_STAGE'] == 'candidate':\n"
        + "\n".join("    " + line for line in action.splitlines())
        + "\n"
    )
    harness.config["suite"] = [harness.config["agent"][0], str(script)]


@pytest.mark.parametrize("tree", ["candidate", "spec", "standards", "implementation"])
def test_candidate_check_cannot_change_verified_source(harness, tree):
    suite_script(
        harness,
        f"(Path.cwd().parent / {tree!r} / 'value.txt').write_text('unverified')",
    )
    record = harness.assert_rejected_gate("candidate")
    invalidated = [g for g in record["gates"] if g.get("verification_status") == "invalidated"]
    assert invalidated
    assert all(not g["passed"] for g in invalidated)
    assert record["ticket"]["candidate_revision"] != harness.base
    assert (harness.output / f"worktrees/{tree}/value.txt").read_text() == "unverified"


@pytest.mark.parametrize("stage", ["spec", "standards", "candidate"])
def test_external_integration_movement_is_preserved(harness, stage):
    action = (
        "import subprocess\n"
        "external = subprocess.check_output(['git', 'commit-tree', 'HEAD^{tree}', '-p', 'HEAD', "
        "'-m', 'External movement'], text=True).strip()\n"
        "subprocess.run(['git', 'update-ref', 'refs/heads/integration', external], check=True)"
    )
    if stage == "candidate":
        suite_script(harness, action)
    else:
        harness.agent_report(stage, action)
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "unrelated").write_text("keep")
    before = harness.git("status", "--porcelain")
    result = harness.run_ticket()
    assert result.returncode != 0
    record = harness.record()
    assert record["outcome"] == "incomplete"
    assert record["failure"]["stage"] == "integration"
    assert "update-ref" in record["failure"]["message"]
    external = harness.git("rev-parse", "integration")
    candidate = record["ticket"]["candidate_revision"]
    assert external not in (harness.base, candidate)
    assert harness.git("show", "-s", "--format=%s", external) == "External movement"
    assert record["gates"][-1]["revision"] == candidate
    assert record["gates"][-1]["passed"]
    assert "done_revision" not in record["ticket"]
    assert harness.git("status", "--porcelain") == before
    assert json.loads(harness.cli("status", harness.output).stdout) == record


def test_failed_merge_preserves_submission_and_merge_diagnostics(harness):
    hook = harness.repo / ".git/hooks/pre-merge-commit"
    hook.write_text("#!/bin/sh\necho 'Controlled merge failure' >&2\nexit 1\n")
    hook.chmod(0o755)
    result = harness.run_ticket()
    assert result.returncode != 0
    record = harness.record()
    assert record["failure"]["stage"] == "candidate"
    assert "Controlled merge failure" in record["failure"]["message"]
    assert record["outcome"] == "incomplete"
    assert "done_revision" not in record["ticket"]
    assert harness.git("rev-parse", "integration") == harness.base
    assert harness.git("show", record["ticket"]["submitted_revision"] + ":value.txt") == "2"
    candidate = harness.output / "worktrees/candidate"
    assert (candidate / "value.txt").read_text() == "2\n"
    assert record["gates"][-1]["stage"] == "standards"
    assert json.loads(harness.cli("status", harness.output).stdout) == record


def test_merge_hook_source_resolution_requires_new_review(harness):
    hook = harness.repo / ".git/hooks/post-merge"
    hook.write_text(
        "#!/bin/sh\nprintf '3\\n' > value.txt\ngit add value.txt\ngit commit --no-edit >/dev/null\n"
    )
    hook.chmod(0o755)
    # Use a passing suite so test failure depends on review validity, not check coverage.
    suite_script(harness, "pass")
    result = harness.run_ticket()
    assert result.returncode != 0
    record = harness.record()
    assert record["failure"]["stage"] == "candidate"
    assert "review" in record["failure"]["message"].lower()
    assert harness.git("rev-parse", "integration") == harness.base
    assert "done_revision" not in record["ticket"]
    assert (harness.output / "worktrees/candidate/value.txt").read_text() == "3\n"


def test_submission_hook_cannot_change_approved_requirements(harness):
    hook = harness.repo / ".git/hooks/pre-commit"
    hook.write_text("#!/bin/sh\necho 'Redefined success' > 01-value.md\ngit add 01-value.md\n")
    hook.chmod(0o755)
    result = harness.run_ticket()
    assert result.returncode != 0
    record = harness.record()
    assert record["failure"]["stage"] == "implementation"
    assert "approved" in record["failure"]["message"].lower()
    assert harness.git("rev-parse", "integration") == harness.base
    assert "done_revision" not in record["ticket"]
    assert (
        harness.git("show", record["ticket"]["submitted_revision"] + ":01-value.md")
        == "Redefined success"
    )


def test_rejected_candidate_preserves_caller_index_and_file_bytes(harness):
    (harness.repo / "value.txt").write_text("caller staged\n")
    harness.git("add", "value.txt")
    (harness.repo / "value.txt").write_text("caller unstaged\n")
    (harness.repo / "unrelated.txt").write_text("caller untracked\n")
    harness.config["suite"].append("candidate")
    record = harness.assert_rejected_gate("candidate")
    assert harness.git("show", ":value.txt") == "caller staged"
    assert (harness.repo / "value.txt").read_text() == "caller unstaged\n"
    assert (harness.repo / "unrelated.txt").read_text() == "caller untracked\n"
    assert harness.git("rev-parse", "HEAD") == harness.base
    assert (harness.output / "worktrees/implementation/value.txt").read_text() == "2\n"
    assert (harness.output / "worktrees/candidate/value.txt").read_text() == "2\n"
    assert harness.git("show", record["ticket"]["submitted_revision"] + ":value.txt") == "2"
