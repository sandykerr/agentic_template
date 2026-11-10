---
name: implement-with-checkboxes
description: Implement a local Markdown ticket with Matt Pocock's workflow, reconcile verified acceptance and completion status, and prepare the next-agent handoff.
---

# Implement with checkboxes

Read and follow [Matt's implementation skill](../../matt-pocock/implement/SKILL.md) for the assigned ticket. This wrapper adds the review checkpoint, completion bookkeeping, and next-agent handoff below; keep the upstream skill unchanged. Where a Skill tool is unavailable, read the referenced skill and perform its workflow directly.

Read the [shared planning reference](../references/planning.md#milestone-membership) for milestone membership and approval boundaries, and its [role and testing contracts](../references/planning.md#role-and-testing-contracts) for defaults and overrides. Use the approved plan's earliest eligible milestone and preferred order, verified prerequisites, and recorded human QA decisions to confirm the assignment is eligible. An explicit target or older lower ticket number cannot bypass a human checkpoint; report the exact blocker for an ineligible assignment.

Use fresh implementation and repair assignments with Medium reasoning by default; apply an explicit ticket worker override to both. Configure the separate fresh Spec and Standards assignments independently, each defaulting to High. Carry the approved model, role guidance and context target; report missing configuration rather than inventing it. These are development assignment settings, not proof of runtime profile enforcement or skill capture.

Read and apply the shared [ownership and review-scope contract](../../../../docs/agents/ownership-review.md)
before implementation/repair and when preparing both upstream `code-review`
assignments. Record the affected flow and changed/unchanged ownership in the
implementation evidence; supply the shared contract to each fresh reviewer. Its
whole-ticket scope and report requirements take precedence over upstream
diff-hunk-only wording and the under-400-word report briefs; retain a concise
summary with enough linked detail for the required evidence.

For this repository's ownership refactors 20–24, use the
[evaluated development-review guidance and corpus](../../../../docs/agents/reviewer-evaluation.md)
when preparing both fresh review assignments. Carry the evaluated guidance
identity and finite limitations; corpus reports do not review the new refactor.

Apply [development architecture checkpoints](../../../../docs/agents/architecture-checkpoints.md)
at ticket start and after implementation. Record each risk trigger and required
broader assessment before integration; no-trigger tickets retain the two existing
review axes. At milestone readiness, carry the cumulative assessment, exact source,
prior findings and missing/stale work into the handoff; a completed review alone
never accepts a milestone.

## Implement and review

Read the repo-owned [review record contract](../../../../docs/agents/review-records.md)
when preparing assessments, saving reports or handling findings. Use its templates
to attach routine Spec/Standards reports to one ticket assessment, preserve the
original baseline/reports and carry full finding keys/history into repairs and
independent re-review. Keep assessment completion, outstanding findings and human
QA separate; record human-owned decisions rather than inferring authority.

1. Follow `AGENTS.md` and the ticket's scoped spec references. Read the repository's [issue-tracker conventions](../../../../docs/agents/issue-tracker.md) and [testing policy](../../../../docs/agents/testing.md). Capture the starting `HEAD` as the review baseline and inspect the worktree, preserving unrelated changes. When adding or changing tests, use [test-strategy](../test-strategy/SKILL.md) to map existing coverage and choose verification scope before the upstream TDD workflow. Implement only the assigned ticket. Use the testing policy's focused development checks and required completion checks; standalone documentation/skill work receives its documented validation rather than an artificial TDD cycle or runtime suite replay.
2. After checks pass, create a checkpoint commit containing only this implementation **before** invoking `code-review`: its current committed-diff review cannot see uncommitted changes. Supply the captured baseline, ticket, and relevant spec requirements. For later repairs, keep that original baseline so the review covers the whole implementation.
3. Obtain the upstream skill's separate, fresh Spec and Standards reviews with the independently configured reviewer settings above. For test changes, supply the coverage map, testing policy, and test-strategy's review guidance to these existing reviewers. Scripted fixture reviewers verify harness behavior; they do not replace reviews of the implementation itself. Resolve blocking findings through fresh repair assignments with the worker setting, rerun affected required checks, commit fixes, and re-review the whole implementation against the original baseline. Record optional suggestions without treating them as mandatory fixes. If implementation already exists and the diff is empty, verify its recorded checks and reviews against the current revision instead of treating an empty review as a pass.

## Reconcile the ticket

After implementation checks and reviews, apply the tracker's **Completion bookkeeping** rules. Map each acceptance criterion to evidence from the verified implementation revision; completing code or receiving an agent's success report alone is insufficient.

Update satisfied acceptance checkboxes. Once every criterion and required gate is verified, set the ticket's header to `**Status:** completed`; record its previous readiness label in the completion comment. Keep `Blocked by:` as the declared dependency history. If verification is incomplete, retain the existing readiness status and explain what remains pending.

Append the completion comment and link evidence from the feature index when present. Before committing, verify that the acceptance markers, header status, completion comment, and feature index agree on the verified outcome. Commit these documentation changes separately from the reviewed implementation; stage only this ticket's bookkeeping. Review any subsequent code changes through the implementation gates again.

Declare the ticket complete only when every criterion is verified, required checks pass, blocking findings are resolved, and implementation and bookkeeping are committed. If a required step fails or approved inputs belong to an active harness run, report the exact blocker and leave completion pending.

## Create the next-agent handoff

After the ticket is fully completed and its implementation and bookkeeping commits exist, automatically call `$create-next-agent-prompt` using [its skill instructions](../create-next-agent-prompt/SKILL.md). Supply the completed ticket, approved plan/milestones, feature index, completion evidence, role settings, recorded QA references and any explicit user sequencing preferences. Where a Skill tool is unavailable, read that skill and perform its workflow directly. It selects eligible implementation work or writes a QA handoff/waiting status at a checkpoint. Ticket completion does not accept a milestone; all tickets Done while final QA is unaccepted does not complete the feature. This step creates the handoff without starting another ticket.

Commit the generated `next_agent_prompt.md` (or the user's chosen destination) separately from implementation and ticket bookkeeping, staging only the generated handoff. If no ticket is eligible, save and commit the skill's handoff status instead of leaving a stale execution prompt. If prompt creation or its commit is blocked, report the completed ticket and the exact handoff blocker without claiming the handoff is ready.

Report the implementation, bookkeeping, and handoff commit references, checks, independent review outcomes, any unchecked criteria, and the next prompt path with its selected ticket or checkpoint/blocker status. Keep orchestration, candidate preparation/promotion, QA-session execution and approval recording in their separately authorized workflows. This development wrapper neither supplies human acceptance nor launches runtime work.
