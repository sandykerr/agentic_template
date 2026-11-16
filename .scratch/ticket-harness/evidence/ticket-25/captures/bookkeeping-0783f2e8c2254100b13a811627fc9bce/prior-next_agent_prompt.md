Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/25-guide-ticket-and-shared-evidence-creation.md`

**25: Guide ticket and shared evidence creation.** Prepared handoff only; this
publication has not started implementation or accepted any evidence milestone.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](GLOSSARY.md), ADRs and the
[tracker](docs/agents/issue-tracker.md). Preserve unrelated changes and capture
your starting HEAD as the fixed whole-ticket review baseline. Read the actual
[ticket](.scratch/ticket-harness/issues/25-guide-ticket-and-shared-evidence-creation.md),
[feature spec](.scratch/ticket-harness/spec.md),
[capture contract](.scratch/ticket-harness/evidence-workflow-spec.md#evidence-creation-skill-and-helper),
[approved shared contract](.scratch/ticket-harness/spec.md#shared-implementation-and-verification-contract)
and [milestones](.scratch/ticket-harness/milestones.md).

Approved plan evidence-policy-1 places EC1 (25–26) before the postponed M2 work.
M1 is actually accepted at source `88e4cd8`; see the
[human decision](.scratch/ticket-harness/evidence/m1-final-review-01/m1-qa-decision.md).
Prerequisite 24 is verified complete at `ab08f7f`; its
[completion evidence](.scratch/ticket-harness/evidence/ticket-24/24-completion.md)
and [independent reviews](.scratch/ticket-harness/reviews/ticket-24.md) retain exact
criteria/results/history. Recheck those identities; readiness alone is not completion.

## Bounded outcome

Deliver only capture-evidence and its Python routing/registration helper: select
ticket or descriptive shared milestone folders, link relevant tickets, preserve
original versus derived evidence and register actual provenance. Give parallel
producers separate destinations and keep shared review decisions free of competing
writes. Establish the authoritative JSON per ticket/shared folder without granting
capture metadata review or deletion authority. Integrate existing development
guidance, protect approved/frozen inputs and demonstrate usable capture through
public command-line and filesystem/JSON observations.

Complete every criterion in the actual ticket. Deletion starts in ticket 26;
parallel assessment, merge review, reassessment and broad calibration belong to
later slices. Automatic harness cleanup remains outside this amendment.

## Roles, ownership and verification

Use fresh GPT-6.1 Sol assignments: Medium implementation/repair, independent High
Spec and High Standards, 250K active-context target. Report unavailable settings
instead of asserting backend enforcement. Apply the
[development review contract](docs/agents/review-records.md): identify routing,
registration and JSON writers, invariants, persistence and failure behavior; assess
architecture triggers before/after implementation and obtain required broader review.

Before Python/checks read the [environment](docs/agents/python-environment.md),
[testing policy](docs/agents/testing.md) and
[test-strategy](.agents/skills/custom/test-strategy/SKILL.md). Follow the current
AGENTS.md ADAPT routing: check hostname, select suitable compute capacity for tests
and intensive work, confirm exact host/architecture/checkout/source/environment,
bound concurrency and retain results in shared storage. Use checkout-local uv.
Read writing-for-agents and skill-creator for skill authoring. Use TDD for distinct
new behavior at the approved public CLI/scripted-process/real-Git seam; map coverage
first and retain required full/static, installed CLI and skill/link/routing checks.

Preserve actual commands, results and source/instruction identities before review.
After passing checks, commit only implementation and obtain separate fresh
Spec/Standards reviews from the original captured baseline under code-review.
Preserve both originals before repairs; resolve blockers with fresh Medium repair,
renew required checks, commit and re-review the whole ticket. Optional findings
stay optional. Product evidence-review roles do not replace implementation reviews.

## Completion and next action

Only after all required criteria/checks/reviews pass, reconcile completion markers,
status and evidence; preserve Blocked by history, record actual commits/results
and commit scoped bookkeeping under the implementation workflow. If incomplete,
leave unverified criteria unchecked and report the blocker. Then refresh the next
handoff through milestone eligibility, with its separate commit when required by
the implementation workflow. Ticket 26 follows 25 within EC1; actual human EC1
acceptance after both gates ticket 27. No automatic next-ticket launch or human
acceptance follows from this handoff. Do not push or mutate frozen active inputs.
Report implementation/bookkeeping/handoff commits, checks, independent review
outcomes, remaining gaps and the next action.
