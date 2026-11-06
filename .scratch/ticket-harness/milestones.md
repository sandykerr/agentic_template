# Published development milestones

The human approved this QA-first plan. Tickets 01–09 are completed baseline work; no new milestone reopens them. This plan's first delivery is the scripted Git/QA cycle, not the original product-first release.

## Eligibility and decisions

- Start with M1. Within it, select prerequisite-ready tickets using the published plan order; the initial ticket is [10](issues/10-produce-approved-harness-inputs-with-planning-skill.md). Open tickets are numbered in preferred execution order; dependencies and human QA gates still determine eligibility.
- A later release milestone is ineligible until every required ticket in the previous milestone is verified complete and the human accepts that milestone.
- Completing a ticket, approving this plan, or passing tests is not milestone acceptance. No QA milestone has been recorded as accepted by this publication.
- Until the new runtime exists, enforce these development checkpoints manually and through handoffs. They are distinct from the target-repository milestones inside the test fixture.
- At QA, use a request-specific decision artifact outside approved requirements and implementation worktrees, with the identities established by the implemented request contract. A separate session records explicit human acceptance. This document defines the plan and is not that decision artifact.
- E1 is a separate experiment selection with its own final acceptance. Prioritize ticket 25 immediately after 24, subject to their actual prerequisites; it never gates release acceptance or acquires unrelated release prerequisites.

## Required release membership

| Milestone | Required tickets in preferred plan order | Gate |
| --- | --- | --- |
| M1: A complete QA-controlled Git cycle | [10](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11](issues/11-stop-development-handoffs-at-qa-milestones.md), [12](issues/12-execute-only-the-current-qa-milestone.md), [13](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14](issues/14-promote-only-the-human-approved-milestone.md), [15](issues/15-continue-from-a-planned-qa-checkpoint.md) | First eligible milestone |
| M2: An unattended operator workflow | [16](issues/16-guide-and-record-human-milestone-qa.md), [17](issues/17-propose-versioned-qa-corrections.md), [18](issues/18-execute-approved-qa-corrections.md), [19](issues/19-operate-the-harness-in-the-background.md), [20](issues/20-continue-independent-work-after-blocks.md) | Human acceptance of M1 |
| M3: Real agents with explicit guidance | [21](issues/21-supply-combined-design-guidance-to-standards-review.md), [22](issues/22-capture-and-deliver-selected-local-skills.md), [23](issues/23-deliver-focused-implementation-and-spec-review-contexts.md), [24](issues/24-run-a-real-codex-ticket-cycle.md) | Human acceptance of M2 |
| M4: First usable release and final acceptance | [26](issues/26-verify-role-write-boundaries.md), [27](issues/27-run-a-generated-plan-through-the-runtime.md), [28](issues/28-demonstrate-the-first-usable-release.md) | Human acceptance of M3 |

Completed 01–09 supply prerequisite evidence rather than new pending membership. The 18 remaining release tickets are assigned exactly once. Ticket 25 belongs only to E1.

## M1: A complete QA-controlled Git cycle

**Required tickets:** [10](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11](issues/11-stop-development-handoffs-at-qa-milestones.md), [12](issues/12-execute-only-the-current-qa-milestone.md), [13](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14](issues/14-promote-only-the-human-approved-milestone.md), [15](issues/15-continue-from-a-planned-qa-checkpoint.md).

**QA status:** Not yet requested or accepted.

**Human QA:** Inspect the unified spec/proposal flow and development handoff. Run the foreground scripted two-milestone demo in a disposable repository: first-group tickets integrate into the feature branch; a tested feature-to-dev candidate waits; stale approval leaves dev unchanged; explicit acceptance promotes only that candidate; stop/restart at QA; second-group work starts only after acceptance; final acceptance completes the feature.

**Acceptance evidence:** Record the assessed source/feature/development/candidate revisions, relevant plan/request identity, actual gate results, observed human checks, findings and explicit decision in the request-specific evidence. Corrections require an approved plan amendment and renewed candidate acceptance.

## M2: An unattended operator workflow

**Required tickets:** [16](issues/16-guide-and-record-human-milestone-qa.md), [17](issues/17-propose-versioned-qa-corrections.md), [18](issues/18-execute-approved-qa-corrections.md), [19](issues/19-operate-the-harness-in-the-background.md), [20](issues/20-continue-independent-work-after-blocks.md).

**QA status:** Not yet requested or accepted.

**Human QA:** Use the QA-session skill to request corrections, approve only the amendment, and inspect renewed QA. Launch in the background, close the original terminal, inspect logs/status, and write the exact decision artifact from a separate session. Verify a blocked ticket can coexist with unrelated eligible success without crossing a QA boundary.

**Acceptance evidence:** Record the assessed source/feature/development/candidate revisions, relevant plan/request identity, actual gate results, observed human checks, findings and explicit decision in the request-specific evidence. Corrections require an approved plan amendment and renewed candidate acceptance.

## M3: Real agents with explicit guidance

**Required tickets:** [21](issues/21-supply-combined-design-guidance-to-standards-review.md), [22](issues/22-capture-and-deliver-selected-local-skills.md), [23](issues/23-deliver-focused-implementation-and-spec-review-contexts.md), [24](issues/24-run-a-real-codex-ticket-cycle.md).

**QA status:** Not yet requested or accepted.

**Human QA:** Inspect combined design/Standards guidance, captured defaults and additions, and scoped implementation/repair/Spec contexts. Observe a tiny real-Codex cycle with Medium worker/repair and High reviewer defaults plus an actual ticket override. Inspect delivered instruction identities and actual reports/gates. Human approval remains separate from model output.

**Acceptance evidence:** Record the assessed source/feature/development/candidate revisions, relevant plan/request identity, actual gate results, observed human checks, findings and explicit decision in the request-specific evidence. Corrections require an approved plan amendment and renewed candidate acceptance.

## M4: First usable release and final acceptance

**Required tickets:** [26](issues/26-verify-role-write-boundaries.md), [27](issues/27-run-a-generated-plan-through-the-runtime.md), [28](issues/28-demonstrate-the-first-usable-release.md).

**QA status:** Not yet requested or accepted.

**Human QA:** Inspect live role/ref/QA-artifact access probes and the generated-plan walkthrough. From a clean checkout operate the full sequential planning, execution, correction, QA, background, and safe-continuation experience. Verify final promotion into dev and accurate documentation of deferred capabilities.

**Acceptance evidence:** Record the assessed source/feature/development/candidate revisions, relevant plan/request identity, actual gate results, observed human checks, findings and explicit decision in the request-specific evidence. Corrections require an approved plan amendment and renewed candidate acceptance.

## E1: Independent early context experiment

**Required tickets:** [25](issues/25-compare-configurable-agent-context-limits.md).

**QA status:** Not yet requested or accepted.

**Human QA:** Review the reproducible 100K/150K/200K/250K comparison, short control and genuine pressure case, actual enforcement/compaction/advisory limitations, peak occupancy versus cumulative/cached usage, and independent acceptance outcomes. Do not silently change defaults.

**Acceptance evidence:** Record the assessed source/feature/development/candidate revisions, relevant plan/request identity, actual gate results, observed human checks, findings and explicit decision in the request-specific evidence. Corrections require an approved plan amendment and renewed candidate acceptance.
