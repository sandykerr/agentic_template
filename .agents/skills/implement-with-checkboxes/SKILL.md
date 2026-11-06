---
name: implement-with-checkboxes
description: Implement a local Markdown ticket with Matt Pocock's implementation workflow, then reconcile acceptance checkboxes and completion status with verification and review evidence.
---

# Implement with checkboxes

Read and follow [Matt's implementation skill](../matt-pocock/implement/SKILL.md) for the assigned ticket. This wrapper adds the review checkpoint and completion bookkeeping below; keep the upstream skill unchanged. Where a Skill tool is unavailable, read the referenced skill and perform its workflow directly.

## Implement and review

1. Follow `AGENTS.md` and the ticket's scoped spec references. Read the repository's [issue-tracker conventions](../../../docs/agents/issue-tracker.md). Capture the starting `HEAD` as the review baseline and inspect the worktree, preserving unrelated changes. Implement only the assigned ticket using the upstream workflow and its TDD/check instructions.
2. After checks pass, create a checkpoint commit containing only this implementation **before** invoking `code-review`: its current committed-diff review cannot see uncommitted changes. Supply the captured baseline, ticket, and relevant spec requirements. For later repairs, keep that original baseline so the review covers the whole implementation.
3. Obtain the upstream skill's separate, fresh Spec and Standards reviews. Scripted fixture reviewers verify harness behavior; they do not replace reviews of the implementation itself. Fix blocking findings, rerun affected checks, commit fixes, and re-review changed code. Record optional suggestions without treating them as mandatory fixes. If implementation already exists and the diff is empty, verify its recorded checks and reviews against the current revision instead of treating an empty review as a pass.

## Reconcile the ticket

After implementation checks and reviews, apply the tracker's **Completion bookkeeping** rules. Map each acceptance criterion to evidence from the verified implementation revision; completing code or receiving an agent's success report alone is insufficient.

Update satisfied acceptance checkboxes. Once every criterion and required gate is verified, set the ticket's header to `**Status:** completed`; record its previous readiness label in the completion comment. Keep `Blocked by:` as the declared dependency history. If verification is incomplete, retain the existing readiness status and explain what remains pending.

Append the completion comment and link evidence from the feature index when present. Before committing, verify that the acceptance markers, header status, completion comment, and feature index agree on the verified outcome. Commit these documentation changes separately from the reviewed implementation; stage only this ticket's bookkeeping. Review any subsequent code changes through the implementation gates again.

Report the implementation and bookkeeping commit references, checks, review outcomes, and any unchecked criteria. Declare completion only when every criterion is verified, required checks pass, blocking findings are resolved, and bookkeeping is saved. If a required step fails or approved inputs belong to an active harness run, report the exact blocker and leave completion pending.
