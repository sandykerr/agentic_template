# Scripted single-ticket harness

Tickets 01–04 execute one selected approved ticket with scripted external agents,
validate its requirements and reports, and bind verification to exact revisions.
Repairs, dependency scheduling, timeouts, live Codex, and an operating-system
sandbox remain later numbered tickets. Run only trusted scripted processes and
project commands.

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

## Canonical input contract

`examples/scripted/project.json` remains a valid minimal example. Configuration is
a JSON object with the following fields. Unknown fields and duplicate keys
(including inside nested objects) are rejected instead of silently ignored.

| Field | Meaning |
| --- | --- |
| `repository` | Git target path, relative to the configuration file or absolute. |
| `base` | Starting commit/ref; must equal the existing integration branch tip. |
| `integration` | Existing local destination branch, not checked out in any worktree. |
| `spec`, `ticket` | Approved Markdown paths, relative to the target or absolute. |
| `tickets` | Optional nonempty array of all Markdown ticket paths in this requirements bundle, including `ticket`. Defaults to `[ticket]`. It provides dependency context, not a multi-ticket execution selection. Paths must be distinct after resolution. |
| `completed_runs` | Optional array of earlier harness `run.json` paths, relative to the configuration file or absolute; defaults to `[]`. These provide prerequisite completion evidence, described below. |
| `standards` | Paths for applicable project rules, AGENTS instructions, ADRs, and policy; list them explicitly. |
| `agent` | Argument array for the trusted scripted executable, used freshly for each role. |
| `suite` | Argument array for broader baseline and candidate checks. |
| `checks` | Nonempty mapping of named lightweight checks to argument arrays. |

All fields except `tickets` and `completed_runs` are required. Paths, refs, and
branch names must be nonempty strings; `standards` is an array of nonempty paths
(it may be empty). Approved files must exist and be readable. `checks` is a
nonempty mapping. Check names match `[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*`.
Every command, including unused named checks, must be a nonempty argument array
of nonempty strings without NUL characters, with an available executable.
Executable availability is checked without invoking it: names resolve on `PATH`;
absolute paths must name executable files. Relative executable paths must name
regular files tracked with executable mode (`100755`) in the approved base tree;
untracked files, caller-only permission changes, symlinks, and paths escaping the
worktree cannot supply a relative executable. Relative executable paths must not
contain `..` segments or end in `/` or `/.`. A bare name resolving through a relative
`PATH` entry is rejected; use an absolute executable path or a tracked `./path`.
Commands execute directly, without a shell, in their assigned detached worktree.
Relative executable/script arguments must also be available at the approved base
revision; preflight does not interpret arbitrary executable arguments or predict
runtime check success. `TICKET_HARNESS_STAGE` identifies the stage for commands.

Markdown uses the existing local tracker conventions:

```markdown
# 02: Follow-up

**Status:** ready-for-agent
**Blocked by:** [01: Change value](01-value.md)
**Checks:** ticket

## Acceptance criteria

- [ ] The follow-up has an observable result.
```

- The header has exactly one `# NN: Title`, with a nonempty title and positive
  decimal numeric ID. Leading zeroes normalize to at least two digits (`1`, `01`,
  and `001` all mean `01`). IDs must be unique across the bundle. A numeric
  `NN-` filename prefix must agree with the heading. Optional `ID:` and `Title:`
  metadata must agree too.
- Header metadata precedes the first `##` section. Both `Status: value` and
  `**Status:** value` forms work (likewise other fields). Whitespace around
  values is trimmed. Duplicate fields are rejected, even when repeated values
  agree. Other descriptive header fields such as `Scope:` remain prose.
  YAML front matter is unsupported and rejected; it cannot override the header.
- `Status:` must use a configured local readiness label: `needs-triage`,
  `needs-info`, `ready-for-agent`, `ready-for-human`, or `wontfix`. Only the
  selected ticket must be `ready-for-agent`. These are triage labels, never
  execution states or proof of prerequisite completion.
- `Blocked by:` is required. No dependencies may be written as `None`, `None.`,
  or the established `None (can start immediately).` form (the final period is
  optional). Otherwise use comma-separated IDs, `NN: Title` references, or
  `[NN: Title](relative-ticket-path.md)` links; a numeric-only link label also
  works. Titles containing commas can be referenced by ID alone. Supplied
  titles and resolved links must agree with the referenced ticket. Every
  dependency must exist in `tickets`; cycles, including self-cycles and cycles
  in unselected work, invalidate the bundle.
- Exactly one `## Acceptance criteria` section must contain at least one
  nonempty `- [ ]`, `- [x]`, or `* [ ]` checklist item (`X` also works). Empty
  checklist items are rejected even beside valid ones. Checked boxes carry
  acceptance text, never harness Done state. Fenced code examples and appended
  `## Comments` history do not supply requirements or metadata.
- Optional `Checks:` lists comma-separated configured check names with no
  duplicates. Omission means all configured checks. Empty or unknown references
  are rejected. Only referenced checks execute and appear in each assignment's
  `required_checks`; the broader `suite` always runs at baseline and candidate.

`run.json.requirements` records the normalized bundle, keyed by canonical ID.
Each entry has `id`, `title`, `readiness`, `dependencies` (canonical IDs),
`acceptance` (checklist text), `checks` (names), and `source` (absolute path).
Original Markdown/configuration bytes remain the approved snapshots.

Readiness and prerequisite satisfaction are independent. To select a dependent
ticket, include its prerequisites in `tickets` and provide their earlier
`run.json` records in `completed_runs`. Each record must report `outcome:
"completed"`, ticket `state: "Done"`, and a `done_revision` already ancestral to
the configured base in the target repository. Its approved ticket source and
SHA-256 must match the current approved prerequisite file. Missing, incomplete,
stale, duplicate, or unintegrated completion evidence rejects the run. A changed
prerequisite file requires fresh completion evidence; checked acceptance boxes
alone never suffice. Completion records are trusted local harness artifacts,
not an authenticated provenance system.

For example, add these fields to select the follow-up above after the earlier
fixture run completed (and use `base: "integration"`):

```json
{
  "ticket": "02-follow-up.md",
  "tickets": ["01-value.md", "02-follow-up.md"],
  "completed_runs": ["../passing-run/run.json"]
}
```

This is eligibility validation only: the harness executes exactly the selected
ticket, never queues or automatically runs its prerequisites. A preflight
rejection returns nonzero with `outcome: "invalid-input"`, an `inputs` failure
message naming the offending field/ticket, no gates or assignments, and attempt
0. No worker/check processes start, no Git worktrees are added, and integration
references remain unchanged. The new output directory may contain diagnostic
records and snapshots. Git/environment preflight also retains the original
base/integration/ref checks before execution.

The output must be a new directory outside the target repository and separate
from approved input files. Each approved file, including configuration, bundle
tickets, completion records, and standards, is copied verbatim to `inputs/`;
`run.json` stores its SHA-256 and
original path. Agent-editable source lives separately under `worktrees/`.

## Assignment and report contracts

Each assignment starts a fresh process with no conversation history. Standard
input is one JSON object containing `role` (`implementation`, `spec`, or
`standards`), `ticket`, `attempt` (1), `base_revision`, `revision`, role
`instructions`, approved `inputs` as text, `required_checks`, actual
`check_results` with artifact paths, and a `report_contract`. The full assignment
is saved before invocation. Reviewers can inspect `git diff BASE REVISION`.

Standard output must contain exactly one JSON object, with diagnostics on
standard error. Missing output, malformed JSON, duplicate keys (at any depth),
nonfinite numbers, extra JSON documents, and incorrect field types are rejected.
Extra diagnostic metadata such as `pid` is allowed but has no authority.
Object/array nesting is limited to 100 levels (the report object is level 1)
to leave serialization headroom for durable records and subsequent assignments.
The assignment's `report_contract` lists required fields, field types, permitted
outcomes, and finding requirements. Existing complete scripted reports remain valid.

Every report copies these identity fields **exactly**, including JSON types:

| Field | Required value/type |
| --- | --- |
| `role` | Assignment string: `implementation`, `spec`, or `standards`. For reviews this is the axis; no separate `axis` field is required. |
| `ticket` | Assignment string, including leading zeros (for example `"01"`). |
| `attempt` | Assignment integer (currently 1); boolean `true`, float `1.0`, and string `"1"` are invalid. |
| `base_revision` | Assignment's Git base commit string. |
| `revision` | Assignment's current source commit string: base for implementation, captured submission for reviews. |

Implementation reports additionally require all of these fields:

| Field | Required value/type |
| --- | --- |
| `result` | `"submitted"` or `"human-decision-needed"`; `"Done"` and other outcomes are invalid. |
| `summary` | Nonempty string. |
| `changed_files` | Array of nonempty strings describing claimed changes; may be empty. |
| `checks` | Array of nonempty strings describing claimed checks; may be empty. |
| `acceptance_evidence` | Array of nonempty strings; at least one entry for `submitted`. May be empty for `human-decision-needed`. |
| `unresolved_questions` | Array of nonempty strings; at least one question for `human-decision-needed`. May be empty for `submitted`. |

Whitespace-only strings are empty for validation purposes. Evidence is descriptive
text; the harness validates its shape and independently establishes Git changes
and check results. It does not treat claims as verified facts. Workers edit their
source worktree and leave committing to the harness. Claimed revisions, file
lists, checks, or execution state never override harness-owned observations.

A complete `human-decision-needed` report is recognized as valid but stops this
attempt with an incomplete outcome and a diagnostic containing its questions.
It does not capture a submission, run checks/reviews, integrate, or start repair.
Broader human-decision lifecycle handling belongs to ticket 06.

Review reports require a `findings` array, in addition to every identity field.
An empty array passes review only for the correct assignment and revision.
Every finding requires all of these fields, including optional suggestions:

| Field | Required value/type |
| --- | --- |
| `id` | Nonempty stable string, unique within this review. |
| `classification` | `"blocking"` or `"optional"`. |
| `location` | Nonempty string identifying code or the closest location for missing behavior. |
| `requirement` | Nonempty string identifying the requirement, project rule, or concrete design risk. |
| `consequence` | Nonempty string describing the impact. |
| `evidence` | Nonempty string supporting the finding. |
| `resolution` | Nonempty string suggesting a proportionate resolution. |
| `human_decision_needed` | JSON boolean (`true` or `false`), never an integer or string. |

A complete blocking finding fails the gate while remaining a valid report.
Optional findings are preserved and allow the gate to pass. Nonzero process exit
fails even with a complete success report; zero exit cannot replace a valid report.

The harness captures the submission, independently runs lightweight checks, and
uses separate detached worktrees and processes for the two review axes. A failed
gate stops this single attempt with preserved evidence; no repairs run.
Check and review worktrees must remain clean and on the submitted revision.
The harness rechecks earlier verified worktrees after each process and before
promotion. Changed HEAD, index, or working files invalidate the affected gate:
`passed` becomes false, `verification_status` is `invalidated`, and `diagnostic`
identifies the changed source. A structurally valid review report retains
`report_status: "valid"`; it cannot approve changed source. This attempt stops;
renewed checks and reviews are required before integration. Automatic repair is
ticket 05. These observations are not an enforced process sandbox (ticket 14).

The harness creates a real merge candidate with the starting integration
revision as first parent, tests it, and atomically updates the integration ref
using the expected previous revision. In this sequential slice, submission
descends from the starting integration revision. Candidate parents must be that
revision and submission, and its tree must equal the reviewed submission tree;
hook-created source resolutions require renewed review. The suite must leave
the exact candidate clean. Only that tested candidate becomes `done_revision`.
An external integration update causes compare-and-swap to fail; the harness
preserves the external tip, candidate, and diagnostics. Failed merges and failed
candidate suites also leave integration unchanged by the harness. Caller HEAD,
index, and working files stay untouched.

Approved source files and snapshots are checked against recorded SHA-256
identities before processes and promotion. Each process is bracketed by integrity
checks covering approved originals, snapshots, copies of approved paths in source
worktrees, `run.json`, assignments, and earlier process artifacts. A submitted
Git diff cannot change an approved input path, including through commit hooks.
Detected edits stop the attempt. Gate `integrity` entries record the path,
expected/observed SHA-256 (`null` for absent contents), and a rejected-content
artifact when bytes exist. Harness-owned snapshots and evidence are restored
from the pre-process bytes after rejected bytes are saved; changed original
inputs and source worktrees remain available for inspection. Restore original
requirements before starting a newly approved run.

Integrity checks observe process boundaries. They do not detect a transient edit
restored before the process returns, authenticate local artifacts, or prevent a
process with unrestricted filesystem/Git access from racing observations. Run
only trusted commands until role access enforcement is supplied by ticket 14.

## Records and artifacts

`run.json` records execution state (`Ready`, `Running`, `Verifying`, `Done`, or
`Blocked`), attempt number, inputs, base/submission/candidate/Done identities,
changed files, gates and findings, final outcome, failures, and artifact paths.
Records are replaced atomically so status does not read a partially written
success. This does not provide crash recovery or resume.

`artifacts/` holds each full assignment, standard output, and standard error;
gates record command arguments, working directory, revision, and exit code.
Agent gates also record the parsed `report` when JSON decoding and the nesting
limit check succeed,
`report_status` (`valid` or `invalid`), and a `diagnostic` on rejection. Report
validity is separate from gate success: a valid report with a nonzero process
exit, blocking finding, or human-decision outcome cannot pass. Invalid reports
set `passed: false`; undecodable or excessively nested output is available verbatim through `stdout`.
`failure` identifies the stage and reason. Run and status expose the same durable
record, including rejected implementation evidence and both review axes.
Worktrees and rejected Git commits remain available for inspection. To remove a
run after inspection, remove its worktrees with `git worktree remove` (use
`--force` only for disposable rejected changes), then delete its output folder.
