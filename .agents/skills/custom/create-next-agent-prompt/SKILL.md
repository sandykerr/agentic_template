---
name: create-next-agent-prompt
description: Create or refresh next_agent_prompt.md with a scoped implementation handoff for a fresh agent, either on request or after a local Markdown ticket is fully completed.
---

# Create next-agent prompt

Write a self-contained prompt for a fresh agent using [implement-with-checkboxes](../implement-with-checkboxes/SKILL.md). Save it to `next_agent_prompt.md` at the repository root unless the user specifies another destination. Creating the prompt does not start another implementation or harness run.

## Select the ticket

1. Read applicable `AGENTS.md` instructions and the repository's issue-tracker, readiness, and domain guidance. Inspect the worktree and any existing destination file; preserve unrelated changes. Use the feature and completed ticket supplied by the caller, or the user's explicit target. Ask for the feature only if repository context cannot identify it.
2. Read the feature index, ticket headers, and completion evidence needed to identify the next eligible ticket. A readiness label alone is not prerequisite completion, and `Blocked by:` remains dependency history even after prerequisites finish. Verify completion from criterion evidence, checks, independent reviews, and implementation/bookkeeping commits rather than inferring it from ticket numbers or header status alone.
3. Honor explicit user selection and documented feature priorities, subject to readiness and prerequisites. Otherwise choose the lowest-numbered open, unclaimed, agent-ready ticket whose prerequisites are verified complete. For an explicit but ineligible target, report its blockers instead of generating an executable assignment. Do not silently substitute another feature or ticket.
4. If no ticket is eligible, write a short handoff status in the destination explaining whether the feature is complete or listing the remaining prerequisite/readiness blockers with evidence links. Replace a stale generated implementation prompt with that status; do not invent work or mark unresolved work complete.

## Gather focused context

Read the selected ticket, its referenced spec sections, relevant glossary/ADRs, current public contracts, documented checks, and prerequisite completion evidence. Inspect implementation entry points or existing tests only as needed to make the handoff concrete. Use the feature's context policy; do not replay sibling transcripts or load unrelated spec sections by default.

Identify every acceptance criterion, the public testing seam, compatibility requirements, explicit scope exclusions, and any unresolved decisions. Use the existing approved testing seam when one exists; otherwise tell the next agent to establish it with the user before writing tests. Preserve requirement wording and scope when translating criteria into implementation instructions.

## Draft the prompt

Write directly to the next agent, beginning with `Use $implement-with-checkboxes to implement only:` and the exact repository-relative ticket path. Include the ticket title, exact scoped spec references, and enough project-specific context to work without the preceding conversation. Use the current skills and tracker rules; keep detailed invariant workflows in their authoritative sources while making the consequential gates explicit in the handoff:

- **Starting state:** Follow `AGENTS.md`; capture the next agent's starting HEAD as its fixed review baseline; inspect/preserve the worktree; verify prerequisite implementation and completion evidence. Historical commit references are context, not a replacement for capturing that baseline.
- **Bounded implementation:** Cover every acceptance criterion with observable evidence, preserve existing passing/rejection behavior, document affected contracts, and name the deferred neighboring features. Do not expand the ticket or resolve an architectural decision the human still owns.
- **Environment and tests:** Read the repository's environment guidance before Python, dependency installation, or checks and use its reusable environment. Reference its testing policy and [test-strategy](../test-strategy/SKILL.md): map existing coverage before adding tests, select focused checks, and plan evidence capture during required verification. Use `$tdd` for missing behavior at the agreed public seam, one failing behavioral test followed by its implementation per slice. Name the project's actual fixture/process/repository requirements and observable success/failure evidence. Preserve the required complete-suite checkpoint and explicit ticket checks; keep detailed selection and evidence-reuse rules in the testing policy.
- **Committed review:** After checks pass, commit only the implementation before `$code-review`, whose committed-diff review cannot see uncommitted work. Supply the captured baseline, ticket, and relevant spec requirements explicitly. Obtain separate fresh Spec and Standards reviews; fixture reviewers are not substitutes. For test changes, supply the coverage map, testing policy, and test-strategy's review guidance to these existing reviewers. Fix blocking findings, rerun affected checks, commit repairs, and re-review changed code against the original baseline. Record optional suggestions separately.
- **Completion bookkeeping:** After verified implementation and reviews, reconcile acceptance markers, set `**Status:** completed`, retain prior readiness in the completion comment, and preserve `Blocked by:`. Record implementation commits, criterion-specific evidence, actual checks, independent review outcomes, and unresolved items; link evidence from the feature index. Commit only this ticket's bookkeeping separately from implementation. If verification fails, leave unverified criteria unchecked and report the exact blocker.
- **Next handoff:** After implementation and bookkeeping are committed and fully complete, follow the implementation skill's automatic `$create-next-agent-prompt` step for the next eligible ticket, including its separate handoff commit and final report.
- **Boundaries and report:** Keep each agent within the applicable context target (250K active context for this feature unless changed by the user). Preserve approved inputs belonging to an active harness run and report that condition as a blocker to mutations. Do not push without explicit authorization. Report implementation/bookkeeping commits, check and review outcomes, unchecked criteria, and the next prompt path or exact handoff blocker. Claim completion only when the required gates actually passed.

Adapt these instructions to the selected ticket rather than copying the previous ticket's criteria, exclusions, expected results, or test counts. Link prerequisite evidence instead of treating old outcomes as proof of the new implementation.

## Save and verify

Write the actual prompt as Markdown, without an enclosing code fence or unresolved template placeholders. Refresh an existing generated handoff; preserve unrelated user-authored content or edits, using a separate destination and reporting the conflict if they cannot be retained safely.

Read the saved file back. Check every ticket/spec/evidence path, criterion coverage, prerequisite eligibility, scope boundaries, and consistency with the current implementation skill. An ineligible/all-complete handoff must clearly be a status report, not an instruction to execute stale work.

Return the destination, selected ticket and selection reason, or the no-eligible-ticket status. When invoked by `implement-with-checkboxes`, leave committing the generated handoff to that caller; when invoked directly, commit only if requested. Never launch the next agent as part of this skill.
