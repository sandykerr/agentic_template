# Scripted single-ticket harness

Ticket 01 implements one approved, dependency-free ticket with scripted external
agents. It does not implement repairs, scheduling, timeouts, live Codex, complete
input/report validation, or an operating-system sandbox. Those remain later
numbered tickets. Run only trusted scripted processes and project commands.

## Python and checks

Use the reusable micromamba Python environment described in
[Python environment guidance](agents/python-environment.md). The runtime uses only
Python 3.12+ and Git. From this checkout, `python -m ticket_harness` requires no
installation. For an installed `ticket-harness` command, install the project with
`python -m pip install '.[dev]'`. The `dev` extra pins pytest, mypy, and Ruff;
packaging uses a pinned setuptools build backend.

For isolated check tools, create a disposable micromamba prefix:

```bash
micromamba --root-prefix /tmp/ticket-harness-mamba create --yes \
  --prefix /tmp/ticket-harness-env --channel conda-forge \
  python=3.12.16 pytest=9.2.0 mypy=1.19.1 ruff=0.14.10
```

With that environment's `bin` directory on `PATH`, run:

```bash
python -m pytest
python -m mypy
python -m ruff check ticket_harness tests examples
python -m ruff format --check ticket_harness tests examples
```

Tests use the public CLI, scripted external processes, real temporary Git
repositories, and observable Git/record artifacts. No network or model is needed.

## Run the minimal fixture

From this checkout, with the micromamba environment's Python on `PATH`:

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

`run` intentionally approves the chosen requirements and commands. Exit 0 means
Done; nonzero means invalid inputs, environment failure, or incomplete work, as
recorded in `outcome` and `failure`. `status RUN_DIRECTORY` prints `run.json`
without running processes or modifying source or records; exit 0 means the
record was read, including for an incomplete run.

To demonstrate rejection, repeat with a fresh fixture and add `"candidate"` as
the last argument in its configured `suite`. Baseline passes, but the candidate
suite exits nonzero. The run is incomplete, the integration branch stays at the
baseline, and the submitted/candidate revisions and logs remain inspectable.
Alternatively, append `["--reject", "spec"]` or `["--reject", "standards"]` to
`agent` for a blocking review.

## Minimal input contract

`examples/scripted/project.json` is the canonical ticket-01 example:

| Field | Meaning |
| --- | --- |
| `repository` | Git target path, relative to the configuration file or absolute. |
| `base` | Starting commit/ref; must equal the existing integration branch tip. |
| `integration` | Existing local destination branch, not checked out in any worktree. |
| `spec`, `ticket` | Approved Markdown paths, relative to the target or absolute. |
| `standards` | Paths for applicable project rules, AGENTS instructions, ADRs, and policy; list them explicitly. |
| `agent` | Argument array for the trusted scripted executable, used freshly for each role. |
| `suite` | Argument array for broader baseline and candidate checks. |
| `checks` | Nonempty mapping of named lightweight checks to argument arrays. |

Check names contain letters, numbers, or hyphens. Commands execute directly,
without a shell, in their assigned detached worktree. Use absolute executable
paths or executables available on `PATH`; relative script arguments resolve in
the worktree. `TICKET_HARNESS_STAGE` identifies the stage for commands.

The ticket starts with `# NN: Title`, retains the authoring readiness line
`**Status:** ready-for-agent`, declares `**Blocked by:** None`, and contains
`## Acceptance criteria` with Markdown checklist items. The numeric heading is
the stable identifier. This slice accepts one dependency-free ticket; it does not
silently execute prerequisites or interpret other readiness labels as execution
states. General Markdown normalization and comprehensive validation are ticket 02.

The output must be a new directory outside the target repository and separate
from approved input files. Each approved file, including configuration and
standards, is copied verbatim to `inputs/`; `run.json` stores its SHA-256 and
original path. Agent-editable source lives separately under `worktrees/`.

## Assignment and report contracts

Each assignment starts a fresh process with no conversation history. Standard
input is one JSON object containing `role` (`implementation`, `spec`, or
`standards`), `ticket`, `attempt` (1), `base_revision`, `revision`, role
`instructions`, approved `inputs` as text, `required_checks`, actual
`check_results` with artifact paths, and a `report_contract`. The full assignment
is saved before invocation. Reviewers can inspect `git diff BASE REVISION`.

Standard output must contain one JSON report, with diagnostics on standard
error. Every report copies the five identity fields from the assignment:
`role`, `ticket`, `attempt`, `base_revision`, and `revision`.

Implementation reports use `result: "submitted"` and include `summary`, claimed
`changed_files`, claimed `checks`, `acceptance_evidence`, and
`unresolved_questions`. Workers edit their source worktree and leave committing
to the harness. A report cannot declare Done; the harness derives changed files
and the submission revision from Git.

Review reports contain a `findings` array. An empty list approves that exact
revision. A finding carries `id`, `classification` (`blocking` or `optional`),
`location`, `requirement`, `consequence`, `evidence`, `resolution`, and
`human_decision_needed`. The initial parser verifies assignment identity,
submitted result, and review classification; comprehensive required-field and
finding-evidence validation is ticket 03. Nonzero process exit always fails.

The harness captures the submission, independently runs lightweight checks, and
uses separate detached worktrees and processes for the two review axes. A failed
gate stops this single attempt with preserved evidence; no repairs run.
Review worktrees must remain clean and on the submitted revision. This detects
ordinary edits; it is not an enforced read-only process sandbox (ticket 14).

The harness creates a real merge candidate with the starting integration
revision as first parent, tests it, and atomically updates the integration ref
using the expected previous revision. Only that tested candidate becomes
`done_revision`. Caller HEAD, index, and working files stay untouched. The
broader tampering/race matrix is ticket 04.

## Records and artifacts

`run.json` records execution state (`Ready`, `Running`, `Verifying`, `Done`, or
`Blocked`), attempt number, inputs, base/submission/candidate/Done identities,
changed files, gates and findings, final outcome, failures, and artifact paths.
Records are replaced atomically so status does not read a partially written
success. This does not provide crash recovery or resume.

`artifacts/` holds each full assignment, standard output, and standard error;
gates record command arguments, working directory, revision, and exit code.
Worktrees and rejected Git commits remain available for inspection. To remove a
run after inspection, remove its worktrees with `git worktree remove` (use
`--force` only for disposable rejected changes), then delete its output folder.
