# 16: Demonstrate the first usable release from a clean checkout

**What to build:** A developer can install the harness, configure a separate small repository, and reproduce the documented successful, repaired, and blocked outcomes.

**Blocked by:** [07: Report optional review suggestions without rework](07-report-optional-suggestions-without-repair.md); [10: Continue unrelated tickets after a blocked prerequisite](10-continue-independent-work-after-blocks.md); [14: Verify implementation and review access boundaries](14-verify-role-write-boundaries.md); [15: Produce executable Markdown requirements with a planning skill](15-produce-approved-harness-inputs-with-planning-skill.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Testing decisions](../spec.md#testing-decisions); [Out of scope](../spec.md#out-of-scope); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** Release acceptance and the runnable walkthrough for the agreed sequential first version; preserve concurrency, recovery, and notifications as later work. The context-limit experiment is an independent early slice after issue 13, rather than a prerequisite for this release demonstration.

## Acceptance criteria

- [ ] Document installation, project commands, role settings, limits, local requirements, run/status usage, and artifact inspection using the interfaces actually implemented.
- [ ] Provide a runnable example showing successful integration, bounded repair, a blocked ticket, a waiting dependent, optional suggestions, and unrelated successful work.
- [ ] Run the complete deterministic suite from a clean checkout without requiring model credentials or network access.
- [ ] Run the separate small live check in the configured Codex environment and record actual integration and skill/access evidence, or report the explicit blocker without claiming complete live validation.
- [ ] Show approved inputs unchanged and integration references bound only to passing candidates.
- [ ] Describe sequential execution and non-resumable interrupted runs accurately, with a clean distinction between the first release and deferred slices.

## Verification

Follow the documented walkthrough from a clean environment against disposable target repositories, collect real command outcomes, and reconcile them with status/report/Git observations.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
