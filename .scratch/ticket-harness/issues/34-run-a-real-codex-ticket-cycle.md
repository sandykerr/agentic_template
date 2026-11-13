# 34: Complete the workflow with real Codex roles

**What to build:** Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Blocked by:** [15: Continue after a deliberate QA stop](15-continue-from-a-planned-qa-checkpoint.md); [32: Deliver focused implementation and Spec contexts](32-deliver-focused-implementation-and-spec-review-contexts.md); [08: Stop stalled assignments and check processes](08-stop-timed-out-process-trees.md); [33: Enforce traceable runtime review checkpoints](33-enforce-traceable-runtime-review-checkpoints.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M3. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R15](../ticket-proposal.md#r15-complete-the-workflow-with-real-codex-roles).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](../spec.md#codex-execution); [skill selection and delivery](../spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](../spec.md#review-work-findings-and-decisions), [runtime adoption](../spec.md#runtime-review-adoption) and [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints).

## Acceptance criteria

- [ ] Verify installed Codex invocation and launch fresh implementation/repair/review processes with explicit working directory, sandbox, positive timeout, model, and output contract; do not silently substitute models.
- [ ] Apply Medium implementation/repair and High Spec/Standards defaults with independently configurable role profiles; validate ticket worker overrides and inherit them in repairs without changing reviewers.
- [ ] Capture machine-readable events and schema-validated reports with actual model/reasoning settings and supplied instruction identities.
- [ ] Demonstrate cross-repository delivery of required custom role/design guidance, project defaults and a role-specific addition, without assuming automatic discovery.
- [ ] Complete a tiny actual implementation plus two independent actual reviews and exact candidate integration within the established milestone workflow; keep human QA approval separate from model results.
- [ ] Retain scripted offline routine checks and a separate explicit live check. Record actual evidence or a concrete blocker; a skipped live check is not completion.

- [ ] Use ticket 33's enforced review lifecycle with actual real-agent assignments, including an explicitly scoped cumulative assessment and a declared seeded concern plus acceptable control. Retain actual delivered guidance, inspected scope, findings/dispositions and exact readiness/QA outcomes; scripted success or M1 development evaluation cannot substitute for live runtime proof.

## Verification

Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R15; the [previous definition](../archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

### Related development-workflow evidence

The completed [workflow-efficiency follow-up](../archive/workflow-efficiency/README.md)
retains original development-instruction reviews and a finite preparation
exercise. It supplies background for the current
[development procedure](../../../docs/agents/review-records.md#prepare-review-and-repair), not live
runtime proof or measured cost savings. This ticket still requires its own actual
role-delivery and runtime evidence under the existing acceptance criteria; no
additional calibration campaign or dependency is introduced by this archive.
