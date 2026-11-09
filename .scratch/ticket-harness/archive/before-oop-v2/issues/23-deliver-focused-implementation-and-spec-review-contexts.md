> Historical approved-plan snapshot from `152b0c4577269789a419079c6261c69f9a0695fd`. Use the [current feature index](../../../README.md) for new work. Original identities and requirement text are retained; relative links are relocated for this archive. Exact pre-publication bytes are preserved in the [source snapshot](../source-snapshot.json).

# 23: Deliver focused implementation and Spec contexts

**What to build:** Retain pre-QA ticket 12's distinct implementation/repair/Spec guidance and fresh context assembly. Supply milestone and ticket constraints while keeping reviews, commits, promotions, state changes, and human approval under harness control. Reuse shared design and test strategy without copying the whole upstream library.

**Blocked by:** [22: Capture and deliver selected local skills](22-capture-and-deliver-selected-local-skills.md).

**Status:** ready-for-agent

**Milestone:** M3. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R14](../ticket-proposal.md#r14-deliver-focused-implementation-and-spec-contexts).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [agent contracts and access](../spec.md#agent-contracts-and-access); [skill selection and delivery](../spec.md#skill-selection-and-delivery).

## Acceptance criteria

- [ ] Create focused implementation/repair guidance for one ticket's contracts, approved behavioral seams, custom test-strategy coverage selection, TDD where needed, evidence, and out-of-scope decisions.
- [ ] Create separate Spec-review guidance for missing, incorrect and unrequested behavior against approved requirements.
- [ ] Provide every assignment fresh role context, captured defaults/additions and scoped references; repairs use the captured version even after source-library edits.
- [ ] Supply exact reviewed revision, relevant source/diff and actual check outcomes to Spec review, with only relevant design guidance for implementers.
- [ ] Keep nested-review orchestration, commits, integration, QA acceptance, state and completion under harness authority; record actual selection origins/content identities and demonstrate a fresh repair.

## Verification

Captured scripted implementation, repair, and Spec assignments show scoped requirements, exact reviewed revisions, stable selected guidance, and role separation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R14; the [previous definition](../../issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
