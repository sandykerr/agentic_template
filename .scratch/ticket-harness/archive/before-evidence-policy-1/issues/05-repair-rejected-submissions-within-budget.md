# 05: Repair rejected submissions within a bounded allowance

**What to build:** A concrete check or review failure requests a fresh repair and repeats verification, ending in verified integration or a preserved Blocked ticket.

**Blocked by:** [03: Reject invalid agent reports and review evidence](03-validate-agent-reports-and-review-evidence.md); [04: Promote only the exact verified candidate](04-promote-only-the-verified-candidate.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions); [Ticket lifecycle](../spec.md#ticket-lifecycle).

**Scope:** One ticket's automatic repair loop, with an initial submission and two repair attempts by default; use the existing process, report, and integration contracts.

## Acceptance criteria

- [x] Make the repair allowance configurable with a default of two after the initial submission; worker-internal edit/test iterations do not each count as repairs.
- [x] Start each repair in fresh context with current changes, rejected revision identities, and concrete check or review evidence.
- [x] Support repair after lightweight-check failures, either review axis, and candidate-integration failures.
- [x] Capture a new repaired revision and rerun the applicable lightweight checks, both fresh reviews, and candidate suite before integration.
- [x] Exhausted repairs preserve the changes and complete attempt history, set the ticket Blocked, and return an incomplete result.
- [x] Demonstrate both a successful repair and an exhausted allowance without an unlimited secondary retry path.

## Verification

Script specific failures and repairs through the public CLI; assert attempts, supplied evidence, renewed revision-bound gates, final Git state, and outcome.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

All six acceptance criteria are verified at implementation checkpoint `34a49b7`, reviewed against the fixed starting baseline `d6abfd62f86165c5a3e63c61b3c0ff86d2af452f`. Previous readiness label: `ready-for-agent`; `Blocked by:` remains prerequisite history. No fixes were needed after the separate independent reviews.

The [criterion-specific completion evidence](../evidence/ticket-05/05-completion.md) and [20 actual CLI/Git observations (compact historical results)](../evidence/ticket-05/05-scenario-results.json) verify the configurable default of two repairs, fresh process/worktree/attempt identity with current changes and concrete rejection evidence, repairs after lightweight checks/either review axis/merge/candidate-suite failures, new captured submissions and all renewed revision-bound gates, complete preserved history and Blocked/incomplete exhaustion, and one bounded policy for invalid reports and process failures. Default final-allowance success and exhaustion both occur on attempt 3. Worker editing/testing remains one attempt. Valid human-decision reports stop without capture/review/repair, including nonzero exits; preflight/baseline failures start no attempts. Caller work, rejected revisions, approved inputs, evidence protection, candidate identities and external branch changes remain preserved.

Final checkpoint checks: **362 tests passed in 408.88s**, including 58 repair cases and all 304 prerequisite cases. Strict mypy, Ruff lint/format, whitespace, wheel/install and installed CLI checks passed. All 20 standalone scenarios passed and status matched durable records. Python used the documented reusable environment. Focused red/green tests and typechecking ran during implementation.

Independent **Spec: no findings. Standards: no findings.** The Spec reviewer additionally reproduced unchanged-content repair through the public CLI and verified a fresh revision and every renewed gate. Both reviews assessed the complete committed diff with fresh contexts under the 250K target; full reports and sources are in the evidence. No optional suggestions, unchecked criteria, or unresolved ticket-05 decisions remain.

No active harness run using these approved feature inputs was found. Bookkeeping follows implementation/review and is committed separately. The pre-existing skill relocation remains unstaged; no push was performed. Broader human-decision handling, suggestion reporting, timeouts, scheduling, live agents/role skills, OS role enforcement, concurrency and recovery remain with later tickets.
