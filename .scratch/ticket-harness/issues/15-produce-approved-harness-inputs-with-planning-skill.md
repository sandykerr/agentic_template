# 15: Produce executable Markdown requirements with a planning skill

**What to build:** An interactive custom planning skill converts human-approved decisions into canonical specs and small dependency-aware Markdown tickets that pass validation and run through the harness.

**Blocked by:** [09: Execute verified dependencies in a stable order](09-execute-dependencies-sequentially.md); [11: Supply combined Python design guidance to Standards review](11-supply-combined-design-guidance-to-standards-review.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** The planning role and a small example input bundle, using the shared design policy and existing local tracker; no autonomous approval of human decisions.

## Acceptance criteria

- [ ] Establish important module interfaces, invariants, and behavioral testing seams with the human and record their decisions durably.
- [ ] Produce independently verifiable vertical tickets with stable IDs, readiness, acceptance requirements, and only genuine prerequisite dependencies.
- [ ] Reuse the shared design-policy authority and appropriate references while supporting Pythonic functional and OO combinations.
- [ ] Match the canonical local Markdown and check-selection contracts without duplicating contradictory metadata.
- [ ] Demonstrate that a small generated example bundle passes preflight and completes a scripted sequential run.
- [ ] Leave execution to intentional CLI invocation and preserve human ownership of requirement or contract changes.

## Verification

Validate the planning skill, review its example outputs against the agreed contracts, and execute the example bundle through the public scripted-agent harness seam.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
