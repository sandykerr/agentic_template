# 14: Consume approval, promote, and continue

**What to build:** Watch the separate decision artifact indefinitely. Require an exact approval field and matching request identities; reject stale, malformed, mismatched, incidental, or consumed approvals. Advance dev only to the tested accepted candidate with expected-old checks, align the feature branch, and admit the next group. Final QA promotion completes the feature.

**Blocked by:** [13: Present a tested feature-to-dev candidate](13-prepare-a-tested-feature-to-dev-candidate.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R05](../ticket-proposal.md#r05-consume-approval-promote-and-continue).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa); [ticket lifecycle](../spec.md#ticket-lifecycle).

## Acceptance criteria

- [ ] Watch a separate QA decision artifact with an exact approval field and matching request identities; incidental text, missing/malformed/mismatched/stale/replayed approvals cannot authorize promotion.
- [ ] Keep QA waits observable and indefinite without consuming repairs or treating human waiting alone as failure; implementation/repair output cannot self-approve.
- [ ] After explicit human acceptance, compare expected branch states and advance dev only to the exact tested candidate; align the feature branch before starting the next milestone.
- [ ] Preserve external branch changes, reject stale approvals, and record the consumed decision so it cannot promote twice.
- [ ] Complete the feature only after final QA promotion; all required tickets Done while awaiting acceptance remains a waiting feature.
- [ ] Demonstrate two foreground scripted milestones, rejected stale approval, first approval unlocking later work, and final approval completing the feature.

## Verification

A two-milestone foreground fixture shows waiting, stale approval rejected without promotion, first acceptance unlocking later work, and final acceptance completing the feature. Branch movement cannot be overwritten; waiting consumes no repairs.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
