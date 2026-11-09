# Ticket harness — proposed OOP amendment

**Draft — unapproved. Plan version:** oop-v1. [Complete proposal and change summary](ticket-proposal.md#change-summary). Publication approval is pending; this draft does not replace the current approved authoring files.

| Document | Review purpose |
| --- | --- |
| [spec.md](spec.md) | Complete requirements carried forward with ownership, compatibility and verification contracts. |
| [ticket-proposal.md](ticket-proposal.md) | Complete bodies for every proposed open ticket 16–31, dependencies and defaults. |
| [milestones.md](milestones.md) | Fixed membership, actionable QA and final cumulative acceptance. |
| [numbering map](numbering-map.md) | Requested sequential renumbering and history/publication scope. |

## Implementation status

Tickets 01–15 remain complete with their original identities and evidence. This draft adds three unimplemented tickets, 16–18, and shifts the 13 existing open tickets to 19–31: 16 open tickets total. M1 has six completed tickets (10–15) and three proposed open tickets (16–18). M1 human QA has not been requested or accepted. No M2 ticket is eligible before M1 acceptance.

After approval/publication, the next proposed implementation is 16; 17 follows its verified attempt-lifecycle prerequisite, while 18 follows completed 15 and is third in preferred order. Planning approval does not start any implementation or harness run.

## Complete ticket index

| ID and title | Prerequisites | Readiness/completion | Milestone |
| --- | --- | --- | --- |
| [01: Complete one scripted ticket through every gate](../../issues/01-complete-one-scripted-ticket-cycle.md) | None | completed | Completed baseline |
| [02: Reject invalid requirements before starting work](../../issues/02-reject-invalid-inputs-before-execution.md) | 01 | completed | Completed baseline |
| [03: Reject invalid agent reports and review evidence](../../issues/03-validate-agent-reports-and-review-evidence.md) | 01 | completed | Completed baseline |
| [04: Promote only the exact verified candidate](../../issues/04-promote-only-the-verified-candidate.md) | 01 | completed | Completed baseline |
| [05: Repair rejected submissions within a bounded allowance](../../issues/05-repair-rejected-submissions-within-budget.md) | 03, 04 | completed | Completed baseline |
| [06: Stop for decisions outside approved contracts](../../issues/06-surface-human-decisions-without-retrying.md) | 05 | completed | Completed baseline |
| [07: Report optional review suggestions without rework](../../issues/07-report-optional-suggestions-without-repair.md) | 05 | completed | Completed baseline |
| [08: Stop stalled assignments and check processes](../../issues/08-stop-timed-out-process-trees.md) | 05 | completed | Completed baseline |
| [09: Execute verified dependencies in a stable order](../../issues/09-execute-dependencies-sequentially.md) | 02 | completed | Completed baseline |
| [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md) | 09 | completed | M1 |
| [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md) | 10 | completed | M1 |
| [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md) | 10 | completed | M1 |
| [13: Present a tested feature-to-dev candidate](../../issues/13-prepare-a-tested-feature-to-dev-candidate.md) | 12 | completed | M1 |
| [14: Consume approval, promote, and continue](../../issues/14-promote-only-the-human-approved-milestone.md) | 13 | completed | M1 |
| [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md) | 14 | completed | M1 |
| [16: Own implementation-attempt transitions](ticket-proposal.md#16-own-implementation-attempt-transitions) | 05, 06 | ready-for-agent (proposed) | M1 |
| [17: Own ticket execution and bounded repairs](ticket-proposal.md#17-own-ticket-execution-and-bounded-repairs) | 16 | ready-for-agent (proposed) | M1 |
| [18: Own milestone review and checkpoint continuation](ticket-proposal.md#18-own-milestone-review-and-checkpoint-continuation) | 15 | ready-for-agent (proposed) | M1 |
| [19: Guide a human through milestone QA](ticket-proposal.md#19-guide-a-human-through-milestone-qa) | 10, 14 | ready-for-agent (proposed) | M2 |
| [20: Propose a versioned correction plan](ticket-proposal.md#20-propose-a-versioned-correction-plan) | 10, 19 | ready-for-agent (proposed) | M2 |
| [21: Execute approved QA corrections](ticket-proposal.md#21-execute-approved-qa-corrections) | 15, 20 | ready-for-agent (proposed) | M2 |
| [22: Operate the orchestrator in the background](ticket-proposal.md#22-operate-the-orchestrator-in-the-background) | 15 | ready-for-agent (proposed) | M2 |
| [23: Continue independent work inside the current milestone](ticket-proposal.md#23-continue-independent-work-inside-the-current-milestone) | 12, 06 | ready-for-agent (proposed) | M2 |
| [24: Supply coherent design guidance to Standards review](ticket-proposal.md#24-supply-coherent-design-guidance-to-standards-review) | 03 | ready-for-agent (proposed) | M3 |
| [25: Capture and deliver selected local skills](ticket-proposal.md#25-capture-and-deliver-selected-local-skills) | 10, 24 | ready-for-agent (proposed) | M3 |
| [26: Deliver focused implementation and Spec contexts](ticket-proposal.md#26-deliver-focused-implementation-and-spec-contexts) | 25 | ready-for-agent (proposed) | M3 |
| [27: Complete the workflow with real Codex roles](ticket-proposal.md#27-complete-the-workflow-with-real-codex-roles) | 15, 26, 08 | ready-for-agent (proposed) | M3 |
| [28: Run the early context-budget comparison](ticket-proposal.md#28-run-the-early-context-budget-comparison) | 27 | ready-for-agent (proposed) | E1 |
| [29: Verify runtime write and approval boundaries](ticket-proposal.md#29-verify-runtime-write-and-approval-boundaries) | 19, 27 | ready-for-agent (proposed) | M4 |
| [30: Run a generated approved plan through the runtime](ticket-proposal.md#30-run-a-generated-approved-plan-through-the-runtime) | 10, 21, 25 | ready-for-agent (proposed) | M4 |
| [31: Demonstrate the revised first usable release](ticket-proposal.md#31-demonstrate-the-revised-first-usable-release) | 11, 22, 23, 29, 30, 07 | ready-for-agent (proposed) | M4 |

Readiness is separate from dependency satisfaction and milestone eligibility. [Milestones](milestones.md) give preferred order: M1 10–18, M2 19–23, M3 24–27, independent E1 28 immediately after verified 27, then M4 29–31 subject to M3 acceptance. M4 requires final cumulative human acceptance of all required release work. E1 never gates release.

## History

The [prior authoring bundle](../../README.md) and [numbering map](numbering-map.md) preserve predecessor identities and approval scope. At publication archive the prior canonical documents and 13 open issue bodies before replacing their live authoring locations. Keep completed issue bodies, captured inputs, evidence and historical decision text unchanged. Current owner links may be updated without rewriting historical identities.

The completion evidence below is carried forward verbatim. Its next-ticket and milestone-state statements describe the time of that completion; this index's current Implementation status and versioned milestones govern new work.

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

During approved harness execution, source specs and tickets remain unchanged and the harness owns execution records. A ready-for-agent label or published ticket alone does not start a run. Concurrency, arbitrary interruption/crash recovery, hosted PRs, and email remain deferred. Planned-QA checkpoint stop/continuation is implemented by ticket 15; development M1 and final feature human acceptance remain pending.

## Early context-budget experiment

[28: Compare configurable 100K–250K agent context limits](ticket-proposal.md#28-run-the-early-context-budget-comparison) is ready for execution immediately after issue 27 supplies the verified real Codex cycle, configured roles, and usage artifacts. Prioritize it then; it does not require the final release demonstration, multi-ticket scheduling, the planning skill, or the later access-boundary probes. It is a separate early experiment, not an additional first-release completion gate.

The user requested configurable per-agent limits of **100K, 150K, 200K, and 250K**. Compare the same workload, model, role reasoning settings, and acceptance checks at each setting. Record verified results, repair behavior, observed active context, compaction/handoff behavior, elapsed time, and cumulative/cached usage separately.

Use a short control to verify configuration and reporting, plus a task-relevant case that can approach the configured context thresholds. If all runs remain below 100K, they cannot establish the comparative effects of the larger budgets.

Verify whether the installed backend enforces a hard limit, applies a compaction threshold, or only supports advisory guidance. Report that distinction explicitly rather than interpreting cumulative input totals as window occupancy or claiming unsupported enforcement.

## Completion evidence

- [01: Complete one scripted ticket through every gate — completed](../../evidence/01-completion.md): implementation `b09e324`, final implementation `1666920`; 8 passing tests and passing checks; separate independent Spec and Standards reviews completed. [Actual fixture observations](../../evidence/01-fixture-observations.json) and the [ticket completion comment](../../issues/01-complete-one-scripted-ticket-cycle.md#comments) record the passing and rejected runs. Later tickets and first-release completion remain outstanding.

- [02: Reject invalid requirements before starting work — completed](../../evidence/02-completion.md): checkpoint `855a4c8`, review fixes `dfdb1a6` and final implementation `b11fd20`; 73 passing tests and passing checks; separate fresh Spec and Standards reviews passed. [Actual CLI/Git observations](../../evidence/02-fixture-observations.json) and the [ticket completion comment](../../issues/02-reject-invalid-inputs-before-execution.md#comments) provide criterion-specific evidence. Eligibility validation is complete; dependency scheduling and later-ticket features remain outstanding.

- [03: Reject invalid agent reports and review evidence — completed](../../evidence/03-completion.md): checkpoint `5b04187`, review fixes `2a27565` and final implementation `07094fa`; 256 passing tests and passing documented checks; independent Spec and Standards reviews passed with no remaining findings. [Actual CLI/Git observations](../../evidence/03-fixture-observations.json) and the [ticket completion comment](../../issues/03-validate-agent-reports-and-review-evidence.md#comments) verify all six criteria. Report validation is complete; the subsequent transaction slice is recorded below. Repairs, broader human-decision handling, and later-ticket features remain outstanding.

- [04: Promote only the exact verified candidate — completed](../../evidence/04-completion.md): checkpoint `dc27eb2`, final implementation/review fixes `8d345bd`; **304 passing tests** and passing documented checks; separate independent Spec and Standards re-reviews passed with no outstanding findings. [16 actual CLI/Git observations](../../evidence/04-fixture-observations.json) and the [ticket completion comment](../../issues/04-promote-only-the-verified-candidate.md#comments) verify all six criteria. Approved-input/state integrity, source approval invalidation, and exact candidate promotion are complete within the documented process-boundary limits. Automatic repairs and later-ticket features remain outstanding.

- [05: Repair rejected submissions within a bounded allowance — completed](../../evidence/05-completion.md): implementation `34a49b7`; **362 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI, and [20 actual CLI/Git observations](../../evidence/05-fixture-observations.json) passed. Separate fresh Spec and Standards reviews found no issues. All six criteria verify configurable bounded repairs, fresh assignments with preserved rejection evidence, renewed exact-revision gates, and preserved Blocked/incomplete exhaustion. No unchecked criteria or unresolved ticket-05 items remain. Human-decision handling and neighboring later-ticket features remain outstanding.

- [06: Stop for decisions outside approved contracts — completed](../../evidence/06-completion.md): implementation `dc1018e`; **399 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI run/status, and [19 actual CLI/Git observations](../../evidence/06-fixture-observations.json) passed. Separate fresh Spec and Standards reviews found no issues; Spec independently passed all 37 decision tests. All five criteria verify validated implementation/either-axis decisions, precise preserved contract/evidence/work handoffs, immediate stopping with repair allowance available, unchanged approved inputs/integration, and matching status/final output with accurate initial/later-repair history. No unchecked criteria or unresolved ticket-06 items remain. Optional-suggestion reporting and other later-ticket features remain outstanding.

- [07: Report optional review suggestions without rework — completed](../../evidence/07-completion.md): checkpoint `83d361d`; **421 passing tests**, strict mypy, Ruff lint/format, whitespace, packaging/installed CLI and [23 actual CLI/Git observations](../../evidence/07-fixture-observations.json) passed. Existing runtime behavior satisfied the ticket; 22 new cases and public contracts verify optional-only integration without consuming available repairs, full evidence/revision retention, mixed-finding repairs/exhaustion, changing suggestions across revisions, validation and human-decision compatibility. Separate fresh Spec and Standards reviews found no blockers; Spec independently passed 12 cases. Standards recorded one optional test-fixture consolidation suggestion. All five criteria are verified; no unchecked criteria or required unresolved items remain. Timeouts and neighboring later-ticket features remain outstanding.

- [08: Stop stalled assignments and check processes — completed](../../evidence/08-completion.md): implementation `fbfc088`; **448 passing tests**, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI passed. [27 actual timeout-test observations plus installed CLI smoke](../../evidence/08-fixture-observations.json) verify positive stage allowances, inherited process-group/child cleanup, partial output, timeout precedence over report claims/zero leader exits, fresh bounded repairs and exact integration, exhaustion, baseline/environment stopping and durable status evidence. Separate fresh Spec and Standards reviews found no blockers; Spec independently verified background-child cleanup after normal completion. Standards recorded optional S1 about streaming output to reduce memory use. All six criteria are verified; no unchecked criteria or required unresolved items remain. Scheduling/continuation, live Codex/role guidance, OS role enforcement and recovery remain later tickets.

- [09: Execute verified dependencies in a stable order — completed](../../evidence/09-completion.md): implementation `7f4eac0`; **469 passing tests**, strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI graph/status passed. [21 final-suite dependency scenarios and installed graph](../../evidence/09-fixture-observations.json) and [actual check output](../../evidence/09-checks.log) verify explicit selection, stable numeric ready order, one baseline, current verified integration bases, dependency unlocking only after Done, per-ticket repairs/evidence, and complete run/status states/revisions. Separate fresh Spec and Standards reviews found no blockers or optional suggestions; Spec independently passed three cases. All six criteria are verified; no unchecked criteria or required unresolved items remain. Continuing unrelated work after blocks remains ticket 20; live Codex/role guidance, OS enforcement, concurrency and recovery remain later work.

- [10: Turn one grilling session into an approved plan — completed](../../evidence/10-completion.md): implementation `70a0122`; custom `grill-to-tickets` and one shared planning reference, upstream unchanged. [Actual checks and independent reviews](../../evidence/10-checks.log) and [raw isolated planning observations](../../evidence/10-planning-observations.json) verify joint spec/proposal feedback, targeted confirmation, declined-publication preservation, and an approved five-ticket 2/2/1 QA bundle with worker override. Official skill validation, 14 source links/anchors, 199 example links/anchors and whitespace passed; separate fresh High Spec/Standards reviews each found zero blockers or optional suggestions. Initial example execution and subsequent final-source numbering audits are distinguished in the evidence. All six criteria are verified; runtime/skill compatibility remains ticket 27. Next is ready M1 ticket 11; no milestone acceptance is implied.

- [11: Stop development handoffs at human checkpoints — completed](../../evidence/11-completion.md): implementation `552fcd6`; both development wrappers now enforce approved milestone/order/prerequisite eligibility and distinguish implementation, QA/waiting and final-acceptance handoffs. [Actual checks](../../evidence/11-checks.log), [static validation](../../evidence/11-static) and [three isolated outputs](../../evidence/11-handoff-observations.json) passed; separate fresh High [Spec](../../evidence/11-review-spec.md) and [Standards](../../evidence/11-review-standards.md) reviews found zero blockers or optional suggestions. All six criteria are verified. Upstream/shared planning guidance and unrelated tracker edits are preserved. Next eligible work is M1 ticket 12; M1 and final feature QA remain unaccepted. No runtime capability or acceptance is claimed.

- [12: Execute only the first eligible milestone — completed](../../evidence/12-completion.md): implementation `14cafef`; optional versioned runtime plans validate/capture fixed membership, final coverage, QA and settings before execution. [499 passing tests and required checks](../../evidence/12-checks.log) and [78 retained final-run observations](../../evidence/12-fixture-observations.json), including 30 new milestone cases, verify first-group-only feature integration and durable preparation-pending with later tickets unstarted and dev unchanged. Separate fresh High [Spec](../../evidence/12-review-spec.md) and [Standards](../../evidence/12-review-standards.md) reviews each found zero blockers or optional suggestions. All five criteria are verified. Ticket 13 is next in M1; candidate preparation, promotion, continuation, and M1/final acceptance remain pending. Captured role settings do not claim live enforcement.

- [13: Present a tested feature-to-dev candidate — completed](../../evidence/13-completion.md): implementation `19ea4f1`; current feature/dev candidates receive a separate exact regression gate and identity-bound QA request, preserving ticket gates, dev and later-group waiting. [509 passing tests and required checks](../../evidence/13-checks.log) and [88 final-run observations](../../evidence/13-fixture-observations.json) verify passing/failed/changed-base requests, source/ref invalidation and conflict-resolution renewal requirements. Separate fresh High [Spec](../../evidence/13-review-spec.md) and [Standards](../../evidence/13-review-standards.md) reviews found zero blockers; Standards recorded one optional duplicate status assertion cleanup. All five criteria are verified. Ticket 14 is next in M1; approval consumption/promotion, continuation, and M1/final acceptance remain pending. Source-changing resolutions stop for renewed checks/reviews; no automatic conflict-repair orchestration is claimed.

- [14: Consume approval, promote, and continue — completed](../../evidence/14-completion.md): implementation `29fb556`; exact separate decision matching, indefinite observable QA waits, atomic expected-old dev/feature promotion and ordered next-group execution are complete. [524 passing tests and required checks](../../evidence/14-checks.log) and [103 final observations](../../evidence/14-fixture-observations.json) verify stale/replayed rejection, preserved external changes, worker/repair authority protection, aligned later work and final-only completion. Separate fresh High [Spec](../../evidence/14-review-spec.md) and [Standards](../../evidence/14-review-standards.md) reviews found zero blockers; Standards retained one optional polling-helper consolidation. All six criteria are verified. Ticket 15 is next in M1; planned stop/continuation and M1/final human acceptance remain pending. Scripted fixture decisions do not accept the development milestone.

- [15: Continue after a deliberate QA stop — completed](../../evidence/15-completion.md): implementation `36ed3e7`, final repair `d11f0bc`; durable QA stop/new-process continuation, exact checkpoint/input/source/evidence/ref validation and exclusive run ownership are complete. [544 passing tests and required checks](../../evidence/15-repair1-check-results.json), [123 renewed observations](../../evidence/15-repair1-fixture-observations.json) and installed CLI success/invalidation establish final proof. Separate fresh High [Spec](../../evidence/15-review-spec.md) and [Standards](../../evidence/15-review-standards.md) whole-diff reviews each found zero blockers or optional suggestions after STD15-01 was repaired and all required gates renewed. All five criteria are verified. **M1 required work is complete; M1 QA preparation and human acceptance are pending.** No development request/run/candidate/decision exists, and ticket 16/M2 remains gated. Fixture decisions do not accept the development milestone.

## Supporting publication updates

The [exact live-reference and handoff changes](publication-updates.md) are also part of this review bundle. Their source files remain unchanged pending approval.
