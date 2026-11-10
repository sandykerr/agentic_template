# 17: Review ownership across affected modules

**What to build:** Require explicit ownership contracts during planning and evidence-based Spec/Standards assessment across the affected workflow. Extend repo-owned planning, implementation, review and handoff guidance so a ticket is assessed with relevant callers, writers and persistence consumers, while preserving independent review axes and scope authority.

**Blocked by:** [16: Record review work, findings and decisions](16-record-review-work-findings-and-decisions.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md), approved review-process-1 revision.

**Milestone:** M1. Follow [membership and human QA](../milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](../spec.md#role-configuration), [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](../spec.md#review-work-findings-and-decisions); [ownership and review scope](../spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](../spec.md#reviewer-evaluation); [verification](../spec.md#review-process-verification); [role defaults](../spec.md#role-configuration). Respect [domain terms](../../../GLOSSARY.md), [ADR-0001](../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

## Acceptance criteria

- [x] For consequential mutable state, planning records the owner, permitted writers, operations preserving invariants, persistence/restoration rules and failure behavior. Workers record the ownership change or explain why existing ownership is unchanged; a missing consequential ownership decision is surfaced for the human rather than invented during implementation.
- [x] Keep the original-baseline whole-ticket review and separate fresh Spec/Standards assignments. Standards follows affected state and responsibilities through relevant unchanged callers, consumers, other writers and save/restore/invalidation paths; Spec checks approved ownership/behavior contracts as well as acceptance requirements. Reviewer scope is not limited to diff hunks or a universal short-report cap.
- [x] Each report states assessed source/baseline, inspected files/flows, explicitly omitted scope and unresolved assumptions. Findings cite the code/contract, concrete consequence, evidence and proportionate remedy; code length or a preference for classes is insufficient. An empty findings list is meaningful only for the recorded inspected scope.
- [x] Carry prior findings and append-only dispositions from ticket 16 into scoped review/repair context, and verify claimed fixes against the repaired revision. Preserve report independence before aggregation; separate evidence/provenance auditing from substantive reasoning so successful hashes or tests cannot substitute for design assessment.
- [x] Update existing development wrappers and next-agent handoffs to apply the shared contract and expose unresolved review work. Preserve upstream skills, required checks, fresh role settings, bounded authorized repairs, optional suggestions and milestone gates. Any concrete breach or correction stays within existing authorization or is surfaced as a human decision.
- [x] Demonstrate an unchanged caller hiding a second state writer, a restoration/invalidation path outside the diff, a documented ownership breach versus an optional design suggestion, and a justified clean review of a long cohesive function. Retain actual scoped assignment/report artifacts and evidence of independence, rather than asserting compliance from added skill links.

## Verification

Validate guidance/links and run isolated development-review walkthroughs against representative source/diffs and explicit ownership contracts. Record actual reviewer assignments/reports; reuse current review and architecture guidance without requiring every review to render HTML. Broad calibration and its acceptance corpus are delivered in ticket 19; this ticket proves the usable review workflow and scope contract.

Use the [testing policy](../../../docs/agents/testing.md), [Python environment](../../../docs/agents/python-environment.md) and [shared review-process verification](../spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](../milestones.md); no automatic next-milestone execution or human acceptance is authorized.

## Comments

### Verified completion

Previous readiness: `ready-for-agent`. Implementation `4814eabd4bf2f196f7fb6915667c4305b7c2d0b9`,
reviewed from fixed baseline `c82b15f504c29a69e8fb708e10568574150e80d3`.
All six criteria are verified in [criterion evidence](../evidence/17-completion.md),
with [actual passing checks](../evidence/17-checks.log) and the
[real assessment](../reviews/ticket-17.md). Separate fresh High
[Spec](../evidence/17-review-spec.md) and [Standards](../evidence/17-review-standards.md)
each found zero blocking or optional findings. No unchecked criteria or unresolved
actual findings/decisions remain. Representative fixture concerns retain their
original scope; failed D and exact D2 verification are preserved. Bookkeeping is
committed separately, followed by the next handoff. M1 remains unaccepted;
ticket 18 is next only through current milestone/prerequisite eligibility.
