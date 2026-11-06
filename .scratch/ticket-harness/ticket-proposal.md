# Approved implementation plan: milestone QA

**Approval state:** Human approved. The QA-first definitions are published as tickets 10–28; tickets 01–09 remain complete.

The [canonical spec](spec.md) defines requirements. This document defines the approved decomposition, skill changes, milestone groups, and mapping from unfinished work. Start from the [feature index](README.md) for execution status. It replaces the [historical seven-ticket proposal](archive/ticket-proposal-original.md); completed tickets 01–09 remain intact.

## Published slice-to-ticket mapping

The QA-first definitions are published as 10–28 in preferred execution order, as requested by the human. Use [milestones](milestones.md) and genuine dependencies to determine eligibility. The [numbering history](archive/ticket-numbering-history.md) maps the earlier QA-first IDs to current IDs; [pre-QA definitions](archive/issues-before-milestone-qa/) retain their historical identities.

| Plan slice | Published ticket | Milestone |
| --- | --- | --- |
| R01 | [10: Turn one grilling session into an approved plan](issues/10-produce-approved-harness-inputs-with-planning-skill.md) | M1 |
| R02 | [11: Stop development handoffs at human checkpoints](issues/11-stop-development-handoffs-at-qa-milestones.md) | M1 |
| R03 | [12: Execute only the first eligible milestone](issues/12-execute-only-the-current-qa-milestone.md) | M1 |
| R04 | [13: Present a tested feature-to-dev candidate](issues/13-prepare-a-tested-feature-to-dev-candidate.md) | M1 |
| R05 | [14: Consume approval, promote, and continue](issues/14-promote-only-the-human-approved-milestone.md) | M1 |
| R06 | [15: Continue after a deliberate QA stop](issues/15-continue-from-a-planned-qa-checkpoint.md) | M1 |
| R07 | [16: Guide a human through milestone QA](issues/16-guide-and-record-human-milestone-qa.md) | M2 |
| R08 | [17: Propose a versioned correction plan](issues/17-propose-versioned-qa-corrections.md) | M2 |
| R09 | [18: Execute approved QA corrections](issues/18-execute-approved-qa-corrections.md) | M2 |
| R10 | [19: Operate the orchestrator in the background](issues/19-operate-the-harness-in-the-background.md) | M2 |
| R11 | [20: Continue independent work inside the current milestone](issues/20-continue-independent-work-after-blocks.md) | M2 |
| R12 | [21: Supply coherent design guidance to Standards review](issues/21-supply-combined-design-guidance-to-standards-review.md) | M3 |
| R13 | [22: Capture and deliver selected local skills](issues/22-capture-and-deliver-selected-local-skills.md) | M3 |
| R14 | [23: Deliver focused implementation and Spec contexts](issues/23-deliver-focused-implementation-and-spec-review-contexts.md) | M3 |
| R15 | [24: Complete the workflow with real Codex roles](issues/24-run-a-real-codex-ticket-cycle.md) | M3 |
| R16 | [25: Run the early context-budget comparison](issues/25-compare-configurable-agent-context-limits.md) | E1 |
| R17 | [26: Verify runtime write and approval boundaries](issues/26-verify-role-write-boundaries.md) | M4 |
| R18 | [27: Run a generated approved plan through the runtime](issues/27-run-a-generated-plan-through-the-runtime.md) | M4 |
| R19 | [28: Demonstrate the revised first usable release](issues/28-demonstrate-the-first-usable-release.md) | M4 |

## Baseline and preservation

- Tickets **01–09 are complete**. Preserve their requirements, commits, code, checks, and [completion evidence](README.md#completion-evidence). Their implemented foundation includes validated inputs/reports, exact ticket-candidate promotion, bounded repairs, decision handoffs, optional suggestions, timeouts, and sequential dependency execution.
- Baseline inspected: `84982495be5d4943301e165f8419421391e75d18`. The ticket-09 evidence records 469 passing tests and independent reviews; this proposal does not claim a new test run.
- Tickets **10–28 are open**. Their approved responsibilities and acceptance requirements are preserved by this numbering refactor. Completed IDs 01–09, prior-run captures, and historical definitions retain their identities.
- `R01`–`R19` below are **plan slice references**, not ticket IDs; use the mapping and current milestone eligibility for executable assignments. They describe 19 published remaining slices: eight original open responsibilities, two additional slices from splitting broad original tickets, and nine new workflow slices. Publication adds eleven open tickets; it does not recreate tickets 01–09.
- Keep the 250K active-context target per agent and focused public behavior per ticket. Existing required verification gates remain mandatory. Initial QA scenarios use foreground scripted workers and real disposable Git repositories.
- The current CLI has no planned QA pause, QA approval parser, second feature-to-dev promotion, background launch, or safe-checkpoint continuation. A completed ticket or an old generated handoff is not evidence those capabilities exist.

## Comparison with the pre-QA open tickets

| Historical pre-QA ticket | Plan slices | Treatment |
| --- | --- | --- |
| [10: Continue unrelated work](archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md) | R11 | Retain failure isolation; restrict continuation to eligible work inside the current milestone. Never cross a QA boundary. |
| [11: Combined design and skill delivery](archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md) | R12, R13 | Split shared design/Standards guidance from generic skill selection/capture/delivery. Preserve all existing requirements. |
| [12: Implementation and Spec guidance](archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md) | R14 | Retain focused role delivery; incorporate milestone contracts without giving workers QA, commit, or orchestration authority. |
| [13: Real Codex cycle](archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) | R15 | Retain real-process validation; add Medium worker/repair defaults, High reviewer defaults, and ticket worker overrides. Exercise the established QA cycle. |
| [14: Role boundaries](archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md) | R17 | Retain live write-boundary probes; extend protected targets to QA decisions and both integration destinations. |
| [15: Planning skill](archive/issues-before-milestone-qa/15-produce-approved-harness-inputs-with-planning-skill.md) | R01, R18 | Move the user-facing planning workflow early. Separate it from later proof that generated guidance/skill metadata flows through the fully implemented runtime. |
| [16: First release](archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md) | R19 | Retain clean-checkout acceptance and expand it to the revised QA/background/correction scope. |
| [17: Context-budget experiment](archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md) | R16 | Preserve experiment scope; the current ID is 25. Prioritize immediately after real Codex (current ticket 24 / R15); do not add final release, comprehensive sandbox probes, or background operation as prerequisites. |

New workflow slices are R02–R10. The original planning and skill-delivery tickets are split to avoid turning milestone support into oversized assignments.

## Skill changes

| Skill or resource | Proposal | Owning slices |
| --- | --- | --- |
| `grill-to-tickets` (planned name) | One custom entry point: grill including milestone/QA questions, confirm understanding, draft/update spec, present and revise ticket/milestone proposals, obtain bundle approval, then publish. Reuse upstream principles/procedures without editing Matt's files. | R01, R08, R18 |
| Shared planning/QA reference | One source for membership, approval identities, role defaults, correction/version rules, and development-versus-runtime authority. Keep workflow guidance aligned with the implemented input validator; do not invent competing schemas in each skill. | R01, extended by the implementing runtime slices |
| `milestone-qa` (planned name) | Guide assessment of the tested candidate, capture findings and explicit human acceptance, and write only the matching decision artifact. Propose corrections through the unified planning workflow. | R07, R08 |
| `implement-with-checkboxes` | Respect milestone eligibility and worker settings; preserve evidence-backed ticket completion and independent review. A completed ticket does not mean QA acceptance or feature completion. | R02 |
| `create-next-agent-prompt` | At a milestone boundary, produce a QA handoff or clear waiting status instead of assigning the next milestone's ticket. Include exact candidate/request/artifact references where available. | R02 |
| `test-strategy` and testing policy | Reuse current coverage/evidence rules. Add narrowly scoped references for ticket-to-feature and feature-to-dev gates; retain required development full-suite checks. | R02, R04 |
| Runtime design/Standards/implementation/Spec guidance | Complete the already-planned focused skills and explicit delivery. Runtime workers receive reusable guidance, not development-wrapper authority over nested reviews, commits, handoffs, or QA acceptance. | R12–R15 |

Plan approval alone does not install or update the planned custom skills. Grilling and publication are one user-facing workflow; the later QA execution session is separate.

## Approved remaining slices

Dependencies below use R references or already completed issue numbers. They describe genuine prerequisites, not numeric execution order. Milestone boundaries impose the additional approved scheduling gate shown later.

### R01: Turn one grilling session into an approved plan

**Depends on:** Completed 09.

Expand the early part of pre-QA ticket 15 into the unified planning skill and shared reference. Resolve QA/milestone decisions during grilling; produce a spec plus focused ticket/milestone proposal; revise them together; publish only after explicit bundle approval. Default to a final QA checkpoint and meaningful earlier ones, honoring an every-N override and worker reasoning overrides.

**Verify:** Skill validation and isolated planning examples show proposal feedback updating the spec, an unapproved proposal remaining unpublished, and an approved dependency-consistent bundle. Runtime compatibility is completed in R18 rather than claimed early.

### R02: Stop development handoffs at human checkpoints

**Depends on:** R01.

Update the two development wrappers to distinguish ticket completion from milestone/feature acceptance, preserve checkbox/status evidence, and respect Medium/High defaults and ticket worker overrides. An eligible next ticket receives an implementation handoff; a QA boundary receives a QA handoff or explicit waiting status. No handoff launches work or invents an approval.

**Verify:** Isolated handoff examples cover a normal next ticket, a waiting milestone, and final tickets complete but final QA unaccepted. Preserve existing development gates and active-input immutability.

### R03: Execute only the first eligible milestone

**Depends on:** R01, completed 09.

Validate and capture a versioned milestone plan, including final coverage and dependency-consistent fixed membership. Run existing ticket gates into the feature branch for the current group only. At its boundary, record that milestone preparation is pending instead of starting later tickets or claiming feature completion. This slice does not present an untested candidate as ready for QA.

**Verify:** A two-group public CLI fixture integrates the first group, leaves the second unstarted, preserves approved inputs, and rejects missing final coverage or invalid membership before workers launch.

### R04: Present a tested feature-to-dev candidate

**Depends on:** R03.

Prepare the current feature revision against the current development branch, run configured local regression checks, and emit an exact QA request with instructions and plan/milestone/source/base/candidate identities. Keep dev unchanged and later work waiting. A failed or changed candidate is not QA-ready; source-changing conflict resolution renews applicable reviews.

**Verify:** Public Git/report observations cover a passing request, a rejected regression gate, and a changed development base. Preserve per-ticket candidate checks as a separate required gate.

### R05: Consume approval, promote, and continue

**Depends on:** R04.

Watch the separate decision artifact indefinitely. Require an exact approval field and matching request identities; reject stale, malformed, mismatched, incidental, or consumed approvals. Advance dev only to the tested accepted candidate with expected-old checks, align the feature branch, and admit the next group. Final QA promotion completes the feature.

**Verify:** A two-milestone foreground fixture shows waiting, stale approval rejected without promotion, first acceptance unlocking later work, and final acceptance completing the feature. Branch movement cannot be overwritten; waiting consumes no repairs.

### R06: Continue after a deliberate QA stop

**Depends on:** R05.

Persist a safe QA checkpoint and support clean stop/continuation there. Revalidate approved inputs, branch/candidate identities, and relevant evidence; serialize active ownership and prevent duplicate promotion. Preserve prior Done tickets and do not restart their assignments merely because the orchestrator restarted. Arbitrary mid-stage recovery remains deferred.

**Verify:** Stop at the first QA checkpoint, launch a new orchestrator process, consume the decision, and finish the second milestone. Reject changed identities and simultaneous ownership without overwriting evidence.

### R07: Guide a human through milestone QA

**Depends on:** R01, R05.

Create the QA-session skill for existing requests. Guide the planned checks, record observed results, and write the exact artifact only after explicit human acceptance. A request to self-approve from passing tests does not authorize acceptance. Findings remain visible and no product code or integration ref is changed by this skill.

**Verify:** Skill validation and isolated QA examples cover explicit approval, withheld approval, and stale candidate identities using disposable artifacts.

### R08: Propose a versioned correction plan

**Depends on:** R01, R07.

Extend the unified planning flow for QA feedback: propose focused correction tickets and affected spec/milestone changes, show the changes from the approved version, and obtain targeted approval. Unchanged requirements retain their approval; prior versions and completed-ticket history remain intact.

**Verify:** A QA feedback example produces a revised proposal, updates the staged spec consistently, leaves unapproved changes unpublished, and publishes only the accepted amendment. Runtime execution belongs to R09.

### R09: Execute approved QA corrections

**Depends on:** R06, R08.

Accept an approved amendment at the QA boundary without editing captured prior inputs. Run its corrections through existing ticket gates inside the current milestone, retain version/evidence lineage, prepare a fresh candidate, and require renewed QA. Later groups remain gated.

**Verify:** A scripted QA rejection leads to an approved correction, a new candidate and decision, then continuation. Old approval cannot accept the corrected revision; an unapproved amendment cannot run.

### R10: Operate the orchestrator in the background

**Depends on:** R06.

Add normal CLI background launch returning a run identity, observational status/log access, documented stopping controls, and foreground mode. QA waiting survives closing the launching terminal; the separate QA session writes its artifact. Specify active-stage stopping behavior without claiming unsupported restart recovery.

**Verify:** Scripted subprocess tests observe launch, logs/status, waiting, approval-driven continuation, clean QA stop/restart, and descendant cleanup. Do not require model or network access.

### R11: Continue independent work inside the current milestone

**Depends on:** R03, completed 06.

Retain pre-QA ticket 10's blocked-root/waiting-dependent/unrelated-success behavior and shared-environment stopping. Unrelated work is eligible only within the current milestone; a block or exhausted repair cannot bypass a QA boundary or produce feature success.

**Verify:** Reuse the pre-QA ticket 10 fixture requirements, adding later-group work that must remain unstarted. Preserve accurate incomplete and waiting outcomes.

### R12: Supply coherent design guidance to Standards review

**Depends on:** Completed 03.

Retain the design-policy and Standards-role portion of pre-QA ticket 11, auditing current custom guidance and synthesizing Matt/Microsoft principles with Pythonic functions and objects. Deliver the required policy/role context explicitly through the existing assignment seam. Evidence-based blockers remain distinct from optional suggestions.

**Verify:** Validate skills, inspect concrete design examples, and capture actual Standards-assignment inputs in a separate scripted target repository. Generic additive skill selection is isolated in R13.

### R13: Capture and deliver selected local skills

**Depends on:** R01, R12.

Retain pre-QA ticket 11's generic role/default/addition contract: explicitly resolve local sources and required references, capture origin/source/content identities, reject missing content, and record actual delivery. Repairs receive captured instructions even after source edits. Keep the planning reference aligned with this canonical metadata.

**Verify:** Scripted cross-repository assignments exercise defaults, role-specific additions, missing references, and source edits after capture without adding live-model variations.

### R14: Deliver focused implementation and Spec contexts

**Depends on:** R13.

Retain pre-QA ticket 12's distinct implementation/repair/Spec guidance and fresh context assembly. Supply milestone and ticket constraints while keeping reviews, commits, promotions, state changes, and human approval under harness control. Reuse shared design and test strategy without copying the whole upstream library.

**Verify:** Captured scripted implementation, repair, and Spec assignments show scoped requirements, exact reviewed revisions, stable selected guidance, and role separation.

### R15: Complete the workflow with real Codex roles

**Depends on:** R06, R14, completed 08.

Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Verify:** Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

### R16: Run the early context-budget comparison

**Depends on:** R15.

Retain pre-QA ticket 17's 100K/150K/200K/250K controls, fixed workload and reasoning settings, genuine context-pressure case, repetitions, raw measurements, and acceptance checks. Distinguish hard enforcement, compaction thresholds, and advisory targets; active occupancy is separate from cumulative/cached usage.

**Verify:** Preserve the current ticket's explicit experiment evidence requirements. Prioritize immediately after R15, before comprehensive boundary probes or release packaging. It remains independent of first-release acceptance dependencies.

### R17: Verify runtime write and approval boundaries

**Depends on:** R07, R15.

Retain pre-QA ticket 14's real sandbox probes and add QA decisions, dev, and feature refs to the protected authority checks. Implementers may edit assigned source; reviewers remain read-only; implementation/repair cannot authorize promotion. Do not silently widen permissions or treat a prompt instruction as proof of enforcement.

**Verify:** Existing disposable sentinel probes plus QA/ref targets provide concrete access evidence without touching caller work. A failed access guarantee leaves verification incomplete.

### R18: Run a generated approved plan through the runtime

**Depends on:** R01, R09, R13.

Complete the remaining integration portion of pre-QA ticket 15. Produce a small plan through the unified skill, validate it against the now-implemented milestone/skill contracts, and execute it through the scripted public seam. Demonstrate project-default guidance and a role-specific ticket addition, preserving required contracts.

**Verify:** A generated example reaches QA and promotion with recorded selection/content identities. Planning publication does not itself launch execution; the example uses an explicit run.

### R19: Demonstrate the revised first usable release

**Depends on:** R02, R10, R11, R17, R18, completed 07.

Expand pre-QA ticket 16's clean-checkout acceptance to planning, background operation, two QA milestones, corrections, safe checkpoint continuation, exact local promotions, blocked/waiting work, optional findings, selected guidance, and actual Codex/access evidence. Clearly document deferred concurrency, arbitrary crash recovery, hosted PRs/GitHub checks, and email.

**Verify:** Run the existing required complete suite and packaging/installed CLI checks, follow the documented disposable-repository walkthrough, and retain actual live evidence or its explicit blocker. R16 is scheduled early but is not a prerequisite for release acceptance.

## Approved development milestones

These checkpoints govern the published remaining harness-development plan. Actual ticket membership and acceptance state are maintained in [milestones.md](milestones.md). They are distinct from the two target-repository milestones exercised inside the deterministic demo. Until the new runtime exists, conduct these development checkpoints manually; do not claim the current harness enforces them or fabricate approvals for completed historical work.

| Milestone | Plan slices | Human QA and acceptance |
| --- | --- | --- |
| M1: A complete QA-controlled cycle | R01–R06 | Inspect the unified proposal/spec flow and development handoff. Run the two-milestone foreground demo; confirm a stale decision leaves dev unchanged, approve the exact candidate, stop/restart at QA, and see later work begin only after acceptance. |
| M2: An unattended operator workflow | R07–R11 | Use the QA-session skill, request a correction, approve its plan change, and inspect renewed QA. Launch in the background, close the launching terminal, inspect status/logs, and verify blocked work cannot cross a milestone. |
| M3: Real agents and early budget evidence | Required: R12–R15. Separately prioritized experiment: R16. | Inspect combined design guidance, role isolation, actual delivered skills and Medium/High settings. Observe a tiny real-agent cycle. Schedule R16 immediately after R15 and review its evidence/limitations when available; completion of that separate experiment is not required for M3 acceptance or release. |
| M4: First usable release and final acceptance | R17–R19 | Inspect live access probes and the generated-plan walkthrough. From a clean checkout, operate the complete experience, inspect final promotion into dev, and confirm documentation accurately separates planned-QA continuation from arbitrary crash recovery. |

Within an accepted milestone, dependency-ready work can be ordered flexibly. No work from a later milestone starts before acceptance of the previous one. Publish R16 under the separate experiment selection/plan, with its own final acceptance checkpoint, so it cannot silently become a dependency of the release's required milestones. Its earliest scheduling priority remains immediately after R15; this separation preserves pre-QA ticket 17's independent phase.

## Ticket reconciliation

The human approved this plan and its spec. Publication reconciled tickets 10–17, added 18–28, recorded the mapping and milestone membership, and refreshed the execution handoff. The human subsequently requested sequential numbering of the 19 open tickets; the [numbering history](archive/ticket-numbering-history.md) records that refactor. Completed 01–09 and their evidence are unchanged; previous open definitions are archived. R references remain historical plan-slice identifiers.

No additional approval of unchanged decisions is needed. If reconciliation reveals a substantive unresolved decision, use targeted grilling and present only the affected spec/plan changes for approval. Existing run captures remain immutable. Document consolidation does not itself publish new issue files, start implementation, or authorize external publishing.
