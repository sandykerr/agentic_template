# 15: Produce executable Markdown requirements with a planning skill

**What to build:** An interactive custom planning skill converts human-approved decisions into canonical specs and small dependency-aware Markdown tickets that pass validation and run through the harness.

**Blocked by:** [09: Execute verified dependencies in a stable order](09-execute-dependencies-sequentially.md); [11: Supply combined Python design guidance to Standards review](11-supply-combined-design-guidance-to-standards-review.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Skill selection and delivery](../spec.md#skill-selection-and-delivery); [Requirements, configuration, and run records](../spec.md#requirements-configuration-and-run-records); [Public interface and approval](../spec.md#public-interface-and-approval).

**Scope:** The planning role and a small example input bundle, reusing grilling, domain modeling, the shared design policy, custom test strategy, issue 11's skill-selection contract, and the existing local tracker. Planning establishes human-approved inputs; it is not an autonomous run stage or a next-agent development handoff.

## Acceptance criteria

- [ ] Establish important module interfaces, invariants, and behavioral testing seams with the human and record their decisions durably.
- [ ] Produce independently verifiable vertical tickets with stable IDs, readiness, acceptance requirements, and only genuine prerequisite dependencies.
- [ ] Reuse the shared design-policy authority and appropriate references while supporting Pythonic functional and OO combinations.
- [ ] Reuse grilling and domain-modeling guidance to resolve decisions with the human and record durable terms/decisions where warranted; use custom test strategy to assess existing coverage, meaningful gaps, agreed seams, and required checks when shaping tickets.
- [ ] Propose relevant role-specific skill additions in tickets when useful, using the canonical metadata from issue 11. Demonstrate a ticket addition that preserves project defaults and required role contracts, and a ticket needing no additions; preserve human approval of the resulting selections.
- [ ] Match the canonical local Markdown and check-selection contracts without duplicating contradictory metadata.
- [ ] Demonstrate that a small generated example bundle passes preflight and completes a scripted sequential run.
- [ ] Leave execution to intentional CLI invocation and preserve human ownership of requirement or contract changes.

## Verification

Validate the planning skill, review its example outputs against the agreed contracts, and execute the example bundle through the public scripted-agent harness seam. Capture the generated default/addition metadata and the selected content delivered to the relevant role; reuse common selection validation from issue 11.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
