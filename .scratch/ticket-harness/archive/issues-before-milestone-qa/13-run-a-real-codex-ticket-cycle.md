# Historical ticket definition

Superseded by the approved QA-first plan. This is the previous unimplemented definition of ticket 13; use the [current ticket](../../issues/24-run-a-real-codex-ticket-cycle.md) for work. Source: `84982495be5d4943301e165f8419421391e75d18:.scratch/ticket-harness/issues/13-run-a-real-codex-ticket-cycle.md`. Relative links were adjusted for this archive location.

# 13: Complete one real Codex ticket with configured role profiles

**What to build:** A small ticket completes the existing verified cycle with actual fresh Codex implementation and review processes in a separate disposable target repository.

**Blocked by:** [08: Stop stalled assignments and check processes](../../issues/08-stop-timed-out-process-trees.md); [12: Deliver focused implementation and Spec-review skills](12-deliver-focused-implementation-and-spec-review-contexts.md)

**Status:** ready-for-agent

**Phase:** First usable release.

**Agent context limit:** 250,000 tokens of active context. Use the [agent context policy](../../README.md#agent-context-policy).

**Context:** [Codex execution](../spec-before-milestone-qa.md#codex-execution); [Skill selection and delivery](../spec-before-milestone-qa.md#skill-selection-and-delivery); [Agent contracts and access](../spec-before-milestone-qa.md#agent-contracts-and-access); [Public interface and approval](../spec-before-milestone-qa.md#public-interface-and-approval).

**Scope:** Replace the scripted process at the existing external seam with the installed Codex CLI; preserve all current gate and role contracts.

## Acceptance criteria

- [ ] Verify the installed CLI invocation and launch fresh assignments without resuming or inheriting the parent development conversation.
- [ ] Apply explicit working directory, role-specific model/reasoning settings, sandbox, timeout, and output contract without silently substituting a different configured model.
- [ ] Capture machine-readable events and schema-validated final results as run artifacts.
- [ ] Explicitly deliver captured custom implementation, Spec-review, Standards-review, and applicable design instructions across the repository boundary, including a project-default custom skill and a ticket-specific addition for its selected role; record source/content identities and actual delivered instructions.
- [ ] Demonstrate a small actual Codex implementation followed by separate actual reviews and successful exact-candidate integration.
- [ ] Keep routine tests scripted and offline; make the authenticated real-Codex check explicit and record actual evidence or a concrete environment blocker rather than counting a skipped check as success.

## Verification

Run existing deterministic checks and the separate tiny real-Codex fixture. Report the CLI version/settings, approved role selections and actual supplied content identities, check outcomes, reviewed/candidate revisions, and observed final integration. Use the small live cycle to demonstrate availability and an observable response to task-relevant selected guidance; retain captured instructions and reports. Keep exhaustive missing-reference, source-edit, and repair variations in deterministic coverage from issues 11–12 rather than multiplying live runs.

## Handoff

Return the implemented behavior, changed commits/files, checks and results, and unresolved questions in a compact report. Follow the [shared worker handoff](../../README.md#worker-handoff).
