---
name: implement-with-checkboxes
description: Implement a local Markdown ticket with Matt Pocock's workflow, reconcile verified acceptance and completion status, and prepare the next-agent handoff.
---

# Implement with checkboxes

Read and follow [Matt's implementation skill](../../matt-pocock/implement/SKILL.md) for the assigned ticket. This wrapper adds the review checkpoint, completion bookkeeping, and next-agent handoff below; keep the upstream skill unchanged. Where a Skill tool is unavailable, read the referenced skill and perform its workflow directly.

## Implement and review

1. Follow `AGENTS.md` and the ticket's scoped spec references. Read the repository's [issue-tracker conventions](../../../../docs/agents/issue-tracker.md) and [testing policy](../../../../docs/agents/testing.md). Capture the starting `HEAD` as the review baseline and inspect the worktree, preserving unrelated changes. When adding or changing tests, use [test-strategy](../test-strategy/SKILL.md) to map existing coverage and choose verification scope before the upstream TDD workflow. Implement only the assigned ticket using that workflow and its required checks.
2. After checks pass, create a checkpoint commit containing only this implementation **before** invoking `code-review`: its current committed-diff review cannot see uncommitted changes. Supply the captured baseline, ticket, and relevant spec requirements. For later repairs, keep that original baseline so the review covers the whole implementation.
3. Obtain the upstream skill's separate, fresh Spec and Standards reviews. For test changes, supply the coverage map, testing policy, and test-strategy's review guidance to these existing reviewers. Scripted fixture reviewers verify harness behavior; they do not replace reviews of the implementation itself. Fix blocking findings, rerun affected checks, commit fixes, and re-review changed code. Record optional suggestions without treating them as mandatory fixes. If implementation already exists and the diff is empty, verify its recorded checks and reviews against the current revision instead of treating an empty review as a pass.

## Reconcile the ticket

After implementation checks and reviews, apply the tracker's **Completion bookkeeping** rules. Map each acceptance criterion to evidence from the verified implementation revision; completing code or receiving an agent's success report alone is insufficient.

Update satisfied acceptance checkboxes. Once every criterion and required gate is verified, set the ticket's header to `**Status:** completed`; record its previous readiness label in the completion comment. Keep `Blocked by:` as the declared dependency history. If verification is incomplete, retain the existing readiness status and explain what remains pending.

Append the completion comment and link evidence from the feature index when present. Before committing, verify that the acceptance markers, header status, completion comment, and feature index agree on the verified outcome. Commit these documentation changes separately from the reviewed implementation; stage only this ticket's bookkeeping. Review any subsequent code changes through the implementation gates again.

Declare the ticket complete only when every criterion is verified, required checks pass, blocking findings are resolved, and implementation and bookkeeping are committed. If a required step fails or approved inputs belong to an active harness run, report the exact blocker and leave completion pending.

## Create the next-agent handoff

After the ticket is fully completed and its implementation and bookkeeping commits exist, automatically call `$create-next-agent-prompt` using [its skill instructions](../create-next-agent-prompt/SKILL.md). Supply the completed ticket, feature index, completion evidence, and any explicit user sequencing preferences. Where a Skill tool is unavailable, read that skill and perform its workflow directly. This step creates the handoff without starting another ticket.

Commit the generated `next_agent_prompt.md` (or the user's chosen destination) separately from implementation and ticket bookkeeping, staging only the generated handoff. If no ticket is eligible, save and commit the skill's handoff status instead of leaving a stale execution prompt. If prompt creation or its commit is blocked, report the completed ticket and the exact handoff blocker without claiming the handoff is ready.

Report the implementation, bookkeeping, and handoff commit references, checks, independent review outcomes, any unchecked criteria, and the next prompt path with its selected ticket or no-eligible-ticket status.
