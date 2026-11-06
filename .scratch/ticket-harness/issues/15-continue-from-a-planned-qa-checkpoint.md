# 15: Continue after a deliberate QA stop

**What to build:** Persist a safe QA checkpoint and support clean stop/continuation there. Revalidate approved inputs, branch/candidate identities, and relevant evidence; serialize active ownership and prevent duplicate promotion. Preserve prior Done tickets and do not restart their assignments merely because the orchestrator restarted. Arbitrary mid-stage recovery remains deferred.

**Blocked by:** [14: Consume approval, promote, and continue](14-promote-only-the-human-approved-milestone.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R06](../ticket-proposal.md#r06-continue-after-a-deliberate-qa-stop).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [corrections and safe continuation](../spec.md#corrections-and-safe-continuation); [public interface and approval](../spec.md#public-interface-and-approval).

## Acceptance criteria

- [ ] Persist a safe planned QA checkpoint that supports deliberate clean stop and continuation by a new orchestrator process.
- [ ] Validate captured approved inputs, plan version, branch/candidate identities and relevant evidence before continuation; reject changed or inconsistent state.
- [ ] Preserve Done tickets and prior artifacts without replaying completed assignments or consuming a QA decision twice.
- [ ] Serialize ownership of the same run and prevent duplicate continuation/promotion; retain diagnosable outcomes for rejected ownership or state.
- [ ] Demonstrate stop/restart at the first QA checkpoint, approval consumption, and completion of the next group; explicitly exclude arbitrary mid-stage crash recovery.

## Verification

Stop at the first QA checkpoint, launch a new orchestrator process, consume the decision, and finish the second milestone. Reject changed identities and simultaneous ownership without overwriting evidence.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
