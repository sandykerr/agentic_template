# 28: Operate the orchestrator in the background

**What to build:** Add normal CLI background launch returning a run identity, observational status/log access, documented stopping controls, and foreground mode. QA waiting survives closing the launching terminal; the separate QA session writes its artifact. Specify active-stage stopping behavior without claiming unsupported restart recovery.

**Blocked by:** [15: Continue after a deliberate QA stop](15-continue-from-a-planned-qa-checkpoint.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M2. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R10](../ticket-proposal.md#r10-operate-the-orchestrator-in-the-background).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [public interface and approval](../spec.md#public-interface-and-approval); [corrections and safe continuation](../spec.md#corrections-and-safe-continuation).

## Acceptance criteria

- [ ] Provide normal CLI background launch returning a run identity, foreground debugging, observational status/log access, and documented stopping controls.
- [ ] Keep execution and QA waiting independent of the launching terminal; the separate QA session writes the approval artifact.
- [ ] Support clean stop/continuation at QA through ticket 15's contract; document active-stage stop outcomes without claiming arbitrary recovery.
- [ ] Preserve durable process/evidence identity and descendant cleanup; background launch success is distinct from feature completion.
- [ ] Verify launch, logs/status, terminal independence, waiting/approval-driven progress, clean QA stop/restart, and cleanup using offline scripted subprocesses.

## Verification

Scripted subprocess tests observe launch, logs/status, waiting, approval-driven continuation, clean QA stop/restart, and descendant cleanup. Do not require model or network access.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
