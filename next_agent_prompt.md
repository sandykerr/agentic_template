Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/24-own-milestone-review-and-checkpoint-continuation.md`

**24: Own milestone review and checkpoint continuation**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/24-own-milestone-review-and-checkpoint-continuation.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
Creating this handoff starts no assignment, harness run, QA session or acceptance.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed original whole-ticket review baseline. Historical references below
do not replace it. Inspect and preserve actual unrelated worktree edits, including
tracker/guidance edits and the workflow-efficiency archival work left unstaged.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md), [index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone without human acceptance. Tickets 10–23 are completed; 24 is
open, unclaimed, ready-for-agent and the sole remaining M1 ticket. Verify its
prerequisites from actual criterion/check/review evidence and commit ancestry:

- **15:** final implementation `d11f0bc60a2c11c40683e58581dffa10e36a91be`,
  bookkeeping `eb58804f275776f9cce8d3ebd2e3485b7928b0f6`;
  [completion/check/review evidence](.scratch/ticket-harness/evidence/15-completion.md).
- **23:** implementation `8b1b37becb544299e8981144e4ad56da42e2d45f`,
  bookkeeping `a1f4fe5ec1b4b70dd1d4db4c5be094dd228ae38d`;
  [seven-criterion completion/check/review evidence](.scratch/ticket-harness/evidence/23-completion.md).

Selection was rechecked at `a1f4fe5`: tickets 10–23 have completed headers and all
criteria checked; prerequisites 15/23 have respectively 5/7 checked criteria,
completion evidence with required checks and separate reviews, and all four listed
implementation/bookkeeping commits are ancestors. Verify these facts again.
Historical source references in 19–21 evidence predate the lossless history repair;
use its [old-to-retained map](docs/history/2026-11-10-large-file-rewrite.json).
Preserve original reports; historical checks prove their own source, not 24.

After 24, M1 still needs actual cumulative architecture work and explicit human
QA. Later required milestones remain gated; E1 retains priority immediately after
verified 34. No push, orchestration, promotion or development acceptance is authorized.

## Current owners, roles and review context

Ticket 23 moved the existing start/continue sequence into `_Run.execute`.
Public `run` creates output/holds exclusive ownership; `continue_run` holds ownership,
validates with `qa.restore`, retains rejection behavior and invokes the same run
operation. The run owns prepared-input consumption, branch/baseline identities,
current-milestone scheduling, failure classification and finalization.
`export_checks()` returns the existing JSON-safe checkpoint triples;
`restore_checks()` rebinds decoded evidence to canonical durable gates. QA uses the
export operation rather than the internal verified tuple collection. Keep these
owners, PreparedInputs22 and ticket/attempt21/20 operations intact.

QA still has the existing `review(execution, checkpoint)` Boolean callable and
checkpoint envelope/candidate/request/evidence/decision logic. Ticket 24 now owns
that migration: give milestone review cohesive operations and an explicit
stopped-versus-promoted outcome, using the run-owned verification interface.
Internal class/method/layout choices remain worker decisions.

Read 23's [ownership/coverage report](.scratch/ticket-harness/evidence/23-implementation-report.md),
[canonical packet](.scratch/ticket-harness/evidence/23-review-packet.md),
[criterion evidence](.scratch/ticket-harness/evidence/23-criterion-evidence.md),
[assessment](.scratch/ticket-harness/reviews/ticket-23.md),
[Spec original](.scratch/ticket-harness/evidence/23-review-spec-01.md),
[Standards original](.scratch/ticket-harness/evidence/23-review-standards-01.md) and
[immutable capture](.scratch/ticket-harness/evidence/23-review-round1-capture.json)
as needed. Its required full suite was **544 passed in 706.22s**; strict mypy,
Ruff lint/format and both whitespace checks passed. All 26 tested identities
independently matched committed source; no tests changed. Both independent axes
report **0 blocking / 0 optional**. These outcomes verify 23, not 24.

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, no
worker override; independently configured **High Spec** and **High Standards**.
Target <=250000 active-context tokens per assignment; report unavailable settings
and telemetry. Configuration proves no backend delivery/runtime enforcement.
Worker/repair/Standards add [OOP](.agents/skills/microsoft/microsoft_oop/SKILL.md),
[codebase design](.agents/skills/matt-pocock/codebase-design/SKILL.md) and
[test strategy](.agents/skills/custom/test-strategy/SKILL.md). Spec uses approved
behavior/coverage contracts. Apply writing-for-agents/skill-creator for applicable
authoring; preserve upstream skills unchanged.

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and
[review index](.scratch/ticket-harness/reviews/README.md). Inventory entry callers,
every owner/writer/consumer, initialization, saved/restored state, aliases and
invalidation. Explain changed and unchanged responsibilities; consequential
missing decisions remain human-owned.

Use evaluated substantive **G2**, final **C5** through
[reviewer guidance](docs/agents/reviewer-evaluation.md), its
[declaration](.scratch/ticket-harness/evidence/19-evaluation-g5/declaration.md),
[manifest](.scratch/ticket-harness/evidence/19-evaluation-g5/source-manifest.json),
[original reports/index](.scratch/ticket-harness/evidence/19-evaluation-g5/README.md)
and [results](.scratch/ticket-harness/evidence/19-evaluation-g5/results.md).
C5 aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
Five evolving eight-case corpora/two guidance versions preserve failures, misses,
invalid controls and differing judgments. One independent final observation per
axis is finite evidence, not a detection/reliability/runtime guarantee or answer
pattern for new 24 source.

Ticket 23's four start/final triggers were independently **No**: existing lifecycle,
persistence/restoration, shared references and writers remained; responsibilities
were localized. Reassess each at 24 start and after changes: new lifecycle,
persistence/restoration path, shared mutable state, additional writer. A positive
trigger requires a separate fresh High broader affected-workflow assessment before
integration. All-negative observations require no unconditional third reviewer.
No unresolved actual full finding key, missing prerequisite report, pending
relevant revalidation or human-owned contract decision carries from 23; its
[explicit history](.scratch/ticket-harness/evidence/23-finding-history.md) retains
historical fixed/fixture concerns at their own scopes.

Real **M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before readiness establish actual feature-start provenance (distinct from your
ticket baseline), exact assessed source and substantive inspection of **every
`ticket_harness` Python file** by a fresh High Standards assignment. No cumulative
baseline, real QA request/run/candidate/gates/decision is currently established.
Missing/stale required work holds readiness. Assessment completion never accepts
M1; after 24 completion create a QA preparation/waiting handoff, never an executable
M2 assignment while acceptance remains absent.

## Bounded implementation and compatibility

The ticket's seven original criteria control. Read scoped spec:
[ownership](.scratch/ticket-harness/spec.md#state-and-decision-ownership),
[refactor verification](.scratch/ticket-harness/spec.md#oop-refactor-verification),
[lifecycle](.scratch/ticket-harness/spec.md#ticket-lifecycle),
[exact revisions](.scratch/ticket-harness/spec.md#independent-checks-and-exact-revisions),
[QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa)
and [safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation).

Keep tested candidate/feature/development identities, exact request content/digest,
frozen evidence identities and last decision observation with one milestone review.
Fresh construction and restored continuation use the same exact-approval,
unchanged-source/evidence and expected-ref rules. The run receives an explicit
stopped-versus-promoted outcome. QA consumes run export/restoration operations,
not the runner's internal verified collection or a new separate checker.

Only explicit matching unconsumed human approval advances both expected refs to
the exact tested candidate. Preserve indefinite waiting and observable rejection
for missing/unreadable/malformed/mismatched/stale/replayed decisions, without
consuming ticket repairs or admitting later milestones. Keep runner-owned command,
report, verification and source-invalidation authority and human promotion authority.

Preserve version1 checkpoint format, filenames, identities, observations and
archived lineage. New-process continuation validates approved inputs, record,
request, frozen evidence, verified sources, both refs and exclusive ownership.
Invalidate the stopped marker before resumed work; retain Done assignments,
baseline, artifacts and consumed decisions without replay. Restored verification
references must resolve to canonical durable gate records so later invalidation,
including after repeated continuation, updates those actual records. Changed
checkpoints/evidence/refs cannot authorize continuation or promotion.

Preserve stage diagnostics, milestone preparation/regression/promotion failures,
status, stop exit2/success exit0, ticket-Done versus promoted versus feature-complete,
commands, saved JSON schemas/values, single-/multi-ticket/milestone artifact naming,
process ownership, integrity protection and atomic persistence. Leave Git/process/
filesystem primitives as functions. Update [code wayfinding](docs/ticket-harness.md)
for final responsibilities. No arbitrary crash recovery, background execution,
correction-plan execution, new approval authority, independent-work29, runtime33/34,
or actual development QA acceptance belongs in this refactor.

## Verification, reviews and completion

Apply [efficient development](docs/agents/development-efficiency.md): complete local
diagnosis/checks and one canonical packet before review. Preserve both originals
before a fresh Medium repair and batch complete authorized related diagnosis.
Ticket 23 had two Medium worker assignments because of a user interruption, one
clean independent review pair, no repair and no repeated review-failure pattern.
Its initial pre-collection capture error and interrupted incomplete tests remain
retained; neither is a pass. Corrected capture uses `tests` on PYTHONPATH. These
historical setup limits do not replace 24's required final-source preparation.

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or tests; use the absolute reusable prefix. Follow
[testing policy](docs/agents/testing.md), test-strategy and
[documented checks](docs/ticket-harness.md#python-and-checks). Map existing exact
approval/promotion, stale/replay rejection, clean stop/new-process continuation,
post-restore canonical invalidation, changed checkpoint/evidence/ref rejection and
repeated lineage cases in test_milestones, test_qa_promotion, test_continuation and
test_transaction. Add only distinct uncovered failures using TDD at the approved
public CLI/scripted-process/isolated-Git seam; avoid private-class prescriptions.
Run focused development checks, then full pytest, strict mypy, Ruff lint/format
and both whitespace checks on final source. Packaging follows actual impact.

Arrange commands/exits/source/test hashes, logs and needed CLI/Git/record/ref
capture before checks. Produce your own genuine pre-24 deliberate checkpoint
**before runtime edits**, preserving live fixture through cleanup and exact
producer provenance; continue it under final source. Also verify checkpoints
produced by new code. Ticket 23's [producer](.scratch/ticket-harness/evidence/23-checkpoint/producer.json),
[final continuation](.scratch/ticket-harness/evidence/23-checkpoint/continuation-final.json),
[archive audit](.scratch/ticket-harness/evidence/23-checkpoint/audit.json) and stopped/
continued archives prove their own sources only, not 24. Preserve all historical
capture limits, including 20's fixture loss/timing and 22's pre-format/final-consumer
history. Fabricating an old checkpoint after the refactor is insufficient.

After final checks, commit only implementation before fresh separate High Spec and
Standards whole-ticket reviews from your original baseline. Supply ownership,
coverage, unchanged flows, exact checks/source, all relevant keys/history, omitted
scope and G2/C5 limits. Save originals before aggregation. Blocking findings use
fresh Medium repair, renewed gates, committed fixes and fresh whole-ticket axes
from the original baseline. Optional suggestions stay optional; consequential
scope/risk/QA decisions remain human-owned.

After every criterion/gate passes, preserve criterion wording/Blocked by, check
verified criteria, set Status completed, retain previous readiness in the completion
comment, link evidence from feature/review indexes and commit only bookkeeping
separately. Automatically use create-next-agent-prompt and separately commit only
the generated QA preparation/waiting handoff; recheck actual milestone/prerequisite
eligibility. Keep candidate preparation, QA-session execution, orchestration,
approval and promotion in separately authorized workflows.

Preserve unrelated edits, original evidence, approved active-run inputs and frozen
QA snapshots. If an intended authoring path is an active input, report the exact
mutation blocker and keep it immutable. Return implementation/bookkeeping/handoff
commits, actual checks, separate review outcomes, criterion evidence, unchecked
items, unresolved full keys and next checkpoint/blocker status. Ticket completion
supplies no M1 acceptance, promotion, push or feature completion.
