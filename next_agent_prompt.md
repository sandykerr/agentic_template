Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/23-own-the-complete-run-lifecycle.md`

**23: Own the complete run lifecycle**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/23-own-the-complete-run-lifecycle.md) and
[implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
Creating this handoff starts no assignment, harness run, QA session or acceptance.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed original whole-ticket review baseline; historical references below
do not replace it. Inspect and preserve actual unrelated worktree changes.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone without human acceptance. Tickets 10–22 are completed; 23 is
open, unclaimed, agent-ready and next in preferred prerequisite-ready order.
Verify actual prerequisite criteria/checks/separate reviews and commit ancestry:

- **15:** final implementation `d11f0bc60a2c11c40683e58581dffa10e36a91be`,
  bookkeeping `eb58804f275776f9cce8d3ebd2e3485b7928b0f6`;
  [completion/check/review evidence](.scratch/ticket-harness/evidence/15-completion.md).
- **21:** retained implementation `a6e777739b3f515f157d3c1e75efa4e957ab1c66`,
  bookkeeping `8e7d6c9fc5bf172a2f6a907c4cee5b947da19d32`;
  [completion/check/review evidence](.scratch/ticket-harness/evidence/21-completion.md).
- **22:** implementation `33fa0ea6e667a3879564ed4628c10f6d59ada21b`, bookkeeping
  `25714b5f08ebb3c8949531ef03ac26302ae4f1a1`;
  [seven-criterion completion/check/review
evidence](.scratch/ticket-harness/evidence/22-completion.md).

Selection was rechecked after ticket 22 bookkeeping at `25714b5`: prerequisites
15/21/22 have respectively 5/7/7 checked criteria, completed evidence with checks
and separate reviews, and the listed implementation/bookkeeping commits are
ancestors. Tickets 10–22 are completed; 24 awaits 23. Verify these observations again.

Historical source references in 19–21 evidence predate
the lossless large-file history repair. Use its
[old-to-retained map](docs/history/2026-11-10-large-file-rewrite.json); preserved
runtime/test/config contents match, while historical reports keep original IDs.
[Ticket 22 prerequisite audit](.scratch/ticket-harness/evidence/22-root-eligibility.json)
records this distinction. Historical checks prove their own source, not 23.

M1 still needs 23–24, actual cumulative architecture work and explicit human QA.
Later required milestones remain gated; E1 retains priority immediately after
verified 34. No push, orchestration, promotion or acceptance is authorized.

## Current source, roles and review context

Ticket 22 input preparation returns `PreparedInputs`: validated settings, snapshots,
normalized requirements, primary/selected/completed IDs, checked plan and workers.
Its `execution_config()` translates to the existing JSON-safe config/checkpoint
shape without enriching raw settings. `inputs.load` requires the caller-created
output/inputs directory; all plan consumers receive validation's checked return.
Keep this preparation owner and the attempt/ticket owners from 20/21 intact.

Read ticket 22's [ownership/coverage](.scratch/ticket-harness/evidence/22-implementation-report.md),
[canonical packet](.scratch/ticket-harness/evidence/22-review-packet.md),
[criterion evidence](.scratch/ticket-harness/evidence/22-criterion-evidence.md),
[assessment](.scratch/ticket-harness/reviews/ticket-22.md),
[Spec original](.scratch/ticket-harness/evidence/22-review-spec-01.md),
[Standards original](.scratch/ticket-harness/evidence/22-review-standards-01.md) and
[immutable capture](.scratch/ticket-harness/evidence/22-review-round1-capture.json)
as needed. Required checks: **544 passed in 709.21s**, strict mypy, Ruff lint/format and
both whitespace checks passed; all 26 tested identities independently matched committed
source. No tests changed. Both independent axes report **0 blocking / 0 optional**.
These checks verify 22, not 23.

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, no
worker override; independently configured **High Spec** and **High Standards**.
Target <=250000 active-context tokens per assignment; report unavailable settings
and telemetry. Configuration does not prove backend delivery/runtime enforcement.
Worker/repair/Standards add [OOP](.agents/skills/microsoft/microsoft_oop/SKILL.md),
[codebase design](.agents/skills/matt-pocock/codebase-design/SKILL.md) and
[test strategy](.agents/skills/custom/test-strategy/SKILL.md). Spec uses agreed
behavior/coverage contracts. Apply writing-for-agents/skill-creator for applicable
authoring, preserving upstream skills unchanged.

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and the
[review index](.scratch/ticket-harness/reviews/README.md). Record entry callers,
owners, every writer/consumer, initialization, save/restore and invalidation;
explain changed and unchanged responsibilities. Consequential missing decisions
remain human-owned.

Use evaluated substantive **G2**, final **C5** through
[reviewer guidance](docs/agents/reviewer-evaluation.md), its
[declaration](.scratch/ticket-harness/evidence/19-evaluation-g5/declaration.md),
[manifest](.scratch/ticket-harness/evidence/19-evaluation-g5/source-manifest.json),
[original reports/index](.scratch/ticket-harness/evidence/19-evaluation-g5/README.md)
and [results](.scratch/ticket-harness/evidence/19-evaluation-g5/results.md).
C5 aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
Five evolving eight-case corpora/two guidance versions preserve failures, misses,
invalid controls and differing judgments. One independent final observation per
axis is finite evidence, not a detection/reliability/runtime guarantee. Corpus
classifications supply no answer pattern for new 23 source.

Ticket 22's four start/final triggers were independently **No**: existing lifecycle,
saved shape, shared references and writers remained; the input owner packages already
prepared values. Reassess each trigger at 23 start and after changes: new lifecycle,
persistence/restoration path, shared mutable state, additional writer. A positive
trigger requires fresh broader affected-workflow assessment before integration;
all-negative observations require no unconditional third reviewer. Ordinary axes
stay independent. No unresolved actual full finding key, missing required prerequisite
report, pending relevant revalidation or human-owned decision carries from 22. See the
[explicit history](.scratch/ticket-harness/evidence/22-finding-history.md).
Historical fixed keys and fixture findings retain original source scopes.

Real **M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before readiness establish actual feature-start provenance (distinct from your
ticket baseline), exact source and substantive inspection of every ticket_harness
Python file. Missing/stale required work holds readiness; assessment completion
never supplies milestone acceptance.

## Bounded implementation and compatibility

The ticket's seven original criteria control. Read scoped spec:
[ownership](.scratch/ticket-harness/spec.md#state-and-decision-ownership),
[refactor verification](.scratch/ticket-harness/spec.md#oop-refactor-verification),
[lifecycle](.scratch/ticket-harness/spec.md#ticket-lifecycle),
[exact revisions](.scratch/ticket-harness/spec.md#independent-checks-and-exact-revisions),
[QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa)
and [safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation).

The run owns initialization and deliberate continuation through cohesive
operations. Public run/continue retain output creation, exclusive ownership and
appropriate rejection, then use a small lifecycle interface. External orchestration
must no longer patch configuration, protected source, milestone index and lifecycle
records in a required sequence. Internal types/methods/layout remain worker choices.

Preserve branch validation and matching base/integration, approved-input protection,
one baseline and no workers/repairs after baseline failure. Retain existing failure
stage diagnostics, outcomes, blocked/pending observations and exits for invalid
inputs, environment/integrity, baseline and later workflow failures. The run
coordinates ticket 21 through ticket 22 prepared inputs, owns milestone progression
and finalization, and keeps fail-fast scheduling and exact human acceptance gates.
Attempt/ticket operations continue owning their lifecycle records.

Continue validated deliberate checkpoints without replaying Done work, baseline,
artifacts or consumed decisions. Invalidate the stopped marker before resumed work;
preserve milestone/history/ref identities, stop exit 2, success exit 0 and rejection
behavior. The run exports and rebuilds verified-check information in the existing
checkpoint shape; QA uses that operation without inspecting internal tuple/list
organization. Restored references must resolve to canonical durable gate records
so later invalidation changes those actual records, including repeated continuation.

Preserve commands, JSON schemas/values, checkpoint version/names, single/multi-ticket
and milestone artifacts, process ownership, integrity and atomic persistence.
Leave Git/process/filesystem primitives as functions. Avoid a separate checker or
generic lifecycle framework. Keep QA callable working; do not implement 24 ownership,
29 isolation, 33/34 runtime, orchestration or actual development QA acceptance.

## Verification, reviews and completion

Apply [efficient development](docs/agents/development-efficiency.md): finish local
diagnosis/checks and one canonical packet before review; preserve both originals
before a fresh Medium repair and batch complete authorized diagnosis. Ticket 22 used one
Medium worker and one clean independent review pair; no repair or repeated-failure
diagnosis carries forward.
Prior capture corrections in [checkpoint
history](.scratch/ticket-harness/evidence/22-checkpoint/history.md)
retain an initial pre-format continuation and a final-source continuation restored
from the genuine stopped archive. No earlier prospective pointer proves final
bytes; use final-consumer-source.json and continuation-final.json with their scope.

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or tests; use the absolute reusable prefix. Follow
[testing policy](docs/agents/testing.md), test-strategy and
[documented checks](docs/ticket-harness.md#python-and-checks). Map existing fresh-run,
failed baseline, invalid input, sequential dependency and status tests in test_cli,
test_preflight, test_dependencies and test_milestones. Map deliberate/new-process/
repeated continuation, active-owner rejection and restored canonical invalidation
in test_continuation and test_qa_promotion. Add only distinct uncovered failures
using TDD at the approved public CLI/scripted-process/isolated-Git seam; avoid tests
prescribing private classes. Use focused development checks, then full pytest,
strict mypy, Ruff lint/format and whitespace on final implementation. Packaging
follows actual impact. Relevant executable edits renew required final-source gates;
bookkeeping alone receives document/link/source-consistency validation.

Arrange commands/exits/source/test hashes, logs and needed CLI/Git/record/ref capture
before checks. Produce a genuine pre-refactor deliberate checkpoint before runtime
edits; preserve actual live fixture through cleanup and producer/source provenance,
then continue it under final source. Ticket 22's
[producer](.scratch/ticket-harness/evidence/22-checkpoint/producer.json),
[final continuation](.scratch/ticket-harness/evidence/22-checkpoint/continuation-final.json),
[consumer identity](.scratch/ticket-harness/evidence/22-checkpoint/final-consumer-source.json)
and stopped/continued archives show retained observations, not a substitute for
your own pre-23 producer. Preserve ticket 20's original fixture-loss/timing limits
and all historical reports. A fabricated post-refactor checkpoint is insufficient.

Commit implementation after final checks and before separate fresh High Spec and
Standards whole-ticket reviews from your original baseline. Supply ownership,
coverage, unchanged flows, exact checks/source, all relevant keys/history, omitted
scope and G2/C5 limits. Preserve originals before aggregation. Blocking findings
use fresh Medium repairs, renewed gates, committed fixes and fresh whole-ticket
axes from the original baseline. Optional suggestions stay optional; consequential
scope/risk/QA authority remains human-owned.

Once every criterion/gate passes, preserve original criterion wording and Blocked
by, check verified criteria, set Status completed, retain previous readiness in
the completion comment, link evidence from feature/review indexes and commit only
bookkeeping separately. Automatically use create-next-agent-prompt, verify actual
milestone/prerequisite eligibility again and separately commit only the generated
handoff. Never start another ticket while creating it.

Preserve unrelated edits, original evidence, completed requirements, archives and
frozen QA snapshots. If a requested authoring file is an active input, report the
exact mutation blocker and keep it immutable. Return implementation/bookkeeping/
handoff commits, actual checks, separate review outcomes, criterion evidence,
unchecked items, unresolved full keys and next selection or exact blocker.
Ticket completion implies no milestone acceptance, promotion or push.
