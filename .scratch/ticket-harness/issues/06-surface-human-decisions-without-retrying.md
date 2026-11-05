# 06: Stop for decisions outside approved contracts

**What to build:** A worker or reviewer can surface missing requirements or an incompatible approved-contract change, blocking the affected ticket without speculative implementation or repair churn.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Public interface and approval](../spec.md#public-interface-and-approval); [Agent contracts and access](../spec.md#agent-contracts-and-access); [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts).

**Scope:** The human-decision outcome and handoff within the existing one-ticket cycle.

## Acceptance criteria

- [ ] Recognize a valid human-decision-needed report from implementation or either review axis.
- [ ] Preserve the current work and record the precise unresolved decision, relevant approved contract, and available evidence.
- [ ] Block the affected ticket immediately rather than spending remaining repairs inventing a requirement or changing an approved interface.
- [ ] Do not edit the approved spec, ticket, or project standards or advance integration in response to the decision request.
- [ ] Expose the decision through status and the final report, with attempt counts reflecting only work actually performed.

## Verification

Use scripted ambiguity and contract-conflict scenarios at different roles; assert immediate bounded handoff, unchanged requirements/integration, and accurate counters.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
