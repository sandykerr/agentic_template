"""Input eligibility through the public CLI in real temporary repositories."""

import json
import sys
from pathlib import Path

import pytest
import test_cli


@pytest.fixture
def case():
    fixture = test_cli.TicketCycleTests()
    fixture.setUp()
    marker = fixture.home / "agent-launched"
    wrapper = fixture.home / "agent.py"
    wrapper.write_text(
        "import runpy\nfrom pathlib import Path\n"
        f"Path({str(marker)!r}).touch()\n"
        f"runpy.run_path({str(fixture.repo / 'agent.py')!r}, run_name='__main__')\n"
    )
    fixture.config["agent"] = [sys.executable, str(wrapper)]
    yield fixture
    fixture.doCleanups()


def reject(case, diagnostic):
    references = case.git("show-ref")
    worktrees = case.git("worktree", "list", "--porcelain")
    status = case.git("status", "--porcelain=v1")
    result = case.run_ticket()
    assert result.returncode != 0, result.stdout + result.stderr
    record = json.loads(result.stdout)
    assert record["outcome"] == "invalid-input", record
    assert record["failure"]["stage"] == "inputs"
    assert diagnostic in record["failure"]["message"], record
    assert record["gates"] == []
    assert record["ticket"]["attempt"] == 0
    assert "done_revision" not in record["ticket"]
    assert not (case.home / "agent-launched").exists()
    assert not list((case.output / "artifacts").glob("*assignment*"))
    assert case.git("show-ref") == references
    assert case.git("worktree", "list", "--porcelain") == worktrees
    assert case.git("status", "--porcelain=v1") == status
    assert json.loads(case.cli("status", case.output).stdout) == record
    return record


def test_missing_acceptance_requirements_rejects_before_any_execution(case):
    (case.repo / "01-value.md").write_text(
        "# 01: Change value\n\n**Status:** ready-for-agent\n**Blocked by:** None\n"
    )
    reject(case, "Acceptance criteria")


def test_authoring_metadata_normalizes_without_treating_checkboxes_as_execution_state(case):
    (case.repo / "01-value.md").write_text(
        "# 1: Change value\n\nStatus: ready-for-agent\n"
        "Blocked by: None (can start immediately).\nChecks: ticket\n"
        "\n## Acceptance criteria\n\n* [x] value.txt contains 2.\n"
        "\n## Comments\nStatus: Done\n"
    )
    result = case.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = json.loads(result.stdout)
    assert record["requirements"]["01"] == {
        "id": "01",
        "title": "Change value",
        "readiness": "ready-for-agent",
        "dependencies": [],
        "acceptance": ["value.txt contains 2."],
        "checks": ["ticket"],
        "source": str(case.repo / "01-value.md"),
    }
    assert record["ticket"]["id"] == "01"
    assert record["ticket"]["state"] == "Done"
    assert record["ticket"]["attempt"] == 1
    assert (case.home / "agent-launched").exists()
    assert case.git("rev-parse", "integration") == record["ticket"]["done_revision"]


def test_conflicting_readiness_is_not_silently_overwritten(case):
    path = case.repo / "01-value.md"
    path.write_text(
        path.read_text().replace("## Acceptance", "Status: ready-for-human\n## Acceptance")
    )
    reject(case, "duplicate Status")


def test_filename_cannot_disagree_with_the_stable_heading_id(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("# 01:", "# 02:"))
    reject(case, "filename ID 01 conflicts with heading ID 02")


def test_unknown_check_reference_rejects_before_worker_launch(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("## Acceptance", "Checks: missing\n## Acceptance"))
    reject(case, "unknown check reference 'missing'")


def test_only_referenced_checks_run_and_are_supplied_to_assignments(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("## Acceptance", "Checks: ticket\n## Acceptance"))
    case.config["checks"]["other"] = [sys.executable, "-c", "raise SystemExit(9)"]
    result = case.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = json.loads(result.stdout)
    assert [g["stage"] for g in record["gates"] if g["stage"].startswith("check-")] == [
        "check-ticket"
    ]
    for gate in record["gates"]:
        if "assignment" in gate:
            assignment = json.loads(Path(gate["assignment"]).read_text())
            assert assignment["required_checks"] == {"ticket": case.config["checks"]["ticket"]}


def test_unusable_check_name_is_rejected_before_any_execution(case):
    case.config["checks"] = {"bad/name": [sys.executable, "check.py"]}
    reject(case, "checks.bad/name: invalid check name")


def test_check_command_must_be_an_argument_array(case):
    case.config["checks"]["ticket"] = "python check.py ticket"
    reject(case, "checks.ticket: expected a nonempty argument array")


def test_unavailable_check_executable_rejects_without_launching_an_agent(case):
    case.config["checks"]["ticket"] = ["ticket-harness-nonexistent-executable"]
    reject(case, "checks.ticket: executable unavailable")


def test_duplicate_json_fields_are_rejected_instead_of_last_value_winning(case):
    case.config_path.write_text(json.dumps(case.config)[:-1] + ', "checks": {}}')
    case.run_ticket = lambda: case.cli("run", "--config", case.config_path, "--output", case.output)
    reject(case, "duplicate JSON key 'checks'")


def test_missing_configuration_field_has_an_actionable_diagnostic(case):
    del case.config["checks"]
    reject(case, "configuration: missing required field 'checks'")


def test_duplicate_ids_in_the_bundle_are_rejected_after_numeric_normalization(case):
    source = (case.repo / "01-value.md").read_text()
    (case.repo / "duplicate.md").write_text(source.replace("# 01:", "# 1:"))
    case.config["tickets"] = ["01-value.md", "duplicate.md"]
    reject(case, "duplicate ticket ID 01")


def test_missing_dependency_reference_names_the_ticket_and_missing_id(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("**Blocked by:** None", "**Blocked by:** 02"))
    reject(case, "ticket 01: missing dependency 02")


def dependency_bundle(case, dependency="02", reverse="None"):
    selected = case.repo / "01-value.md"
    text = selected.read_text()
    selected.write_text(text.replace("**Blocked by:** None", f"**Blocked by:** {dependency}"))
    (case.repo / "02-other.md").write_text(
        text.replace("# 01: Change value", "# 02: Other work").replace(
            "**Blocked by:** None", f"**Blocked by:** {reverse}"
        )
    )
    case.config["tickets"] = ["01-value.md", "02-other.md"]


def test_dependency_cycle_is_rejected_even_before_eligibility_is_considered(case):
    dependency_bundle(case, reverse="01")
    reject(case, "dependency cycle: 01 -> 02 -> 01")


def test_titled_markdown_dependencies_normalize_and_reject_unsatisfied_prerequisites(case):
    dependency_bundle(case, dependency="[02: Other work](02-other.md)")
    path = case.repo / "02-other.md"
    path.write_text(path.read_text().replace("[ ]", "[x]"))
    reject(case, "ticket 01: unsatisfied prerequisites ['02']")


def test_dependency_link_cannot_name_a_different_id_than_its_label(case):
    dependency_bundle(case, dependency="[02: Other work](01-value.md)")
    reject(case, "dependency 02 link conflicts")


def test_dependency_title_cannot_disagree_with_its_target(case):
    dependency_bundle(case, dependency="02: Incorrect title")
    reject(case, "dependency 02 title conflicts")


def test_prerequisite_done_in_an_integrated_run_permits_only_the_selected_ticket(case):
    # Produce genuine harness-owned Done evidence, rather than a hand-written assertion.
    result = case.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    completed = case.output
    first = json.loads(result.stdout)
    path = case.repo / "02-other.md"
    path.write_text(
        "# 02: Follow-up\nStatus: ready-for-agent\n"
        "Blocked by: [01: Change value](01-value.md)\n"
        "\n## Acceptance criteria\n- [ ] value.txt contains 3.\n"
    )
    # A second scripted submission is a distinct public external-agent behavior.
    agent = case.repo / "agent.py"
    agent.write_text(agent.read_text().replace('write_text("2\\n")', 'write_text("3\\n")'))
    case.config.update(
        ticket="02-other.md",
        tickets=["01-value.md", "02-other.md"],
        completed_runs=[str(completed / "run.json")],
        base="integration",
        checks={
            "ticket": [
                sys.executable,
                "-c",
                "from pathlib import Path; assert Path('value.txt').read_text() == '3\\n'",
            ]
        },
        suite=[sys.executable, "-c", "pass"],
    )
    case.output = case.home / "follow-up"
    (case.home / "agent-launched").unlink()
    result = case.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = json.loads(result.stdout)
    assert record["ticket"]["id"] == "02"
    assert record["requirements"]["02"]["dependencies"] == ["01"]
    assert record["base_revision"] == first["ticket"]["done_revision"]
    assert case.git("show", "integration:value.txt") == "3"
    assert [g["stage"] for g in record["gates"]].count("implementation") == 1
    assert record["inputs"]["completed-run-0"]["source"] == str(completed / "run.json")


@pytest.mark.parametrize("field,value", [("ID", "99"), ("Title", "Wrong title")])
def test_explicit_metadata_cannot_conflict_with_the_heading(case, field, value):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("## Acceptance", f"{field}: {value}\n## Acceptance"))
    reject(case, f"{field} metadata conflicts with heading")


def test_empty_acceptance_item_cannot_hide_beside_a_valid_requirement(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text() + "- [ ]   \n")
    reject(case, "empty acceptance requirement")


def test_ambiguous_multiple_ticket_headings_are_rejected(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("**Status:", "# 02: Another ticket\n**Status:"))
    reject(case, "expected exactly one ticket heading")


def test_front_matter_cannot_supply_a_second_silent_metadata_contract(case):
    path = case.repo / "01-value.md"
    path.write_text("---\nid: 99\nstatus: ready-for-human\n---\n" + path.read_text())
    reject(case, "YAML front matter is unsupported")


def test_bundle_can_contain_human_ready_work_without_executing_it(case):
    dependency_bundle(case, dependency="None")
    other = case.repo / "02-other.md"
    other.write_text(other.read_text().replace("ready-for-agent", "ready-for-human"))
    result = case.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = json.loads(result.stdout)
    assert record["requirements"]["02"]["readiness"] == "ready-for-human"
    assert record["ticket"]["id"] == "01"
    assert len([g for g in record["gates"] if g["stage"] == "implementation"]) == 1


@pytest.mark.parametrize("readiness", ["needs-triage", "needs-info", "ready-for-human", "wontfix"])
def test_non_agent_ready_selection_rejects_even_with_no_dependencies(case, readiness):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("ready-for-agent", readiness))
    reject(case, "selected Status must be ready-for-agent")


@pytest.mark.parametrize("mutation", ["incomplete", "unintegrated", "stale"])
def test_prerequisite_completion_requires_current_integrated_done_evidence(case, mutation):
    result = case.run_ticket()
    assert result.returncode == 0
    completed = case.output / "run.json"
    record = json.loads(completed.read_text())
    if mutation == "incomplete":
        record["outcome"] = "incomplete"
        record["ticket"]["state"] = "Blocked"
    elif mutation == "unintegrated":
        case.git("update-ref", "refs/heads/integration", case.base)
    else:
        path = case.repo / "01-value.md"
        path.write_text(path.read_text().replace("contains 2", "contains 99"))
    completed.write_text(json.dumps(record))
    (case.repo / "02-other.md").write_text(
        "# 02: Follow-up\nStatus: ready-for-agent\nBlocked by: 01\n"
        "\n## Acceptance criteria\n- [ ] Follow-up works.\n"
    )
    case.config.update(
        ticket="02-other.md",
        tickets=["01-value.md", "02-other.md"],
        completed_runs=[str(completed)],
        base="integration",
    )
    case.output = case.home / "rejected-follow-up"
    (case.home / "agent-launched").unlink()
    reject(case, "invalid prerequisite completion evidence")


def test_multiple_acceptance_sections_do_not_choose_one_silently(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text() + "\n## Acceptance criteria\n- [ ] Different requirements.\n")
    reject(case, "duplicate Acceptance criteria section")


def test_example_checklist_does_not_supply_missing_acceptance_content(case):
    (case.repo / "01-value.md").write_text(
        "# 01: Change value\nStatus: ready-for-agent\nBlocked by: None\n"
        "\n```markdown\n## Acceptance criteria\n- [ ] Just an example.\n```\n"
    )
    reject(case, "Acceptance criteria")


def test_unknown_configuration_key_is_not_silently_ignored(case):
    case.config["check"] = case.config["checks"]
    reject(case, "configuration: unsupported field 'check'")


@pytest.mark.parametrize(
    "field,value,diagnostic",
    [
        ("checks", {}, "configuration.checks"),
        ("checks", [], "configuration.checks"),
        ("suite", [], "suite: expected"),
        ("agent", "python agent.py", "agent: expected"),
        ("suite", [sys.executable, None], "suite: expected"),
        ("suite", [sys.executable, "\0"], "suite: expected"),
        ("base", None, "configuration.base"),
        ("standards", "STANDARDS.md", "configuration.standards"),
        ("tickets", "01-value.md", "configuration.tickets"),
        ("tickets", [], "must include the selected ticket"),
        ("tickets", ["01-value.md", "./01-value.md"], "duplicate ticket paths"),
        ("completed_runs", "run.json", "configuration.completed_runs"),
        ("spec", "missing.md", "missing.md"),
        ("base", "nonexistent-ref", "nonexistent-ref"),
        ("integration", "bad ref", "bad ref"),
    ],
)
def test_invalid_configuration_shapes_and_references_reject_before_execution(
    case, field, value, diagnostic
):
    case.config[field] = value
    reject(case, diagnostic)


@pytest.mark.parametrize(
    "replacement,diagnostic",
    [
        ("# 00: Change value", "positive numeric identifier"),
        ("# nope: Change value", "expected '# NN: Title'"),
        ("# 01:   ", "expected '# NN: Title'"),
    ],
)
def test_invalid_stable_heading_rejects(case, replacement, diagnostic):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace("# 01: Change value", replacement))
    reject(case, diagnostic)


def test_cycle_in_unselected_work_still_invalidates_the_bundle(case):
    dependency_bundle(case, dependency="None", reverse="02")
    reject(case, "dependency cycle: 02 -> 02")


def test_duplicate_check_references_are_an_ambiguous_contract(case):
    path = case.repo / "01-value.md"
    path.write_text(
        path.read_text().replace("## Acceptance", "Checks: ticket, ticket\n## Acceptance")
    )
    reject(case, "duplicate check reference")


@pytest.mark.parametrize(
    "line,diagnostic",
    [
        ("**Status:** ready-for-agent", "Status must be a triage readiness label"),
        ("**Blocked by:** None", "invalid Blocked by reference"),
        ("- [ ] value.txt contains 2.", "Acceptance criteria needs nonempty checklist items"),
    ],
)
def test_required_metadata_and_acceptance_content_cannot_be_omitted(case, line, diagnostic):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text().replace(line, ""))
    reject(case, diagnostic)


def test_second_heading_after_acceptance_is_still_conflicting_metadata(case):
    path = case.repo / "01-value.md"
    path.write_text(path.read_text() + "\n# 02: Hidden second ticket\n")
    reject(case, "expected exactly one ticket heading")
