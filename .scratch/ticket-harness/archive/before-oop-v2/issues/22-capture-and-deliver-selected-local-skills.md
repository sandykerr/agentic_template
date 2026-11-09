> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](../source-snapshot.json).

# 22: Capture and deliver selected local skills

**What to build:** Retain pre-QA ticket 11's generic role/default/addition contract: explicitly resolve local sources and required references, capture origin/source/content identities, reject missing content, and record actual delivery. Repairs receive captured instructions even after source edits. Keep the planning reference aligned with this canonical metadata.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [21: Supply coherent design guidance to Standards review](21-supply-combined-design-guidance-to-standards-review.md).

**Status:** ready-for-agent

**Milestone:** M3. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R13](../ticket-proposal.md#r13-capture-and-deliver-selected-local-skills).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [skill selection and delivery](../spec.md#skill-selection-and-delivery); [agent contracts and access](../spec.md#agent-contracts-and-access).

## Acceptance criteria

- [ ] Document one canonical additive skill-selection/source-resolution contract compatible with the planning reference and tickets without additions.
- [ ] Support explicit local harness, target-repository, and installed-library sources; role-specific ticket additions preserve project defaults and mandatory role/access/output contracts.
- [ ] At run start capture selected skills and required local references with role, selection origin, source identity and content identity; reject missing required content before affected assignments.
- [ ] Deliver captured instructions explicitly and record actual delivered content; repairs use captured content despite later source edits.
- [ ] Demonstrate defaults, role-specific additions, missing references and edits after capture in a separate scripted target repository; preserve upstream files and defer discovery/download/installation.

## Verification

Scripted cross-repository assignments exercise defaults, role-specific additions, missing references, and source edits after capture without adding live-model variations.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
