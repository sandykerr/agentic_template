Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/18-gate-development-on-cumulative-architecture-review.md`

**18: Gate development on cumulative architecture review**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/18-gate-development-on-cumulative-architecture-review.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
This handoff starts no assignment, harness run, reviewer evaluation or QA session.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), applicable [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed whole-ticket review baseline; inspect and preserve the actual worktree.

Approved **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md).
M1 (10–24) is the earliest required milestone awaiting human acceptance.
Tickets 10–17 are completed; 18 is open, unclaimed, agent-ready and next in
preferred prerequisite-ready order. Its declared prerequisites are 16 and 17.

Verify both prerequisites from actual evidence and ancestor commits:

- 16: [completion](.scratch/ticket-harness/evidence/16-completion.md),
  [checks](.scratch/ticket-harness/evidence/16-checks.log),
  [Spec](.scratch/ticket-harness/evidence/16-review-spec.md),
  [Standards](.scratch/ticket-harness/evidence/16-review-standards.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-16.md).
  Implementation `3c8d4ab52c5da112552275d1d5fffdef001c1451`;
  bookkeeping `6b8dae9eb8f436e60224bea9b9fd4b0b8bf61e02`.
- 17: [criterion evidence](.scratch/ticket-harness/evidence/17-completion.md),
  [checks](.scratch/ticket-harness/evidence/17-checks.log),
  [Spec](.scratch/ticket-harness/evidence/17-review-spec.md),
  [Standards](.scratch/ticket-harness/evidence/17-review-standards.md),
  [assessment](.scratch/ticket-harness/reviews/ticket-17.md),
  [bookkeeping validation](.scratch/ticket-harness/evidence/17-bookkeeping-checks.log).
  Implementation `4814eabd4bf2f196f7fb6915667c4305b7c2d0b9`;
  bookkeeping `91e285ff3cb1b46f4404b7fc534625637bdff015`.

The worktree was clean after ticket 17 bookkeeping; inspect again. Historical
checks prove their recorded source, not ticket 18. Keep historical publication/
completion descriptions at their original scope; current milestone membership governs.
Preserve active-run inputs and frozen QA evidence; active-input mutation is an exact blocker.

## Roles, ownership and review context

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**,
independently configured **High Spec** and **High Standards**, no worker override.
Target at most **250,000 active-context tokens per assignment**, leaving headroom
for checks/handoff. Report unavailable settings rather than guessing. These are
development settings, not proof of runtime enforcement or instruction delivery.
Apply ticket role guidance: test-strategy and codebase-design for worker/repair
and Standards; authors also use writing-for-agents and installed skill-creator.
Preserve upstream skills.

Read the scoped spec contracts:
[review records](.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership/scope](.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review),
[cumulative checkpoints](.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints),
[reviewer evaluation](.scratch/ticket-harness/spec.md#reviewer-evaluation),
[verification](.scratch/ticket-harness/spec.md#review-process-verification) and
[roles](.scratch/ticket-harness/spec.md#role-configuration).

Apply [ownership and review scope](docs/agents/ownership-review.md),
[review records/templates](docs/agents/review-records.md) and
[review index](.scratch/ticket-harness/reviews/README.md).
Planning records consequential state owner, permitted writers, operations,
persistence/restoration/invalidation and failure behavior. Explain changed or
unchanged ownership; missing consequential choices stay human-owned. Ticket 17
changed guidance responsibility only: the shared scope contract owns substantive
reasoning; review records own identity/history/authority. Executable owners and
saved schemas are unchanged. Ticket 18 must assess its own affected flows,
including unchanged planning, implementation, review, milestone and handoff consumers.

Both prerequisite assessments have **no unresolved real findings**, missing
reports or pending exact-source revalidation/human decisions. Original reports
and identities are linked above. Cumulative M1 assessment is **not yet performed**;
M1 QA is **not requested/accepted**. The responsible next action is ticket 18's
bounded checkpoint-guidance/evidence work, then remaining M1 work and eventual
actual cumulative assessment/QA under their authorized workflows.

[Ticket 17 walkthroughs](.scratch/ticket-harness/evidence/17-walkthroughs/README.md)
are finite development examples: A/B/C concerns remain intentionally open in
representative sources, D's failed trial is retained and its exact fixture fix
independently verified, and C's optional proposal remains separate from its blocker.
They are not real harness blockers, broad calibration or milestone acceptance.
Ticket 16 miniature concerns/decisions remain synthetic. Carry real future findings
by full review/report/local key with append-only history; never rewrite originals.

## Bounded outcome: all six criteria

The ticket's exact wording controls:

1. Create cumulative work before each required development milestone QA request,
   recording exact source, cumulative baseline, complete inventory and prior findings.
   Use the last accepted milestone or feature starting revision for the first;
   keep this distinct from the ticket's newly captured review baseline. Identify
   actual evidence rather than inventing an accepted baseline. A package assessment
   covers all `ticket_harness` Python files; larger targets cover the affected workflow.
2. Assess risk triggers at ticket start and after implementation: new lifecycle,
   persistence/restoration path, shared state or additional writer. A trigger
   requires broader assessment before integration; expose missing/incomplete work.
   Do not add a third unconditional review to every ticket.
3. Use a fresh High Standards assignment for cumulative scope, retaining independent
   ticket Spec/Standards axes. Examine ownership and concrete edits for a plausible
   change. Reuse an audit only if exact source, coverage and dispositions still match.
4. Keep open findings visible; fixed requires exact independent verification,
   deferral needs a linked ticket, consequential acceptance/deferral/contract change
   needs actual human authority and applicable amendment. Existing in-scope blockers
   prevent affected integration/readiness; optional suggestions remain optional.
5. Distinguish assessment complete, findings resolved/dispositioned, candidate ready
   and milestone accepted. Clean reviews progress autonomously within scope.
   Changed source invalidates relevant prior readiness until renewed review;
   comments do not automatically require human approval.
6. Demonstrate accumulating cross-module trouble despite passing ticket reviews,
   risk-triggered pre-integration review, stale-source rejection, clean checkpoint,
   blocked progression, human disposition and deferred-work handoff. Retain actual
   cumulative assignments/reports, source inventory and observed readiness outcomes.
   Preserve original evidence, decisions and active snapshots. Label isolated example
   human statements honestly; do not invent actual human acceptance.

Use existing repo-owned workflows and shared contracts. Automated runtime adoption
belongs to 33, broad calibration/corpus to 19, ownership refactors to 20–24 and
real delivery to 34. Do not start neighboring tickets or enlarge runtime schemas.
Existing example evidence cannot substitute for this ticket's actual observations.
Reuse architecture guidance without requiring every assessment to render HTML.

## Checks, independent review and completion

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or checks; reuse its absolute micromamba environment. Follow
[testing policy](docs/agents/testing.md),
[test-strategy](.agents/skills/custom/test-strategy/SKILL.md) and
[documented checks](docs/ticket-harness.md#python-and-checks).
Map acceptance requirements to existing coverage and missing observations; plan
evidence retention before checks. Standalone guidance needs document/skill,
link/anchor/routing and isolated workflow validation. Historical evidence helpers
may overwrite saved outputs: inspect them and use read-only routines for audits.
Executable harness changes require TDD at the public CLI/scripted-process/real
isolated-Git seam and full final-source pytest, strict mypy, Ruff lint/format,
whitespace and explicit gates; packaging checks follow impact/policy.

Commit only implementation before code-review, supplying the original fixed
baseline, exact source, ticket/contracts, scope inventory, prior finding history
and check/coverage evidence. Obtain separate fresh High Spec/Standards reports.
Standards follows unchanged callers, writers, consumers and restore/invalidation;
Spec checks approved behavior/ownership. Each records inspected/omitted scope,
assumptions, source/guidance identity and concrete reasoning; no universal short cap.
Preserve both original axes before aggregation. Provenance audits/tests cannot
replace substantive design assessment. Resolve authorized blockers through fresh
Medium repairs, renew affected checks, commit and independently re-review the
whole ticket from its original baseline; keep optional suggestions separate.

Only after every criterion and gate passes, mark verified checkboxes, set
`**Status:** completed`, retain previous `ready-for-agent`, preserve `Blocked by:`,
append criterion/check/review evidence and link it from the index. Commit bookkeeping
separately. Then automatically use create-next-agent-prompt and commit the handoff
separately, rechecking eligibility; 19 is expected next only if evidence permits.
Do not begin another ticket. Unverified criteria remain unchecked with exact blockers.

M1 still requires 18–24 plus cumulative assessment and explicit human QA.
M2 (25–29) remains gated until M1 acceptance; later M3/final M4 and separate E1
priority immediately after verified 34 follow the published milestones. Ticket Done,
review completion and plan approval never accept a candidate. No push, promotion
or human acceptance is authorized.

Return implementation/bookkeeping/handoff commits, actual checks, separate review
outcomes, criterion evidence, unchecked items, unresolved findings and next prompt
path/selection or exact checkpoint/blocker status.
