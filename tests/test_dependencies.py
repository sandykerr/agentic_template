"""Selected dependency graphs observed through CLI launches and real integration history."""

import json
import os
import sys
from pathlib import Path

import pytest
from test_cli import TicketFixture
from test_preflight import reject


class DependencyFixture(TicketFixture):
    def setUp(self):
        super().setUp()
        self.cli_observations = []

    def cli(self, *args):
        result = super().cli(*args)
        output = Path(args[-1])
        record_path = output / "run.json"
        self.cli_observations.append(
            {
                "command": [sys.executable, "-m", "ticket_harness", *map(str, args)],
                "exit_code": result.returncode,
                "stderr": result.stderr,
                "stdout_matches_record": record_path.exists()
                and result.stdout == record_path.read_text(),
                "record": json.loads(result.stdout) if result.stdout else None,
            }
        )
        return result


@pytest.fixture
def graph(request):
    fixture = DependencyFixture()
    fixture.setUp()
    fixture.config["checks"]["other"] = fixture.config["checks"]["ticket"]
    paths = {}
    for ticket, dependencies in (("01", "None"), ("02", "03, 04"), ("03", "None"), ("04", "01")):
        path = "01-value.md" if ticket == "01" else f"{ticket}-work.md"
        paths[ticket] = path
        (fixture.repo / path).write_text(
            f"# {ticket}: Work {ticket}\n\nStatus: ready-for-agent\n"
            f"Blocked by: {dependencies}\nChecks: {'other' if ticket == '03' else 'ticket'}\n"
            f"\n## Acceptance criteria\n\n- [ ] Deliver work {ticket}.\n"
        )
    (fixture.repo / "05-context.md").write_text(
        "# 05: Human context\n\nStatus: ready-for-human\nBlocked by: None\n"
        "\n## Acceptance criteria\n\n- [ ] Human work.\n"
    )
    (fixture.repo / "07-context.md").write_text(
        "# 07: Agent context\nStatus: ready-for-agent\nBlocked by: 05\n"
        "\n## Acceptance criteria\n- [ ] Context work.\n"
    )
    fixture.config.update(
        ticket=paths["02"],
        tickets=[paths[t] for t in ("04", "02", "03", "01")] + ["05-context.md", "07-context.md"],
        selected_tickets=[paths[t] for t in ("04", "02", "03", "01")],
    )
    fixture.git("add", ".")
    fixture.git("commit", "-m", "Approved dependency graph")
    fixture.base = fixture.git("rev-parse", "HEAD")
    fixture.git("update-ref", "refs/heads/integration", fixture.base)
    agent = fixture.home / "graph-agent.py"
    agent.write_text(
        "import json, os, subprocess, sys\nfrom pathlib import Path\n"
        "a = json.load(sys.stdin)\n"
        f"home = Path({str(fixture.home)!r})\n"
        "lock = home / 'active-process'\n"
        "fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)\n"
        "os.close(fd)\n"
        "def git(*args):\n"
        "    return subprocess.check_output(['git', *args], text=True).strip()\n"
        "record = json.loads((Path.cwd().parents[1] / 'run.json').read_text())\n"
        "event = dict(ticket=a['ticket'], role=a['role'], attempt=a['attempt'],\n"
        "    head=git('rev-parse', 'HEAD'), integration=git('rev-parse', 'integration'),\n"
        "    states=record.get('tickets'), base=a['base_revision'], pid=os.getpid())\n"
        "with (home / 'launches.jsonl').open('a') as out:\n"
        "    out.write(json.dumps(dict(event, event='start')) + '\\n')\n"
        "assert a['inputs']['ticket'].startswith('# ' + a['ticket'] + ':')\n"
        "r = {k: a[k] for k in ('role', 'ticket', 'attempt', 'base_revision', 'revision')}\n"
        "r['pid'] = os.getpid()\n"
        "if a['role'] == 'implementation':\n"
        "    Path('work-' + a['ticket']).write_text('delivered ' + a['ticket'] + '\\n')\n"
        "    Path('last-ticket').write_text(a['ticket'])\n"
        "    r.update(result='submitted', summary='Delivered ticket', changed_files=[],\n"
        "        checks=[], acceptance_evidence=['Delivered cumulative work'], unresolved_questions=[])\n"
        "else:\n"
        "    r['findings'] = []\n"
        "with (home / 'launches.jsonl').open('a') as out:\n"
        "    out.write(json.dumps(dict(event, event='end')) + '\\n')\n"
        "lock.unlink()\n"
        "print(json.dumps(r))\n"
    )
    fixture.config["agent"] = [fixture.config["agent"][0], str(agent)]
    check = fixture.home / "graph-check.py"
    check.write_text(
        "import os, subprocess\nfrom pathlib import Path\n"
        "stage = os.environ['TICKET_HARNESS_STAGE']\n"
        "print(stage, subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())\n"
        "if stage != 'baseline':\n"
        "    ticket = Path('last-ticket').read_text()\n"
        "    assert Path('work-' + ticket).read_text() == 'delivered ' + ticket + '\\n'\n"
        "    for dep in {'02': ['01', '04'], '04': ['01']}.get(ticket, []):\n"
        "        assert Path('work-' + dep).exists()\n"
    )
    fixture.config["suite"] = [fixture.config["agent"][0], str(check)]
    fixture.config["checks"] = {name: fixture.config["suite"] for name in ("ticket", "other")}
    try:
        yield fixture
    finally:
        observations = os.environ.get("TICKET_HARNESS_TEST_OBSERVATIONS")
        if observations and (fixture.output / "run.json").exists():
            record = fixture.record()
            evidence = {
                "scenario": request.node.name,
                "record": record,
                "cli_observations": fixture.cli_observations,
                "integration": fixture.git("rev-parse", "integration"),
                "history": fixture.git("log", "--format=%H %P %s", "integration"),
                "caller_status": fixture.git("status", "--porcelain"),
                "launches": launches(fixture),
                "outputs": {
                    p.name: p.read_text()
                    for g in record["gates"]
                    for p in (Path(g["stdout"]), Path(g["stderr"]))
                },
            }
            destination = Path(observations)
            destination.mkdir(parents=True, exist_ok=True)
            (destination / (fixture.home.name + ".json")).write_text(json.dumps(evidence, indent=2))
        fixture.doCleanups()


def launches(graph):
    path = graph.home / "launches.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def test_dependency_chain_and_independent_work_use_verified_integration_in_stable_order(graph):
    (graph.repo / "value.txt").write_text("caller staged\n")
    graph.git("add", "value.txt")
    (graph.repo / "value.txt").write_text("caller unstaged\n")
    (graph.repo / "untracked").write_text("keep caller work")
    before = graph.git("status", "--porcelain")
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "completed"
    assert record["selected_tickets"] == ["01", "02", "03", "04"]
    assert set(record["tickets"]) == {"01", "02", "03", "04"}
    events = launches(graph)
    assert [e["event"] for e in events] == ["start", "end"] * 12
    starts = events[::2]
    assert [(e["ticket"], e["role"]) for e in starts] == [
        (ticket, role)
        for ticket in ("01", "03", "04", "02")
        for role in ("implementation", "spec", "standards")
    ]
    assert len({e["pid"] for e in starts}) == 12
    gates = record["gates"]
    assert [(g["stage"], g["attempt"]) for g in gates if g["stage"] == "baseline"] == [
        ("baseline", 0)
    ]
    previous = graph.base
    completed = []
    for ticket in ("01", "03", "04", "02"):
        state = record["tickets"][ticket]
        assert state["state"] == "Done"
        assert state["attempt"] == 1
        worker = next(e for e in starts if e["ticket"] == ticket and e["role"] == "implementation")
        assert worker["head"] == worker["base"] == worker["integration"] == previous
        assert all(worker["states"][t]["state"] == "Done" for t in completed)
        assert worker["states"][ticket]["state"] == "Running"
        if ticket == "01":
            assert worker["states"]["02"]["state"] == "Pending"
            assert worker["states"]["04"]["state"] == "Pending"
        if ticket == "03":
            assert worker["states"]["04"]["state"] == "Ready"
            assert worker["states"]["02"]["state"] == "Pending"
        ticket_gates = [g for g in gates if g.get("ticket") == ticket]
        check = "other" if ticket == "03" else "ticket"
        assert [g["stage"] for g in ticket_gates] == [
            "implementation",
            f"check-{check}",
            "spec",
            "standards",
            "candidate",
        ]
        assert all(g["passed"] for g in ticket_gates)
        assert all(g["revision"] == state["submitted_revision"] for g in ticket_gates[1:4])
        assert ticket_gates[-1]["revision"] == state["done_revision"]
        for gate in ticket_gates:
            if "assignment" in gate:
                a = json.loads(Path(gate["assignment"]).read_text())
                assert a["ticket"] == ticket
                assert a["base_revision"] == previous
                assert set(a["required_checks"]) == {check}
                assert all(g.get("ticket") in (None, ticket) for g in a["check_results"])
        done = state["done_revision"]
        assert graph.git("show", "-s", "--format=%P", done).split() == [
            previous,
            state["submitted_revision"],
        ]
        assert graph.git("rev-parse", done + "^{tree}") == graph.git(
            "rev-parse", state["submitted_revision"] + "^{tree}"
        )
        completed.append(ticket)
        for earlier in completed:
            assert graph.git("show", done + ":work-" + earlier) == "delivered " + earlier
        previous = done
    assert graph.git("rev-parse", "integration") == record["integration_revision"] == previous
    assert [a["ticket"] for a in record["attempts"]] == ["01", "03", "04", "02"]
    for a in record["attempts"]:
        assert all(g["ticket"] == a["ticket"] for g in gates[a["gate_start"] : a["gate_end"]])
    assert len({g["stdout"] for g in gates}) == len(gates)
    assert len({o["stage"] for o in record["operations"]}) == len(record["operations"])
    assert all(Path(g["stdout"]).exists() for g in gates)
    assert graph.git("status", "--porcelain") == before
    assert graph.git("show", ":value.txt") == "caller staged"
    assert (graph.repo / "value.txt").read_text() == "caller unstaged\n"
    assert graph.cli("status", graph.output).stdout == result.stdout
    assert json.loads(result.stdout) == record


@pytest.mark.parametrize(
    "selection,diagnostic",
    [
        ([], "nonempty and include ticket"),
        ("01-value.md", "expected an array"),
        ([None], "expected an array"),
        (["01-value.md"], "nonempty and include ticket"),
        (["02-work.md", "./02-work.md"], "duplicate ticket paths"),
        (["02-work.md", "missing.md"], "subset of tickets"),
        (
            ["01-value.md", "02-work.md", "03-work.md", "04-work.md", "05-context.md"],
            "selected Status must be ready-for-agent",
        ),
        (["02-work.md"], "unsatisfied prerequisites"),
    ],
)
def test_invalid_selection_rejects_before_workers_checks_or_git_changes(
    graph, selection, diagnostic
):
    graph.config["selected_tickets"] = selection
    reject(graph, diagnostic)
    assert launches(graph) == []


def test_unselected_context_cycles_and_unavailable_unused_checks_still_reject(graph):
    (graph.repo / "05-context.md").write_text(
        (graph.repo / "05-context.md").read_text().replace("Blocked by: None", "Blocked by: 05")
    )
    reject(graph, "dependency cycle")
    graph.output = graph.home / "second-rejection"
    (graph.repo / "05-context.md").write_text(
        (graph.repo / "05-context.md").read_text().replace("Blocked by: 05", "Blocked by: None")
    )
    graph.config["checks"]["unused"] = ["/missing/ticket09-check"]
    reject(graph, "executable unavailable")
    assert launches(graph) == []


def test_multi_ticket_completion_evidence_unlocks_only_explicit_follow_up_selection(graph):
    assert graph.run_ticket().returncode == 0
    completed = graph.output / "run.json"
    previous = graph.git("rev-parse", "integration")
    # The next approval adds a new ticket while preserving the original approved prerequisite bytes.
    path = graph.repo / "06-follow-up.md"
    path.write_text(
        "# 06: Follow up\nStatus: ready-for-agent\nBlocked by: 01, 02, 03, 04\nChecks: ticket\n"
        "\n## Acceptance criteria\n- [ ] Deliver follow up.\n"
    )
    graph.config.update(
        ticket=path.name,
        tickets=graph.config["tickets"] + [path.name],
        selected_tickets=[path.name],
        completed_runs=[str(completed)],
        base="integration",
    )
    graph.output = graph.home / "follow-up"
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert set(record["tickets"]) == {"06"}
    assert [e["ticket"] for e in launches(graph)[::2] if e["role"] == "implementation"] == [
        "01",
        "03",
        "04",
        "02",
        "06",
    ]
    worker = record["gates"][1]
    assert worker["revision"] == previous
    assert record["tickets"]["06"]["state"] == "Done"
    assert graph.git("show", "integration:work-01") == "delivered 01"
    assert graph.cli("status", graph.output).stdout == result.stdout


def extend_agent(graph, code):
    path = Path(graph.config["agent"][1])
    path.write_text(
        path.read_text().replace("print(json.dumps(r))", code + "\nprint(json.dumps(r))")
    )


def test_repairs_keep_ticket_local_attempts_fixed_bases_and_all_earlier_evidence(graph):
    graph.config["max_repairs"] = 1
    extend_agent(
        graph,
        "if a['ticket'] in ('01', '03'):\n"
        "    if a['role'] == 'implementation':\n"
        "        if a['attempt'] == 1:\n"
        "            Path('note-' + a['ticket']).write_text('preserve rejected work')\n"
        "        else:\n"
        "            assert Path('note-' + a['ticket']).read_text() == 'preserve rejected work'\n"
        "            Path('repair-' + a['ticket']).write_text('verified repair')\n"
        "    elif a['role'] == 'spec' and a['attempt'] == 1:\n"
        "        r['findings'] = [dict(id='repair', classification='blocking',\n"
        "            location='work-' + a['ticket'], requirement='Scripted repair requirement',\n"
        "            consequence='Current work needs repair', evidence='First revision rejected',\n"
        "            resolution='Repair with fresh checks', human_decision_needed=False)]",
    )
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    record = graph.record()
    assert record["outcome"] == "completed"
    assert [(a["ticket"], a["attempt"], a["state"]) for a in record["attempts"]] == [
        ("01", 1, "Rejected"),
        ("01", 2, "Done"),
        ("03", 1, "Rejected"),
        ("03", 2, "Done"),
        ("04", 1, "Done"),
        ("02", 1, "Done"),
    ]
    for ticket in ("01", "03"):
        rejected, repaired = [a for a in record["attempts"] if a["ticket"] == ticket]
        gates = record["gates"][repaired["gate_start"] : repaired["gate_end"]]
        assert [(g["ticket"], g["attempt"]) for g in gates] == [(ticket, 2)] * 5
        assert [g["stage"] for g in gates] == [
            "implementation",
            "check-ticket" if ticket == "01" else "check-other",
            "spec",
            "standards",
            "candidate",
        ]
        prompt = json.loads(Path(gates[0]["assignment"]).read_text())
        assert prompt["base_revision"] == rejected["starting_revision"]
        assert prompt["revision"] == repaired["starting_revision"] == rejected["submitted_revision"]
        assert prompt["repair_context"]["rejected_revisions"] == [rejected["submitted_revision"]]
        assert all(g["ticket"] in (None, ticket) for g in prompt["check_results"])
        assert (
            Path(rejected["source"]) / ("note-" + ticket)
        ).read_text() == "preserve rejected work"
        assert not (Path(rejected["source"]) / ("repair-" + ticket)).exists()
        assert graph.git("show", "integration:repair-" + ticket) == "verified repair"
        for gate in gates[1:4]:
            assert gate["revision"] == repaired["submitted_revision"]
            assert gate["passed"]
    assert len({g["stdout"] for g in record["gates"]}) == len(record["gates"])
    assert len({a["source"] for a in record["attempts"]}) == len(record["attempts"])
    for a in record["attempts"]:
        assert all(
            g["ticket"] == a["ticket"] and g["attempt"] == a["attempt"]
            for g in record["gates"][a["gate_start"] : a["gate_end"]]
        )
    assert graph.cli("status", graph.output).stdout == result.stdout


@pytest.mark.parametrize("mutation", ["delete", "directory", "hook", "source"])
def test_later_ticket_cannot_destroy_earlier_evidence_or_reuse_invalidated_approval(
    graph, mutation
):
    graph.config["max_repairs"] = 2
    target = graph.output / "artifacts/ticket-01-spec.stdout"
    if mutation == "hook":
        hook = graph.repo / ".git/hooks/pre-commit"
        hook.write_text(f"#!/bin/sh\nif [ \"$(cat last-ticket)\" = 03 ]; then\nrm '{target}'\nfi\n")
        hook.chmod(0o755)
    else:
        action = {
            "delete": "p.unlink()",
            "directory": "p.unlink(); p.mkdir(); (p / 'rejected').write_text('tampered directory')",
            "source": "p.write_text('tampered earlier source')",
        }[mutation]
        path = graph.output / "worktrees/ticket-01-spec/work-01" if mutation == "source" else target
        extend_agent(
            graph,
            "if a['ticket'] == '03' and a['role'] == 'implementation':\n"
            f"    p = Path({str(path)!r})\n    {action}",
        )
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert {t: s["state"] for t, s in record["tickets"].items()} == {
        "01": "Done",
        "02": "Pending",
        "03": "Blocked",
        "04": "Ready",
    }
    assert [(e["ticket"], e["role"]) for e in launches(graph)[::2]] == [
        ("01", "implementation"),
        ("01", "spec"),
        ("01", "standards"),
        ("03", "implementation"),
    ]
    assert graph.git("rev-parse", "integration") == record["tickets"]["01"]["done_revision"]
    assert record["tickets"]["03"]["attempt"] == 1
    if mutation == "source":
        spec = next(g for g in record["gates"] if g["ticket"] == "01" and g["stage"] == "spec")
        assert not spec["passed"]
        assert spec["verification_status"] == "invalidated"
    else:
        assert json.loads(target.read_text())["ticket"] == "01"
        assert "Integrity violation" in record["failure"]["message"]
        if mutation == "directory":
            integrity = record["gates"][-1]["integrity"][0]
            assert (Path(integrity["artifact"]) / "rejected").read_text() == "tampered directory"
    assert graph.cli("status", graph.output).stdout == result.stdout


def test_decision_stops_affected_ticket_without_unlocking_dependents_or_erasing_done_work(graph):
    graph.config["max_repairs"] = 2
    extend_agent(
        graph,
        "if a['ticket'] == '03' and a['role'] == 'implementation':\n"
        "    r.update(result='human-decision-needed', summary='Resolve approved contract',\n"
        "        unresolved_questions=['Which interface does the approved contract require?'])",
    )
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert record["outcome"] == "incomplete"
    assert {t: s["state"] for t, s in record["tickets"].items()} == {
        "01": "Done",
        "02": "Pending",
        "03": "Blocked",
        "04": "Ready",
    }
    assert [a["ticket"] for a in record["attempts"]] == ["01", "03"]
    assert record["tickets"]["03"]["human_decision"]["report"]["ticket"] == "03"
    assert graph.git("rev-parse", "integration") == record["tickets"]["01"]["done_revision"]
    assert graph.cli("status", graph.output).stdout == result.stdout


def test_later_candidate_cannot_overwrite_external_integration_movement(graph):
    graph.config["max_repairs"] = 2
    check = Path(graph.config["suite"][1])
    check.write_text(
        check.read_text()
        + "\nif stage == 'candidate' and Path('last-ticket').read_text() == '03':\n"
        f"    subprocess.run(['git', 'update-ref', 'refs/heads/integration', {graph.base!r}], check=True)\n"
    )
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert record["failure"]["stage"] == "integration"
    assert record["tickets"]["01"]["state"] == "Done"
    assert record["tickets"]["03"]["state"] == "Blocked"
    assert record["tickets"]["02"]["state"] == "Pending"
    assert graph.git("rev-parse", "integration") == graph.base
    assert record["integration_revision"] == record["tickets"]["01"]["done_revision"]
    assert [a["ticket"] for a in record["attempts"]] == ["01", "03"]


def test_failed_shared_baseline_does_not_launch_any_ticket_or_consume_repairs(graph):
    graph.config["max_repairs"] = 2
    graph.config["suite"] = [graph.config["agent"][0], "-c", "raise SystemExit(7)"]
    result = graph.run_ticket()
    assert result.returncode == 1
    record = graph.record()
    assert record["outcome"] == "environment"
    assert record["attempts"] == []
    assert [(g["stage"], g["attempt"], g["ticket"]) for g in record["gates"]] == [
        ("baseline", 0, None)
    ]
    assert launches(graph) == []
    assert all(t["attempt"] == 0 for t in record["tickets"].values())
    assert graph.git("rev-parse", "integration") == graph.base


def test_legacy_completion_evidence_without_ticket_mapping_still_accepts_normalized_id(graph):
    graph.config.update(ticket="03-work.md", selected_tickets=["03-work.md"])
    assert graph.run_ticket().returncode == 0
    completed = graph.output / "run.json"
    old = graph.record()
    del old["tickets"]
    old["ticket"]["id"] = "3"
    completed.write_text(json.dumps(old))
    path = graph.repo / "06-follow-up.md"
    path.write_text(
        "# 06: Follow up\nStatus: ready-for-agent\nBlocked by: 03\nChecks: ticket\n"
        "\n## Acceptance criteria\n- [ ] Follow up.\n"
    )
    graph.config.update(
        ticket=path.name,
        tickets=graph.config["tickets"] + [path.name],
        selected_tickets=[path.name],
        completed_runs=[str(completed)],
        base="integration",
    )
    graph.output = graph.home / "follow-up"
    result = graph.run_ticket()
    assert result.returncode == 0, result.stdout + result.stderr
    assert graph.record()["tickets"]["06"]["state"] == "Done"


def test_malformed_external_snapshot_mapping_rejects_before_any_new_execution(graph):
    graph.config.update(ticket="03-work.md", selected_tickets=["03-work.md"])
    assert graph.run_ticket().returncode == 0
    completed = graph.output / "run.json"
    old = graph.record()
    old["inputs"] = []
    completed.write_text(json.dumps(old))
    graph.config.update(
        ticket="01-value.md",
        selected_tickets=["01-value.md"],
        completed_runs=[str(completed)],
        base="integration",
    )
    graph.output = graph.home / "malformed-evidence"
    before = launches(graph)
    reject(graph, "invalid prerequisite completion evidence")
    assert launches(graph) == before
