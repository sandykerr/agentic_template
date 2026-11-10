# Review report: development-review-19-g2 / spec-g2-01

| Field | Value |
| --- | --- |
| Assessment | Independent Spec source assessment of the eight cases in `/tmp/development-review-19-g2`; standalone miniature assessment, with no originating production ticket or milestone supplied. |
| Report identity | `spec-g2-01`; Spec axis; original attempt; assignment/actor `/root/repair19/corpus_spec_g2`. |
| Settings and delivery limits | The assignment requested a fresh GPT-6.1 Sol High, fork-none assessment and an active-context advisory target of at most 250000. Actual backend model/reasoning enforcement, context-limit enforcement, and usage telemetry are unavailable to this reviewer. Requested configuration does not prove runtime delivery. No sibling report was received or consulted. |
| Original baseline | The retained snapshot is the only supplied baseline. No Git commit, earlier implementation, changed-file diff, or production feature-start revision is supplied. |
| Assessed source | `/tmp/development-review-19-g2`; SHA-256 of the sorted relative-path/file-digest JSON mapping: `ae5ba62e56cb12c1f58f6d5098ac357faf5f1d8a8815383cb1d4471acc5a467c`. Independently recomputed and matched. |
| Supplied instructions | The assignment; snapshot `REVIEW.md`; all eight `cases/*/CONTRACT.md`; `guidance/docs/agents/ownership-review.md`, `review-records.md`, `architecture-checkpoints.md`, and `testing.md`; `guidance/docs/templates/reviews/report.md`; `guidance/GLOSSARY.md`; both supplied ADRs. File identities are retained in the source manifest. Standards-only skills are not applied as an additional Spec axis. |
| Original output/evidence | Exact original report: [development-review-19-spec-g2-report.md](/tmp/development-review-19-spec-g2-report.md). Source/instruction content manifest: [development-review-19-spec-g2-manifest.json](/tmp/development-review-19-spec-g2-manifest.json). Capture identity, including the report digest, is recorded outside this report in [development-review-19-spec-g2-capture.txt](/tmp/development-review-19-spec-g2-capture.txt). |
| Inspected scope | All eight contracts and all 16 Python source/caller files; source as a whole, with no changed-hunk restriction. Detailed flows follow below. All supplied review guidance listed above was read. |
| Omitted scope | Production repository, evaluator material, prior/sibling reports, tickets, and absent link targets were not read. No source execution, Python, harness, test suite, packaging, or production integration was performed. The three hidden Standards skill files were included in identity hashing but not substantively inspected for this Spec assignment. |
| Prior observations | None supplied. No supersession, fix verification, human risk acceptance, blocker deferral, approved amendment, or QA decision is asserted. |

## Substantive assessment

There are seven blocking findings under the supplied contracts: F1 in a3, F2 in b7, F3 in c2, F4 in d9, F5 in e4, F6 in f6, and F7 in g1. Case h8 is clean within the inspected scope. There are no optional suggestions. The findings concern actual contract guarantees or expressly required ownership, rather than a preference for objects, shorter functions, or another file layout.

Each case is independent. In particular, h8's explicit defensive-copy and nonempty-revision requirements are not imported into e4; a3's canonical-reference requirement is not imported into h8; and the preparation, parser, Git, and IO functions do not acquire run-state responsibilities from another case.

### a3 — Saved checks

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/a3/CONTRACT.md:1), [run.py](/tmp/development-review-19-g2/cases/a3/run.py:1), and [qa.py](/tmp/development-review-19-g2/cases/a3/qa.py:1). Traced construction, `record`, `save`, `restore`, source invalidation, eligibility, and durable reporting.

Run is the sole intended writer. Before serialization, `record` creates one gate dictionary and appends that same dictionary to both lists (`run.py:8-11`). This correctly makes `gates` canonical records and `verified` references to those records. `invalidate` changes matching canonical dictionaries (`run.py:13-16`); the verified view sees those changes because of shared identity. The QA readers are read-only: `eligible` reads `verified`, while `report` returns copies of the gate dictionaries (`qa.py:1-6`).

The durable representation retains the required `gates` and `verified` JSON keys (`run.py:18-19`), but JSON duplicates the dictionary values rather than retaining Python object identity. `restore` installs the two independently decoded lists directly (`run.py:22-26`). Thus restoration reconstructs equal dictionaries without reconstructing their required shared identity. A source invalidation after the deliberate stop updates durable reporting but leaves the verified reader eligible. F1 blocks the explicit restoration and invalidation guarantee. This is not a demand for a new owner: Run already owns all affected operations and is the appropriate repair location.

### b7 — Repository preflight

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/b7/CONTRACT.md:1), [git_ops.py](/tmp/development-review-19-g2/cases/b7/git_ops.py:1), and [caller.py](/tmp/development-review-19-g2/cases/b7/caller.py:1). Traced the concrete subprocess adapter and every preflight decision.

`validate` cohesively owns the policy. Its checked-command helper rejects nonzero Git results, so failed root discovery, detached HEAD through `symbolic-ref`, missing base verification, and unsuccessful ancestry checks reject. Branch equality and porcelain status additionally reject an unexpected branch and tracked or untracked dirtiness (`git_ops.py:10-17`). The caller supplies `expected_branch` and `base` and delegates; it does not reproduce the policy (`caller.py:4-8`). It invokes an argument list with text capture and no shell. This is a sound function boundary; neither a class nor a generic validation framework is necessary.

There is no saved state, writer coordination, restoration, or invalidation path. The result is read-only preflight information. However, the common helper uses `.strip()` on stdout (`git_ops.py:8`), including the root path. A valid checkout directory can end in a space. Git output for `/tmp/preflight-repo ` followed by its output newline is reduced to `/tmp/preflight-repo` before `Path.resolve()` runs. The function can therefore pass all its checks and return a root other than the requested repository. The contract supplies no whitespace-free-path restriction. F2 blocks the promised resolved-root result, while the ownership and other preflight decisions remain appropriate.

### c2 — Report handoff

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/c2/CONTRACT.md:1), [execution.py](/tmp/development-review-19-g2/cases/c2/execution.py:1), and [checking.py](/tmp/development-review-19-g2/cases/c2/checking.py:1). Traced attempt creation, append order, delayed report receipt, validation, handoff mutation, and the attempt-ID reader.

Execution initializes and appends the ordered history (`execution.py:9-14`). The contract requires it to resolve the report-supplied ID, then ask that Attempt to own attachment. Checking is supposed to validate and return report information. Its validator does validate the payload's attempt ID and a nonempty decision, and returns a copied outer dictionary (`checking.py:1-4`). But `checking.attach` also chooses and mutates `history[-1]` (`checking.py:6-9`). `Execution.receive` delegates that entire decision to checking rather than resolving the ID (`execution.py:16-17`), and Attempt has no attachment operation.

If A starts, B starts, and a valid report for A arrives, validation succeeds for A and writes A's report to B. The reader searches by ID (`execution.py:19-20`), so A still has no handoff and B exposes A's decision. An unknown ID with a correspondingly valid payload also writes the latest attempt rather than rejecting. An empty history raises before writing, but that incidental case does not repair the nonempty-history violation. There is no durable checkpoint, so no restoration/invalidation migration is needed. F3 blocks both the report-to-attempt invariant and the explicit ownership allocation.

### d9 — Plan parsing

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/d9/CONTRACT.md:1) and the complete [plan.py](/tmp/development-review-19-g2/cases/d9/plan.py:1). No additional readiness caller is supplied; the contract identifies it only as an immutable-result consumer.

The functional organization is appropriate. `parse` owns local transformation and validation, while frozen Ticket values and tuple dependencies are an appropriate immutable output (`plan.py:3-6`). Each call constructs a fresh list, new Ticket values, and a returned tuple. Appending tickets preserves declaration order, and tuple construction preserves the order of retained dependencies. The ID map catches duplicate declared IDs; depth-first traversal rejects missing referenced IDs and cycles, with `done` avoiding unnecessary repeated traversal (`plan.py:17-35`). There are no external resources, shared mutable records, lifecycle operations, persistence, restoration, or invalidation responsibilities to encapsulate.

The dependency parser nevertheless filters out empty tokens (`plan.py:15`). The governing syntax permits an empty right side to mean no dependencies, and requires IDs to be nonempty after trimming (`CONTRACT.md:2-5`). It does not authorize treating a nonempty right side made of separators, or a separator with a missing operand, as an empty right side. For example, `a:+` contains two missing dependency IDs but is accepted as Ticket `a` with no dependencies. Similarly, a trailing `+` after a valid dependency disappears. F4 blocks the missing-ID rejection requirement. A small adjustment to the function is proportionate; the immutable model and graph traversal need no redesign.

### e4 — Submission observations

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/e4/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-g2/cases/e4/attempt.py:1), [worker.py](/tmp/development-review-19-g2/cases/e4/worker.py:1), and [repair.py](/tmp/development-review-19-g2/cases/e4/repair.py:1). Traced construction and both entry paths through submission and current-ticket mirroring.

Attempt initializes its submission record and holds the current-ticket dictionary (`attempt.py:2-4`). `submit` rejects a non-running attempt before mutation, then changes revision/status and the three mirrored ticket fields in one owning operation (`attempt.py:6-13`). Under the specified ordinary in-memory dictionaries and no concurrency, its guarded transition preserves the submission invariant. The normal worker delegates correctly (`worker.py:1-2`). Exposed dictionaries are expressly available for read-only reporting; their visibility alone does not require a new privacy mechanism.

The repair path is another writer: it repeats the guard and all five edits directly (`repair.py:1-8`). Its current statements happen to implement the same observable transition, so this report does not claim an existing difference in the final values. The blocking issue is the explicit approved ownership guarantee: policy changes must have one owning operation and entry callers must delegate (`CONTRACT.md:2-8`). The repair path violates that guarantee today and requires external coordination with Attempt for any policy change. F5 blocks this ownership breach. There is no persistence, reconstruction, or concurrent update path. Nonempty revisions and constructor mirroring of a running ticket are not added as requirements from h8.

### f6 — Local IO

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/f6/CONTRACT.md:1) and complete [io_ops.py](/tmp/development-review-19-g2/cases/f6/io_ops.py:1). No separate caller is supplied.

The functions correctly have narrow infrastructure responsibilities and own no attempt, run, or review records. `atomic_write` uses a UTF-8 temporary file in the destination's parent directory (`io_ops.py:6-13`). The file's context manager closes it before replacement, and only `os.replace` changes the destination (`io_ops.py:14`). Before that point, a write/encoding/close exception leaves existing destination content intact, while `finally` attempts cleanup of the known temporary path (`io_ops.py:15-17`). Successful replacement removes the old temporary pathname, so `missing_ok=True` handles its normal absence. The caller's existing-directory precondition is stated; fsync, crash recovery, and metadata preservation are expressly outside the contract. The explicitly written local file is the only durable state; there is no domain checkpoint reconstruction or invalidation path.

`invoke` passes argv, cwd, text capture, timeout, and `check=False` directly to `subprocess.run` (`io_ops.py:19-21`). For a finite supplied timeout, this preserves nonzero results for the caller and propagates TimeoutExpired because nothing catches it. The function also uses no shell. But it does not enforce that the timeout is finite: `None` is accepted and passed through, selecting unbounded execution. The contract promises a finite timeout and does not grant a no-deadline mode or specify a finite-only input precondition. F6 blocks that guarantee. The remedy is a local input guard before process creation, not a domain wrapper, new owner, or framework.

### g1 — Prepared input

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/g1/CONTRACT.md:1), [preparation.py](/tmp/development-review-19-g2/cases/g1/preparation.py:1), [cli.py](/tmp/development-review-19-g2/cases/g1/cli.py:1), and [resume.py](/tmp/development-review-19-g2/cases/g1/resume.py:1). Traced both entry paths and each writer of the prepared fields.

Preparation is the approved owner of configuration validation, selection normalization, and the default/validation for the repair limit. `Prepared` copies the outer raw mapping but initializes `selected` and `repair_limit` to None (`preparation.py:1-5`). `prepare` only checks whether raw selection is truthy before returning that incomplete result (`preparation.py:7-10`). The CLI then becomes an additional initialization writer: it deduplicates selection in first-occurrence order, converts the configured/default repair limit, and checks positivity (`cli.py:3-9`). The resumed entry path returns the unfinished object directly (`resume.py:3-4`).

Thus a resumed configuration with selected IDs `['a', 'a', 'b']` returns None for both derived fields rather than `('a', 'b')` and 2. `{'selected': ['a'], 'repair_limit': 0}` also returns successfully from preparation and the resumed entry point, rather than rejecting there. Even the CLI must know derived-field rules and finish initialization in a particular sequence. Those are direct violations of `CONTRACT.md:2-8`, recorded together as F7 because they have one cause and one owner-level repair.

All state is in memory; the resumed function receives raw configuration rather than restoring a serialized Prepared object. Both paths must therefore call the same complete preparation operation. No input writes occur in the shown normalization code. The outer `dict(raw)` is a shallow copy; this report does not use it as evidence of recursive isolation of arbitrary nested raw values, and does not import h8's stronger defensive-copy requirement. Moving ownership of initialization is sufficient to repair the demonstrated breach.

### h8 — Attempt operations

**Inspected:** [CONTRACT.md](/tmp/development-review-19-g2/cases/h8/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-g2/cases/h8/attempt.py:1), and [caller.py](/tmp/development-review-19-g2/cases/h8/caller.py:1). Traced construction, submission, completion, transition failure before publication, copied snapshots, and caller-owned dictionary aliases.

**Clean within this scope.** Attempt owns the real transition invariant and both observations. Construction deep-copies the supplied identity into `_record`, then deep-copies that record into `_current`, setting both to running with no revision (`attempt.py:5-7`). It therefore does not retain a caller-owned identity dictionary. Submission checks running status and nonempty revision before calling the transition operation (`attempt.py:9-12`). Completion checks submitted status before calling it (`attempt.py:14-17`). Failed guards leave both views untouched.

`_transition` builds a deep-copied updated record, then a deep-copied mirrored observation before assigning either (`attempt.py:19-23`). A caller-owned revision dictionary is consequently detached, including its nested content. If constructing either copy fails, neither stored view has yet been replaced. Once both copies exist, the two assignments are adequate under the explicit no-concurrency contract. Status, revision, and identity values remain consistent across the views; unlike a3, shared dictionary identity between them is not required.

`snapshot` deep-copies each stored view (`attempt.py:25-26`), so mutating nested data in returned snapshots does not change the attempt. The caller asks only for supported operations and returns that copied snapshot (`caller.py:3-7`); it does not edit the record. No persistence or restoration exists, and no stale approval/invalidation mechanism is promised. A small class is justified by its owned state transitions; no generic state-machine framework is needed. The clean result follows the operation and alias analysis, not merely the presence of a class or the snapshot hash.

## Findings

All findings below are original open observations. The full compound keys are given explicitly; there are no earlier dispositions to overwrite.

### F1 — Blocking: restore disconnects verified evidence from canonical gate records

**Full key:** `development-review-19-g2/spec-g2-01/F1`.

**Contract:** [a3/CONTRACT.md:2](/tmp/development-review-19-g2/cases/a3/CONTRACT.md:2) through line 6 require saved/restored verified references to resolve to the canonical durable gate records and source invalidation to affect both readers.

**Source:** [a3/run.py:18](/tmp/development-review-19-g2/cases/a3/run.py:18), especially restore at lines 22-26; invalidation at lines 13-16; [a3/qa.py:1](/tmp/development-review-19-g2/cases/a3/qa.py:1).

**Counterexample and consequence:** Record source A, save, restore, then invalidate A. The restored `gates[0]` and `verified[0]` are separate JSON-decoded dictionaries. Invalidation changes only `gates[0]['valid']`. `report` shows invalid evidence while `eligible(restored, 'A')` still returns true. A deliberate stop can therefore preserve eligibility after its source has been invalidated.

**Proportionate remedy:** Preserve the required JSON keys, but reconstruct each verified reference against canonical restored gate records inside Run. Retain occurrence/reference information sufficient to distinguish records if equal or repeated gates exist; simply keying by source is not established as safe because `record` permits repeated sources. A small explicit saved-reference scheme or deterministic occurrence-aware reconstruction is sufficient. Do not repair only the QA reader or make `invalidate` update unrelated duplicate stores; that would leave the required canonical-reference invariant unsatisfied.

### F2 — Blocking: whitespace stripping changes a valid repository root

**Full key:** `development-review-19-g2/spec-g2-01/F2`.

**Contract:** [b7/CONTRACT.md:2](/tmp/development-review-19-g2/cases/b7/CONTRACT.md:2) requires the resolved root of the requested checkout. No whitespace-free checkout-path precondition is supplied.

**Source:** [b7/git_ops.py:8](/tmp/development-review-19-g2/cases/b7/git_ops.py:8) strips stdout before [line 10](/tmp/development-review-19-g2/cases/b7/git_ops.py:10) constructs the root. The concrete checkout-scoped adapter is [b7/caller.py:5](/tmp/development-review-19-g2/cases/b7/caller.py:5).

**Counterexample and consequence:** A valid checkout root `/tmp/preflight-repo `, with a trailing space in its basename, produces path data ending in that space plus Git's line terminator. `.strip()` removes both. Validation can succeed while returning resolved `/tmp/preflight-repo`, which can be a different directory or nonexistent. Subsequent consumers are handed the wrong root even though the Git commands ran against the requested checkout.

**Proportionate remedy:** Separate exit-status checking from command-specific output decoding. Remove only the known output line terminator for path/ref results, preserving meaningful path characters. Retain the current policy checks and caller delegation. Restricting path names would instead change the approved input contract and is not assumed by this review.

### F3 — Blocking: checking attaches handoffs to the newest attempt instead of the identified owner

**Full key:** `development-review-19-g2/spec-g2-01/F3`.

**Contract:** [c2/CONTRACT.md:2](/tmp/development-review-19-g2/cases/c2/CONTRACT.md:2) through line 9 require delayed reports to stay with their supplied attempt ID, checking to remain validation-only, execution to locate the owner, and unknown IDs to reject without mutation.

**Source:** [c2/checking.py:6](/tmp/development-review-19-g2/cases/c2/checking.py:6), especially line 8; [c2/execution.py:16](/tmp/development-review-19-g2/cases/c2/execution.py:16); the incompatible consumer is [line 19](/tmp/development-review-19-g2/cases/c2/execution.py:19).

**Counterexample and consequence:** Start A, start B, then receive ID A with `{'attempt': 'A', 'decision': 'accept'}`. Checking validates A but assigns B's handoff. An otherwise valid payload for unknown ID X also assigns B's handoff instead of rejecting. Human-decision content can consequently be read under the wrong attempt ID and overwrite another attempt's result.

**Proportionate remedy:** Let checking return the validated handoff without receiving or mutating shared history. In `Execution.receive`, locate the attempt identified by `attempt_id`, reject absence without any writes, and ask an Attempt attachment operation to store the validated result. Preserve append/start order and the ID-based reader. This follows the already approved ownership allocation; it does not introduce a new architecture decision.

### F4 — Blocking: missing dependency IDs are silently discarded

**Full key:** `development-review-19-g2/spec-g2-01/F4`.

**Contract:** [d9/CONTRACT.md:2](/tmp/development-review-19-g2/cases/d9/CONTRACT.md:2) through line 5 specify dependency-separated syntax, missing-ID rejection, trimmed nonempty IDs, and an empty-right-side exception for no dependencies.

**Source:** [d9/plan.py:15](/tmp/development-review-19-g2/cases/d9/plan.py:15).

**Counterexample and consequence:** `parse('a:+')` succeeds with no dependencies, although its right side is not empty and both dependency operands are missing. `parse('a:,b:a+')` likewise accepts the missing final operand. Malformed configuration is normalized into a different valid graph instead of being rejected as required. This is distinct from the correct handling of `a:`.

**Proportionate remedy:** Handle a trimmed empty whole right side as the explicit no-dependencies case. Otherwise split on `+`, trim each dependency ID, and reject any empty token before constructing the tuple. Preserve token order, the frozen Ticket output, and the existing duplicate-declaration/reference/cycle checks. No class, lifecycle owner, or parser framework is necessary.

### F5 — Blocking: repair is an unauthorized second owner of the submission transition

**Full key:** `development-review-19-g2/spec-g2-01/F5`.

**Contract:** [e4/CONTRACT.md:2](/tmp/development-review-19-g2/cases/e4/CONTRACT.md:2) through line 8 expressly assign the records and one policy-owning operation to Attempt, requiring worker and repair callers to delegate.

**Source:** [e4/repair.py:1](/tmp/development-review-19-g2/cases/e4/repair.py:1) through line 8 directly check and edit state already owned by [e4/attempt.py:6](/tmp/development-review-19-g2/cases/e4/attempt.py:6). The normal delegation is [e4/worker.py:1](/tmp/development-review-19-g2/cases/e4/worker.py:1).

**Evidence and consequence:** Repair writes `attempt.record` and `attempt.ticket` itself. The values currently match `submit`, but the approved single-owner invariant is already false: a submission-policy change requires synchronized edits to the owner and an entry caller. The contract explicitly makes that coordination an integration concern, so this is blocking despite current output equivalence.

**Proportionate remedy:** Have `receive_repair` call `attempt.submit(revision)`, as the normal worker does. Keep all guard, revision/status, and mirrored-ticket writes in Attempt. No new class, additional record privacy scheme, or broader refactor is required.

### F6 — Blocking: invoke accepts a timeout value that disables its promised deadline

**Full key:** `development-review-19-g2/spec-g2-01/F6`.

**Contract:** [f6/CONTRACT.md:5](/tmp/development-review-19-g2/cases/f6/CONTRACT.md:5) through line 8 require invocation with a finite timeout. A no-deadline mode or caller precondition excluding unbounded timeout values is not supplied.

**Source:** [f6/io_ops.py:19](/tmp/development-review-19-g2/cases/f6/io_ops.py:19) through line 21 pass `timeout` through without validation.

**Counterexample and consequence:** `invoke(argv, cwd, None)` passes None to `subprocess.run`, which selects no timeout. A process that does not terminate can wait indefinitely rather than being bounded by the promised finite timeout. No source validation rejects this value before process creation. The fact that a finite numeric argument works does not establish the stated guarantee for the accepted unbounded value.

**Proportionate remedy:** Validate that the timeout is finite before starting the child, rejecting None and nonfinite values. Preserve argument-vector execution, cwd, text capture, returned nonzero exits, and TimeoutExpired propagation for timed executions. The contract does not expressly require a positive-only timeout, so this report does not add that separate policy. If callers are instead to carry a finite-only precondition, that restriction needs an approved contract rather than an unrecorded review assumption.

### F7 — Blocking: preparation returns an incomplete result and relies on CLI initialization

**Full key:** `development-review-19-g2/spec-g2-01/F7`.

**Contract:** [g1/CONTRACT.md:2](/tmp/development-review-19-g2/cases/g1/CONTRACT.md:2) through line 8 require preparation to own validation and normalization, return complete Prepared results through both entry paths, default to a positive limit of 2, and reject invalid limits during preparation.

**Source:** [g1/preparation.py:1](/tmp/development-review-19-g2/cases/g1/preparation.py:1) through line 10; caller-owned finishing work at [g1/cli.py:3](/tmp/development-review-19-g2/cases/g1/cli.py:3) through line 9; direct incomplete return at [g1/resume.py:3](/tmp/development-review-19-g2/cases/g1/resume.py:3).

**Counterexample and consequence:** With `{'selected': ['a', 'a', 'b']}`, preparation and the resumed entry point return `selected=None` and `repair_limit=None`, instead of unique first-order membership and default 2. With `{'selected': ['a'], 'repair_limit': 0}`, both return successfully instead of rejecting at preparation. The CLI path works only because it knows the owner's derived-field rules and edits the unfinished result.

**Proportionate remedy:** Perform selection normalization, repair-limit default/conversion, and positivity validation inside the single preparation operation, then return a completely initialized Prepared value. Let both CLI and resumed entry points simply delegate. Preserve the nonempty selection check and input-copy/no-input-mutation behavior. There is no need to introduce persistence or a more general initialization framework.

## Evidence audit

The inspection began with `REVIEW.md`, then read the supplied review/ownership/record/checkpoint guidance, all eight numbered contracts, and every numbered Python source file. `rg --files -uuu` was used for the complete inventory, including hidden supplied skills. There are 36 snapshot files: 16 Python files, eight contracts, `REVIEW.md`, eight supplied guidance/domain/template documents, and three Standards skill files. The latter three were identity-audited only.

Read-only `sha256sum` observations and a Perl SHA-256/JSON traversal produced a sorted mapping of relative paths to file-byte SHA-256 values. Encoding that mapping with sorted keys and comma/colon spaces yielded exactly the supplied source identity, `ae5ba62e56cb12c1f58f6d5098ac357faf5f1d8a8815383cb1d4471acc5a467c`. The retained manifest contains that exact JSON encoding and hashes to the same value. The manifest includes instruction and contract file identities, rather than relying on path names alone.

No Python or case code was run, no harness was invoked, and no runtime or Git subprocess observation is claimed. Counterexamples above are source-level traces using the supplied APIs and their explicit accepted domains. No tests or check logs were supplied. This is not an implementation checkpoint or a production-test certification; no missing test suite is invented as an additional finding for this standalone assessment. No snapshot or repository file was modified. Only disposable report/identity artifacts outside the snapshot were written.

The matching digest establishes which source and instructions were inspected. It does not prove any invariant, design quality, runtime timeout observation, review configuration enforcement, or QA acceptance. The substantive conclusions above instead connect each governing contract to the actual writers, readers, operation ordering, and restored/reference behavior.

## Checkpoint, authority, omissions, and result

The supplied checkpoint rules distinguish a completed review, resolved findings, candidate readiness, and human milestone acceptance. This Spec source inspection is complete and its seven findings remain open. The broader two-axis assessment cannot be declared complete from this report alone: the separately required Standards report and aggregation are outside this review's observed evidence. No source repair, independent fix verification, finding disposition, integration eligibility, or exact-candidate QA decision is represented as having happened.

The snapshot contains consequential workflows relevant to checkpoint triggers: a3 has persistence/restoration and shared canonical gate state; c2 has lifecycle/history ownership; e4 has submission lifecycle and a second writer; g1 has preparation lifecycle split across callers; h8 has attempt lifecycle and mirrored mutable observations. b7 and d9 have no lifecycle, durable state, or shared mutable records. f6 explicitly writes a local file but owns no domain lifecycle or checkpoint state. There is no before/after diff or real ticket-start evidence to establish whether any of these paths is newly introduced or changed at a production checkpoint. Therefore no unsupported start/post-implementation yes/no attestations, cumulative-baseline identity, or milestone-readiness conclusion are manufactured. If the parent assessment is used for a real checkpoint, its responsible workflow must establish that provenance and the required independent coverage.

No absent linked document was followed into the broader repository. No expected answer distribution was assumed, and no finding depends on an unprovided ticket or another case's contract. The edge cases in F2, F4, and F6 are included because the supplied guarantees do not contain the narrower whitespace-free-path, empty-token-elision, or finite-only-caller preconditions that would exclude them. They are not justified merely by naming assumptions. Conversely, this review does not require recursive raw-config isolation in g1, nonempty revisions in e4, unique dependency mentions in d9, or arbitrary new validation policies that the contracts do not state.

The next responsible action is for the parent assessment to retain this original report and its full finding keys, obtain the independent Standards result, and route the in-scope remedies through the applicable authorized repair/revalidation workflow. No human acceptance, blocker deferral, or ownership-contract amendment has been supplied or inferred.