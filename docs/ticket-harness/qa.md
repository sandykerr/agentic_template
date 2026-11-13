# Milestone QA and continuation

An approved [milestone plan](inputs.md#approved-milestone-plans) runs fixed groups
into `integration`, the feature branch. Plan approval authorizes those inputs;
milestone acceptance requires a human decision for an exact tested candidate.
Development checkpoints for building this harness are separate from these
target-repository runtime plans. Return to the [harness guide](../ticket-harness.md).

## Prepare a milestone candidate

Once the group's tickets are Done, the milestone candidate combines the exact
feature tip and **current** development tip; starting development remains recorded
separately. Preparation exposes `outcome: "preparing_milestone"` / milestone state
`preparing` and reruns `suite` on that exact candidate with
`TICKET_HARNESS_STAGE=milestone-regression` and the `candidate` timeout. This
separate regression neither skips ticket candidate gates nor reuses their evidence.

Clean automatic merges support nonoverlapping edits within one file. An independent
plain merge in an isolated bare Git directory ignores project hooks/configuration/
attributes to detect source-changing resolutions. Git must support
`merge-tree --write-tree` and global `--attr-source`; missing support fails closed.
Unresolved conflicts or candidates differing from the clean merge stop with source
preserved. Custom merge-driver resolutions and merge-hook edits need renewed
applicable checks/reviews before QA; prior approvals cannot authorize them.
Automatic conflict repair/renewal workers are not provided.

Before issuing a request, the harness revalidates approved inputs, all verified
sources and both branch tips. Failed regression, mutated candidate/source or moved
branches stop with `outcome: "incomplete"` / milestone `preparation_failed`.
Candidate/source/gate evidence and external refs remain; completed tickets stay
Done. No QA request is issued. Preparation has no automatic repair budget and
does not consume ticket attempts.

## Inspect the QA request

Successful preparation keeps the foreground process running indefinitely with
`outcome: "awaiting_human_qa"`, `feature_complete: false`, and a `milestone` object
containing `id`, `state: "awaiting_human_qa"`, `feature_revision`,
`development_revision` and `candidate_revision`. The `tickets` mapping includes all
required tickets; later groups remain `Pending` with attempt zero.
`selected_tickets` contains only the current group in numeric order.

`qa_request` points to `qa-request.json` in the run directory, outside source
worktrees. It records unique request/run identities, the run directory, approved
plan version/approval and captured plan identity, milestone, feature/development
branches and revisions, exact candidate/worktree, planned human setup/actions/pass
conditions, and the actual passing regression gate with command, revision,
exit/timeout result and output artifact paths. The request supplies no human
decision. Candidate preparation never advances development or starts later work;
even a single final group with all tickets Done waits for human acceptance.

## Record acceptance of the exact request

The foreground runner watches separate run-directory `qa-decision.json`. Its exact
JSON contract has two fields: `decision`, the case-sensitive string `"APPROVED"`,
and `request`, the complete JSON object from the current `qa-request.json`, including
every identity, human check and regression-evidence field. Object key order and
whitespace do not matter; field names, value types and values must match. Duplicate
keys, extra fields, malformed JSON, incidental approval text, missing fields, stale
requests and replayed approvals cannot promote or unlock work.

Write decisions atomically (write a temporary sibling file, then rename it) after
the human accepts that exact request. The human/QA session owns this artifact;
agent assignments and implementation/repair output cannot authorize QA. Requests,
decisions, run records and prior evidence are protected across external process
boundaries under the [trusted-process integrity contract](agents.md#trust-and-integrity).
This protection does not provide an operating-system sandbox.

`qa_decision` names the watched path. `qa_decision_status` reports `missing`,
`unreadable`, `rejected` or `consumed`; `qa_observations` retains each distinct read
decision's actual bytes in an artifact, SHA-256, request identity and validation
diagnostic. A regular file is required; directories and symlinks remain unreadable
waits. Invalid or absent decisions leave `awaiting_human_qa` and do not consume
repairs or use agent/check timeouts. `status RUN_DIRECTORY` observes these waits.

## Promote and admit the next group

Before consuming exact acceptance, the runner revalidates captured inputs, all
applicable verified sources, the unchanged request and retained evidence bytes.
A single Git ref transaction compares both expected feature/development tips and
advances both to the exact tested candidate. Neither branch may be checked out in
any caller worktree. External ref movement is preserved; stale source/input/request/
evidence or branch state stops with `incomplete` and milestone `promotion_failed`,
requiring renewed candidate checks and acceptance. Ticket Done states remain intact.
No ref partially advances if either expected tip mismatches.

`qa_decisions` records consumed decision artifact/hash/request identities; `milestones`
records promoted groups. Requests are archived per group under `artifacts`; the
current `qa-request.json` is replaced for the next group. Consumption admits only
that next fixed group, starting workers from the aligned feature revision and
retaining every per-ticket gate and repair allowance. Later regression and candidate
artifacts use distinct milestone names. All required tickets Done still leaves
`feature_complete: false` until final acceptance promotes. Only then does the run
exit 0 with `outcome: "completed"` and `feature_complete: true`.

## Stop at an active QA wait

Request a deliberate clean stop from another shell:

```bash
python -m ticket_harness stop RUN_DIRECTORY
python -m ticket_harness status RUN_DIRECTORY
```

The installed `ticket-harness` command supports the same subcommands. `stop` exits 0
after acknowledging `outcome: "stop_requested"`; wait for the owning foreground
process to exit **2** and status to show `outcome: "stopped_at_qa"` before continuing.
Exit 2 means a successful planned stop with `feature_complete: false`.
Stop is supported only during an active QA wait; it never terminates a worker,
review, check or merge. An approval racing a stop can win first; acknowledgement
alone does not establish a stopped checkpoint. Inspect the actual run outcome.

## Continue a stopped checkpoint

```bash
python -m ticket_harness continue RUN_DIRECTORY
```

The durable `qa-checkpoint.json` and immutable `checkpoints/<checkpoint_id>.json`
archive bind the normalized approved configuration, typed run state, plan/version,
Done/attempt/consumed-decision identities, every applicable verified source,
request bytes and original evidence hashes. New decision observations are also
bound. Prior checkpoints remain archived across repeated stops.

`continue` acquires exclusive ownership of the run directory and validates captured
approved sources and snapshots, checkpoint/record/request/evidence identities,
clean verified trees, and both expected branch tips and checked-out status before
changing the run. Changed or inconsistent state rejects with exit 1 and a unique
diagnostic under `rejections/`, preserving prior records, checkpoints, artifacts
and refs. Keep the run directory and checkpoint/history unchanged to resume it.

Continuation watches the same exact separate QA decision contract, including a
decision written while stopped. It preserves Done tickets and previous artifacts,
skips their assignments and baseline, and admits only the approved next group.
It remains foreground and waits indefinitely at subsequent QA checkpoints; only
final acceptance exits 0/completed/true.

Each run has one active owner, serialized by a POSIX lock on the directory inode.
Concurrent continuation rejects rather than repeating assignments or consuming/
promoting acceptance twice. The operating system releases ownership on process exit,
but only deliberately persisted `stopped_at_qa` is eligible for continuation.
Arbitrary mid-stage crash recovery and background launch are not provided; process
access follows the [trusted-process contract](agents.md#trust-and-integrity).
A new `run` cannot use recorded ticket completion to skip first-group QA.
`status` remains observational and does not revalidate stopped candidates.
