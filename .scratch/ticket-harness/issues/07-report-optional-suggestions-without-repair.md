# 07: Report optional review suggestions without rework

**What to build:** A ticket with passing gates and optional review suggestions integrates normally, while the suggestions remain available in the final report.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Agent contracts and access](../spec.md#agent-contracts-and-access); [Ticket lifecycle](../spec.md#ticket-lifecycle).

**Scope:** The optional-finding path across report validation, repair decisions, and status/final output.

## Acceptance criteria

- [ ] Treat valid optional findings from either review axis as non-blocking while retaining their evidence and source-revision identity.
- [ ] Do not launch a repair or consume its allowance solely for optional suggestions.
- [ ] Integrate a passing ticket with optional suggestions and expose those suggestions in the recorded and human-readable result.
- [ ] When blockers and suggestions coexist, send blockers into repair and retain suggestions without converting preferences into requirements.
- [ ] Preserve which findings belong to which reviewed revision when later repairs occur.

## Verification

Drive optional-only and mixed-finding fixtures through the CLI; inspect agent launches, attempt counts, integration success, and report contents.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
