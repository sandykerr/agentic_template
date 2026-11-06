# 12: Execute only the first eligible milestone

**What to build:** Validate and capture a versioned milestone plan, including final coverage and dependency-consistent fixed membership. Run existing ticket gates into the feature branch for the current group only. At its boundary, record that milestone preparation is pending instead of starting later tickets or claiming feature completion. This slice does not present an untested candidate as ready for QA.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md).

**Status:** ready-for-agent

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R03](../ticket-proposal.md#r03-execute-only-the-first-eligible-milestone).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [ticket lifecycle](../spec.md#ticket-lifecycle).

## Acceptance criteria

- [ ] Define, validate, and capture approved plan/version and fixed milestone membership, final required coverage, dependency consistency, QA conditions, and applicable worker settings.
- [ ] Reject missing/duplicate membership, missing final coverage, invalid cross-group dependencies, and conflicting metadata before workers or branch changes.
- [ ] Execute existing per-ticket checks/reviews/candidate gates into the feature branch for the current milestone only, using the latest verified feature revision.
- [ ] At the milestone boundary, persist preparation-pending status and leave later work unstarted; do not present an untested dev candidate as QA-ready or declare feature completion.
- [ ] Demonstrate two groups through the public CLI with scripted processes and real Git, preserving caller work, approved snapshots, and exact revision evidence.

## Verification

A two-group public CLI fixture integrates the first group, leaves the second unstarted, preserves approved inputs, and rejects missing final coverage or invalid membership before workers launch.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.
