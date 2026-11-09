# Historical ticket definition

Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 12; use the [current ticket](../../issues/32-deliver-focused-implementation-and-spec-review-contexts.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/12-deliver-focused-implementation-and-spec-review-contexts.md`. Relative links were adjusted for this archive location.

# 12: Deliver focused implementation and Spec-review skills

**What to build:** Implementation, repair, and Spec-review assignments receive distinct repo-owned guidance, applicable project-default and ticket-added skills, and bounded requirements, code pointers, and evidence relevant to their roles.

**Blocked by:** [11: Supply combined Python design guidance to Standards review](11-supply-combined-design-guidance-to-standards-review.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../../README.md#agent-context-policy).

**Context:** [Agent contracts and access](../spec-before-milestone-qa.md#agent-contracts-and-access); [Custom skills and design policy](../spec-before-milestone-qa.md#custom-skills-and-design-policy); [Skill selection and delivery](../spec-before-milestone-qa.md#skill-selection-and-delivery); [Codex execution](../spec-before-milestone-qa.md#codex-execution).

**Scope:** The custom implementation and Spec-review roles and their context assembly, reusing issue 11's selection/capture/delivery contract, shared design policy, and Standards role. Adapt reusable guidance from existing custom skills while preserving the harness's ownership of checks, review orchestration, commits/integration, execution records, and completion.

## Acceptance criteria

- [ ] Create an implementation skill that follows one ticket's approved contracts, uses agreed behavioral test seams, reports evidence, and surfaces decisions outside scope; reuse custom test strategy to assess existing coverage before TDD for missing behavior, preserving configured verification gates.
- [ ] Create a Spec-review skill focused on missing, incorrect, and unrequested behavior against the approved spec and ticket.
- [ ] Give every implementation, repair, and review assignment fresh context with required role instructions, captured project defaults, applicable ticket additions, and scoped references. Reuse the run's captured content for repairs even if source skills change.
- [ ] Supply implementation-relevant design constraints without copying every upstream skill or unrelated ticket into its prompt.
- [ ] Supply Spec review with the exact reviewed revision, approved acceptance requirements, relevant source/diff, and actual check results.
- [ ] Keep development-wrapper bookkeeping, nested-review orchestration, and next-agent handoff authority outside runtime worker instructions; any adapted practices preserve harness role/access/output contracts.
- [ ] Record the selected role skills, their selection origins, and the source/content identities actually supplied to each assignment; demonstrate role-appropriate defaults and ticket additions across a separate target repository, including a fresh repair assignment.

## Verification

Use skill-authoring checks and public scripted-agent runs that capture each role's inputs and produce schema-valid results; verify role separation, additive selection, stable captured guidance across repair, and preserved harness authority through observable assignment contents and outcomes. Reuse issue 11's common selection/capture coverage and add only distinct role or repair behavior.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../../README.md#worker-handoff).
