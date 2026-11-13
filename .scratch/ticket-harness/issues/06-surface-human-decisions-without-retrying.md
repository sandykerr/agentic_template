# 06: Stop for decisions outside approved contracts

**What to build:** A worker or reviewer can surface missing requirements or an incompatible approved-contract change, blocking the affected ticket without speculative implementation or repair churn.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Public interface and approval](../spec.md#public-interface-and-approval); [Agent contracts and access](../spec.md#agent-contracts-and-access); [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts).

**Scope:** The human-decision outcome and handoff within the existing one-ticket cycle.

## Acceptance criteria

- [x] Recognize a valid human-decision-needed report from implementation or either review axis.
- [x] Preserve the current work and record the precise unresolved decision, relevant approved contract, and available evidence.
- [x] Block the affected ticket immediately rather than spending remaining repairs inventing a requirement or changing an approved interface.
- [x] Do not edit the approved spec, ticket, or project standards or advance integration in response to the decision request.
- [x] Expose the decision through status and the final report, with attempt counts reflecting only work actually performed.

## Verification

Use scripted ambiguity and contract-conflict scenarios at different roles; assert immediate bounded handoff, unchanged requirements/integration, and accurate counters.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

All five acceptance criteria are verified at implementation checkpoint `dc1018e`, reviewed against the fixed starting baseline `2adf9b5fd906e8337c5147e94ab5ceb35ac8dbef`. Previous readiness label: `ready-for-agent`; `Blocked by:` remains dependency history. No fixes were needed after separate independent Spec and Standards reviews.

The [criterion-specific completion evidence](../evidence/ticket-06/06-completion.md) and [19 saved actual CLI/Git observations (compact historical results)](../evidence/ticket-06/06-scenario-results.json) demonstrate validated decisions from implementation and both review axes, preserved current work and precise contract/decision/evidence handoffs, immediate Blocked/incomplete stopping with default repair allowance available, unchanged approved inputs/integration and caller work, and matching read-only status/final JSON with actual attempt counts/history. Initial and later-repair decisions cover exits 0/7. Invalid decision-like output remains untrusted and bounded; mixed findings respect decision precedence and optional findings retain ordinary nonblocking behavior.

Final checks: **399 tests passed in 232.26s** (37 decision cases plus all 362 prerequisite cases), strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI run/status checks. All 19 checkpoint observations passed. Independent **Spec: no findings; 37 focused tests independently passed. Standards: no findings.** No optional suggestions, unchecked criteria or unresolved ticket-06 decisions remain.

No active harness run using these feature requirements was found. Bookkeeping follows implementation, checks and separate fresh reviews and is committed separately. The pre-existing skill relocation remains unstaged; no push was performed. Optional-suggestion reporting, timeouts, scheduling/continuation, new role-skill/live Codex delivery, OS access enforcement, concurrency and recovery remain with later tickets.
