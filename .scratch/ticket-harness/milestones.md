# Development milestones — ownership and review amendment

**Approved plan version:** oop-v2. **Revision:** review-process-1.

**Publication approval:** [Human decision and scope](approval.md).

## Eligibility and decisions

Completed 01–15 retain their evidence. M1 gains nine required tickets 16–24 before its still-unrequested QA. Review workflow/evaluation precedes the five refactors; later milestones wait for explicit human acceptance of the previous one. Required architecture assessments and disposition rules precede QA readiness, while review completion and review decisions never equal candidate acceptance. E1 remains independent, immediately after verified 34.

Before any required milestone QA request, use the shared
[development checkpoint contract](../../docs/agents/architecture-checkpoints.md).
Record cumulative baseline provenance, exact source, all package Python files,
prior findings and a fresh High Standards report. Missing/incomplete/stale work
or unresolved in-scope blockers holds readiness, even with all tickets completed.
Assessment completed, findings dispositioned, candidate ready and milestone
accepted are separate observations. Real M1 cumulative assessment remains
unperformed; ticket 18's isolated examples cannot substitute for it.

## Required release membership

| Milestone | Required tickets in preferred order | Gate |
| --- | --- | --- |
| M1: A complete QA-controlled Git cycle | [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Record review work, findings and decisions](issues/16-record-review-work-findings-and-decisions.md), [17: Review ownership across affected modules](issues/17-review-ownership-across-affected-modules.md), [18: Gate development on cumulative architecture review](issues/18-gate-development-on-cumulative-architecture-review.md), [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md), [20: Own implementation-attempt transitions](issues/20-own-implementation-attempt-transitions.md), [21: Own ticket execution and bounded repairs](issues/21-own-ticket-execution-and-bounded-repairs.md), [22: Return clearly prepared inputs](issues/22-return-clearly-prepared-inputs.md), [23: Own the complete run lifecycle](issues/23-own-the-complete-run-lifecycle.md), [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md) | First eligible group |
| M2: An unattended operator workflow | [25: Guide a human through milestone QA](issues/25-guide-and-record-human-milestone-qa.md), [26: Propose a versioned correction plan](issues/26-propose-versioned-qa-corrections.md), [27: Execute approved QA corrections](issues/27-execute-approved-qa-corrections.md), [28: Operate the orchestrator in the background](issues/28-operate-the-harness-in-the-background.md), [29: Continue independent work inside the current milestone](issues/29-continue-independent-work-after-blocks.md) | Explicit human acceptance of M1 |
| M3: Real agents with explicit guidance | [30: Supply coherent design guidance to Standards review](issues/30-supply-combined-design-guidance-to-standards-review.md), [31: Capture and deliver selected local skills](issues/31-capture-and-deliver-selected-local-skills.md), [32: Deliver focused implementation and Spec contexts](issues/32-deliver-focused-implementation-and-spec-review-contexts.md), [33: Enforce traceable runtime review checkpoints](issues/33-enforce-traceable-runtime-review-checkpoints.md), [34: Complete the workflow with real Codex roles](issues/34-run-a-real-codex-ticket-cycle.md) | Explicit human acceptance of M2 |
| M4: First usable release and final acceptance | [36: Verify runtime write and approval boundaries](issues/36-verify-role-write-boundaries.md), [37: Run a generated approved plan through the runtime](issues/37-run-a-generated-plan-through-the-runtime.md), [38: Demonstrate the revised first usable release](issues/38-demonstrate-the-first-usable-release.md) | Explicit human acceptance of M3 |

Every required ticket 10–34 and 36–38 has exactly one required membership (28 tickets, including completed 10–15). Completed baseline 01–09 remains intact. Ticket 35 belongs only to E1. M4 supplies final cumulative feature acceptance. Development milestones remain distinct from runtime fixture milestones.

## M1: A complete QA-controlled Git cycle

**Required tickets:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Record review work, findings and decisions](issues/16-record-review-work-findings-and-decisions.md), [17: Review ownership across affected modules](issues/17-review-ownership-across-affected-modules.md), [18: Gate development on cumulative architecture review](issues/18-gate-development-on-cumulative-architecture-review.md), [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md), [20: Own implementation-attempt transitions](issues/20-own-implementation-attempt-transitions.md), [21: Own ticket execution and bounded repairs](issues/21-own-ticket-execution-and-bounded-repairs.md), [22: Return clearly prepared inputs](issues/22-return-clearly-prepared-inputs.md), [23: Own the complete run lifecycle](issues/23-own-the-complete-run-lifecycle.md), [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md)

**QA status:** Not yet requested or accepted.

**QA setup:** Use an isolated miniature tracker and actual development reviewer evaluation artifacts, then a disposable foreground scripted two-milestone target repository with the refactored final source. Include the nine new ticket outcomes, genuine pre-refactor checkpoint evidence and a cumulative all-file architecture assessment.

**Human actions:** Follow a review concern through its immutable report, human/agent disposition, repair ticket/commit and verification. Inspect all declared evaluation cases, misses/false positives and guidance versions. Confirm risk-triggered/milestone assessments expose unresolved work, clean reviews progress, and changed source invalidates stale assessments. Inspect ownership reports for refactors 20–24. Then demonstrate first-group feature integration, exact tested QA request, stale-approval rejection, deliberate stop/new-process continuation without replay, exact human approval/promotion and final-only completion. Inspect invalid-input/failed-baseline and canonical restored-evidence invalidation observations.

**Pass conditions:** All M1 work is verified; review records explain why code changed, meaningful decisions remain human-owned, the declared reviewer corpus meets its criteria, and cumulative architecture assessment has no unresolved in-scope blocker. Existing CLI/record/checkpoint compatibility and exact QA behavior remain intact. Scripted approvals and review completion do not accept the development milestone.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.

## M2: An unattended operator workflow

**Required tickets:** [25: Guide a human through milestone QA](issues/25-guide-and-record-human-milestone-qa.md), [26: Propose a versioned correction plan](issues/26-propose-versioned-qa-corrections.md), [27: Execute approved QA corrections](issues/27-execute-approved-qa-corrections.md), [28: Operate the orchestrator in the background](issues/28-operate-the-harness-in-the-background.md), [29: Continue independent work inside the current milestone](issues/29-continue-independent-work-after-blocks.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After M1 acceptance, use QA-session/correction guidance and a disposable plan with independent and dependent work; include a review-originated correction and separate operator sessions.

**Human actions:** Inspect review findings/reasons alongside the candidate, request a correction and approve its amendment without accepting the candidate. Observe renewed QA, terminal-independent background operation, accurate status/logs, blocked-root/unrelated-success behavior, and cumulative architecture assessment before M2 QA.

**Pass conditions:** Review dispositions, correction approval and exact candidate acceptance remain distinct. Background status is observational, independent work respects prerequisite/milestone gates, and significant unresolved findings prevent readiness under the shared review contract.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.

## M3: Real agents with explicit guidance

**Required tickets:** [30: Supply coherent design guidance to Standards review](issues/30-supply-combined-design-guidance-to-standards-review.md), [31: Capture and deliver selected local skills](issues/31-capture-and-deliver-selected-local-skills.md), [32: Deliver focused implementation and Spec contexts](issues/32-deliver-focused-implementation-and-spec-review-contexts.md), [33: Enforce traceable runtime review checkpoints](issues/33-enforce-traceable-runtime-review-checkpoints.md), [34: Complete the workflow with real Codex roles](issues/34-run-a-real-codex-ticket-cycle.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After M2 acceptance, prepare scripted runtime review/decision cases and a tiny real-Codex plan using captured role guidance, a worker override, a seeded concern and an acceptable control.

**Human actions:** Inspect actual captured/delivered ownership/review instructions, inspected scope, immutable reports, finding/decision history and independent role profiles. Observe scripted runtime blocking/stale/authority/continuation cases and a real cumulative assessment plus independent ticket reviews. Verify no consumable QA request appears with unresolved required review work. Schedule E1 immediately after verified 34.

**Pass conditions:** Runtime review enforcement and actual real-agent instruction delivery/judgment are evidenced separately from M1 development evaluation. Human risk decisions and QA acceptance stay separate. E1 never gates release or supplies assumed model/context defaults.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.

## M4: First usable release and final acceptance

**Required tickets:** [36: Verify runtime write and approval boundaries](issues/36-verify-role-write-boundaries.md), [37: Run a generated approved plan through the runtime](issues/37-run-a-generated-plan-through-the-runtime.md), [38: Demonstrate the revised first usable release](issues/38-demonstrate-the-first-usable-release.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After M3 acceptance, start from a clean installed checkout and disposable target with generated-plan and role/access evidence, linked review history and all prior accepted milestone assessments.

**Human actions:** Operate the full planning, execution, review/decision, correction, background/status, deliberate stop/continue and exact QA/promotion cycle. Follow a concern from report through human rationale, implementation revision and independent verification. Inspect review-authority probes, final cumulative architecture assessment, unresolved/deferred findings and documented limitations.

**Pass conditions:** All required tickets 10–34 and 36–38 and prior milestone acceptances are accounted for cumulatively; the final source has the required architecture assessment, exact tested candidate and explicit final human acceptance. Review completion, all ticket Done states and automated gates alone are insufficient.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.

## E1: Independent early context experiment

**Required tickets:** [35: Run the early context-budget comparison](issues/35-compare-configurable-agent-context-limits.md)

**QA status:** Not yet requested or accepted.

**QA setup:** Immediately after verified 34 supplies the real backend and usage/settings evidence, select experiment 35 independently of release work.

**Human actions:** Review the controlled 100K/150K/200K/250K comparison, pressure case, active versus cumulative/cached usage, compaction behavior and measured quality/limitations. Keep reviewer effectiveness evidence distinct from this context-budget experiment.

**Pass conditions:** Document actual enforcement/compaction/advisory limits and independent experiment acceptance without making E1 a release prerequisite or silently changing role/context defaults.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.
