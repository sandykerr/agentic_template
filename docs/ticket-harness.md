# Ticket harness

The harness runs explicitly approved tickets sequentially through trusted scripted
agents, project checks, independent reviews, bounded repairs and local Git
integration. Approved milestone plans add exact-candidate human QA, promotion and
planned stop/continuation. Live model execution, continuing unrelated work after a
block and OS sandboxing remain later work; use the [feature index](../.scratch/ticket-harness/README.md)
for development status.

Choose the reference for the task:

| Task | Read |
| --- | --- |
| Use or create a Python environment | [Environment guidance](agents/python-environment.md) |
| Develop the harness or choose/run checks | [Testing policy and commands](agents/testing.md) and [development review contract](agents/review-records.md) |
| Configure a target, ticket bundle or executable milestone plan | [Runtime inputs](ticket-harness/inputs.md) |
| Inspect, accept, stop or continue a milestone candidate | [Runtime QA](ticket-harness/qa.md) |
| Implement a scripted agent or diagnose reports, repairs and artifacts | [Agent and execution reference](ticket-harness/agents.md) |

## Python and checks

Use Python 3.12+, Git and POSIX process groups. The tests additionally use Linux
`/proc` to observe child termination. Follow [environment guidance](agents/python-environment.md)
before Python or dependency changes; [testing guidance](agents/testing.md#check-commands)
owns development tool setup and check commands.

From this checkout, `python -m ticket_harness` requires no installation. For an
installed `ticket-harness` command, install with `python -m pip install '.[dev]'`;
both entry points support the same subcommands. Commands and Git hooks run as
trusted local processes with unrestricted access; read the
[trust and integrity limits](ticket-harness/agents.md#trust-and-integrity).

## Run the minimal fixture

From this checkout, with the environment's Python on `PATH`:

```bash
fixture=$(mktemp -d /tmp/ticket-harness-fixture.XXXXXX)
cp -R examples/scripted "$fixture/target"
git -C "$fixture/target" init -b main
git -C "$fixture/target" add .
git -C "$fixture/target" -c user.name=Fixture \
  -c user.email=fixture@example.invalid commit -m 'Fixture baseline'
git -C "$fixture/target" branch integration
python -m ticket_harness run --config "$fixture/target/project.json" \
  --output "$fixture/passing-run"
python -m ticket_harness status "$fixture/passing-run"
```

No network or model is needed. Starting `run` intentionally approves the chosen
requirements and commands. Run output and `status RUN_DIRECTORY` print the same
JSON as `run.json`; status only reads the record and exits 0 even for incomplete
work. It launches no processes, changes no records and does not revalidate candidates.

For `run`/`continue`, exit 0 means every selected ticket is Done in legacy mode,
or final human-accepted promotion in milestone mode. A successful planned stop
makes the owning process exit 2; other unsuccessful runs record their `outcome`
and `failure`. See [runtime QA](ticket-harness/qa.md) for stop acknowledgements,
QA waits and continuation.

To demonstrate rejection, use a fresh fixture and append `"candidate"` to its
configured `suite` argument array. Baseline passes; candidate regression fails,
integration stays at baseline and revisions/logs remain inspectable. Alternatively,
append `["--reject", "spec"]` or `["--reject", "standards"]` to `agent` for a blocker.

## Approved milestone plans

A configuration's `plan` enables fixed groups, feature-to-development candidate
preparation and foreground human QA waits. All tickets Done still requires final
acceptance. Read the [plan JSON contract](ticket-harness/inputs.md#approved-milestone-plans)
and [candidate, acceptance and stop/continuation procedure](ticket-harness/qa.md).
Planning skills produce authoring documents; they do not automatically produce
executable runtime JSON or grant candidate acceptance.

## Canonical input contract

[Runtime inputs](ticket-harness/inputs.md) defines configuration/path rules,
accepted Markdown, prerequisite evidence, selection modes and preflight rejection.

## Assignment and report contracts

[Assignments and reports](ticket-harness/agents.md#assignment-and-report-contracts)
defines the stdin/stdout JSON protocol, exact identities and decision handling.

## Optional review suggestions

[Reading findings](ticket-harness/agents.md#optional-review-suggestions) explains
optional suggestions, report-local IDs and which attempt/revision to inspect.

## Stage timeouts and cleanup

[Timeouts and process cleanup](ticket-harness/agents.md#stage-timeouts-and-cleanup)
defines allowances, failure precedence and process-group limits.

## Records and artifacts

[Records and artifacts](ticket-harness/agents.md#records-and-artifacts) explains
run state, attempts, gates, source identities and retained output. Inspect rejected
work before removing its Git worktrees with `git worktree remove` (`--force` only
for disposable rejected changes), then delete the output directory.

## Finding the code

| Owner | Responsibility |
| --- | --- |
| [runner.py](../ticket_harness/runner.py) | Run coordination, verification and canonical checkpoint restoration. |
| [tickets.py](../ticket_harness/tickets.py) | Ticket eligibility, implementation and bounded repairs. |
| [qa.py](../ticket_harness/qa.py) | Candidate/request/evidence, acceptance, stop, continuation and promotion. |
| [git.py](../ticket_harness/git.py) | Worktrees, submissions, merge validation and branch transactions. |
| [records.py](../ticket_harness/records.py) | Process cleanup, output, protection and atomic writes. |
| [agents.py](../ticket_harness/agents.py) | Assignments and report formats. |
| [inputs.py](../ticket_harness/inputs.py) / [plans.py](../ticket_harness/plans.py) | Approved inputs, configuration, dependency and plan validation. |

Public commands and saved formats are caller/test contracts. For design authority
and rationale, follow the [approved spec](../.scratch/ticket-harness/spec.md) and
[ADRs](adr/). Development review records/checkpoints do not change runtime schemas;
their enforcement remains separate from the scripted harness.
