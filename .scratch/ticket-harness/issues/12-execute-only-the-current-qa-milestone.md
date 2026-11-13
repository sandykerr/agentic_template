# 12: Execute only the first eligible milestone

**What to build:** Validate and capture a versioned milestone plan, including final coverage and dependency-consistent fixed membership. Run existing ticket gates into the feature branch for the current group only. At its boundary, record that milestone preparation is pending instead of starting later tickets or claiming feature completion. This slice does not present an untested candidate as ready for QA.

**Blocked by:** [10: Turn one grilling session into an approved plan](10-produce-approved-harness-inputs-with-planning-skill.md).

**Status:** completed

**Milestone:** M1. Follow [milestone eligibility](../milestones.md) before selecting work.

**Plan slice:** [R03](../ticket-proposal.md#r03-execute-only-the-first-eligible-milestone).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Context:** [planning and milestone contract](../spec.md#planning-and-milestone-contract); [ticket lifecycle](../spec.md#ticket-lifecycle).

## Acceptance criteria

- [x] Define, validate, and capture approved plan/version and fixed milestone membership, final required coverage, dependency consistency, QA conditions, and applicable worker settings.
- [x] Reject missing/duplicate membership, missing final coverage, invalid cross-group dependencies, and conflicting metadata before workers or branch changes.
- [x] Execute existing per-ticket checks/reviews/candidate gates into the feature branch for the current milestone only, using the latest verified feature revision.
- [x] At the milestone boundary, persist preparation-pending status and leave later work unstarted; do not present an untested dev candidate as QA-ready or declare feature completion.
- [x] Demonstrate two groups through the public CLI with scripted processes and real Git, preserving caller work, approved snapshots, and exact revision evidence.

## Verification

A two-group public CLI fixture integrates the first group, leaves the second unstarted, preserves approved inputs, and rejects missing final coverage or invalid membership before workers launch.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](../milestones.md); do not start the next ticket automatically.

## Comments

Verified complete at implementation `14cafef40726eba80d8648d98d9c263fde3a5d0b`, reviewed against original baseline `2e15004338b45d61719656de113c2cbfdea56345`. Previous readiness: `ready-for-agent`; declared dependency history is preserved. [Completion evidence](../evidence/ticket-12/12-completion.md) maps each criterion to the [78 retained final-run CLI/Git scenarios (compact historical results)](../evidence/ticket-12/12-scenario-results.json), including 30 new milestone cases, and the [coverage map](../evidence/ticket-12/12-coverage-map.md).

All five criteria are proven: approved plan/settings capture, preflight rejection, existing exact ticket gates on latest feature bases, preparation-pending without later execution or QA readiness, and the isolated two-group caller/snapshot/revision demonstration. [Actual final checks (retirement summary)](../evidence/ticket-12/README.md#retired-evidence): 499 tests passed in 400.57s; strict mypy, Ruff lint/format, and whitespace passed. Separate fresh High [Spec](../evidence/ticket-12/12-review-spec.md) and [Standards](../evidence/ticket-12/12-review-standards.md) reviews each found zero blockers and zero optional suggestions. No implementation changes followed review; interrupted/development checks are not completion evidence.

No unchecked criterion or unresolved ticket-12 item remains. Completion bookkeeping and generated handoff receive separate commits. Ticket 13 is the next prerequisite-ready M1 assignment; this record does not start it, accept M1, prepare/promote a dev candidate, or complete the feature. No push occurred.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
