# 33: Enforce traceable runtime review checkpoints

**What to build:** Carry the evaluated review contract into the runtime as traceable per-ticket and cumulative assessment records. Enforce scoped review completion, findings and architecture checkpoints before affected integration and milestone QA readiness, using scripted processes first so the real-agent ticket consumes an already verified lifecycle.

**Blocked by:** [19: Evaluate reviewers on known and acceptable designs](19-evaluate-reviewers-on-known-and-acceptable-designs.md); [24: Own milestone review and checkpoint continuation](24-own-milestone-review-and-checkpoint-continuation.md); [30: Supply coherent design guidance to Standards review](30-supply-combined-design-guidance-to-standards-review.md); [31: Capture and deliver selected local skills](31-capture-and-deliver-selected-local-skills.md); [32: Deliver focused implementation and Spec contexts](32-deliver-focused-implementation-and-spec-review-contexts.md).

**Status:** ready-for-agent

**Plan version:** [oop-v2](../spec.md), approved review-process-1 revision.

**Milestone:** M3. Follow [membership and human QA](../milestones.md) before selecting work.

**Worker reasoning:** Inherit Medium for implementation and repair; no override. Spec and Standards reviewers independently inherit High. Use GPT-6.1 Sol, fresh assignments and the 250,000 active-context target.

**Role guidance:** Inherit [project role defaults](../spec.md#role-configuration), [test strategy](../../../.agents/skills/custom/test-strategy/SKILL.md) and [codebase design](../../../.agents/skills/matt-pocock/codebase-design/SKILL.md) for implementation/repair and Standards. Skill authors additionally follow [writing for agents](../../../.agents/skills/matt-pocock/writing-for-agents/SKILL.md) and [skill creation](/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md) where applicable. Preserve upstream skills unchanged; repo-owned wrappers/references carry project-specific policy.

**Context:** [review contract](../spec.md#review-work-findings-and-decisions); [ownership and review scope](../spec.md#ownership-contracts-and-cross-module-review); [architecture checkpoints](../spec.md#cumulative-architecture-checkpoints); [reviewer evaluation](../spec.md#reviewer-evaluation); [verification](../spec.md#review-process-verification); [role defaults](../spec.md#role-configuration); [runtime adoption](../spec.md#runtime-review-adoption); [exact revisions](../spec.md#independent-checks-and-exact-revisions); [QA](../spec.md#feature-to-development-promotion-and-human-qa). Respect [domain terms](../../../GLOSSARY.md), [ADR-0001](../../../docs/adr/0001-reusable-harness-and-local-integration.md) and [ADR-0002](../../../docs/adr/0002-human-qa-gates-feature-promotion.md).

## Acceptance criteria

- [ ] Runtime ticket reviews retain separate fresh Spec/Standards reports and exact revision identities, supplied ownership contracts, prior findings/dispositions and actual inspected/omitted scope. Record review/report identities, instruction/settings identities, finding keys and repair/verification links in additive harness-owned artifacts, with observational status/navigation exposing pending reviews and decisions.
- [ ] Implement the shared milestone-boundary and risk-trigger architecture assessments through an explicitly identified cumulative scope using Standards, rather than silently treating it as an ordinary ticket attempt or adding an unconditional third ticket reviewer. Pin source/cumulative baseline and inventory, preserve separate review history, and reject missing, incomplete or stale assessments before affected integration or QA readiness.
- [ ] Ordinary in-scope ticket blockers follow existing bounded repair policy; a cumulative blocker that cannot be corrected under that policy, a proposed scope/ownership change or consequential risk decision preserves work and stops with an incomplete human-decision handoff, without inventing extra repairs. Resolve it through an explicitly authorized amendment/fresh run with prior evidence linked; a disposition alone cannot resume a stopped run. Such work cannot integrate or obtain a consumable QA request while required blocking review work is unresolved. Optional findings retain inspectable dispositions and do not trigger repairs merely for being optional.
- [ ] Human review decisions remain separate from exact-candidate QA acceptance. Validate the review/scope/revision/finding identity and explicit reason before applying a disposition; agents cannot author their own consequential acceptance. Review completion, findings dispositioned, candidate awaiting QA, milestone promoted and feature complete remain distinct recorded outcomes.
- [ ] Keep immutable reports, append-only disposition history and completed work linked across deliberate stop/continue. Produce required review artifacts before freezing QA evidence; during a frozen QA wait, reject edits or preserve new proposals outside the frozen evidence and require renewed readiness/request as applicable. Preserve legacy report identity/finding fields, checkpoint version 1, gate evidence and artifact names; new review state is additive/optional for old records and never creates legacy review attestations retroactively.
- [ ] Verify through the public CLI with scripted external processes and real isolated Git: clean ticket/cumulative review, missing coverage, stale source, duplicate local finding IDs, fixed/deferred/awaiting-decision histories, blocked readiness/integration, rejected unauthorized dispositions, optional-only progress, failed review invocation and deliberate continuation with preserved records. Extend guide/status contracts and retained evidence, with actual live-agent proof left to ticket 34.

## Verification

Map existing report, human-decision, repair, optional-finding, milestone and continuation scenarios first. Add only distinct new runtime review-history/checkpoint/authority cases at the existing public CLI/scripted-process/real-Git seam. Run the full final-source suite and static gates, plus installed CLI checks where this ticket changes entry points or their observable contract. Genuine old checkpoint compatibility remains required; new review artifacts cannot invalidate a frozen old checkpoint merely by being introduced.

Use the [testing policy](../../../docs/agents/testing.md), [Python environment](../../../docs/agents/python-environment.md) and [shared review-process verification](../spec.md#review-process-verification). Validate documents, skills, source links and isolated workflow observations for guidance changes; executable harness changes retain the full final-source suite, strict typing, lint, format, whitespace and independent implementation reviews. Preserve actual command results, source/guidance/model identities and raw observations; scripted reviewers cannot establish reviewer judgment.

## Handoff

Use the [shared worker handoff](../README.md#worker-handoff). Carry pending reviews and unresolved findings without rewriting prior reports. Ticket completion does not accept a milestone. Select further work only through [milestone eligibility](../milestones.md); no automatic next-milestone execution or human acceptance is authorized.

## Comments

### Related development-workflow evidence

The completed [workflow-efficiency follow-up](../archive/workflow-efficiency/README.md)
retains the preparation, repair-diagnosis and evidence-reuse lessons learned after
ticket 19, including original independent reviews. The current
[development procedure](../../../docs/agents/review-records.md#prepare-review-and-repair) is reached
through existing skill/handoff routes. Consult the archive for rationale when
implementing this ticket's approved runtime review contract; the development
guidance is not evidence that runtime enforcement already exists. This context
adds no acceptance criterion or dependency.
