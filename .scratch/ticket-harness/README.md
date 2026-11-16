# Ticket harness — evidence policy and operator workflow

**Approved plan version:** evidence-policy-1. **Base:** oop-v2 / review-process-1.

**Ticket publication decision:** [Human instruction and scope](#ticket-publication-decision).

Read the [feature spec](spec.md), [evidence workflow spec](evidence-workflow-spec.md),
[authoritative ticket files](#complete-ticket-index), [milestones](milestones.md)
and [old-to-new numbering map](archive/evidence-policy-numbering-history.md).
The [prior authoring bundle](archive/before-evidence-policy-1/README.md) preserves
the previous approved requirements and navigation.

**M1 is accepted** at `88e4cd8`; [actual human decision](evidence/m1-final-review-01/m1-qa-decision.md).
Ticket25 is verified complete; next eligible work is ticket26 in EC1. Tickets
01–25 are complete, and26–30 remain subject to their dependencies and gates. The
former open 25–38 are now 31–44. No implementation starts with this publication.

## Document ownership

The [feature spec](spec.md) owns shared implementation, role and verification
contracts; [individual issue files](issues/) own ticket bodies and criteria;
[milestones](milestones.md) own human QA and progression gates. This index links
those sources and records current status. The
[retired proposal](archive/README.md#retired-evidence-policy-1-proposal) preserves
publication history and is no longer synchronized with current tickets.

The [evidence workflow spec](evidence-workflow-spec.md) owns evidence requirements.
The [capture skill](../../.agents/skills/custom/capture-evidence/SKILL.md) provides
producer steps; the [helper reference](../../docs/agents/evidence-capture.md)
describes implemented commands, records and failure behavior.

## Ticket publication decision

For evidence-policy-1, extending oop-v2 / review-process-1, the human accepted the
evidence workflow spec, requested capture before cleanup and explicit ADAPT
execution criteria in ticket 26, then instructed:

> Ok, use $to-tickets to create the markdown ticket files, including the newly ordered tickets from previous tickets 25-onward.

The decision authorized local publication of tickets 25–30 and renumbering the
former open tickets 25–38 to 31–44, with the reviewed public CLI testing seam and
role defaults. EC1 covers 25–26, EC2 covers 27, and EC3 covers 28–30, followed by
the existing M2–M4. E1 remains independent after verified ticket 40. Completed
tickets 01–24 and actual M1 acceptance retain their existing authority.

Publication itself authorized no implementation, run, evidence deletion,
milestone acceptance, Git-history rewrite or external publication.

This concise reconstruction replaces `evidence-policy-approval.md`. The
[publication record](evidence-policy-publication-record.json) and
[validation](evidence-policy-publication-validation.json) retain the original
publication paths and identities; their hashes describe the original document.
The former `evidence-policy.md` is now [the workflow spec](evidence-workflow-spec.md).

## Implementation status

Required development order: accepted M1 → EC1 (25–26) → EC2 (27) → EC3 (28–30)
→ M2 (31–35) → M3 (36–40) → M4 (42–44). Human acceptance gates each next group.
E1 (41) is independent immediately after verified real-agent ticket 40.
Ticket25 is complete; ticket26 is next within EC1. Later groups remain gated by
actual human acceptance; the generated root handoff starts no implementation.

Evidence remains [organized by ticket](evidence/README.md), with retirement notes
in the affected ticket READMEs. Historical completion and acceptance records keep
their original IDs, scope and paths; use the numbering map for current open-ticket
navigation.

## Complete ticket index

| ID and title | Prerequisites | Readiness/completion | Milestone |
| --- | --- | --- | --- |
| [01: Complete one scripted ticket through every gate](issues/01-complete-one-scripted-ticket-cycle.md) | None | completed | Completed baseline |
| [02: Reject invalid requirements before starting work](issues/02-reject-invalid-inputs-before-execution.md) | 01 | completed | Completed baseline |
| [03: Reject invalid agent reports and review evidence](issues/03-validate-agent-reports-and-review-evidence.md) | 01 | completed | Completed baseline |
| [04: Promote only the exact verified candidate](issues/04-promote-only-the-verified-candidate.md) | 01 | completed | Completed baseline |
| [05: Repair rejected submissions within a bounded allowance](issues/05-repair-rejected-submissions-within-budget.md) | 03, 04 | completed | Completed baseline |
| [06: Stop for decisions outside approved contracts](issues/06-surface-human-decisions-without-retrying.md) | 05 | completed | Completed baseline |
| [07: Report optional review suggestions without rework](issues/07-report-optional-suggestions-without-repair.md) | 05 | completed | Completed baseline |
| [08: Stop stalled assignments and check processes](issues/08-stop-timed-out-process-trees.md) | 05 | completed | Completed baseline |
| [09: Execute verified dependencies in a stable order](issues/09-execute-dependencies-sequentially.md) | 02 | completed | Completed baseline |
| [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md) | 09 | completed | M1 |
| [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md) | 10 | completed | M1 |
| [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md) | 10 | completed | M1 |
| [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md) | 12 | completed | M1 |
| [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md) | 13 | completed | M1 |
| [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md) | 14 | completed | M1 |
| [16: Record review work, findings and decisions](issues/16-record-review-work-findings-and-decisions.md) | 10, 11 | completed | M1 |
| [17: Review ownership across affected modules](issues/17-review-ownership-across-affected-modules.md) | 16 | completed | M1 |
| [18: Gate development on cumulative architecture review](issues/18-gate-development-on-cumulative-architecture-review.md) | 16, 17 | completed | M1 |
| [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md) | 17, 18 | completed | M1 |
| [20: Own implementation-attempt transitions](issues/20-own-implementation-attempt-transitions.md) | 05, 06, 19 | completed | M1 |
| [21: Own ticket execution and bounded repairs](issues/21-own-ticket-execution-and-bounded-repairs.md) | 20 | completed | M1 |
| [22: Return clearly prepared inputs](issues/22-return-clearly-prepared-inputs.md) | 02, 12, 19 | completed | M1 |
| [23: Own the complete run lifecycle](issues/23-own-the-complete-run-lifecycle.md) | 15, 21, 22 | completed | M1 |
| [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md) | 15, 23 | completed | M1 |
| [25: Guide ticket and shared evidence creation](issues/25-guide-ticket-and-shared-evidence-creation.md) | 24 | completed | EC1 |
| [26: Review and safely retire routine ticket evidence](issues/26-review-and-safely-retire-routine-ticket-evidence.md) | 25 | ready-for-agent | EC1 |
| [27: Assess evidence in parallel and consolidate fresh review](issues/27-assess-evidence-in-parallel-and-consolidate-fresh-review.md) | 26 | ready-for-agent | EC2 |
| [28: Guide human review of summaries and proposed merges](issues/28-guide-human-review-of-summaries-and-proposed-merges.md) | 27 | ready-for-agent | EC3 |
| [29: Reassess retained evidence during ticket completion](issues/29-reassess-retained-evidence-during-ticket-completion.md) | 28 | ready-for-agent | EC3 |
| [30: Calibrate and adopt the complete evidence workflow](issues/30-calibrate-and-adopt-the-complete-evidence-workflow.md) | 29 | ready-for-agent | EC3 |
| [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md) | 10, 14, 30 | ready-for-agent | M2 |
| [32: Propose a versioned correction plan](issues/32-propose-versioned-qa-corrections.md) | 10, 31 | ready-for-agent | M2 |
| [33: Execute approved QA corrections](issues/33-execute-approved-qa-corrections.md) | 15, 32 | ready-for-agent | M2 |
| [34: Operate the orchestrator in the background](issues/34-operate-the-harness-in-the-background.md) | 15 | ready-for-agent | M2 |
| [35: Continue independent work inside the current milestone](issues/35-continue-independent-work-after-blocks.md) | 12, 06 | ready-for-agent | M2 |
| [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md) | 03, 19 | ready-for-agent | M3 |
| [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md) | 10, 36 | ready-for-agent | M3 |
| [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md) | 37, 19 | ready-for-agent | M3 |
| [39: Enforce traceable runtime review checkpoints](issues/39-enforce-traceable-runtime-review-checkpoints.md) | 19, 24, 36, 37, 38 | ready-for-agent | M3 |
| [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md) | 15, 38, 08, 39 | ready-for-agent | M3 |
| [41: Run the early context-budget comparison](issues/41-compare-configurable-agent-context-limits.md) | 40 | ready-for-agent | E1 |
| [42: Verify runtime write and approval boundaries](issues/42-verify-role-write-boundaries.md) | 31, 40 | ready-for-agent | M4 |
| [43: Run a generated approved plan through the runtime](issues/43-run-a-generated-plan-through-the-runtime.md) | 10, 33, 37 | ready-for-agent | M4 |
| [44: Demonstrate the revised first usable release](issues/44-demonstrate-the-first-usable-release.md) | 11, 34, 35, 42, 43, 07 | ready-for-agent | M4 |

## Agent context policy

- Use GPT-6.1 Sol as requested, with one fresh context for each implementation, review, or repair assignment.
- Target at most **250,000 tokens of active context per agent**, including instructions, relevant source, tool results, reasoning/output retained in context, and room to finish verification and the handoff.
- This is a per-agent context constraint, not a cumulative per-ticket usage budget. Reprocessing cached input across requests can make cumulative usage much larger than the currently occupied context.
- Read the assigned issue and its scoped spec references first. Follow the repository's glossary/ADR instructions, discover the affected source, and pull extra references when necessary. Sibling transcripts and entire upstream skill libraries are not default inputs.
- Keep headroom for debugging and final checks. If the bounded outcome will not fit, preserve useful work and report the evidence and proposed split before expanding the assignment.
- No numerical implementation-usage estimate is claimed before measurements exist. These slices are scoped by observable outcomes and the context required to understand them.
- The current local Codex catalog reports 500,000 nominal tokens and a 95% effective-window setting for gpt-6.1-sol; the inspected session reports a 475,000 effective window. The requested 8M figure was clarified to a 250K agent target after distinguishing cumulative usage from active context.
- The 250K target guides the agents implementing these issues. Configurable runtime context controls and empirical comparison belong to the early live-backend experiment below; this document does not claim that a new hard runtime cap has already been implemented.

## Worker handoff

Start from the latest integrated prerequisite work. Read the current interface and evidence needed for this issue rather than replaying prior development conversations. Work on this issue's acceptance behavior and test at the public CLI/Git/report seam described by the spec.

Return a compact report with the outcome, commit references/changed files, actual check commands and exit results, and remaining decisions or risks. Preserve verbose logs as artifacts and link to them when needed.

During approved harness execution, source specs and tickets remain unchanged and the harness owns execution records. A ready-for-agent label or published ticket alone does not start a run. Concurrency, arbitrary interruption/crash recovery, hosted PRs, and email remain deferred. Planned-QA checkpoint stop/continuation is implemented by ticket 15; development M1 is accepted, while later milestones and final feature acceptance remain pending.

## Review records

Apply [development architecture checkpoints](../../docs/agents/review-records.md#architecture-checkpoints)
for ticket risk triggers and milestone readiness. Cumulative work belongs in the
[review index](reviews/README.md); missing/stale assessments and unresolved blockers
remain visible in handoffs. Current cumulative renewal and human M1 acceptance are complete.


Development assessments use the [review index](reviews/README.md) and repo-owned
[record contract/templates](../../docs/agents/review-records.md). Ticket 16's
[isolated example](evidence/ticket-16/16-miniature/README.md) shows finding histories and
source-specific decisions with synthetic reviewers/human decisions; it supplies
no real review result or milestone acceptance.

## Early context-budget experiment

[41: Compare configurable 100K–250K agent context limits](issues/41-compare-configurable-agent-context-limits.md) is ready for execution immediately after issue 40 supplies the verified real Codex cycle, configured roles, and usage artifacts. Prioritize it then; it does not require the final release demonstration, multi-ticket scheduling, the planning skill, or the later access-boundary probes. It is a separate early experiment, not an additional first-release completion gate.

The user requested configurable per-agent limits of **100K, 150K, 200K, and 250K**. Compare the same workload, model, role reasoning settings, and acceptance checks at each setting. Record verified results, repair behavior, observed active context, compaction/handoff behavior, elapsed time, and cumulative/cached usage separately.

Use a short control to verify configuration and reporting, plus a task-relevant case that can approach the configured context thresholds. If all runs remain below 100K, they cannot establish the comparative effects of the larger budgets.

Verify whether the installed backend enforces a hard limit, applies a compaction threshold, or only supports advisory guidance. Report that distinction explicitly rather than interpreting cumulative input totals as window occupancy or claiming unsupported enforcement.

## Completion evidence

- [01: Complete one scripted ticket through every gate — completed](evidence/ticket-01/01-completion.md): implementation `b09e324`, final implementation `1666920`; 8 passing tests and passing checks; separate independent Spec and Standards reviews completed. [Actual fixture observations](evidence/ticket-01/01-fixture-observations.json) and the [ticket completion comment](issues/01-complete-one-scripted-ticket-cycle.md#comments) record the passing and rejected runs. Later tickets and first-release completion remain outstanding.

- [02: Reject invalid requirements before starting work — completed](evidence/ticket-02/02-completion.md): checkpoint `855a4c8`, review fixes `dfdb1a6` and final implementation `b11fd20`; 73 passing tests and passing checks; separate fresh Spec and Standards reviews passed. [Actual CLI/Git observations](evidence/ticket-02/02-fixture-observations.json) and the [ticket completion comment](issues/02-reject-invalid-inputs-before-execution.md#comments) provide criterion-specific evidence. Eligibility validation is complete; dependency scheduling and later-ticket features remain outstanding.

- [03: Reject invalid agent reports and review evidence — completed](evidence/ticket-03/03-completion.md): checkpoint `5b04187`, review fixes `2a27565` and final implementation `07094fa`; 256 passing tests and passing documented checks; independent Spec and Standards reviews passed with no remaining findings. [Actual CLI/Git observations (compact historical results)](evidence/ticket-03/03-scenario-results.json) and the [ticket completion comment](issues/03-validate-agent-reports-and-review-evidence.md#comments) verify all six criteria. Report validation is complete; the subsequent transaction slice is recorded below. Repairs, broader human-decision handling, and later-ticket features remain outstanding.

- [04: Promote only the exact verified candidate — completed](evidence/ticket-04/04-completion.md): checkpoint `dc27eb2`, final implementation/review fixes `8d345bd`; **304 passing tests** and passing documented checks; separate independent Spec and Standards re-reviews passed with no outstanding findings. [16 actual CLI/Git observations (compact historical results)](evidence/ticket-04/04-scenario-results.json) and the [ticket completion comment](issues/04-promote-only-the-verified-candidate.md#comments) verify all six criteria. Approved-input/state integrity, source approval invalidation, and exact candidate promotion are complete within the documented process-boundary limits. Automatic repairs and later-ticket features remain outstanding.

- [05: Repair rejected submissions within a bounded allowance — completed](evidence/ticket-05/05-completion.md): implementation `34a49b7`; **362 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI, and [20 actual CLI/Git observations (compact historical results)](evidence/ticket-05/05-scenario-results.json) passed. Separate fresh Spec and Standards reviews found no issues. All six criteria verify configurable bounded repairs, fresh assignments with preserved rejection evidence, renewed exact-revision gates, and preserved Blocked/incomplete exhaustion. No unchecked criteria or unresolved ticket-05 items remain. Human-decision handling and neighboring later-ticket features remain outstanding.

- [06: Stop for decisions outside approved contracts — completed](evidence/ticket-06/06-completion.md): implementation `dc1018e`; **399 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI run/status, and [19 actual CLI/Git observations (compact historical results)](evidence/ticket-06/06-scenario-results.json) passed. Separate fresh Spec and Standards reviews found no issues; Spec independently passed all 37 decision tests. All five criteria verify validated implementation/either-axis decisions, precise preserved contract/evidence/work handoffs, immediate stopping with repair allowance available, unchanged approved inputs/integration, and matching status/final output with accurate initial/later-repair history. No unchecked criteria or unresolved ticket-06 items remain. Optional-suggestion reporting and other later-ticket features remain outstanding.

- [07: Report optional review suggestions without rework — completed](evidence/ticket-07/07-completion.md): checkpoint `83d361d`; **421 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI and [23 actual CLI/Git observations (compact historical results)](evidence/ticket-07/07-scenario-results.json) passed. Existing runtime behavior satisfied the ticket; 22 new cases and public contracts verify optional-only integration without consuming available repairs, full evidence/revision retention, mixed-finding repairs/exhaustion, changing suggestions across revisions, validation and human-decision compatibility. Separate fresh Spec and Standards reviews found no blockers; Spec independently passed 12 cases. Standards recorded one optional test-fixture consolidation suggestion. All five criteria are verified; no unchecked criteria or required unresolved items remain. Timeouts and neighboring later-ticket features remain outstanding.

- [08: Stop stalled assignments and check processes — completed](evidence/ticket-08/08-completion.md): implementation `fbfc088`; **448 passing tests**, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI passed. [27 actual timeout-test observations plus installed CLI smoke (compact historical results)](evidence/ticket-08/08-scenario-results.json) verify positive stage allowances, inherited process-group/child cleanup, partial output, timeout precedence over report claims/zero leader exits, fresh bounded repairs and exact integration, exhaustion, baseline/environment stopping and durable status evidence. Separate fresh Spec and Standards reviews found no blockers; Spec independently verified background-child cleanup after normal completion. Standards recorded optional S1 about streaming output to reduce memory use. All six criteria are verified; no unchecked criteria or required unresolved items remain. Scheduling/continuation, live Codex/role guidance, OS role enforcement and recovery remain later tickets.

- [09: Execute verified dependencies in a stable order — completed](evidence/ticket-09/09-completion.md): implementation `7f4eac0`; **469 passing tests**, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI graph/status passed. [21 final-suite dependency scenarios and installed graph (compact historical results)](evidence/ticket-09/09-scenario-results.json) and [actual check output (retirement summary)](evidence/ticket-09/README.md#retired-evidence) verify explicit selection, stable numeric ready order, one baseline, current verified integration bases, dependency unlocking only after Done, per-ticket repairs/evidence, and complete run/status states/revisions. Separate fresh Spec and Standards reviews found no blockers or optional suggestions; Spec independently passed three cases. All six criteria are verified; no unchecked criteria or required unresolved items remain. Continuing unrelated work after blocks remains ticket 20; live Codex/role guidance, OS enforcement, concurrency and recovery remain later work.

- [10: Turn one grilling session into an approved plan — completed](evidence/ticket-10/10-completion.md): implementation `70a0122`; custom `grill-to-tickets` and one shared planning reference, upstream unchanged. [Actual checks and independent reviews](evidence/ticket-10/10-checks.log) and [raw isolated planning observations](evidence/ticket-10/10-planning-observations.json) verify joint spec/proposal feedback, targeted confirmation, declined-publication preservation, and an approved five-ticket 2/2/1 QA bundle with worker override. Official skill validation, 14 source links/anchors, 199 example links/anchors and whitespace passed; separate fresh High Spec/Standards reviews each found zero blockers or optional suggestions. Initial example execution and subsequent final-source numbering audits are distinguished in the evidence. All six criteria are verified; runtime/skill compatibility remains ticket 27. Next is ready M1 ticket 11; no milestone acceptance is implied.

- [11: Stop development handoffs at human checkpoints — completed](evidence/ticket-11/11-completion.md): implementation `552fcd6`; both development wrappers now enforce approved milestone/order/prerequisite eligibility and distinguish implementation, QA/waiting and final-acceptance handoffs. [Actual checks (retirement summary)](evidence/ticket-11/README.md#retired-evidence), [static validation](evidence/ticket-11/11-static/) and [three isolated outputs](evidence/ticket-11/11-handoff-observations.json) passed; separate fresh High [Spec](evidence/ticket-11/11-review-spec.md) and [Standards](evidence/ticket-11/11-review-standards.md) reviews found zero blockers or optional suggestions. All six criteria are verified. Upstream/shared planning guidance and unrelated tracker edits are preserved. Next eligible work is M1 ticket 12; M1 and final feature QA remain unaccepted. No runtime capability or acceptance is claimed.

- [12: Execute only the first eligible milestone — completed](evidence/ticket-12/12-completion.md): implementation `14cafef`; optional versioned runtime plans validate/capture fixed membership, final coverage, QA and settings before execution. [499 passing tests and required checks (retirement summary)](evidence/ticket-12/README.md#retired-evidence) and [78 retained final-run observations (compact historical results)](evidence/ticket-12/12-scenario-results.json), including 30 new milestone cases, verify first-group-only feature integration and durable preparation-pending with later tickets unstarted and dev unchanged. Separate fresh High [Spec](evidence/ticket-12/12-review-spec.md) and [Standards](evidence/ticket-12/12-review-standards.md) reviews each found zero blockers or optional suggestions. All five criteria are verified. Ticket 13 is next in M1; candidate preparation, promotion, continuation, and M1/final acceptance remain pending. Captured role settings do not claim live enforcement.

- [13: Present a tested feature-to-dev candidate — completed](evidence/ticket-13/13-completion.md): implementation `19ea4f1`; current feature/dev candidates receive a separate exact regression gate and identity-bound QA request, preserving ticket gates, dev and later-group waiting. [509 passing tests and required checks (retirement summary)](evidence/ticket-13/README.md#retired-evidence) and [88 final-run observations (compact historical results)](evidence/ticket-13/13-scenario-results.json) verify passing/failed/changed-base requests, source/ref invalidation and conflict-resolution renewal requirements. Separate fresh High [Spec](evidence/ticket-13/13-review-spec.md) and [Standards](evidence/ticket-13/13-review-standards.md) reviews found zero blockers; Standards recorded one optional duplicate status assertion cleanup. All five criteria are verified. Ticket 14 is next in M1; approval consumption/promotion, continuation, and M1/final acceptance remain pending. Source-changing resolutions stop for renewed checks/reviews; no automatic conflict-repair orchestration is claimed.

- [14: Consume approval, promote, and continue — completed](evidence/ticket-14/14-completion.md): implementation `29fb556`; exact separate decision matching, indefinite observable QA waits, atomic expected-old dev/feature promotion and ordered next-group execution are complete. [524 passing tests and required checks (retirement summary)](evidence/ticket-14/README.md#retired-evidence) and [103 final observations (compact historical results)](evidence/ticket-14/14-scenario-results.json) verify stale/replayed rejection, preserved external changes, worker/repair authority protection, aligned later work and final-only completion. Separate fresh High [Spec](evidence/ticket-14/14-review-spec.md) and [Standards](evidence/ticket-14/14-review-standards.md) reviews found zero blockers; Standards retained one optional polling-helper consolidation. All six criteria are verified. Ticket 15 is next in M1; planned stop/continuation and M1/final human acceptance remain pending. Scripted fixture decisions do not accept the development milestone.

- [15: Continue after a deliberate QA stop — completed](evidence/ticket-15/15-completion.md): implementation `36ed3e7`, final repair `d11f0bc`; durable QA stop/new-process continuation, exact checkpoint/input/source/evidence/ref validation and exclusive run ownership are complete. [544 passing tests and required checks](evidence/ticket-15/15-repair1-check-results.json), [123 renewed observations](evidence/ticket-15/15-repair1-fixture-observations.json) and installed CLI success/invalidation establish final proof. Separate fresh High [Spec](evidence/ticket-15/15-review-spec.md) and [Standards](evidence/ticket-15/15-review-standards.md) whole-diff reviews each found zero blockers or optional suggestions after STD15-01 was repaired and all required gates renewed. All five criteria are verified. **M1 required work is complete; M1 QA preparation and human acceptance are pending.** No development request/run/candidate/decision exists, and ticket 16/M2 remains gated. Fixture decisions do not accept the development milestone.

- [16: Record review work, findings and decisions — completed](evidence/ticket-16/16-completion.md): implementation `3c8d4ab`; authoritative record contract, four templates and tracker/workflow navigation. [Actual checks](evidence/ticket-16/16-checks.log) passed both skill validators, 316 links/anchors, all six isolated history cases and protected-record/whitespace checks. Separate fresh High [Spec](evidence/ticket-16/16-review-spec.md) and [Standards](evidence/ticket-16/16-review-standards.md) reviews each found zero blockers or optional findings; [real assessment](evidence/ticket-16/README.md#review-assessment) retains source/report identities. All six criteria verified, no unresolved real findings. Next is M1 ticket 17; M1 and final human QA remain unaccepted. Synthetic decisions do not establish actual risk acceptance or reviewer calibration.

- [17: Review ownership across affected modules — completed](evidence/ticket-17/17-completion.md): implementation `4814eab`; shared ownership/scope contract and custom workflow routing, four actual review scenarios with five fresh assignments, seven preserved outputs/supplements and failed D/exact D2 repair history. [Checks](evidence/ticket-17/17-checks.log) passed three skill validators, 94 links/anchors, routing/source identities, 6,228 preserved files and whitespace. Separate fresh High [Spec](evidence/ticket-17/17-review-spec.md) and [Standards](evidence/ticket-17/17-review-standards.md) each found zero blocking or optional findings; [assessment](evidence/ticket-17/README.md#review-assessment) preserves identities and scope. All six criteria verified; no unresolved actual findings or decisions. Next is M1 ticket 18; M1 and final QA remain unaccepted. Finite walkthroughs do not establish broad calibration or runtime delivery.

- [18: Gate development on cumulative architecture review — completed](evidence/ticket-18/18-completion.md): implementation `816aecb`; shared checkpoint contract and existing planning/implementation/review/milestone/handoff routes. [Checks](evidence/ticket-18/18-checks.log) passed both skill validators, 392 links, 6,314 protected paths, source/bundle/report identities, six process and seven guidance observations, and whitespace. Six fresh fixture assignments preserve independently passing A/B, actual cumulative risk blocker and exact clean fix, stale/missing/blocked outcomes and explicitly synthetic deferred-human branch. Separate fresh High [Spec](evidence/ticket-18/18-review-spec.md) and [Standards](evidence/ticket-18/18-review-standards.md) each report zero blocking/optional findings; [assessment](evidence/ticket-18/README.md#review-assessment) preserves exact source and identities. All six criteria verified; no unresolved actual findings or decisions. Next is M1 ticket 19; real M1 cumulative provenance/assessment and human QA remain pending. Finite observations grant no actual human authority, broad calibration or runtime enforcement.

- [19: Evaluate reviewers on known and acceptable designs — completed](evidence/ticket-19/19-completion.md): implementation `e90abb6`, repairs `ce4e57d` and final `8e2c826`. Exact G2/C5 finite corpus meets all six criteria; all five evolving corpora/ten original axis reports and failed trials retained. Final [checks](evidence/ticket-19/19-repair-c5-checks.log) pass three official skill validators, syntax, 182 links and 6742 protected paths, with one precisely documented immutable raw EOF exception. Final fresh High [Spec](evidence/ticket-19/19-review-spec-03.md) and [Standards](evidence/ticket-19/19-review-standards-03.md) each 0 new blockers/0 optional, both actual full keys independently fixed. [Assessment/history](evidence/ticket-19/README.md#review-assessment) retains all three rounds. New [evaluate-reviewers skill](../../.agents/skills/custom/evaluate-reviewers/SKILL.md) is the conditional authoring workflow reached through [evaluated guidance/lessons](../../.agents/skills/custom/evaluate-reviewers/SKILL.md#repository-evaluation-history), not an ordinary source-review or runtime gate. No unresolved actual findings/criteria. Next 20 has completed 05/06/19; real M1 cumulative assessment and human QA remain pending.


- [20: Own implementation-attempt transitions — completed](evidence/ticket-20/20-completion.md):
  implementation `0aa2660505e4233ca2e321cee439ba51b150e055`; **544 passed in
  703.66s**, strict mypy, Ruff lint/format and whitespace passed. No tests added.
  [Independent assessment](evidence/ticket-20/README.md#review-assessment): Spec 0 blocking/0 optional;
  Standards 0 blocking/0 optional, with immutable originals, exact source identities
  and explicit no-finding history. All seven criteria verified; no unresolved key
  or pending relevant revalidation. Baseline-code checkpoint continued under final
  source; original capture loss and renewed producer timing are retained. All four
  start/final triggers No. M1 still requires 21–24, actual cumulative assessment
  and human QA; no acceptance or promotion inferred.

- [21: Own ticket execution and bounded repairs — completed](evidence/ticket-21/21-completion.md):
  implementation `10b7050ec1fc06767e473b90217fa0d0bd100a0f`; **544 passed in
  775.37s**, strict mypy, Ruff lint/format and whitespace passed. No tests changed.
  [Independent assessment](evidence/ticket-21/README.md#review-assessment): Spec 0 blocking/0 optional;
  Standards 0 blocking/0 optional, with immutable originals and explicit no-finding
  history. All seven criteria verified; no unresolved actual key or pending relevant
  revalidation. Genuine pre-edit checkpoint continued under final source; both
  live Git fixture archives retained. All four start/final triggers independently No.
  Next 22 has completed 02/12/19; M1 still requires 22–24, actual cumulative
  provenance/all-package assessment and explicit human QA. No acceptance or promotion inferred.

- [22: Return clearly prepared inputs — completed](evidence/ticket-22/22-completion.md):
  implementation `33fa0ea6e667a3879564ed4628c10f6d59ada21b`; **544 passed in 709.21s**,
  strict mypy, Ruff lint/format and whitespace passed. All26 tested identities
  match committed source;10446 raw files retained/streamed.
  [Independent assessment](evidence/ticket-22/README.md#review-assessment): separate Spec and Standards each
  0 blocking/0 optional, originals and explicit history preserved. All seven
  criteria verified; genuine baseline checkpoint continued under final source.
  All four start/final triggers independently No; no unresolved actual key or
  pending relevant revalidation. Next23 has completed15/21/22. M1 still requires
  23–24, cumulative feature-start/all-package assessment and explicit human QA.

- [23: Own the complete run lifecycle — completed](evidence/ticket-23/23-completion.md):
  implementation `8b1b37becb544299e8981144e4ad56da42e2d45f`; **544 passed in
  706.22s**, strict mypy, Ruff lint/format and both whitespace checks passed.
  [Independent assessment](evidence/ticket-23/README.md#review-assessment): Spec 0 blocking / 0 optional;
  Standards 0 blocking / 0 optional, originals captured before aggregation.
  All seven criteria verified; no unresolved actual key or pending relevant
  revalidation. Genuine pre-edit checkpoint continued under exact final source;
  interrupted captures retain no-pass limits. All four start/final triggers
  independently No. Next is M1 ticket 24, backed by completed 15 and 23;
  actual M1 cumulative work and human QA remain unperformed.

- [24: Own milestone review and checkpoint continuation — completed](evidence/ticket-24/24-completion.md): final reviewed source `ab08f7f`;559 passed/1284.57s, strict mypy, Ruff lint/format and whitespace passed. Independent fresh High Spec0/0 and Standards0/0; all3 prior full keys independently fixed, originals/history preserved. Genuine pre-refactor checkpoint renewed; no unchecked criterion. All four start/final triggersNo. All M1 tickets10–24 complete; feature-start/cumulative all-package assessment and actual human QA remain absent. Next is M1 preparation/waiting; M2 remains ineligible.

## M1 acceptance — 2026-11-16

[Human QA decision](evidence/m1-final-review-01/m1-qa-decision.md) accepts source
`88e4cd8aabc78e76e66efc02983fec3900ab0a23` and development request
`41a556a9352d44a3922a9c41f30f36af` after the explicit final condition passed.
[Mechanical acceptance result](evidence/m1-final-review-01/m1-acceptance-result.json)
retains both exact final refs, exit0/completed/true, two consumed actual human
demo approvals and no baseline/attempt/gate/agent-launch replay.

Caller-index repair `e06eeaf` is independently fixed. Fresh High Spec, Standards
and all-package cumulative Standards each report zero blocking/optional findings;
[originals and identities](evidence/m1-final-review-01/README.md),
[cumulative assessment](reviews/M1-architecture-01.md),
[repair assessment](reviews/M1-architecture-01.md#caller-index-repair-assessment),
[append-only finding history](reviews/M1-architecture-01-history.md).
All 28 executable/test/configuration hashes match retained 563/full and static
passes. The reviewed instruction snapshot and later status-only bookkeeping remain
separately identified. Historical completion summaries above preserve their original
then-pending scope, not current acceptance status. M2 ticket25 is next; the overall
feature still requires M2/M3/M4 and final acceptance.

## Ticket 25 capture completion

2026-11-16: [25: Guide ticket and shared evidence creation — completed](evidence/ticket-25/25-completion.md)
at `febd86321851e2acec994237f9d1a1adea824c55`, original checkpoint `3b0c1ab` and
fixed baseline `2c01fe9`. All seven criteria pass; 589/full tests and strict
type/lint/format/whitespace, skill/routing/link and installed checks pass. An
interrupted terminal's three completed checks were preserved and reused only
after exact-input hash verification; remaining gates completed separately.
Fresh independent Spec02, Standards02 and triggered all-package Standards02
each report zero new blocking/optional findings. All five original full keys are
independently fixed; [review index](reviews/README.md) and
[append-only history](evidence/ticket-25/25-finding-history.md) retain provenance.
The current evidence-policy-1 planning bundle remains separately supplied workspace
input; this scoped completion does not publish unrelated planning/archive edits.
Ticket26 is next within EC1, without starting it. Future cumulative EC1 review and
actual human acceptance after25–26 still gate27; the earlier M1 summary's M2/old25
next-step wording above retains its historical context. No EC1 acceptance, evidence
deletion, promotion or push occurred.
