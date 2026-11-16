# Current instruction navigation during repair verification

A concurrent workspace documentation edit renamed the feature's evidence-policy.md
to evidence-workflow-spec.md and replaced the missing approval link with the
feature index's ticket-publication-decision section. Actual live files were
compared with the original retained inputs: ticket25 acceptance criteria and
capture/structured-record/shared ownership contracts are unchanged. Changes are
current navigation/title/publication provenance plus removal of an unrelated
historical cleanup-account requirement. Current spec/ticket/milestones link to
the new authoritative name. These edits belong to the concurrent authoring work;
this implementation preserves them rather than restoring an obsolete path.

The original round1 reports/snapshots retain their actual old input identities and
missing-link observation. [Current instruction snapshots](instructions-current/)
preserve the now-current feature spec, workflow spec, milestones and ticket.
Original relative links resolve against their original feature/issue locations.
The live feature index documents the rename and publication reconstruction.
No human approval is invented by this implementation; the exact current user
implementation request remains the task authorization.

The first repair full-check driver stopped before running any test because its
input-manifest path used the old name. 25-repair1-full-driver.log is retained with
that preparation failure (exit1), not relabeled a runtime test failure or pass.
The original verifier script stays unchanged as execution evidence. The new
25-verify-repair1.py changes only the governing input filename and is now running
through retained Forest203 session10089, job PID4020397. Its actual capture is
verification-71288fc1a1da4058830978bc454711dc. Required source/check/evidence gates
remain unchanged, and repaired product/test bytes remain frozen.
