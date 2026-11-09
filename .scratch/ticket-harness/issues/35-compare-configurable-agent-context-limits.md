# 35: Run the early context-budget comparison

**What to build:** Retain pre-QA ticket 17's 100K/150K/200K/250K controls, fixed workload and reasoning settings, genuine context-pressure case, repetitions, raw measurements, and acceptance checks. Distinguish hard enforcement, compaction thresholds, and advisory targets; active occupancy is separate from cumulative/cached usage.

**Blocked by:** [34: Complete the workflow with real Codex roles](34-run-a-real-codex-ticket-cycle.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** E1 (independent context experiment; not a release gate). Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R16](../ticket-proposal.md#r16-run-the-early-context-budget-comparison).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](../spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](../spec.md#codex-execution); [agent contracts and access](../spec.md#agent-contracts-and-access).

## Acceptance criteria

- [ ] Expose 100000, 150000, 200000 and 250000 active-context settings, starting at 250000; verify enforcement, compaction signals or advisory behavior without claiming an unsupported hard cap.
- [ ] Measure peak active context separately from cumulative input/output and cached usage, recording role, attempt, model, reasoning, and configured limit.
- [ ] Use a fixed bounded workload and acceptance suite, consistent settings and documented repetitions at every limit.
- [ ] Include both a short control and a task-relevant pressure case capable of approaching thresholds; below-100K runs cannot establish comparative higher-limit effects.
- [ ] Report verified outcomes, failures, repairs, compactions/handoffs, elapsed time and raw usage evidence; context pressure cannot bypass gates.
- [ ] Publish reproducible findings and limitations without silently changing defaults. Execute immediately after ticket 34 under independent experiment checkpoint E1; do not add release, comprehensive access, background, or completed planning-integration gates.

## Verification

Preserve the current ticket's explicit experiment evidence requirements. Prioritize immediately after ticket 34, before comprehensive boundary probes or release packaging. It remains independent of first-release acceptance dependencies.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R16; the [previous definition](../archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
