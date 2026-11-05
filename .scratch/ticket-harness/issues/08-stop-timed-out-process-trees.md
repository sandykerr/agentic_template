# 08: Stop stalled assignments and check processes

**What to build:** Each worker, reviewer, and check invocation finishes or is terminated within its configured timeout, with bounded handling and useful evidence.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts); [Codex execution](../spec.md#codex-execution).

**Scope:** Stage timeouts and process-tree cleanup through the existing runner and repair policy; no interrupted-run resume.

## Acceptance criteria

- [ ] Require positive configurable timeouts for implementation, repair, both review roles, lightweight checks, baseline checks, and candidate checks.
- [ ] Stop a timed-out process and its descendants and collect available output without leaving the stage indefinitely active.
- [ ] Apply remaining repair allowances or block the affected ticket without granting an unbounded timeout-specific retry loop.
- [ ] Treat failed baseline/shared-environment stages as run failures without spending ticket repair attempts.
- [ ] Record the timed-out role/check, allowance, available evidence, and resulting ticket/run outcome through status.
- [ ] Demonstrate worker, reviewer, and check timeouts, including a child process, using controlled scripted processes.

## Verification

Use bounded fixture processes with observable child cleanup and public run/status outcomes; avoid time-sensitive assertions tighter than the environment can reliably support.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
