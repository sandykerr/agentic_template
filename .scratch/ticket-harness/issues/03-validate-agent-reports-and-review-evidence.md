# 03: Reject invalid agent reports and review evidence

**What to build:** An assignment can satisfy a verification gate only with a complete, correctly identified report for the current ticket, attempt, role, and source revision.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Agent contracts and access](../spec.md#agent-contracts-and-access); [Custom skills and design policy](../spec.md#custom-skills-and-design-policy).

**Scope:** Strengthen the existing assignment/report seam for implementation and both review axes; report validation alone does not introduce automatic repair.

## Acceptance criteria

- [ ] Validate implementation results, including submitted versus human-decision-needed outcomes, against the documented assignment identity and required evidence fields.
- [ ] Validate each review's axis, ticket, attempt, base/revision identity, and findings; require blocker consequence/evidence and optional-versus-blocking classification.
- [ ] Accept an empty findings list only in a complete review for the correct assignment and revision.
- [ ] Reject missing, malformed, incomplete, stale, or mismatched reports even when the process exits zero; reject nonzero process exits even when a report claims success.
- [ ] Derive authoritative source changes and revisions from Git rather than report claims, and never accept an agent's declaration that a ticket is Done.
- [ ] Keep invalid outcomes and their available artifacts visible through run/status without advancing integration.

## Verification

Exercise the CLI with scripted processes that return valid, malformed, missing, nonzero-exit, and wrong-revision outcomes; assert gate behavior and durable diagnostics.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
