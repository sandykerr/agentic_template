# 37: Run a generated approved plan through the runtime

**What to build:** Complete the remaining integration portion of pre-QA ticket 15. Produce a small plan through the unified skill, validate it against the now-implemented milestone/skill contracts, and execute it through the scripted public seam. Demonstrate project-default guidance and a role-specific ticket addition, preserving required contracts.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md); [27: Execute approved QA corrections](27-execute-approved-qa-corrections.md); [31: Capture and deliver selected local skills](31-capture-and-deliver-selected-local-skills.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M4. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R18](../ticket-proposal.md#r18-run-a-generated-approved-plan-through-the-runtime).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [skill selection and delivery](../spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](../spec.md#review-work-findings-and-decisions), [runtime adoption](../spec.md#runtime-review-adoption) and [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints).

## Acceptance criteria

- [ ] Generate a small human-approved spec/ticket/milestone bundle through the unified planning skill and validate it against the implemented canonical contracts.
- [ ] Demonstrate explicit project defaults and an applicable role-specific ticket addition, plus a ticket requiring no additions, preserving mandatory role guidance.
- [ ] Run the approved example through intentional scripted CLI execution, reaching planned QA and exact local promotion with captured/delivered instruction identities.
- [ ] Keep publishing distinct from execution and QA planning distinct from acceptance; preserve original inputs and evidence.
- [ ] Include interfaces, invariants, testing seams, Pythonic shared design, and appropriate test strategy without replaying all selection validation already covered by ticket 31.

- [ ] Run a generated approved plan carrying ownership/review metadata and required checkpoint scope, verifying backward-compatible tickets without additions and exact linkage of review history to implementation and milestone evidence.

## Verification

A generated example reaches QA and promotion with recorded selection/content identities. Planning publication does not itself launch execution; the example uses an explicit run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
