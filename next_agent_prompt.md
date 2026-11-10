Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/22-return-clearly-prepared-inputs.md`

**22: Return clearly prepared inputs**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/22-return-clearly-prepared-inputs.md) and
[implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
Creating this handoff starts no assignment, harness run, QA session or acceptance.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed original whole-ticket review baseline; historical references below
do not replace it. Inspect and preserve the actual worktree and unrelated changes.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone without human acceptance. Tickets 10–21 are completed; 22 is
open, unclaimed, agent-ready and next in preferred prerequisite-ready order.
Verify actual prerequisites from checked criteria, checks, separate reviews and
implementation/bookkeeping ancestry:

- **02:** implementation `b11fd20f37dbb18730278bd271cf3d47d05f6e82`, bookkeeping
  `1f7a199006bfd9ea8d0608f2ddc4fbfca4369457`;
  [five-criterion completion/check/review evidence](.scratch/ticket-harness/evidence/02-completion.md).
  Its historical readiness header remains ready-for-agent; actual checked criteria,
  completion comment/evidence, checks/reviews and commits establish completion.
  Preserve that historical record.
- **12:** implementation `14cafef40726eba80d8648d98d9c263fde3a5d0b`, bookkeeping
  `969f043db6de11728a9c99b0d66c6877961dbf7e`;
  [five-criterion completion/check/review evidence](.scratch/ticket-harness/evidence/12-completion.md).
- **19:** final implementation `8e2c82679a2314e31ebff69accab3743f55f996d`, bookkeeping
  `c63570666b21cb5cb8c6063c4f328c9273aaa15b`;
  [six-criterion completion/check/review evidence](.scratch/ticket-harness/evidence/19-completion.md),
  [assessment/history](.scratch/ticket-harness/reviews/ticket-19.md).

[Eligibility/producer audit](.scratch/ticket-harness/evidence/21-root-eligibility.json)
records those identities. Historical checks establish their source, not ticket 22.
M1 still needs 22–24, actual cumulative assessment and explicit human QA. Later
required milestones remain gated; E1 retains priority immediately after verified 34.
No push or promotion is authorized.

## Current source, roles and review context

Ticket **21** implementation `10b7050ec1fc06767e473b90217fa0d0bd100a0f` and
bookkeeping `09072acd7c03c00e4cfc7212c3f66f1ddb50454b` are complete. Read its
[completion](.scratch/ticket-harness/evidence/21-completion.md),
[ownership/coverage report](.scratch/ticket-harness/evidence/21-implementation-report.md),
[criterion observations](.scratch/ticket-harness/evidence/21-criterion-evidence.md),
[assessment](.scratch/ticket-harness/reviews/ticket-21.md),
[Spec original](.scratch/ticket-harness/evidence/21-review-spec-01.md),
[Standards original](.scratch/ticket-harness/evidence/21-review-standards-01.md) and
[immutable capture](.scratch/ticket-harness/evidence/21-review-round1-capture.json)
as needed. Required checks: **544 passed in 775.37s**, strict mypy, Ruff lint/format
and whitespace all passed on bytes independently matched to 26 committed identities.
No tests changed. Both independent axes report 0 blocking/0 optional; Spec
independently reproduced four CLI cases. Those checks do not verify ticket 22.

One ticket execution now owns the complete fixed-base cycle and bounded repairs.
Runner coordinates eligible tickets and consumes a promoted result, retaining
checking, canonical invalidation and scoped verification effects. Attempt ownership
from 20 stays intact. Input preparation still enters through `inputs.load`, with
runner consumers and plan validation. Inspect actual definitions/usages and saved
checkpoint consumers; preserve completed 20/21 ownership while doing only this slice.

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, no
worker override; independently configured **High Spec** and **High Standards**.
Target <=250000 active-context tokens per assignment; report unavailable settings
and telemetry. Configuration does not prove backend delivery/runtime enforcement.
Worker/repair/Standards add [OOP](.agents/skills/microsoft/microsoft_oop/SKILL.md),
[codebase design](.agents/skills/matt-pocock/codebase-design/SKILL.md) and
[test strategy](.agents/skills/custom/test-strategy/SKILL.md). Spec uses agreed
behavior/coverage contracts. Apply writing-for-agents/skill-creator when authoring
requires them; preserve upstream skills unchanged.

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records/templates](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and the
[review index](.scratch/ticket-harness/reviews/README.md). Record entry callers,
owners, every writer/consumer, initialization, save/restore and invalidation, with
changed/unchanged responsibility reasoning. Missing consequential decisions remain
human-owned.

Use [evaluated guidance](docs/agents/reviewer-evaluation.md): substantive **G2**,
final **C5** [declaration](.scratch/ticket-harness/evidence/19-evaluation-g5/declaration.md),
[manifest](.scratch/ticket-harness/evidence/19-evaluation-g5/source-manifest.json),
[original reports/index](.scratch/ticket-harness/evidence/19-evaluation-g5/README.md)
and [results](.scratch/ticket-harness/evidence/19-evaluation-g5/results.md).
C5 aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`.
Five evolving eight-case corpora/two guidance versions preserve failed trials,
misses, invalid controls and differing judgments. One independent final observation
per axis is finite evidence, not a detection/reliability/runtime guarantee.
Assess actual ticket-22 source; corpus classifications supply no answer pattern.

Ticket 21's four start/final triggers were independently **No**: existing lifecycle,
state and persistence paths stayed; writers migrated to approved owners. Reassess
**each trigger at ticket 22 start and after changes**: new lifecycle,
persistence/restoration path, shared mutable state, additional writer. A positive
trigger requires fresh broader affected-workflow assessment before integration;
negative triggers require no unconditional third reviewer. Ordinary axes remain
independent. No unresolved actual key, missing required prerequisite report,
pending relevant revalidation or human-owned decision carries from 21; see its
[explicit history](.scratch/ticket-harness/evidence/21-finding-history.md).
Prior fixed keys and historical fixture findings retain their source scopes.

Real **M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before eventual readiness establish actual feature-start provenance, distinct from
your ticket baseline, exact source and substantive inspection of **all
`ticket_harness` Python files**. Missing/stale required work holds readiness;
assessment completion never supplies milestone acceptance.

## Bounded implementation and compatibility

The ticket's **seven original criteria** control. Read scoped spec:
[state/decision ownership](.scratch/ticket-harness/spec.md#state-and-decision-ownership),
[refactor verification](.scratch/ticket-harness/spec.md#oop-refactor-verification),
[ticket lifecycle](.scratch/ticket-harness/spec.md#ticket-lifecycle),
[exact revisions](.scratch/ticket-harness/spec.md#independent-checks-and-exact-revisions),
[QA/promotion](.scratch/ticket-harness/spec.md#feature-to-development-promotion-and-human-qa)
and [safe continuation](.scratch/ticket-harness/spec.md#corrections-and-safe-continuation).

Return one explicit complete prepared-input result containing validated execution
settings, approved snapshots, normalized requirements, ticket selection, completion
evidence and applicable worker settings. Make filesystem preparation requirements
explicit. Keep raw settings separate from derived values; the run consumes the
result without repeating preparation rules or externally filling calculated fields
into raw configuration. Internal result types/names/layout remain worker decisions.

Preserve one preparation operation's executable-command validation, approved-file
capture/identities, normalization, dependency/completion validation, eligible
selection and worker settings. Missing/malformed/conflicting/changed inputs retain
actionable diagnostics and invalid-input rejection before workers, checks or ref
advancement. All plan consumers, including first-milestone selection, must use the
**checked plan returned by validation**. Membership, dependency order, role defaults
and worker overrides stay governed together by validation. Callers cannot depend
on mutation of the original plan; making validation pure is not required.

Preserve legacy no-plan runs, versioned plans, externally completed prerequisites,
explicit selection, primary-ticket handling, readiness/completion/metadata rules,
worker default/override inheritance and later-milestone eligibility. Keep config
and approved input files byte-for-byte unchanged during execution. Preserve copied
input names/hashes, output separation, JSON-safe saved configuration/checkpoint
contents, checkpoint version and status behavior. Translate any new in-memory
result into the existing saved shape; genuine older checkpoints must continue.

Complete every caller migration. Pure parsing, normalization, graph checks and
transformations remain functions where they own no independent lifecycle. Avoid
a configuration framework or private testing seam. Do not implement run/restore
ownership 23, milestone review 24, blocked-work isolation 29, runtime 33/34,
orchestration, QA-session execution or acceptance.

## Verification, reviews and completion

Apply [efficient development](docs/agents/development-efficiency.md): finish local
diagnosis/checks and retain one canonical packet before review; preserve both
originals before fresh repair and batch the complete authorized diagnosis. Ticket
21 used one worker and one clean review pair; no repair/repeated-failure diagnosis
carries forward. Its interrupted slow archive audit was evidence-only, corrected
with streaming access; [history](.scratch/ticket-harness/evidence/21-audit-history.md)
retains that limit without calling it a runtime failure or requiring suite replay.

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or tests; use the absolute reusable prefix. Apply
[testing policy](docs/agents/testing.md), test-strategy and
[documented checks](docs/ticket-harness.md#python-and-checks). Map criteria first to
existing public CLI/scripted-process/isolated-Git cases in test_preflight,
test_dependencies and test_milestones, plus affected continuation/repair coverage.
Preserve invalid-plan rejection before processes/refs, normalized first-group
selection and worker-setting metadata. Add only distinct uncovered failures using
TDD at the approved seam; no private result-class or mutation-free-validator tests.
Use focused development checks, then full pytest, strict mypy, Ruff lint/format
and whitespace on final implementation. Packaging follows actual impact. Renew
required exact-source checks after relevant executable changes; bookkeeping alone
receives document/link/source-consistency validation.

Arrange command/exit/source/test hashes, logs and necessary CLI/Git/record/ref
capture **before execution**. Establish a genuine pre-refactor deliberate checkpoint
before runtime edits, retain producer/source provenance and the actual live fixture
through cleanup, then continue it under final source. Ticket 21's
[producer](.scratch/ticket-harness/evidence/21-checkpoint/producer.json),
[continuation](.scratch/ticket-harness/evidence/21-checkpoint/continuation.json)
and stopped/continued live archives show successful capture. Ticket 20's
[preservation history](.scratch/ticket-harness/evidence/20-checkpoint/preservation-history.md)
retains its original fixture loss and later baseline-code producer timing limit;
preserve that history. A fabricated post-refactor checkpoint alone is insufficient.

After final checks, commit implementation **before** fresh High Spec/Standards
whole-ticket review from your own original baseline. Supply ownership/coverage,
unchanged flows, exact-source/check evidence, prior full keys/history, omissions
and G2/C5 limits. Preserve originals before aggregation. Blocking findings use
fresh Medium repairs, renewed applicable final gates, committed fixes and fresh
whole-ticket axes from the original baseline. Optional suggestions stay optional;
consequential scope/risk/QA authority stays human-owned.

After every criterion/gate passes, reconcile unchanged criterion wording, set
Status completed, retain previous readiness in the completion comment and preserve
Blocked by. Link criterion/check/review evidence from the feature index; commit
bookkeeping separately. Automatically use create-next-agent-prompt after completion,
verify milestone/prerequisite eligibility again and commit only the generated
handoff separately. Never start another ticket while creating it.

Preserve original reports, append-only histories, completed requirements, archives
and frozen QA evidence. If an authoring file belongs to an active run, report the
exact mutation blocker and keep approved inputs immutable. Return implementation,
bookkeeping and handoff commits, actual checks, separate review outcomes, criterion
evidence, unchecked items, unresolved full keys and next prompt selection or exact
blocker. No ticket completion implies M1/final acceptance, orchestration or promotion.
