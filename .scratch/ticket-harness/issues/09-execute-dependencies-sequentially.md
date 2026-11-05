# 09: Execute verified dependencies in a stable order

**What to build:** A successful multi-ticket run processes one ready ticket at a time and starts dependents only after prerequisite changes are integrated and verified.

**Blocked by:** [02: Reject invalid requirements before starting work](02-reject-invalid-inputs-before-execution.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Ticket lifecycle](../spec.md#ticket-lifecycle); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

**Scope:** Extend the existing single-ticket run to a validated dependency graph; retain sequential execution.

## Acceptance criteria

- [ ] Select ready agent-eligible tickets with a documented stable ordering and at most one active implementation ticket.
- [ ] Run the broader starting baseline once for the run, while retaining per-ticket lightweight checks and per-candidate broader checks.
- [ ] Base each new implementation worktree on the current verified integration revision.
- [ ] Unlock a dependent only when all prerequisites are Done in this run's integration state.
- [ ] Report the observed state and integrated revision of every selected ticket and return success only when all selected work is Done.
- [ ] Demonstrate a dependency chain and independent ready tickets using scripted agents and real Git repositories.

## Verification

Run fixture graphs through the public CLI and inspect the source revisions delivered to workers, verified integration history, final states, and exit result.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
