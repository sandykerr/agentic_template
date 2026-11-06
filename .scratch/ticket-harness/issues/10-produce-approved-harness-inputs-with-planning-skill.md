# 10: Turn one grilling session into an approved plan

**What to build:** Expand the early part of pre-QA ticket 15 into the unified planning skill and shared reference. Resolve QA/milestone decisions during grilling; produce a spec plus focused ticket/milestone proposal; revise them together; publish only after explicit bundle approval. Default to a final QA checkpoint and meaningful earlier ones, honoring an every-N override and worker reasoning overrides.

**Blocked by:** [09: Execute verified dependencies in a stable order](09-execute-dependencies-sequentially.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R01](../ticket-proposal.md#r01-turn-one-grilling-session-into-an-approved-plan).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [custom skills and design policy](../spec.md#custom-skills-and-design-policy).

## Acceptance criteria

- [ ] Provide one user-facing skill that reuses grilling, domain modeling, spec synthesis, and vertical-ticket/dependency principles while leaving upstream skills unchanged.
- [ ] Resolve milestone/QA decisions during grilling; confirm shared understanding, draft a spec and ticket/milestone proposal, and revise both from feedback. Reopen targeted grilling for consequential new decisions.
- [ ] Publish individual tickets, the spec, milestone definitions, and index only after explicit approval of the coherent bundle; leave unapproved proposals unpublished.
- [ ] Always include final QA; propose capability milestones by default, or honor an explicit every-N cadence through fixed dependency-consistent groups and a smaller final group.
- [ ] Record Medium worker/repair and High reviewer defaults, explicit ticket worker overrides, agreed testing seams, QA actions and acceptance conditions in one authoritative planning reference.
- [ ] Validate isolated examples including proposal feedback changing the spec and declined publication. Full runtime/skill-metadata compatibility belongs to ticket 27.

## Verification

Skill validation and isolated planning examples show proposal feedback updating the spec, an unapproved proposal remaining unpublished, and an approved dependency-consistent bundle. Runtime compatibility is completed in ticket 27 rather than claimed early.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R01; the [previous definition](../archive/issues-before-milestone-qa/15-produce-approved-harness-inputs-with-planning-skill.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
