> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](../source-snapshot.json).

# 16: Guide a human through milestone QA

**What to build:** Create the QA-session skill for existing requests. Guide the planned checks, record observed results, and write the exact artifact only after explicit human acceptance. A request to self-approve from passing tests does not authorize acceptance. Findings remain visible and no product code or integration ref is changed by this skill.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [14: Consume approval, promote, and continue](../../../issues/14-promote-only-the-human-approved-milestone.md).

**Status:** ready-for-agent

**Milestone:** M2. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R07](../ticket-proposal.md#r07-guide-a-human-through-milestone-qa).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [feature to development promotion and human qa](../spec.md#feature-to-development-promotion-and-human-qa).

## Acceptance criteria

- [ ] Create a focused QA-session skill that reads the exact request/candidate and guides the human through planned checks, evidence inspection, and observable acceptance conditions.
- [ ] Record findings and withhold acceptance until the human explicitly approves; passing automated tests or an agent recommendation is insufficient.
- [ ] Write only the precise decision artifact for matching current identities, preserving provenance and rejecting stale requests.
- [ ] Do not implement corrections or change product source/integration refs; propose findings for the versioned planning workflow.
- [ ] Validate isolated explicit-approval, withheld-approval, stale-request, and self-approval-request examples without altering actual user work.

## Verification

Skill validation and isolated QA examples cover explicit approval, withheld approval, and stale candidate identities using disposable artifacts.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
