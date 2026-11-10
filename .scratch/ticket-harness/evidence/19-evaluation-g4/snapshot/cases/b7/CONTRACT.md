# Repository preflight
`validate` owns the local repository preflight and returns the resolved root and
requested branch. Reject failed Git commands, detached HEAD, an unexpected branch,
a dirty worktree (including untracked files), absent base revision, and a base that
is not an ancestor of HEAD. Read-only; no saved state or mutation. The injected
`git` callable accepts argument lists and returns CompletedProcess-like results;
it runs against the requested checkout with text capture, never a shell. Git
failure details may be reduced to ValueError. No class requirement or generic
validation framework. The caller selects policies through `expected_branch` and
`base`; it should not reproduce these validation decisions.
