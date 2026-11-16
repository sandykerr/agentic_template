# 29: Reassess retained evidence during ticket completion

**What to build:** Ticket completion checks matching reassess-later entries from
the review artifacts, resolves eligible items through the existing workflow and
carries unresolved choices into the next milestone's human evidence review.

**Blocked by:** [28: Guide human review of summaries and proposed merges.](28-guide-human-review-of-summaries-and-proposed-merges.md).

**Status:** ready-for-agent

**Plan version:** [evidence-policy-1](../spec.md); [evidence workflow spec](../evidence-workflow-spec.md).

**Milestone:** EC3.

**Agent context limit:** 250,000 active tokens; [role defaults](../spec.md#role-configuration).

**Worker reasoning:** Inherit Medium for implementation and repair.

**Role guidance:** Shared contract; TDD and test-strategy; applicable development
completion/handoff and skill-writing guidance.

**Context:** Reassessment during ticket completion; single authoritative artifacts;
generated QA views and separate cleanup versus software acceptance.

## Acceptance criteria

- [ ] Record remaining purpose and a context-qualified triggering ticket in temporarily protected entries, within their authoritative ticket/shared JSON artifact rather than a second independent ledger.
- [ ] Generate the reassessment view and have development completion guidance check current-ticket matches after feature development and code/policy integration, before final completion bookkeeping.
- [ ] Reassess matching entries through the existing criteria, fresh review and guarded execution. Trigger matching is a request to reassess and never deletion approval.
- [ ] Preserve evidence that remains unresolved and expose its reason and decision on the next milestone's human QA queue. Handle uncertainty without a usable trigger visibly; do not require an indefinite chain of invented future tickets.
- [ ] Keep unresolved/deferred choices protected across review pause/resume and ticket handoff. Do not confuse a ticket's implementation completion with clearance to delete its evidence or acceptance of its milestone.
- [ ] Show an earlier ticket's retained evidence becoming relevant to a later ticket, one resolved case reaching approved cleanup, and one unresolved case reaching human QA without silent loss or duplicate authoritative decisions.
- [ ] Integrate the development checklist and review skill with existing handoff routes. Leave automatic harness cleanup and frozen-input mutation outside this implementation.

## Verification

Exercise matching/nonmatching ticket identities, shared evidence references,
resolved cleanup, unresolved escalation and resumed human review through public
commands, record outcomes and isolated workflow examples. Validate instruction
routing and required implementation checks. No runtime ticket-completion cleanup
mechanism is implied by adopting the development checklist.

## Shared requirements and handoff

Follow the [scoped evidence contract](../evidence-workflow-spec.md#reassessment-during-ticket-completion), [approved shared verification/ownership contract](../spec.md#shared-implementation-and-verification-contract), and [milestone gates](../milestones.md). Apply the current [AGENTS.md compute routing](../../../AGENTS.md#adapt-compute), [environment](../../../docs/agents/python-environment.md), [testing policy](../../../docs/agents/testing.md) and [development review contract](../../../docs/agents/review-records.md). Map coverage and run required final-source checks; preserve separate fresh Spec/Standards reviews and actual provenance.

Use the [worker handoff](../README.md#worker-handoff). Reconcile acceptance and completion only from verified evidence. Ticket completion and review approval do not accept a milestone. Select the next action through the published milestone gates; do not automatically start later work.
