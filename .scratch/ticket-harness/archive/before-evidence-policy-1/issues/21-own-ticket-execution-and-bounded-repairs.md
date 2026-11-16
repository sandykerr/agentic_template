# 21: Own ticket execution and bounded repairs

**What to build:** Give one ticket execution ownership of its complete implementation, verification and bounded repair cycle. Keep the original approved base, current attempt, repair starting revision, previous source worktree and failure context together. Use the attempt lifecycle delivered by ticket 20; finish the caller migration so existing selected-ticket runs stay green.

**Blocked by:** [20: Own implementation-attempt transitions](20-own-implementation-attempt-transitions.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [x] A ticket execution owns the complete cycle and repair policy through a small interface. The runner coordinates eligible tickets and retains checking; ticket workflow code no longer obtains unrestricted access to the runner merely to manipulate its shared state.
- [x] The original ticket base remains fixed across attempts, while a repair starts from the observed rejected submission or preserved uncommitted work as applicable. Fresh assignments and worktrees receive the correct failure, rejected revisions, ticket-scoped evidence and configured check selection.
- [x] Initial assignment plus configured repairs remains bounded. Repairable gate/Git/process/timeout failures, exhausted allowance, human decisions, environment/integrity failures and external ref/HEAD movement retain their existing repair-or-stop decisions and preserved history.
- [x] Every changed submission receives renewed applicable checks, both independent reviews and an exact candidate suite. Earlier approval cannot authorize a repaired source; approved inputs, earlier evidence and the caller worktree stay protected.
- [x] Only successful expected-old advancement of the integration branch records the exact tested candidate as Done and unlocks dependents. Later tickets use the current verified integration revision; existing fail-fast behavior after a blocked ticket remains unchanged until the separate blocked-work-isolation ticket.
- [x] CLI behavior, single-/multi-ticket artifact names, baseline reuse, attempt numbering, gate ranges and saved record formats remain compatible. Existing readiness calculations and Git primitives remain functions where they provide no independent state lifetime.

- [x] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing successful repair, invalid-report preservation, repair exhaustion, later-ticket fixed-base/history, evidence invalidation and external-integration scenarios. Prior art: `tests/test_repairs.py`, `tests/test_dependencies.py`, `tests/test_transaction.py` and `tests/test_timeouts.py`. This ticket does not implement later independent-work scheduling or add private-class tests.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

## Comments

Implemented and verified at `10b7050ec1fc06767e473b90217fa0d0bd100a0f` from fixed
baseline `8574c6e5fb0a55ea3539e52c7c53044f1c036583`. Previous readiness: `ready-for-agent`.
All seven unchanged criteria are verified in [completion evidence](../evidence/ticket-21/21-completion.md)
and [criterion observations](../evidence/ticket-21/21-criterion-evidence.md). Required final
checks: **544 passed in 775.37s**, strict mypy, Ruff lint/format and whitespace all
passed; all 26 tested identities match committed Git blobs. Genuine pre-edit
checkpoint continued under final source with earlier history and one baseline
preserved; original live fixture archives retained. No tests changed.

Separate fresh High [Spec](../evidence/ticket-21/21-review-spec-01.md) and
[Standards](../evidence/ticket-21/21-review-standards-01.md) each found **0 blocking / 0 optional**.
[Assessment](../reviews/ticket-21.md), [immutable originals/capture](../evidence/ticket-21/21-review-round1-capture.json)
and [finding history](../evidence/ticket-21/21-finding-history.md) preserve scope, identities,
independent reasoning and all four negative start/final triggers. No unchecked
criterion, unresolved actual key, missing required ticket report, pending relevant
revalidation or human-owned decision remains.

Bookkeeping is committed separately from implementation; the generated handoff
will be committed separately after eligibility verification. Next eligible work
is 22, backed by completed 02/12/19. M1 still requires 22–24, actual cumulative
provenance/all-package assessment and explicit human QA; no acceptance, promotion,
runtime orchestration or push is implied. Blocked by remains declared history.

M1 QA preparation, 2026-11-12: this ticket contributes to [cumulative assessment review-M1-architecture-01](../reviews/M1-architecture-01.md) at `d02e61e`, fixed feature-start baseline `1a623ba`. [Current QA preparation and observations](../evidence/m1-qa-01/qa-guide.md). Ticket completion retains its original verification; this cross-ticket assessment and actual human QA are separate gates.
