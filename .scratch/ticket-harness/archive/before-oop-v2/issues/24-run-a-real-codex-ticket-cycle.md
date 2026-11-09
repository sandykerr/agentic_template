> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](../source-snapshot.json).

# 24: Complete the workflow with real Codex roles

**What to build:** Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Blocked by:** [15: Continue after a deliberate QA stop](../../../issues/15-continue-from-a-planned-qa-checkpoint.md); [23: Deliver focused implementation and Spec contexts](23-deliver-focused-implementation-and-spec-review-contexts.md); [08: Stop stalled assignments and check processes](../../../issues/08-stop-timed-out-process-trees.md).

**Status:** ready-for-agent

**Milestone:** M3. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R15](../ticket-proposal.md#r15-complete-the-workflow-with-real-codex-roles).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [codex execution](../spec.md#codex-execution); [skill selection and delivery](../spec.md#skill-selection-and-delivery).

## Acceptance criteria

- [ ] Verify installed Codex invocation and launch fresh implementation/repair/review processes with explicit working directory, sandbox, positive timeout, model, and output contract; do not silently substitute models.
- [ ] Apply Medium implementation/repair and High Spec/Standards defaults with independently configurable role profiles; validate ticket worker overrides and inherit them in repairs without changing reviewers.
- [ ] Capture machine-readable events and schema-validated reports with actual model/reasoning settings and supplied instruction identities.
- [ ] Demonstrate cross-repository delivery of required custom role/design guidance, project defaults and a role-specific addition, without assuming automatic discovery.
- [ ] Complete a tiny actual implementation plus two independent actual reviews and exact candidate integration within the established milestone workflow; keep human QA approval separate from model results.
- [ ] Retain scripted offline routine checks and a separate explicit live check. Record actual evidence or a concrete blocker; a skipped live check is not completion.

## Verification

Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R15; the [previous definition](../../issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
