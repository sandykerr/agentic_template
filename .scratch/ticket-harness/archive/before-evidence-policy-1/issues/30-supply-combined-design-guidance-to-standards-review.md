# 30: Supply coherent design guidance to Standards review

**What to build:** Retain the design-policy and Standards-role portion of pre-QA ticket 11, auditing current custom guidance and synthesizing Matt/Microsoft principles with Pythonic functions and objects. Deliver the required policy/role context explicitly through the existing assignment seam. Evidence-based blockers remain distinct from optional suggestions.

**Blocked by:** [03: Reject invalid agent reports and review evidence](03-validate-agent-reports-and-review-evidence.md); [19: Evaluate reviewers on known and acceptable designs](19-evaluate-reviewers-on-known-and-acceptable-designs.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M3. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R12](../ticket-proposal.md#r12-supply-coherent-design-guidance-to-standards-review).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [custom skills and design policy](../spec.md#custom-skills-and-design-policy); [cohesive module responsibilities](../spec.md#cohesive-module-responsibilities).

**Review amendment:** Inherit [review records](../spec.md#review-work-findings-and-decisions), [runtime adoption](../spec.md#runtime-review-adoption) and [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints).

## Acceptance criteria

- [ ] Audit current custom guidance and create one combined design authority with focused references for deep modules, information hiding, cohesive responsibility/invariant ownership, composition, substitutability, justified injection, and behavioral tests.
- [ ] Support Pythonic functions, objects and combinations without mandating speculative patterns or class hierarchies.
- [ ] Create Standards guidance respecting project rules and accepted ADRs; blockers need concrete evidence and consequences, while preferences remain optional.
- [ ] Reuse custom test-strategy review guidance without adding a reviewer or gate, and explicitly supply required design/Standards context through the existing assignment seam.
- [ ] Validate skills and concrete design examples; capture Standards inputs in a separate scripted repository. Generic default/addition capture and source-edit stability are owned by ticket 31.

- [ ] Explicitly deliver the evaluated ownership/cross-module review contract and its scope/coverage declaration through the existing Standards assignment seam. Capture actual scripted delivered instruction identities; cumulative runtime scheduling remains ticket 33.

## Verification

Validate skills, inspect concrete design examples, and capture actual Standards-assignment inputs in a separate scripted target repository. Generic additive skill selection is isolated in ticket 31.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R12; the [previous definition](../archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
