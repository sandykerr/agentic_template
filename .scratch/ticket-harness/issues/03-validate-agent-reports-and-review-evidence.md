# 03: Reject invalid agent reports and review evidence

**What to build:** An assignment can satisfy a verification gate only with a complete, correctly identified report for the current ticket, attempt, role, and source revision.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** completed

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Agent contracts and access](../spec.md#agent-contracts-and-access); [Custom skills and design policy](../spec.md#custom-skills-and-design-policy).

**Scope:** Strengthen the existing assignment/report seam for implementation and both review axes; report validation alone does not introduce automatic repair.

## Acceptance criteria

- [x] Validate implementation results, including submitted versus human-decision-needed outcomes, against the documented assignment identity and required evidence fields.
- [x] Validate each review's axis, ticket, attempt, base/revision identity, and findings; require blocker consequence/evidence and optional-versus-blocking classification.
- [x] Accept an empty findings list only in a complete review for the correct assignment and revision.
- [x] Reject missing, malformed, incomplete, stale, or mismatched reports even when the process exits zero; reject nonzero process exits even when a report claims success.
- [x] Derive authoritative source changes and revisions from Git rather than report claims, and never accept an agent's declaration that a ticket is Done.
- [x] Keep invalid outcomes and their available artifacts visible through run/status without advancing integration.

## Verification

Exercise the CLI with scripted processes that return valid, malformed, missing, nonzero-exit, and wrong-revision outcomes; assert gate behavior and durable diagnostics.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

Completed ticket 03 in implementation checkpoint `5b04187` and review fixes `2a27565` and final implementation `07094fa`. The fixed review baseline was `9a61ec62389e7cb1dcbf440adfbdbf2c30009e72`; the checkpoint preceded independent review, and every subsequent round retained that baseline. Previous readiness label: `ready-for-agent`. The dependency declaration remains prerequisite history.

All six criteria are verified in the [criterion-specific completion evidence](../evidence/03-completion.md) and [18 saved actual CLI/Git observations](../evidence/03-fixture-observations.json). Implementation reports require complete typed identity/evidence and distinguish submitted from human-decision-needed. Both review axes require exact assignment/revision identity and complete typed findings, including stable IDs, classification, consequence, evidence, and human-decision flags; empty findings pass only with complete current identity. Missing/malformed/incomplete/stale/mismatched/mistyped reports, nonzero exits claiming success, duplicate/nonfinite/overflow JSON, and excessive nesting reject durably. Git and independent checks override agent claims, and agents cannot declare Done. All 15 non-success saved scenarios preserve available reports/logs/diagnostics, match status, preserve caller work, and leave integration unchanged. Valid human-decision reports stop before submission/review/repair.

Checks at `07094fa`: full suite **256 passed** (183 report cases plus 73 original CLI/preflight cases); strict mypy, Ruff lint/format, and whitespace checks exited 0. Final wheel build/install, installed CLI entry-point smoke check, and standalone 18-scenario observations passed through the documented reusable Python/check environments. Focused red/green tests and typechecking ran during implementation and review fixes.

Independent outcomes: **Standards: no findings. Spec: no remaining findings.** Numeric-overflow and deep-nesting durability findings were fixed, committed, and independently re-reviewed against the original baseline. The final Spec reviewer separately reran all 21 JSON/nesting regression cases successfully. Full separate review reports and sources are in the evidence. No optional suggestions, unchecked criteria, or unresolved decisions remain.

No active harness run using these approved feature inputs was found. Ticket 01's cycle and ticket 02's input validation remain passing. Only ticket 03 is completed here; transaction hardening, automatic repairs, broader human-decision handling, scheduling, timeouts, live Codex, and role-skill delivery remain assigned to later tickets. Pre-existing skill relocation edits were preserved. No push was performed.
