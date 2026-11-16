# 14: Consume approval, promote, and continue

**What to build:** Watch the separate decision artifact indefinitely. Require an exact approval field and matching request identities; reject stale, malformed, mismatched, incidental, or consumed approvals. Advance dev only to the tested accepted candidate with expected-old checks, align the feature branch, and admit the next group. Final QA promotion completes the feature.

**Blocked by:** [13: Present a tested feature-to-dev candidate](13-prepare-a-tested-feature-to-dev-candidate.md).

**Status:** completed

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R05](../ticket-proposal.md#r05-consume-approval-promote-and-continue).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa); [ticket lifecycle](../spec.md#ticket-lifecycle).

## Acceptance criteria

- [x] Watch a separate QA decision artifact with an exact approval field and matching request identities; incidental text, missing/malformed/mismatched/stale/replayed approvals cannot authorize promotion.
- [x] Keep QA waits observable and indefinite without consuming repairs or treating human waiting alone as failure; implementation/repair output cannot self-approve.
- [x] After explicit human acceptance, compare expected branch states and advance dev only to the exact tested candidate; align the feature branch before starting the next milestone.
- [x] Preserve external branch changes, reject stale approvals, and record the consumed decision so it cannot promote twice.
- [x] Complete the feature only after final QA promotion; all required tickets Done while awaiting acceptance remains a waiting feature.
- [x] Demonstrate two foreground scripted milestones, rejected stale approval, first approval unlocking later work, and final approval completing the feature.

## Verification

A two-milestone foreground fixture shows waiting, stale approval rejected without promotion, first acceptance unlocking later work, and final acceptance completing the feature. Branch movement cannot be overwritten; waiting consumes no repairs.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

Completed at implementation `29fb5569cf53c75bd351d6bd176bb29889c42a65`, reviewed
against fixed starting baseline `d67c12d91495af00557b279d0bf0e1da518e6fcc`.
Previous readiness: `ready-for-agent`; declared dependency history is unchanged.

All six criteria are verified in [criterion-specific completion evidence](../evidence/ticket-14/14-completion.md):
strict separate decisions reject incidental/malformed/mismatched/stale/replayed
approvals; observable indefinite waits consume no repairs and workers cannot
write QA authority; one expected-old transaction advances dev and aligns feature
to the tested accepted candidate before later work; stale source/evidence/ref
states preserve external movement and consume no approval; final acceptance alone
completes the feature; a two-milestone foreground fixture demonstrates the cycle.

[Actual checks (retirement summary)](../evidence/ticket-14/README.md#retired-evidence): **524 passed in 684.03s**, strict mypy,
Ruff lint/format and whitespace all passed. All 21 final source hashes match the
implementation and all 103 retained scenarios match raw observations. Separate
fresh High [Spec](../evidence/ticket-14/14-review-spec.md) and
[Standards](../evidence/ticket-14/14-review-standards.md) reviews found zero blockers.
Spec recorded zero optional suggestions and independently passed the two-group
CLI scenario; Standards recorded one optional polling-helper consolidation.
No unchecked criterion or required unresolved item remains.

Implementation is committed separately from ticket/index/evidence bookkeeping;
this comment's Git history identifies the bookkeeping commit. Next-agent handoff
receives a separate commit and does not launch ticket 15. Ticket 15 is next within
M1; M1 and final feature human QA remain unaccepted. Scripted fixture decisions do
not accept this development milestone. No push occurred.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
