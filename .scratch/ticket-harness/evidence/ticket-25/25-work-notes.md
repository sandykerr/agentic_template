# Ticket 25 implementation notes

Fixed baseline: `2c01fe9fe04c78fa10a2dac11e94826876467562`. Existing worktree
changes are retained in starting-status.txt/starting-worktree.patch; the approved
new bundle is already present but uncommitted and must be read as supplied input.
Ticket 24 completion/source and actual M1 acceptance checked against their records.
No active harness run has been launched by this assignment.

Ownership: the standalone `python -m ticket_harness.evidence` development CLI owns
allocation and capture registration. Producers write only within their assigned
payload directories. A feature evidence-directory advisory lock serializes helper
writers. Review namespaces have no capture writer: the helper preserves them;
future reviewers/tools must use the same lock protocol. Ticket artifacts point to
shared JSON artifacts, whose scope links back to the issue paths. Approved issue
files are never modified by capture. No harness runtime caller is added.

Durable state: immutable allocation receipts, append-only capture identities in
one evidence-review.json per folder, relative shared references. Registration
hashes payloads and records supplied source/activity/result facts, distinguishes
original/derived and records original identities for derivations. New allocations
have new IDs even when producer/purpose/bytes match; no approval is copied.
Malformed metadata, changed registered originals, unsafe paths and declared
protected destinations fail visibly on stderr/nonzero. JSON replacement is atomic;
shared-link updates span files and are idempotent, so a partial link write may be
retried without losing captures/decisions. No crash-recovery guarantee is added.

Protection: only `.scratch/<feature>/evidence` in the current Git repository is
writable. Reject symlink components and linked metadata/payloads. The operator
supplies active-input/frozen roots with --protect (persisted in allocations), and
must retain capture outside active approved/frozen inputs. No automatic discovery
of arbitrary external harness runs or adoption of run-owned output is claimed.

Architecture triggers at start: new capture lifecycle YES; persistence/restoration
YES (new receipts and JSON); shared mutable state YES; additional writer YES
(helper owns capture namespace, existing future review owner remains separate).
Broader affected-workflow High Standards assessment required before integration.

Coverage map (approved CLI/process/real Git/filesystem seam):
- Existing tests: harness run/status/QA/continuation compatibility; no capture cases.
- New tracer: ticket allocation + source/activity/result/hash and observed bytes.
- New shared case: descriptive/milestone destination and references from two tickets.
- New concurrency case: distinct allocations plus no lost JSON capture updates.
- New failure cases: overwrite/changed-original, traversal/aliases, frozen roots,
  malformed metadata and missing source/derived identity; preserve decision fields.
- Guidance: skill validator, relative links, isolated skill-guided actual capture.
Completion: full pytest, strict mypy, Ruff lint/format, whitespace; standalone
installed-module CLI check for the newly packaged helper, and skill validation.
Actual evidence retained before fresh independent Spec/Standards review.

Configured assignments: GPT-6.1 Sol Medium worker/repair, High separate reviewers,
250000 active-context target. This session cannot change its root model/reasoning;
actual backend enforcement/telemetry unavailable. Fresh reviewer assignments will
request the approved settings and report availability rather than invent delivery.

## Compute environment diagnosis

All 23 new focused cases pass. First full verification was deliberately interrupted
after 4 failed / 243 passed (pytest exit2): Forest203's /tmp and /var/tmp are both
noexec. Its Git-hook integrity cases and executable-file preflight cases therefore
cannot exercise their intended paths. Isolated hook reproduction failed on /tmp
and passed unchanged in executable shared TMPDIR. Host mount/probe output is in
25-hook-host-probe.log; actual reproductions in 25-hook-reproduction.log and
25-hook-executable-temp.log. The disposable hook probe observed Git's explicit
"ignored because it's not set as executable" warning. No runtime/test source was
changed for this environmental correction. New full run uses checkout-local
.scratch/ticket25-compute-temp as TMPDIR with one BLAS/OpenMP thread. This path is
execution scratch, not authoritative evidence or a feature input; retained
observations are copied to the allocated verification destination.

The first wheel command also showed no setuptools in the frozen development
environment. The retry uses pip's standard isolated build with pyproject.toml's
pinned backend, preserving the checkout environment; no dependency change is made.
First verification capture remains registered as failures, never relabeled passed.

The executable shared-TMPDIR full run passed its first groups but took roughly ten
minutes for only the first12% (retained progress/process evidence). A later host
probe found /dev/shm executable with57GiB available; direct executable probe passed.
The slow run was deliberately interrupted for resource-efficient verification,
with its partial results preserved. The final full run uses a fresh owner-private
/dev/shm/ticket25-verification-* temporary directory on the same idle Forest203,
unchanged source and one thread. Required observations are still retained on shared
storage. This is a temporary-storage correction, not test/source weakening or a
claim that an interrupted suite passed. Use executable node-local scratch for this
host's future Git-hook/executable checks; /tmp and /var/tmp remain unsuitable.
