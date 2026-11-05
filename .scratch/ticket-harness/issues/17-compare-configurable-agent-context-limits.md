# 17: Compare configurable 100K–250K agent context limits

**What to build:** An early live-backend experiment configures 100K, 150K, 200K, and 250K per-agent active-context limits and compares verified outcomes on a fixed workload.

**Blocked by:** [13: Complete one real Codex ticket with configured role profiles](13-run-a-real-codex-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** Early experiment immediately after 13; separate from first-release completion requirements.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Early context-budget experiment](../README.md#early-context-budget-experiment); [baseline spec](../spec.md).

**Scope:** Extend the first verified real-Codex cycle with context controls and measurements. Prioritize this issue as soon as 13 is integrated; final release packaging, custom planning, and the comprehensive access-boundary probes are not prerequisites. Preserve this issue's stable identifier and avoid introducing automatic model selection.

## Acceptance criteria

- [ ] Expose configurable per-agent context limits of 100000, 150000, 200000, and 250000 tokens with 250000 as the starting target.
- [ ] Verify what the installed backend actually enforces or signals at each setting; distinguish enforced limits, compaction thresholds, and advisory targets instead of claiming an unsupported hard cap.
- [ ] Measure observed peak active context separately from cumulative input/output usage and cached-input counts, recording role, attempt, limit, model, and reasoning settings.
- [ ] Run the same bounded fixture workload and acceptance suite at each setting with consistent model/role settings and documented repetitions.
- [ ] Include a short control and a task-relevant context-pressure case capable of approaching the configured thresholds. Distinguish policy-wiring checks from comparative runs that actually exercise a limit; do not infer an optimal budget from runs that remain below every threshold.
- [ ] Report verified completion, failures, repairs, compactions or context-pressure handoffs, elapsed time, and cumulative usage alongside observed peak context.
- [ ] Prevent context pressure from skipping checks or producing false completion; record unsupported enforcement or missing measurements as explicit limitations.
- [ ] Publish a reproducible comparison and evidence-based recommendation without silently changing the established defaults.

## Verification

Exercise the configured limits using the existing public CLI/live backend and fixed disposable-repository workload, retaining raw usage evidence and independent acceptance results.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
