# 02: Reject invalid requirements before starting work

**What to build:** A run rejects incomplete or contradictory requirements, invalid dependencies, and invalid check configuration before launching workers or changing integration state.

**Blocked by:** [01: Complete one scripted ticket through every gate](01-complete-one-scripted-ticket-cycle.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** Extend the existing CLI preflight and canonical Markdown/configuration contract; preserve the configured local authoring conventions.

## Acceptance criteria

- [ ] Normalize stable ticket IDs, titles, readiness labels, dependencies, acceptance requirements, and check references into one documented contract.
- [ ] Reject duplicate IDs, missing dependency references, dependency cycles, contradictory metadata, missing acceptance requirements, and unusable check configuration with actionable diagnostics.
- [ ] Keep triage readiness distinct from dependency satisfaction: non-agent-ready work and selections with unsatisfied prerequisites cannot silently execute.
- [ ] Do not launch a worker or change integration references when preflight rejects the inputs.
- [ ] Demonstrate valid and invalid bundles through CLI outcomes in real temporary repositories.

## Verification

Use fixture bundles with one invalid condition at a time and assert diagnostics, nonzero outcomes, and unchanged Git references rather than parser internals.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
