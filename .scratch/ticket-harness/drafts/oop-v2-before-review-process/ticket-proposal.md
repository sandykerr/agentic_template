# Ticket harness ownership amendment and complete open-ticket proposal

**Draft — unapproved. Plan version:** oop-v2.

Review the [spec](spec.md), full ticket bodies below, [milestones](milestones.md), [index](README.md), [numbering map](numbering-map.md) and supporting publication updates as one bundle. Intended destination: `.scratch/ticket-harness/`, with one approved ticket per file under `issues/`. Canonical authoring files remain unchanged pending publication approval.

## Change summary

- Cover all seven architecture findings in five complete refactor slices: attempts/report outcomes, ticket repairs, prepared inputs/returned checked plans, run lifecycle/verification restoration, and milestone review/checkpoint ownership.
- Preserve completed 01–15 and every unchanged feature requirement. Insert new 16–20 into M1; published open 16–28 become 21–33. Retain stable R-slice identities and the old-to-new mapping.
- M1 becomes 10–20, M2 21–25, M3 26–29, independent E1 30, and final M4 31–33. M1 QA remains not requested/accepted, and later milestones stay gated.
- Keep runner-owned checking, commands, failure precedence, saved JSON/checkpoint formats, artifact names and genuine old-checkpoint compatibility. Retain current role defaults, the agreed testing seam and required final-source verification.
- The earlier oop-v1 three-ticket proposal remains unapproved historical planning material. This expanded draft carries forward its contracts and adds input/run ownership; it does not implement later release features or change ADRs/domain meanings.

## Shared understanding and publication decision

The human requested these refactors in M1, authorized reordering open tickets to preserve a consecutive execution sequence, and answered “1. yes” to the five-ticket scope/granularity proposal. These decisions authorize this complete draft. Coherent-bundle publication approval is pending; planning does not implement tickets, start execution or accept a milestone.

<a id="published-slice-to-ticket-mapping"></a>

## Preferred order, dependencies and membership

Preferred order is completed 01–15, new M1 work 16–20, M2 21–25 after M1 acceptance, M3 26–29 after M2 acceptance, independent experiment 30 immediately after verified 29, then M4 31–33 after M3 acceptance. Numbers express preferred execution order; declared dependencies express actual prerequisites.

| Ticket | Stable slice | Prerequisites | Membership | Worker override |
| --- | --- | --- | --- | --- |
| [16: Own implementation-attempt transitions](#16-own-implementation-attempt-transitions) | O01 | 05, 06 | M1 | None; inherit Medium |
| [17: Own ticket execution and bounded repairs](#17-own-ticket-execution-and-bounded-repairs) | O02 | 16 | M1 | None; inherit Medium |
| [18: Return clearly prepared inputs](#18-return-clearly-prepared-inputs) | O04 | 02, 12 | M1 | None; inherit Medium |
| [19: Own the complete run lifecycle](#19-own-the-complete-run-lifecycle) | O05 | 15, 17, 18 | M1 | None; inherit Medium |
| [20: Own milestone review and checkpoint continuation](#20-own-milestone-review-and-checkpoint-continuation) | O03 | 15, 19 | M1 | None; inherit Medium |
| [21: Guide a human through milestone QA](#21-guide-a-human-through-milestone-qa) | R07 | 10, 14 | M2 | None; inherit Medium |
| [22: Propose a versioned correction plan](#22-propose-a-versioned-correction-plan) | R08 | 10, 21 | M2 | None; inherit Medium |
| [23: Execute approved QA corrections](#23-execute-approved-qa-corrections) | R09 | 15, 22 | M2 | None; inherit Medium |
| [24: Operate the orchestrator in the background](#24-operate-the-orchestrator-in-the-background) | R10 | 15 | M2 | None; inherit Medium |
| [25: Continue independent work inside the current milestone](#25-continue-independent-work-inside-the-current-milestone) | R11 | 12, 06 | M2 | None; inherit Medium |
| [26: Supply coherent design guidance to Standards review](#26-supply-coherent-design-guidance-to-standards-review) | R12 | 03 | M3 | None; inherit Medium |
| [27: Capture and deliver selected local skills](#27-capture-and-deliver-selected-local-skills) | R13 | 10, 26 | M3 | None; inherit Medium |
| [28: Deliver focused implementation and Spec contexts](#28-deliver-focused-implementation-and-spec-contexts) | R14 | 27 | M3 | None; inherit Medium |
| [29: Complete the workflow with real Codex roles](#29-complete-the-workflow-with-real-codex-roles) | R15 | 15, 28, 08 | M3 | None; inherit Medium |
| [30: Run the early context-budget comparison](#30-run-the-early-context-budget-comparison) | R16 | 29 | E1 | None; inherit Medium |
| [31: Verify runtime write and approval boundaries](#31-verify-runtime-write-and-approval-boundaries) | R17 | 21, 29 | M4 | None; inherit Medium |
| [32: Run a generated approved plan through the runtime](#32-run-a-generated-approved-plan-through-the-runtime) | R18 | 10, 23, 27 | M4 | None; inherit Medium |
| [33: Demonstrate the revised first usable release](#33-demonstrate-the-revised-first-usable-release) | R19 | 11, 24, 25, 31, 32, 07 | M4 | None; inherit Medium |

New 16 uses completed repair/decision contracts 05/06. New 17 consumes 16's attempt operations. New 18 preserves completed 02's preflight and 12's plan-validation contracts and can land independently of 16/17. New 19 consumes the completed ticket-execution and prepared-input interfaces from 17/18 and the implemented deliberate-continuation contract from 15. New 20 uses 19's run lifecycle and verification export/restoration operations plus completed 15's checkpoint rules. No additional edge is added solely to enforce numeric order. Later tickets retain their actual existing prerequisites; M1 acceptance supplies their refactor gate.

## Testing and review contracts

Use [refactor verification](spec.md#oop-refactor-verification), [role defaults](spec.md#role-configuration) and each ticket's coverage map. Preserve the public CLI with scripted external processes, real isolated Git repositories and observable records. Map existing cases before adding coverage; new cases must detect a distinct missing failure. Ownership is reviewed through the implementation diff, with no mandated class-shape tests. Genuine old-checkpoint continuation must retain producer/source provenance. Each final implementation ticket retains the full suite, strict typing, lint, format, whitespace and independent Spec/Standards reviews required by policy.

## Milestone definitions and QA

The full [milestone definitions](milestones.md) specify fixed membership, setup, human actions, pass conditions and evidence. All QA states remain not requested/accepted. Final M4 accepts every required release outcome cumulatively; independent E1 never gates release.

## Full proposed open-ticket bodies

New 16–20 add refactor requirements. Existing open tickets become 21–33 with their accepted criteria and genuine dependencies preserved except for current-reference renumbering and explicit inherited metadata.

<!-- Proposed publication: issues/16-own-implementation-attempt-transitions.md -->

## 16: Own implementation-attempt transitions

**What to build:** Give each implementation attempt responsibility for its own lifecycle observations. Submission, rejection, completion and human-decision handoff update the correct attempt and ticket consistently, while the runner continues to execute checks and validate reports. Complete the migration of existing callers within this ticket so the CLI stays usable.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](../../issues/05-repair-rejected-submissions-within-budget.md); [06: Stop for decisions outside approved contracts](../../issues/06-surface-human-decisions-without-retrying.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] Attempt-owned operations maintain the existing Running, Verifying, Rejected and Done observations, revision identities, changed-file observations, and inclusive/exclusive gate ranges. Corresponding current-ticket observations remain consistent, including failures before a submission exists.
- [ ] The runner retains check execution, report validation, source-evidence invalidation and failure precedence. It communicates validated human-decision evidence to the owning attempt without selecting an attempt through the last entry in shared history or mutating its lifecycle record directly. Report parsing and validation return their findings or failure information; they do not mutate the canonical gate record. The runner records the final report/check status, preserving report content and diagnostics on rejected reports and the current precedence among process exit, timeout, report validity, blocking findings, human decisions and integrity/environment failures.
- [ ] Implementation and either review axis can stop the correct initial or repair attempt for a validated human decision, including a nonzero process exit. Preserve the complete handoff on both existing record locations, preserved work, diagnostic, Blocked/incomplete outcome, and immediate stop without later gates or extra repairs.
- [ ] Malformed decision-like reports, optional findings, ordinary report/process failures and timeouts retain their existing distinct validation and bounded-failure behavior; they cannot gain decision authority or produce false success.
- [ ] Public commands, exit behavior, record keys/values, artifact naming, historical attempt evidence and caller/approved-input protection remain compatible. Atomic persistence still exposes meaningful intermediate observations.
- [ ] Design review confirms transition rules live with attempt state and callers use those operations; private naming/layout remains an implementation choice, with no getter/setter-only wrapper or inheritance framework.

### Verification

Map existing repair/history and human-decision cases, including initial/later attempts, implementation/either-axis decisions, decision precedence and durable status output. Prior art: `tests/test_repairs.py`, `tests/test_human_decisions.py`, `tests/test_optional_suggestions.py`, `tests/test_timeouts.py` and multi-ticket attempt-history cases in `tests/test_dependencies.py`. Preserve report validation and integrity regression coverage. Include existing `tests/test_reports.py` coverage for malformed reports, valid reports with failed processes, and preserved diagnostics.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/17-own-ticket-execution-and-bounded-repairs.md -->

## 17: Own ticket execution and bounded repairs

**What to build:** Give one ticket execution ownership of its complete implementation, verification and bounded repair cycle. Keep the original approved base, current attempt, repair starting revision, previous source worktree and failure context together. Use the attempt lifecycle delivered by ticket 16; finish the caller migration so existing selected-ticket runs stay green.

**Blocked by:** [16: Own implementation-attempt transitions](#16-own-implementation-attempt-transitions).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] A ticket execution owns the complete cycle and repair policy through a small interface. The runner coordinates eligible tickets and retains checking; ticket workflow code no longer obtains unrestricted access to the runner merely to manipulate its shared state.
- [ ] The original ticket base remains fixed across attempts, while a repair starts from the observed rejected submission or preserved uncommitted work as applicable. Fresh assignments and worktrees receive the correct failure, rejected revisions, ticket-scoped evidence and configured check selection.
- [ ] Initial assignment plus configured repairs remains bounded. Repairable gate/Git/process/timeout failures, exhausted allowance, human decisions, environment/integrity failures and external ref/HEAD movement retain their existing repair-or-stop decisions and preserved history.
- [ ] Every changed submission receives renewed applicable checks, both independent reviews and an exact candidate suite. Earlier approval cannot authorize a repaired source; approved inputs, earlier evidence and the caller worktree stay protected.
- [ ] Only successful expected-old advancement of the integration branch records the exact tested candidate as Done and unlocks dependents. Later tickets use the current verified integration revision; existing fail-fast behavior after a blocked ticket remains unchanged until the separate blocked-work-isolation ticket.
- [ ] CLI behavior, single-/multi-ticket artifact names, baseline reuse, attempt numbering, gate ranges and saved record formats remain compatible. Existing readiness calculations and Git primitives remain functions where they provide no independent state lifetime.

### Verification

Map existing successful repair, invalid-report preservation, repair exhaustion, later-ticket fixed-base/history, evidence invalidation and external-integration scenarios. Prior art: `tests/test_repairs.py`, `tests/test_dependencies.py`, `tests/test_transaction.py` and `tests/test_timeouts.py`. This ticket does not implement later independent-work scheduling or add private-class tests.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/18-return-clearly-prepared-inputs.md -->

## 18: Return clearly prepared inputs

**What to build:** Make input preparation return one explicit, complete result containing validated execution settings, approved snapshots, normalized requirements, ticket selection, completion evidence and applicable worker settings. Keep raw settings separate from calculated values, and make all callers use the checked plan returned by validation. Complete caller migration while preserving current input acceptance, rejection, capture and execution behavior.

**Blocked by:** [02: Reject invalid requirements before starting work](../../issues/02-reject-invalid-inputs-before-execution.md); [12: Execute only the first eligible milestone](../../issues/12-execute-only-the-current-qa-milestone.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] The input-loading interface provides the complete prepared result and makes its filesystem preparation requirements explicit. The run consumes that result without repeating preparation rules or externally filling calculated fields into raw configuration. Existing configuration and approved input files remain byte-for-byte unchanged.
- [ ] One input preparation operation still validates executable commands, captures approved files and identities, normalizes tickets, validates dependency graphs and completion evidence, and establishes eligible selection and worker settings. Missing, malformed, conflicting or changed inputs retain existing diagnostics, invalid-input behavior and rejection before workers, checks or branch advancement.
- [ ] All plan consumers use the checked plan returned by validation, including first-milestone selection. Normalized membership, dependency order, role defaults and worker overrides remain governed together by plan validation; callers need not rely on mutation of the original plan object. Requiring validation to become a pure function is not part of this ticket.
- [ ] Legacy runs without a plan, versioned plans, externally completed prerequisites, explicit selections and primary-ticket handling retain their current behavior. Readiness, completion evidence, selected prerequisites, metadata conflicts, default/override inheritance and later-milestone eligibility rules remain intact.
- [ ] Snapshot hashes, copied input names, output separation, persisted configuration/checkpoint contents and status output remain compatible. Any new in-memory result representation is translated into the existing JSON-safe saved shape so pre-existing checkpoints and later restoration keep working.
- [ ] Pure parsing, normalization, graph checks and transformations remain ordinary functions where they own no independent lifecycle. The change introduces neither a configuration framework nor a new testing seam, and the full public CLI path is usable after this ticket.

### Verification

Map existing preflight/configuration, duplicate metadata, graph/selection/completion-evidence and plan-validation cases in `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`. In particular, preserve invalid-plan rejection before processes/ref changes, normalized first-group selection and worker-setting metadata. Check the implementation diff to confirm callers use the returned checked plan and prepared result; avoid tests that assert a particular result class or require mutation-free validation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/19-own-the-complete-run-lifecycle.md -->

## 19: Own the complete run lifecycle

**What to build:** Give the run ownership of its complete start/continue lifecycle: consume prepared inputs, establish branch and baseline identities, coordinate eligible ticket executions and milestones, classify failures, and finalize durable outcomes. Also make the run own export and restoration of verification references. Migrate existing callers and preserve the CLI throughout; the milestone workflow may remain behind its existing callable until ticket 20.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [17: Own ticket execution and bounded repairs](#17-own-ticket-execution-and-bounded-repairs); [18: Return clearly prepared inputs](#18-return-clearly-prepared-inputs).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] The run owns initialization and deliberate continuation through cohesive operations; an external orchestration function no longer patches configuration, source protection, milestone index and lifecycle records in a required sequence. Public run/continue functions retain output creation, exclusive ownership and existing rejection behavior as appropriate, then invoke the run lifecycle through a small interface.
- [ ] Fresh execution retains branch validation, the required matching base/integration commit, approved-input protection, exactly one baseline and no worker launches/repairs after a failed baseline. Baseline, invalid-input, environment/integrity and later workflow failures preserve their existing stage diagnostics, outcomes, blocked/pending observations and exit codes.
- [ ] The run coordinates the ticket-execution interface from ticket 17 using the prepared inputs from ticket 18. It owns current milestone progression and finalization while ticket and attempt operations own their lifecycle records; it retains current fail-fast scheduling and never starts later-milestone work before exact human acceptance.
- [ ] Continuation consumes a deliberate validated checkpoint without replaying completed tickets, baseline work, artifacts or decisions. It invalidates the stopped marker before resumed work and preserves milestone position, history, feature/development identities, stop exit 2, success exit 0 and existing failed/rejected-continuation behavior.
- [ ] The run provides the existing checkpoint-shaped export and reconstruction of verified-check information. QA no longer inspects the runner's internal tuple/list organization. Restoration resolves references to the canonical gates in the durable run record; later source invalidation changes those actual records, including after repeated stop/continue cycles.
- [ ] Commands, saved JSON schemas/values, checkpoint version and filenames, single-/multi-ticket and milestone artifact naming, process ownership, integrity safeguards and atomic persistence remain compatible. Leave Git/process/filesystem primitives as functions and avoid a separate checker object or generic lifecycle framework.

### Verification

Map existing fresh-run, failed shared baseline, invalid-input, sequential multi-ticket and run/status cases in `tests/test_cli.py`, `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`; map deliberate/new-process/repeated continuation, active-owner rejection and post-restore canonical-gate invalidation in `tests/test_continuation.py` and `tests/test_qa_promotion.py`. Keep the existing QA callable working during this slice. Continue a genuine pre-refactor checkpoint and retain producer/source provenance, rather than generating compatibility evidence solely with the refactored implementation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/20-own-milestone-review-and-checkpoint-continuation.md -->

## 20: Own milestone review and checkpoint continuation

**What to build:** Give one milestone review ownership of its tested candidate, exact QA request, frozen evidence identities, decision observations and deliberate stop/continuation lifecycle. Fresh preparation and restoration enter the same review rules. Complete caller migration while retaining runner-owned checks and existing human authority over promotion.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [19: Own the complete run lifecycle](#19-own-the-complete-run-lifecycle).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M1. Follow [membership and QA](milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](spec.md#state-and-decision-ownership), [refactor verification](spec.md#oop-refactor-verification), [ticket lifecycle](spec.md#ticket-lifecycle), [independent checks](spec.md#independent-checks-and-exact-revisions), [QA and promotion](spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../../GLOSSARY.md) and [ADR-0002](../../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

### Acceptance criteria

- [ ] A milestone review keeps its candidate/feature/development identities, request content and digest, evidence identities and last observed decision together. Fresh and restored reviews use the same approval, unchanged-source/evidence and expected-ref rules; the caller receives an explicit stopped-versus-promoted outcome instead of a Boolean whose meaning depends on implementation knowledge. Use the run-owned verification export/restoration interface from ticket 19 instead of reading the runner's internal verified-check collection.
- [ ] Only an explicit matching, unconsumed human approval advances both expected feature/development refs to the exact regression-tested candidate. Missing, unreadable, malformed, mismatched, stale and replayed decisions retain observable waiting/rejection behavior without consuming ticket repairs or starting later milestones.
- [ ] Deliberate stop preserves the existing checkpoint version/format, identities, observations and archived lineage. Continue in a new process validates all approved inputs, record/request/evidence/source identities, both refs and exclusive ownership, without replaying completed assignments, completed baseline work or consumed decisions.
- [ ] Continue a genuine deliberate checkpoint written by pre-refactor code as well as one written by the new code. After JSON restoration, later source invalidation updates the canonical gate in the durable run record rather than a detached copy; changed evidence/checkpoints/refs cannot authorize continuation or promotion.
- [ ] Milestone preparation/regression/promotion failure observations, indefinite waits, stop exit behavior, status, ticket-Done versus milestone-promoted versus feature-complete distinctions, command interfaces and record/artifact formats remain compatible.
- [ ] Keep runner-owned checking and source-validation authority. Do not introduce arbitrary crash recovery, background execution, correction-plan execution, new approval authority, or later milestone features in this refactor. Update code wayfinding to describe the final responsibilities.

### Verification

Map existing exact approval/promotion, stale/replay rejection, clean stop/new-process continuation, post-restore gate invalidation, changed checkpoint/evidence/ref rejection and repeated-stop lineage cases. Prior art: `tests/test_milestones.py`, `tests/test_qa_promotion.py`, `tests/test_continuation.py` and `tests/test_transaction.py`. Retain provenance for a disposable pre-refactor checkpoint and its continuation with the final implementation; reuse existing compatibility evidence only when it actually covers that source. No live Codex or new private seam is needed.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

<!-- Proposed publication: issues/21-guide-and-record-human-milestone-qa.md -->

<a id="r07-guide-a-human-through-milestone-qa"></a>

## 21: Guide a human through milestone QA

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

### Acceptance criteria

- [ ] Create a focused QA-session skill that reads the exact request/candidate and guides the human through planned checks, evidence inspection, and observable acceptance conditions.
- [ ] Record findings and withhold acceptance until the human explicitly approves; passing automated tests or an agent recommendation is insufficient.
- [ ] Write only the precise decision artifact for matching current identities, preserving provenance and rejecting stale requests.
- [ ] Do not implement corrections or change product source/integration refs; propose findings for the versioned planning workflow.
- [ ] Validate isolated explicit-approval, withheld-approval, stale-request, and self-approval-request examples without altering actual user work.

### Verification

Skill validation and isolated QA examples cover explicit approval, withheld approval, and stale candidate identities using disposable artifacts.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/22-propose-versioned-qa-corrections.md -->

<a id="r08-propose-a-versioned-correction-plan"></a>

## 22: Propose a versioned correction plan

**What to build:** Extend the unified planning flow for QA feedback: propose focused correction tickets and affected spec/milestone changes, show the changes from the approved version, and obtain targeted approval. Unchanged requirements retain their approval; prior versions and completed-ticket history remain intact.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [21: Guide a human through milestone QA](#21-guide-a-human-through-milestone-qa).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R08](#r08-propose-a-versioned-correction-plan).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [corrections and safe continuation](spec.md#corrections-and-safe-continuation).

### Acceptance criteria

- [ ] Use the unified planning workflow to turn QA findings into focused correction-ticket and affected spec/milestone proposals.
- [ ] Show changes from the approved version, retain approval of unchanged requirements, and reopen targeted grilling for substantive unresolved decisions.
- [ ] Keep unapproved changes staged; publish only explicitly accepted amendments with a new plan version and stable IDs/history.
- [ ] Preserve prior snapshots, completed-ticket evidence, decisions, and the current milestone's gate on later work.
- [ ] Demonstrate feedback updating both the proposal and staged spec consistently. Runtime execution of amendments belongs to ticket 23.

### Verification

A QA feedback example produces a revised proposal, updates the staged spec consistently, leaves unapproved changes unpublished, and publishes only the accepted amendment. Runtime execution belongs to ticket 23.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/23-execute-approved-qa-corrections.md -->

<a id="r09-execute-approved-qa-corrections"></a>

## 23: Execute approved QA corrections

**What to build:** Accept an approved amendment at the QA boundary without editing captured prior inputs. Run its corrections through existing ticket gates inside the current milestone, retain version/evidence lineage, prepare a fresh candidate, and require renewed QA. Later groups remain gated.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [22: Propose a versioned correction plan](#22-propose-a-versioned-correction-plan).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M2. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R09](#r09-execute-approved-qa-corrections).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [corrections and safe continuation](spec.md#corrections-and-safe-continuation); [independent checks and exact revisions](spec.md#independent-checks-and-exact-revisions).

### Acceptance criteria

- [ ] Accept an explicitly approved versioned amendment at the current QA boundary without editing captured prior inputs or executing unapproved corrections.
- [ ] Execute correction tickets through fresh implementation/repair assignments, independent checks, both reviews, and exact feature-candidate gates.
- [ ] Retain plan-version lineage, prior Done history, rejected evidence, and the distinction between QA corrections and bounded in-assignment repairs.
- [ ] Prepare a fresh dev candidate and require renewed human acceptance; old approval cannot accept changed source and later groups remain gated.
- [ ] Demonstrate QA rejection, targeted amendment approval, correction, renewed QA, and continuation through the scripted public seam.

### Verification

A scripted QA rejection leads to an approved correction, a new candidate and decision, then continuation. Old approval cannot accept the corrected revision; an unapproved amendment cannot run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/24-operate-the-harness-in-the-background.md -->

<a id="r10-operate-the-orchestrator-in-the-background"></a>

## 24: Operate the orchestrator in the background

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

<!-- Proposed publication: issues/25-continue-independent-work-after-blocks.md -->

<a id="r11-continue-independent-work-inside-the-current-milestone"></a>

## 25: Continue independent work inside the current milestone

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

<!-- Proposed publication: issues/26-supply-combined-design-guidance-to-standards-review.md -->

<a id="r12-supply-coherent-design-guidance-to-standards-review"></a>

## 26: Supply coherent design guidance to Standards review

**What to build:** Retain the design-policy and Standards-role portion of pre-QA ticket 11, auditing current custom guidance and synthesizing Matt/Microsoft principles with Pythonic functions and objects. Deliver the required policy/role context explicitly through the existing assignment seam. Evidence-based blockers remain distinct from optional suggestions.

**Blocked by:** [03: Reject invalid agent reports and review evidence](../../issues/03-validate-agent-reports-and-review-evidence.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R12](#r12-supply-coherent-design-guidance-to-standards-review).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [custom skills and design policy](spec.md#custom-skills-and-design-policy); [cohesive module responsibilities](spec.md#cohesive-module-responsibilities).

### Acceptance criteria

- [ ] Audit current custom guidance and create one combined design authority with focused references for deep modules, information hiding, cohesive responsibility/invariant ownership, composition, substitutability, justified injection, and behavioral tests.
- [ ] Support Pythonic functions, objects and combinations without mandating speculative patterns or class hierarchies.
- [ ] Create Standards guidance respecting project rules and accepted ADRs; blockers need concrete evidence and consequences, while preferences remain optional.
- [ ] Reuse custom test-strategy review guidance without adding a reviewer or gate, and explicitly supply required design/Standards context through the existing assignment seam.
- [ ] Validate skills and concrete design examples; capture Standards inputs in a separate scripted repository. Generic default/addition capture and source-edit stability are owned by ticket 27.

### Verification

Validate skills, inspect concrete design examples, and capture actual Standards-assignment inputs in a separate scripted target repository. Generic additive skill selection is isolated in ticket 27.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R12; the [previous definition](../../archive/issues-before-milestone-qa/11-supply-combined-design-guidance-to-standards-review.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/27-capture-and-deliver-selected-local-skills.md -->

<a id="r13-capture-and-deliver-selected-local-skills"></a>

## 27: Capture and deliver selected local skills

**What to build:** Retain pre-QA ticket 11's generic role/default/addition contract: explicitly resolve local sources and required references, capture origin/source/content identities, reject missing content, and record actual delivery. Repairs receive captured instructions even after source edits. Keep the planning reference aligned with this canonical metadata.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [26: Supply coherent design guidance to Standards review](#26-supply-coherent-design-guidance-to-standards-review).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R13](#r13-capture-and-deliver-selected-local-skills).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [skill selection and delivery](spec.md#skill-selection-and-delivery); [agent contracts and access](spec.md#agent-contracts-and-access).

### Acceptance criteria

- [ ] Document one canonical additive skill-selection/source-resolution contract compatible with the planning reference and tickets without additions.
- [ ] Support explicit local harness, target-repository, and installed-library sources; role-specific ticket additions preserve project defaults and mandatory role/access/output contracts.
- [ ] At run start capture selected skills and required local references with role, selection origin, source identity and content identity; reject missing required content before affected assignments.
- [ ] Deliver captured instructions explicitly and record actual delivered content; repairs use captured content despite later source edits.
- [ ] Demonstrate defaults, role-specific additions, missing references and edits after capture in a separate scripted target repository; preserve upstream files and defer discovery/download/installation.

### Verification

Scripted cross-repository assignments exercise defaults, role-specific additions, missing references, and source edits after capture without adding live-model variations.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/28-deliver-focused-implementation-and-spec-review-contexts.md -->

<a id="r14-deliver-focused-implementation-and-spec-contexts"></a>

## 28: Deliver focused implementation and Spec contexts

**What to build:** Retain pre-QA ticket 12's distinct implementation/repair/Spec guidance and fresh context assembly. Supply milestone and ticket constraints while keeping reviews, commits, promotions, state changes, and human approval under harness control. Reuse shared design and test strategy without copying the whole upstream library.

**Blocked by:** [27: Capture and deliver selected local skills](#27-capture-and-deliver-selected-local-skills).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R14](#r14-deliver-focused-implementation-and-spec-contexts).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [skill selection and delivery](spec.md#skill-selection-and-delivery).

### Acceptance criteria

- [ ] Create focused implementation/repair guidance for one ticket's contracts, approved behavioral seams, custom test-strategy coverage selection, TDD where needed, evidence, and out-of-scope decisions.
- [ ] Create separate Spec-review guidance for missing, incorrect and unrequested behavior against approved requirements.
- [ ] Provide every assignment fresh role context, captured defaults/additions and scoped references; repairs use the captured version even after source-library edits.
- [ ] Supply exact reviewed revision, relevant source/diff and actual check outcomes to Spec review, with only relevant design guidance for implementers.
- [ ] Keep nested-review orchestration, commits, integration, QA acceptance, state and completion under harness authority; record actual selection origins/content identities and demonstrate a fresh repair.

### Verification

Captured scripted implementation, repair, and Spec assignments show scoped requirements, exact reviewed revisions, stable selected guidance, and role separation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R14; the [previous definition](../../archive/issues-before-milestone-qa/12-deliver-focused-implementation-and-spec-review-contexts.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/29-run-a-real-codex-ticket-cycle.md -->

<a id="r15-complete-the-workflow-with-real-codex-roles"></a>

## 29: Complete the workflow with real Codex roles

**What to build:** Retain pre-QA ticket 13's real CLI invocation, events, reports, cross-repository skill delivery, and independent reviews. Establish Medium implementation/repair and High reviewer defaults with validated ticket worker overrides. Exercise the existing local milestone flow without treating model output as human QA approval.

**Blocked by:** [15: Continue after a deliberate QA stop](../../issues/15-continue-from-a-planned-qa-checkpoint.md); [28: Deliver focused implementation and Spec contexts](#28-deliver-focused-implementation-and-spec-contexts); [08: Stop stalled assignments and check processes](../../issues/08-stop-timed-out-process-trees.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M3. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R15](#r15-complete-the-workflow-with-real-codex-roles).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [codex execution](spec.md#codex-execution); [skill selection and delivery](spec.md#skill-selection-and-delivery).

### Acceptance criteria

- [ ] Verify installed Codex invocation and launch fresh implementation/repair/review processes with explicit working directory, sandbox, positive timeout, model, and output contract; do not silently substitute models.
- [ ] Apply Medium implementation/repair and High Spec/Standards defaults with independently configurable role profiles; validate ticket worker overrides and inherit them in repairs without changing reviewers.
- [ ] Capture machine-readable events and schema-validated reports with actual model/reasoning settings and supplied instruction identities.
- [ ] Demonstrate cross-repository delivery of required custom role/design guidance, project defaults and a role-specific addition, without assuming automatic discovery.
- [ ] Complete a tiny actual implementation plus two independent actual reviews and exact candidate integration within the established milestone workflow; keep human QA approval separate from model results.
- [ ] Retain scripted offline routine checks and a separate explicit live check. Record actual evidence or a concrete blocker; a skipped live check is not completion.

### Verification

Routine tests remain offline. A tiny explicit live fixture records actual settings, delivered content, checks/reviews and exact ticket integration; its QA decision is separately explicit and attributable. Report any live blocker as incomplete validation.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R15; the [previous definition](../../archive/issues-before-milestone-qa/13-run-a-real-codex-ticket-cycle.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/30-compare-configurable-agent-context-limits.md -->

<a id="r16-run-the-early-context-budget-comparison"></a>

## 30: Run the early context-budget comparison

**What to build:** Retain pre-QA ticket 17's 100K/150K/200K/250K controls, fixed workload and reasoning settings, genuine context-pressure case, repetitions, raw measurements, and acceptance checks. Distinguish hard enforcement, compaction thresholds, and advisory targets; active occupancy is separate from cumulative/cached usage.

**Blocked by:** [29: Complete the workflow with real Codex roles](#29-complete-the-workflow-with-real-codex-roles).

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
- [ ] Publish reproducible findings and limitations without silently changing defaults. Execute immediately after ticket 29 under independent experiment checkpoint E1; do not add release, comprehensive access, background, or completed planning-integration gates.

### Verification

Preserve the current ticket's explicit experiment evidence requirements. Prioritize immediately after ticket 29, before comprehensive boundary probes or release packaging. It remains independent of first-release acceptance dependencies.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R16; the [previous definition](../../archive/issues-before-milestone-qa/17-compare-configurable-agent-context-limits.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/31-verify-role-write-boundaries.md -->

<a id="r17-verify-runtime-write-and-approval-boundaries"></a>

## 31: Verify runtime write and approval boundaries

**What to build:** Retain pre-QA ticket 14's real sandbox probes and add QA decisions, dev, and feature refs to the protected authority checks. Implementers may edit assigned source; reviewers remain read-only; implementation/repair cannot authorize promotion. Do not silently widen permissions or treat a prompt instruction as proof of enforcement.

**Blocked by:** [21: Guide a human through milestone QA](#21-guide-a-human-through-milestone-qa); [29: Complete the workflow with real Codex roles](#29-complete-the-workflow-with-real-codex-roles).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R17](#r17-verify-runtime-write-and-approval-boundaries).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [agent contracts and access](spec.md#agent-contracts-and-access); [feature to development promotion and human qa](spec.md#feature-to-development-promotion-and-human-qa).

### Acceptance criteria

- [ ] Verify an implementer can edit only assigned source while reviewers have read-only source sufficient to produce their reports.
- [ ] Probe disposable sentinels for sibling source, approved inputs, authoritative records, QA decisions, and feature/development refs; refuse or detect out-of-scope effects before acceptance.
- [ ] Keep submission capture, both integration destinations, QA decision consumption and execution state under harness authority; implementation/repair cannot authorize acceptance.
- [ ] Reject assignments when required access/instruction guarantees cannot be established; do not silently widen permissions or substitute prompt claims for probes.
- [ ] Record actual backend/sandbox/file/ref observations while preserving caller work and approved inputs.

### Verification

Existing disposable sentinel probes plus QA/ref targets provide concrete access evidence without touching caller work. A failed access guarantee leaves verification incomplete.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R17; the [previous definition](../../archive/issues-before-milestone-qa/14-verify-role-write-boundaries.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

<!-- Proposed publication: issues/32-run-a-generated-plan-through-the-runtime.md -->

<a id="r18-run-a-generated-approved-plan-through-the-runtime"></a>

## 32: Run a generated approved plan through the runtime

**What to build:** Complete the remaining integration portion of pre-QA ticket 15. Produce a small plan through the unified skill, validate it against the now-implemented milestone/skill contracts, and execute it through the scripted public seam. Demonstrate project-default guidance and a role-specific ticket addition, preserving required contracts.

**Blocked by:** [10: Turn one grilling session into an approved plan](../../issues/10-produce-approved-harness-inputs-with-planning-skill.md); [23: Execute approved QA corrections](#23-execute-approved-qa-corrections); [27: Capture and deliver selected local skills](#27-capture-and-deliver-selected-local-skills).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R18](#r18-run-a-generated-approved-plan-through-the-runtime).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [planning and milestone contract](spec.md#planning-and-milestone-contract); [skill selection and delivery](spec.md#skill-selection-and-delivery).

### Acceptance criteria

- [ ] Generate a small human-approved spec/ticket/milestone bundle through the unified planning skill and validate it against the implemented canonical contracts.
- [ ] Demonstrate explicit project defaults and an applicable role-specific ticket addition, plus a ticket requiring no additions, preserving mandatory role guidance.
- [ ] Run the approved example through intentional scripted CLI execution, reaching planned QA and exact local promotion with captured/delivered instruction identities.
- [ ] Keep publishing distinct from execution and QA planning distinct from acceptance; preserve original inputs and evidence.
- [ ] Include interfaces, invariants, testing seams, Pythonic shared design, and appropriate test strategy without replaying all selection validation already covered by ticket 27.

### Verification

A generated example reaches QA and promotion with recorded selection/content identities. Planning publication does not itself launch execution; the example uses an explicit run.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

<!-- Proposed publication: issues/33-demonstrate-the-first-usable-release.md -->

<a id="r19-demonstrate-the-revised-first-usable-release"></a>

## 33: Demonstrate the revised first usable release

**What to build:** Expand pre-QA ticket 16's clean-checkout acceptance to planning, background operation, two QA milestones, corrections, safe checkpoint continuation, exact local promotions, blocked/waiting work, optional findings, selected guidance, and actual Codex/access evidence. Clearly document deferred concurrency, arbitrary crash recovery, hosted PRs/GitHub checks, and email.

**Blocked by:** [11: Stop development handoffs at human checkpoints](../../issues/11-stop-development-handoffs-at-qa-milestones.md); [24: Operate the orchestrator in the background](#24-operate-the-orchestrator-in-the-background); [25: Continue independent work inside the current milestone](#25-continue-independent-work-inside-the-current-milestone); [31: Verify runtime write and approval boundaries](#31-verify-runtime-write-and-approval-boundaries); [32: Run a generated approved plan through the runtime](#32-run-a-generated-approved-plan-through-the-runtime); [07: Report optional review suggestions without rework](../../issues/07-report-optional-suggestions-without-repair.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](spec.md).

**Milestone:** M4. Follow [milestone eligibility](milestones.md) before selecting work.

**Plan slice:** [R19](#r19-demonstrate-the-revised-first-usable-release).

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](README.md#agent-context-policy).

**Worker reasoning:** Medium by default; an explicit ticket override applies to implementation and repair. Spec and Standards review default to High with independent role configuration.

**Role guidance:** Inherit the development role defaults in [Role Configuration](spec.md#role-configuration); no ticket-specific additions. Preserve this ticket's existing runtime role/skill requirements.

**Context:** [testing decisions](spec.md#testing-decisions); [out of scope](spec.md#out-of-scope).

### Acceptance criteria

- [ ] Document installation, actual CLI/background/foreground/status/log/stop/continue interfaces, role settings, limits, requirements, skill selections and artifact/decision inspection.
- [ ] Provide a clean-checkout disposable example covering two milestones, planned QA waits, explicit approval, correction-plan amendment, safe continuation and exact feature-to-dev promotion.
- [ ] Retain repaired/blocked/dependent/unrelated/optional-finding examples and final feature acceptance without bypassing any QA boundary.
- [ ] Run the complete deterministic suite and required static/packaging/installed CLI checks without routine model credentials or network access.
- [ ] Retain actual small Codex/skill/access evidence or report its blocker; show immutable approved inputs and exact candidate-bound branch advancement.
- [ ] Clearly separate sequential operation and planned-QA continuation from deferred concurrency, arbitrary crash recovery, hosted PR/GitHub checks, and email. Context experiment 30 is prioritized separately, not a release gate.

### Verification

Run the existing required complete suite and packaging/installed CLI checks, follow the documented disposable-repository walkthrough, and retain actual live evidence or its explicit blocker. Ticket 30 is scheduled early but is not a prerequisite for release acceptance.

Follow the repository's testing policy; document-only skill changes use skill/link/workflow validation, while executable changes retain their required suite and checks. Preserve actual source/check/review evidence.

### Handoff

Use the [shared worker handoff](README.md#worker-handoff). Verify and record this ticket's completion without treating it as milestone acceptance. Select further work only through the [published milestone plan](milestones.md); do not start the next ticket automatically.

### Comments

#### QA realignment

Reconciled with approved slice R19; the [previous definition](../../archive/issues-before-milestone-qa/16-demonstrate-the-first-usable-release.md) is retained for history. This revision supersedes the old product-first execution order without reopening completed tickets 01–09.

## Prior decomposition and history

Existing R01–R19 preserve their responsibilities and historical lineage in the [prior approved proposal](../../ticket-proposal.md). O01–O05 identify this amendment's added ownership work. The [numbering map](numbering-map.md) governs current owner lookup; completed-ticket evidence keeps its historical IDs.

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

The [prior approved proposal](../../ticket-proposal.md#comparison-with-the-pre-qa-open-tickets) retains the pre-QA decomposition comparison. Look up current owners through the [numbering map](numbering-map.md).

## Supporting publication updates

The [exact supporting reference and handoff changes](publication-updates.md) are part of this bundle. Their sources remain unchanged pending approval.
