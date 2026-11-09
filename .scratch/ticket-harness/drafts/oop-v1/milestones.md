# Development milestones — OOP amendment

**Draft — unapproved. Plan version:** oop-v1. [Scope and change summary](ticket-proposal.md#change-summary). No milestone is accepted by this draft.

## Eligibility and decisions

- Completed 01–15 retain their identities and evidence. M1 is extended before its still-pending human QA; new M1 work is 16–18 in preferred order. Ticket 16 is the first proposed implementation after amendment publication, but planning does not start it.
- Follow genuine dependencies inside the current milestone. Later release milestones wait for verified completion and explicit human acceptance of the preceding milestone. Stable milestone IDs M1–M4 remain unchanged.
- Development milestones govern this repository's work and are distinct from target-repository milestones exercised by fixtures. An approved plan, a passing test, a completed ticket or a scripted fixture decision never accepts a development candidate.
- Actual QA uses request-specific evidence and a separate explicit human decision with the implemented candidate/input identities. No existing active run's approved inputs may be edited by publication; historical evidence and captures keep their original IDs.
- E1 is independent; prioritize 28 immediately after verified 27, with its own final acceptance. It does not gate M3, M4 or release.

## Required release membership

| Milestone | Required tickets in preferred order | Entry gate |
| --- | --- | --- |
| M1: A complete QA-controlled Git cycle | [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](../../issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](../../issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Own implementation-attempt transitions](ticket-proposal.md#16-own-implementation-attempt-transitions), [17: Own ticket execution and bounded repairs](ticket-proposal.md#17-own-ticket-execution-and-bounded-repairs), [18: Own milestone review and checkpoint continuation](ticket-proposal.md#18-own-milestone-review-and-checkpoint-continuation) | First eligible milestone after amendment approval |
| M2: An unattended operator workflow | [19: Guide a human through milestone QA](ticket-proposal.md#19-guide-a-human-through-milestone-qa), [20: Propose a versioned correction plan](ticket-proposal.md#20-propose-a-versioned-correction-plan), [21: Execute approved QA corrections](ticket-proposal.md#21-execute-approved-qa-corrections), [22: Operate the orchestrator in the background](ticket-proposal.md#22-operate-the-orchestrator-in-the-background), [23: Continue independent work inside the current milestone](ticket-proposal.md#23-continue-independent-work-inside-the-current-milestone) | Explicit human acceptance of M1 |
| M3: Real agents with explicit guidance | [24: Supply coherent design guidance to Standards review](ticket-proposal.md#24-supply-coherent-design-guidance-to-standards-review), [25: Capture and deliver selected local skills](ticket-proposal.md#25-capture-and-deliver-selected-local-skills), [26: Deliver focused implementation and Spec contexts](ticket-proposal.md#26-deliver-focused-implementation-and-spec-contexts), [27: Complete the workflow with real Codex roles](ticket-proposal.md#27-complete-the-workflow-with-real-codex-roles) | Explicit human acceptance of M2 |
| M4: First usable release and final acceptance | [29: Verify runtime write and approval boundaries](ticket-proposal.md#29-verify-runtime-write-and-approval-boundaries), [30: Run a generated approved plan through the runtime](ticket-proposal.md#30-run-a-generated-approved-plan-through-the-runtime), [31: Demonstrate the revised first usable release](ticket-proposal.md#31-demonstrate-the-revised-first-usable-release) | Explicit human acceptance of M3 |

Every required ticket 10–27 and 29–31 has exactly one required membership (21 tickets, including completed 10–15). Completed baseline 01–09 is preserved. Ticket 28 belongs only to E1. M4 is the final checkpoint with cumulative acceptance of all required work.

## M1: A complete QA-controlled Git cycle

**Required tickets:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md), [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md), [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md), [13: Present a tested feature-to-dev candidate](../../issues/13-prepare-a-tested-feature-to-dev-candidate.md), [14: Consume approval, promote, and continue](../../issues/14-promote-only-the-human-approved-milestone.md), [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md), [16: Own implementation-attempt transitions](ticket-proposal.md#16-own-implementation-attempt-transitions), [17: Own ticket execution and bounded repairs](ticket-proposal.md#17-own-ticket-execution-and-bounded-repairs), [18: Own milestone review and checkpoint continuation](ticket-proposal.md#18-own-milestone-review-and-checkpoint-continuation)

**QA status:** Not yet requested or accepted.

**QA setup:** Use a disposable repository with the existing foreground scripted two-milestone setup and the final refactored source. Inspect the approved planning output and development handoff, retained attempt/gate history from a repair or decision case, and a deliberate checkpoint produced by pre-refactor code.

**Human actions:** Observe first-group integration into the feature branch, a regression-tested feature-to-dev candidate and a QA wait. Submit a stale approval and confirm dev/later-group work stay unchanged. Stop and continue in a new process; confirm completed assignments/baseline are not replayed and history persists. Approve the exact current request, confirm both refs advance only to its candidate, and observe later-group work start only then. Complete the final fixture QA; inspect correct attempt/ticket states and final-only feature completion. Assess the prior-code checkpoint continuation evidence and post-restore canonical-gate invalidation evidence.

**Pass conditions:** All new refactor tickets are verified, the current source preserves the public CLI/record/checkpoint behavior, and observed identities agree with exact tested/accepted candidates. Refactor completion and scripted approvals alone do not accept the development milestone.

**Acceptance evidence:** Retain assessed harness/source/feature/development/candidate revisions, approved plan version and request identity, actual gate results and preserved artifacts, observed human checks, findings, and the explicit request-specific decision. Corrections require an approved amendment and renewed candidate acceptance; unchanged historical acceptance evidence retains its original scope.

## M2: An unattended operator workflow

**Required tickets:** [19: Guide a human through milestone QA](ticket-proposal.md#19-guide-a-human-through-milestone-qa), [20: Propose a versioned correction plan](ticket-proposal.md#20-propose-a-versioned-correction-plan), [21: Execute approved QA corrections](ticket-proposal.md#21-execute-approved-qa-corrections), [22: Operate the orchestrator in the background](ticket-proposal.md#22-operate-the-orchestrator-in-the-background), [23: Continue independent work inside the current milestone](ticket-proposal.md#23-continue-independent-work-inside-the-current-milestone)

**QA status:** Not yet requested or accepted.

**QA setup:** After explicit M1 acceptance, use the QA-session guidance and a disposable plan with a correction and independent/dependent tickets; use separate operator sessions.

**Human actions:** Request a correction, approve only its versioned amendment, inspect renewed QA, launch in the background, close the launching terminal, inspect status/logs and write the exact decision artifact separately. Observe blocked work alongside unrelated success while dependents and later milestones remain gated.

**Pass conditions:** Correction approval is distinct from candidate acceptance; background operation remains inspectable; blocked roots do not block unrelated eligible work or unlock dependents/later milestones.

**Acceptance evidence:** Retain assessed harness/source/feature/development/candidate revisions, approved plan version and request identity, actual gate results and preserved artifacts, observed human checks, findings, and the explicit request-specific decision. Corrections require an approved amendment and renewed candidate acceptance; unchanged historical acceptance evidence retains its original scope.

## M3: Real agents with explicit guidance

**Required tickets:** [24: Supply coherent design guidance to Standards review](ticket-proposal.md#24-supply-coherent-design-guidance-to-standards-review), [25: Capture and deliver selected local skills](ticket-proposal.md#25-capture-and-deliver-selected-local-skills), [26: Deliver focused implementation and Spec contexts](ticket-proposal.md#26-deliver-focused-implementation-and-spec-contexts), [27: Complete the workflow with real Codex roles](ticket-proposal.md#27-complete-the-workflow-with-real-codex-roles)

**QA status:** Not yet requested or accepted.

**QA setup:** After explicit M2 acceptance, prepare a tiny real-Codex case with project defaults, one applicable ticket addition and a worker override, preserving separate reviewer profiles.

**Human actions:** Inspect combined design guidance, captured/delivered instruction identities, focused implementation/repair/Spec contexts and actual role settings/reports. Observe the real cycle and exact QA-controlled promotion. Schedule E1 immediately after verified 27 when its prerequisites are met.

**Pass conditions:** Real process invocation and delivered instructions are evidenced; worker/repair use their agreed setting independently of High reviewers. Human approval stays separate from model output. E1 completion is not a condition of this milestone or release.

**Acceptance evidence:** Retain assessed harness/source/feature/development/candidate revisions, approved plan version and request identity, actual gate results and preserved artifacts, observed human checks, findings, and the explicit request-specific decision. Corrections require an approved amendment and renewed candidate acceptance; unchanged historical acceptance evidence retains its original scope.

## M4: First usable release and final acceptance

**Required tickets:** [29: Verify runtime write and approval boundaries](ticket-proposal.md#29-verify-runtime-write-and-approval-boundaries), [30: Run a generated approved plan through the runtime](ticket-proposal.md#30-run-a-generated-approved-plan-through-the-runtime), [31: Demonstrate the revised first usable release](ticket-proposal.md#31-demonstrate-the-revised-first-usable-release)

**QA status:** Not yet requested or accepted.

**QA setup:** After explicit M3 acceptance, start from a clean checkout and disposable target repository with the documented installed interfaces and retained access/real-agent evidence.

**Human actions:** Inspect live role/file/ref/QA-authority probes and generated-plan execution. Operate planning, foreground/background launch, correction, status/logs, planned stop/continue, blocked/dependent/unrelated work, optional findings and two QA milestones. Inspect final exact development promotion and the documented deferred capabilities.

**Pass conditions:** All required work from M1–M4 is verified and its prior milestone acceptances are recorded; the current release passes the complete walkthrough and explicit final human acceptance. Ticket Done and all automated gates alone are insufficient. Coverage is cumulative across every required ticket 10–27 and 29–31, with completed baseline 01–09 preserved.

**Acceptance evidence:** Retain assessed harness/source/feature/development/candidate revisions, approved plan version and request identity, actual gate results and preserved artifacts, observed human checks, findings, and the explicit request-specific decision. Corrections require an approved amendment and renewed candidate acceptance; unchanged historical acceptance evidence retains its original scope.

## E1: Independent early context experiment

**Required tickets:** [28: Run the early context-budget comparison](ticket-proposal.md#28-run-the-early-context-budget-comparison)

**QA status:** Not yet requested or accepted.

**QA setup:** Immediately after verified 27 supplies the actual backend, configured role settings and usage artifacts, select experiment 28 independently of release milestones.

**Human actions:** Review the controlled 100K, 150K, 200K and 250K runs, task-relevant pressure case, cumulative/cached usage versus active occupancy, compaction behavior, result quality and measured limitations.

**Pass conditions:** Evidence distinguishes hard enforcement, compaction thresholds and advisory limits without inferring unsupported claims. This experiment has its own final acceptance and never becomes a release prerequisite.

**Acceptance evidence:** Retain assessed harness/source/feature/development/candidate revisions, approved plan version and request identity, actual gate results and preserved artifacts, observed human checks, findings, and the explicit request-specific decision. Corrections require an approved amendment and renewed candidate acceptance; unchanged historical acceptance evidence retains its original scope.
