# Spec source assessment: development-review-19-c3 / spec-c3

The assessment is complete. Four cases have blocking contract violations: a3 loses canonical gate identity on restore; c2 attaches handoffs to the latest attempt rather than the identified attempt; e4 gives repair a second submission writer; g1 returns an incomplete prepared result. No findings were identified in b7, d9, f6 or h8 within the inspected scope. There are no optional suggestions in this report.

## Report envelope

| Field | Value |
| --- | --- |
| Assessment | `development-review-19-c3`; standalone assessment of eight independent miniature cases. No originating ticket, milestone or assessment index was supplied. |
| Report identity | `spec-c3`, Spec axis, original independent assessment, assignment `/root/repair19/corpus_spec_c3`. Report-local finding IDs F1–F4 are namespaced below. |
| Assignment settings | Requested fresh GPT-6.1 Sol, High reasoning, fork-none; active-context advisory target at most 250,000 tokens. Actual backend/model delivery, reasoning enforcement, context enforcement and usage telemetry are unavailable to this reviewer. Requested configuration does not establish runtime delivery or enforcement. |
| Original baseline | The supplied complete snapshot, not a Git diff. No separate earlier implementation revision or feature/cumulative baseline was supplied. |
| Assessed source | `/tmp/development-review-19-c3`, SHA-256 `b33636d1b8fdcacd572de6c063064afd5068b4e1275c2714bf0091651513b5c4` over the sorted JSON mapping of relative file paths to their SHA-256 digests. Independently reproduced, including hidden guidance files. |
| Governing instructions | Assignment; `REVIEW.md`; all eight case `CONTRACT.md` files; supplied ownership-review, review-records, architecture-checkpoints and report-envelope guidance. Their exact bytes are covered by the snapshot identity and separately retained manifest. The supplied glossary, both ADRs and testing policy were also read. |
| Original output and audit evidence | This complete original report: `/tmp/development-review-19-spec-c3-report.md`. Source/instruction manifest: `/tmp/development-review-19-spec-c3-manifest.json`. The report digest is captured separately, outside this report. |
| Inspected implementation scope | Every Python source/caller in a3, b7, c2, d9, e4, f6, g1 and h8, as detailed below; all eight local contracts. No changed-hunk restriction. |
| Omitted scope | Broader repository, evaluator files, ticket material, prior/sibling reports, production package and runtime/harness execution were excluded by assignment. Absent linked documents were not followed outside the snapshot. Standards-specific design/OOP/test-strategy skills were inventoried and hashed, but not applied as additional Spec requirements; that is the separately assigned Standards axis. |
| Prior observations / decisions | None supplied or consulted. No prior finding keys, disposition history, repair, human decision, QA acceptance or amendment is claimed. |
| Review lifecycle | Completed for this defined Spec assignment; findings remain open. Overall combined review completion, integration eligibility, candidate readiness and milestone acceptance are not established here. |

All source references below resolve within the assessed snapshot. The case contracts are authoritative independently; an ownership or alias rule in one case is not imported into another.

## Substantive assessment

### a3 — saved checks: blocking F1

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/a3/CONTRACT.md:1), [run.py](/tmp/development-review-19-c3/cases/a3/run.py:1) and [qa.py](/tmp/development-review-19-c3/cases/a3/qa.py:1). Run initializes both lists, records evidence, invalidates source evidence, serializes it and reconstructs it. Run is the only implementation writer. QA's `eligible` reads `verified`; reporting reads `gates` and returns new top-level gate dictionaries. These consumers make no writes.

The governing invariant is stronger than equal values: verified references must resolve to the same canonical gate records used by durable reporting, including after a deliberate stop/restore. That identity allows one source invalidation to affect both views ([contract lines 2–7](/tmp/development-review-19-c3/cases/a3/CONTRACT.md:2)). Live construction satisfies it: `record` creates one gate dictionary and appends that same object to both lists ([run.py:9](/tmp/development-review-19-c3/cases/a3/run.py:9)). `invalidate` therefore reaches both live views by editing the canonical gates ([run.py:13](/tmp/development-review-19-c3/cases/a3/run.py:13)).

**Restoration failure.** JSON preserves the two named arrays and their values, but not their shared dictionary identities. `restore` independently adopts `value["gates"]` and `value["verified"]` ([run.py:25](/tmp/development-review-19-c3/cases/a3/run.py:25), [run.py:26](/tmp/development-review-19-c3/cases/a3/run.py:26)). Each array now contains its own decoded dictionaries. No reconstruction relinks verified references to canonical records.

A concrete contract-permitted sequence is: record source A; save; restore; invalidate A. The canonical gate's `valid` becomes false, so `report` reports invalid evidence. The separately decoded verified gate retains `passed=True, valid=True`, so `eligible(restored, "A")` still returns true ([qa.py:2](/tmp/development-review-19-c3/cases/a3/qa.py:2)). This is source reasoning, not a claim that the sequence was executed. The caller's explicit permission to invalidate A after restore makes this an immediate accepted-path failure, rather than a speculative outside mutation.

**Conclusion.** Blocking F1. The saved key names are preserved, but the promised later invalidation semantics and QA eligibility are not. The owner is correct; its reconstruction operation fails to re-establish its own invariant. No new owner or generic persistence framework is needed.

### b7 — repository preflight: clean within scope

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/b7/CONTRACT.md:1), [caller.py](/tmp/development-review-19-c3/cases/b7/caller.py:1) and [git_ops.py](/tmp/development-review-19-c3/cases/b7/git_ops.py:1). `preflight` supplies the requested checkout and policy values. Its injected Git function executes an argument list using `git -C <checkout>`, captures text and leaves nonzero-result policy to `validate` ([caller.py:5](/tmp/development-review-19-c3/cases/b7/caller.py:5)). No shell is used.

`validate` owns the decisions through its local `checked` operation: every invoked Git result is rejected on nonzero return code, with permitted reduction of details to ValueError ([git_ops.py:4](/tmp/development-review-19-c3/cases/b7/git_ops.py:4)). It obtains and resolves the root; rejects detached HEAD because `symbolic-ref --short HEAD` fails; rejects a different branch; checks porcelain status including all untracked files; verifies a commit-valued base; and requires that base to be an ancestor of HEAD ([git_ops.py:10](/tmp/development-review-19-c3/cases/b7/git_ops.py:10), [git_ops.py:14](/tmp/development-review-19-c3/cases/b7/git_ops.py:14), [git_ops.py:16](/tmp/development-review-19-c3/cases/b7/git_ops.py:16)). Success returns the resolved root and the branch already proven equal to the requested branch.

**State, readers and failures.** There is no run/attempt mutable state, saved representation, restore or invalidation path. The function's local variables are disposable results of read-only Git commands. Its reader is the caller receiving the pair. The caller does not duplicate branch, cleanliness, base-existence or ancestry rules. Failed Git commands, including failed base verification and non-ancestor exit results, abort before a successful return.

**Conclusion.** No finding. One function owns the cohesive preflight policy and exposes a small interface to its caller, precisely as permitted by the contract. The nested helper does not leak coordination responsibilities or require a class. This conclusion is based on the supplied CompletedProcess-like injected-callable contract; execution with actual Git and unusual external filesystem/process failures was not observed.

### c2 — report handoff: blocking F2

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/c2/CONTRACT.md:1), [checking.py](/tmp/development-review-19-c3/cases/c2/checking.py:1) and [execution.py](/tmp/development-review-19-c3/cases/c2/execution.py:1). Execution initializes and appends the ordered history through `start`. Each Attempt holds an ID and handoff. `receive` passes the shared history, supplied attempt ID and payload to Checking; `decision` reads a handoff by attempt ID ([execution.py:13](/tmp/development-review-19-c3/cases/c2/execution.py:13), [execution.py:16](/tmp/development-review-19-c3/cases/c2/execution.py:16), [execution.py:19](/tmp/development-review-19-c3/cases/c2/execution.py:19)).

The contract explicitly permits a report for an older attempt to finish after a newer attempt has started. It assigns validation to Checking, identified-owner lookup to Execution, and attachment to the identified attempt ([contract lines 2–9](/tmp/development-review-19-c3/cases/c2/CONTRACT.md:2)). There is no durable checkpoint, restore or invalidation mechanism to assess.

**Wrong destination and incompatible writer.** `validate_handoff` verifies only that the payload names the supplied ID and has a decision, then returns a dictionary ([checking.py:1](/tmp/development-review-19-c3/cases/c2/checking.py:1)). That validation does not establish which history member owns the handoff. `attach` then writes `history[-1].handoff` regardless of the supplied ID ([checking.py:8](/tmp/development-review-19-c3/cases/c2/checking.py:8)). Execution neither locates the named attempt nor asks that owner to attach anything; Attempt has no attachment operation.

Concrete accepted sequence: `start("A")`, `start("B")`, then `receive("A", {"attempt": "A", "decision": "approve"})`. Validation succeeds, but B receives A's handoff and A stays without one. The ordered history remains physically ordered, yet the ID-based reader returns the wrong association: `decision("A")` is None, while `decision("B")` exposes a handoff validated for A.

Unknown IDs also violate the rejection invariant. With either known attempt in history, `receive("unknown", {"attempt": "unknown", "decision": "approve"})` passes validation and changes the last attempt. No existence check occurs. An empty history would instead raise on indexing, but that does not repair the nonempty-history mutation. These are two consequences of the same absent identified-owner operation and are reported as one finding.

**Conclusion.** Blocking F2. Checking is an unauthorized shared-history writer and guesses recency as ownership. The defect defeats both delayed report delivery and unknown-ID safety. Preserve history order; change routing and ownership rather than forbidding contract-permitted delayed completion.

### d9 — plan parsing: clean within scope

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/d9/CONTRACT.md:1) and the complete [plan.py](/tmp/development-review-19-c3/cases/d9/plan.py:1). No separate readiness consumer implementation was supplied. The parser transforms the contract's text syntax into local Ticket values. The dataclass is frozen and its dependency sequence is a tuple of strings ([plan.py:3](/tmp/development-review-19-c3/cases/d9/plan.py:3)); the returned outer sequence is also a tuple ([plan.py:41](/tmp/development-review-19-c3/cases/d9/plan.py:41)).

**Invariant reasoning.** Partitioning requires a colon and a trimmed nonempty ID. An empty or whitespace-only right side becomes an empty dependency tuple, while nonempty right sides are split and trimmed, and empty dependency elements reject ([plan.py:11](/tmp/development-review-19-c3/cases/d9/plan.py:11), [plan.py:15](/tmp/development-review-19-c3/cases/d9/plan.py:15)). The local list preserves declaration order, and each tuple preserves dependency order. The dictionary-length check rejects duplicate IDs ([plan.py:19](/tmp/development-review-19-c3/cases/d9/plan.py:19)).

The iterative traversal rejects referenced IDs absent from `by_id` and detects a cycle when a node is encountered on the active `visiting` path ([plan.py:31](/tmp/development-review-19-c3/cases/d9/plan.py:31), [plan.py:33](/tmp/development-review-19-c3/cases/d9/plan.py:33)). The leaving marker removes that active mark and adds the node to `done`; a previously completed shared dependency is then skipped rather than treated as a cycle. Reversing dependency insertion onto the LIFO stack preserves normal dependency traversal order. Neither traversal set changes the returned ordering.

**State and failures.** Each invocation creates its own local tickets, lookup and traversal sets. Rejection discards that partial local work; there is no externally visible partial mutation. The output's strings, tuples and frozen Tickets provide the promised immutable data to readiness calculations. There is no resource lifecycle, shared mutable state, persistence, restoration or invalidation.

**Conclusion.** No finding. The function owns one ordinary transformation with its required validations. Its local parsing and graph bookkeeping do not require a service object or framework. Input outside the specified string syntax is not a requirement; duplicate dependency names are not separately forbidden by the contract and are not invented as an error condition here.

### e4 — submission observations: blocking F3

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/e4/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-c3/cases/e4/attempt.py:1), [worker.py](/tmp/development-review-19-c3/cases/e4/worker.py:1) and [repair.py](/tmp/development-review-19-c3/cases/e4/repair.py:1). Attempt constructs its running record and retains the current-ticket dictionary. Its `submit` operation checks that the attempt is running, updates revision/status, then mirrors attempt ID, revision and submitted status into the ticket ([attempt.py:6](/tmp/development-review-19-c3/cases/e4/attempt.py:6)). The normal worker entry delegates to that operation ([worker.py:2](/tmp/development-review-19-c3/cases/e4/worker.py:2)).

The contract deliberately exposes records to read-only reporting, permits only the owner to write, and explicitly requires submission policy to have one owning operation ([contract lines 2–8](/tmp/development-review-19-c3/cases/e4/CONTRACT.md:2)). There is no concurrent observation or persistence requirement here. Public exposure alone therefore is not a reason to demand copied snapshots or private fields; those would add requirements belonging to a different case.

**Second writer.** The repair entry independently checks running status and writes both dictionaries itself ([repair.py:2](/tmp/development-review-19-c3/cases/e4/repair.py:2), [repair.py:4](/tmp/development-review-19-c3/cases/e4/repair.py:4)). For ordinary running records, its current edits happen to match `Attempt.submit`. For non-running records, both entry paths currently reject before their own edits. That behavioral agreement does not satisfy the approved one-owner requirement: repair reproduces the policy and the mirrored-field transition rather than asking Attempt to perform it.

A concrete policy change would require coordinated edits to `Attempt.submit` and `receive_repair`; updating the approved owner alone would leave repair on the old policy. The present violation is the expressly forbidden second writer, not an assertion that such a future divergence has already occurred.

**Readers, restore and conclusion.** Reporting is only described in the contract; no reporting function is supplied. All actual writers in this snapshot are construction, `Attempt.submit` and the incompatible repair path. No save/restore or invalidation path exists. Blocking F3 follows directly from the explicit ownership acceptance requirement. It can be repaired by delegating repair to the existing operation, without redesigning record representation or adding a state-machine framework.

### f6 — local IO: clean within scope

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/f6/CONTRACT.md:1) and the complete [io_ops.py](/tmp/development-review-19-c3/cases/f6/io_ops.py:1). There are no supplied caller files or run/attempt/review records. These functions own only their local resource operations; domain policy remains with their eventual callers.

**Atomic write.** `atomic_write` creates a named UTF-8 text temporary file in `destination.parent`, which the contract requires the caller to supply as an existing directory ([io_ops.py:11](/tmp/development-review-19-c3/cases/f6/io_ops.py:11)). That places temporary and destination on the same filesystem. It writes to the temporary file and exits its context, closing/flushing it, before calling `os.replace` ([io_ops.py:14](/tmp/development-review-19-c3/cases/f6/io_ops.py:14), [io_ops.py:15](/tmp/development-review-19-c3/cases/f6/io_ops.py:15)). Thus an exception during creation, writing or closing before replacement does not overwrite the destination. The finally block removes the known temporary path on failure, and tolerates its absence after successful replacement ([io_ops.py:16](/tmp/development-review-19-c3/cases/f6/io_ops.py:16)). The function does not promise fsync/crash durability or preservation of destination metadata, and the contract expressly excludes both.

**Invocation.** `invoke` rejects nonfinite or nonnumeric timeout values through the finite check and ValueError path ([io_ops.py:21](/tmp/development-review-19-c3/cases/f6/io_ops.py:21)). It then passes the supplied argument vector and cwd to `subprocess.run` with text capture, a timeout and `check=False` ([io_ops.py:27](/tmp/development-review-19-c3/cases/f6/io_ops.py:27)). The default shell setting is false; it does not construct a command string. Nonzero exits return for domain interpretation, while TimeoutExpired is not caught and propagates. The contract requires finiteness, not a strictly positive timeout, so no extra positivity requirement is imposed.

**State, restoration and conclusion.** The only durable output is the requested file; its eventual reader/restoration policy is outside this primitive's contract and absent from the snapshot. The temporary resource has an operation-scoped cleanup lifecycle. There are no domain-record writers, saved run representation, domain restore or invalidation paths. No finding. The two functions are appropriate owners of these cohesive primitives; adding domain objects or lifecycle scaffolding would not address a demonstrated contract problem. Actual OS cleanup failures and subprocess timing behavior were not exercised.

### g1 — prepared input: blocking F4

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/g1/CONTRACT.md:1), [preparation.py](/tmp/development-review-19-c3/cases/g1/preparation.py:1), [cli.py](/tmp/development-review-19-c3/cases/g1/cli.py:1) and [resume.py](/tmp/development-review-19-c3/cases/g1/resume.py:1). Preparation should own validation, normalization and complete result creation for both entry paths. Consumers are expressly permitted to use the prepared result immediately; they should not know derived-field rules.

**Incomplete owner operation.** `Prepared.__init__` copies the raw dictionary but initializes both `selected` and `repair_limit` to None ([preparation.py:3](/tmp/development-review-19-c3/cases/g1/preparation.py:3)). `prepare` checks only truthiness of `raw["selected"]` and returns that incomplete result ([preparation.py:7](/tmp/development-review-19-c3/cases/g1/preparation.py:7)). It neither normalizes membership nor establishes the positive default limit, nor rejects an invalid limit.

The CLI compensates by assigning a first-order deduplicated tuple, converting/defaulting the repair limit and checking positivity itself ([cli.py:5](/tmp/development-review-19-c3/cases/g1/cli.py:5), [cli.py:6](/tmp/development-review-19-c3/cases/g1/cli.py:6)). It therefore writes derived result state and knows preparation rules the contract assigns to Preparation. The resumed entry merely returns `prepare(raw)` ([resume.py:4](/tmp/development-review-19-c3/cases/g1/resume.py:4)) and receives none of the CLI's compensating writes.

Concrete accepted input `{"selected": ["A", "A", "B"]}` through the resumed entry produces `selected=None, repair_limit=None`, instead of normalized membership `("A", "B")` with default 2. Even `{"selected": ["A"], "repair_limit": 0}` returns normally through `prepare` and the resumed entry, despite the required preparation-time rejection. These failures do not depend on executing any later worker.

**State and restoration.** The top-level raw dictionary is copied and none of the supplied code mutates the caller's raw configuration. The contract does not demand a deep snapshot of every nested raw value, so shallow copying is not separately treated as an alias violation. This is an in-memory preparation boundary; `from_saved_config` re-enters it with raw configuration, and is not a checkpoint serialization implementation. No durable representation or invalidation mechanism is supplied.

**Conclusion.** Blocking F4. The CLI happens to finish one path, but `prepare` violates its complete-result interface and the resumed path exposes that defect directly. Centralize validation and normalization in Preparation, build a complete result before returning, and have both callers delegate. A different class layout is unnecessary.

### h8 — attempt operations: clean within scope

**Inspected flow and owner.** Read [CONTRACT.md](/tmp/development-review-19-c3/cases/h8/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-c3/cases/h8/attempt.py:1) and [caller.py](/tmp/development-review-19-c3/cases/h8/caller.py:1). Attempt owns construction, transition and snapshot operations. The caller constructs an attempt, asks it to submit and complete, and returns the copied snapshots without editing records ([caller.py:4](/tmp/development-review-19-c3/cases/h8/caller.py:4)).

**Initial state and operations.** Construction deep-copies the supplied identity and builds a separate deep-copied current view with matching id/status/revision ([attempt.py:6](/tmp/development-review-19-c3/cases/h8/attempt.py:6)). Submission rejects unless running and revision is nonempty before transitioning; completion rejects unless submitted ([attempt.py:10](/tmp/development-review-19-c3/cases/h8/attempt.py:10), [attempt.py:15](/tmp/development-review-19-c3/cases/h8/attempt.py:15)). These rejected operations do not reach either assignment.

The shared transition operation first deep-copies the proposed updated record and its mirrored current view, then installs both ([attempt.py:19](/tmp/development-review-19-c3/cases/h8/attempt.py:19)). Copying occurs before either stored reference is replaced; under the stated no-concurrency contract there is no intervening observer of the two assignments. Both views therefore retain matching values through running → submitted → completed. A failed deep copy also occurs before installation and leaves the prior views intact.

**Aliases and consumers.** The copy protection covers the actual accepted dictionary inputs, rather than assuming identities and revisions are immutable strings. Mutating a nested identity dictionary after construction cannot change either view. A nonempty dictionary revision accepted by submission is deep-copied into internal state, so later caller mutation cannot change it. `snapshot` deep-copies both returned dictionaries ([attempt.py:25](/tmp/development-review-19-c3/cases/h8/attempt.py:25)), protecting state from mutations through nested snapshot values as well. No public operation returns a live record. Underscored implementation attributes are not a consumer API grant to write state.

**Restoration and conclusion.** No persistence, restore or source-invalidation behavior is required or supplied; the lifecycle is entirely in memory. No finding. The small class is justified by the real multi-view transition invariant and protected operations, and the caller crosses the intended narrow interface. No general state-machine framework is needed.

## Findings

### F1 — blocking: restore breaks canonical gate references

- **Full key:** `development-review-19-c3/spec-c3/F1`.
- **Contract:** [a3/CONTRACT.md:2](/tmp/development-review-19-c3/cases/a3/CONTRACT.md:2), especially canonical identity and post-restore invalidation.
- **Source:** [a3/run.py:25](/tmp/development-review-19-c3/cases/a3/run.py:25), [a3/run.py:26](/tmp/development-review-19-c3/cases/a3/run.py:26), read against [invalidate:13](/tmp/development-review-19-c3/cases/a3/run.py:13) and [QA reader:2](/tmp/development-review-19-c3/cases/a3/qa.py:2).
- **Consequence:** A restored source can be invalid in durable reporting and still eligible in QA.
- **Proportionate remedy:** Restore verified entries as references to their canonical restored gate objects, preserving the JSON keys. Use an unambiguous correspondence supported by the saved representation/current record invariant; a source-only lookup must not accidentally conflate multiple records for the same source. The current record operation appends the same evidence to both lists in the same order, which can support a bounded reconstruction. No new owner is required.
- **Focused verification after repair:** Record A, save/restore, invalidate A, and establish both reporting invalidity and QA ineligibility. Include repeated same-source records if the reconstruction uses matching. No such repair or verification was performed here.
- **Original disposition:** Open; no repair, independent verification or human risk decision supplied.

### F2 — blocking: Checking attaches to recency rather than the identified attempt

- **Full key:** `development-review-19-c3/spec-c3/F2`.
- **Contract:** [c2/CONTRACT.md:2](/tmp/development-review-19-c3/cases/c2/CONTRACT.md:2), including late report ownership, role separation and unknown-ID rejection.
- **Source:** [c2/checking.py:6](/tmp/development-review-19-c3/cases/c2/checking.py:6), particularly the write at line 8; [c2/execution.py:16](/tmp/development-review-19-c3/cases/c2/execution.py:16); Attempt's existing representation at [execution.py:5](/tmp/development-review-19-c3/cases/c2/execution.py:5).
- **Consequence:** A delayed A handoff overwrites B's observation; an unknown ID can mutate the latest known attempt.
- **Proportionate remedy:** Keep Checking validation-only. Execution resolves the supplied ID against history and rejects an unknown ID without mutation, then asks that Attempt's owning attachment operation to store the validated handoff. Preserve start-order history and the existing ID-based reader. This implements the already-approved owner; it does not create a new architectural mandate.
- **Focused verification after repair:** Start A then B, attach a valid A handoff, and observe A changed while B stayed untouched; reject a validly shaped unknown-ID handoff with all known attempts unchanged.
- **Original disposition:** Open; no repair, independent verification or human risk decision supplied.

### F3 — blocking: repair is a second submission-policy writer

- **Full key:** `development-review-19-c3/spec-c3/F3`.
- **Contract:** [e4/CONTRACT.md:2](/tmp/development-review-19-c3/cases/e4/CONTRACT.md:2), explicitly requiring one owning operation and delegated entry paths.
- **Source:** [e4/repair.py:2](/tmp/development-review-19-c3/cases/e4/repair.py:2), contrasted with the owning [Attempt.submit:6](/tmp/development-review-19-c3/cases/e4/attempt.py:6) and delegating [worker.py:2](/tmp/development-review-19-c3/cases/e4/worker.py:2).
- **Consequence:** Submission validation and both mirrored record edits have two implementation owners. A policy change cannot be made through the single operation promised by the approved contract.
- **Proportionate remedy:** Replace repair's duplicated guard/record edits with delegation to `attempt.submit(revision)`. Retain the intentional read-only reporting exposure and current data shape.
- **Focused verification after repair:** Confirm both entry paths delegate to the same operation, and retain the meaningful running-success/non-running-rejection observations for both views. The ownership assertion requires source inspection as well as observed equivalent outputs.
- **Original disposition:** Open; no repair, independent verification or human risk decision supplied.

### F4 — blocking: preparation returns unfinished derived state

- **Full key:** `development-review-19-c3/spec-c3/F4`.
- **Contract:** [g1/CONTRACT.md:2](/tmp/development-review-19-c3/cases/g1/CONTRACT.md:2), requiring complete normalized results, preparation-time rejection and caller independence.
- **Source:** [g1/preparation.py:4](/tmp/development-review-19-c3/cases/g1/preparation.py:4), [prepare:7](/tmp/development-review-19-c3/cases/g1/preparation.py:7), compensating writes at [cli.py:5](/tmp/development-review-19-c3/cases/g1/cli.py:5), and the exposed resumed path at [resume.py:4](/tmp/development-review-19-c3/cases/g1/resume.py:4).
- **Consequence:** Direct/resumed preparation returns None derived fields, omits default 2 and accepts invalid limits until some later consumer fails; callers must know how to finish construction.
- **Proportionate remedy:** Preparation performs membership normalization, ordered deduplication and repair-limit defaulting/validation before returning a complete Prepared value. Both entry paths then return that result directly. Preserve copying and nonmutation of raw input.
- **Focused verification after repair:** Compare direct, CLI and resumed preparation for duplicate selected IDs and omitted limit; require nonpositive limit rejection during preparation and unchanged raw configuration.
- **Original disposition:** Open; no repair, independent verification or human risk decision supplied.

These verification suggestions identify distinct contract failures and suitable observations; they are not new test files, executed checks or replacements for any actual target's approved verification gates.

## Checkpoint applicability and change reasoning

This is not a ticket implementation or a cumulative milestone QA review. No before/after ticket source, feature starting revision, last accepted milestone or actual QA decision was supplied. Therefore the required ticket-start/post-implementation newness assessments and cumulative-baseline acceptance cannot be established. Their absence is an assessment limit, not an invented defect in these standalone cases. This Spec report also does not replace the separate fresh High Standards assignment required for an applicable architecture checkpoint.

The responsibility inventory identifies where a real change would encounter the checkpoint triggers:

| Case | Exposed state/workflow responsibility | Bounded plausible change and required coordination |
| --- | --- | --- |
| a3 | Durable gate/verified records, shared identity, save/restore and source invalidation. | Adding a gate attribute or evidence category belongs to Run's record/restore/invalidate semantics; QA/report readers must retain the same canonical evidence meaning. A restoration repair must re-establish aliases, not merely alter output formatting. |
| b7 | Read-only preflight policy, no shared state or restore. | Another validation policy belongs in validate; the caller should only supply its policy input and Git seam. A policy-only extension does not inherently create a new lifecycle. |
| c2 | Ordered attempt lifecycle/history and per-attempt handoff writing. | Another report result should be validated by Checking, routed by Execution and attached by the identified Attempt, with ID-based consumption intact. It must not depend on latest-history position. |
| d9 | Local transformation into immutable values, no lifecycle or durable state. | Another syntax/graph rule belongs in parse and its immutable output contract; no reader should be asked to finish validation. |
| e4 | Submission lifecycle and shared mirrored observations with worker/repair writers. | A submission-policy change belongs in Attempt.submit, with both entries delegating. No save/restore updates are needed under this contract. |
| f6 | Operation-scoped temporary-file lifecycle and explicit file persistence only. | An IO-policy change belongs in the primitive and observable file/process outcomes; domain state restoration remains outside this module. |
| g1 | Configuration preparation and complete derived in-memory state across two entries. | Another derived preparation field belongs in Preparation and its complete result; CLI/resume should not acquire another completion step. No checkpoint format is present. |
| h8 | Encapsulated attempt lifecycle and mirrored views with copied input/output. | Another permitted transition belongs in Attempt's guards and shared transition operation; caller operations and snapshot expectations change accordingly. No saved representation exists. |

These are traces of responsibilities present in source, not yes/no claims that each was newly introduced by an unavailable diff. Open blockers above prevent a clean conclusion for their respective approved outcomes. None of the clean conclusions grants integration authority, resumes a run or records human acceptance.

## Evidence audit

1. Started with the supplied `REVIEW.md`, then read all eight contracts and every source/caller file using numbered source output. Also read the supplied ownership, review-record, checkpoint, envelope, glossary, ADR and testing documents. The first inventory omitted hidden paths because ordinary `rg --files` excludes them; a complete `rg --files --hidden --no-ignore | sort` inventory corrected that before the final identity audit.
2. The complete inventory contains 36 files: REVIEW.md, eight contracts, 16 Python files, three Standards-only skill files and eight other guidance documents. All 16 Python files were assessed; the three Standards-only skills were hashed for identity without importing their requirements into this Spec axis.
3. Ran `rg --files --hidden --no-ignore | sort | xargs sha256sum` with the snapshot as cwd. Constructed a lexicographically sorted JSON object mapping relative paths to those digests, using a space after each colon and comma, with no trailing newline. Hashing that JSON reproduced `b33636d1b8fdcacd572de6c063064afd5068b4e1275c2714bf0091651513b5c4`. Earlier hashes over the incomplete nonhidden inventory did not match and were not used as final source identity.
4. Retained that complete JSON mapping outside the snapshot at the manifest path in the envelope. It identifies source and supplied guidance, including the case contracts; it is not behavioral evidence.
5. No Python, dependencies, tests, production harness, process invocation from the cases, Git fixture or executable observation was run. The assignment explicitly calls for standalone source/document assessment without a harness. Counterexamples above are reasoned traces of the supplied operations, not fabricated runtime results.
6. No snapshot or repository file was modified. Only this report and its audit artifacts were written outside the snapshot. No sibling was contacted and no sibling/prior report was read.

The matching content hash establishes assessed-byte identity. It does not prove the approved invariants. The per-case caller/writer/reader/restoration reasoning supplies the design and behavior judgment; the four concrete violating paths supply the blocking findings.

## Assumptions, omitted scope and assessment result

The contracts delimit accepted behavior. The injected Git callable is treated as CompletedProcess-like text execution in the selected checkout, as explicitly promised. The parser consumes the specified string syntax. The IO caller supplies an existing directory and an argument vector. No concurrency is introduced into cases that exclude it. Caller-owned dictionary aliases are explicitly considered where h8 guarantees protection, and restored shared identities are considered where a3 requires them. I have not assumed that all identities/revisions are immutable strings to bypass those guarantees.

There is no supplied external reader implementation for d9 readiness, e4 reporting or f6 written-file consumption. Their permitted boundaries are assessed from the contracts and the actual exposed interfaces; unseen behavior is not attested. Linked domain/environment/ticket/template material absent from the snapshot was not fetched from the broader repository. No runtime verification evidence, repair revision, human acceptance or prior assessment history exists in this assignment.

The original result is **completed Spec assessment with four open blocking findings and no optional suggestions**. Clean cases are clean only for their local contracts and inspected source. The next responsible action is to carry F1–F4, this original report, the fixed snapshot identity and the contracts to the coordinating reviewer/authorized repair workflow. Any repair requires relevant independent review of its exact new source; this report remains an observation of the supplied snapshot. Findings resolution, broader review completion, QA readiness and human milestone acceptance remain separate and are not claimed.

