# 18: Gate development on cumulative architecture review

**What to build:** Require source-identified cumulative architecture assessments at development milestone boundaries and earlier risk triggers. Make the existing tracker/handoff workflow surface these assessments and human finding dispositions before implementation is integrated or a milestone is presented as ready for QA.

**Blocked by:** [16: Record review work, findings and decisions](16-record-review-work-findings-and-decisions.md); [17: Review ownership across affected modules](17-review-ownership-across-affected-modules.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md), approved review-process-1 revision.

**Milestone:** M1. Follow [membership and human QA](../milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](../spec.md#role-configuration), [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](../spec.md#review-work-findings-and-decisions); [ownership and review scope](../spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](../spec.md#reviewer-evaluation); [verification](../spec.md#review-process-verification); [role defaults](../spec.md#role-configuration). Respect [domain terms](../../../GLOSSARY.md), [ADR-0001](../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

## Acceptance criteria

- [ ] Create a cumulative review work item before each required development milestone QA request. Pin its cumulative baseline to the last accepted milestone (or feature starting revision for the first), assessed source, complete scope inventory and unresolved prior findings. Review all ticket_harness Python files for this small package; larger targets document the complete affected workflow and collaborators.
- [ ] At ticket start and after implementation, assess whether the ticket introduces a new lifecycle, persistence/restoration path, shared mutable state or an additional writer. Such a trigger requires a broader architecture assessment before that ticket integrates, covering the affected workflow rather than only its diff. Missing/incomplete assessment remains visible and prevents readiness; avoid a third unconditional reviewer on every ticket.
- [ ] Use a fresh High Standards assignment for cumulative architecture scope, with the existing Spec/Standards contract and review-record history. Examine ownership and the concrete edits needed for a plausible change, such as another review stage or repair-policy adjustment. An existing audit may satisfy the checkpoint only when its source identity, coverage and retained dispositions actually match.
- [ ] Record each finding as fixed with verification, deferred with a linked ticket, accepted with a reason, or awaiting a human decision; keep open observations visible. In-scope blockers prevent affected integration and milestone readiness. Deferral/acceptance of significant risk needs an explicit human decision and applicable approved amendment, never an agent relabeling or a completed-review status alone.
- [ ] Update milestone/handoff guidance to distinguish assessment completed, findings resolved/dispositioned, candidate ready for human QA and milestone accepted. A clean assessment proceeds autonomously within approved work; it does not generate a human approval request for every comment or replace exact-candidate QA. Changed assessed source requires renewed relevant review before the old assessment can authorize readiness.
- [ ] Demonstrate multiple individually passing tickets accumulating a cross-module ownership problem, a risk-triggered review before integration, stale-source review rejection, a clean checkpoint, blocked progression, human disposition and a handoff preserving deferred work. Archive and reuse report evidence without rewriting old decisions or active-run snapshots.

## Verification

Use isolated planning/implementation/handoff examples and actual cumulative review artifacts, with the fixed source inventory and observed readiness outcomes. Development checkpoint enforcement is in repo-owned guidance and tracker/handoff records; automated runtime execution of the same rules is ticket 33. Skill/document validations and reproducible workflow observations complement the normal implementation reviews.

Use the [testing policy](../../../docs/agents/testing.md), [Python environment](../../../docs/agents/python-environment.md) and [shared review-process verification](../spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](../milestones.md); no automatic next-milestone execution or human acceptance is authorized.
