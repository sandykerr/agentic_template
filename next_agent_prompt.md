Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md`

**19: Evaluate reviewers on known and acceptable designs**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
This handoff starts no assignment, evaluation, harness run or QA session.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), relevant [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed whole-ticket review baseline. Inspect/preserve the actual worktree.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md). M1 (10–24) is the earliest
required milestone awaiting human acceptance. Tickets 10–18 are completed; 19 is
open, unclaimed, agent-ready and next in preferred prerequisite-ready order.
Its prerequisites are 17 and 18. Verify evidence and ancestor commits:

- 17: [completion](.scratch/ticket-harness/evidence/17-completion.md),
  [checks](.scratch/ticket-harness/evidence/17-checks.log),
  [Spec](.scratch/ticket-harness/evidence/17-review-spec.md),
  [Standards](.scratch/ticket-harness/evidence/17-review-standards.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-17.md).
  Implementation `4814eabd4bf2f196f7fb6915667c4305b7c2d0b9`;
  bookkeeping `91e285ff3cb1b46f4404b7fc534625637bdff015`.
- 18: [criterion evidence](.scratch/ticket-harness/evidence/18-completion.md),
  [checks](.scratch/ticket-harness/evidence/18-checks.log),
  [Spec](.scratch/ticket-harness/evidence/18-review-spec.md),
  [Standards](.scratch/ticket-harness/evidence/18-review-standards.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-18.md),
  [bookkeeping validation](.scratch/ticket-harness/evidence/18-bookkeeping-checks.log).
  Implementation `816aecbaa67f79ca5fd97c78f40593cdb007c45a`;
  bookkeeping `aef9625c3d155815df22f3e827559ef23fcdcf03`.

The worktree was clean after ticket 18 bookkeeping; inspect again. Historical
checks prove their recorded source, not ticket 19. Preserve original completed
requirements, reports, decisions, archives and frozen QA evidence. If an intended
authoring file is an active-run input, report that exact mutation blocker.

## Roles, ownership and checkpoint context

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**,
independently configured **High Spec** and **High Standards**, no worker override.
Target at most **250,000 active-context tokens per assignment**. Report unavailable
settings; configuration does not prove backend enforcement or instruction delivery.
Use test-strategy and codebase-design for worker/repair and Standards. Authors
also use writing-for-agents and installed skill-creator where applicable.
Preserve upstream skills; repo-owned wrappers/references carry project policy.

Read the scoped spec:
[review work](.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership/scope](.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review),
[checkpoints](.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints),
[reviewer evaluation](.scratch/ticket-harness/spec.md#reviewer-evaluation),
[verification](.scratch/ticket-harness/spec.md#review-process-verification) and
[role configuration](.scratch/ticket-harness/spec.md#role-configuration).

Apply [ownership/scope](docs/agents/ownership-review.md),
[review records/templates](docs/agents/review-records.md),
[architecture checkpoints](docs/agents/architecture-checkpoints.md) and the
[review index](.scratch/ticket-harness/reviews/README.md). Record affected entry
callers, owners, writers, consumers, persistence/restoration and invalidation.
Explain changed/unchanged ownership. Shared scope guidance owns substantive
inspection; review records own identity/history/authority; checkpoint guidance
owns when cumulative work gates progression. Existing planning, implementation,
milestone and both handoff branches consume these contracts. Executable owners
and schemas were unchanged by 17/18. Missing consequential decisions stay human-owned.

Both prerequisite assessments have **no unresolved actual findings**, missing
reports, pending relevant revalidation or required actual human decisions.
Record all four risk triggers at ticket start and after implementation. A positive
trigger requires broader affected-workflow assessment before integration; a
negative result needs no unconditional third review. Preserve independent ticket
Spec/Standards axes. Carry full finding keys and append-only dispositions.

**Real M1 cumulative assessment remains unperformed**, QA not requested/accepted.
Before eventual readiness, establish actual feature-start provenance (or the last
accepted milestone for later checkpoints), distinct from your ticket baseline,
and inspect all `ticket_harness` Python files on the then-current exact source.
Missing provenance/report or stale required work holds affected readiness. Ticket
18's real-package inventory is inventory only. Assessment complete, findings
dispositioned, candidate ready and milestone accepted are separate. Clean review
progresses autonomously within scope; exact-candidate acceptance remains human-owned.

Prior finite examples are context, not this ticket's declared evaluation corpus:
[17 walkthroughs](.scratch/ticket-harness/evidence/17-walkthroughs/README.md) retain
failed D/exact D2 and representative concerns;
[18 walkthrough](.scratch/ticket-harness/evidence/18-walkthrough/README.md) retains
four clean A/B axes and actual risk/clean cumulative reports. Isolated
`review-18-fixture-cumulative/standards-risk-01/F1` is independently fixed only at
fixture `8078239cfc1062acbf8e3f59ac2392925da4586a` through preserved
[E04](.scratch/ticket-harness/evidence/18-walkthrough/finding-history.md#e04--independent-exact-source-fix-verification).
Its synthetic alternate human branch retains deferred D/missing scope review and
grants no actual authority. Risk reviewer disclosed incidental builder repair
visibility; no blind-calibration claim was made. No fixture concern is a real
harness blocker. Preserve originals and evaluate ticket 19 independently.

## Bounded outcome: all six criteria

The actual ticket wording controls:

1. Declare a source-identified corpus **before evaluation**: at least four concerns
   and four acceptable controls, expected relevant axis and rationale. Concerns:
   detached restored gate evidence, positional attempt selection, duplicated
   lifecycle-record edits, externally coordinated initialization. Controls:
   cohesive Git validation, pure plan/parsing transformations, atomic file/process
   primitives, explicit owned transitions.
2. Use actual fresh reviewers with agreed settings and exact guidance identities.
   Supply cases/contracts **without the evaluator answer key**, preserve axis
   independence and raw outputs. Scripted reports/text matching/link audits cannot
   establish judgment quality. Keep evaluator/repair material out of reviewer
   inputs where it would reveal expected results; use read-only source snapshots.
3. Detect every seeded required concern with source-specific evidence and
   proportionate classification/remedy. Controls receive no unsupported blocker.
   Judge optional suggestions on evidence. Explain expected/observed matches and
   mismatches, not merely finding counts.
4. Preserve all misses, false blockers, failed trials and guidance versions. A
   required miss/false blocker prevents completion. After guidance correction,
   evaluate final guidance on the **complete declared corpus**; surface unresolved
   limits if criteria cannot be met. Report finite cases and actual repetitions,
   without guarantees of future detection or runtime effectiveness.
5. Publish evaluated guidance version/corpus references through planning and next
   handoffs for refactors 20–24. Preserve authorized repairs and human design/QA
   authority. Actual later refactor evidence belongs to those tickets and M1 QA,
   not a prerequisite to completing this evaluation.
6. Keep development evaluation separate from runtime backend availability and
   delivery. Enforcement/delivery proof belongs to 33/34. Use isolated development
   assignments without launching a harness run, fabricating acceptance or adding
   private-module production tests.

Do not implement refactors 20–24 or runtime ticket 33, launch ticket 34, enlarge
runtime schemas or accept M1. Evaluate reviewers and publish usable evidence
within existing workflows.

## Validation, independent review and completion

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or checks; reuse its absolute micromamba environment. Follow
[testing policy](docs/agents/testing.md),
[test strategy](.agents/skills/custom/test-strategy/SKILL.md) and
[documented checks](docs/ticket-harness.md#python-and-checks). Map requirements to
existing coverage/missing observations and arrange evidence capture first.
Standalone guidance/evaluation receives document/skill, source/link/routing and
actual isolated workflow validation. Inspect historical helpers before reuse:
some overwrite saved outputs. Retain raw inputs, assignment identities, commands,
exits, outputs and all trials. Production executable changes require TDD at the
approved public CLI/scripted-process/real isolated-Git seam and full final-source
pytest, strict mypy, Ruff lint/format, whitespace and explicit gates; packaging
checks follow impact/policy. Preserve the agreed seam.

After checks pass, commit only implementation before code-review. Supply your
original fixed baseline, exact source, ticket/spec, contracts, affected scope,
prior finding history and coverage/check evidence to separate fresh High
Spec/Standards reviewers. Each assesses source substantively; Standards follows
unchanged collaborators, writers and restore/invalidation. Preserve both original
axes before aggregation. Corpus reviewers do not replace implementation reviews.
Resolve blockers through fresh Medium repairs, renew affected checks, commit and
independently re-review the whole ticket from its original baseline. Optional
suggestions remain optional; no universal short cap hides required reasoning.

Only after every criterion/gate passes, reconcile checkboxes without changing
wording, set `**Status:** completed`, retain previous `ready-for-agent` in the
completion comment and preserve `Blocked by:`. Link criterion/check/review
evidence from the index and commit bookkeeping separately. Unverified criteria
remain unchecked with exact blockers. Then automatically use
[create-next-agent-prompt](.agents/skills/custom/create-next-agent-prompt/SKILL.md)
and commit only the generated handoff separately. Recheck eligibility; 20 is
expected next only if prerequisites/evidence permit. Do not begin another ticket.

M1 still requires 19–24 plus its genuine cumulative assessment and explicit human
QA. M2 (25–29) waits for M1 acceptance; M3/final M4 and separate E1 priority
immediately after verified 34 follow published milestones. Ticket Done and plan
approval never accept a candidate. No push, promotion or human acceptance is
authorized. Keep orchestration, candidate preparation, QA execution and approval
recording in separately authorized workflows.

Return implementation/bookkeeping/handoff commits, actual checks, separate review
outcomes, criterion evidence, unchecked items, unresolved full finding keys and
next prompt path/selection or exact checkpoint/blocker status.
