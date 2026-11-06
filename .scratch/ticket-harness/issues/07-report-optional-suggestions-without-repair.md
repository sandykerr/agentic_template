# 07: Report optional review suggestions without rework

**What to build:** A ticket with passing gates and optional review suggestions integrates normally, while the suggestions remain available in the final report.

**Blocked by:** [05: Repair rejected submissions within a bounded allowance](05-repair-rejected-submissions-within-budget.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Agent contracts and access](../spec.md#agent-contracts-and-access); [Ticket lifecycle](../spec.md#ticket-lifecycle).

**Scope:** The optional-finding path across report validation, repair decisions, and status/final output.

## Acceptance criteria

- [x] Treat valid optional findings from either review axis as non-blocking while retaining their evidence and source-revision identity.
- [x] Do not launch a repair or consume its allowance solely for optional suggestions.
- [x] Integrate a passing ticket with optional suggestions and expose those suggestions in the recorded and human-readable result.
- [x] When blockers and suggestions coexist, send blockers into repair and retain suggestions without converting preferences into requirements.
- [x] Preserve which findings belong to which reviewed revision when later repairs occur.

## Verification

Drive optional-only and mixed-finding fixtures through the CLI; inspect agent launches, attempt counts, integration success, and report contents.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

Verified at checkpoint `83d361d06b9f127a365b437b51ca9cc2a0f58896` against captured review baseline `44c7267553a411e8285f9ac7e7e1bf76f5d72601`. Previous readiness label: `ready-for-agent`; `Blocked by:` remains declared prerequisite history. Runtime behavior already met this ticket; the checkpoint adds 22 behavioral cases and documents the existing assignment/report/run/status contracts without introducing a new runtime layer.

The [criterion-specific completion evidence](../evidence/07-completion.md) and [23 saved CLI/Git observations](../evidence/07-fixture-observations.json) verify both axes separately/together, optional decision flags, one-attempt integration with two repairs available, complete evidence and exact reviewed revisions, mixed-finding successful/exhausted repairs, cross-axis rejection, suggestions appearing/disappearing and IDs reused across fresh revision reports, invalid optional evidence/stale reports/nonzero exits, and immediate human-decision compatibility. Run/status retain the complete suggestions in indented JSON; exact candidate integration, approved inputs, caller work and earlier artifacts remain preserved.

Checks: **421 tests passed in 315.49s**, including all 22 new and 399 prerequisite cases. Pre-change repair/decision checks passed all 95 cases; focused slices and strict mypy passed during development. Final strict mypy, Ruff lint/format, whitespace, packaging/installed CLI and all 23 saved scenarios passed. The installed-only run/status case integrates both axes' optional findings on attempt 1.

Independent **Spec: 0 blockers, 0 optional suggestions; Standards: 0 blockers, 1 optional suggestion**. Spec independently passed 12 CLI/Git cases. Standards suggested sharing the repeated default-repair test fixture; this maintenance preference is recorded separately in the evidence and remains optional. Both fresh reviewers assessed the full committed diff and existing runtime; fixture reviewers did not replace implementation review. No fixes, unchecked criteria or required unresolved ticket-07 items remain.

No active harness run using these feature inputs was found. Bookkeeping follows verified checks/reviews and is committed separately. The pre-existing skill relocation remains unstaged; no push was performed. Timeouts, dependency scheduling/continuation, role/design-skill delivery, live Codex, OS access enforcement, concurrency and recovery remain outside this slice.
