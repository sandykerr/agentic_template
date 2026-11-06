# Ticket numbering history

The human requested sequential execution numbers after approving and publishing the QA-first plan. This refactor changes the identities of its 19 unimplemented tickets, preserving their scope, dependencies, acceptance criteria and readiness. Completed tickets 01–09 and their evidence remain unchanged. No implementation or human QA acceptance is implied.

The previous QA-first IDs below refer to the published QA realignment before sequential renumbering. The older [pre-QA definitions](issues-before-milestone-qa/) are a different historical stage: their IDs, requirements and dependency text remain historical. Their “current ticket” pointers lead to the present owner; original 11 and 15 were split across two current tickets each, as the [approved plan](../ticket-proposal.md#comparison-with-the-pre-qa-open-tickets) explains.

| Previous QA-first ID | Current ID | Stable plan slice | Current ticket |
| --- | --- | --- | --- |
| 15 | 10 | R01 | [Turn one grilling session into an approved plan](../issues/10-produce-approved-harness-inputs-with-planning-skill.md) |
| 18 | 11 | R02 | [Stop development handoffs at human checkpoints](../issues/11-stop-development-handoffs-at-qa-milestones.md) |
| 19 | 12 | R03 | [Execute only the first eligible milestone](../issues/12-execute-only-the-current-qa-milestone.md) |
| 20 | 13 | R04 | [Present a tested feature-to-dev candidate](../issues/13-prepare-a-tested-feature-to-dev-candidate.md) |
| 21 | 14 | R05 | [Consume approval, promote, and continue](../issues/14-promote-only-the-human-approved-milestone.md) |
| 22 | 15 | R06 | [Continue after a deliberate QA stop](../issues/15-continue-from-a-planned-qa-checkpoint.md) |
| 23 | 16 | R07 | [Guide a human through milestone QA](../issues/16-guide-and-record-human-milestone-qa.md) |
| 24 | 17 | R08 | [Propose a versioned correction plan](../issues/17-propose-versioned-qa-corrections.md) |
| 25 | 18 | R09 | [Execute approved QA corrections](../issues/18-execute-approved-qa-corrections.md) |
| 26 | 19 | R10 | [Operate the orchestrator in the background](../issues/19-operate-the-harness-in-the-background.md) |
| 10 | 20 | R11 | [Continue independent work inside the current milestone](../issues/20-continue-independent-work-after-blocks.md) |
| 11 | 21 | R12 | [Supply coherent design guidance to Standards review](../issues/21-supply-combined-design-guidance-to-standards-review.md) |
| 27 | 22 | R13 | [Capture and deliver selected local skills](../issues/22-capture-and-deliver-selected-local-skills.md) |
| 12 | 23 | R14 | [Deliver focused implementation and Spec contexts](../issues/23-deliver-focused-implementation-and-spec-review-contexts.md) |
| 13 | 24 | R15 | [Complete the workflow with real Codex roles](../issues/24-run-a-real-codex-ticket-cycle.md) |
| 17 | 25 | R16 | [Run the early context-budget comparison](../issues/25-compare-configurable-agent-context-limits.md) |
| 14 | 26 | R17 | [Verify runtime write and approval boundaries](../issues/26-verify-role-write-boundaries.md) |
| 28 | 27 | R18 | [Run a generated approved plan through the runtime](../issues/27-run-a-generated-plan-through-the-runtime.md) |
| 16 | 28 | R19 | [Demonstrate the revised first usable release](../issues/28-demonstrate-the-first-usable-release.md) |

Current groups: M1 = 10–15; M2 = 16–20; M3 = 21–24; E1 = 25 (independent, immediately after 24); M4 = 26–28. Dependencies and human QA acceptance still gate execution. Ticket 25 does not gate release acceptance.
