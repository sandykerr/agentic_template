# 11: Stop development handoffs at human checkpoints

**What to build:** Update the two development wrappers to distinguish ticket completion from milestone/feature acceptance, preserve checkbox/status evidence, and respect Medium/High defaults and ticket worker overrides. An eligible next ticket receives an implementation handoff; a QA boundary receives a QA handoff or explicit waiting status. No handoff launches work or invents an approval.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R02](../ticket-proposal.md#r02-stop-development-handoffs-at-human-checkpoints).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [agent contracts and access](../spec.md#agent-contracts-and-access).

## Acceptance criteria

- [ ] Preserve evidence-backed checkbox/status reconciliation, checkpoint-before-review, separate fresh reviews, and implementation/bookkeeping/handoff commits in the existing development workflow.
- [ ] Select handoffs using the earliest eligible milestone and genuine prerequisites; an old lower-numbered ticket cannot bypass the QA-first order.
- [ ] Produce an implementation handoff for eligible work and a QA handoff or explicit waiting status at a checkpoint; all tickets Done without final acceptance is not feature completion.
- [ ] Carry Medium worker/repair defaults, ticket overrides, High reviewer defaults, and exact QA request/candidate/artifact references when available without inventing approvals.
- [ ] Reuse testing policy for focused development checks and required completion checks; keep runtime orchestration, promotion, and approval authority outside worker guidance.
- [ ] Demonstrate isolated normal-next-ticket, waiting-milestone, and awaiting-final-QA handoffs. Generating a prompt does not launch work.

## Verification

Isolated handoff examples cover a normal next ticket, a waiting milestone, and final tickets complete but final QA unaccepted. Preserve existing development gates and active-input immutability.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
