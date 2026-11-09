# Ticket harness ownership and review amendment — complete proposal

**Draft — unapproved. Plan version:** oop-v2. **Draft revision:** review-process-1.

Review the [spec](spec.md), all full ticket bodies below, [milestones](milestones.md), [index](README.md), [numbering map](numbering-map.md), domain additions and exact supporting updates as one bundle. Intended publication destination remains `.scratch/ticket-harness/`, including individual approved implementation files under `issues/`. Nothing has been published by this revision.

## Change summary

- Incorporate all five agreed review improvements: explicit ownership contracts; cross-module Spec/Standards assessment; cumulative milestone/early-risk architecture reviews; persistent finding disposition/carry-forward; actual reviewer evaluation.
- Add review work items, immutable reports and append-only findings/decision history to the existing tracker. Preserve why a change was made and link it to repairs/tickets, commits, independent verification and milestone evidence. Review records do not consume implementation IDs or form another scheduler.
- Place development review work 16–19 before the original five ownership refactors, now 20–24. Preserve those five outcomes and completed 01–15; apply the evaluated review workflow to the refactors.
- Add scripted runtime review enforcement 33 before real agents 34. Existing guidance/capture/context/QA/access/release work consumes the same contract through explicit additional criteria; M1 evaluation does not claim runtime delivery or backend availability.
- Renumber coherently: M1 10–24; M2 25–29; M3 30–34; independent E1 35 immediately after 34; final M4 36–38. Preserve original criteria and genuine dependencies, disclosing the three new consumed-interface edges on inherited guidance/real-agent work.
- Keep human risk/ownership/scope decisions separate from exact-candidate QA acceptance, and preserve existing commands/reports/checkpoints during the five refactors. Runtime review state is additive, with frozen-evidence and old-record compatibility explicitly required.

## Shared understanding and publication decision

The human confirmed the original five-refactor split and sequential renumbering, then agreed to the proposed review improvements and existing-tracker review history, and explicitly requested incorporating both into the previous oop-v2 spec/tickets/etc. This authorizes the expanded draft. Publication approval of the complete review-process-1 bundle is pending. Detailed thresholds, cadence, authority and sequencing are proposed explicitly below for that decision; no evaluation or implementation has been executed.

<a id="published-slice-to-ticket-mapping"></a>

## Preferred order, dependencies and membership

Preferred order is completed 01–15, M1 new 16–24, M2 25–29 after M1 acceptance, M3 30–34 after M2 acceptance, E1 35 immediately after verified 34, then final M4 36–38 after M3 acceptance. Numbers express preferred sequence; actual prerequisite edges and human milestone gates govern eligibility.

| Ticket | Stable slice | Prerequisites | Membership | Worker override |
| --- | --- | --- | --- | --- |
| [16: Record review work, findings and decisions](#16-record-review-work-findings-and-decisions) | RV01 | 10, 11 | M1 | None; inherit Medium |
| [17: Review ownership across affected modules](#17-review-ownership-across-affected-modules) | RV02 | 16 | M1 | None; inherit Medium |
| [18: Gate development on cumulative architecture review](#18-gate-development-on-cumulative-architecture-review) | RV03 | 16, 17 | M1 | None; inherit Medium |
| [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs) | RV04 | 17, 18 | M1 | None; inherit Medium |
| [20: Own implementation-attempt transitions](#20-own-implementation-attempt-transitions) | O01 | 05, 06, 19 | M1 | None; inherit Medium |
| [21: Own ticket execution and bounded repairs](#21-own-ticket-execution-and-bounded-repairs) | O02 | 20 | M1 | None; inherit Medium |
| [22: Return clearly prepared inputs](#22-return-clearly-prepared-inputs) | O04 | 02, 12, 19 | M1 | None; inherit Medium |
| [23: Own the complete run lifecycle](#23-own-the-complete-run-lifecycle) | O05 | 15, 21, 22 | M1 | None; inherit Medium |
| [24: Own milestone review and checkpoint continuation](#24-own-milestone-review-and-checkpoint-continuation) | O03 | 15, 23 | M1 | None; inherit Medium |
| [25: Guide a human through milestone QA](#25-guide-a-human-through-milestone-qa) | R07 | 10, 14 | M2 | None; inherit Medium |
| [26: Propose a versioned correction plan](#26-propose-a-versioned-correction-plan) | R08 | 10, 25 | M2 | None; inherit Medium |
| [27: Execute approved QA corrections](#27-execute-approved-qa-corrections) | R09 | 15, 26 | M2 | None; inherit Medium |
| [28: Operate the orchestrator in the background](#28-operate-the-orchestrator-in-the-background) | R10 | 15 | M2 | None; inherit Medium |
| [29: Continue independent work inside the current milestone](#29-continue-independent-work-inside-the-current-milestone) | R11 | 12, 06 | M2 | None; inherit Medium |
| [30: Supply coherent design guidance to Standards review](#30-supply-coherent-design-guidance-to-standards-review) | R12 | 03, 19 | M3 | None; inherit Medium |
| [31: Capture and deliver selected local skills](#31-capture-and-deliver-selected-local-skills) | R13 | 10, 30 | M3 | None; inherit Medium |
| [32: Deliver focused implementation and Spec contexts](#32-deliver-focused-implementation-and-spec-contexts) | R14 | 31, 19 | M3 | None; inherit Medium |
| [33: Enforce traceable runtime review checkpoints](#33-enforce-traceable-runtime-review-checkpoints) | RV05 | 19, 24, 30, 31, 32 | M3 | None; inherit Medium |
| [34: Complete the workflow with real Codex roles](#34-complete-the-workflow-with-real-codex-roles) | R15 | 15, 32, 08, 33 | M3 | None; inherit Medium |
| [35: Run the early context-budget comparison](#35-run-the-early-context-budget-comparison) | R16 | 34 | E1 | None; inherit Medium |
| [36: Verify runtime write and approval boundaries](#36-verify-runtime-write-and-approval-boundaries) | R17 | 25, 34 | M4 | None; inherit Medium |
| [37: Run a generated approved plan through the runtime](#37-run-a-generated-approved-plan-through-the-runtime) | R18 | 10, 27, 31 | M4 | None; inherit Medium |
| [38: Demonstrate the revised first usable release](#38-demonstrate-the-revised-first-usable-release) | R19 | 11, 28, 29, 36, 37, 07 | M4 | None; inherit Medium |

Review 16 consumes completed planning/handoff contracts 10/11; 17 uses its record/history contract; 18 uses 17's scoped reviewers and 16's records; 19 evaluates 17/18. Refactors 20 and 22 explicitly wait for evaluated review 19, while 21 consumes 20,23 consumes 21/22 and completed 15, and 24 consumes 23/15. This makes the stronger review available before the work meant to exercise it. Runtime 33 consumes evaluated policy 19, refactored checkpoint ownership 24, delivered Standards policy 30, captured guidance 31 and focused contexts 32. Real-agent 34 consumes 33. Existing guidance 30 and focused-context32 also explicitly consume 19's evaluated contract. No dependency is added merely to simulate a numeric chain.

## Changes to inherited ticket requirements

All original inherited acceptance criteria remain in their original order with current references renumbered. Added review criteria are explicitly marked in tickets 25–27,30–32,34,36–38: QA/correction rationale links; actual Standards policy delivery; captured/scoped prior findings; real-agent proof of enforced runtime reviews; review-decision access probes; generated-plan metadata; final end-to-end review history. Tickets28/29 retain their original background/independent-work criteria unchanged; later33 owns the new observational runtime-review status behavior. New consumed-contract edges are 19→30,19→32 and 33→34; prior genuine dependencies are retained. No completed ticket is reopened.

## Testing and review contracts

Keep existing role defaults, independent Spec/Standards assignments and the public CLI/scripted-process/real-Git seam for runtime changes. Guidance work uses document/skill and isolated workflow validation. Actual development-reviewer evaluation is a declared M1 requirement; scripted output cannot satisfy it. The proposed minimum corpus is four concern cases plus four acceptable controls, with required concerns detected and no unsupported blocking control findings. Preserve failed trials and scope limitations. Final implementation tickets retain policy-required verification and independent reviews.

## Review improvement coverage

| Agreed improvement | Development delivery | Runtime adoption and evidence |
| --- | --- | --- |
| Explicit ownership contracts | 17; applied in 20–24 | 30–34 |
| Review affected callers, writers and persistence beyond the diff | 17; actual evaluation in 19 | 30, 32–34 |
| Cumulative milestone and early-risk architecture checkpoints | 18; final M1 assessment | 33–34 and later milestone QA |
| Finding disposition and carry-forward | 16–18; refactor histories | 25–27, 32–34 |
| Evaluate actual reviewer judgment | 19 with concerns and acceptable controls | 34 with actual live delivery/enforcement |
| Navigable review work, reports and human decision rationale | 16; review history across 17–24 | 33–34, access/generated-plan/final release 36–38 |

## Milestone definitions and QA

Use the full [milestone definitions](milestones.md). M1 now demonstrates traceable review workflow, evaluated reviewers and five refactors before its existing scripted QA cycle. M3 separately proves runtime enforcement and actual real-agent delivery. Cumulative architecture assessment precedes each required milestone QA; risk triggers require earlier assessment before affected integration. All QA remains not requested/accepted; final M4 is cumulative and independent E1 never gates release.

## Full proposed open-ticket bodies


<!-- Proposed publication: issues/16-record-review-work-findings-and-decisions.md -->

## 16: Record review work, findings and decisions

**What to build:** Make review work, source-identified reports, findings and their decisions navigable in the existing local tracker. Provide a repo-owned record contract and usable templates/navigation so the human can follow a concern through its disposition, repair commit, verification and milestone evidence without a second issue system.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md), review-process-1 draft revision.

**Milestone:** M1. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](../../../../../../.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration). Respect [domain terms](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Define one review work item for an assessment scope, with identity, linked originating ticket(s)/milestone, purpose, fixed baseline, assessed revision, reviewer axis/settings/instruction identity, status, inspected/omitted scope, report links and current unresolved findings. Routine ticket Spec/Standards reports attach to the ticket assessment; cross-ticket architecture assessments have their own review work item. Reviews are not selected implementation tickets and do not consume or renumber implementation IDs.
- [ ] Retain original reports and evidence as immutable source-identified snapshots. Key a finding by review/report identity plus its report-local ID so different axes, attempts or reviews may reuse local IDs safely. Maintain an append-only disposition history with actor, reason, evidence, affected revision and links; correction or re-review appends a superseding observation rather than rewriting the original report.
- [ ] Support recorded dispositions open, fixed, deferred to a linked ticket, accepted with a reason, and awaiting a human decision. Fixed requires independent verification for the exact repair revision; a later changed revision needs revalidation. Review completion means its assessment/report is complete, while unresolved findings and integration/milestone eligibility remain separately visible.
- [ ] Preserve human authority: agents may perform authorized repairs and record evidence or proposals; accepting consequential risk, deferring an integration-blocking finding, changing an ownership contract or expanding scope requires an explicit human decision and any necessary approved amendment. A review disposition is not QA acceptance and cannot grant promotion authority or silently turn a blocker into permission to integrate.
- [ ] Publish a compact navigable chain from originating scope to finding/evidence, decision/reason, linked implementation ticket or repair, commit and verification, and eventual milestone assessment. Demonstrate a fixed finding, a deferred optional finding, an explicit human risk decision, duplicate report-local IDs, a reopened concern on changed source and a completed review with outstanding findings.
- [ ] Keep review records in the existing feature tracker context and evidence locations, with review-specific lifecycle fields documented separately from ticket readiness. Historical reports/completed tickets and captured run inputs remain unchanged. During a harness run, new review artifacts belong to harness-owned output; post-run tracker links never mutate active approved inputs or frozen QA evidence.

### Verification

Use the standalone document/skill/workflow validation approach established by completed planning and handoff work. Create an isolated miniature tracker with real Markdown review records and source/report identities, exercise the six history/navigation cases above, and inspect retained artifacts. This ticket implements the development record contract and templates, not runtime scheduling or a new report wire schema.

Use the [testing policy](../../../../docs/agents/testing.md), [Python environment](../../../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

<!-- Proposed publication: issues/17-review-ownership-across-affected-modules.md -->

## 17: Review ownership across affected modules

**What to build:** Require explicit ownership contracts during planning and evidence-based Spec/Standards assessment across the affected workflow. Extend repo-owned planning, implementation, review and handoff guidance so a ticket is assessed with relevant callers, writers and persistence consumers, while preserving independent review axes and scope authority.

**Blocked by:** [16: Record review work, findings and decisions](#16-record-review-work-findings-and-decisions).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md), review-process-1 draft revision.

**Milestone:** M1. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](../../../../../../.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration). Respect [domain terms](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] For consequential mutable state, planning records the owner, permitted writers, operations preserving invariants, persistence/restoration rules and failure behavior. Workers record the ownership change or explain why existing ownership is unchanged; a missing consequential ownership decision is surfaced for the human rather than invented during implementation.
- [ ] Keep the original-baseline whole-ticket review and separate fresh Spec/Standards assignments. Standards follows affected state and responsibilities through relevant unchanged callers, consumers, other writers and save/restore/invalidation paths; Spec checks approved ownership/behavior contracts as well as acceptance requirements. Reviewer scope is not limited to diff hunks or a universal short-report cap.
- [ ] Each report states assessed source/baseline, inspected files/flows, explicitly omitted scope and unresolved assumptions. Findings cite the code/contract, concrete consequence, evidence and proportionate remedy; code length or a preference for classes is insufficient. An empty findings list is meaningful only for the recorded inspected scope.
- [ ] Carry prior findings and append-only dispositions from ticket 16 into scoped review/repair context, and verify claimed fixes against the repaired revision. Preserve report independence before aggregation; separate evidence/provenance auditing from substantive reasoning so successful hashes or tests cannot substitute for design assessment.
- [ ] Update existing development wrappers and next-agent handoffs to apply the shared contract and expose unresolved review work. Preserve upstream skills, required checks, fresh role settings, bounded authorized repairs, optional suggestions and milestone gates. Any concrete breach or correction stays within existing authorization or is surfaced as a human decision.
- [ ] Demonstrate an unchanged caller hiding a second state writer, a restoration/invalidation path outside the diff, a documented ownership breach versus an optional design suggestion, and a justified clean review of a long cohesive function. Retain actual scoped assignment/report artifacts and evidence of independence, rather than asserting compliance from added skill links.

### Verification

Validate guidance/links and run isolated development-review walkthroughs against representative source/diffs and explicit ownership contracts. Record actual reviewer assignments/reports; reuse current review and architecture guidance without requiring every review to render HTML. Broad calibration and its acceptance corpus are delivered in ticket 19; this ticket proves the usable review workflow and scope contract.

Use the [testing policy](../../../../docs/agents/testing.md), [Python environment](../../../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

<!-- Proposed publication: issues/18-gate-development-on-cumulative-architecture-review.md -->

## 18: Gate development on cumulative architecture review

**What to build:** Require source-identified cumulative architecture assessments at development milestone boundaries and earlier risk triggers. Make the existing tracker/handoff workflow surface these assessments and human finding dispositions before implementation is integrated or a milestone is presented as ready for QA.

**Blocked by:** [16: Record review work, findings and decisions](#16-record-review-work-findings-and-decisions); [17: Review ownership across affected modules](#17-review-ownership-across-affected-modules).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md), review-process-1 draft revision.

**Milestone:** M1. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](../../../../../../.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration). Respect [domain terms](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Create a cumulative review work item before each required development milestone QA request. Pin its cumulative baseline to the last accepted milestone (or feature starting revision for the first), assessed source, complete scope inventory and unresolved prior findings. Review all ticket_harness Python files for this small package; larger targets document the complete affected workflow and collaborators.
- [ ] At ticket start and after implementation, assess whether the ticket introduces a new lifecycle, persistence/restoration path, shared mutable state or an additional writer. Such a trigger requires a broader architecture assessment before that ticket integrates, covering the affected workflow rather than only its diff. Missing/incomplete assessment remains visible and prevents readiness; avoid a third unconditional reviewer on every ticket.
- [ ] Use a fresh High Standards assignment for cumulative architecture scope, with the existing Spec/Standards contract and review-record history. Examine ownership and the concrete edits needed for a plausible change, such as another review stage or repair-policy adjustment. An existing audit may satisfy the checkpoint only when its source identity, coverage and retained dispositions actually match.
- [ ] Record each finding as fixed with verification, deferred with a linked ticket, accepted with a reason, or awaiting a human decision; keep open observations visible. In-scope blockers prevent affected integration and milestone readiness. Deferral/acceptance of significant risk needs an explicit human decision and applicable approved amendment, never an agent relabeling or a completed-review status alone.
- [ ] Update milestone/handoff guidance to distinguish assessment completed, findings resolved/dispositioned, candidate ready for human QA and milestone accepted. A clean assessment proceeds autonomously within approved work; it does not generate a human approval request for every comment or replace exact-candidate QA. Changed assessed source requires renewed relevant review before the old assessment can authorize readiness.
- [ ] Demonstrate multiple individually passing tickets accumulating a cross-module ownership problem, a risk-triggered review before integration, stale-source review rejection, a clean checkpoint, blocked progression, human disposition and a handoff preserving deferred work. Archive and reuse report evidence without rewriting old decisions or active-run snapshots.

### Verification

Use isolated planning/implementation/handoff examples and actual cumulative review artifacts, with the fixed source inventory and observed readiness outcomes. Development checkpoint enforcement is in repo-owned guidance and tracker/handoff records; automated runtime execution of the same rules is ticket 33. Skill/document validations and reproducible workflow observations complement the normal implementation reviews.

Use the [testing policy](../../../../docs/agents/testing.md), [Python environment](../../../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

<!-- Proposed publication: issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md -->

## 19: Evaluate reviewers on known and acceptable designs

**What to build:** Evaluate the strengthened development reviewers against known failures, design risks and acceptable implementations before using them on the five refactors. Retain the case contracts, actual fresh reviewer inputs/outputs, misses, false positives and guidance changes so the human can judge what the evaluation establishes.

**Blocked by:** [17: Review ownership across affected modules](#17-review-ownership-across-affected-modules); [18: Gate development on cumulative architecture review](#18-gate-development-on-cumulative-architecture-review).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md), review-process-1 draft revision.

**Milestone:** M1. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](../../../../../../.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration). Respect [domain terms](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Prepare a small source-identified corpus with at least four concern cases and four acceptable controls, with expected relevant review axis and rationale recorded before evaluation. Concerns cover detached restored gate evidence, positional attempt selection, duplicated lifecycle-record edits and externally coordinated initialization; controls cover cohesive Git validation, pure plan/parsing transformations, atomic file/process primitives and explicit owned transitions.
- [ ] Assess the relevant cases with actual fresh development reviewer assignments using the agreed model/role settings and exact guidance identities. Supply cases/contracts without the evaluator answer key, preserve axis independence and retain raw reports. Scripted reviewer output, deterministic text matching and source-link validation alone cannot establish judgment quality.
- [ ] For the declared required corpus, detect every seeded required correctness/ownership concern with source-specific evidence and a proportionate classification/remedy; acceptable controls receive no unsupported blocking finding. Optional observations are judged on evidence, not counted as failures merely for existing. The evaluator explains each expected/observed match and mismatch rather than scoring findings by count alone.
- [ ] Record missed concerns, unsupported blockers and guidance revisions without deleting failed trials. A required miss or false blocker prevents this ticket completing; revise guidance or surface the unresolved limitation, then evaluate the final guidance on the complete declared corpus. Report the finite case set and actual repetitions; no guarantee of future detection or runtime backend effectiveness is inferred.
- [ ] Publish the evaluated guidance version and corpus references through planning and next-agent handoffs so subsequent refactors 20–24 can consume them. Preserve ordinary autonomous repairs and human design/QA authority. This ticket completes on the declared corpus evaluation and usable handoff; actual refactor review/decision evidence belongs to tickets 20–24 and M1 QA, not a prerequisite for completing this ticket.
- [ ] Keep M1 evaluation separate from harness live-backend availability. Actual runtime role/instruction delivery and enforcement must later be verified by tickets 33/34; this development evaluation uses isolated reviewer assignments and does not launch a harness run, fabricate acceptance or add private module tests.

### Verification

Use standalone skill/workflow evaluation with actual development reviewers and isolated writable case fixtures where needed; reviewers receive read-only source snapshots. Retain corpus source/contracts, expected axes, assignment/settings/guidance identities, raw outputs, evaluator reasoning and all trial outcomes. Preserve the CLI/real-Git seam for executable harness changes; this evaluation is a distinct, explicit evidence requirement for review guidance, not a substitute for runtime tests.

Use the [testing policy](../../../../docs/agents/testing.md), [Python environment](../../../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

<!-- Proposed publication: issues/20-own-implementation-attempt-transitions.md -->

## 20: Own implementation-attempt transitions

**What to build:** Give each implementation attempt responsibility for its own lifecycle observations. Submission, rejection, completion and human-decision handoff update the correct attempt and ticket consistently, while the runner continues to execute checks and validate reports. Complete the migration of existing callers within this ticket so the CLI stays usable.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](../../issues/05-repair-rejected-submissions-within-budget.md); [06: Stop for decisions outside approved contracts](../../issues/06-surface-human-decisions-without-retrying.md); [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](spec.md#cumulative-architecture-checkpoints); [review records](spec.md#review-work-findings-and-decisions).

### Acceptance criteria

- [ ] Attempt-owned operations maintain the existing Running, Verifying, Rejected and Done observations, revision identities, changed-file observations, and inclusive/exclusive gate ranges. Corresponding current-ticket observations remain consistent, including failures before a submission exists.
- [ ] The runner retains check execution, report validation, source-evidence invalidation and failure precedence. It communicates validated human-decision evidence to the owning attempt without selecting an attempt through the last entry in shared history or mutating its lifecycle record directly. Report parsing and validation return their findings or failure information; they do not mutate the canonical gate record. The runner records the final report/check status, preserving report content and diagnostics on rejected reports and the current precedence among process exit, timeout, report validity, blocking findings, human decisions and integrity/environment failures.
- [ ] Implementation and either review axis can stop the correct initial or repair attempt for a validated human decision, including a nonzero process exit. Preserve the complete handoff on both existing record locations, preserved work, diagnostic, Blocked/incomplete outcome, and immediate stop without later gates or extra repairs.
- [ ] Malformed decision-like reports, optional findings, ordinary report/process failures and timeouts retain their existing distinct validation and bounded-failure behavior; they cannot gain decision authority or produce false success.
- [ ] Public commands, exit behavior, record keys/values, artifact naming, historical attempt evidence and caller/approved-input protection remain compatible. Atomic persistence still exposes meaningful intermediate observations.
- [ ] Design review confirms transition rules live with attempt state and callers use those operations; private naming/layout remains an implementation choice, with no getter/setter-only wrapper or inheritance framework.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

### Verification

Map existing repair/history and human-decision cases, including initial/later attempts, implementation/either-axis decisions, decision precedence and durable status output. Prior art: `tests/test_repairs.py`, `tests/test_human_decisions.py`, `tests/test_optional_suggestions.py`, `tests/test_timeouts.py` and multi-ticket attempt-history cases in `tests/test_dependencies.py`. Preserve report validation and integrity regression coverage. Include existing `tests/test_reports.py` coverage for malformed reports, valid reports with failed processes, and preserved diagnostics.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/21-own-ticket-execution-and-bounded-repairs.md -->

## 21: Own ticket execution and bounded repairs

**What to build:** Give one ticket execution ownership of its complete implementation, verification and bounded repair cycle. Keep the original approved base, current attempt, repair starting revision, previous source worktree and failure context together. Use the attempt lifecycle delivered by ticket 20; finish the caller migration so existing selected-ticket runs stay green.

**Blocked by:** [20: Own implementation-attempt transitions](#20-own-implementation-attempt-transitions).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](spec.md#cumulative-architecture-checkpoints); [review records](spec.md#review-work-findings-and-decisions).

### Acceptance criteria

- [ ] A ticket execution owns the complete cycle and repair policy through a small interface. The runner coordinates eligible tickets and retains checking; ticket workflow code no longer obtains unrestricted access to the runner merely to manipulate its shared state.
- [ ] The original ticket base remains fixed across attempts, while a repair starts from the observed rejected submission or preserved uncommitted work as applicable. Fresh assignments and worktrees receive the correct failure, rejected revisions, ticket-scoped evidence and configured check selection.
- [ ] Initial assignment plus configured repairs remains bounded. Repairable gate/Git/process/timeout failures, exhausted allowance, human decisions, environment/integrity failures and external ref/HEAD movement retain their existing repair-or-stop decisions and preserved history.
- [ ] Every changed submission receives renewed applicable checks, both independent reviews and an exact candidate suite. Earlier approval cannot authorize a repaired source; approved inputs, earlier evidence and the caller worktree stay protected.
- [ ] Only successful expected-old advancement of the integration branch records the exact tested candidate as Done and unlocks dependents. Later tickets use the current verified integration revision; existing fail-fast behavior after a blocked ticket remains unchanged until the separate blocked-work-isolation ticket.
- [ ] CLI behavior, single-/multi-ticket artifact names, baseline reuse, attempt numbering, gate ranges and saved record formats remain compatible. Existing readiness calculations and Git primitives remain functions where they provide no independent state lifetime.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

### Verification

Map existing successful repair, invalid-report preservation, repair exhaustion, later-ticket fixed-base/history, evidence invalidation and external-integration scenarios. Prior art: `tests/test_repairs.py`, `tests/test_dependencies.py`, `tests/test_transaction.py` and `tests/test_timeouts.py`. This ticket does not implement later independent-work scheduling or add private-class tests.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/22-return-clearly-prepared-inputs.md -->

## 22: Return clearly prepared inputs

**What to build:** Make input preparation return one explicit, complete result containing validated execution settings, approved snapshots, normalized requirements, ticket selection, completion evidence and applicable worker settings. Keep raw settings separate from calculated values, and make all callers use the checked plan returned by validation. Complete caller migration while preserving current input acceptance, rejection, capture and execution behavior.

**Blocked by:** [02: Reject invalid requirements before starting work](../../issues/02-reject-invalid-inputs-before-execution.md); [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md); [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](spec.md#cumulative-architecture-checkpoints); [review records](spec.md#review-work-findings-and-decisions).

### Acceptance criteria

- [ ] The input-loading interface provides the complete prepared result and makes its filesystem preparation requirements explicit. The run consumes that result without repeating preparation rules or externally filling calculated fields into raw configuration. Existing configuration and approved input files remain byte-for-byte unchanged.
- [ ] One input preparation operation still validates executable commands, captures approved files and identities, normalizes tickets, validates dependency graphs and completion evidence, and establishes eligible selection and worker settings. Missing, malformed, conflicting or changed inputs retain existing diagnostics, invalid-input behavior and rejection before workers, checks or branch advancement.
- [ ] All plan consumers use the checked plan returned by validation, including first-milestone selection. Normalized membership, dependency order, role defaults and worker overrides remain governed together by plan validation; callers need not rely on mutation of the original plan object. Requiring validation to become a pure function is not part of this ticket.
- [ ] Legacy runs without a plan, versioned plans, externally completed prerequisites, explicit selections and primary-ticket handling retain their current behavior. Readiness, completion evidence, selected prerequisites, metadata conflicts, default/override inheritance and later-milestone eligibility rules remain intact.
- [ ] Snapshot hashes, copied input names, output separation, persisted configuration/checkpoint contents and status output remain compatible. Any new in-memory result representation is translated into the existing JSON-safe saved shape so pre-existing checkpoints and later restoration keep working.
- [ ] Pure parsing, normalization, graph checks and transformations remain ordinary functions where they own no independent lifecycle. The change introduces neither a configuration framework nor a new testing seam, and the full public CLI path is usable after this ticket.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

### Verification

Map existing preflight/configuration, duplicate metadata, graph/selection/completion-evidence and plan-validation cases in `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`. In particular, preserve invalid-plan rejection before processes/ref changes, normalized first-group selection and worker-setting metadata. Check the implementation diff to confirm callers use the returned checked plan and prepared result; avoid tests that assert a particular result class or require mutation-free validation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/23-own-the-complete-run-lifecycle.md -->

## 23: Own the complete run lifecycle

**What to build:** Give the run ownership of its complete start/continue lifecycle: consume prepared inputs, establish branch and baseline identities, coordinate eligible ticket executions and milestones, classify failures, and finalize durable outcomes. Also make the run own export and restoration of verification references. Migrate existing callers and preserve the CLI throughout; the milestone workflow may remain behind its existing callable until ticket 24.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [21: Own ticket execution and bounded repairs](#21-own-ticket-execution-and-bounded-repairs); [22: Return clearly prepared inputs](#22-return-clearly-prepared-inputs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](spec.md#cumulative-architecture-checkpoints); [review records](spec.md#review-work-findings-and-decisions).

### Acceptance criteria

- [ ] The run owns initialization and deliberate continuation through cohesive operations; an external orchestration function no longer patches configuration, source protection, milestone index and lifecycle records in a required sequence. Public run/continue functions retain output creation, exclusive ownership and existing rejection behavior as appropriate, then invoke the run lifecycle through a small interface.
- [ ] Fresh execution retains branch validation, the required matching base/integration commit, approved-input protection, exactly one baseline and no worker launches/repairs after a failed baseline. Baseline, invalid-input, environment/integrity and later workflow failures preserve their existing stage diagnostics, outcomes, blocked/pending observations and exit codes.
- [ ] The run coordinates the ticket-execution interface from ticket 21 using the prepared inputs from ticket 22. It owns current milestone progression and finalization while ticket and attempt operations own their lifecycle records; it retains current fail-fast scheduling and never starts later-milestone work before exact human acceptance.
- [ ] Continuation consumes a deliberate validated checkpoint without replaying completed tickets, baseline work, artifacts or decisions. It invalidates the stopped marker before resumed work and preserves milestone position, history, feature/development identities, stop exit 2, success exit 0 and existing failed/rejected-continuation behavior.
- [ ] The run provides the existing checkpoint-shaped export and reconstruction of verified-check information. QA no longer inspects the runner's internal tuple/list organization. Restoration resolves references to the canonical gates in the durable run record; later source invalidation changes those actual records, including after repeated stop/continue cycles.
- [ ] Commands, saved JSON schemas/values, checkpoint version and filenames, single-/multi-ticket and milestone artifact naming, process ownership, integrity safeguards and atomic persistence remain compatible. Leave Git/process/filesystem primitives as functions and avoid a separate checker object or generic lifecycle framework.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

### Verification

Map existing fresh-run, failed shared baseline, invalid-input, sequential multi-ticket and run/status cases in `tests/test_cli.py`, `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`; map deliberate/new-process/repeated continuation, active-owner rejection and post-restore canonical-gate invalidation in `tests/test_continuation.py` and `tests/test_qa_promotion.py`. Keep the existing QA callable working during this slice. Continue a genuine pre-refactor checkpoint and retain producer/source provenance, rather than generating compatibility evidence solely with the refactored implementation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/24-own-milestone-review-and-checkpoint-continuation.md -->

## 24: Own milestone review and checkpoint continuation

**What to build:** Give one milestone review ownership of its tested candidate, exact QA request, frozen evidence identities, decision observations and deliberate stop/continuation lifecycle. Fresh preparation and restoration enter the same review rules. Complete caller migration while retaining runner-owned checks and existing human authority over promotion.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [23: Own the complete run lifecycle](#23-own-the-complete-run-lifecycle).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](spec.md#cumulative-architecture-checkpoints); [review records](spec.md#review-work-findings-and-decisions).

### Acceptance criteria

- [ ] A milestone review keeps its candidate/feature/development identities, request content and digest, evidence identities and last observed decision together. Fresh and restored reviews use the same approval, unchanged-source/evidence and expected-ref rules; the caller receives an explicit stopped-versus-promoted outcome instead of a Boolean whose meaning depends on implementation knowledge. Use the run-owned verification export/restoration interface from ticket 23 instead of reading the runner's internal verified-check collection.
- [ ] Only an explicit matching, unconsumed human approval advances both expected feature/development refs to the exact regression-tested candidate. Missing, unreadable, malformed, mismatched, stale and replayed decisions retain observable waiting/rejection behavior without consuming ticket repairs or starting later milestones.
- [ ] Deliberate stop preserves the existing checkpoint version/format, identities, observations and archived lineage. Continue in a new process validates all approved inputs, record/request/evidence/source identities, both refs and exclusive ownership, without replaying completed assignments, completed baseline work or consumed decisions.
- [ ] Continue a genuine deliberate checkpoint written by pre-refactor code as well as one written by the new code. After JSON restoration, later source invalidation updates the canonical gate in the durable run record rather than a detached copy; changed evidence/checkpoints/refs cannot authorize continuation or promotion.
- [ ] Milestone preparation/regression/promotion failure observations, indefinite waits, stop exit behavior, status, ticket-Done versus milestone-promoted versus feature-complete distinctions, command interfaces and record/artifact formats remain compatible.
- [ ] Keep runner-owned checking and source-validation authority. Do not introduce arbitrary crash recovery, background execution, correction-plan execution, new approval authority, or later milestone features in this refactor. Update code wayfinding to describe the final responsibilities.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

### Verification

Map existing exact approval/promotion, stale/replay rejection, clean stop/new-process continuation, post-restore gate invalidation, changed checkpoint/evidence/ref rejection and repeated-stop lineage cases. Prior art: `tests/test_milestones.py`, `tests/test_qa_promotion.py`, `tests/test_continuation.py` and `tests/test_transaction.py`. Retain provenance for a disposable pre-refactor checkpoint and its continuation with the final implementation; reuse existing compatibility evidence only when it actually covers that source. No live Codex or new private seam is needed.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/25-guide-and-record-human-milestone-qa.md -->

<a id="r07-guide-a-human-through-milestone-qa"></a>

## 25: Guide a human through milestone QA

**What to build:** Create the QA-session skill for existing requests. Guide the planned checks, record observed results, and write the exact artifact only after explicit human acceptance. A request to self-approve from passing tests does not authorize acceptance. Findings remain visible and no product code or integration ref is changed by this skill.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [14: Consume approval, promote, and continue](../../issues/14-promote-only-the-human-approved-milestone.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R07](#r07-guide-a-human-through-milestone-qa).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [feature to development promotion and human qa](spec.md#feature-to-development-promotion-and-human-qa).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Create a focused QA-session skill that reads the exact request/candidate and guides the human through planned checks, evidence inspection, and observable acceptance conditions.
- [ ] Record findings and withhold acceptance until the human explicitly approves; passing automated tests or an agent recommendation is insufficient.
- [ ] Write only the precise decision artifact for matching current identities, preserving provenance and rejecting stale requests.
- [ ] Do not implement corrections or change product source/integration refs; propose findings for the versioned planning workflow.
- [ ] Validate isolated explicit-approval, withheld-approval, stale-request, and self-approval-request examples without altering actual user work.

- [ ] QA guidance presents source-identified review reports, open findings and human disposition reasons alongside candidate evidence; recording a review decision never substitutes for the exact separate QA acceptance.

### Verification

Skill validation and isolated QA examples cover explicit approval, withheld approval, and stale candidate identities using disposable artifacts.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/26-propose-versioned-qa-corrections.md -->

<a id="r08-propose-a-versioned-correction-plan"></a>

## 26: Propose a versioned correction plan

**What to build:** Extend the unified planning flow for QA feedback: propose focused correction tickets and affected spec/milestone changes, show the changes from the approved version, and obtain targeted approval. Unchanged requirements retain their approval; prior versions and completed-ticket history remain intact.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [25: Guide a human through milestone QA](#25-guide-a-human-through-milestone-qa).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R08](#r08-propose-a-versioned-correction-plan).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [corrections and safe continuation](spec.md#corrections-and-safe-continuation).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Use the unified planning workflow to turn QA findings into focused correction-ticket and affected spec/milestone proposals.
- [ ] Show changes from the approved version, retain approval of unchanged requirements, and reopen targeted grilling for substantive unresolved decisions.
- [ ] Keep unapproved changes staged; publish only explicitly accepted amendments with a new plan version and stable IDs/history.
- [ ] Preserve prior snapshots, completed-ticket evidence, decisions, and the current milestone's gate on later work.
- [ ] Demonstrate feedback updating both the proposal and staged spec consistently. Runtime execution of amendments belongs to ticket 27.

- [ ] A proposed review follow-up that changes approved scope, ownership or milestone conditions enters the versioned amendment workflow with its originating finding and human rationale linked; captured prior review/plan/QA inputs remain unchanged.

### Verification

A QA feedback example produces a revised proposal, updates the staged spec consistently, leaves unapproved changes unpublished, and publishes only the accepted amendment. Runtime execution belongs to ticket 27.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/27-execute-approved-qa-corrections.md -->

<a id="r09-execute-approved-qa-corrections"></a>

## 27: Execute approved QA corrections

**What to build:** Accept an approved amendment at the QA boundary without editing captured prior inputs. Run its corrections through existing ticket gates inside the current milestone, retain version/evidence lineage, prepare a fresh candidate, and require renewed QA. Later groups remain gated.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [26: Propose a versioned correction plan](#26-propose-a-versioned-correction-plan).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R09](#r09-execute-approved-qa-corrections).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [corrections and safe continuation](spec.md#corrections-and-safe-continuation); [independent checks and exact revisions](spec.md#independent-checks-and-exact-revisions).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Accept an explicitly approved versioned amendment at the current QA boundary without editing captured prior inputs or executing unapproved corrections.
- [ ] Execute correction tickets through fresh implementation/repair assignments, independent checks, both reviews, and exact feature-candidate gates.
- [ ] Retain plan-version lineage, prior Done history, rejected evidence, and the distinction between QA corrections and bounded in-assignment repairs.
- [ ] Prepare a fresh dev candidate and require renewed human acceptance; old approval cannot accept changed source and later groups remain gated.
- [ ] Demonstrate QA rejection, targeted amendment approval, correction, renewed QA, and continuation through the scripted public seam.

- [ ] Approved correction execution links its originating review finding, human amendment decision, repair/implementation revision and renewed review evidence, without relabeling a finding disposition as candidate acceptance.

### Verification

A scripted QA rejection leads to an approved correction, a new candidate and decision, then continuation. Old approval cannot accept the corrected revision; an unapproved amendment cannot run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/28-operate-the-harness-in-the-background.md -->

<a id="r10-operate-the-orchestrator-in-the-background"></a>

## 28: Operate the orchestrator in the background

**What to build:** Add normal CLI background launch returning a run identity, observational status/log access, documented stopping controls, and foreground mode. QA waiting survives closing the launching terminal; the separate QA session writes its artifact. Specify active-stage stopping behavior without claiming unsupported restart recovery.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R10](#r10-operate-the-orchestrator-in-the-background).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [public interface and approval](spec.md#public-interface-and-approval); [corrections and safe continuation](spec.md#corrections-and-safe-continuation).

### Acceptance criteria

- [ ] Provide normal CLI background launch returning a run identity, foreground debugging, observational status/log access, and documented stopping controls.
- [ ] Keep execution and QA waiting independent of the launching terminal; the separate QA session writes the approval artifact.
- [ ] Support clean stop/continuation at QA through ticket 15's contract; document active-stage stop outcomes without claiming arbitrary recovery.
- [ ] Preserve durable process/evidence identity and descendant cleanup; background launch success is distinct from feature completion.
- [ ] Verify launch, logs/status, terminal independence, waiting/approval-driven progress, clean QA stop/restart, and cleanup using offline scripted subprocesses.

### Verification

Scripted subprocess tests observe launch, logs/status, waiting, approval-driven continuation, clean QA stop/restart, and descendant cleanup. Do not require model or network access.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/29-continue-independent-work-after-blocks.md -->

<a id="r11-continue-independent-work-inside-the-current-milestone"></a>

## 29: Continue independent work inside the current milestone

**What to build:** Retain pre-QA ticket 10's blocked-root/waiting-dependent/unrelated-success behavior and shared-environment stopping. Unrelated work is eligible only within the current milestone; a block or exhausted repair cannot bypass a QA boundary or produce feature success.

**Blocked by:** [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md); [06: Stop for decisions outside approved contracts](../../issues/06-surface-human-decisions-without-retrying.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R11](#r11-continue-independent-work-inside-the-current-milestone).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [ticket lifecycle](spec.md#ticket-lifecycle); [bounded failures and timeouts](spec.md#bounded-failures-and-timeouts).

### Acceptance criteria

- [ ] Keep human-decision/exhausted-repair tickets Blocked and their dependent tickets Pending without implicit retries.
- [ ] Continue unrelated ready work inside the current milestone from the latest verified feature revision; no ticket from a later milestone starts.
- [ ] Stop when no executable current-milestone work remains and accurately distinguish Done, Blocked, dependency-waiting, and QA-waiting states.
- [ ] Return an incomplete outcome for unresolved required work even if unrelated tickets succeeded; shared environment/integrity failures stop the run.
- [ ] Demonstrate a blocked root, waiting dependent, unrelated success, and later-group ticket that remains unstarted, retaining each ticket's evidence.

### Verification

Reuse the pre-QA ticket 10 fixture requirements, adding later-group work that must remain unstarted. Preserve accurate incomplete and waiting outcomes.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R11; the [previous definition](../../archive/issues-before-milestone-qa/10-continue-independent-work-after-blocks.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/30-supply-combined-design-guidance-to-standards-review.md -->

<a id="r12-supply-coherent-design-guidance-to-standards-review"></a>

## 30: Supply coherent design guidance to Standards review

**What to build:** Retain the design-policy and Standards-role portion of pre-QA ticket 11, auditing current custom guidance and synthesizing Matt/Microsoft principles with Pythonic functions and objects. Deliver the required policy/role context explicitly through the existing assignment seam. Evidence-based blockers remain distinct from optional suggestions.

**Blocked by:** [03: Reject invalid agent reports and review evidence](../../issues/03-validate-agent-reports-and-review-evidence.md); [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R12](#r12-supply-coherent-design-guidance-to-standards-review).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [custom skills and design policy](spec.md#custom-skills-and-design-policy); [cohesive module responsibilities](spec.md#cohesive-module-responsibilities).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Audit current custom guidance and create one combined design authority with focused references for deep modules, information hiding, cohesive responsibility/invariant ownership, composition, substitutability, justified injection, and behavioral tests.
- [ ] Support Pythonic functions, objects and combinations without mandating speculative patterns or class hierarchies.
- [ ] Create Standards guidance respecting project rules and accepted ADRs; blockers need concrete evidence and consequences, while preferences remain optional.
- [ ] Reuse custom test-strategy review guidance without adding a reviewer or gate, and explicitly supply required design/Standards context through the existing assignment seam.
- [ ] Validate skills and concrete design examples; capture Standards inputs in a separate scripted repository. Generic default/addition capture and source-edit stability are owned by ticket 31.

- [ ] Explicitly deliver the evaluated ownership/cross-module review contract and its scope/coverage declaration through the existing Standards assignment seam. Capture actual scripted delivered instruction identities; cumulative runtime scheduling remains ticket 33.

### Verification

Validate skills, inspect concrete design examples, and capture actual Standards-assignment inputs in a separate scripted target repository. Generic additive skill selection is isolated in ticket 31.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R12; the [previous definition](../../archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/31-capture-and-deliver-selected-local-skills.md -->

<a id="r13-capture-and-deliver-selected-local-skills"></a>

## 31: Capture and deliver selected local skills

**What to build:** Retain pre-QA ticket 11's generic role/default/addition contract: explicitly resolve local sources and required references, capture origin/source/content identities, reject missing content, and record actual delivery. Repairs receive captured instructions even after source edits. Keep the planning reference aligned with this canonical metadata.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [30: Supply coherent design guidance to Standards review](#30-supply-coherent-design-guidance-to-standards-review).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R13](#r13-capture-and-deliver-selected-local-skills).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [skill selection and delivery](spec.md#skill-selection-and-delivery); [agent contracts and access](spec.md#agent-contracts-and-access).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Document one canonical additive skill-selection/source-resolution contract compatible with the planning reference and tickets without additions.
- [ ] Support explicit local harness, target-repository, and installed-library sources; role-specific ticket additions preserve project defaults and mandatory role/access/output contracts.
- [ ] At run start capture selected skills and required local references with role, selection origin, source identity and content identity; reject missing required content before affected assignments.
- [ ] Deliver captured instructions explicitly and record actual delivered content; repairs use captured content despite later source edits.
- [ ] Demonstrate defaults, role-specific additions, missing references and edits after capture in a separate scripted target repository; preserve upstream files and defer discovery/download/installation.

- [ ] Capture the selected shared review contract and required references under the existing role/default/addition mechanism, retaining source identities and stable delivered content across repairs.

### Verification

Scripted cross-repository assignments exercise defaults, role-specific additions, missing references, and source edits after capture without adding live-model variations.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/32-deliver-focused-implementation-and-spec-review-contexts.md -->

<a id="r14-deliver-focused-implementation-and-spec-contexts"></a>

## 32: Deliver focused implementation and Spec contexts

**What to build:** Retain pre-QA ticket 12's distinct implementation/repair/Spec guidance and fresh context assembly. Supply milestone and ticket constraints while keeping reviews, commits, promotions, state changes, and human approval under harness control. Reuse shared design and test strategy without copying the whole upstream library.

**Blocked by:** [31: Capture and deliver selected local skills](#31-capture-and-deliver-selected-local-skills); [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R14](#r14-deliver-focused-implementation-and-spec-contexts).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Create focused implementation/repair guidance for one ticket's contracts, approved behavioral seams, custom test-strategy coverage selection, TDD where needed, evidence, and out-of-scope decisions.
- [ ] Create separate Spec-review guidance for missing, incorrect and unrequested behavior against approved requirements.
- [ ] Provide every assignment fresh role context, captured defaults/additions and scoped references; repairs use the captured version even after source-library edits.
- [ ] Supply exact reviewed revision, relevant source/diff and actual check outcomes to Spec review, with only relevant design guidance for implementers.
- [ ] Keep nested-review orchestration, commits, integration, QA acceptance, state and completion under harness authority; record actual selection origins/content identities and demonstrate a fresh repair.

- [ ] Implementation/repair and Spec contexts include relevant ownership contracts, prior finding identities/dispositions and exact reviewed source/check evidence, while reviewers remain independently assigned and completed prior reports remain immutable.

### Verification

Captured scripted implementation, repair, and Spec assignments show scoped requirements, exact reviewed revisions, stable selected guidance, and role separation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R14; the [previous definition](../../archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/33-enforce-traceable-runtime-review-checkpoints.md -->

## 33: Enforce traceable runtime review checkpoints

**What to build:** Carry the evaluated review contract into the runtime as traceable per-ticket and cumulative assessment records. Enforce scoped review completion, findings and architecture checkpoints before affected integration and milestone QA readiness, using scripted processes first so the real-agent ticket consumes an already verified lifecycle.

**Blocked by:** [19: Evaluate reviewers on known and acceptable designs](#19-evaluate-reviewers-on-known-and-acceptable-designs); [24: Own milestone review and checkpoint continuation](#24-own-milestone-review-and-checkpoint-continuation); [30: Supply coherent design guidance to Standards review](#30-supply-coherent-design-guidance-to-standards-review); [31: Capture and deliver selected local skills](#31-capture-and-deliver-selected-local-skills); [32: Deliver focused implementation and Spec contexts](#32-deliver-focused-implementation-and-spec-contexts).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md), review-process-1 draft revision.

**Milestone:** M3. Follow [membership and human QA](milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](spec.md#role-configuration), [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](../../../../../../.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](spec.md#review-work-findings-and-decisions); [ownership and review scope](spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](spec.md#reviewer-evaluation); [verification](spec.md#review-process-verification); [role defaults](spec.md#role-configuration); [runtime adoption](spec.md#runtime-review-adoption); [exact revisions](spec.md#independent-checks-and-exact-revisions); [QA](spec.md#feature-to-development-promotion-and-human-qa). Respect [domain terms](../../../../GLOSSARY.md), [ADR-0001](../../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Runtime ticket reviews retain separate fresh Spec/Standards reports and exact revision identities, supplied ownership contracts, prior findings/dispositions and actual inspected/omitted scope. Record review/report identities, instruction/settings identities, finding keys and repair/verification links in additive harness-owned artifacts, with observational status/navigation exposing pending reviews and decisions.
- [ ] Implement the shared milestone-boundary and risk-trigger architecture assessments through an explicitly identified cumulative scope using Standards, rather than silently treating it as an ordinary ticket attempt or adding an unconditional third ticket reviewer. Pin source/cumulative baseline and inventory, preserve separate review history, and reject missing, incomplete or stale assessments before affected integration or QA readiness.
- [ ] Ordinary in-scope ticket blockers follow existing bounded repair policy; a cumulative blocker that cannot be corrected under that policy, a proposed scope/ownership change or consequential risk decision preserves work and stops with an incomplete human-decision handoff, without inventing extra repairs. Resolve it through an explicitly authorized amendment/fresh run with prior evidence linked; a disposition alone cannot resume a stopped run. Such work cannot integrate or obtain a consumable QA request while required blocking review work is unresolved. Optional findings retain inspectable dispositions and do not trigger repairs merely for being optional.
- [ ] Human review decisions remain separate from exact-candidate QA acceptance. Validate the review/scope/revision/finding identity and explicit reason before applying a disposition; agents cannot author their own consequential acceptance. Review completion, findings dispositioned, candidate awaiting QA, milestone promoted and feature complete remain distinct recorded outcomes.
- [ ] Keep immutable reports, append-only disposition history and completed work linked across deliberate stop/continue. Produce required review artifacts before freezing QA evidence; during a frozen QA wait, reject edits or preserve new proposals outside the frozen evidence and require renewed readiness/request as applicable. Preserve legacy report identity/finding fields, checkpoint version 1, gate evidence and artifact names; new review state is additive/optional for old records and never creates legacy review attestations retroactively.
- [ ] Verify through the public CLI with scripted external processes and real isolated Git: clean ticket/cumulative review, missing coverage, stale source, duplicate local finding IDs, fixed/deferred/awaiting-decision histories, blocked readiness/integration, rejected unauthorized dispositions, optional-only progress, failed review invocation and deliberate continuation with preserved records. Extend guide/status contracts and retained evidence, with actual live-agent proof left to ticket 34.

### Verification

Map existing report, human-decision, repair, optional-finding, milestone and continuation scenarios first. Add only distinct new runtime review-history/checkpoint/authority cases at the existing public CLI/scripted-process/real-Git seam. Run the full final-source suite and static gates, plus installed CLI checks where this ticket changes entry points or their observable contract. Genuine old checkpoint compatibility remains required; new review artifacts cannot invalidate a frozen old checkpoint merely by being introduced.

Use the [testing policy](../../../../docs/agents/testing.md), [Python environment](../../../../docs/agents/python-environment.md) and [shared review-process verification](spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](milestones.md); no automatic next-milestone execution or human acceptance is authorized.

<!-- Proposed publication: issues/34-run-a-real-codex-ticket-cycle.md -->

<a id="r15-complete-the-workflow-with-real-codex-roles"></a>

## 34: Complete the workflow with real Codex roles

**What to build:** Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [32: Deliver focused implementation and Spec contexts](#32-deliver-focused-implementation-and-spec-contexts); [08: Stop stalled assignments and check processes](../../issues/08-stop-timed-out-process-trees.md); [33: Enforce traceable runtime review checkpoints](#33-enforce-traceable-runtime-review-checkpoints).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R15](#r15-complete-the-workflow-with-real-codex-roles).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](spec.md#codex-execution); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Verify installed Codex invocation and launch fresh implementation/repair/review processes with explicit working directory, sandbox, positive timeout, model, and output contract; do not silently substitute models.
- [ ] Apply Medium implementation/repair and High Spec/Standards defaults with independently configurable role profiles; validate ticket worker overrides and inherit them in repairs without changing reviewers.
- [ ] Capture machine-readable events and schema-validated reports with actual model/reasoning settings and supplied instruction identities.
- [ ] Demonstrate cross-repository delivery of required custom role/design guidance, project defaults and a role-specific addition, without assuming automatic discovery.
- [ ] Complete a tiny actual implementation plus two independent actual reviews and exact candidate integration within the established milestone workflow; keep human QA approval separate from model results.
- [ ] Retain scripted offline routine checks and a separate explicit live check. Record actual evidence or a concrete blocker; a skipped live check is not completion.

- [ ] Use ticket 33's enforced review lifecycle with actual real-agent assignments, including an explicitly scoped cumulative assessment and a declared seeded concern plus acceptable control. Retain actual delivered guidance, inspected scope, findings/dispositions and exact readiness/QA outcomes; scripted success or M1 development evaluation cannot substitute for live runtime proof.

### Verification

Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R15; the [previous definition](../../archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/35-compare-configurable-agent-context-limits.md -->

<a id="r16-run-the-early-context-budget-comparison"></a>

## 35: Run the early context-budget comparison

**What to build:** Retain pre-QA ticket 17's 100K/150K/200K/250K controls, fixed workload and reasoning settings, genuine context-pressure case, repetitions, raw measurements, and acceptance checks. Distinguish hard enforcement, compaction thresholds, and advisory targets; active occupancy is separate from cumulative/cached usage.

**Blocked by:** [34: Complete the workflow with real Codex roles](#34-complete-the-workflow-with-real-codex-roles).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** E1 (independent context experiment; not a release gate). Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R16](#r16-run-the-early-context-budget-comparison).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](spec.md#codex-execution); [agent contracts and access](spec.md#agent-contracts-and-access).

### Acceptance criteria

- [ ] Expose 100000, 150000, 200000 and 250000 active-context settings, starting at 250000; verify enforcement, compaction signals or advisory behavior without claiming an unsupported hard cap.
- [ ] Measure peak active context separately from cumulative input/output and cached usage, recording role, attempt, model, reasoning, and configured limit.
- [ ] Use a fixed bounded workload and acceptance suite, consistent settings and documented repetitions at every limit.
- [ ] Include both a short control and a task-relevant pressure case capable of approaching thresholds; below-100K runs cannot establish comparative higher-limit effects.
- [ ] Report verified outcomes, failures, repairs, compactions/handoffs, elapsed time and raw usage evidence; context pressure cannot bypass gates.
- [ ] Publish reproducible findings and limitations without silently changing defaults. Execute immediately after ticket 34 under independent experiment checkpoint E1; do not add release, comprehensive access, background, or completed planning-integration gates.

### Verification

Preserve the current ticket's explicit experiment evidence requirements. Prioritize immediately after ticket 34, before comprehensive boundary probes or release packaging. It remains independent of first-release acceptance dependencies.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R16; the [previous definition](../../archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/36-verify-role-write-boundaries.md -->

<a id="r17-verify-runtime-write-and-approval-boundaries"></a>

## 36: Verify runtime write and approval boundaries

**What to build:** Retain pre-QA ticket 14's real sandbox probes and add QA decisions, dev, and feature refs to the protected authority checks. Implementers may edit assigned source; reviewers remain read-only; implementation/repair cannot authorize promotion. Do not silently widen permissions or treat a prompt instruction as proof of enforcement.

**Blocked by:** [25: Guide a human through milestone QA](#25-guide-a-human-through-milestone-qa); [34: Complete the workflow with real Codex roles](#34-complete-the-workflow-with-real-codex-roles).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R17](#r17-verify-runtime-write-and-approval-boundaries).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [feature to development promotion and human qa](spec.md#feature-to-development-promotion-and-human-qa).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Verify an implementer can edit only assigned source while reviewers have read-only source sufficient to produce their reports.
- [ ] Probe disposable sentinels for sibling source, approved inputs, authoritative records, QA decisions, and feature/development refs; refuse or detect out-of-scope effects before acceptance.
- [ ] Keep submission capture, both integration destinations, QA decision consumption and execution state under harness authority; implementation/repair cannot authorize acceptance.
- [ ] Reject assignments when required access/instruction guarantees cannot be established; do not silently widen permissions or substitute prompt claims for probes.
- [ ] Record actual backend/sandbox/file/ref observations while preserving caller work and approved inputs.

- [ ] Exercise reviewer read-only source/report/disposition authority and protection of human review decisions separately from QA acceptance, including attempts to rewrite review history or self-accept a consequential risk.

### Verification

Existing disposable sentinel probes plus QA/ref targets provide concrete access evidence without touching caller work. A failed access guarantee leaves verification incomplete.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R17; the [previous definition](../../archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/37-run-a-generated-plan-through-the-runtime.md -->

<a id="r18-run-a-generated-approved-plan-through-the-runtime"></a>

## 37: Run a generated approved plan through the runtime

**What to build:** Complete the remaining integration portion of pre-QA ticket 15. Produce a small plan through the unified skill, validate it against the now-implemented milestone/skill contracts, and execute it through the scripted public seam. Demonstrate project-default guidance and a role-specific ticket addition, preserving required contracts.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [27: Execute approved QA corrections](#27-execute-approved-qa-corrections); [31: Capture and deliver selected local skills](#31-capture-and-deliver-selected-local-skills).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R18](#r18-run-a-generated-approved-plan-through-the-runtime).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [skill selection and delivery](spec.md#skill-selection-and-delivery).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Generate a small human-approved spec/ticket/milestone bundle through the unified planning skill and validate it against the implemented canonical contracts.
- [ ] Demonstrate explicit project defaults and an applicable role-specific ticket addition, plus a ticket requiring no additions, preserving mandatory role guidance.
- [ ] Run the approved example through intentional scripted CLI execution, reaching planned QA and exact local promotion with captured/delivered instruction identities.
- [ ] Keep publishing distinct from execution and QA planning distinct from acceptance; preserve original inputs and evidence.
- [ ] Include interfaces, invariants, testing seams, Pythonic shared design, and appropriate test strategy without replaying all selection validation already covered by ticket 31.

- [ ] Run a generated approved plan carrying ownership/review metadata and required checkpoint scope, verifying backward-compatible tickets without additions and exact linkage of review history to implementation and milestone evidence.

### Verification

A generated example reaches QA and promotion with recorded selection/content identities. Planning publication does not itself launch execution; the example uses an explicit run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/38-demonstrate-the-first-usable-release.md -->

<a id="r19-demonstrate-the-revised-first-usable-release"></a>

## 38: Demonstrate the revised first usable release

**What to build:** Expand pre-QA ticket 16's clean-checkout acceptance to planning, background operation, two QA milestones, corrections, safe checkpoint continuation, exact local promotions, blocked/waiting work, optional findings, selected guidance, and actual Codex/access evidence. Clearly document deferred concurrency, arbitrary crash recovery, hosted PRs/GitHub checks, and email.

**Blocked by:** [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md); [28: Operate the orchestrator in the background](#28-operate-the-orchestrator-in-the-background); [29: Continue independent work inside the current milestone](#29-continue-independent-work-inside-the-current-milestone); [36: Verify runtime write and approval boundaries](#36-verify-runtime-write-and-approval-boundaries); [37: Run a generated approved plan through the runtime](#37-run-a-generated-approved-plan-through-the-runtime); [07: Report optional review suggestions without rework](../../issues/07-report-optional-suggestions-without-repair.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R19](#r19-demonstrate-the-revised-first-usable-release).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [testing decisions](spec.md#testing-decisions); [out of scope](spec.md#out-of-scope).

**Review amendment:** Inherit [review records](spec.md#review-work-findings-and-decisions), [runtime adoption](spec.md#runtime-review-adoption) and [architecture checkpoints](spec.md#cumulative-architecture-checkpoints).

### Acceptance criteria

- [ ] Document installation, actual CLI/background/foreground/status/log/stop/continue interfaces, role settings, limits, requirements, skill selections and artifact/decision inspection.
- [ ] Provide a clean-checkout disposable example covering two milestones, planned QA waits, explicit approval, correction-plan amendment, safe continuation and exact feature-to-dev promotion.
- [ ] Retain repaired/blocked/dependent/unrelated/optional-finding examples and final feature acceptance without bypassing any QA boundary.
- [ ] Run the complete deterministic suite and required static/packaging/installed CLI checks without routine model credentials or network access.
- [ ] Retain actual small Codex/skill/access evidence or report its blocker; show immutable approved inputs and exact candidate-bound branch advancement.
- [ ] Clearly separate sequential operation and planned-QA continuation from deferred concurrency, arbitrary crash recovery, hosted PR/GitHub checks, and email. Context experiment 35 is prioritized separately, not a release gate.

- [ ] The final walkthrough includes navigable review work, immutable reports, a concern-to-human-decision-to-change-to-verification history, cumulative architecture assessment and unresolved-finding visibility across stop/continue; human final acceptance remains separate.

### Verification

Run the existing required complete suite and packaging/installed CLI checks, follow the documented disposable-repository walkthrough, and retain actual live evidence or its explicit blocker. Ticket 35 is scheduled early but is not a prerequisite for release acceptance.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R19; the [previous definition](../../archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

## Prior decomposition and history

The [prior approved proposal](../../ticket-proposal.md) retains historical R01–R19 requirements; current owners follow the [numbering map](numbering-map.md). The earlier unapproved five-refactor-only draft remains under `drafts/oop-v2-before-review-process/`. Completed-ticket reports/evidence and historical decisions remain unchanged.

### Completed stable slices

<a id="r01-turn-one-grilling-session-into-an-approved-plan"></a>

- R01: [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md) — completed; retain original evidence.

<a id="r02-stop-development-handoffs-at-human-checkpoints"></a>

- R02: [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md) — completed; retain original evidence.

<a id="r03-execute-only-the-first-eligible-milestone"></a>

- R03: [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md) — completed; retain original evidence.

<a id="r04-present-a-tested-feature-to-dev-candidate"></a>

- R04: [13: Present a tested feature-to-dev candidate](../../issues/13-prepare-a-tested-feature-to-dev-candidate.md) — completed; retain original evidence.

<a id="r05-consume-approval-promote-and-continue"></a>

- R05: [14: Consume approval, promote, and continue](../../issues/14-promote-only-the-human-approved-milestone.md) — completed; retain original evidence.

<a id="r06-continue-after-a-deliberate-qa-stop"></a>

- R06: [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md) — completed; retain original evidence.

<a id="comparison-with-the-pre-qa-open-tickets"></a>

The [prior approved comparison](../../ticket-proposal.md#comparison-with-the-pre-qa-open-tickets) retains earlier decomposition identities. Use current milestone membership and the numbering map for new work.

## Supporting publication updates

The [exact supporting changes](publication-updates.md) and [domain additions](domain-additions.md) are part of this current bundle. Their canonical sources remain unchanged pending approval.
