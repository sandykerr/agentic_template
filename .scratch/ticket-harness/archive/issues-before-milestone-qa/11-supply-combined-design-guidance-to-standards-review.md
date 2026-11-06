# Historical ticket definition

Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 11; use the [current ticket](../../issues/21-supply-combined-design-guidance-to-standards-review.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/11-supply-combined-design-guidance-to-standards-review.md`. Relative links were adjusted for this archive location.

# 11: Supply combined Python design guidance to Standards review

**What to build:** Standards review receives a repo-owned skill and coherent Python design policy that reuse applicable custom, Matt Pocock, and Microsoft guidance. A shared skill-selection contract captures project defaults and ticket additions for delivery across repositories.

**Blocked by:** [03: Reject invalid agent reports and review evidence](../../issues/03-validate-agent-reports-and-review-evidence.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec-before-milestone-qa.md#custom-skills-and-design-policy); [Skill selection and delivery](../spec-before-milestone-qa.md#skill-selection-and-delivery); [Cohesive module responsibilities](../spec-before-milestone-qa.md#cohesive-module-responsibilities); [Agent contracts and access](../spec-before-milestone-qa.md#agent-contracts-and-access).

**Scope:** Establish common selection, validation, capture, and delivery of local skill content; create the shared code-design guidance and Standards-review role through the existing assignment seam. Document canonical project-default and ticket-addition metadata and source resolution. Use skill-creation and writing-for-agents guidance when authoring skills. Issue 12 applies this foundation to implementation and Spec review; automatic discovery and installation remain outside scope.

## Acceptance criteria

- [ ] Audit existing custom guidance and create one authoritative combined policy with focused references for deep modules, information hiding, responsibility/invariant ownership, composition, substitutability, justified dependency injection, and behavioral testing; record which existing guidance is reused and where role adaptation is needed.
- [ ] Explicitly support Pythonic functions, objects, and combinations; avoid mandating patterns, class hierarchies, or speculative extension points.
- [ ] Define a Standards-review skill that explains blocker evidence and consequences, keeps optional suggestions non-blocking, respects target-project standards and accepted architecture decisions, and incorporates the custom test-strategy review guidance without adding a reviewer or gate.
- [ ] Support explicit local skill sources from the harness library, target repository, and already installed libraries. Project defaults apply by role; optional ticket additions supplement them while required role contracts remain present. Preserve compatibility for tickets without additions.
- [ ] At run start, capture selected skill content and required references with their role, selection origin, source identity, and content identity; report unavailable required content before affected work starts. Later source edits leave the captured instructions unchanged.
- [ ] Deliver captured policy, selected skills, and applicable target-project references explicitly to a Standards assignment and record the content actually delivered instead of assuming cross-repository skill discovery.
- [ ] Retain the installed upstream libraries as references rather than editing or duplicating competing authorities.
- [ ] Demonstrate through captured scripted-agent inputs and review outputs in a different target repository that defaults and a ticket addition reach the appropriate role, required contracts remain present, missing skills/references are rejected, and edits to source skills/references after capture do not alter delivered content.

## Verification

Validate the skills using their supported authoring checks, inspect concrete good/bad design examples, and exercise the public assignment path with captured scripted inputs and correctly identified review results. Map the selection/capture scenarios to existing CLI/Git/report coverage and extend it for missing behavior; retain relevant prompts and artifacts from those executions.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../../README.md#worker-handoff).
