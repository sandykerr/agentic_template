# 08: Stop stalled assignments and check processes

**What to build:** Each worker, reviewer, and check invocation finishes or is terminated within its configured timeout, with bounded handling and useful evidence.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts); [Codex execution](../spec.md#codex-execution).

**Scope:** Stage timeouts and process-tree cleanup through the existing runner and repair policy; no interrupted-run resume.

## Acceptance criteria

- [x] Require positive configurable timeouts for implementation, repair, both review roles, lightweight checks, baseline checks, and candidate checks.
- [x] Stop a timed-out process and its descendants and collect available output without leaving the stage indefinitely active.
- [x] Apply remaining repair allowances or block the affected ticket without granting an unbounded timeout-specific retry loop.
- [x] Treat failed baseline/shared-environment stages as run failures without spending ticket repair attempts.
- [x] Record the timed-out role/check, allowance, available evidence, and resulting ticket/run outcome through status.
- [x] Demonstrate worker, reviewer, and check timeouts, including a child process, using controlled scripted processes.

## Verification

Use bounded fixture processes with observable child cleanup and public run/status outcomes; avoid time-sensitive assertions tighter than the environment can reliably support.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

All six acceptance criteria are verified at implementation checkpoint `fbfc088`, independently reviewed against starting baseline `3d78722ae2e0f53c40eb169234aebec50e2140fb`. Previous readiness label: `ready-for-agent`; `Blocked by:` remains dependency history.

The [criterion-specific evidence and full reviews](../evidence/ticket-08/08-completion.md) and [27 actual timeout-test observations plus installed CLI smoke (compact historical results)](../evidence/ticket-08/08-scenario-results.json) verify positive independent stage allowances, process-group/descendant cleanup with bounded output draining and reaping, retained partial output and exact attempt/revision identity, successful renewed verification after worker/either-review/check/candidate timeouts, default bounded exhaustion, baseline/environment stopping without repair churn, protected earlier evidence, and matching durable run/status/final JSON. A complete success/decision report or zero leader exit cannot override a timeout caused by children retaining output handles. Current role/report/command interfaces remain unchanged.

Final checks: **448 tests passed in 432.71s**, including 27 new timeout and all 421 prerequisite cases; focused timeout/repair tests **85 passed**. Strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI run/status passed through the documented reusable Python environment. Observations were captured during the required full run and source hashes verified against the checkpoint.

Independent **Spec: 0 blockers, 0 optional suggestions**; it also reproduced cleanup of a background child after ordinary worker completion. Independent **Standards: 0 blockers, 1 optional suggestion S1** to stream captured output into artifacts to reduce memory growth from verbose commands. S1 is retained without a required repair; full review reports and provenance are in the evidence. No fix commit, unchecked criterion or required unresolved item remains.

Timeout cleanup uses inherited POSIX process groups with trusted commands, as documented; OS role enforcement and deliberate session/group escape containment remain outside this mechanism. No active harness run uses these feature requirements. No unrelated edits were staged and no push was performed. Scheduling/continuation, live Codex/role guidance and recovery remain later tickets. Bookkeeping is committed separately from implementation; the next handoff follows afterward.
