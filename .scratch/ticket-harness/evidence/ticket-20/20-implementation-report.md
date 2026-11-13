# Ticket 20 implementation report

Implementation checkpoint only; independent review and completion bookkeeping
remain root-owned. Fixed whole-ticket baseline:
`0d79d016907a03ce39d33c749523a8700e4233a4`.
[Criterion-specific evidence](20-criterion-evidence.md) links the actual public
observations and pending independent design/history criteria. Final executable/test identity is [20-final-source.json](20-final-source.json),
including the exact baseline-to-working source diff. This report's commit contains
that exact implementation. No tests, entry points, packaging or dependencies changed.

## Ownership and complete caller migration

`ticket_harness/tickets.py` adds an attempt owner receiving only the existing
current-ticket dictionary, attempt history and gate sequence plus ticket/attempt/
starting identity. It receives no runner, configuration, execution callbacks or
Git operations. Its operations establish Running, observe source, submit and
project Verifying with changed files/revision, observe candidate, complete Done
and exclusive gate end, reject with failure/range even before a submission exists,
return the preserved rejected-work observations, and attach an identity-checked
validated decision to both established locations. There is no framework or
inheritance hierarchy. These are lifecycle operations, not arbitrary field setters.

`execute` migrates every initialization/submission/candidate/completion/rejection
writer to those operations, including initial and repair paths and worktree/report
failures before submission. It retains bounded repair policy, original approved
base, source carry, starting-source selection and repair prompt construction.
These are ticket 21 responsibilities and were not otherwise refactored.
The rejected failure dictionary returned for repair context is consumed read-only;
no caller writes lifecycle observations through it. Existing gate/history readers
remain unchanged. `agents.assignment` serializes this context and prior canonical
gates into the next process assignment, without modifying them.

The public ticket projection intentionally retains the pre-existing distinctions:
source is attempt-only before submission; submission projects the existing attempt
fields; gate_end/failure remain historical attempt evidence; Rejected is an attempt
state, while the public ticket retains Running/Verifying until a repair starts
Running or the run classifies terminal failure Blocked. This preserves public
lifecycle vocabulary and intermediate record values, including pre-submission
failures. A preliminary local edit mirrored Rejected into ticket state; it was
removed before final-source verification after tracing the spec lifecycle table.
No final record schema or field naming changes were introduced.

`runner.py:_Run.check` receives the exact owning attempt from the execution caller.
It constructs decision evidence only after complete report validation and sends it
to that identified owner, which checks ticket/attempt/assigned revision. It never
selects history[-1] or mutates an attempt record. Non-ticket baseline/milestone
checks have no owner and no decision-producing prompt. All ticket gate callers
receive the owner, including implementation and either review axis on every repair.

`agents.report` receives only stdout path and expected identity. Its local return
contains parsed report/status or invalid-report content/diagnostic/failure data.
It has no canonical gate to edit. `_Run.check` publishes those observations,
persists invalid reports, and raises the existing diagnostic. Bounded nesting is
checked before retaining report content exactly as before. Invalid readable
objects retain their content; malformed/ambiguous/deep payloads retain the same
failure information and raw stdout/stderr.

## Unchanged workflow and precedence

The runner still owns command execution, report validation orchestration, canonical
gate status/diagnostics, verification registration and source invalidation.
Environment execution failure precedes evaluation. Timed-out agent reports remain
not-evaluated. Invalid reports stop before decisions gain authority. Valid decisions
retain priority over ordinary process/review failures and immediately stop repair,
including exit 7; their diagnostics include that nonzero exit. Ordinary nonzero
process exit overrides otherwise complete success; complete blocking reviews fail
on exit zero; optional findings remain nonblocking. Integrity makes the result
nonrepairable, and subsequent source validation retains existing precedence and
canonical invalidation. Git/integration failure classification is unchanged.

`records.execute`, protection/restore context managers and `write_json` remain
unchanged. Existing atomic saves expose Running before worktree work, source after
the protected worktree operation, Verifying after capture, candidate before suite,
Rejected/range after failure and Done after promotion. Report rejection additionally
persists its canonical invalid gate before unwinding. No partial success is written.
The outer run retains terminal Blocked/outcome classification and failure precedence.

QA serialization/restoration and version-1 checkpoint structure remain unchanged.
At a deliberate checkpoint all completed attempts are plain existing dictionaries;
future ticket execution creates fresh owners. Existing `restore_checks` reconstructs
verification references from canonical gates; source invalidation continues to
update those canonical gates. QA evidence freezing, approvals, two-ref promotion,
input preparation, dependency readiness/unlocking and public CLI parsing remain
unchanged. `inputs` reads prior completed ticket observations; status emits saved
JSON; assignment/report consumers continue to see existing keys/artifact names.
No later refactor or runtime orchestration/QA acceptance is implemented.

## Start and final architecture trigger assessments

[Entry record](20-start.md) captures the start decision and coverage map before
runtime edits. At final source [identity](20-final-source.json), each trigger is
reassessed against the actual three-file diff:

| Trigger | Start | Final | Source rationale |
| --- | --- | --- | --- |
| New lifecycle | No | No | Existing attempt states/operations move from execute/check into owner; no new state or execution phase. Public ticket lifecycle unchanged. |
| New persistence/restoration path | No | No | Existing saves, plain dictionaries, QA version-1 snapshot and restore_checks remain; no new serialized object or reconstruction route. |
| New shared mutable state | No | No | Owner wraps already shared attempt/ticket/gate observations, retaining canonical history/reference identity; no additional run/global state. |
| Additional writer | No | No | Existing execute/check lifecycle writers migrate to owner; parser loses canonical gate write authority. Run remains canonical check writer and terminal outcome classifier. |

No positive trigger requires a third broader assignment for this slice. Both
independent ordinary axes still inspect all relevant changed/unchanged collaborators.
Real M1 cumulative assessment remains required and unperformed; ticket tests and
source review do not establish M1 readiness or human acceptance.

## Coverage, execution evidence and limitations

The criterion-to-existing-test map is in [20-start.md](20-start.md). No uncovered
behavior justified another test or private seam; no manufactured red test is claimed
for a preservation refactor. Focused exploratory checks passed 348 cases; this run
began before the removed transient projection edit and is not the final-source gate.
[20-focused.log](20-focused.log) retains its actual result; exact exploratory
observations are compressed in [focused archive](20-focused-observations.tar.gz)
with a [byte manifest](20-focused-raw-manifest.json). The final-source full
suite and static/whitespace results are recorded separately in
[commands and results](20-final-check-results.json), [driver log](20-final-checks.log)
and individual `20-final-check-N.log` files, against the final hash map. Source
identity is asserted unchanged after the complete driver.

[Raw observation index](20-observation-index.json) maps exact public scenarios to
retained record/status, CLI/foreground observations, refs/history and raw files.
[20-raw-manifest.json](20-raw-manifest.json) hashes all files within the compressed
[raw archive](20-final-raw.tar.gz). The capture plugin runs before existing fixture
cleanup and does not change tests or production behavior; passing status results
are independently compared with the saved record. The index additionally checks
inclusive/exclusive ranges identify only their own ticket/attempt and validated
handoffs identify the owning attempt and existing current-ticket projection.
All 544 scenarios in this execution produced retained run observations; their
pytest outcomes remain in the full check log. Archive paths in the index/manifest
are relative to its `ticket20-final-raw/` prefix. Relevant assertions in existing tests establish caller work,
Git/source preservation and immediate stopping before fixture cleanup.

[Genuine checkpoint history](20-checkpoint/preservation-history.md) records both
original capture and failed live retention, renewed isolated baseline-code producer
and successful final-source continuation. It explicitly retains the chronological
limitation: the continued checkpoint was produced later from exact baseline source,
not by the final code, while the original producer preceded runtime edits. Both
source identities, stop observations, actual immutable checkpoint copies and renewed
before/after real repository/worktree archives remain. Synthetic fixture decisions
supply no actual feature QA authority.

Initial missing mypy and sandbox DNS failure remain in [tool transcription](20-tool-unavailable.log)
and [original pip log](20-tool-setup.log). Approved escalated pinned mypy 1.19.1 and
Ruff 0.14.10 installation into /tmp succeeded; [setup log](20-tool-setup-escalated.log).
Reusable absolute Python is used throughout; no shared environment mutation.
Packaging/installed checks are omitted because no packaging/entry-point change or
remaining installation uncertainty exists under the approved refactor contract.
No exception to whitespace rules is used for newly authored evidence/source;
historical frozen EOF copies are outside this ticket's baseline diff.

Fresh GPT-6.1 Sol Medium / <=250000 active-context target was requested for this
assignment; backend delivered model/reasoning enforcement, hard context enforcement
and measured active context telemetry are unavailable. Configuration is not proof.
The exact evaluated G2/C5 guidance and finite limitations from ticket 19 remain
applicable; no calibration report substitutes for source review. No unresolved
actual prior finding is carried from 19. Criteria 6/7 and final acceptance of this
packet still require root's independent fresh High Spec/Standards reports and
review-record/bookkeeping steps; this worker does not declare ticket completion.

## Actual final gate results

- Full final suite: **544 passed in 703.66s**, exit 0; driver wall time 704.062s.
- Strict mypy: exit 0, no issues in 10 source files.
- Ruff lint: exit 0. Ruff format: exit 0, 24 files already formatted.
- Working-tree and baseline-to-working executable whitespace: exit 0.
- Staged full-diff whitespace: recorded separately in `20-staged-whitespace.log`.
- Same-run capture: **544 scenarios / 10446 raw files**; all raw archive bytes
  match [manifest](20-raw-manifest.json), and all 26 executable/test/config source
  hashes remain unchanged ([capture audit](20-capture-audit.json)).

Actual recorded outcomes include expected rejected scenarios: 119 invalid-input,
347 incomplete, 5 environment, 52 completed, 15 stopped_at_qa and 6 awaiting_human_qa.
These are intentional public regression outcomes, not test failures. Records retain
1158 valid and 277 invalid report evaluations, 10 timed-out/not-evaluated reports,
and validated decisions on implementation (8), Spec (7) and Standards (7).
The existing twelve-role/attempt/exit matrix is included; broader decision scenarios
account for the remaining decision observations.
