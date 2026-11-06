Use $implement-with-checkboxes to implement only:
.scratch/ticket-harness/issues/04-promote-only-the-verified-candidate.md

Ticket: **04: Promote only the exact verified candidate**.

Follow AGENTS.md and the ticket's scoped sections in .scratch/ticket-harness/spec.md:

- Independent checks and exact revisions
- Requirements, configuration, and run records
- Agent contracts and access

Keep each agent below the feature's 250K active-context target. Read docs/agents/python-environment.md before Python, dependency installation, or checks, and use its reusable micromamba environment. Follow the domain glossary and relevant ADRs before exploration/design.

Before changing code:

- Capture your current HEAD as the fixed review baseline; historical revisions below are context, not your baseline.
- Inspect the worktree and preserve unrelated edits. The preceding implementation left a pre-existing skill relocation from .agents/skills/implement-with-checkboxes/ to .agents/skills/custom/ unstaged; inspect its current state before making assumptions.
- Verify ticket 01's prerequisite implementation and completion evidence: .scratch/ticket-harness/evidence/01-completion.md and its ticket/index comments. Its legacy header retains ready-for-agent, so verify completion from actual criteria, implementation/bookkeeping commits, checks, and independent reviews rather than the label alone.
- Read the current CLI/input/report contracts in docs/ticket-harness.md, runner.py, git.py, inputs.py, agents.py, records.py under ticket_harness/, and relevant tests in tests/test_cli.py, tests/test_preflight.py, and tests/test_reports.py.
- Preserve ticket 01's passing cycle and gate rejection, ticket 02's preflight behavior, and ticket 03's complete typed report validation and durable diagnostics. Ticket 03's final implementation is 07094fa; bookkeeping is 9604651. See .scratch/ticket-harness/evidence/03-completion.md and .scratch/ticket-harness/evidence/02-completion.md for compatibility context. Prior test counts are historical evidence, not proof of this implementation.

Protect the existing submission-to-integration transaction and its approved snapshots. Cover every ticket-04 acceptance criterion with actual observable evidence:

- Record approved input identities and detect attempts to alter requirements or harness-owned state from an agent assignment.
- Bind lightweight checks and both review results to the submitted revision, and the broader suite to the candidate revision.
- Advance integration only to the exact tested candidate while the expected previous integration revision is still current.
- If integration changes externally, a merge fails, or candidate verification fails, preserve evidence and leave the current integration branch unchanged by this operation.
- Source changes after review invalidate that approval and require renewed verification before integration.
- Preserve unrelated caller work and rejected work for inspection; never mark an unverified revision Done.

Git already owns submission capture, detached worktrees, candidate merges, source-cleanliness checks, and compare-and-swap promotion. Strengthen their observable invariants rather than treating report claims as authority. Approved snapshots and harness execution records are separate from editable source. Report validation currently rejects malformed/incomplete/stale/incorrectly typed reports, nonzero exits, duplicate/nonfinite/overflow JSON, and nesting above 100 object/array levels. Valid human-decision-needed reports stop before submission/review/repair; preserve that behavior. Document any affected public contract.

Use $tdd at the already agreed public CLI/Git/report seam: scripted external processes and real temporary Git repositories. Write one failing behavioral test, implement that slice, and repeat. Exercise controlled external branch movement, approved-input or state tampering, failed merge/candidate checks, and source/revision changes after verification. Assert exit/outcome, exact Git identities, gate validity, preserved artifacts/diagnostics, unchanged caller work, and no unverified Done through public observations, not parser internals or internal mocks.

This ticket does not add automatic repairs, crash recovery/resume, concurrent ticket execution, dependency scheduling, timeouts, live Codex, new role-skill delivery, or operating-system role-access enforcement. Leave those features with their owning tickets. Apply the existing combined design policy without inventing abstractions or resolving architectural choices the human still owns.

Run focused tests and strict typechecking during implementation, then the complete suite and documented checks using the reusable Python environment. Available check tools at the preceding handoff were /tmp/ticket-harness-env/bin/mypy and /tmp/ticket-harness-env/bin/ruff; verify availability rather than assuming temporary tools persist. Documented checks include pytest, strict mypy, Ruff lint/format, and whitespace; verify packaging/installed CLI when appropriate.

After checks pass, create an implementation checkpoint commit containing only ticket 04 before invoking $code-review; its committed-diff review cannot see uncommitted code. Supply the captured baseline, ticket 04, and scoped spec requirements explicitly. Obtain separate fresh Spec and Standards reviews; scripted reviewers inside fixtures do not replace them. Fix blocking findings, rerun affected checks, commit fixes, and re-review changed code against the original baseline. Record optional suggestions separately.

After verified implementation and review, follow docs/agents/issue-tracker.md Completion bookkeeping:

- Ensure implementation and review fixes are committed.
- Check each acceptance criterion only with evidence from the verified revision and required independent reviews.
- Set ticket 04 to **Status:** completed only when all criteria and gates pass; record its previous ready-for-agent label in the completion comment and preserve Blocked by as dependency history.
- Append criterion-specific implementation/check/review evidence and unresolved items; link completion evidence from .scratch/ticket-harness/README.md.
- Verify the acceptance markers, header, completion comment, and feature index agree. Commit only ticket 04's bookkeeping separately from implementation.
- After implementation and bookkeeping commits exist and completion is fully verified, follow the implementation skill's automatic $create-next-agent-prompt step and commit that handoff separately. Do not start the next ticket.

Do not modify approved inputs belonging to an active harness run; report that condition as a blocker. Do not push. If any gate or required workflow step remains blocked, leave unverified criteria unchecked and report the exact blocker. Claim completion only after implementation, checks, independent reviews, commits, and bookkeeping are finished. Report implementation/bookkeeping/handoff commit references, check and separate review outcomes, unchecked criteria, and the next prompt path with its selected ticket or no-eligible-ticket status.
