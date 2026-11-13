# Source assessment: review-development-19-c5 / spec-c5-01

| Field | Value |
| --- | --- |
| Assessment | `review-development-19-c5`, independent Spec assessment of eight miniature cases; no external work item supplied. |
| Report identity | `spec-c5-01`; Spec axis; first report in this assignment; actor `/root/repair19_branch/corpus_spec_c5`. |
| Assignment and actual settings | The assignment specifies a fresh, fork-none GPT-6.1 Sol High reviewer and an active-context advisory target of at most 250,000 tokens. These are supplied configuration claims. Backend/model-delivery evidence, enforced reasoning/context settings, measured context use and enforcement telemetry are unavailable. Configuration does not establish runtime delivery or backend enforcement. |
| Original baseline | No earlier commit, changed-hunk baseline or repair history was supplied. This is a whole-source assessment of the fixed supplied snapshot, not a comparison against an inferred historical baseline. |
| Assessed source | `/tmp/development-review-19-c5`; aggregate SHA-256 `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`, verified over every regular file, including hidden guidance files. |
| Supplied instructions | Assignment; `REVIEW.md`; all eight `cases/*/CONTRACT.md`; supplied ownership, review-record, architecture-checkpoint and report-envelope guidance; supplied glossary, ADRs and testing policy. Their file identities are included in the retained snapshot manifest. Standards-only skill files were included in the identity audit; this report does not substitute for their separate Standards assessment. |
| Original output and evidence | Exact original report: `/tmp/development-review-19-spec-c5-report.md`. File-digest mapping: `/tmp/development-review-19-spec-c5-manifest.json`. Report digest is recorded separately at `/tmp/development-review-19-spec-c5-report.sha256`, avoiding a self-referential report hash. |
| Inspected scope | All eight case contracts and all 16 Python source/caller files in those cases, including unchanged collaborators and every supplied writer/reader/restore path. Details appear below. |
| Omitted scope | Broader repository, evaluator material, sibling/prior reports, tickets, external implementations and links whose targets are absent from this snapshot. No runtime harness, Python execution, production tests, integration or QA execution. These omissions follow the assignment and snapshot boundary. |
| Prior observations and decisions | None supplied. No prior finding is claimed fixed, superseded, accepted or deferred. No human risk or QA decision is inferred. |

The assessment is complete for the supplied Spec scope. There are four blocking findings, affecting a3, c2, e4 and g1. Cases b7, d9, f6 and h8 have no Spec finding within the inspected scope. There are no optional suggestions. The matching snapshot identity supports provenance; the conclusions below come from the actual contracts and call/data flow.

## Substantive assessment

### a3 — Saved checks

Inspected `cases/a3/CONTRACT.md`, `cases/a3/run.py` and `cases/a3/qa.py`. The contract requires Run to own the durable gates and verified references, including restoration of the canonical reference relationship and later invalidation semantics (`CONTRACT.md:2–7`).

`Run.__init__` initializes both lists (`run.py:4–6`). `record` creates one gate dictionary and appends that same object to both lists (`run.py:8–11`). Before serialization, this correctly makes `invalidate`'s edit through `gates` visible through `verified` (`run.py:13–16`). `qa.report` reads the durable list into dictionary copies, and `qa.eligible` reads the verified list (`qa.py:1–6`). Both supplied consumers are read-only. The only supplied record writer is Run; the problem is its reconstruction operation, not an unauthorized consumer writer.

`save` writes both required JSON keys (`run.py:18–19`), but JSON represents values rather than shared dictionary identity. `restore` separately assigns the decoded `gates` and `verified` lists without reconciling their records (`run.py:22–27`). The restored lists therefore contain separate gate dictionaries. Retaining equal field values at restoration time does not retain the promised invalidation behavior.

#### F1 — Blocking: restore loses canonical gate identity and leaves QA evidence valid

Full key: `review-development-19-c5/spec-c5-01/F1`.

Locations: [restore assignments](/tmp/development-review-19-c5/cases/a3/run.py:25), [invalidation writer](/tmp/development-review-19-c5/cases/a3/run.py:13), [QA reader](/tmp/development-review-19-c5/cases/a3/qa.py:1), governed by [the canonical-reference and invalidation guarantee](/tmp/development-review-19-c5/cases/a3/CONTRACT.md:3).

A concrete supplied-domain sequence is: create a Run, `record("A")`, save it, restore it, then `invalidate("A")` on the restored Run. The gate in `run.gates` becomes invalid. Its separately decoded counterpart in `run.verified` retains `valid=True`, so `qa.eligible(run, "A")` remains true while `qa.report(run)` reports an invalid gate. This is precisely the post-stop invalidation sequence the contract permits; no concurrency or consumer mutation is needed.

Run's restoration operation must reconnect the verified view to the canonical gate records according to the saved representation, retaining the required JSON keys and verified membership/order. A representation-compatible canonicalization is sufficient; an unrelated persistence framework or new owner is unnecessary. Merely invalidating two independent lists would not fulfill the explicit same-canonical-record requirement. Revalidation should cover the save/restore/invalidate/QA flow and shared-record semantics, not just equality immediately after decoding.

No other caller or persistence path is supplied. The finding is open; no source repair or independent repair verification was performed.

### b7 — Repository preflight

Inspected `cases/b7/CONTRACT.md`, `cases/b7/git_ops.py` and `cases/b7/caller.py`. No Spec finding.

The owner is the `validate` function, rather than a mutable object: it owns the sequence of read-only repository decisions (`git_ops.py:3–21`). The caller supplies checkout/process mechanics and the two approved policy inputs, `expected_branch` and `base` (`caller.py:5–19`). It does not duplicate branch, cleanliness or ancestry decisions. The environment-discovery failure check is a process prerequisite, not a second implementation of those policies.

The nested `checked` operation rejects every nonzero injected Git result before consuming its output (`git_ops.py:4–8`). Consequently, detached HEAD is rejected when `symbolic-ref HEAD` fails, and even a successful non-local-branch reference is rejected explicitly (`git_ops.py:11–13`). The local branch name is compared exactly with the requested branch (`git_ops.py:14–16`). `status --porcelain --untracked-files=all` makes ordinary tracked changes and untracked files reject (`git_ops.py:17–18`). The base must resolve as a commit and then pass `merge-base --is-ancestor base HEAD` (`git_ops.py:19–20`); absence and non-ancestry both result in rejection. The successful return is the resolved root and checked requested branch (`git_ops.py:10,21`).

The actual injected callable uses an argument list, the requested checkout through `-C`, captured output and no shell; it converts captured bytes to text before returning the CompletedProcess-like result (`caller.py:13–18`). It removes Git's listed local environment variables from a copied environment and disables optional locks (`caller.py:6–15`), supporting the requested-checkout and read-only boundaries. No mutation command appears in either file.

There is no saved state, shared domain record, restore or invalidation path. Temporary local values remain inside one cohesive validation operation. Changing a preflight policy would affect `validate`; the caller would continue supplying the same policy values and process adapter. The contract expressly permits functions and reduced ValueError details, so lack of a class or richer error hierarchy is not a defect.

This conclusion assumes the injected callable obeys its explicit contract; the supplied caller supports that assumption. It does not claim observations against a real Git repository or additional policies such as remote synchronization or ignored-file rejection, which are not promised here.

### c2 — Report handoff

Inspected `cases/c2/CONTRACT.md`, `cases/c2/checking.py` and `cases/c2/execution.py`. The contract separates validation from ownership: checking validates and returns report information; execution identifies the attempt; that attempt owns attachment (`CONTRACT.md:2–9`). Report completion may occur after a subsequent attempt starts, so the requested ID is essential routing information.

`Execution.start` appends Attempt records, preserving start order (`execution.py:10–14`). `Execution.receive` forwards the report's ID but delegates history mutation to checking (`execution.py:16–17`). `validate_handoff` correctly checks that the payload names the requested ID and has a decision, then returns a dictionary copy (`checking.py:1–4`). However, `checking.attach` ignores that ID for ownership selection and writes the most recently appended attempt (`checking.py:6–9`). `Execution.decision` reads by ID (`execution.py:19–20`), so it exposes the mismatch rather than correcting it. Attempt has no attachment operation at present (`execution.py:4–7`).

#### F2 — Blocking: handoff attachment targets the latest attempt, including for unknown IDs

Full key: `review-development-19-c5/spec-c5-01/F2`.

Locations: [history mutation in checking](/tmp/development-review-19-c5/cases/c2/checking.py:6), [execution delegation](/tmp/development-review-19-c5/cases/c2/execution.py:16), [attempt owner definition](/tmp/development-review-19-c5/cases/c2/execution.py:4), governed by [ID-directed ownership and unknown-ID rejection](/tmp/development-review-19-c5/cases/c2/CONTRACT.md:2).

Start attempt A, then B, then receive `("A", {"attempt": "A", "decision": "accept"})`. Payload validation succeeds, but `history[-1]` is B. B receives A's handoff, A remains without it, and ID-based consumers report the wrong historical ownership. Start-order preservation itself is correct; selecting the last element is the error.

Likewise, after any attempt exists, receiving `("unknown", {"attempt": "unknown", "decision": "accept"})` passes payload validation and changes the latest real attempt instead of rejecting without mutation. With an empty history, attachment fails on list indexing rather than performing an owner lookup. These cases need no concurrent execution: delayed report completion is expressly supported.

Keep checking responsible for validating and returning the handoff. Have Execution resolve the requested ID without changing history order, reject an absent owner before any assignment, and ask the identified Attempt to attach the validated handoff through its owning operation. This is a small routing/ownership repair under the existing approved contract, not permission to redefine which attempt owns delayed work. Revalidation should distinguish delayed A-after-B attachment and unknown-ID rejection with every existing handoff unchanged.

The only supplied readers/writers are those described above. This state is in-memory, with no checkpoint, restore or invalidation path. The finding is open; no repair was performed.

### d9 — Plan parsing

Inspected `cases/d9/CONTRACT.md` and `cases/d9/plan.py`, including the entire parser and graph traversal. No separate readiness caller is supplied. No Spec finding.

`parse` owns an ordinary transformation over local data (`plan.py:8–41`). It constructs fresh Tickets in declaration order, trimming IDs, requiring the colon separator and a nonempty declared ID, and interpreting an empty right side as an empty dependency tuple (`plan.py:9–18`). Dependency strings are trimmed, retained in their declared order, and empty dependency IDs are rejected. Repeated declared IDs cannot silently replace one another: the index-size check rejects them (`plan.py:19–21`).

The graph walk checks each encountered identity against the complete declaration index, so forward references are allowed while genuinely missing dependencies reject (`plan.py:23–32`). `visiting` represents the active traversal path and `done` represents completed nodes. Encountering an active node rejects a cycle; encountering a completed node safely skips repeated traversal (`plan.py:26–38`). Leave markers remove only the path entry they previously entered. Dependency scheduling is reversed for stack processing, and neither the stack nor the visited sets rewrite a Ticket's stored dependency sequence (`plan.py:39–40`). Thus traversal order cannot reorder the returned values. Duplicate dependency references are not forbidden by this contract, and the traversal can skip their completed occurrences without treating them as cycles.

The return is a tuple of newly constructed frozen Ticket values whose dependency fields are tuples of strings (`plan.py:3–6,18,41`). The mutable list, index and traversal sets are local implementation data, not externally coordinated state. There is no external writer, persistence, restoration or invalidation responsibility. The supplied result supports read-only readiness calculations without requiring consumers to finish construction. An object wrapping the parse lifecycle would add no contract value and would conflict with the instruction to keep ordinary transformations as functions.

This conclusion uses the provided comma/colon/plus syntax. No escaping mechanism, alternate configuration format, cross-call cache, recursion-limit policy or unspecified dependency deduplication rule is inferred.

### e4 — Submission observations

Inspected `cases/e4/CONTRACT.md`, `cases/e4/attempt.py`, `cases/e4/worker.py` and `cases/e4/repair.py`. The contract requires Attempt to be the sole writer and the single owning submission operation; both worker and repair entry paths must delegate (`CONTRACT.md:2–8`). Exposed dictionaries are deliberately available for read-only reporting, so their public visibility alone is not a defect.

Construction creates the attempt record and retains the mirrored ticket reference (`attempt.py:2–4`). `Attempt.submit` rejects non-running state before editing, then updates revision/status and all current-ticket fields in one synchronous operation (`attempt.py:6–13`). The ordinary worker calls that operation (`worker.py:1–2`). With the stated absence of concurrency and ordinary supplied dictionaries, this path maintains the approved submission transition.

The repair entry path reads and edits both dictionaries itself, copying the guard and all five assignments (`repair.py:1–8`). Its current values match the owner operation, but the required ownership boundary has already been crossed. No persistence/restore/invalidation path or additional reporting implementation is supplied.

#### F3 — Blocking: repair is an independent writer and duplicate submission-policy owner

Full key: `review-development-19-c5/spec-c5-01/F3`.

Locations: [repair's copied guard and record edits](/tmp/development-review-19-c5/cases/e4/repair.py:1), [the intended owner operation](/tmp/development-review-19-c5/cases/e4/attempt.py:6), [delegating normal caller](/tmp/development-review-19-c5/cases/e4/worker.py:1), governed by [the single-operation and only-owner-write requirements](/tmp/development-review-19-c5/cases/e4/CONTRACT.md:5).

This is an explicit Spec breach even though both paths currently produce the same simple submission result. Submission policy is implemented in two independent places. For example, a future change to the guard in `Attempt.submit` would govern the worker path while repairs would keep using the old guard and write records directly. Today, repair itself already violates the requirement that only the owner write these records and callers delegate. Passing the current happy path would not establish that required outcome.

Replace repair's policy and assignments with delegation to `attempt.submit(revision)`, preserving its existing entry function if needed. The operation already owns exactly the state and ordering in question. No additional encapsulation framework, generic state machine, or restriction on the approved read-only reporting interface is needed. Revalidation should cover both entry paths' delegation and rejection without mutation for non-running attempts.

The contract here does not add h8's separate construction-consistency, nonempty-revision or copied-snapshot requirements; those have not been imported as extra findings. F3 is open, with no repair or risk decision supplied.

### f6 — Local IO

Inspected `cases/f6/CONTRACT.md` and all of `cases/f6/io_ops.py`. No caller is supplied beyond these primitive interfaces. No Spec finding.

`atomic_write` owns only the explicitly requested file operation (`io_ops.py:7–18`). It creates a UTF-8 temporary file in `destination.parent`, so the temporary and destination are on the same filesystem under the supplied existing-directory precondition (`io_ops.py:8–13`). It writes and closes the temporary before `os.replace` touches the destination (`io_ops.py:14–15`). A write/encoding/close failure before replace therefore leaves existing destination content untouched. The temporary path is retained once creation succeeds; `finally` unlinks it on an earlier failure, and the missing-ok cleanup is harmless after a successful rename (`io_ops.py:9–18`). The function does not truncate the existing destination as an intermediate step.

`invoke` owns process invocation rather than domain exit policy (`io_ops.py:20–28`). Its finite-timeout validation rejects nonfinite values and values for which finiteness checking fails (`io_ops.py:21–26`). It passes the vector directly to `subprocess.run`, uses the supplied cwd, captures text, sets the timeout and leaves `check=False` (`io_ops.py:27–28`). Shell invocation is not enabled. Nonzero process exits are returned as required, and no catch suppresses or translates TimeoutExpired. The contract does not require a positive timeout, so adding that rule would be a policy expansion rather than a repair.

There are no run/attempt/review records, shared domain readers or writers, checkpoints, restored aliases or domain invalidation paths. File persistence is the explicit output, not evidence that this module should own a run lifecycle. A normal operating-system operation can itself fail; this review does not claim immunity to inaccessible directories or cleanup failures caused by filesystem failure. The stated guarantees do not include fsync/crash durability or metadata preservation, and those omissions are not findings. The provided source keeps these helpers as small cohesive operations with domain decisions left to their callers.

### g1 — Prepared input

Inspected `cases/g1/CONTRACT.md`, `cases/g1/preparation.py`, `cases/g1/cli.py` and `cases/g1/resume.py`. The contract gives preparation complete responsibility for validation, normalization, selection membership and repair-limit initialization. Both entry paths must return a usable Prepared result without further ordering knowledge (`CONTRACT.md:2–8`).

`Prepared.__init__` makes a new top-level raw dictionary but explicitly initializes both derived fields to None (`preparation.py:1–5`). `prepare` checks only whether raw selection is truthy, then returns that incomplete object (`preparation.py:7–10`). The CLI caller becomes a second initializer: it computes unique ordered membership, converts/defaults the repair limit, assigns the fields and rejects limits below one (`cli.py:3–9`). The resumed caller simply returns `prepare(raw)` (`resume.py:3–4`), so it omits all of those steps.

The raw dictionary is not written by these paths; the new top-level dictionary at `preparation.py:3` supports that part of the contract. The defect is not that every configuration field must be deep-copied or that another class is needed. It is that the claimed prepared interface exports unfinished state and moves its required decisions into one entry caller. There is no checkpoint serializer here: `from_saved_config` is an alternate raw-config entry path, not a restoration mechanism that can justify skipping preparation.

#### F4 — Blocking: preparation exports incomplete state and skips resumed validation

Full key: `review-development-19-c5/spec-c5-01/F4`.

Locations: [incomplete Prepared construction](/tmp/development-review-19-c5/cases/g1/preparation.py:1), [prepare's premature return](/tmp/development-review-19-c5/cases/g1/preparation.py:7), [CLI-only initialization and validation](/tmp/development-review-19-c5/cases/g1/cli.py:3), [resumed entry](/tmp/development-review-19-c5/cases/g1/resume.py:3), governed by [complete-result and preparation-owned validation requirements](/tmp/development-review-19-c5/cases/g1/CONTRACT.md:2).

For the ordinary valid input `{"selected": ["A", "A", "B"]}`, direct preparation and the resumed entry return `selected=None` and `repair_limit=None`, instead of the ordered unique selection and default limit 2. The CLI returns populated fields only because it knows and performs the missing construction rules. For `{"selected": ["A"], "repair_limit": 0}`, preparation and the resumed entry also return normally instead of rejecting an invalid limit during preparation. A consumer cannot safely use either result under the approved interface.

Move the selection normalization and repair-limit conversion/default/positive validation into preparation's owning operation, and return only a completely initialized result. Have both entry paths consume or return that result directly. Preserve the input-copy/no-mutation rule and first-occurrence ordering; do not add an unsupported alternate normalization grammar. A fully initialized class or another small immutable representation is an implementation choice, not a new requirement. Revalidation should compare both entry paths with direct preparation for ordered duplicates, default limits and invalid limits, and confirm that raw input is unchanged.

Only the supplied preparation and CLI code write these derived fields; there is no concurrent writer, persistence, or later invalidation mechanism that can repair the returned incomplete result. F4 is open.

### h8 — Attempt operations

Inspected `cases/h8/CONTRACT.md`, `cases/h8/attempt.py` and `cases/h8/caller.py`. No Spec finding.

Attempt owns both its record and mirrored current observation. Construction deep-copies the supplied identity into the running record and deep-copies that record into the current view (`attempt.py:5–7`). Both therefore begin consistently, while ordinary nested caller-owned dictionary/list values are detached from internal state. The public caller only requests submit, complete and snapshot operations (`caller.py:3–7`); it does not coordinate record edits.

Submission checks both required preconditions before changing either view (`attempt.py:9–12`). Completion checks submitted state before changing either view and retains the existing revision (`attempt.py:14–17`). `_transition` prepares a complete new record and a separate deep-copied current view before publishing either one (`attempt.py:19–23`). In the specified nonconcurrent setting, that preserves the mirrored fields across both valid transitions. Validation failure occurs before publication, and failure during preparation of the copies also precedes publication. No status/revision partial edit is exposed through the supplied interface.

The deep copy in `_transition` also detaches accepted mutable revision dictionaries from the caller, including nested contents (`attempt.py:20–21`). `snapshot` independently deep-copies both views before giving them to consumers (`attempt.py:25–26`), preventing mutation of a returned nested dictionary from altering either internal view or a later snapshot. This matters because the contract explicitly mentions caller-owned input dictionaries; a shallow copy would not establish the same conclusion. The implementation does not rely on an undocumented string-only restriction for identities or revisions. Nonempty revision is checked by its ordinary truth value; no stronger string grammar is specified.

There are no other supplied writers, durable checkpoints, restoration paths or invalidation responsibilities. The small class is justified by its transition and mirrored-observation invariant, and the caller crosses a compact operation interface. No generic state-machine framework or different file arrangement is required for compliance.

## Checkpoint and progression applicability

The supplied architecture-checkpoint guidance distinguishes newly introduced lifecycle, persistence/restoration, shared mutable state and additional writers from the mere presence of functions or files. The visible affected workflows include durable/restored shared gate state in a3; in-memory attempt history and handoff ownership in c2; mirrored submission state with an additional actual writer in e4; preparation construction and caller initialization responsibilities in g1; and correctly owned in-memory transitions and mirrored views in h8. b7 is read-only validation, d9 returns immutable values, and f6 owns only the specified file/process primitives.

All supplied collaborators for those workflows were inspected, rather than limiting review to owner definitions. However, no before/after implementation revision, originating milestone, integration request or QA candidate was supplied. Consequently this report cannot truthfully declare a ticket-start/post-implementation new-trigger result, a production cumulative baseline, checkpoint fulfillment for an external milestone, integration eligibility or human acceptance. It supplies the requested source assessment, not invented workflow records or a third reviewer gate. An actual integration/QA workflow must establish its own applicable checkpoint and exact-candidate evidence. These missing external contexts do not become additional miniature-code findings.

The four blockers are within their respective supplied ownership contracts and have proportionate repairs under those contracts. This report neither authorizes changed ownership nor accepts their risks. Optional improvements have not been promoted into blockers. Any later repair needs exact-source independent revalidation while preserving this original report and its finding keys.

## Evidence audit

1. Read `REVIEW.md` first, then inventoried the snapshot with `rg --files --hidden -g '!**/.git/**'`. Read every case contract and every case source/caller with line-numbered output. Read the supplied ownership, review-record, architecture-checkpoint and report-envelope guidance, glossary, both ADRs and testing policy. Links leading outside the supplied snapshot were not followed.
2. Independently enumerated all regular snapshot files using Perl `File::Find`, computed each content SHA-256 using `Digest::SHA`, and constructed a JSON object mapping relative path to digest. Keys were sorted lexicographically; key/value strings were JSON encoded; entries used comma-space and colon-space separators, matching the specified default `json.dumps(sort_keys=True)` serialization for this ASCII manifest. The aggregate hash excludes a trailing newline.
3. The inventory contains 36 regular files: `REVIEW.md`, eight contracts, 16 case Python files, three hidden skill files and eight other supplied guidance files. The computed aggregate is `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`, matching the assignment. The manifest retains the identity of every supplied instruction/source file, including hidden `guidance/.agents` content; it is not an assessment of unread Standards-only skill content.
4. Saved that exact sorted path/digest JSON to `/tmp/development-review-19-spec-c5-manifest.json`. Saved this original report outside the snapshot and recorded its digest separately. The snapshot and repository were not modified. The only writes are disposable review artifacts under `/tmp` outside the snapshot.
5. No Python, harness, runtime tests, dependency installation or production checks were run. The assignment explicitly permits a standalone source assessment without runtime tests. The counterexamples above are source-derived traces, not claims of executed test outcomes. No sibling report, answer key, broader repository or evaluator file was consulted.

A content hash establishes which source/instructions were assessed. It does not show canonical restoration, correct attempt routing, single-owner mutation or complete preparation; those conclusions require the substantive reasoning above. Conversely, not running a test does not erase a direct contract/source contradiction. No passing mechanical observation is used to infer design approval or human acceptance.

## Assessment result

Spec assessment completed for all eight independent cases. Open blocking findings are F1/a3, F2/c2, F3/e4 and F4/g1; there are no optional findings. b7, d9, f6 and h8 are clean within the recorded source scope and contracts. No finding has a fixed, deferred or accepted disposition, and no integration or QA readiness determination is made.

Unresolved external information is limited to the absent historical baseline/change provenance, production workflow context and backend delivery/context telemetry described above. No unresolved assumption is used to narrow away an accepted-input counterexample to the four reported guarantees. Each case was judged independently; requirements were not imported from another case.