# 15: Continue after a deliberate QA stop

**What to build:** Persist a safe QA checkpoint and support clean stop/continuation there. Revalidate approved inputs, branch/candidate identities, and relevant evidence; serialize active ownership and prevent duplicate promotion. Preserve prior Done tickets and do not restart their assignments merely because the orchestrator restarted. Arbitrary mid-stage recovery remains deferred.

**Blocked by:** [14: Consume approval, promote, and continue](14-promote-only-the-human-approved-milestone.md).

**Status:** completed

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R06](../ticket-proposal.md#r06-continue-after-a-deliberate-qa-stop).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [corrections and safe continuation](../spec.md#corrections-and-safe-continuation); [public interface and approval](../spec.md#public-interface-and-approval).

## Acceptance criteria

- [x] Persist a safe planned QA checkpoint that supports deliberate clean stop and continuation by a new orchestrator process.
- [x] Validate captured approved inputs, plan version, branch/candidate identities and relevant evidence before continuation; reject changed or inconsistent state.
- [x] Preserve Done tickets and prior artifacts without replaying completed assignments or consuming a QA decision twice.
- [x] Serialize ownership of the same run and prevent duplicate continuation/promotion; retain diagnosable outcomes for rejected ownership or state.
- [x] Demonstrate stop/restart at the first QA checkpoint, approval consumption, and completion of the next group; explicitly exclude arbitrary mid-stage crash recovery.

## Verification

Stop at the first QA checkpoint, launch a new orchestrator process, consume the decision, and finish the second milestone. Reject changed identities and simultaneous ownership without overwriting evidence.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### Verified completion

Previous readiness: `ready-for-agent`. All five acceptance criteria are verified.
Implementation `36ed3e72c278cf147c84ae9c282cd2899af23ad0`; review repair/final
implementation `d11f0bc60a2c11c40683e58581dffa10e36a91be`; original fixed review
baseline `90255aaf6faf9aedce18f7159093f5dbfde294b7`.

[Completion evidence](../evidence/ticket-15/15-completion.md) maps each criterion to actual
CLI/Git/checkpoint/request/decision/ownership observations. The renewed final suite
passed **544 tests**, with strict mypy, Ruff lint/format, working/staged/committed
whitespace, pinned wheel/isolated install and installed CLI continuation/invalidation.
All 23 final source identities and 123 retained scenarios agree with final source.
Separate fresh High [Spec](../evidence/ticket-15/15-review-spec.md) and
[Standards](../evidence/ticket-15/15-review-standards.md) reviews of the whole implementation
against the original baseline each report **0 blockers and 0 optional suggestions**.
Initial Standards blocker STD15-01 was reproduced and fixed by a fresh Medium repair,
with renewed required gates; initial evidence is retained separately.

No unchecked criteria or unresolved ticket 15 blockers remain. Dependency history
is preserved. M1 work is complete, but M1 human QA has not been requested or accepted.
The next handoff is M1 QA preparation/waiting; ticket 16 and M2 remain ineligible
until recorded human acceptance. Scripted fixture decisions do not accept this
development milestone. No development QA, next ticket or push was launched.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
