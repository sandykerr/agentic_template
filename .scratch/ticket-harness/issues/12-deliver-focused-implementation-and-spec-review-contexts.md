# 12: Deliver focused implementation and Spec-review skills

**What to build:** Implementation and Spec-review assignments receive distinct repo-owned skills and the bounded requirements, code pointers, and evidence relevant to their roles.

**Blocked by:** [11: Supply combined Python design guidance to Standards review](11-supply-combined-design-guidance-to-standards-review.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Agent contracts and access](../spec.md#agent-contracts-and-access); [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Codex execution](../spec.md#codex-execution).

**Scope:** The custom implementation and Spec-review roles and their context assembly, reusing the existing shared design policy and Standards role.

## Acceptance criteria

- [ ] Create an implementation skill that follows one ticket's approved contracts, uses agreed behavioral test seams, reports evidence, and surfaces decisions outside scope.
- [ ] Create a Spec-review skill focused on missing, incorrect, and unrequested behavior against the approved spec and ticket.
- [ ] Give every implementation, repair, and review assignment fresh context with role-specific instructions and scoped references.
- [ ] Supply implementation-relevant design constraints without copying every upstream skill or unrelated ticket into its prompt.
- [ ] Supply Spec review with the exact reviewed revision, approved acceptance requirements, relevant source/diff, and actual check results.
- [ ] Record the role-skill and reference identities supplied to each assignment and demonstrate their availability across a separate target repository.

## Verification

Use skill-authoring checks and public scripted-agent runs that capture each role's inputs and produce schema-valid results; verify role separation through observable assignment contents and outcomes.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
