# 11: Stop development handoffs at human checkpoints

**What to build:** Update the two development wrappers to distinguish ticket completion from milestone/feature acceptance, preserve checkbox/status evidence, and respect Medium/High defaults and ticket worker overrides. An eligible next ticket receives an implementation handoff; a QA boundary receives a QA handoff or explicit waiting status. No handoff launches work or invents an approval.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md).

**Status:** completed

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R02](../ticket-proposal.md#r02-stop-development-handoffs-at-human-checkpoints).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [agent contracts and access](../spec.md#agent-contracts-and-access).

## Acceptance criteria

- [x] Preserve evidence-backed checkbox/status reconciliation, checkpoint-before-review, separate fresh reviews, and implementation/bookkeeping/handoff commits in the existing development workflow.
- [x] Select handoffs using the earliest eligible milestone and genuine prerequisites; an old lower-numbered ticket cannot bypass the QA-first order.
- [x] Produce an implementation handoff for eligible work and a QA handoff or explicit waiting status at a checkpoint; all tickets Done without final acceptance is not feature completion.
- [x] Carry Medium worker/repair defaults, ticket overrides, High reviewer defaults, and exact QA request/candidate/artifact references when available without inventing approvals.
- [x] Reuse testing policy for focused development checks and required completion checks; keep runtime orchestration, promotion, and approval authority outside worker guidance.
- [x] Demonstrate isolated normal-next-ticket, waiting-milestone, and awaiting-final-QA handoffs. Generating a prompt does not launch work.

## Verification

Isolated handoff examples cover a normal next ticket, a waiting milestone, and final tickets complete but final QA unaccepted. Preserve existing development gates and active-input immutability.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.


## Comments

Completed with implementation `552fcd6b87909b96ac7bcd6a878d0db6bbbd2869`, reviewed against original baseline `5af3b343ad962b05ce44e359b791b65a8865f05a`. Previous readiness: `ready-for-agent`. All six criteria are verified in the [criterion-specific completion evidence](../evidence/11-completion.md), with [actual commands/exits](../evidence/11-checks.log), [static checks](../evidence/11-static/) and [raw isolated handoff observations](../evidence/11-handoff-observations.json).

Both official skill validators, 19 source links/anchors, whitespace/upstream/reference checks, and three actual isolated handoffs passed. Normal output selects preferred M1 work despite lower IDs; waiting output preserves exact existing QA references and holds M2; final output reports awaiting final QA with missing references explicit. Protected inputs and HEADs are unchanged; generation launches no work. Synthetic fixture reviews do not substitute for implementation review.

Separate fresh GPT-6.1 Sol High [Spec](../evidence/11-review-spec.md) and [Standards](../evidence/11-review-standards.md) reviews assessed `552fcd6` against the original baseline: each found zero blockers and zero optional suggestions. No source repair was needed. The standalone skill/document policy applies; no runtime suite replay or new testing seam was required. Upstream/shared planning guidance and the unrelated tracker edit are preserved.

Acceptance wording and declared dependencies are unchanged. Implementation, this bookkeeping, and the next handoff use separate commits. No unchecked criteria or unresolved ticket-11 items remain. Completion does not accept M1 or the feature: prerequisite-ready ticket 12 is next in M1; M2 still waits for recorded human acceptance at the M1 boundary. No runtime QA, promotion, next-ticket launch or push occurred.
