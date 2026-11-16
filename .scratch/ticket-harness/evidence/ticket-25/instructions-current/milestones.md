# Development milestones — evidence policy and operator workflow

**Approved plan version:** evidence-policy-1. **Base:** oop-v2 / review-process-1.

**Ticket publication decision:** [Human instruction and scope](README.md#ticket-publication-decision).

## Eligibility and decisions

M1 is accepted. EC1 is the next required group, followed by EC2, EC3, M2, M3 and M4. Every later required group waits for actual human acceptance of its predecessor. Tickets Done, evidence review and source-review completion are separate from milestone acceptance. Before each QA readiness claim, apply the [development architecture checkpoint contract](../../docs/agents/review-records.md#architecture-checkpoints), preserving accepted-baseline provenance and outstanding findings.

## Required release membership

| Milestone | Required tickets | Entry gate |
| --- | --- | --- |
| M1 | [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Record review work, findings and decisions](issues/16-record-review-work-findings-and-decisions.md), [17: Review ownership across affected modules](issues/17-review-ownership-across-affected-modules.md), [18: Gate development on cumulative architecture review](issues/18-gate-development-on-cumulative-architecture-review.md), [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md), [20: Own implementation-attempt transitions](issues/20-own-implementation-attempt-transitions.md), [21: Own ticket execution and bounded repairs](issues/21-own-ticket-execution-and-bounded-repairs.md), [22: Return clearly prepared inputs](issues/22-return-clearly-prepared-inputs.md), [23: Own the complete run lifecycle](issues/23-own-the-complete-run-lifecycle.md), [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md) | Already accepted; preserve original decision |
| EC1 | [25: Guide ticket and shared evidence creation](issues/25-guide-ticket-and-shared-evidence-creation.md), [26: Review and safely retire routine ticket evidence](issues/26-review-and-safely-retire-routine-ticket-evidence.md) | Accepted M1 |
| EC2 | [27: Assess evidence in parallel and consolidate fresh review](issues/27-assess-evidence-in-parallel-and-consolidate-fresh-review.md) | Accepted EC1 |
| EC3 | [28: Guide human review of summaries and proposed merges](issues/28-guide-human-review-of-summaries-and-proposed-merges.md), [29: Reassess retained evidence during ticket completion](issues/29-reassess-retained-evidence-during-ticket-completion.md), [30: Calibrate and adopt the complete evidence workflow](issues/30-calibrate-and-adopt-the-complete-evidence-workflow.md) | Accepted EC2 |
| M2 | [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md), [32: Propose a versioned correction plan](issues/32-propose-versioned-qa-corrections.md), [33: Execute approved QA corrections](issues/33-execute-approved-qa-corrections.md), [34: Operate the orchestrator in the background](issues/34-operate-the-harness-in-the-background.md), [35: Continue independent work inside the current milestone](issues/35-continue-independent-work-after-blocks.md) | Accepted EC3 |
| M3 | [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md), [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md), [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md), [39: Enforce traceable runtime review checkpoints](issues/39-enforce-traceable-runtime-review-checkpoints.md), [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md) | Accepted M2 |
| M4 | [42: Verify runtime write and approval boundaries](issues/42-verify-role-write-boundaries.md), [43: Run a generated approved plan through the runtime](issues/43-run-a-generated-plan-through-the-runtime.md), [44: Demonstrate the revised first usable release](issues/44-demonstrate-the-first-usable-release.md) | Accepted M3 |

Every required ticket 10–40 and 42–44 has exactly one required membership (34 tickets). Completed baseline 01–09 remains unchanged. E1 contains only 41, independently after verified 40 and not as a release gate. M4 is final cumulative acceptance of the prior harness outcomes and new evidence feature; automatic runtime cleanup remains outside this amendment.

## M1: A complete QA-controlled Git cycle

**Required tickets:** [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Record review work, findings and decisions](issues/16-record-review-work-findings-and-decisions.md), [17: Review ownership across affected modules](issues/17-review-ownership-across-affected-modules.md), [18: Gate development on cumulative architecture review](issues/18-gate-development-on-cumulative-architecture-review.md), [19: Evaluate reviewers on known and acceptable designs](issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md), [20: Own implementation-attempt transitions](issues/20-own-implementation-attempt-transitions.md), [21: Own ticket execution and bounded repairs](issues/21-own-ticket-execution-and-bounded-repairs.md), [22: Return clearly prepared inputs](issues/22-return-clearly-prepared-inputs.md), [23: Own the complete run lifecycle](issues/23-own-the-complete-run-lifecycle.md), [24: Own milestone review and checkpoint continuation](issues/24-own-milestone-review-and-checkpoint-continuation.md)

**QA status:** **Accepted 2026-11-16** for source
`88e4cd8aabc78e76e66efc02983fec3900ab0a23`, development request
`41a556a9352d44a3922a9c41f30f36af`.
[Actual human decisions and fulfilled condition](evidence/m1-final-review-01/m1-qa-decision.md),
[exact promotion/completion/no-replay result](evidence/m1-final-review-01/m1-acceptance-result.json).
Human code/documentation review was completed earlier. Caller-index F1 is
independently fixed, all required reviews/checks pass, and the fresh two-milestone
demo completed only after both actual exact-request human approvals. M2 is now
eligible; no M2 implementation has started.

**QA setup:** Use an isolated miniature tracker and actual development reviewer evaluation artifacts, then a disposable foreground scripted two-milestone target repository with the refactored final source. Include the nine new ticket outcomes, genuine pre-refactor checkpoint evidence and a cumulative all-file architecture assessment.

**Human actions:** Follow a review concern through its immutable report, human/agent disposition, repair ticket/commit and verification. Inspect all declared evaluation cases, misses/false positives and guidance versions. Confirm risk-triggered/milestone assessments expose unresolved work, clean reviews progress, and changed source invalidates stale assessments. Inspect ownership reports for refactors 20–24. Then demonstrate first-group feature integration, exact tested QA request, stale-approval rejection, deliberate stop/new-process continuation without replay, exact human approval/promotion and final-only completion. Inspect invalid-input/failed-baseline and canonical restored-evidence invalidation observations.

**Pass conditions:** All M1 work is verified; review records explain why code changed, meaningful decisions remain human-owned, the declared reviewer corpus meets its criteria, and cumulative architecture assessment has no unresolved in-scope blocker. Existing CLI/record/checkpoint compatibility and exact QA behavior remain intact. Scripted approvals and review completion do not accept the development milestone.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.


## EC1: A small working capture-to-deletion path

**Required membership:** [25: Guide ticket and shared evidence creation](issues/25-guide-ticket-and-shared-evidence-creation.md), [26: Review and safely retire routine ticket evidence](issues/26-review-and-safely-retire-routine-ticket-evidence.md). **Entry gate:** accepted M1. **QA state:** not requested/accepted.

**Setup:** Disposable ticket evidence with routine output, protected/unknown files,
a changed file and existing navigation. Use the delivered local tool; do not wait
for the postponed general QA-session skill.

**Human actions:** Label the small sample before agent recommendations are shown.
Inspect saved independent assessor/reviewer choices and compare them with yours.
Preview an eligible deletion and a blocked deletion; explicitly permit execution
only on the isolated trial files. Inspect retained result/source identity and the
actual deletion/navigation record. Verify missing or stale approvals cannot act.
Inspect ticket 26's actual execution-host, architecture, source/environment and
resource-selection evidence under the current ADAPT policy; historical results
are not relabeled as new-policy verification.

**Pass conditions:** Useful eligible deletion works, protected/unknown content
survives, and actual results match recorded state. Explain or correct disagreements
in the early sample; disputed files stay. An agent cannot accept this milestone.

**Acceptance evidence:** Exact tested source/tool/criteria and sample identities,
original agent decisions, human labels/comparison, command/results and actual
explicit human development QA decision. No scripted fixture approval suffices.

## EC2: Consistent capture and independent parallel assessment

**Required membership:** [27: Assess evidence in parallel and consolidate fresh review](issues/27-assess-evidence-in-parallel-and-consolidate-fresh-review.md). **Entry gate:** actual human EC1 acceptance.
**QA state:** not requested/accepted.

**Setup:** Disposable ticket and descriptively named shared milestone evidence,
including an embedded review in a log/archive and a dependency across assignments.

**Human actions:** Observe capture routing/provenance and links from relevant
tickets. Supply labels before recommendations are revealed. Inspect separate worker
proposals, fresh reviewer synthesis and the consolidated JSON. Check that the
cross-ticket use and protected mixed-content record are retained. Compare worker
and reviewer choices with yours before approving isolated eligible deletion.

**Pass conditions:** Parallel workers do not overwrite one another, final review
catches remaining relationships, required evidence survives and independently
eligible groups can be retired. Changed/incomplete proposals remain blocked.
Resolve observed disagreements or retain affected items with visible reasons.

**Acceptance evidence:** Exact source, criteria, corpus, assignment/settings and
original judgments, human labels/adjudication, capture/preview/execution outcomes
and explicit human development QA acceptance. Include cumulative EC1 regression
and required architecture assessment; this does not prove unlimited reliability.

## EC3: Guided human review, reassessment and final evidence acceptance

**Required membership:** [28: Guide human review of summaries and proposed merges](issues/28-guide-human-review-of-summaries-and-proposed-merges.md), [29: Reassess retained evidence during ticket completion](issues/29-reassess-retained-evidence-during-ticket-completion.md), [30: Calibrate and adopt the complete evidence workflow](issues/30-calibrate-and-adopt-the-complete-evidence-workflow.md). **Entry gate:** actual human EC2 acceptance.
**QA state:** not requested/accepted. **Final coverage:** all new tickets 25–30
and the complete accepted evidence spec, including EC1/EC2 capabilities.

**Setup:** Representative isolated evidence and the full local workflow, an
agent-prepared merge, a later-ticket reassessment and unresolved milestone choice.

**Human actions:** Review small related batches, inspect proposed merged content
and omissions, request a correction, defer an item, pause/resume and approve a
corrected merge. Follow a ticket-triggered reassessment to resolution and another
to human QA. Compare repeat independent assessments against hidden human labels.
Inspect actual Python execution, protected survivors, honest deleted navigation
and historical-account relocation.

**Pass conditions:** The workflow removes eligible evidence, preserves useful
knowledge and protected originals, makes reassessment visible and limits review
to manageable decisions. Changed proposals require new approval. Cleanup approval
cannot accept software or promote refs. Calibration discloses its finite scope
and remaining limitations. All required implementation and cumulative gates pass.

**Acceptance evidence:** Same-source checks/reviews, cumulative assessment with
the correct accepted baseline, criteria/corpus identities, actual agent and human
judgments, resumable review decisions and execution outcomes, plus explicit human
development acceptance. Unresolved cleanup choices can remain protected; unresolved
implementation blockers cannot be concealed by deferring their evidence.


## M2: An unattended operator workflow

**Required tickets:** [31: Guide a human through milestone QA](issues/31-guide-and-record-human-milestone-qa.md), [32: Propose a versioned correction plan](issues/32-propose-versioned-qa-corrections.md), [33: Execute approved QA corrections](issues/33-execute-approved-qa-corrections.md), [34: Operate the orchestrator in the background](issues/34-operate-the-harness-in-the-background.md), [35: Continue independent work inside the current milestone](issues/35-continue-independent-work-after-blocks.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After EC3 acceptance, use QA-session/correction guidance and a disposable plan with independent and dependent work; include a review-originated correction and separate operator sessions.

**Human actions:** Inspect review findings/reasons alongside the candidate, request a correction and approve its amendment without accepting the candidate. Observe renewed QA, terminal-independent background operation, accurate status/logs, blocked-root/unrelated-success behavior, and cumulative architecture assessment before M2 QA.

**Pass conditions:** Review dispositions, correction approval and exact candidate acceptance remain distinct. Background status is observational, independent work respects prerequisite/milestone gates, and significant unresolved findings prevent readiness under the shared review contract.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.


## M3: Real agents with explicit guidance

**Required tickets:** [36: Supply coherent design guidance to Standards review](issues/36-supply-combined-design-guidance-to-standards-review.md), [37: Capture and deliver selected local skills](issues/37-capture-and-deliver-selected-local-skills.md), [38: Deliver focused implementation and Spec contexts](issues/38-deliver-focused-implementation-and-spec-review-contexts.md), [39: Enforce traceable runtime review checkpoints](issues/39-enforce-traceable-runtime-review-checkpoints.md), [40: Complete the workflow with real Codex roles](issues/40-run-a-real-codex-ticket-cycle.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After M2 acceptance, prepare scripted runtime review/decision cases and a tiny real-Codex plan using captured role guidance, a worker override, a seeded concern and an acceptable control.

**Human actions:** Inspect actual captured/delivered ownership/review instructions, inspected scope, immutable reports, finding/decision history and independent role profiles. Observe scripted runtime blocking/stale/authority/continuation cases and a real cumulative assessment plus independent ticket reviews. Verify no consumable QA request appears with unresolved required review work. Schedule E1 immediately after verified 40.

**Pass conditions:** Runtime review enforcement and actual real-agent instruction delivery/judgment are evidenced separately from M1 development evaluation. Human risk decisions and QA acceptance stay separate. E1 never gates release or supplies assumed model/context defaults.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.


## M4: First usable release and final acceptance

**Required tickets:** [42: Verify runtime write and approval boundaries](issues/42-verify-role-write-boundaries.md), [43: Run a generated approved plan through the runtime](issues/43-run-a-generated-plan-through-the-runtime.md), [44: Demonstrate the revised first usable release](issues/44-demonstrate-the-first-usable-release.md)

**QA status:** Not yet requested or accepted.

**QA setup:** After M3 acceptance, start from a clean installed checkout and disposable target with generated-plan and role/access evidence, linked review history and all prior accepted milestone assessments.

**Human actions:** Operate the full planning, execution, review/decision, correction, background/status, deliberate stop/continue and exact QA/promotion cycle. Follow a concern from report through human rationale, implementation revision and independent verification. Inspect review-authority probes, final cumulative architecture assessment, unresolved/deferred findings and documented limitations.

**Pass conditions:** Accepted evidence milestones EC1–EC3 are included cumulatively; automatic runtime cleanup remains out of scope. All required tickets 10–40 and 42–44 and prior milestone acceptances are accounted for cumulatively; the final source has the required architecture assessment, exact tested candidate and explicit final human acceptance. Review completion, all ticket Done states and automated gates alone are insufficient.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.


## E1: Independent early context experiment

**Required tickets:** [41: Run the early context-budget comparison](issues/41-compare-configurable-agent-context-limits.md)

**QA status:** Not yet requested or accepted.

**QA setup:** Immediately after verified 40 supplies the real backend and usage/settings evidence, select experiment 41 independently of release work.

**Human actions:** Review the controlled 100K/150K/200K/250K comparison, pressure case, active versus cumulative/cached usage, compaction behavior and measured quality/limitations. Keep reviewer effectiveness evidence distinct from this context-budget experiment.

**Pass conditions:** Document actual enforcement/compaction/advisory limits and independent experiment acceptance without making E1 a release prerequisite or silently changing role/context defaults.

**Acceptance evidence:** Retain assessed source/feature/development/candidate revisions, plan/run/request identities, actual gate results, cumulative review scope/baseline, immutable reports and finding/decision history, observed human checks and explicit request-specific QA decision. Changed source or accepted corrections require renewed applicable review/candidate checks and human acceptance. Historical fixture decisions are not development milestone acceptance.


## M1 QA preparation history

2026-11-12: human requested beginning QA after ticket24. [Current cumulative work](reviews/M1-architecture-01.md) assesses `d02e61e` from established starting snapshot `1a623ba`; [QA guide/evidence](evidence/m1-qa-01/qa-guide.md) retains the stopped disposable demonstration. Required cumulative assessment completed with open/blocking `review-M1-architecture-01/standards-01/F1`; finding gate unresolved, readiness held, no human acceptance and no M2 authorization. Approved membership, setup, actions and pass conditions above remain unchanged.

2026-11-16: [Fresh exact-source repair reviews and cumulative renewal](evidence/m1-final-review-01/README.md)
completed with zero new blocking/optional findings. [Original cumulative F1 fixed](reviews/M1-architecture-01-history.md#event06--independent-exact-source-repair-verification)
at `88e4cd8`, repair `e06eeaf`; same-source 563/full and required statics retained.
[Fresh candidate/request and human actions](evidence/m1-final-review-01/qa-guide.md)
replace the absent historical live demo. Human code/documentation review remains
complete; no fixture approval or development M1 acceptance is inferred.

2026-11-16: the human approved the first exact demo request, then approved the
final exact demo and conditionally accepted development M1 request
`41a556a9352d44a3922a9c41f30f36af` at `88e4cd8`. Both demo refs advanced exactly
to `2338f88cce672b05ca2fb44127f35ce3659a8cfa`; final continuation exited0 with
completed/true and no replay. [Condition fulfilled; M1 accepted](evidence/m1-final-review-01/m1-qa-decision.md).
This decision admits M2 under approved ordering but starts no later ticket and
accepts no later milestone or final feature release.
