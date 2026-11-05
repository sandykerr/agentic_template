# 05: Repair rejected submissions within a bounded allowance

**What to build:** A concrete check or review failure requests a fresh repair and repeats verification, ending in verified integration or a preserved Blocked ticket.

**Blocked by:** [03: Reject invalid agent reports and review evidence](03-validate-agent-reports-and-review-evidence.md); [04: Promote only the exact verified candidate](04-promote-only-the-verified-candidate.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Bounded failures and timeouts](../spec.md#bounded-failures-and-timeouts); [Independent checks and exact revisions](../spec.md#independent-checks-and-exact-revisions); [Ticket lifecycle](../spec.md#ticket-lifecycle).

**Scope:** One ticket's automatic repair loop, with an initial submission and two repair attempts by default; use the existing process, report, and integration contracts.

## Acceptance criteria

- [ ] Make the repair allowance configurable with a default of two after the initial submission; worker-internal edit/test iterations do not each count as repairs.
- [ ] Start each repair in fresh context with current changes, rejected revision identities, and concrete check or review evidence.
- [ ] Support repair after lightweight-check failures, either review axis, and candidate-integration failures.
- [ ] Capture a new repaired revision and rerun the applicable lightweight checks, both fresh reviews, and candidate suite before integration.
- [ ] Exhausted repairs preserve the changes and complete attempt history, set the ticket Blocked, and return an incomplete result.
- [ ] Demonstrate both a successful repair and an exhausted allowance without an unlimited secondary retry path.

## Verification

Script specific failures and repairs through the public CLI; assert attempts, supplied evidence, renewed revision-bound gates, final Git state, and outcome.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
