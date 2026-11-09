# Supporting publication updates

**Draft — unapproved. Plan version:** oop-v2. **Draft revision:** review-process-1.

The exact diffs below update current-owner pointers, proposed domain terms and the stale next-agent entry point. Preserve the old root handoff under `archive/before-oop-v2/next_agent_prompt.md` before replacement. Workflow implementation itself belongs to the new tickets, not this publication; upstream skills remain unchanged. Historical identities/evidence are retained, with only current-owner navigation links changed inside older archives.

## GLOSSARY.md

```diff
--- GLOSSARY.md
+++ GLOSSARY.md
@@ -61,3 +61,17 @@
 **Candidate merge**:
 The proposed combination of source changes and a destination branch, evaluated before that destination advances. A ticket candidate targets the feature branch; a milestone candidate targets the development branch.

+**Review work item**:
+An identified assessment of a defined source revision and scope, linked to its reports and outstanding findings. Completing the assessment does not itself resolve its findings or accept a milestone.
+
+**Review report**:
+The preserved result of one reviewer assignment against an identified source and scope, including inspected coverage, findings and unresolved assumptions.
+
+**Finding disposition**:
+The recorded treatment of a review finding, with its reason, authority and supporting evidence. Its history connects the original concern to a verified fix, linked deferral or explicit human decision.
+
+**Review decision**:
+A human's recorded choice about consequential review risk, scope, ownership or deferral. It is separate from a QA decision accepting an exact milestone candidate.
+
+**Architecture checkpoint**:
+A required cumulative assessment of responsibility and invariant ownership across an affected workflow before specified integration or milestone-readiness progression.
```

## docs/ticket-harness.md

```diff
--- docs/ticket-harness.md
+++ docs/ticket-harness.md
@@ -461,7 +461,7 @@
 Success requires every selection to reach Done. This slice stops the run on the
 first blocked ticket or shared environment failure; selected dependents remain
 Pending and unrelated selections retain their observed Ready state. Continuing
-unrelated work after a block belongs to ticket 20. A shared baseline failure
+unrelated work after a block belongs to ticket 29. A shared baseline failure
 launches no workers and consumes no repairs; the compatibility `ticket` entry
 (the configured primary before execution) becomes Blocked and other selections
 retain their pre-baseline states. Integration changes made outside the harness
@@ -609,7 +609,7 @@
 identifies the changed source. A structurally valid review report retains
 `report_status: "valid"`; it cannot approve changed source. This attempt stops;
 renewed checks and reviews are required before integration. These observations
-are not an enforced process sandbox (ticket 26).
+are not an enforced process sandbox (ticket 36).

 The harness creates a real merge candidate with the starting integration
 revision as first parent, tests it, and atomically updates the integration ref
@@ -642,7 +642,7 @@
 Integrity checks observe process boundaries. They do not detect a transient edit
 restored before the process returns, authenticate local artifacts, or prevent a
 process with unrestricted filesystem/Git access from racing observations. Run
-only trusted commands until role access enforcement is supplied by ticket 26.
+only trusted commands until role access enforcement is supplied by ticket 36.

 ## Optional review suggestions

```

## .agents/skills/custom/references/planning.md

```diff
--- .agents/skills/custom/references/planning.md
+++ .agents/skills/custom/references/planning.md
@@ -285,4 +285,4 @@
 any remaining execution prerequisites. This workflow authors approved inputs;
 it does not implement scheduling, branch promotion, approval watching, restart,
 QA execution, background launch, or runtime skill selection. Generated-bundle
-runtime and skill-metadata proof remains ticket 27 in the harness project.
+runtime and skill-metadata proof remains ticket 37 in the harness project.
```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 12; use the [current ticket](../../issues/23-deliver-focused-implementation-and-spec-review-contexts.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/12-deliver-focused-implementation-and-spec-review-contexts.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 12; use the [current ticket](../../issues/32-deliver-focused-implementation-and-spec-review-contexts.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/12-deliver-focused-implementation-and-spec-review-contexts.md`. Relative links were adjusted for this archive location.

 # 12: Deliver focused implementation and Spec-review skills

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 16; use the [current ticket](../../issues/28-demonstrate-the-first-usable-release.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/16-demonstrate-the-first-usable-release.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 16; use the [current ticket](../../issues/38-demonstrate-the-first-usable-release.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/16-demonstrate-the-first-usable-release.md`. Relative links were adjusted for this archive location.

 # 16: Demonstrate the first usable release from a clean checkout

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 17; use the [current ticket](../../issues/25-compare-configurable-agent-context-limits.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/17-compare-configurable-agent-context-limits.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 17; use the [current ticket](../../issues/35-compare-configurable-agent-context-limits.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/17-compare-configurable-agent-context-limits.md`. Relative links were adjusted for this archive location.

 # 17: Compare configurable 100K–250K agent context limits

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 10; use the [current ticket](../../issues/20-continue-independent-work-after-blocks.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/10-continue-independent-work-after-blocks.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 10; use the [current ticket](../../issues/29-continue-independent-work-after-blocks.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/10-continue-independent-work-after-blocks.md`. Relative links were adjusted for this archive location.

 # 10: Continue unrelated tickets after a blocked prerequisite

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 11; use the [current ticket](../../issues/21-supply-combined-design-guidance-to-standards-review.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/11-supply-combined-design-guidance-to-standards-review.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 11; use the [current ticket](../../issues/30-supply-combined-design-guidance-to-standards-review.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/11-supply-combined-design-guidance-to-standards-review.md`. Relative links were adjusted for this archive location.

 # 11: Supply combined Python design guidance to Standards review

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 14; use the [current ticket](../../issues/26-verify-role-write-boundaries.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/14-verify-role-write-boundaries.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 14; use the [current ticket](../../issues/36-verify-role-write-boundaries.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/14-verify-role-write-boundaries.md`. Relative links were adjusted for this archive location.

 # 14: Verify implementation and review access boundaries

```

## .scratch/ticket-harness/archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md

```diff
--- .scratch/ticket-harness/archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md
+++ .scratch/ticket-harness/archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md
@@ -1,6 +1,6 @@
 # Historical ticket definition

-Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 13; use the [current ticket](../../issues/24-run-a-real-codex-ticket-cycle.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/13-run-a-real-codex-ticket-cycle.md`. Relative links were adjusted for this archive location.
+Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 13; use the [current ticket](../../issues/34-run-a-real-codex-ticket-cycle.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/13-run-a-real-codex-ticket-cycle.md`. Relative links were adjusted for this archive location.

 # 13: Complete one real Codex ticket with configured role profiles

```

## .scratch/ticket-harness/archive/ticket-numbering-history.md

```diff
--- .scratch/ticket-harness/archive/ticket-numbering-history.md
+++ .scratch/ticket-harness/archive/ticket-numbering-history.md
@@ -1,4 +1,6 @@
 # Ticket numbering history
+
+Historical IDs and membership retain their earlier meaning. Current-owner links follow the [ownership/review amendment map](oop-numbering-history.md). Use [current milestones](../milestones.md) for eligibility.

 The human requested sequential execution numbers after approving and publishing the QA-first plan. This refactor changes the identities of its 19 unimplemented tickets, preserving their scope, dependencies, acceptance criteria and readiness. Completed tickets 01–09 and their evidence remain unchanged. No implementation or human QA acceptance is implied.

@@ -12,18 +14,18 @@
 | 20 | 13 | R04 | [Present a tested feature-to-dev candidate](../issues/13-prepare-a-tested-feature-to-dev-candidate.md) |
 | 21 | 14 | R05 | [Consume approval, promote, and continue](../issues/14-promote-only-the-human-approved-milestone.md) |
 | 22 | 15 | R06 | [Continue after a deliberate QA stop](../issues/15-continue-from-a-planned-qa-checkpoint.md) |
-| 23 | 16 | R07 | [Guide a human through milestone QA](../issues/16-guide-and-record-human-milestone-qa.md) |
-| 24 | 17 | R08 | [Propose a versioned correction plan](../issues/17-propose-versioned-qa-corrections.md) |
-| 25 | 18 | R09 | [Execute approved QA corrections](../issues/18-execute-approved-qa-corrections.md) |
-| 26 | 19 | R10 | [Operate the orchestrator in the background](../issues/19-operate-the-harness-in-the-background.md) |
-| 10 | 20 | R11 | [Continue independent work inside the current milestone](../issues/20-continue-independent-work-after-blocks.md) |
-| 11 | 21 | R12 | [Supply coherent design guidance to Standards review](../issues/21-supply-combined-design-guidance-to-standards-review.md) |
-| 27 | 22 | R13 | [Capture and deliver selected local skills](../issues/22-capture-and-deliver-selected-local-skills.md) |
-| 12 | 23 | R14 | [Deliver focused implementation and Spec contexts](../issues/23-deliver-focused-implementation-and-spec-review-contexts.md) |
-| 13 | 24 | R15 | [Complete the workflow with real Codex roles](../issues/24-run-a-real-codex-ticket-cycle.md) |
-| 17 | 25 | R16 | [Run the early context-budget comparison](../issues/25-compare-configurable-agent-context-limits.md) |
-| 14 | 26 | R17 | [Verify runtime write and approval boundaries](../issues/26-verify-role-write-boundaries.md) |
-| 28 | 27 | R18 | [Run a generated approved plan through the runtime](../issues/27-run-a-generated-plan-through-the-runtime.md) |
-| 16 | 28 | R19 | [Demonstrate the revised first usable release](../issues/28-demonstrate-the-first-usable-release.md) |
+| 23 | 16 | R07 | [Guide a human through milestone QA](../issues/25-guide-and-record-human-milestone-qa.md) |
+| 24 | 17 | R08 | [Propose a versioned correction plan](../issues/26-propose-versioned-qa-corrections.md) |
+| 25 | 18 | R09 | [Execute approved QA corrections](../issues/27-execute-approved-qa-corrections.md) |
+| 26 | 19 | R10 | [Operate the orchestrator in the background](../issues/28-operate-the-harness-in-the-background.md) |
+| 10 | 20 | R11 | [Continue independent work inside the current milestone](../issues/29-continue-independent-work-after-blocks.md) |
+| 11 | 21 | R12 | [Supply coherent design guidance to Standards review](../issues/30-supply-combined-design-guidance-to-standards-review.md) |
+| 27 | 22 | R13 | [Capture and deliver selected local skills](../issues/31-capture-and-deliver-selected-local-skills.md) |
+| 12 | 23 | R14 | [Deliver focused implementation and Spec contexts](../issues/32-deliver-focused-implementation-and-spec-review-contexts.md) |
+| 13 | 24 | R15 | [Complete the workflow with real Codex roles](../issues/34-run-a-real-codex-ticket-cycle.md) |
+| 17 | 25 | R16 | [Run the early context-budget comparison](../issues/35-compare-configurable-agent-context-limits.md) |
+| 14 | 26 | R17 | [Verify runtime write and approval boundaries](../issues/36-verify-role-write-boundaries.md) |
+| 28 | 27 | R18 | [Run a generated approved plan through the runtime](../issues/37-run-a-generated-plan-through-the-runtime.md) |
+| 16 | 28 | R19 | [Demonstrate the revised first usable release](../issues/38-demonstrate-the-first-usable-release.md) |

-Current groups: M1 = 10–15; M2 = 16–20; M3 = 21–24; E1 = 25 (independent, immediately after 24); M4 = 26–28. Dependencies and human QA acceptance still gate execution. Ticket 25 does not gate release acceptance.
+Groups at that publication: M1 = 10–15; M2 = 16–20; M3 = 21–24; E1 = 25 (independent, immediately after 24); M4 = 26–28. Dependencies and human QA acceptance still gate execution. Ticket 25 does not gate release acceptance.
```

## next_agent_prompt.md

```diff
--- next_agent_prompt.md
+++ next_agent_prompt.md
@@ -1,145 +1,11 @@
-# Awaiting milestone QA — M1 preparation pending
+# Ticket harness — current plan entry point

-Ticket 15 is fully verified and committed. M1's required implementation work is
-complete. **M1 human QA has not been requested or accepted; M2 remains ineligible.**
-This is a checkpoint handoff, not an executable ticket 16 assignment. Creating this
-handoff launches no implementation, candidate preparation, harness run or QA session.
+The published plan is **oop-v2 / review-process-1**: [index](.scratch/ticket-harness/README.md), [spec](.scratch/ticket-harness/spec.md), [proposal](.scratch/ticket-harness/ticket-proposal.md) and [milestones](.scratch/ticket-harness/milestones.md).

-Follow `AGENTS.md`, [tracker conventions](docs/agents/issue-tracker.md),
-[domain guidance](docs/agents/domain.md), [GLOSSARY](GLOSSARY.md), applicable
-[ADRs](docs/adr/), and the
-[shared milestone/approval policy](.agents/skills/custom/references/planning.md#milestone-membership).
-Preserve the worktree and capture the next session's starting HEAD before any
-subsequently authorized work. The unrelated unstaged `docs/agents/issue-tracker.md`
-edit remains, SHA-256
-`3803de99e541e60d2e9f733d5c98b009a43e60a9584e3819adffc55eae0214ce`.
+Completed01–15 keep their evidence. M1 now requires10–24, with new review work16–19 before the five refactors20–24. Human M1 QA is not requested/accepted; M2 remains gated. Next proposed work is [16: Record review work, findings and decisions](.scratch/ticket-harness/issues/16-record-review-work-findings-and-decisions.md), backed by completed10/11. Publication starts no implementation, evaluation, run or QA session.

-## Approved checkpoint and verified work
+When implementation is requested, follow AGENTS.md, the [implementation workflow](.agents/skills/custom/implement-with-checkboxes/SKILL.md) and the selected ticket's scoped contracts. Capture the session's starting HEAD/worktree, verify prerequisite evidence, and retain actual check/review provenance. Apply the strengthened ownership/scope/disposition/checkpoint guidance as its implementing tickets land; do not claim those future capabilities already exist. Carry open review work and unresolved findings without rewriting original reports. Use GPT-6.1 Sol Medium worker/repair, independent High Spec/Standards and cumulative Standards, fresh assignments and the250K active-context target.

-The approved plan is the canonical human-approved milestone-QA realignment in
-[spec.md](.scratch/ticket-harness/spec.md),
-[ticket-proposal.md](.scratch/ticket-harness/ticket-proposal.md),
-[milestones.md](.scratch/ticket-harness/milestones.md), and the
-[feature index](.scratch/ticket-harness/README.md). The development documents do not
-supply a captured machine-readable runtime plan/version or a request-specific QA
-acceptance. Fixture plan version `v1` is synthetic and is not a development run identity.
+After all required M1 work, obtain the source-identified cumulative architecture assessment before human QA readiness. A completed review, finding disposition, ticket Done or scripted approval is not milestone acceptance. Later groups wait for the recorded human QA decision. Runtime review enforcement33 precedes real agents34; independent experiment35 follows verified34 and never gates release.

-M1, **A complete QA-controlled Git cycle**, requires exactly tickets **10, 11, 12,
-13, 14, 15** in the published order. Their verified completion records are:
-
-- [10: Approved planning inputs](.scratch/ticket-harness/evidence/10-completion.md).
-- [11: Development checkpoint handoffs](.scratch/ticket-harness/evidence/11-completion.md).
-- [12: Current milestone execution](.scratch/ticket-harness/evidence/12-completion.md).
-- [13: Tested feature-to-development candidate](.scratch/ticket-harness/evidence/13-completion.md).
-- [14: Exact acceptance, promotion and next group](.scratch/ticket-harness/evidence/14-completion.md).
-- [15: Planned QA stop and continuation](.scratch/ticket-harness/evidence/15-completion.md).
-
-Ticket 15 implementation is `36ed3e72c278cf147c84ae9c282cd2899af23ad0`; final repair
-and verified source is `d11f0bc60a2c11c40683e58581dffa10e36a91be`. Its completion
-bookkeeping is `eb58804f275776f9cce8d3ebd2e3485b7928b0f6`.
-The original review baseline was `90255aaf6faf9aedce18f7159093f5dbfde294b7`;
-historical baselines are not a substitute for a future session's own starting HEAD.
-
-All five ticket 15 criteria are verified. The renewed final suite passed **544 tests
-in 910.17s**; strict mypy, Ruff lint/format, working/staged/committed whitespace,
-pinned wheel, isolated install, and installed continuation/invalidation passed.
-[Final source identity](.scratch/ticket-harness/evidence/15-repair1-final-source-identity.json),
-[actual gates](.scratch/ticket-harness/evidence/15-repair1-check-results.json),
-[123 retained scenarios](.scratch/ticket-harness/evidence/15-repair1-fixture-observations.json)
-and [root audit](.scratch/ticket-harness/evidence/15-repair1-root-audit.json)
-confirm current/committed source and retained evidence. Final fresh High
-[Spec](.scratch/ticket-harness/evidence/15-review-spec.md) and
-[Standards](.scratch/ticket-harness/evidence/15-review-standards.md) reviews each
-found zero blockers and zero optional suggestions. STD15-01 was repaired by a fresh
-Medium assignment and every required gate renewed. Initial 543-test results and
-initial reviews remain historical. No ticket 15 blocker or unchecked criterion remains.
-
-## Development QA inputs still missing
-
-No development M1 runtime QA artifacts have been created. The following remain
-explicitly unavailable:
-
-| Required development QA identity | Current state |
-| --- | --- |
-| Run identity and separate run-output directory | Not created. |
-| Runtime configuration, captured approved plan/version/approval and input snapshots | Not captured for development M1 QA. |
-| Assessed source/feature revision and feature branch | Not recorded for QA; verified implementation above is available for preparation. |
-| Development branch and expected development base | Not selected or recorded. |
-| Exact tested milestone candidate and candidate worktree | Not prepared. |
-| Candidate regression command/result/evidence | No development candidate gate executed. Automated implementation checks above remain separate. |
-| Request ID, current/archived request paths and identity | No development `qa-request.json` exists. |
-| Decision path, human observations and recorded decision | No development decision artifact or acceptance exists. |
-| Promotion/continuation/checkpoint for this development assessment | Not executed or recorded. |
-
-Paths and identities under `15-observations/` and the installed proof are
-**scripted target-repository fixtures**. Their requests, candidates, gates and
-synthetic decisions cannot fill these missing development references or accept M1.
-No active development harness run using the approved inputs was identified at
-completion. Recheck before any later input mutation; active-run approved inputs
-and snapshots must remain immutable.
-
-## Next responsible workflow and human checks
-
-The next step belongs to separately authorized **M1 QA preparation and human
-assessment**. Establish the missing development configuration/branches/output,
-assessed source, exact tested candidate and request-specific evidence through the
-applicable preparation workflow. Preserve candidate preparation, promotion,
-continuation, QA-session execution and approval recording as separately authorized
-operations. No such operation is authorized merely by this generated status file.
-
-Use M1's [published human QA](.scratch/ticket-harness/milestones.md#m1-a-complete-qa-controlled-git-cycle):
-
-1. Inspect the unified approved spec/proposal flow and this development handoff.
-2. In an isolated disposable repository, demonstrate foreground scripted execution
-   with two runtime milestones: first-group integration into feature, a tested
-   feature-to-current-development candidate, observable indefinite QA waiting and
-   later tickets still Pending at attempt zero.
-3. Show stale acceptance leaves development unchanged. Stop deliberately at the
-   first QA checkpoint using `stop RUN_DIRECTORY`; observe owner exit 2 and
-   `stopped_at_qa`. Continue through a new foreground process, preserving Done work,
-   baseline/artifacts/history, ownership serialization and stale-state rejection.
-4. Record explicit matching acceptance from the human/QA session. Confirm only the
-   exact tested candidate promotes and feature aligns before later work begins.
-   Preserve consumed-decision history across any further planned stop. Confirm
-   final acceptance alone completes the feature.
-
-Setup/contracts are in [the public guide](docs/ticket-harness.md), including the
-canonical runtime plan and exact decision schema. The disposable builders and
-scenarios in [test_milestones.py](tests/test_milestones.py),
-[test_qa_promotion.py](tests/test_qa_promotion.py), and
-[test_continuation.py](tests/test_continuation.py) provide inspected setup examples;
-automated execution is not the human's acceptance. Read
-[Python environment guidance](docs/agents/python-environment.md) before Python and
-[testing policy](docs/agents/testing.md) plus
-[test-strategy](.agents/skills/custom/test-strategy/SKILL.md) for any verification work.
-
-Record the actual assessed source/feature/development/candidate revisions,
-plan/run/request identities, real gate output, observed human checks, findings and
-explicit decision in request-specific evidence. The existing runtime decision
-contract remains separate `qa-decision.json` with exactly
-`{"decision":"APPROVED","request":<complete current qa-request.json object>}`,
-matching JSON fields/types/values and rejecting duplicate/extra/stale/replayed
-approval. The human/QA session owns it outside approved requirements and worker
-worktrees. A worker cannot author its own acceptance. Changed inputs require
-renewed candidate verification and human assessment; corrections need an approved
-versioned amendment and renewed acceptance.
-
-## Eligibility and boundaries
-
-M2 tickets **16–20** remain gated by recorded human acceptance of M1. After that
-acceptance, select prerequisite-ready work through the approved milestone order;
-readiness alone does not satisfy a human checkpoint. QA-session/correction workflows
-(16–18), background operation (19), independent progress (20), live Codex, runtime
-role-skill capture, OS enforcement and release acceptance remain later slices.
-Arbitrary mid-stage crash recovery remains excluded. Ticket completion and plan
-approval do not accept M1 or complete the feature before final human QA.
-
-Carry the approved development role settings into any later authorized assignment:
-fresh GPT-6.1 Sol Medium implementation/repair, independently configured fresh High
-Spec and High Standards; a ticket worker override changes implementation/repair
-only. Inherit required project/scoped role guidance from the approved spec, including
-custom test strategy/TDD and applicable combined design guidance. Report missing
-configuration rather than guessing. Target 250K active context per assignment.
-Development settings do not prove runtime profile enforcement or skill capture.
-E1 ticket 25 retains its separate priority immediately after verified 24 and never
-gates release acceptance. No push is authorized by this handoff.
+The [prior QA-waiting handoff](.scratch/ticket-harness/archive/before-oop-v2/next_agent_prompt.md) is historical; its verified source evidence keeps its scope while old scheduling is superseded. Preserve active-run inputs, old reports/checkpoints and human decisions. No new development run/request/candidate/decision identity or push is authorized by this handoff.
```
