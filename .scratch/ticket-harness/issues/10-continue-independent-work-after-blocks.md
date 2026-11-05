# 10: Continue unrelated tickets after a blocked prerequisite

**What to build:** A blocked ticket leaves dependents waiting while unrelated ready tickets finish, and the run ends with an accurate incomplete-work report.

**Blocked by:** [06: Stop for decisions outside approved contracts](06-surface-human-decisions-without-retrying.md); [09: Execute verified dependencies in a stable order](09-execute-dependencies-sequentially.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Ticket lifecycle](../spec.md#ticket-lifecycle); [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** Failure isolation and termination of the existing sequential dependency scheduler.

## Acceptance criteria

- [ ] Keep a ticket requiring a human decision or exhausting repairs Blocked; keep its dependent tickets Pending rather than runnable.
- [ ] Continue unrelated ready tickets from the latest verified integration revision without retrying the blocked ticket implicitly.
- [ ] Stop when no executable work remains and distinguish Done, Blocked, and Pending tickets in status and the final report.
- [ ] Return a nonzero incomplete outcome when selected work remains unresolved, even if unrelated tickets succeeded.
- [ ] A shared environment failure stops the run instead of repeatedly failing every remaining ticket.
- [ ] Demonstrate one blocked root, one waiting dependent, and one unrelated successful ticket in the same fixture run.

## Verification

Exercise exhausted-repair and human-decision fixtures through a real multi-ticket run; inspect branch history, launched assignments, waiting states, and the final outcome.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
