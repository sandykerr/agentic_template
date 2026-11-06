# 20: Continue independent work inside the current milestone

**What to build:** Retain pre-QA ticket 10's blocked-root/waiting-dependent/unrelated-success behavior and shared-environment stopping. Unrelated work is eligible only within the current milestone; a block or exhausted repair cannot bypass a QA boundary or produce feature success.

**Blocked by:** [12: Execute only the first eligible milestone](12-execute-only-the-current-qa-milestone.md); [06: Stop for decisions outside approved contracts](06-surface-human-decisions-without-retrying.md).

**Status:** ready-for-agent

**Milestone:** M2. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R11](../ticket-proposal.md#r11-continue-independent-work-inside-the-current-milestone).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [ticket lifecycle](../spec.md#ticket-lifecycle); [bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts).

## Acceptance criteria

- [ ] Keep human-decision/exhausted-repair tickets Blocked and their dependent tickets Pending without implicit retries.
- [ ] Continue unrelated ready work inside the current milestone from the latest verified feature revision; no ticket from a later milestone starts.
- [ ] Stop when no executable current-milestone work remains and accurately distinguish Done, Blocked, dependency-waiting, and QA-waiting states.
- [ ] Return an incomplete outcome for unresolved required work even if unrelated tickets succeeded; shared environment/integrity failures stop the run.
- [ ] Demonstrate a blocked root, waiting dependent, unrelated success, and later-group ticket that remains unstarted, retaining each ticket's evidence.

## Verification

Reuse the pre-QA ticket 10 fixture requirements, adding later-group work that must remain unstarted. Preserve accurate incomplete and waiting outcomes.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

### QA realignment

Reconciled with approved slice R11; the [previous definition](../archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.
