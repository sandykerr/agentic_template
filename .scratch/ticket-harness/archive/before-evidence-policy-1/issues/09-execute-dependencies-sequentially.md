# 09: Execute verified dependencies in a stable order

**What to build:** A successful multi-ticket run processes one ready ticket at a time and starts dependents only after prerequisite changes are integrated and verified.

**Blocked by:** [02: Reject invalid requirements before starting work](02-reject-invalid-inputs-before-execution.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Ticket lifecycle](../spec.md#ticket-lifecycle); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions).

**Scope:** Extend the existing single-ticket run to a validated dependency graph; retain sequential execution.

## Acceptance criteria

- [x] Select ready agent-eligible tickets with a documented stable ordering and at most one active implementation ticket.
- [x] Run the broader starting baseline once for the run, while retaining per-ticket lightweight checks and per-candidate broader checks.
- [x] Base each new implementation worktree on the current verified integration revision.
- [x] Unlock a dependent only when all prerequisites are Done in this run's integration state.
- [x] Report the observed state and integrated revision of every selected ticket and return success only when all selected work is Done.
- [x] Demonstrate a dependency chain and independent ready tickets using scripted agents and real Git repositories.

## Verification

Run fixture graphs through the public CLI and inspect the source revisions delivered to workers, verified integration history, final states, and exit result.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

Implemented in `7f4eac0` against fixed original baseline `be2244f`. All six original criteria are verified in the [criterion-specific completion evidence](../evidence/ticket-09/09-completion.md) and [21 saved final-suite CLI/Git scenarios plus installed graph (compact historical results)](../evidence/ticket-09/09-scenario-results.json).

The explicit `selected_tickets` contract preserves `tickets` as context. Successful graphs execute the lowest numeric ready ID sequentially from the latest verified integration tip, run one shared baseline and all per-ticket/exact-candidate gates, and unlock dependents only after promotion and Done. Durable run/status expose every selected state/revision with ticket-local repairs and collision-free retained evidence. Multi-ticket and legacy external completion evidence remain validated. This slice stops at the first blocked ticket; continuation belongs to ticket 10.

Checks: **469 passed in 370.27s**, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI graph/status all exited 0 at the committed source. [Actual command output (retirement summary)](../evidence/ticket-09/README.md#retired-evidence) preserves source hashes and results. Separate fresh independent **Spec and Standards reviews passed with zero blockers or optional suggestions**; Spec independently passed three focused cases. No implementation changes followed review.

Previous readiness was `ready-for-agent`; the header now records terminal verified completion. The declared dependency remains history. Approved inputs were unchanged during fixture runs, and no active harness run using these feature files was found before bookkeeping. All six markers, header, comment and feature index agree; no unchecked criteria or unresolved required items remain. No push was performed. The generated next-agent prompt is committed separately after this bookkeeping; it does not start another ticket.
