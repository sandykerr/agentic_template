Use $implement-with-checkboxes to implement only:
`.scratch/ticket-harness/issues/17-review-ownership-across-affected-modules.md`

**17: Review ownership across affected modules**

Work in `/home/ajkerr1/development/agentic_template`. Read the actual
[ticket](.scratch/ticket-harness/issues/17-review-ownership-across-affected-modules.md)
and [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md).
This handoff starts no assignment, harness run, reviewer evaluation or QA session.

## Starting state and eligibility

Follow [AGENTS.md](AGENTS.md), [domain guidance](docs/agents/domain.md),
[GLOSSARY.md](GLOSSARY.md), applicable [ADRs](docs/adr/),
[tracker conventions](docs/agents/issue-tracker.md) and
[readiness guidance](docs/agents/triage-labels.md). Capture your own starting HEAD
as the fixed whole-ticket review baseline and preserve the actual worktree.

Approved plan **oop-v2 / review-process-1** is recorded in the
[approval](.scratch/ticket-harness/approval.md),
[index](.scratch/ticket-harness/README.md),
[proposal](.scratch/ticket-harness/ticket-proposal.md) and
[milestones](.scratch/ticket-harness/milestones.md).
M1 (10–24) is the earliest required milestone awaiting human acceptance. Tickets
10–16 are completed; 17 is open, unclaimed, agent-ready and next in preferred
prerequisite-ready order. Its only declared prerequisite is 16. Verify its
[criterion evidence](.scratch/ticket-harness/evidence/16-completion.md),
[actual checks](.scratch/ticket-harness/evidence/16-checks.log),
[Spec report](.scratch/ticket-harness/evidence/16-review-spec.md),
[Standards report](.scratch/ticket-harness/evidence/16-review-standards.md), and
[real assessment](.scratch/ticket-harness/reviews/ticket-16.md).
Implementation is `3c8d4ab52c5da112552275d1d5fffdef001c1451`; bookkeeping is
`6b8dae9eb8f436e60224bea9b9fd4b0b8bf61e02`. Both must be ancestors of your starting HEAD. Historical
checks verify their source, not ticket 17. Prior publication records and historical
completion descriptions retain their original scope; current membership governs.

The prior worktree was clean after ticket 16. Inspect again rather than assuming
that remains true. Preserve approved inputs during active runs and all original
reports/frozen QA evidence; report active-input mutation as an exact blocker.

## Scope, roles and existing records

Read scoped spec sections for
[review records](.scratch/ticket-harness/spec.md#review-work-findings-and-decisions),
[ownership and review scope](.scratch/ticket-harness/spec.md#ownership-contracts-and-cross-module-review),
[architecture checkpoints](.scratch/ticket-harness/spec.md#cumulative-architecture-checkpoints),
[reviewer evaluation](.scratch/ticket-harness/spec.md#reviewer-evaluation),
[verification](.scratch/ticket-harness/spec.md#review-process-verification) and
[roles](.scratch/ticket-harness/spec.md#role-configuration).

Use fresh **GPT-6.1 Sol** assignments: **Medium implementation and repairs**, and
separately configured **High Spec** and **High Standards** reviewers. No ticket
worker override applies. Target at most **250,000 active-context tokens per
assignment**, leaving headroom for checks/handoff. Report unavailable model or
configuration rather than guessing. These development settings do not establish
runtime profile enforcement or skill capture. Follow ticket role guidance:
test-strategy and codebase-design for worker/repair and Standards; authoring also
uses writing-for-agents and the installed skill-creator. Keep upstream unchanged.

Use the landed [record contract](docs/agents/review-records.md), linked templates,
[feature review index](.scratch/ticket-harness/reviews/README.md) and
[miniature records](.scratch/ticket-harness/evidence/16-miniature/README.md).
Ticket 16 has no unresolved real findings. Its miniature's open/deferred synthetic
findings are examples, not real accepted risk, blockers or completed milestone
assessments. Carry actual prior findings by full review/report/local key with
append-only dispositions; keep original reports immutable. Changed source requires
relevant exact-source revalidation, not reuse of a historical clean report.

## Bounded outcome: all six criteria

The ticket's exact wording controls. Implement usable repo-owned guidance and
retain observable evidence for:

1. Planning records consequential state owner, permitted writers, invariant-preserving
   operations, persistence/restoration and failures. Workers explain changed or
   unchanged ownership. Surface missing consequential decisions for the human.
2. Preserve the original-baseline whole-ticket review and separate fresh axes.
   Standards follows affected state through unchanged callers/consumers, other
   writers and save/restore/invalidation paths. Spec assesses approved behavior and
   ownership contracts. Scope exceeds diff hunks; no universal short-output cap.
3. Reports identify exact source/baseline, inspected flows/files, omitted scope
   and assumptions. Findings cite concrete contract/code evidence, consequence and
   proportionate remedy. Length or preference for classes alone is insufficient.
4. Carry ticket-16 finding/disposition context into review/repair and independently
   verify fixes against exact repaired source. Preserve axis independence before
   aggregation. Mechanical provenance auditing does not replace design reasoning.
5. Update existing custom planning/implementation/review/handoff guidance to apply
   the shared scope/ownership contract and expose unresolved review work. Preserve
   upstream skills, checks, fresh settings, authorized repairs, optional suggestions
   and milestone gates. Do not invent scope/ownership authority.
6. Demonstrate four cases: an unchanged caller hiding a second state writer; a
   restoration/invalidation path outside the diff; an ownership breach versus an
   optional design suggestion; and a justified clean review of a long cohesive
   function. Retain actual scoped assignments/reports and independence evidence.

Use isolated representative sources/diffs and explicit ownership contracts with
actual fresh development reviewers. Static links or synthetic report text alone
cannot satisfy actual walkthrough evidence. Preserve raw outputs and guidance/model
identities. Broader calibration/corpus belongs to 19; architecture gating to 18;
refactors to 20–24; runtime enforcement/delivery to 33/34. Do not launch neighboring
work or expand runtime schemas merely to implement guidance.

## Checks, review and completion

Read [Python environment](docs/agents/python-environment.md) before Python,
dependencies or checks; reuse its absolute micromamba environment. Follow
[testing policy](docs/agents/testing.md),
[test-strategy](.agents/skills/custom/test-strategy/SKILL.md) and
[documented checks](docs/ticket-harness.md#python-and-checks).
Map requirements to existing coverage and missing walkthrough cases before adding
checks. Plan evidence capture first. Standalone docs/skills use document/skill,
link/anchor/routing validation and retained isolated observations. Executable
harness changes use TDD at the approved public CLI/scripted-process/real-isolated-Git
seam and retain full final-source pytest, strict mypy, Ruff lint/format, whitespace
and explicit gates; packaging follows impact/policy. Do not manufacture runtime
tests for prose or relabel prior evidence as new verification.

Commit only implementation before $code-review, supplying your original fixed
baseline, ticket/scoped spec and coverage/check evidence. Obtain separate fresh
High Spec/Standards reports, preserve originals in the feature evidence context
and attach to one ticket assessment. Record inspected/omitted scope and findings.
For blockers use fresh Medium repairs, renew affected checks, commit, and re-review
the whole implementation against the original baseline. Optional suggestions remain
optional. A consequential decision remains human-owned.

After all criteria/checks/reviews are verified, reconcile the six checkboxes, set
`**Status:** completed`, retain previous `ready-for-agent` in the completion comment
and preserve `Blocked by:`. Link criterion evidence, commits, checks and independent
reports from the ticket/index; commit only bookkeeping separately. Unverified
criteria remain unchecked with the exact blocker. Then follow the implementation
workflow's automatic $create-next-agent-prompt step and separate handoff commit.
Re-evaluate eligibility: 18 is expected next only if current evidence/order permits.
Carry pending reviews/findings and do not start another ticket.

M1 QA remains not requested/accepted. Its boundary requires all 10–24 outcomes
and cumulative architecture assessment; M2 25–29 remains gated until explicit M1
acceptance. M3/final M4 and separate E1 priority immediately after verified 34
follow the published milestones. Ticket Done and plan approval do not accept a
candidate. No push or human QA acceptance is authorized.

Return implementation/bookkeeping/handoff commits, actual check and separate
review outcomes, criterion evidence, unchecked items, unresolved findings, and
next prompt path/selection or exact blocker.
