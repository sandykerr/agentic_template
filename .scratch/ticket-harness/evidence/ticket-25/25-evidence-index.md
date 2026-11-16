# Ticket 25 canonical evidence index

Ticket: [25](../../issues/25-guide-ticket-and-shared-evidence-creation.md).
Baseline: `2c01fe9fe04c78fa10a2dac11e94826876467562`.
[Work/ownership/coverage notes](25-work-notes.md) record starting architecture
triggers and scope. All four triggers are also YES after implementation: new
allocation/registration lifecycle, durable receipts/JSON, shared mutable metadata
and a new helper writer. Runtime run/attempt/QA owners remain unchanged; the
broader assessment must inspect all package files and affected guidance before
integration. The future evidence reviewer retains assessment/approval ownership;
no capture method assigns those outcomes.

## Required final-source checks

[Verification allocation](captures/verification-c0cae20c448046a885e8cc35aa6e28dc/allocation.json),
[source/instruction/environment identities](captures/verification-c0cae20c448046a885e8cc35aa6e28dc/source-and-instructions.json),
[driver](25-final-driver.log), [exact verification script](25-verify.py).
Command stdout/stderr, check-results.json and new CLI/JSON observations are written
inside this allocated folder. The full suite is in progress; no completion is
claimed before its actual result and static/installed/skill checks are recorded.
The source manifest's file hashes, not its parent HEAD alone, identify the tested
uncommitted implementation. A post-commit binding will compare those hashes to Git.

[First red](25-red-ticket.log), [first green/typecheck](25-green-ticket.log),
[protection red](25-red-protection.log), [protection green](25-green-protection.log),
[final focused cases](25-focused-final.log): 23 focused cases passed before the
full suite. The two actual protection regressions (allocation metadata alias and
an unrelated frozen subtree blocking all capture) were corrected before final
verification. These logs preserve actual failures and earlier source scope.

## Shared capture and guidance

[Shared EC1 artifact](../evidence-capture-workflow/EC1/evidence-review.json) is the
single authoritative shared capture artifact, linked by `shared_records` from
[ticket 25](evidence-review.json) and [ticket 26](../ticket-26/evidence-review.json).
Its guidance capture checks 37 actual relative paths/anchors and implementation,
testing and review routing, with zero failures. [Actual command/result](25-guidance-driver.log),
[script](25-guidance-check.py). This is shared guidance evidence for the capture
and subsequent cleanup slices; it supplies no review/deletion approval or EC1 QA.

## Original instructions and existing work

[Starting status](starting-status.txt), [tracked input patch](starting-worktree.patch)
and [input snapshots](instructions/) preserve the supplied uncommitted planning
bundle. Snapshots retain original content and original-path semantics; resolve
links against their original paths, not this snapshot directory. Approved inputs
are read for scope, not swept into the implementation commit. The preexisting
publication links to evidence-policy-approval.md are missing from the supplied
worktree; no human decision or replacement approval is invented. The current
explicit implementation request supplies task authorization. Existing M1 actual
acceptance and EC1 membership are verified from their authoritative records.

## Independent reviews

Pending required final-source checks and checkpoint commit: fresh separate High
Spec and High Standards, plus the trigger-required broader High Standards affected
workflow assessment. Original reports will be captured to separate producer paths
and linked here before reconciliation. No report is fabricated by fixture tests.

## Corrected final verification

The first verification allocation above is retained as an interrupted failed run:
4 failed / 243 passed, exit2. See the compute-environment diagnosis in work notes.
The unchanged-source final run is now
[capture verification-778bf1a0cac64d768f73b59424f9bdf3](captures/verification-778bf1a0cac64d768f73b59424f9bdf3/allocation.json),
with [source identities](captures/verification-778bf1a0cac64d768f73b59424f9bdf3/source-and-instructions.json),
[driver](25-final-executable-temp-driver.log) and
[actual script](25-verify-executable-temp.py). It uses executable shared TMPDIR,
standard isolated pinned-backend wheel building and captured installed allocation/
registration. Both runs remain separately identified. Final outcome is pending.

## Final node-local verification

Shared-TMPDIR run778bf1a0 was interrupted for measured filesystem overhead, with
no failure reported before interruption. The final unchanged-source run is
[capture verification-4b71b49c9cfa46b388bf30f16b1e4c2b](captures/verification-4b71b49c9cfa46b388bf30f16b1e4c2b/allocation.json),
[source/environment identities](captures/verification-4b71b49c9cfa46b388bf30f16b1e4c2b/source-and-instructions.json),
[driver](25-final-memory-temp-driver.log), running the retained
25-verify-executable-temp.py with /dev/shm/ticket25-verification-1EQrbx on
Forest203 x86_64. /dev/shm is executable and had57GiB free. Test concurrency and
BLAS/OpenMP threads remain one. Observations are copied directly to shared
capture storage and additionally archived losslessly without removing originals.

## Verified checkpoint for independent review

Implementation checkpoint: **3b0c1ab7ec41929d3febab44269f791e55897e70**; separate
requested ADAPT guidance commit ec1a1e5 (final reuse-first wording also in checkpoint).
[Exact-source binding](25-committed-source-binding.json) verifies all tested files
remain identical; committed product sources match Git, while supplied planning/
AGENTS inputs retain their explicit uncommitted-source provenance.

Final runtime: **586 passed in680.31s**, exit0. Strict mypy11files, Ruff lint,
format26files, whitespace, skill validation, isolated wheel/install, installed
capture/harness help and actual installed allocation/registration all exit0.
The installed module's SHA256 matches the tested implementation. Source-unchanged
check is0 with no changed file. Final helper registration returned0; the ticket
artifact records this capture as all passed. Original outputs and copied CLI/Git/
JSON observations are retained in the final allocation; observations.tar.gz is a
lossless additional archive, with no removal of originals.

Current ADAPT guidance's standalone [final validation](25-compute-guidance-validation-final.json)
also passes; [follow-up provenance](25-compute-guidance-update.md) records the exact
user request and earlier/current snapshots. No live Slurm execution is claimed.
Separate Spec, Standards and broader architecture assessments now assess this
checkpoint; their reports remain pending until each independent assignment returns.

## Original review and bounded repair1

Original independent reports at3b0c1ab are all preserved/registered: Spec01 one
blocker, Standards01 two, broader Architecture01 two; each zero optional. The
five distinct full keys in [append-only history](25-finding-history.md) consolidate
to two concrete defects. [Original payload digests](25-review-round1-digests.sha256),
[actual counterexamples](25-probe-execution-results.md), original report paths and
[corrected Spec navigation context](25-review-spec-01-envelope.md) retain provenance.
No original result is rewritten as clean.

Fresh Medium /root/repair25_1 produced the [bounded repair report](25-repair1-report.md).
[Focused allocation](25-repair1-allocation.json) holds exact per-stage source
snapshots and raw commands/results: empty-name red2fail/6pass, green10pass; retry
red1fail; complete current capture family26pass in6.03s; strict type/affected lint/
format/whitespace0. Product changed only consistent optional-name presence tests
and completion of the prior-original loop before matching-ID success. Three public
behavior cases were added. Capture owner/schema/locking and all four original
architecture triggers remain unchanged; runtime ownership is unaffected.

Fresh required full/static/installed checks now run on that repaired source through
retained Forest203 session10089 with executable node-local TMPDIR and one-thread
limits. [Driver](25-repair1-full-driver.log), PID4019509. Product edits are frozen.
All finding dispositions remain open pending exact-source fresh independent review.

## Current input navigation and repaired final verification

[Input refresh](25-instruction-refresh.md) records the concurrent workflow-spec
rename and live publication/navigation updates, with original and current snapshots
kept distinct. Ticket25 criteria/capture contracts are unchanged. The first repair
full driver failed before tests while reading the old filename; that original
preparation error is preserved. The corrected
[driver](25-repair1-current-inputs-driver.log) runs retained25-verify-repair1.py,
which changes only the input path, through the existing terminal and host.

Current repaired-source full check allocation:
[verification-71288fc1a1da4058830978bc454711dc](captures/verification-71288fc1a1da4058830978bc454711dc/allocation.json).
Its source/environment/check stdout/stderr and observation archive remain at this
unique path. The original586 pass remains evidence only for3b0c1ab, not this repair.
The [focused repair registration](25-repair1-registration-result.json) saved50
original source-state/report/output files; both red and green results survive.

## Current repaired checkpoint and verification recovery

Repair commit: **febd86321851e2acec994237f9d1a1adea824c55**. The original
whole-ticket baseline remains unchanged. Product hashes match the frozen repair.
The old terminal/process ended during formatting: reconnect to Forest203 found
neither original shell/driver PID nor any verification process. Its completed
**589 tests passed in 813.40s**, strict mypy and lint remain actual passing results.
The original empty format outputs are interrupted evidence, never a pass.

[Recovery adapter](25-resume-verification.py) checked every original source/input
hash, reused only those three recorded passes, then completed the remaining
checks in a [separate allocation](captures/verification-resume-44c46221b60444d4b2ff2512e4603e48/allocation.json).
[Actual results](captures/verification-resume-44c46221b60444d4b2ff2512e4603e48/check-results.json)
are all zero: format, whitespace, skill validation, isolated wheel/install,
installed help/allocation/registration, installed module hash and source-unchanged.
[Reuse provenance](captures/verification-resume-44c46221b60444d4b2ff2512e4603e48/reuse-provenance.json)
binds the original three passes; registration returned zero. No full suite replay.
[Driver](25-resume-driver.log),
[committed binding](25-repair1-committed-source-binding.json) distinguish committed
product files from supplied uncommitted governing inputs. Original and recovery
captures remain separate. New persistent Forest203 terminal: **43198**, x86_64,
one-thread limits, executable `/dev/shm/ticket25-resume-cC4Wm4`; no Slurm allocation.
Original registered reports and all five finding keys remain in the append-only
history pending fresh exact-source review. See [round2 context](25-review-round2-context.md).

## Current independent review outcome

Fresh whole-ticket [Spec02](captures/spec-02-5900732a47de41b589f24b1257f5be7b/report.md),
[Standards02](captures/standards-02-fb83db1963cc4831bb95ec2576576f03/report.md) and
[broader architecture Standards02](captures/architecture-02-4332dc4df4614538b4444cf6a932e3db/report.md)
each report zero new blockers/optional suggestions at exact commit `febd863`.
Requested fresh GPT-6.1 Sol High settings and <=250000 active-context target are
recorded separately from unavailable backend enforcement/measured telemetry.
The broader original records full inspection of all eleven package files and
affected guidance; routine axes retain their distinct scope and judgments.
[External digests](25-review-round2-digests.sha256) and
[registration](25-review-round2-registration.json) preserve originals.
All five distinct original full keys are independently verified fixed and
dispositioned in [append-only events T25-R2-F01–F05](25-finding-history.md).
No open finding, deferred blocker or missing report remains for this source.
See [routine assessment](../../reviews/ticket-25.md),
[triggered assessment](../../reviews/EC1-capture-architecture-01.md) and
[criterion completion record](25-completion.md).
Ticket26, the future full EC1 cumulative checkpoint and human acceptance are
separate pending work. No evidence deletion, runtime adoption or promotion occurred.

## Completion record validation

[Scoped bookkeeping validation](25-bookkeeping-validation.json) passed seven
unchanged criteria, completed status, exact original report hashes, unchanged
reviewed product, current review summaries and 66 record links/anchors. The
administrative status/comment changes are separate from assessed instruction
snapshots. Staged Markdown/Python whitespace checks pass. A blanket staged check
also diagnoses whitespace in preserved raw command transcripts and patch snapshots;
those original bytes are intentionally retained, with no normalization or relabeled
pass. Required final-product whitespace previously passed in the source-bound checks.
Only task-owned index additions are staged; supplied planning/archive edits stay
intact in the worktree. Large copied fixture directories remain locally retained,
with their registered lossless archives committed alongside original check records.
