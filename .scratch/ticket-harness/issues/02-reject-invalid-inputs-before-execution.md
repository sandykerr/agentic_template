# 02: Reject invalid requirements before starting work

**What to build:** A run rejects incomplete or contradictory requirements, invalid dependencies, and invalid check configuration before launching workers or changing integration state.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** Extend the existing CLI preflight and canonical Markdown/configuration contract; preserve the configured local authoring conventions.

## Acceptance criteria

- [x] Normalize stable ticket IDs, titles, readiness labels, dependencies, acceptance requirements, and check references into one documented contract.
- [x] Reject duplicate IDs, missing dependency references, dependency cycles, contradictory metadata, missing acceptance requirements, and unusable check configuration with actionable diagnostics.
- [x] Keep triage readiness distinct from dependency satisfaction: non-agent-ready work and selections with unsatisfied prerequisites cannot silently execute.
- [x] Do not launch a worker or change integration references when preflight rejects the inputs.
- [x] Demonstrate valid and invalid bundles through CLI outcomes in real temporary repositories.

## Verification

Use fixture bundles with one invalid condition at a time and assert diagnostics, nonzero outcomes, and unchanged Git references rather than parser internals.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).

## Comments

### Completion — 2026-11-06

Implemented ticket 02 in checkpoint `855a4c8`, with executable-validation review fixes `dfdb1a6` and final implementation `b11fd20`. The fixed baseline was captured before editing as `0efc06333ca0996fa8953d69c3ae682a86e47ce7`; the checkpoint was committed before independent review, and every later review retained that original baseline.

All five acceptance criteria are verified at `b11fd20` in the [criterion-specific completion evidence](../evidence/02-completion.md). The [saved actual CLI/Git observations](../evidence/02-fixture-observations.json) record 19 final-revision scenarios. The valid normalized bundle passed every gate; all 18 invalid bundles exited 1 during input validation with attempt 0, no agent launch, no gates, and unchanged refs/worktrees. The suite additionally verifies genuine integrated prerequisite Done evidence, rejection of incomplete/stale/unintegrated evidence, non-agent-ready selections, and execution of only the selected ticket. The [canonical contract](../../../docs/ticket-harness.md#canonical-input-contract) documents IDs, titles, readiness, dependencies, acceptance text, checks, configuration, and authoring compatibility.

Checks: complete suite **73 passed** (the original eight ticket-01 tests plus 65 preflight cases); strict mypy, Ruff lint/format, and whitespace checks exited 0. Final wheel build/install, installed CLI smoke check, and the standalone observation run all passed using the documented micromamba environments. Focused CLI tests and typechecking ran throughout red/green implementation and review repairs.

Separate fresh independent reviews of the entire committed implementation: **Standards: no findings. Spec: no findings**, with the final Spec reviewer independently rerunning all 73 tests. Two earlier blocking Spec findings about executable resolution were fixed, committed, and independently re-reviewed; no optional suggestions or unresolved findings remain. Full review history and outcomes are in the evidence.

No active harness run using these approved inputs was found; this completion bookkeeping follows verification outside a run. Criterion wording, dependency declaration, and `ready-for-agent` triage label are preserved. Only ticket 02 is completed here; dependency scheduling, automatic prerequisite execution, comprehensive reports, transaction hardening, repairs, and live Codex remain deferred. No unchecked criteria or unresolved questions remain. No push was performed.
