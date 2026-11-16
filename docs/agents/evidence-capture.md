# Development evidence capture

Use [capture-evidence](../../.agents/skills/custom/capture-evidence/SKILL.md) before
producing development checks, reviews or supporting captures. The standalone helper
is available as `.venv/bin/python -m ticket_harness.evidence`; runtime adoption is
separate. See its subcommand `--help` for arguments.

`allocate` accepts one ticket, or a descriptive shared name with two or more
relevant tickets. Tickets are matched uniquely from the feature's `issues/` paths.
Destinations are `evidence/ticket-ID/captures/ACTOR-UUID` or
`evidence/SHARED[/MILESTONE]/captures/ACTOR-UUID`. Reuse the same shared scope for
later producers; a different ticket membership requires a different descriptive
shared destination. Ticket folders are reserved; shared names cannot use `ticket-`.
Existing files and specialized historical subfolders are retained in place.

Each evidence folder has one `evidence-review.json` with schema version 1:

| Field | Owner and meaning |
| --- | --- |
| `folder`, `scope` | Helper: feature-relative folder and ticket issue links, shared name/milestone or explicit null |
| `captures` | Helper: append-only producer/purpose/source/activity/result, original/derived label, file paths/sizes/SHA256 and derivation identities |
| `shared_records` | Helper: feature-relative paths to authoritative shared artifacts; no copied shared decisions |
| `assessments` | Later assessment workflow; initially empty |
| `approvals` | Later review/human workflow; initially empty |
| `execution_results` | Later guarded execution tool; initially empty |

Allocation metadata in each producer directory records its scope and protected
paths. These receipts are capture provenance, never additional review decisions.
`register` reads completed regular files, checks previously registered captures in
that artifact, then atomically appends the new capture. An identical retry returns
the same record. A changed capture or result requires a new allocation; registration
rejects changed/missing originals instead of silently refreshing their identity.
New UUIDs never inherit existing approvals. Empty review arrays mean no review has
been recorded; an unknown historical outcome must be stated as unknown rather than
being converted to a passing result or zero. Source/activity/result are attributed
to the producer; hashing certifies file identity, not those statements' correctness.

All helper mutations acquire an exclusive `flock` on the feature's `evidence/`
directory descriptor. Future tools updating review namespaces must acquire this
same lock; producers do not edit consolidated JSON. Capture preserves review
fields, including unknown future fields, and rejects incompatible schemas rather
than resetting them. JSON replacement is atomic per file; shared references span
multiple files and a partial filesystem failure may leave incomplete links. The
command reports failure; retry allocation with the same scope to complete references.
An allocated but unregistered payload remains unreviewed and protected from any
inference of deletion eligibility. Arbitrary crash recovery is not promised.

The helper limits writes to the existing Git checkout's `.scratch/FEATURE/evidence`,
rejects symlink components and hard-linked mutable files/payloads, and never writes
issue/spec bodies or harness state. Pass all applicable active-input/frozen paths
with `--protect` before each subcommand; allocation protections persist for later
registration. A new freeze must be supplied at registration. Protection of a
subtree permits unrelated captures elsewhere. The helper does not discover external
runs or guarantee safety against concurrent adversarial filesystem replacement;
operators must keep active/frozen inputs outside writable output and producers must
honor their assignments. During active runs, use only the authorized run-owned
output workflow outside approved inputs; this helper is development-only.

Failures print a diagnostic on stderr and exit nonzero. Inspect returned artifacts
before retrying a partially completed operation. Never interpret registration or
schema validity as independent review, retention/deletion approval, finding
resolution, milestone acceptance or permission to promote.
