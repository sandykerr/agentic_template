# 23: Own the complete run lifecycle

**What to build:** Give the run ownership of its complete start/continue lifecycle: consume prepared inputs, establish branch and baseline identities, coordinate eligible ticket executions and milestones, classify failures, and finalize durable outcomes. Also make the run own export and restoration of verification references. Migrate existing callers and preserve the CLI throughout; the milestone workflow may remain behind its existing callable until ticket 24.

**Blocked by:** [15: Continue after a deliberate QA stop](15-continue-from-a-planned-qa-checkpoint.md); [21: Own ticket execution and bounded repairs](21-own-ticket-execution-and-bounded-repairs.md); [22: Return clearly prepared inputs](22-return-clearly-prepared-inputs.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [ ] The run owns initialization and deliberate continuation through cohesive operations; an external orchestration function no longer patches configuration, source protection, milestone index and lifecycle records in a required sequence. Public run/continue functions retain output creation, exclusive ownership and existing rejection behavior as appropriate, then invoke the run lifecycle through a small interface.
- [ ] Fresh execution retains branch validation, the required matching base/integration commit, approved-input protection, exactly one baseline and no worker launches/repairs after a failed baseline. Baseline, invalid-input, environment/integrity and later workflow failures preserve their existing stage diagnostics, outcomes, blocked/pending observations and exit codes.
- [ ] The run coordinates the ticket-execution interface from ticket 21 using the prepared inputs from ticket 22. It owns current milestone progression and finalization while ticket and attempt operations own their lifecycle records; it retains current fail-fast scheduling and never starts later-milestone work before exact human acceptance.
- [ ] Continuation consumes a deliberate validated checkpoint without replaying completed tickets, baseline work, artifacts or decisions. It invalidates the stopped marker before resumed work and preserves milestone position, history, feature/development identities, stop exit 2, success exit 0 and existing failed/rejected-continuation behavior.
- [ ] The run provides the existing checkpoint-shaped export and reconstruction of verified-check information. QA no longer inspects the runner's internal tuple/list organization. Restoration resolves references to the canonical gates in the durable run record; later source invalidation changes those actual records, including after repeated stop/continue cycles.
- [ ] Commands, saved JSON schemas/values, checkpoint version and filenames, single-/multi-ticket and milestone artifact naming, process ownership, integrity safeguards and atomic persistence remain compatible. Leave Git/process/filesystem primitives as functions and avoid a separate checker object or generic lifecycle framework.

- [ ] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing fresh-run, failed shared baseline, invalid-input, sequential multi-ticket and run/status cases in `tests/test_cli.py`, `tests/test_preflight.py`, `tests/test_dependencies.py` and `tests/test_milestones.py`; map deliberate/new-process/repeated continuation, active-owner rejection and post-restore canonical-gate invalidation in `tests/test_continuation.py` and `tests/test_qa_promotion.py`. Keep the existing QA callable working during this slice. Continue a genuine pre-refactor checkpoint and retain producer/source provenance, rather than generating compatibility evidence solely with the refactored implementation.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.
