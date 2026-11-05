# 11: Supply combined Python design guidance to Standards review

**What to build:** Standards review receives a repo-owned skill and one coherent Python design policy synthesized from Matt's and Microsoft's guidance, alongside applicable target-project rules.

**Blocked by:** [03: Reject invalid agent reports and review evidence](03-validate-agent-reports-and-review-evidence.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../README.md#agent-context-policy).

**Context:** [Custom skills and design policy](../spec.md#custom-skills-and-design-policy); [Cohesive module responsibilities](../spec.md#cohesive-module-responsibilities); [Agent contracts and access](../spec.md#agent-contracts-and-access).

**Scope:** Create the shared code-design guidance and Standards-review role and deliver them through the existing assignment seam. Use the skill-creation and writing-for-agents guidance when authoring these skills.

## Acceptance criteria

- [ ] Create one authoritative combined policy with focused references for deep modules, information hiding, responsibility/invariant ownership, composition, substitutability, justified dependency injection, and behavioral testing.
- [ ] Explicitly support Pythonic functions, objects, and combinations; avoid mandating patterns, class hierarchies, or speculative extension points.
- [ ] Define a Standards-review skill that explains blocker evidence and consequences, keeps optional suggestions non-blocking, and respects target-project standards and accepted architecture decisions.
- [ ] Deliver the policy and applicable target-project references explicitly to a Standards assignment and record their identities instead of assuming cross-repository skill discovery.
- [ ] Retain the installed upstream libraries as references rather than editing or duplicating competing authorities.
- [ ] Demonstrate through captured scripted-agent inputs and review outputs that the correct policy and project context reach the assignment in a different target repository.

## Verification

Validate the skills using their supported authoring checks, inspect concrete good/bad design examples, and exercise the public assignment path with captured scripted inputs and correctly identified review results.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../README.md#worker-handoff).
