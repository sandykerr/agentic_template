# 20: Own implementation-attempt transitions

**What to build:** Give each implementation attempt responsibility for its own lifecycle observations. Submission, rejection, completion and human-decision handoff update the correct attempt and ticket consistently, while the runner continues to execute checks and validate reports. Complete the migration of existing callers within this ticket so the CLI stays usable.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md); [06: Stop for decisions outside approved contracts](06-surface-human-decisions-without-retrying.md); [19: Evaluate reviewers on known and acceptable designs](19-evaluate-reviewers-on-known-and-acceptable-designs.md).

**Status:** completed

**Plan version:** [oop-v2](../spec.md).

**Milestone:** M1. Follow [membership and QA](../milestones.md#m1-a-complete-qa-controlled-git-cycle) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Independent Spec and Standards reviewers inherit High. All roles inherit GPT-6.1 Sol and the 250,000 active-context target.

**Role guidance:** Inherit [development defaults](../spec.md#role-configuration). For implementation, repair and Standards, add [object-oriented design](../../../.agents/skills/microsoft/microsoft_oop/SKILL.md), [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md), and [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md). Spec review uses the agreed spec and testing contracts; no additional skill selection. These development additions do not select runtime instructions for target-repository agents.

**Context:** [ownership contracts](../spec.md#state-and-decision-ownership), [refactor verification](../spec.md#oop-refactor-verification), [ticket lifecycle](../spec.md#ticket-lifecycle), [independent checks](../spec.md#independent-checks-and-exact-revisions), [QA and promotion](../spec.md#feature-to-development-promotion-and-human-qa), and [safe continuation](../spec.md#corrections-and-safe-continuation). Respect [domain terms](../../../GLOSSARY.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

**Review amendment:** [development review contract](../spec.md#ownership-contracts-and-cross-module-review); [checkpoint rules](../spec.md#cumulative-architecture-checkpoints); [review records](../spec.md#review-work-findings-and-decisions).

## Acceptance criteria

- [x] Attempt-owned operations maintain the existing Running, Verifying, Rejected and Done observations, revision identities, changed-file observations, and inclusive/exclusive gate ranges. Corresponding current-ticket observations remain consistent, including failures before a submission exists.
- [x] The runner retains check execution, report validation, source-evidence invalidation and failure precedence. It communicates validated human-decision evidence to the owning attempt without selecting an attempt through the last entry in shared history or mutating its lifecycle record directly. Report parsing and validation return their findings or failure information; they do not mutate the canonical gate record. The runner records the final report/check status, preserving report content and diagnostics on rejected reports and the current precedence among process exit, timeout, report validity, blocking findings, human decisions and integrity/environment failures.
- [x] Implementation and either review axis can stop the correct initial or repair attempt for a validated human decision, including a nonzero process exit. Preserve the complete handoff on both existing record locations, preserved work, diagnostic, Blocked/incomplete outcome, and immediate stop without later gates or extra repairs.
- [x] Malformed decision-like reports, optional findings, ordinary report/process failures and timeouts retain their existing distinct validation and bounded-failure behavior; they cannot gain decision authority or produce false success.
- [x] Public commands, exit behavior, record keys/values, artifact naming, historical attempt evidence and caller/approved-input protection remain compatible. Atomic persistence still exposes meaningful intermediate observations.
- [x] Design review confirms transition rules live with attempt state and callers use those operations; private naming/layout remains an implementation choice, with no getter/setter-only wrapper or inheritance framework.

- [x] Use the evaluated review workflow from tickets 16–19: record the relevant ownership change, independent cross-module review scope, immutable reports and finding dispositions; perform a cumulative assessment when the shared risk triggers apply. Preserve a navigable rationale-to-change-to-verification history and carry unresolved findings into the next handoff.

## Verification

Map existing repair/history and human-decision cases, including initial/later attempts, implementation/either-axis decisions, decision precedence and durable status output. Prior art: `tests/test_repairs.py`, `tests/test_human_decisions.py`, `tests/test_optional_suggestions.py`, `tests/test_timeouts.py` and multi-ticket attempt-history cases in `tests/test_dependencies.py`. Preserve report validation and integrity regression coverage. Include existing `tests/test_reports.py` coverage for malformed reports, valid reports with failed processes, and preserved diagnostics.

Use the existing public CLI with scripted external processes, real temporary Git repositories, and observable Git/record outcomes. Map criteria to existing coverage first; add cases only for distinct uncovered failures. Design review verifies ownership and encapsulation without tests that require particular private classes or method names. Follow [refactor verification](../spec.md#oop-refactor-verification) for the full suite, static checks, evidence and independent reviews on the final source.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Preserve completed tickets 01–15 and their evidence. Ticket completion does not accept M1; after all M1 work is verified, prepare QA or a waiting handoff. Do not start M2 before explicit human acceptance of M1.

## Comments

### Verified completion — 2026-11-10

Previous readiness: `ready-for-agent`. All seven acceptance criteria are verified
at implementation `0aa2660505e4233ca2e321cee439ba51b150e055`, from fixed baseline
`0d79d016907a03ce39d33c749523a8700e4233a4`. Criterion wording and `Blocked by:`
dependency history are unchanged.

[Criterion-by-criterion completion evidence](../evidence/20-completion.md) links
actual ownership/coverage and CLI/Git/record evidence. Final checks: **544 passed
in 703.66s**, strict mypy, Ruff lint/format and working/staged/committed whitespace
all exit 0. No tests added; packaging is outside impact scope. The genuine
baseline-source checkpoint continuation passed; its original capture loss and
renewed producer timing limit remain explicit in the evidence and both reviews.

Independent whole-ticket [Spec spec-01](../evidence/20-review-spec-01.md): **0
blocking/0 optional**; independent [Standards standards-01](../evidence/20-review-standards-01.md):
**0 blocking/0 optional**. [Assessment and immutable report identities](../reviews/ticket-20.md)
and [finding/authority history](../evidence/20-finding-history.md) preserve originals.
No unresolved full finding key, unchecked criterion, missing required ticket
report, pending relevant revalidation or actual human decision remains. All four
start/final architecture triggers are No. Requested role settings are recorded;
backend enforcement/delivery and measured context telemetry remain unavailable.

Implementation was committed before review; this bookkeeping is committed
separately. The next handoff is a third separate commit selecting eligible work
without launching it. M1 still needs 21–24, actual feature-start provenance and
all-package cumulative assessment, then explicit human QA. No M1 readiness,
acceptance, promotion, later-milestone authorization or push is inferred.
