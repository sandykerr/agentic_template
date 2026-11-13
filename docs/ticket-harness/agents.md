# Scripted agents, execution and records

Use this reference when adapting a scripted agent or interpreting execution,
failures and saved evidence. See [inputs](inputs.md) for approved configuration,
[QA](qa.md) for milestone promotion/continuation, and the
[harness guide](../ticket-harness.md) for operator commands.

## Assignment and report contracts

Each assignment starts a fresh process without conversation history. Standard
input is one JSON object containing `role` (`implementation`, `spec`, or
`standards`), `ticket`, `attempt` (initially 1, then 2, 3, ...), `base_revision`,
`revision`, role `instructions`, approved `inputs` as text, `required_checks`,
actual `check_results` with artifact paths, and `report_contract`. The full
assignment is saved before invocation. Reviewers can inspect `git diff BASE REVISION`.

Repairs retain role `implementation`; their `revision` is the starting source
commit and `base_revision` remains the original approved integration revision.
`repair_context` is null for initial assignments and reviews; for repairs it
contains previous `failure` (stage/message) and all recorded `rejected_revisions`
(submission/candidate identities). `check_results` contains complete prior gate
history, parsed findings, diagnostics and readable stdout/stderr paths. Failed Git
operations include their diagnostic in the failure message. Workers receive current
working contents in a fresh detached worktree, including uncommitted edits after
invalid reports; previous worktrees remain inspectable. Reports copy the new
attempt identity exactly.

Standard output must contain exactly one JSON object; diagnostics go to standard
error. Missing output, malformed JSON, duplicate keys at any depth, nonfinite
numbers, extra JSON documents and incorrect field types reject. Extra diagnostic
metadata such as `pid` is allowed without authority. Object/array nesting is
limited to 100 levels (report object is level 1), leaving serialization headroom
for records/subsequent assignments. `report_contract` lists required fields/types,
permitted outcomes and finding requirements. Existing complete scripted reports
remain valid.

Every report copies these identity fields **exactly**, including JSON types:

| Field | Required value/type |
| --- | --- |
| `role` | Assignment string: `implementation`, `spec`, or `standards`. Review role is the axis; no separate `axis` field is required. |
| `ticket` | Assignment string, including leading zeros (for example `"01"`). |
| `attempt` | Assignment integer; stale attempts, booleans, floats and strings are invalid. |
| `base_revision` | Assignment's Git base commit string. |
| `revision` | Assignment's current source commit string: starting source for implementation/repair, captured submission for reviews. |

### Implementation reports

All these fields are required:

| Field | Required value/type |
| --- | --- |
| `result` | `"submitted"` or `"human-decision-needed"`; `"Done"` and other outcomes are invalid. |
| `summary` | Nonempty string. |
| `changed_files` | Array of nonempty strings describing claimed changes; may be empty. |
| `checks` | Array of nonempty strings describing claimed checks; may be empty. |
| `acceptance_evidence` | Array of nonempty strings; at least one entry for `submitted`. May be empty for `human-decision-needed`. |
| `unresolved_questions` | Array of nonempty strings; at least one question for `human-decision-needed`. May be empty for `submitted`. |

Whitespace-only strings are empty. Evidence is descriptive text: the harness
validates shape and independently establishes Git changes/check results. Claimed
revisions, file lists, checks and execution state never override its observations.
Workers edit their source worktree and leave committing to the harness.

### Review reports

Reviews require `findings`, an array, plus every identity field. An empty array
passes only for the correct assignment/revision and successful process exit.
Every finding, including optional suggestions, requires all these fields:

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

A blocking finding fails the gate while remaining a valid report. Nonzero process
exit fails even with a complete success report; zero exit cannot replace a valid
report. See [timeouts](#stage-timeouts-and-cleanup) for precedence over reports.

## Human decisions and bounded repairs

A complete implementation `human-decision-needed` report stops the attempt even
on nonzero exit. Describe the precise decision and relevant approved requirement
or interface in `summary`/`unresolved_questions`, with available evidence in
`acceptance_evidence`; no extra report fields are required. Current work stays in
its worktree without submission capture, further checks/reviews, integration or repair.

A blocking finding with `human_decision_needed: true` from either review axis
also stops immediately, including on nonzero exit. Use `requirement` for the
approved contract, `evidence`/`consequence` for the conflict and `resolution` for
the precise decision. The diagnostic includes requirement and resolution. This
finding takes precedence over ordinary repairable blockers in the same validated
report. The entire report must pass identity, shape and evidence validation before
recognizing a decision; invalid decision-like output follows ordinary bounded
report-failure handling.

Both decisions leave the ticket Blocked and run incomplete without consuming
remaining repairs or launching subsequent verification. Approved spec/ticket/
standards and last verified integration stay unchanged. Later-repair decisions
retain previous attempts, rejected revisions, prompts and output. Human resolution
owns the contract conflict; the harness does not infer requirements or change an
approved interface. A new run needs human-approved inputs; QA continuation does
not resume this blocked decision state.

For a submission, the harness independently runs lightweight checks and uses
separate detached worktrees/processes for the two review axes. Lightweight-check
failures, blocking reviews, failed merges/candidate suites, missing/invalid reports
and ordinary process failures reject the attempt with preserved evidence and use
one shared repair allowance, without secondary retries. Worker-internal editing/
testing iterations belong to their single assignment.

Every repaired submission becomes a new commit, even when repair only reruns
verification; changed paths derive against the original base. Applicable checks,
both fresh reviews and a new exact candidate suite must pass. Rejected approvals
never authorize new source; validation restarts while retaining the shared baseline.
Exhaustion leaves Blocked/incomplete with all rejected revisions/worktrees/history.
Baseline/preflight failures start no attempts. Valid human decisions, approved-input
or evidence integrity violations, worker-owned HEAD changes and external integration
movement stop without more repairs. Repairs cannot change baseline or requirements.

## Optional review suggestions

Optional findings follow the [whole report contract](#assignment-and-report-contracts)
and successful-exit requirement. They never fail review, consume repairs or request
a human decision, even with `human_decision_needed: true`. Mixed reports follow
[blocker precedence](#human-decisions-and-bounded-repairs). Repair inputs carry
optional suggestions as context; successful repairs may leave them unimplemented.
Findings may appear, disappear or reuse report-local IDs between submissions;
disappearance does not prove resolution. Use the original revision/attempt and
[gate ranges](#records-and-artifacts) to distinguish earlier suggestions.

## Exact source and ticket integration

Check/review worktrees must remain clean on the submitted revision. Assume-unchanged
and skip-worktree index flags reject so tracked edits cannot be concealed.
After each process and before promotion, the harness rechecks earlier verified
worktrees. Changed HEAD/index/working files invalidate the affected gate:
`passed: false`, `verification_status: "invalidated"`, and a source diagnostic.
A structurally valid review retains `report_status: "valid"` but cannot approve
changed source. The attempt stops; renewed checks/reviews are required.

The real merge candidate has the starting integration revision as first parent;
submission descends from that revision in this sequential slice. Candidate parents
must be that revision and submission, and its tree must equal the reviewed
submission tree. Hook-created source resolutions require renewed review. The
suite must leave the exact candidate clean. Only this tested candidate becomes
`done_revision`; integration advances atomically using the expected previous revision.
External movement makes compare-and-swap fail, preserving external tip, candidate
and diagnostics. Failed merges/suites also leave integration unchanged by the harness.

Destination branches must be direct refs, validated while Git holds their locks.
Setup, ticket integration and QA
stop/continuation/promotion reject symbolic branch aliases; expected-old updates
never dereference refs, preserving feature/development separation.

The intended contract preserves caller HEAD, index and working files. The known
inherited `GIT_INDEX_FILE` routing defect remains open as
`review-M1-architecture-01/standards-01/F1`; see the
[current M1 assessment](../../.scratch/ticket-harness/reviews/M1-architecture-01.md) and
[human-review response](../human_qa/m1_review.md#m1-status).

Git hooks are disabled for the final atomic ref update so user code cannot run
after final validation. Checkout, submission and merge hooks operate within the
following integrity checks. [Milestone QA](qa.md) separately governs feature-to-dev promotion.

## Trust and integrity

Approved source files/snapshots are checked against recorded SHA-256 before
processes and promotion. Each process and hook-capable Git worktree/submission/
merge operation is bracketed by checks covering approved originals, snapshots,
approved-path copies in source worktrees, `run.json`, assignments and earlier
process artifacts. Submitted diffs cannot change approved paths, including through
commit hooks; detected edits stop the attempt.

Gate/Git operation `integrity` entries retain path, expected/observed SHA-256
(`null` for absent/unreadable contents) and rejected-content artifact when bytes
exist. A directory replacing a harness-owned file moves intact to its rejected
artifact before restoration. Harness-owned snapshots/evidence restore from
pre-process bytes after rejected bytes are saved; changed originals/source worktrees
remain inspectable. Restore original requirements before a newly approved run.

These checks observe process boundaries: transient edits restored before return
are undetected; local artifacts are unauthenticated; unrestricted filesystem/Git
access can race observations. Run only trusted commands until role access enforcement
(ticket 36). These observations and process-group cleanup are not an OS sandbox.

## Stage timeouts and cleanup

Timeouts include assignment delivery and output collection. `timeouts` configures
independent wall-clock allowances:

| Key | Default seconds | Invocation |
| --- | --- | --- |
| `implementation` | 1800 | Initial implementation assignment. |
| `repair` | 1800 | Each later implementation assignment; role remains `implementation`. |
| `spec` | 900 | Spec review on every attempt. |
| `standards` | 900 | Standards review on every attempt. |
| `checks` | 300 | Each configured lightweight check, separately. |
| `baseline` | 1800 | Starting broader suite, attempt 0. |
| `candidate` | 1800 | Exact ticket candidate suite on every attempt and separate `milestone-regression` suite. |

For example, `"timeouts": {"checks": 60, "baseline": 1200, "candidate": 2400}`
keeps agent defaults. Fractional seconds are allowed; the one-week cap prevents
platform pipe-wait overflow. No allowance is infinite/disabled. See
[input validation](inputs.md#canonical-input-contract) for accepted values.
Command arrays, assignment identities and report schemas remain unchanged.

Each invocation starts a POSIX session/process group. Timeout sends SIGKILL to
that group, including inherited children ignoring SIGTERM, and saves available
stdout/stderr bytes. Deadlines remain active after leader exit while children
hold output pipes. A timed-out stage cannot pass or request a trusted human
decision, even with a complete report/zero leader exit; raw output is retained.
Non-timed-out reports retain whole-report validation and human-decision precedence,
including on nonzero exit.

Final output draining and leader reaping each have a separate five-second bound.
Failure to drain/reap or an unavailable executable gives shared environment failure:
`outcome: "environment"`, gate `execution_error`, no further repairs. Ordinary
stage timeouts use the shared repair allowance; baseline timeout is environment/
attempt 0 without a worker. Cleanup precedes integrity checks/repair copying,
preserving stopped work/prior evidence. Normal completion also kills the group
to remove background children. Trusted commands must keep descendants in that
group; detached sessions/groups are uncontained. Deadlines cover configured agents/
checks, not arbitrary Git operations/hooks, which retain their integrity rules.

## Records and artifacts

`run.json` records execution state (`Pending`, `Ready`, `Running`,
`Verifying`, `Done`, `Blocked`), attempt, inputs, base/submission/candidate/Done
identities, changed files, gates/findings, outcome, failures and artifact paths.
`max_repairs` and `timeouts` hold normalized allowances (timeouts in seconds).

`attempts` is ordered. Entries record `attempt`, `starting_revision`, source
worktree, state (`Running`, `Verifying`, `Rejected`, `Done`), observed submission/
changed files/candidate when available and rejection failure stage/message.
`gate_start` (inclusive) / `gate_end` (exclusive, set at attempt end) index the
complete top-level `gates`. Gate/operation `attempt` is zero for baseline and
positive for ticket attempts; numbering/repair allowance restart per ticket.
Rejected evidence stays attached to its revision after repair, exhaustion or
final `completed` outcome; earlier findings/approvals do not transfer.

`selected_tickets` holds canonical IDs in numeric order; `tickets` maps each to
state, attempt and available submission/candidate/Done identities. Context-only
tickets appear only in `requirements`. `integration_revision` is this run's last
verified/promoted tip, historical if externally moved; `base_revision` stays the
starting base. Compatibility `ticket` mirrors active/last attempted ticket
(configured primary before assignments). Earlier identities remain in `attempts`.
Every attempt/gate/Git operation carries canonical `ticket`; shared baseline uses null.

### Gates and decisions

Gates record stage, argv, cwd, revision, actual attempt, output paths and exit code,
plus `timeout_category`, `timeout_seconds` and `timed_out`. `cleanup` records
`process_group`, `signal` (`SIGKILL`) and whether `sent`. `timed_out: true` fails
even with leader exit 0; its diagnostic names stage/allowance.

Agent gates retain parsed `report` when JSON decoding/nesting checks succeed.
`report_status` is `valid`, `invalid`, or `not-evaluated` for a timed-out agent;
an execution-environment failure can precede setting any report status.
Rejection `diagnostic` explains failure. Validity differs from success: nonzero
exit, blockers and human decisions cannot pass. Invalid reports set `passed: false`;
undecodable/excessively nested output remains verbatim in `stdout`. `failure`
names stage/reason.

Read Spec/Standards gates' `report.findings` for location, requirement, consequence,
evidence and resolution. A passing gate on a Done ticket may include optional
findings. Gate/report `attempt` and `revision` identify reviewed submission;
`base_revision` is the fixed approved baseline, while `ticket.done_revision` is
the separately tested merge candidate.

A valid decision report adds `human_decision` to latest `ticket` and affected
`attempts` entry: `role`, actual `attempt`, assigned `revision`, complete validated
`report`, approved paths/snapshots/SHA-256 in `approved_inputs`, and `assignment`,
`stdout`, `stderr` artifact paths. Attempt retains implementation source path;
gate `cwd` identifies reporting worktree. Precise questions or full findings/
contracts/evidence remain descriptive, never passing approval. Nonzero exit stays
beside the decision diagnostic. Counters/ranges include only actual assignments/
processes; stopped attempt is `Rejected`, ticket `Blocked`.

### Operations and retained files

`operations` separately records Git worktree preparation, submission capture and
candidate merge, with `passed` and applicable integrity diagnostics. If an operation
fails before returning a revision, rejected observations remain on ticket or
retained Git worktree. Atomic replacement prevents partial status reads; it does
not provide crash recovery/resume. Planned [QA continuation](qa.md) has its own contract.

`artifacts/` retains full assignments/stdout/stderr. Initial artifact/worktree/
operation names use `implementation`, `spec`, `standards`, `check-NAME`, `candidate`;
later attempts prefix `attempt-2-`, `attempt-3-`, etc., without configured-check
name collisions. Multi-ticket names additionally prefix `ticket-ID-`, e.g.
`ticket-03-attempt-2-spec`; shared baseline stays `baseline`. Single-ticket names
remain compatible. Stage names/`TICKET_HARNESS_STAGE` keep original role/check
values. Earlier evidence is protected from later processes/Git hooks; attempts
never reuse worktrees or assignment processes.

Worktrees/rejected commits remain inspectable; follow the
[inspection and disposal steps](../ticket-harness.md#records-and-artifacts).
