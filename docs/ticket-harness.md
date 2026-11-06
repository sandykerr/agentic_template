# Scripted sequential ticket harness

Tickets 01–09 execute explicitly selected approved tickets sequentially with scripted external agents,
validate its requirements and reports, bind verification to exact revisions, and
repair rejected submissions within a configured allowance, stopping immediately
when a valid report requires a human decision outside approved contracts.
Optional review suggestions remain visible without requiring repair or delaying integration.
Stage timeouts stop stalled processes and their process-group descendants.
Continuing unrelated work after a blocked ticket, live Codex, and an operating-system
sandbox remain later numbered tickets. Run only trusted scripted processes and
project commands.

## Python and checks

Use the [testing policy](agents/testing.md) to select focused development checks,
preserve the full-suite completion gate, and capture evidence without redundant runs.

Use the reusable micromamba Python environment described in
[Python environment guidance](agents/python-environment.md). The runtime uses only
Python 3.12+, Git, and POSIX process groups (the fixtures also use Linux `/proc`
to observe child termination). From this checkout, `python -m ticket_harness` requires no
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
| `selected_tickets` | Optional nonempty array of ticket paths to execute, relative to the target or absolute. Defaults to `[ticket]`; must include `ticket` and be a subset of `tickets`, with distinct resolved paths. Bundle context alone never selects work. |
| `completed_runs` | Optional array of earlier harness `run.json` paths, relative to the configuration file or absolute; defaults to `[]`. These provide prerequisite completion evidence, described below. |
| `standards` | Paths for applicable project rules, AGENTS instructions, ADRs, and policy; list them explicitly. |
| `agent` | Argument array for the trusted scripted executable, used freshly for each role. |
| `suite` | Argument array for broader baseline and candidate checks. |
| `checks` | Nonempty mapping of named lightweight checks to argument arrays. |
| `max_repairs` | Optional nonnegative integer; defaults to `2` repairs after the initial assignment. `0` stops on the first rejection. Booleans, floats, strings, and null are invalid. |
| `timeouts` | Optional object overriding stage allowances in seconds; omitted keys use the defaults below. Every supplied value must be a positive finite JSON number no greater than `604800` (one week). Booleans, strings, null, unknown stages, and unsafe numeric ranges are rejected before any worker/check starts. |

All fields except `tickets`, `selected_tickets`, `completed_runs`, `max_repairs`, and `timeouts` are required. Paths, refs, and
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
  `needs-info`, `ready-for-agent`, `ready-for-human`, or `wontfix`. Every
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

Readiness and prerequisite satisfaction are independent. Include every prerequisite
in `tickets`. Select prerequisites for execution in this run or provide their
earlier `run.json` records in `completed_runs`. Each completion record must report
`outcome: "completed"`; every entry in its `tickets` mapping must be `Done`,
with a `done_revision` already ancestral to the configured base. Legacy records
without `tickets` use their single `ticket` entry. Every completed ticket must
exist in the current bundle, and its approved source path and SHA-256 must match
the current prerequisite file. Missing, incomplete, stale, duplicate, or
unintegrated completion evidence rejects the run. A changed prerequisite file
requires fresh completion evidence; checked acceptance boxes alone never suffice.
Completion records are trusted local harness artifacts, not an authenticated
provenance system. Explicitly selected prerequisites must reach Done again in
this run; external evidence cannot unlock their dependents early.

For example, add these fields to select the follow-up above after the earlier
fixture run completed (and use `base: "integration"`):

```json
{
  "ticket": "02-follow-up.md",
  "tickets": ["01-value.md", "02-follow-up.md"],
  "completed_runs": ["../passing-run/run.json"]
}
```

To execute a dependency graph in one run, explicitly select its tickets:

```json
{
  "ticket": "02-follow-up.md",
  "tickets": ["01-value.md", "02-follow-up.md", "03-independent.md", "04-human-context.md"],
  "selected_tickets": ["02-follow-up.md", "03-independent.md", "01-value.md"]
}
```

After preflight validates the entire bundle and all commands, the broader starting
baseline runs once. At each selection, the harness chooses the lowest **numeric**
canonical ID among Ready selected tickets, independently of configuration order.
Unselected agent-ready and human-ready context never executes automatically.
A ticket is Pending until all its prerequisites are either externally verified
at the starting base or Done in this run. Integration promotion precedes Done and
unlocking. There is at most one active implementation ticket, including repairs;
its checks, both reviews and exact-candidate broader suite complete before the
next selection. Every new ticket starts at the latest verified integration tip,
including already completed independent changes. Its assignment `base_revision`
is fixed to that tip across its own repairs. Each assignment's `inputs.ticket`
is the active ticket's approved content; other bundle snapshots remain context.
`required_checks` and `check_results` contain that ticket's checks and reports,
plus the shared baseline, without transferring earlier tickets' findings or approvals.
The durable record retains all earlier evidence.

Success requires every selection to reach Done. This slice stops the run on the
first blocked ticket or shared environment failure; selected dependents remain
Pending and unrelated selections retain their observed Ready state. Continuing
unrelated work after a block belongs to ticket 10. A shared baseline failure
launches no workers and consumes no repairs; the compatibility `ticket` entry
(the configured primary before execution) becomes Blocked and other selections
retain their pre-baseline states. Integration changes made outside the harness
are never overwritten by candidate promotion.

A preflight rejection returns nonzero with `outcome: "invalid-input"`, an `inputs` failure
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
`standards`), `ticket`, `attempt` (1 for the initial assignment, then 2, 3, ...), `base_revision`, `revision`, role
`instructions`, approved `inputs` as text, `required_checks`, actual
`check_results` with artifact paths, and a `report_contract`. The full assignment
is saved before invocation. Reviewers can inspect `git diff BASE REVISION`.
Repairs retain role `implementation`. Their `revision` is the starting source
commit, while `base_revision` remains the original approved integration revision.
`repair_context` is null for the initial assignment and reviews; for repairs it
contains the previous `failure` (stage/message) and all recorded
`rejected_revisions` (submission and candidate identities). `check_results`
contains the complete prior gate history, including parsed findings, diagnostics,
and readable stdout/stderr paths. Failed Git operations include their diagnostic
in the failure message. Workers receive current working contents in a fresh
detached worktree, including uncommitted edits after invalid reports; previous
worktrees remain inspectable. Reports must copy the new attempt identity exactly.

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
| `attempt` | Assignment integer; stale attempts, booleans, floats, and strings are invalid. |
| `base_revision` | Assignment's Git base commit string. |
| `revision` | Assignment's current source commit string: starting source for implementation/repair, captured submission for reviews. |

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

A complete `human-decision-needed` report stops the attempt with an incomplete
outcome, even if the process exits nonzero. Describe the precise decision and
relevant approved requirement or interface in `summary`/`unresolved_questions`,
and available evidence in `acceptance_evidence`. These existing fields remain the
report contract; no new report fields are required. Current work stays in its
worktree without submission capture, further checks/reviews, integration, or repair.

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

A blocking finding with `human_decision_needed: true` from either review axis
stops immediately, including on nonzero process exit. Use `requirement` to identify
the approved contract, `evidence`/`consequence` to explain the conflict, and
`resolution` for the precise decision needed. The diagnostic includes the
requirement and resolution. A blocking decision finding takes precedence
over ordinary repairable blockers in the same validated report. Optional findings
retain their non-blocking behavior, including when their decision flag is true.
The entire report must pass identity, shape, and evidence validation before any
decision is recognized; invalid decision-like output follows ordinary bounded
report-failure handling. Report claims never become verified source/check facts.

Both kinds of decision leave the ticket Blocked and the run incomplete without
consuming the remaining repairs or launching subsequent verification processes.
Approved spec, ticket, and standards stay unchanged; integration stays at its
last verified revision. Later-repair decisions retain all previous attempts,
rejected revisions, prompts, and output. The harness hands off the conflict for
human resolution rather than inferring requirements or changing an approved
interface. Starting a new run after a decision requires human-approved inputs;
this slice does not provide continuation or resume.

The harness captures the submission, independently runs lightweight checks, and
uses separate detached worktrees and processes for the two review axes. A failed
gate rejects the attempt with preserved evidence and enters the remaining repair
allowance. Lightweight-check failures, either blocking review axis, failed merges,
and failed candidate suites can request repair. Missing/invalid reports and process
failures use this same allowance, with no secondary retries. Worker-internal
editing/testing iterations consume only their single assignment.

Every repaired submission is captured as a new commit (even if a repair only
requires rerunning verification), with changed paths derived against the original
base. Applicable lightweight checks, both fresh reviews, and a new exact candidate
suite must pass. Rejected attempts' approvals never authorize the new source;
source validation starts again for the new attempt while retaining the shared
baseline check. Exhaustion leaves the ticket Blocked with an incomplete outcome,
all rejected revisions/worktrees and full history intact. Baseline and preflight
failures start no attempts. Valid human-decision reports, approved-input
or evidence integrity violations, worker-owned HEAD changes, and external
integration movement stop without authorizing more repairs. Repairs cannot change
the approved baseline or requirements. Timeouts share this same repair allowance.
Check and review worktrees must remain clean and on the submitted revision.
Assume-unchanged and skip-worktree index flags are rejected so tracked edits
cannot be concealed from source validation.
The harness rechecks earlier verified worktrees after each process and before
promotion. Changed HEAD, index, or working files invalidate the affected gate:
`passed` becomes false, `verification_status` is `invalidated`, and `diagnostic`
identifies the changed source. A structurally valid review report retains
`report_status: "valid"`; it cannot approve changed source. This attempt stops;
renewed checks and reviews are required before integration. These observations
are not an enforced process sandbox (ticket 14).

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
index, and working files stay untouched. Git hooks are disabled for the final
atomic ref update so user code cannot run after final validation. Checkout,
submission, and merge hooks execute within the integrity checks described below.

Approved source files and snapshots are checked against recorded SHA-256
identities before processes and promotion. Each process and hook-capable Git
worktree/submission/merge operation is bracketed by integrity
checks covering approved originals, snapshots, copies of approved paths in source
worktrees, `run.json`, assignments, and earlier process artifacts. A submitted
Git diff cannot change an approved input path, including through commit hooks.
Detected edits stop the attempt. Gate or Git operation `integrity` entries record the path,
expected/observed SHA-256 (`null` for absent or unreadable file contents), and a rejected-content
artifact when bytes exist. A directory replacing a harness-owned file is moved
intact to its rejected artifact before restoration. Harness-owned snapshots and evidence are restored
from the pre-process bytes after rejected bytes are saved; changed original
inputs and source worktrees remain available for inspection. Restore original
requirements before starting a newly approved run.

Integrity checks observe process boundaries. They do not detect a transient edit
restored before the process returns, authenticate local artifacts, or prevent a
process with unrestricted filesystem/Git access from racing observations. Run
only trusted commands until role access enforcement is supplied by ticket 14.

## Optional review suggestions

Both review axes accept complete findings classified as `optional`. They do not
fail a review, consume a repair allowance, or request a human decision, even when
their `human_decision_needed` flag is true. Every optional finding still requires
all documented finding fields and exact report identity. Whole-report validation
and process success remain required: malformed optional evidence or a nonzero
review exit cannot approve a submission.

Run and status print the same indented, human-readable JSON as `run.json`.
Read each Spec/Standards gate's `report.findings` for suggestions, including its
location, requirement, consequence, evidence and suggested resolution. For example,
a passing gate can contain `"classification": "optional"` while the ticket is
`"state": "Done"`. The gate and report's `attempt` and `revision` identify the
reviewed submission; `base_revision` identifies the fixed approved baseline.
`ticket.done_revision` identifies the separately tested candidate merge.

When blocking and optional findings coexist, the ordinary blocking failure
triggers bounded repair. The repair assignment's `repair_context.failure` names
the rejected stage, and `check_results` retains the complete review report.
Optional findings in that history are context, not mandatory repair requirements.
A blocking finding requiring a human decision still stops immediately under the
decision rules above. A passing repaired ticket may retain an unimplemented
optional suggestion.

Earlier gate reports and artifacts remain attached to their original reviewed
revisions, including after a successful repair or exhausted allowance. Each new
submission requires renewed checks and fresh reviews. A suggestion may disappear,
appear, or reuse an ID in a new report; its ID is unique only within that report.
Read `attempts` and their gate ranges to distinguish earlier suggestions from the
latest review. No earlier finding or approval is transferred to a later revision,
and retained history does not assert that a disappeared suggestion was resolved.
Status only reads these durable observations and launches no agents.

## Stage timeouts and cleanup

Timeouts are wall-clock process allowances, including assignment input delivery
and output collection. Configure independent allowances with `timeouts`:

| Key | Default seconds | Invocation |
| --- | --- | --- |
| `implementation` | 1800 | Initial implementation assignment. |
| `repair` | 1800 | Each later implementation assignment; role remains `implementation`. |
| `spec` | 900 | Spec review on every attempt. |
| `standards` | 900 | Standards review on every attempt. |
| `checks` | 300 | Each configured lightweight check, separately. |
| `baseline` | 1800 | Starting broader suite, attempt 0. |
| `candidate` | 1800 | Exact candidate suite on every attempt. |

For example, `"timeouts": {"checks": 60, "baseline": 1200, "candidate": 2400}`
uses defaults for all agent roles. Fractional seconds are allowed. The one-week
upper bound avoids platform pipe-wait overflow; no timeout is disabled or infinite.
Existing command arrays, assignment identities and report schemas are unchanged.

Each invocation starts a new POSIX session/process group. At timeout the harness
sends SIGKILL to that group, stopping the command and inherited descendants,
including children that ignore SIGTERM. It collects available stdout/stderr as
bytes into their artifacts. Output pipes also keep the deadline active if the
leader exits while children retain output handles. Even a complete report and a
zero leader exit cannot approve that timed-out stage or request a trusted human
decision: `report_status` is `not-evaluated`, with raw output retained for inspection.
Completed, non-timed-out reports retain whole-report validation and the existing
human-decision precedence, including nonzero exits.

Final output draining and leader reaping each have a separate five-second cleanup
bound. Failure to drain/reap or an unavailable executable is a shared execution
environment failure: `outcome: "environment"`, no further repairs, and an
`execution_error` on the gate. Ordinary stage timeouts enter the existing repair
allowance or finish Blocked/incomplete when exhausted. A baseline timeout is an
environment outcome with attempt 0 and no worker assignment. Cleanup runs before
integrity checks and repair copying, preserving stopped work and earlier evidence.
The group is also killed at normal command completion to stop leftover background
children. Commands are trusted and must keep descendants in their inherited
process group; this mechanism does not supply an OS sandbox or contain a process
that deliberately detaches into another session/group. Git operations/hooks are
still governed by the existing integrity checks; this ticket adds deadlines to
configured worker/reviewer/check invocations, not arbitrary Git plumbing.

Each gate records `timeout_category`, `timeout_seconds`, and `timed_out`, alongside
its unchanged stage, actual attempt, revision, argv, output paths and exit code.
`cleanup` identifies the `process_group`, `signal` (`SIGKILL`), and whether a signal
was `sent`. A timed-out leader may already have exit code 0; `timed_out: true`
always fails. The diagnostic names the stage and allowance. Attempts retain the
failure and gate range; run/status expose the resulting outcome and latest ticket
state. Repairs receive this complete gate/output evidence through `check_results`
and the previous failure through `repair_context`; no timeout-specific retry loop
or reuse of an earlier approval exists.

`tests/test_timeouts.py` drives controlled finite scripted processes with a generous
external CLI watchdog, asserting process/child termination through Linux `/proc`,
partial output, report precedence, fresh repairs and exact candidate integration,
exhaustion, preflight/baseline/environment failures, and evidence protection.
Setting `TICKET_HARNESS_TEST_OBSERVATIONS` to a directory retains each case's actual
record, output text, integration revision, and caller status before fixture cleanup.

## Records and artifacts

`run.json` records execution state (`Pending`, `Ready`, `Running`, `Verifying`, `Done`, or
`Blocked`), attempt number, inputs, base/submission/candidate/Done identities,
changed files, gates and findings, final outcome, failures, and artifact paths.
`max_repairs` records the normalized repair allowance; `timeouts` records all
normalized stage allowances in seconds. `attempts` is ordered and records
each assignment's `attempt`, `starting_revision`, source worktree path, state
(`Running`, `Verifying`, `Rejected`, or `Done`), observed submission/changed files
and candidate when available, and a failure stage/message on rejection.
`gate_start` (inclusive) and `gate_end` (exclusive, set when the attempt ends)
index that attempt's gates in the complete top-level `gates` array. Gate and
operation `attempt` is zero for baseline work and positive for ticket attempts.
`selected_tickets` lists selected canonical IDs in numeric order; `tickets` maps
each to its observed state, attempt and available submitted/candidate/Done identities.
Context-only tickets appear in `requirements`, never in this execution mapping.
`integration_revision` records the last tip verified/promoted by this run; it is
historical evidence if an external process later moves the branch. `base_revision`
remains the run's starting base. The top-level `ticket` mirrors the active or last
attempted ticket for compatibility (the configured primary before assignments).
Earlier identities remain in `attempts`. Every attempt, gate and Git operation
carries `ticket` as its canonical ID; shared baseline gates/operations use null.
Gate ranges still index the complete run-wide `gates` array, and each ticket's
attempt numbering and repair allowance start afresh. A successful repair retains rejected
failure evidence there while the run's final outcome is completed.
When a valid report requests a human decision, the latest `ticket` and affected
`attempts` entry also expose `human_decision`: the `role`, actual `attempt` and
assigned `revision`, complete validated `report`, approved input paths/snapshots
and SHA-256 identities in `approved_inputs`, and `assignment`, `stdout`, `stderr`
artifact paths. The implementation source path remains on the attempt; the gate's
`cwd` identifies the reporting worktree. The report retains the precise questions
or complete review findings, including the contract and available evidence.
This handoff is descriptive evidence, not a passing gate or approval. A nonzero
exit remains recorded and appears alongside the decision diagnostic. Attempt
counters and gate ranges include only assignments and processes actually run;
the stopped attempt is `Rejected` while the ticket is `Blocked`. Run's final JSON
and read-only status display the same handoff and preserved history.
`operations` records Git worktree preparation, submission capture, and candidate
merge stages, with `passed` and integrity diagnostics when applicable. These are
separate from check/agent gates; rejected observed revisions remain on the ticket
or in the retained Git worktree if an operation failed before returning a revision.
Records are replaced atomically so status does not read a partially written
success. This does not provide crash recovery or resume.

`artifacts/` holds each full assignment, standard output, and standard error;
initial names remain `implementation`, `spec`, `standards`, `check-NAME`, and
`candidate`; later attempts prefix artifact/worktree/operation names with
`attempt-2-`, `attempt-3-`, etc. This cannot collide with configured check names.
For multi-ticket selections, all ticket-specific artifact/worktree/operation
names additionally begin `ticket-ID-` (for example `ticket-03-attempt-2-spec`);
the shared baseline stays `baseline`. Single-ticket selections retain the existing
names. Earlier ticket evidence remains protected during later tickets and repairs.
Stage names and `TICKET_HARNESS_STAGE` retain their original role/check
values. Prior artifacts are protected against overwrite by later processes and
Git hooks. No attempt reuses a previous worktree or assignment process.
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
