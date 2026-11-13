# Standards source assessment: development-review-19-c5 / standards-c5-01

Assessment completed. Four blocking findings are open: restored verification references in a3, handoff ownership and routing in c2, the second submission writer in e4, and incomplete prepared results in g1. No findings were identified in b7, d9, f6, or h8 within the supplied scope. There are no optional suggestions in this report. These are independent case judgments, not classifications inferred from another case.

## Report envelope

| Field | Value |
| --- | --- |
| Assessment | `development-review-19-c5`, independent Standards assessment of the eight miniature source cases; no originating production ticket or milestone was supplied. |
| Report identity | `standards-c5-01`; Standards; original attempt 1 for this assignment; actor/task `/root/repair19_branch/corpus_standards_c5`. |
| Settings and limits | Assignment specifies a fresh GPT-6.1 Sol High, fork-none assessment and an advisory active-context target of at most 250,000 tokens. Actual backend model/reasoning delivery, context telemetry, and target enforcement are unavailable to this reviewer. Configuration is not proof of runtime delivery or enforcement. |
| Original baseline | The retained snapshot at `/tmp/development-review-19-c5`; no historical Git baseline or change diff was supplied. The fixed source identity below is the baseline for this standalone assessment. |
| Assessed source | All 36 regular files in that snapshot, including hidden guidance files. SHA-256 of the sorted relative-path/content-digest mapping: `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`. Independently recomputed and matched. |
| Supplied instructions | The parent assignment; `REVIEW.md`; all eight case contracts; supplied ownership, report-envelope, record, checkpoint and testing guidance; supplied codebase-design, microsoft_oop and test-strategy skills; supplied glossary and both ADRs. The retained snapshot and path/digest manifest identify their exact contents. No backend instruction-delivery attestation is available. |
| Original report | `/tmp/development-review-19-standards-c5-report.md`, saved outside the read-only snapshot. Its capture digest belongs in a separate manifest, not inside this report. |
| Source identity evidence | `/tmp/development-review-19-standards-c5-source-manifest.json`, the complete sorted JSON path/digest mapping, outside the snapshot. |
| Inspected scope | Every supplied source file and caller in all eight cases, and every supplied guidance file; detailed flows below. No changed-hunk restriction. |
| Omitted scope | Broader repository, evaluator material, other reports, tickets, production harness, runtime tests, Git execution and OS fault injection. These were outside this assignment or not supplied. |
| Prior observations | None supplied or consulted. No prior finding keys, dispositions, repair evidence, human decisions or amendments are known. |

The applicable skills are the copies inside this snapshot. The object-oriented guidance is used to assess responsibility and change locality, not to impose classes. The codebase-design guidance permits a function to be a deep module. The test-strategy guidance does not establish a requirement to run a production suite for this standalone source assessment.

## Scope, contracts and assumptions

I began with `REVIEW.md`, then read every case contract and its complete source/caller set. The cases are unrelated; their own contracts control accepted behavior, owners, permitted writers, persistence and failure handling. In particular, a3 requires canonical reference identity after restore, e4 permits exposed records for read-only reporting, and h8 separately requires copied snapshots and isolation from caller-owned dictionaries. Those distinct requirements have not been transferred between cases.

The source inventory is complete for the supplied cases:

| Case | Contract and executable files inspected | Traced flow |
| --- | --- | --- |
| a3 | `CONTRACT.md`, `run.py`, `qa.py` | Construction, record, save, restore, source invalidation, QA eligibility and durable reporting. |
| b7 | `CONTRACT.md`, `git_ops.py`, `caller.py` | Caller environment preparation, injected Git operation, every preflight check, returned checkout/branch. |
| c2 | `CONTRACT.md`, `execution.py`, `checking.py` | Attempt start/history, report receipt, content validation, handoff attachment, ID-based decision read. |
| d9 | `CONTRACT.md`, `plan.py` | Parsing, immutable value construction, duplicate/reference validation, iterative cycle detection, returned ordering. |
| e4 | `CONTRACT.md`, `attempt.py`, `worker.py`, `repair.py` | Attempt initialization, both submission entries, guard, revision/status changes and mirrored ticket writes. |
| f6 | `CONTRACT.md`, `io_ops.py` | Temporary-file creation/write/close/replace/cleanup, timeout validation and process invocation. |
| g1 | `CONTRACT.md`, `preparation.py`, `cli.py`, `resume.py` | Raw copy, initial validation, object construction, CLI normalization, resumed-config return. |
| h8 | `CONTRACT.md`, `attempt.py`, `caller.py` | Construction/input copying, submit and complete guards, mirrored transition, copied snapshots, caller sequence. |

No additional caller implementation is supplied for a3, d9 or f6; their explicit consumer descriptions and the available callable interfaces define the review extent. In c2, the external report command is described by the contract; `Execution.receive` is the supplied entry carrying its ID. I do not claim inspection of an unprovided command implementation.

Referenced targets absent from the snapshot, including domain guidance, Python-environment guidance, the production harness guide, feature trackers, other templates and skill supplements, were not followed outside the snapshot. Supplied `GLOSSARY.md` and ADRs were read. No Python, dependency installation, tests or harness were run. There are no supplied tests or check records to assess for redundancy, isolation or actual passing behavior; that absence does not itself violate the explicit standalone-assessment contract.

The reasoning below uses concrete accepted values and ordinary supplied data structures. It does not rely on a narrower input domain to excuse a failed guarantee. It does not invent requirements for uniqueness of source names, positive rather than merely finite process timeouts, crash durability, private fields, copied reporting in e4, or a generic state-machine framework.

## Substantive source assessment

### a3 — restored references cease to be canonical

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/a3/CONTRACT.md:2), lines 2–7, assigns Run ownership of durable gates and verified references. Save/restore must retain the JSON keys and later source-invalidation semantics. Verified records must resolve to the same canonical records as durable reporting; QA reads verified evidence, and invalidating A after a deliberate-stop restore is explicitly allowed.

**Owner, writers and readers.** [Run](/tmp/development-review-19-c5/cases/a3/run.py:3) initializes the two lists at lines 4–6. `record`, lines 8–11, creates one dictionary and appends that same object to both lists. `invalidate`, lines 13–16, is the owner operation that changes the durable gate's `valid` field. `restore`, lines 22–27, is another authorized Run writer. [QA](/tmp/development-review-19-c5/cases/a3/qa.py:1), lines 1–3, reads the verified list to decide eligibility; `report`, lines 5–6, reads the gate list and copies each dictionary. Neither consumer writes the owner state in the supplied source.

**Actual behavior and restoration.** Before persistence, alias identity makes invalidation visible in both lists. `save`, lines 18–19, serializes both lists' values. JSON does not preserve their shared object identity. `restore` assigns independently decoded dictionaries to `run.gates` and `run.verified` at lines 25–26 without reconstructing references. This is not an objection to the two-list representation by preference: the contract explicitly requires their canonical relationship, and the supplied readers depend on it.

A concrete allowed sequence is `record("A")`, `save()`, `Run.restore(saved)`, then `invalidate("A")`. After that sequence, the durable gate has `valid=False`, while its decoded verified counterpart still has `valid=True`. `qa.eligible(restored, "A")` therefore remains true even though durable reporting shows the source evidence invalid. No concurrency, extra writer, malformed saved input or duplicate-source assumption is needed.

**Conclusion.** Blocking finding F1. Keeping the Run interface is appropriate; its recovery operation must restore the invariant that its normal operation already establishes. A new gate policy should remain local to Run, while QA continues to read the agreed views. A repair should reconstruct verified references into canonical restored gates rather than require QA to coordinate invalidation or compare a second source of truth.

### b7 — cohesive read-only preflight

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/b7/CONTRACT.md:2), lines 2–10, gives `validate` responsibility for the listed Git preflight decisions. It permits ValueError on failed Git operations, requires a read-only injected argument-vector operation against the requested checkout, and leaves expected-branch/base policy selection to the caller. It explicitly does not require a class or generic validation framework.

**Owner, caller and reads.** [The caller](/tmp/development-review-19-c5/cases/b7/caller.py:5), lines 5–19, discovers Git-local environment names, copies the process environment, removes those names, and constructs an injected operation using `git --no-optional-locks -C <checkout>`. All command arguments are passed as a vector; no shell is enabled. Returned bytes are decoded with `os.fsdecode` and wrapped as CompletedProcess-like text results. The caller selects the expected branch and base, then delegates to `validate`; it does not reimplement cleanliness, ancestry or branch policy.

[The validation function](/tmp/development-review-19-c5/cases/b7/git_ops.py:3), lines 3–21, owns the ordering and rejection decisions. Its internal `checked` operation rejects every nonzero command result. It resolves the root, checks symbolic HEAD is a local branch, compares the requested branch, checks porcelain status with untracked files included, verifies the base as a commit, and checks that base is an ancestor of HEAD. A detached HEAD fails the symbolic-ref call and is rejected. An unexpected branch or dirty status is rejected before successful return. The ancestry command's nonzero result is rejected rather than interpreted as permission to continue.

**Accepted values and effects.** `removesuffix("\n")` removes the output terminator without stripping arbitrary path/branch characters. The caller's filesystem decoding is appropriate for filesystem values. The supplied Git operations read the checkout; the local environment copy is ephemeral and does not mutate `os.environ`. There is no durable representation, shared run state, recovery path or invalidation requirement here.

**Conclusion.** Clean within scope. The function is a deep module because the caller learns one preflight interface instead of coordinating six decisions. Replacing it with an object or splitting each check into a public interface would add caller knowledge without fixing an observed defect. An additional preflight condition belongs in `validate`; the caller's checkout/environment adapter and policy arguments can remain unchanged. No process execution was performed to extend this source judgment into a runtime claim.

### c2 — content validation is followed by attachment to the wrong owner

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/c2/CONTRACT.md:2), lines 2–9, allows report work to finish after a later attempt starts. Handoffs belong to the supplied attempt ID. Checking validates/returns information; it must not choose or edit an attempt from shared history. Execution must locate the identified owner and ask that owner to attach. An unknown ID must reject without changing any attempt. There is no durable checkpoint.

**Owners, writer and reader.** [Execution](/tmp/development-review-19-c5/cases/c2/execution.py:4), lines 4–17, constructs Attempt values, owns the ordered history, appends starts and delegates receipt to Checking while passing that entire mutable history. Attempt currently contains only the ID and handoff fields. [Checking](/tmp/development-review-19-c5/cases/c2/checking.py:1), lines 1–9, validates the payload's ID and decision, copies the payload dictionary, then writes it into `history[-1].handoff`. That makes Checking both validator and attempt selector/writer. `Execution.decision`, lines 19–20, reads handoffs by requested ID; it cannot correct the earlier misrouting.

**Concrete consequences.** Start attempt A, then attempt B, then receive A's valid `{"attempt": "A", "decision": "accept"}` report. Content validation succeeds for A, but attachment changes B. `decision("A")` still returns None, while `decision("B")` yields A's decision payload. Similarly, a valid payload for unknown C passes validation and overwrites the latest existing attempt rather than rejecting without changes. Both examples use distinct IDs and valid report content, so neither depends on an unspecified duplicate-ID policy.

**Conclusion.** Blocking finding F2. The ownership violation is directly responsible for incorrect observable decisions. The solution is to remove shared-history selection/writing from Checking, resolve the supplied ID in Execution, reject an unknown ID without mutation, and attach validated information through the identified Attempt's operation. History order can remain unchanged. Another handoff-content rule should change Checking's validation without changing owner selection; a routing change should remain in Execution. There is no restoration or invalidation layer that could repair the current wrong-owner write later.

### d9 — immutable parsing and graph validation stay behind one interface

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/d9/CONTRACT.md:2), lines 2–8, requires fresh immutable Ticket results, specified parsing/rejection rules, preserved declaration/dependency order and no lifecycle, shared mutable state or persistence. It explicitly keeps ordinary transformations as functions.

**State and operations.** [The parser](/tmp/development-review-19-c5/cases/d9/plan.py:3), lines 3–41, creates frozen Ticket values with string IDs and tuple dependencies. All mutable lists, dictionaries, sets and stack entries are local to a call. Construction checks empty IDs and missing separators, trims IDs/dependencies, permits an empty right side, rejects empty dependency tokens and duplicate ticket IDs, then validates graph references and cycles before returning a tuple.

**Graph reasoning.** The `by_id` mapping owns lookup only within parsing. For each ticket, the stack models entry and leaving frames. An entered node remains in `visiting` until its leaving frame is processed. A dependency encountered in `visiting` is therefore a cycle; a completed node in `done` may be skipped safely. An unknown dependency is rejected before lookup/use. Shared dependencies and repeated dependency references do not alone create a cycle: each fully processed dependency is in `done` before a later reference is visited. The iterative traversal does not impose the recursion-depth limit of a recursive DFS. None of those traversal choices reorder the returned tickets or their dependencies, which come from the original parsed sequence.

**Readers and lifecycle.** The contract's readiness calculations consume the immutable returned value; their implementation is not supplied. No caller must finish validation or coordinate mutable graph state. Frozen Ticket fields and tuple dependencies make ordinary consumer mutation unavailable. There is no durable representation or recovery/invalidation behavior to preserve.

**Conclusion.** Clean within scope. The function's parsing and graph validation have one cohesive responsibility, and its interface hides that work from readiness readers. Its length alone is not a defect, and the supplied contract provides no second configuration variant that would justify a strategy hierarchy. A new syntax or graph-validation rule changes this parser; immutable consumers should not need to reproduce that rule.

### e4 — repair is an unauthorized second writer of submission policy

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/e4/CONTRACT.md:2), lines 2–8, gives Attempt ownership of submission and mirrored ticket observation. Only a running attempt may submit; revision/status and ticket observations must agree. Both entry paths must delegate to one owning operation. Exposed records are deliberately available for read-only reporting, and only the owner may write them. There is no concurrency or persistence.

**Owner and normal caller.** [Attempt](/tmp/development-review-19-c5/cases/e4/attempt.py:2), lines 2–13, initializes its running record and retains the ticket observation. `submit` guards status before writing and then performs all five corresponding record/ticket updates. [The normal worker](/tmp/development-review-19-c5/cases/e4/worker.py:1), lines 1–2, calls this operation. Its caller does not need to know the fields or update order.

**Additional writer.** [The repair entry](/tmp/development-review-19-c5/cases/e4/repair.py:1), lines 1–8, reproduces the guard and writes Attempt's record and ticket directly. The current copied statements happen to implement the same ordinary transition. That does not satisfy the explicit ownership contract: repair is already an additional writer, and changing `Attempt.submit` does not change repair policy. For example, adding an owner-side submission rejection or another mirrored observation in the approved owning operation would immediately leave repair following the old rules. The caller must currently learn the complete record representation and transition ordering to stay correct.

**Conclusion.** Blocking finding F3 for the documented ownership requirement, with a concrete two-site maintenance consequence. This is not a demand for private fields, defensive copies or a general framework. Read-only record exposure is authorized. The proportionate repair is for `receive_repair` to call `attempt.submit(revision)`, matching the worker. Initialization and submission then remain owner writes, while reporting remains read-only. There is no save/restore or invalidation path to migrate.

### f6 — local IO policy remains separate from domain decisions

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/f6/CONTRACT.md:2), lines 2–9, requires complete UTF-8 replacement using a temporary file on the destination filesystem, survival of existing contents if an exception occurs before replacement, and temporary-file cleanup on failure. The directory already exists. It excludes crash durability/fsync and metadata preservation. Process invocation uses an argument vector, supplied cwd, text capture and finite timeout; nonzero exits are returned for caller policy and TimeoutExpired propagates. These operations own no run, attempt or review records.

**File operation and failure ordering.** [The implementation](/tmp/development-review-19-c5/cases/f6/io_ops.py:7), lines 7–18, creates its named temporary file in `destination.parent`, with UTF-8 text encoding and automatic deletion disabled. It remembers the temporary path before writing, closes the file through the context manager, and only then calls `os.replace`. Writing or closing failures occur before the destination replacement, while `finally` attempts to remove the remembered temporary file. If replacement fails, that same cleanup path applies. After successful replacement the old temporary pathname is absent, and `missing_ok=True` permits cleanup to finish without undoing success. The destination is never opened for in-place truncation. Same-directory temporary placement supplies the required filesystem relationship.

**Process operation and caller policy.** `invoke`, lines 20–28, checks timeout finiteness and rejects invalid/nonfinite values with ValueError. It calls `subprocess.run` with the supplied vector and cwd, text capture, explicit timeout and `check=False`. The default shell setting is false; nonzero exit results are returned rather than converted into domain failures. No catch intercepts TimeoutExpired. The contract says finite, not positive, so zero/negative finite timeout values do not justify inventing an additional positivity rule. No caller implementation is supplied; its required policy choice is how to interpret the returned process result, not how to implement process capture or file replacement.

**Ownership and persistence.** The file function owns the temporary pathname and replacement sequence, and the process function owns invocation options. Their only durable output is the explicitly replaced file. Neither reads or edits run/attempt/review records, defines a checkpoint representation, or needs a domain invalidation path. The source does not claim fsync, restored file metadata or durability across a crash. Filesystem availability, successful cleanup permissions and subprocess platform behavior are ordinary environmental prerequisites; no fault-injection result is claimed.

**Conclusion.** Clean within scope. These are appropriate function modules: adding a cleanup rule belongs in `atomic_write`, while interpreting a nonzero process result remains with its domain caller. No stateful object or generic IO framework is required. Verification here is source-level reasoning about the supplied ordering and options, not an execution or a claim to have proved all operating-system failures.

### g1 — preparation returns objects whose invariants still belong to one caller

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/g1/CONTRACT.md:2), lines 2–8, assigns configuration validation and normalization to Preparation. Both CLI and resumed entry paths must receive a complete result with nonempty selection, unique membership preserving first order and a positive repair limit defaulting to 2. Raw configuration must be copied, not mutated. Callers must not finish initialization or know the derived-field rules. Invalid repair limits reject during preparation.

**Construction and entry paths.** [Preparation](/tmp/development-review-19-c5/cases/g1/preparation.py:1), lines 1–10, copies the raw mapping, sets `selected` and `repair_limit` to None, checks only raw selection truthiness and returns that incomplete instance. [The CLI](/tmp/development-review-19-c5/cases/g1/cli.py:3), lines 3–9, then writes both derived fields, deduplicates selection, converts/defaults the repair limit and rejects values below 1. [The resumed entry](/tmp/development-review-19-c5/cases/g1/resume.py:3), lines 3–4, returns the incomplete result directly.

**Concrete consequences.** Preparing `{"selected": ["A", "A", "B"]}` returns None derived fields rather than `("A", "B")` and default 2. The CLI happens to finish those fields; the resumed entry does not. With `{"selected": ["A"], "repair_limit": 0}`, direct preparation and resumed entry return rather than reject at preparation. Thus a caller permitted to consume Prepared directly gets neither the stated values nor the stated rejection behavior. No checkpoint serializer is involved: the resumed path receives saved configuration, and the contract expressly says result state has no serialization here.

**Writers, readers and ownership.** Preparation constructs the result, but the CLI has become a second initializer and sole owner of several configuration rules. Consumers of resumed results cannot rely on the same interface. The raw mapping itself is copied and the shown functions do not mutate the supplied mapping; that part of the contract is satisfied. The contract does not separately promise the deep alias isolation required by h8, so I do not invent that additional finding here.

**Conclusion.** Blocking finding F4. Build and validate the complete result inside Preparation before returning. Both entry paths should only delegate to it and consume the result. Defaulting, normalization and positivity should have one implementation; a change to the default or normalization rule should then change Preparation alone. There is no requirement to add a builder, inheritance or a generic configuration framework.

### h8 — the class owns a genuine transition invariant and isolates observations

**Governing invariant.** [The contract](/tmp/development-review-19-c5/cases/h8/CONTRACT.md:2), lines 2–8, requires running → submitted → completed transitions, consistent mirrored observations at construction and transitions, guarded operations with no changes on rejection, copied snapshots and isolation from caller-owned input dictionaries. A small class is explicitly allowed; persistence and concurrency are absent.

**Owner and writers.** [Attempt](/tmp/development-review-19-c5/cases/h8/attempt.py:4), lines 4–26, is the only supplied writer. Construction deep-copies the identity into its record and deep-copies that record for the current observation. `submit` rejects a non-running state or empty revision before transition. `complete` rejects a non-submitted state before transition. `_transition` creates deep-copied next record/current values before installing either reference. This keeps the two observations value-consistent and isolates an accepted mutable revision from later caller changes. Even a failure while constructing a copied next value precedes either assignment.

**Caller and readers.** [The caller](/tmp/development-review-19-c5/cases/h8/caller.py:3), lines 3–7, creates an attempt, requests submission and completion in sequence and returns its snapshot. It makes no field-level transition decision. `snapshot`, lines 25–26, deep-copies both observations, so mutating returned nested dictionaries cannot edit the owner. Neither input identity dictionaries nor accepted revision dictionaries are retained as writable aliases. Rejected operations leave both views at their previous state. There is no requirement for these two observations to share object identity: their consistency and isolation requirements differ from a3's canonical-reference requirement.

**Conclusion.** Clean within scope. This class earns its interface by keeping lifecycle guards, mirrored updates and copying decisions together. Another submission/completion guard would change Attempt while the caller keeps asking for operations. There is no need for a general state-machine framework, additional wrappers or changes to caller behavior. There is no durable representation or restoration/invalidation path to assess.

## Findings

### F1 — blocking: restore breaks gate/reference identity

- **Full key:** `development-review-19-c5/standards-c5-01/F1`.
- **Locations:** `cases/a3/run.py:22–27`, especially assignments at lines 25–26; original shared identity at lines 8–11; invalidation at lines 13–16; QA eligibility at `cases/a3/qa.py:1–3`. Governing guarantee: `cases/a3/CONTRACT.md:2–7`.
- **Evidence and consequence:** The allowed record/save/restore/invalidate sequence leaves verified evidence valid after the canonical durable gate is invalid. QA can incorrectly treat an invalidated source as eligible.
- **Proportionate remedy:** Preserve the JSON keys and reconstruct verified entries as references into the restored canonical gates. In this supplied model, record appends the same gate to both lists in the same order, so that correspondence can be restored directly. If using an explicit identity scheme instead, it must preserve repeated-source records; resolving by source alone is insufficient because no unique-source restriction exists. Keep invalidation inside Run and leave consumers read-only.
- **Status:** Open original observation. No repair, independent verification, deferral or human decision is supplied.

### F2 — blocking: Checking selects and mutates the latest attempt instead of the identified owner

- **Full key:** `development-review-19-c5/standards-c5-01/F2`.
- **Locations:** `cases/c2/checking.py:6–9`, particularly line 8; caller at `cases/c2/execution.py:16–17`; reader at lines 19–20. Governing ownership and late-report guarantees: `cases/c2/CONTRACT.md:2–9`.
- **Evidence and consequence:** A's valid report delivered after B starts is attached to B. A valid unknown-ID report can also overwrite the latest attempt rather than reject without mutation. Consumers reading by ID receive missing or misattributed decisions.
- **Proportionate remedy:** Keep Checking responsible for validating/returning report information. Execution must locate the supplied attempt ID and reject unknown IDs without changing history, then ask that Attempt to attach validated information. Remove the need for Checking to receive or edit mutable shared history. Retain start ordering and the existing ID-based read semantics.
- **Status:** Open original observation. No repair, independent verification, deferral or human decision is supplied.

### F3 — blocking: repair reproduces submission writes outside the owning operation

- **Full key:** `development-review-19-c5/standards-c5-01/F3`.
- **Locations:** `cases/e4/repair.py:1–8`; owning operation at `cases/e4/attempt.py:6–13`; delegating worker at `cases/e4/worker.py:1–2`. Governing one-operation/permitted-writer requirement: `cases/e4/CONTRACT.md:2–8`.
- **Evidence and consequence:** Repair directly checks and changes the same records as Attempt.submit. This violates the explicit owner-only write rule and makes submission policy require coordinated edits in two independent implementations. Current equality of their statements does not supply the required single owning operation.
- **Proportionate remedy:** Replace the copied guard/updates in `receive_repair` with `attempt.submit(revision)`. Keep read-only reporting access as the contract permits. No broader encapsulation rewrite is needed.
- **Status:** Open original observation. No repair, independent verification, deferral or human decision is supplied. This is a contract-backed ownership blocker, not merely an optional preference for deduplication.

### F4 — blocking: preparation leaks incomplete initialization and limit validation to the CLI

- **Full key:** `development-review-19-c5/standards-c5-01/F4`.
- **Locations:** `cases/g1/preparation.py:1–10`; caller-side initialization at `cases/g1/cli.py:4–8`; direct resumed return at `cases/g1/resume.py:3–4`. Governing complete-result/one-owner guarantees: `cases/g1/CONTRACT.md:2–8`.
- **Evidence and consequence:** Direct and resumed preparation return `selected=None` and `repair_limit=None` even for a valid nonempty selection, and do not reject raw limit 0. Only the CLI repairs initialization and applies several owning rules. Consumers cannot safely use the promised prepared result.
- **Proportionate remedy:** Move unique-order selection normalization, default/conversion policy and positive-limit validation into Preparation and return only a fully initialized Prepared value. Have both entry paths delegate without further derived-field writes. Preserve raw-input nonmutation.
- **Status:** Open original observation. No repair, independent verification, deferral or human decision is supplied.

## Architecture-checkpoint and progression observations

The snapshot contains consequential lifecycle/shared-state responsibilities in a3, c2, e4 and h8, and a persistence/restoration path in a3. g1 contains coordinated result construction across entry paths. b7, d9 and f6 have no run/attempt/review lifecycle or shared domain-state owner; f6 has only its expressly scoped file replacement. The full supplied flows, including callers, readers, restoration and the repair writer, were inspected above rather than only listing files.

No change baseline, ticket start record, post-implementation trigger record, cumulative milestone source, prior accepted candidate or QA decision was supplied. I therefore cannot determine whether these responsibilities are newly introduced, attest a ticket's start/post-implementation trigger decisions, or certify a cumulative milestone checkpoint. I have not manufactured missing production workflow records as case findings. The applicable source assessment is complete for these independent snapshots; it does not stand in for an unperformed broader production assessment.

The four observations required by the checkpoint guidance remain separate:

| Observation | Result for this report |
| --- | --- |
| Assessment completed | Yes, this Standards assignment's complete supplied scope was assessed and its original report preserved. A parent assessment requiring other reports cannot be declared complete by this report alone. |
| Findings resolved/dispositioned | No. F1–F4 remain open blocking observations. No fix verification or authorized disposition exists in the supplied context. |
| Candidate ready for human QA | Not established. No actual production candidate, required membership/check evidence or cumulative checkpoint package was supplied. |
| Milestone accepted | Not established. No actual human exact-candidate QA decision was supplied; review completion cannot provide one. |

The proposed remedies stay within the explicitly documented owners. This report authorizes no implementation or contract change. If an eventual workflow seeks to accept a consequential risk, defer a blocker or change ownership instead of preserving these contracts, the existing record/checkpoint guidance requires its actual human decision and applicable amendment; no such decision is inferred here. Optional suggestions would remain optional, but this report has none.

## Evidence audit and limits

1. Read-only inventory used `rg --files --hidden /tmp/development-review-19-c5`; all eight case directories and all supplied guidance were included.
2. Complete source/contract inspection used `cat` and numbered reads with `nl -ba`. Guidance was read with `cat`; outputs that were truncated in the initial combined guidance read were reread completely before assessment. Exact case line references above come from the numbered source reads.
3. Identity verification used Perl `File::Find`, `Digest::SHA` and JSON string encoding. Every regular file under the snapshot, including `guidance/.agents/...`, contributed its relative path and SHA-256 content digest. Mapping keys were sorted, entries joined with comma-space, keys/values with colon-space, and the aggregate SHA-256 computed over that JSON text without a trailing newline. All paths/digests are ASCII, so this encoding matches the requested default `json.dumps(mapping, sort_keys=True)` separators and escaping for these entries. Count: 36 regular files. Result: `332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`, matching the supplied identity. The exact mapping was retained outside the snapshot.
4. Only disposable review artifacts were written under `/tmp`, outside the supplied snapshot. Neither snapshot nor repository was modified. No harness, production tests, Python, Git commands from the cases, subprocess examples or mutation scenarios were executed.
5. The examples in this report are source-derived counterexamples and reasoning, not claimed test executions. Hash agreement establishes which source/guidance was read; it does not establish correctness. Conversely, the substantive findings follow the actual contracts and data flow rather than the digest result.
6. Runtime delivery/model/context enforcement telemetry, hidden evaluations, sibling reports, broader callers and historical acceptance/disposition records remain unavailable or deliberately excluded. No claim is made about them.

## Assessment result

This original Standards assessment is complete for the exact supplied snapshot. a3, c2, e4 and g1 have the four open blocking findings above. b7, d9, f6 and h8 are clean within the recorded inspection; that is not universal approval beyond their contracts or supplied flows. No optional findings, completed repairs, superseded observations or human risk acceptances are recorded. The next responsible action is for the parent assessment to preserve this original report and carry its full finding keys into its normal aggregation and authorized repair/disposition workflow, without rewriting these observations.