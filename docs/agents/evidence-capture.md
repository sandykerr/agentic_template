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

## Explicit local retirement execution

`preview --authority FEATURE_RELATIVE_PATH --group ID` and `execute` with the
same arguments consume a **new** `retirement` proposal in the named existing
`evidence-review.json`. Repeat `--group` for an explicit selection. Preview reads
and locks existing evidence without writing. Execution performs complete preflight
before deleting anything, then rechecks authority, dependencies and each original
before its unlink. Any partial failure exits nonzero and appends the actual
per-file results to `execution_results`; approvals remain separate and unchanged.
Re-execution against missing originals is blocked. Arbitrary crash recovery is
not supported. All metadata/deletion mutations use the capture directory flock.

This is a minimum development-only execution contract, not ticket26 completion,
full inventory/assessment/reassessment tooling, runtime adoption or EC1 acceptance.
Historical assessments/approvals are never executable authority. Their `keep` and
`merge proposed` groups remain protected. Fresh review must establish contents,
remaining uses and applicable policy/consumer identities; an empty search or
capture registration cannot establish eligibility.

The exact new proposal schema is an object with these fields (no extra fields):

- `schema_version`: integer `1`.
- `source_identity`: nonempty description of the assessed source version.
- `protected`: array of regular-file identities for all lasting decisions, actual
  human approvals, independent reviews, needed inputs and other protected survivors.
- `groups`: nonoverlapping groups with exactly `id`, `action` (`keep`, `delete`,
  `merge`), `assessor`, `evidence_type`, `reason`, `files`, `remaining_uses`,
  `conditions`, `retained_results`, `source`, `replacements`, and `protected`.

An identity has exactly `path` (canonical feature-relative path), `size` (integer
bytes), `sha256` (hex digest), and `kind` (`regular`). Every source, retained
result, replacement, protection and condition-evidence identity must still match.
`source` includes retained exact code/source plus current policy and reader-context
identities needed to validate the decision. Files listed by unselected or keep
groups, all approval reports, source/results/replacements and condition evidence
are protected from every selected deletion. Operator `--protect PATH` additionally
protects active/frozen/continuable inputs or subtrees; operators must supply all
such inputs, because external runs are not discovered. Protected originals outside
evidence may be listed within the feature; use `--protect` for other paths.

Eligible groups have `evidence_type: "routine"`, nonempty retained results/source,
no remaining uses (`[]`), and nonempty `conditions`. Each condition has exactly
`id` (reason), `resolved: true`, and nonempty `evidence` identities. Uncertain,
durable or mixed-content originals stay protected. Classifications are attributed
judgments, not automatically inferred from filenames or hashes.

The sibling `retirement_approvals` array contains one fresh independent approval
for each selected group. Each object has exactly `group`, `proposal_sha256`,
`reviewer` (different from the assessor), `decision: "approve"`, `report` (identity
of the original independent report), and `human_merge` (normally null). The digest
is SHA256 of the complete `retirement` object serialized as UTF-8 JSON with sorted
keys, separators `(',', ':')`, default ASCII escaping and no NaN values. It binds
all groups, identities, retention conditions and context. The report retains
actual assignment/settings/inspection provenance; hashing does not prove judgment.
Missing, conflicting, stale or non-independent approvals cannot act.

A merge additionally requires nonempty `replacements` and `human_merge` with exactly
`actor`, `statement` (actual human approval), `proposal_sha256`, and `replacements`
(exactly matching the proposal). Changed originals or replacement bytes block
execution. Durable originals remain protected despite a replacement.

Only explicit, unaliased regular files within this feature's evidence directory
may be removed. Symlink components, hard links, traversal, control artifacts
(`evidence-review.json`, `allocation.json`) and overlapping retained dependencies
are rejected. Capture arrays and unknown top-level future fields survive updates;
unknown execution schema versions/fields are rejected. The tool assumes cooperative
writers; it does not guarantee safety against adversarial filesystem races.

Navigation remains `pending operator reconciliation` in the execution result.
After successful removals, the operator updates maintained navigation using actual
outcomes, preserving historical reports/manifests. Record that reconciliation under
the same evidence-directory lock. Failed removals must retain their live links.

If recording fails after an unlink, execution stops and returns nonzero with
`state: "partial"`, the actual observed per-file outcomes and `recording_error`
on stdout. The authority can therefore be incomplete; preserve stdout and resolve
that discrepancy before another proposal. The tool never invents a successful
record write or continues deleting after a failed outcome write.
