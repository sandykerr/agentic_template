# Checkpoint preservation history

1. `produce.py` ran from clean starting source before any runtime edits; its actual
   producer/source identity, exit-2 stop and checkpoint/run copies are retained.
2. Its attempt to retain the TemporaryDirectory detached its automatic finalizer,
   but the graph generator subsequently called explicit fixture.doCleanups at
   interpreter shutdown. This erased the live repository. The first archive
   command failed with `Cannot stat: No such file or directory`, exit 2; the
   resulting empty `stopped-fixture.tar.gz` remains an unsuccessful capture only.
   It cannot support continuation, and no continuation is claimed for that fixture.
3. After local runtime edits, `git worktree add --detach` for an isolated producer
   failed with `.git/worktrees/... Read-only file system`, exit 128. No worktree
   was created or original source restored. Active focused checks were preserved.
4. `git archive 0d79d016907a03ce39d33c749523a8700e4233a4 | tar -x` created an
   isolated exact-baseline source snapshot at `/tmp/ticket20-producer-baseline`.
   `reproduce.py` uses that snapshot's tests/package/examples. It suppresses
   explicit fixture cleanup as well as detaching the temp finalizer. Its renewed
   actual record/checkpoint, source hashes, CLI stop and foreground exit 2 remain
   under `renewed/`; all runtime and test hashes independently match baseline Git
   blobs in `continue.py` before any continuation. This is a genuine baseline-code
   producer, never a post-refactor producer or hand-edited checkpoint.
5. The renewed live fixture was archived before continuing (`renewed/stopped-fixture.tar.gz`).
   `continue.py` ran from the final working source, completed remaining M2 work
   under a fresh owner, retained prior attempts/gates, observed one baseline,
   exactly two consumed fixture approvals and matching integration/dev final refs.
   `continue.log`, `renewed/continuation.json` and `renewed/continued-fixture.tar.gz`
   preserve the successful observation and all its real Git/worktree/CLI artifacts.

Chronological limitation: the original genuine producer preceded runtime edits but
its live state was lost. The successfully continued producer ran after local edits
in a separately verified pre-refactor source snapshot. Both original and renewed
provenance are retained; no claim that the renewed execution preceded those edits.
Root accepted this bounded recovery for substantive baseline compatibility and
independent reviews will assess the full history. All approvals here are synthetic
fixture data and supply no actual feature milestone QA acceptance.

The original continuation observation's `consumer_source` label has an incorrect
relative path. [Supplemental source mapping](renewed/consumer-source-crosscheck.json)
supplies the correct `../../20-final-source.json` path and identity digest, with
all final runtime hashes rechecked unchanged. The original observation is preserved.
