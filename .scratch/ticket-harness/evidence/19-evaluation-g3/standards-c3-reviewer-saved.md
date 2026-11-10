# Standards source assessment: development-review-19-c3 / standards-c3

This independent Standards assessment found four blocking issues: restored gate references lose their canonical identity (a3), report checking attaches to the latest attempt instead of the identified attempt (c2), repair submission bypasses the designated owner (e4), and preparation returns an unfinished result that callers must initialize (g1). Cases b7, d9, f6, and h8 have no findings within the supplied contracts and inspected scope. No optional suggestions are recorded.

## Report envelope

| Field | Value |
| --- | --- |
| Assessment | `development-review-19-c3`, the eight independent miniature cases in the retained snapshot. No originating production ticket, approved milestone, or work-item index was supplied. |
| Report identity | `standards-c3`; independent original Standards report; assignment/actor `/root/repair19/corpus_standards_c3`. Local finding IDs F1–F4 belong to this report. |
| Settings and their limits | The assignment requests a fresh GPT-6.1 Sol High, fork-none assessment with an active-context advisory target of at most 250,000 tokens. These are assignment/configuration statements. Independent backend/model/reasoning delivery confirmation, context-enforcement evidence, and observed context telemetry are unavailable. Configuration does not establish runtime delivery or backend enforcement. |
| Original baseline | The supplied standalone snapshot, SHA-256 `b33636d1b8fdcacd572de6c063064afd5068b4e1275c2714bf0091651513b5c4` over the sorted relative-path/file-digest JSON mapping described below. No earlier source revision or Git baseline was supplied; this is a whole-source assessment, not a diff review. |
| Assessed source | `/tmp/development-review-19-c3`, independently verified against that same aggregate digest. All 36 supplied files were read. |
| Instructions | [REVIEW.md](/tmp/development-review-19-c3/REVIEW.md); all eight case contracts; supplied ownership, review-record, checkpoint, testing, glossary, ADR, report-envelope, codebase-design, object-oriented-design, and test-strategy guidance. Their exact bytes are included in the retained snapshot and external source manifest. |
| Original output/evidence | Exact original report: `/tmp/development-review-19-standards-c3-report.md`. Source/instruction manifest: `/tmp/development-review-19-standards-c3-source-manifest.json`. Report content digest is recorded separately after capture, rather than self-embedded. |
| Prior observations/decisions | None supplied or consulted. No sibling reports, earlier reports, evaluator files, ticket material, or human risk-acceptance decisions were read. |
| Lifecycle | This Standards assignment is completed. Four findings remain open. This says nothing about delivery/completion of another reviewer axis or a production assessment. |

## Scope, method, and assumptions

I started with REVIEW.md, read every case's CONTRACT.md, and inspected every source file and supplied caller. The inspected case inventory is:

| Case | Complete case inventory and traced flow |
| --- | --- |
| a3 | CONTRACT.md, run.py, qa.py: construction → record → save → restore → invalidate → verified eligibility and durable reporting. |
| b7 | CONTRACT.md, git_ops.py, caller.py: caller supplies checkout/policies → injected Git operations → repository preflight → returned root/branch or rejection. |
| c2 | CONTRACT.md, checking.py, execution.py: start/history append → report receive/validation/attachment → decision read by attempt ID, including delayed and unknown-ID reports. |
| d9 | CONTRACT.md, plan.py: syntax splitting/normalization → frozen ticket construction → duplicate/reference/cycle checks → immutable result. No readiness caller was supplied. |
| e4 | CONTRACT.md, attempt.py, worker.py, repair.py: attempt construction → normal or repair submission → attempt record and current-ticket observation. No reporting implementation was supplied. |
| f6 | CONTRACT.md, io_ops.py: temporary-file write/close/replace/cleanup and finite-timeout process invocation. No external caller was supplied. |
| g1 | CONTRACT.md, preparation.py, cli.py, resume.py: preparation construction/validation → CLI initialization versus resumed direct return. No downstream execution implementation was supplied. |
| h8 | CONTRACT.md, attempt.py, caller.py: construction → guarded submit → guarded complete → copied snapshots, including caller-input and output aliases. |

The guidance inventory was ownership-review.md, review-records.md, architecture-checkpoints.md, the report template, the supplied codebase-design, microsoft_oop, and test-strategy SKILL.md files, testing.md, GLOSSARY.md, and both supplied ADRs. Functions and classes were evaluated as modules with an interface. I applied depth, locality, responsibility ownership, information hiding, and proportionate verification; I did not treat a class, extra abstraction, shorter function, or private field as inherently required.

The case contracts govern each independent case. I did not transfer requirements between cases: for example, e4 permits records exposed to read-only reporting, whereas h8 explicitly promises isolation from caller-owned dictionaries and copied snapshots. Likewise, h8's nonempty-revision rule is not silently imposed on e4.

Omitted scope is explicit: there is no supplied production package, prior baseline/diff, test suite, harness, issue history, migration corpus, installed environment, live Git checkout under review, milestone candidate, or human QA record. None was fetched or inferred. Links to targets absent from this snapshot were not followed outside it. No Python, runtime harness, or production tests were run, and no snapshot/repository files were modified. This is source/documentation assessment, as authorized by REVIEW.md, rather than production verification.

I assume the ordinary standard-library/local-filesystem behavior used by these examples, the injected Git contract stated in b7, and the explicit concurrency and persistence limits of each contract. I do not assume chronological report completion in c2, that only the CLI calls preparation in g1, or that a3's JSON round-trip preserves object identity. I do not infer hostile consumers writing records that a contract explicitly restricts to read-only use. Unspecified extensions such as crash durability, a generic validation framework, arbitrary-interruption recovery, and a new persistence schema are outside this review.

## Substantive assessment

### a3 — Canonical saved checks: blocking finding F1

The approved owner is Run. Its permitted operations register successful evidence, save/restore the durable representation, and invalidate a source; consumers only read. The contract explicitly requires verified references and durable reporting to resolve to the same canonical gate records after restoration ([CONTRACT.md:2–7](/tmp/development-review-19-c3/cases/a3/CONTRACT.md:2)).

Before serialization, ownership and reference identity are coherent: [run.py:8–11](/tmp/development-review-19-c3/cases/a3/run.py:8) creates one gate dictionary and puts that dictionary in both lists. Consequently, `invalidate` at [run.py:13–16](/tmp/development-review-19-c3/cases/a3/run.py:13) changes the object read through either view. `eligible` reads verified records; `report` returns copies of durable gate records ([qa.py:1–6](/tmp/development-review-19-c3/cases/a3/qa.py:1)). Neither consumer writes the owner's state.

That relationship is not reconstructed. Saving both lists as JSON preserves values and keys, but JSON contains no shared-reference identity. Loading produces separate dictionaries, and [run.py:25–26](/tmp/development-review-19-c3/cases/a3/run.py:25) installs both independent lists directly. `invalidate` then updates only the durable list. The concrete allowed flow `record("A") → save → restore → invalidate("A")` leaves the restored durable gate invalid while `eligible(restored, "A")` still finds valid verified evidence. This is an ownership/restoration defect with a QA consequence, not a preference about representation.

The remedy belongs in Run's save/restore relationship, preserving the required JSON keys and reconstructing verified entries as references to the canonical gates. In this miniature, registration maintains a one-to-one ordered correspondence; restoration can use that documented relation, with appropriate correspondence checks. If a more general saved relation is needed, its identifiers/migration rules must be explicit. Matching only on source is insufficient as a general remedy because the contract does not prohibit repeated evidence for a source. QA should continue reading its prescribed view rather than independently repeating invalidation logic.

For a plausible added gate attribute, Run should own its registration and restored canonical representation; consumers should learn only any newly required reporting field. A repair that makes invalidation synchronize unrelated duplicate dictionaries instead would preserve a fragile coordination obligation and would not satisfy the explicit same-canonical-record requirement.

### b7 — Cohesive repository preflight: no finding

`validate` is the owner of preflight policy, with no mutable run state, durable representation, restoration, or invalidation path. The caller supplies a checkout and the `expected_branch`/`base` policies and receives a resolved root and branch. [caller.py:4–8](/tmp/development-review-19-c3/cases/b7/caller.py:4) constructs the Git adapter using an argument vector, text capture, `check=False`, and `git -C` against the requested checkout. It does not duplicate validation decisions.

The nested `checked` operation at [git_ops.py:4–8](/tmp/development-review-19-c3/cases/b7/git_ops.py:4) rejects nonzero results before consuming output, matching the permitted ValueError reduction of Git failure details. The flow then obtains/resolves the repository root, uses `symbolic-ref --short HEAD` so detached HEAD rejects through that same failure path, checks the expected branch, rejects any porcelain status output including untracked files, verifies a commit-like base, and verifies ancestry ([git_ops.py:10–18](/tmp/development-review-19-c3/cases/b7/git_ops.py:10)). An unexpected branch, missing base, or failed ancestry cannot reach the success return. Removing one command-terminating newline does not strip arbitrary root-path whitespace.

This is a suitably deep function: its interface hides the sequence, status interpretation, and error decisions from the caller. The injected Git callable is a meaningful seam; a separate preflight class or generic validator would not improve the demonstrated ownership. A new repository precondition would be added within `validate`, while checkout/process mechanics remain in the supplied adapter. No source evidence justifies a blocking or optional finding under [CONTRACT.md:2–10](/tmp/development-review-19-c3/cases/b7/CONTRACT.md:2).

### c2 — Attempt-specific report ownership: blocking finding F2

The contract deliberately permits report work to finish after a subsequent attempt starts. History preserves start order, the report's attempt ID identifies its owner, checking only validates/returns report information, and execution must find the identified attempt and ask it to attach. Unknown IDs must reject without mutation ([CONTRACT.md:2–9](/tmp/development-review-19-c3/cases/c2/CONTRACT.md:2)). There is no durable checkpoint or restoration path.

`Execution.start` owns history initialization/append and `decision` reads an attempt by ID ([execution.py:10–20](/tmp/development-review-19-c3/cases/c2/execution.py:10)). However, `receive` delegates the entire mutable history to checking, and [checking.py:6–9](/tmp/development-review-19-c3/cases/c2/checking.py:6) writes `history[-1].handoff`. `validate_handoff` checks the payload's ID against the supplied report ID and requires a decision; it never establishes that the last history element owns that ID ([checking.py:1–4](/tmp/development-review-19-c3/cases/c2/checking.py:1)). The Attempt data record itself has no attachment operation.

For example, after `start("A")` and `start("B")`, receiving report A with `{"attempt": "A", "decision": "accept"}` successfully validates and places A's decision on B. `decision("A")` remains `None`; `decision("B")` returns A's handoff. An unknown ID with a self-consistent payload also validates and overwrites the latest known attempt. These flows need no simultaneous calls: permitted delayed completion is enough. With empty history, the implementation also raises an indexing error instead of locating/rejecting an unknown owner.

The proportional repair is to leave checking with validation/result creation, have execution resolve the supplied ID or reject without writes, and have the identified Attempt own attachment. Keep the history order intact. A change to validation content should be local to checking; a change to how history finds an owner should be local to execution; neither should require checking to understand shared-history ordering. Finding F2 covers both the wrong target and the unknown-ID mutation because they share this ownership error.

### d9 — Immutable plan transformation: no finding

There is no consequential mutable owner to invent here. `parse` owns one transformation/validation operation; each invocation initializes private lists/maps/sets and returns a fresh tuple of frozen Ticket values. The Ticket fields are strings and tuples of strings, so the frozen result has no nested mutable payload under this syntax ([plan.py:3–6](/tmp/development-review-19-c3/cases/d9/plan.py:3), [CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/d9/CONTRACT.md:2)). No external caller or readiness implementation was supplied; readiness is described only as a reader of this immutable result.

The parser trims IDs and dependency IDs, rejects missing IDs or a missing separator, interprets an empty right side as no dependencies, and rejects empty dependency tokens ([plan.py:8–18](/tmp/development-review-19-c3/cases/d9/plan.py:8)). The ordered ticket list and dependency tuples are never replaced by map/set order. The `by_id` cardinality check rejects duplicate normalized ticket IDs ([plan.py:19–21](/tmp/development-review-19-c3/cases/d9/plan.py:19)).

The iterative depth-first traversal uses `visiting` for the active ancestor path and `done` for fully traversed vertices. An enter operation checks reference existence, then active-path recurrence, then completed work. A leave marker removes the vertex from the active path and marks it completed. Reversed dependency pushes preserve ordinary left-to-right processing while siblings are not marked active prematurely ([plan.py:22–40](/tmp/development-review-19-c3/cases/d9/plan.py:22)). Thus missing dependencies and cycles reject, while shared dependencies and repeated already-completed dependencies do not become false cycles. The returned tuple preserves original declarations ([plan.py:41](/tmp/development-review-19-c3/cases/d9/plan.py:41)).

Persistence, restoration, and invalidation are absent by contract. Re-parsing creates a new immutable result. A syntax or validation change belongs in this parser, with a Ticket shape change only if the resulting data actually changes. Replacing the ordinary function with a parser lifecycle/class hierarchy would add obligations without repairing a demonstrated problem.

### e4 — Submission owner bypassed by repair: blocking finding F3

Attempt is the approved owner of submission and the mirrored current-ticket observation. Records may be exposed for read-only reporting, but only the owner may write them; both entry paths must delegate to one submission operation so policy has one owning implementation ([CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/e4/CONTRACT.md:2)). There is no concurrency, serialization, restoration, or saved-state invalidation path.

`Attempt.__init__` initializes its running record and retains the ticket observation target ([attempt.py:2–4](/tmp/development-review-19-c3/cases/e4/attempt.py:2)). `Attempt.submit` checks running status before mutation, records revision/status, and updates the ticket's attempt/revision/status ([attempt.py:6–13](/tmp/development-review-19-c3/cases/e4/attempt.py:6)). With the supplied ordinary dictionaries and no concurrent calls, this operation owns the complete submission transition. `receive_worker` appropriately delegates ([worker.py:1–2](/tmp/development-review-19-c3/cases/e4/worker.py:1)).

In contrast, [repair.py:1–8](/tmp/development-review-19-c3/cases/e4/repair.py:1) repeats the guard and every record mutation. The current statements happen to mirror `submit`, so this finding does not allege an already-demonstrated difference between their successful output values. It is a direct breach of the expressly approved single-writer/single-policy operation: repair is an additional writer, coupled to record shape, transition ordering, and mirror fields. A submission-policy fix in Attempt can leave repair following obsolete rules. This is exactly the cross-entry coordination that the contract rules out, so it is blocking even though both copies currently say the same thing.

The remedy is simply `receive_repair` delegating to `attempt.submit(revision)`. No class hierarchy, new owner, immutable-record conversion, or blanket snapshot-copy requirement is needed. A later policy change would then be made once in `Attempt.submit`, with both entry paths retaining the same narrow interface. Source inspection remains necessary to verify that ownership repair; matching behavioral tests alone cannot prove there is one owning operation.

### f6 — Local IO primitives with explicit guarantees: no finding

These functions own local IO mechanics rather than run, attempt, review, or submission state. The only persistence is the file the caller explicitly requests. There is no domain restoration or invalidation mechanism, and no caller code was supplied. The contract deliberately excludes crash durability/fsync and metadata preservation ([CONTRACT.md:2–9](/tmp/development-review-19-c3/cases/f6/CONTRACT.md:2)).

`atomic_write` normalizes the destination to a Path and creates its temporary file in `destination.parent`, meeting the same-filesystem requirement. It uses UTF-8, writes within the context manager, and closes the temporary file before `os.replace` ([io_ops.py:7–15](/tmp/development-review-19-c3/cases/f6/io_ops.py:7)). Existing destination content is untouched during creation, encoding, writing, and close; failures before replace therefore preserve that existing content. The `finally` block removes a named temporary file on failure; after successful replacement, `missing_ok=True` makes removal of the old temporary pathname harmless ([io_ops.py:16–18](/tmp/development-review-19-c3/cases/f6/io_ops.py:16)). There is no unsupported claim that this protects against process death, storage failure during cleanup, or external filesystem interference.

`invoke` explicitly rejects values that do not pass its finite-number check, then delegates process execution using the supplied argv/cwd, captured text, and timeout. It uses no shell and `check=False`, so an ordinary nonzero exit remains available to caller policy; no catch swallows `TimeoutExpired` ([io_ops.py:20–28](/tmp/development-review-19-c3/cases/f6/io_ops.py:20)). The contract does not impose a positive timeout, so I do not flag finite zero/negative timeouts merely because they may expire immediately. It also does not promise successful execution for unsupported argument types, unlaunchable programs, or every numeric timeout outside the subprocess/platform's usable range.

The functions have small, useful interfaces and cohesive implementation responsibilities. A different domain failure policy belongs to their callers, while a change to local write mechanics belongs inside `atomic_write`. Creating a lifecycle owner around these stateless primitives would not repair a supplied invariant.

### g1 — Preparation requires caller completion: blocking finding F4

Preparation owns validation and normalization. Both entry paths must receive a complete result: nonempty selected IDs, unique membership in first-occurrence order, and a positive repair limit with default 2. Callers must not know initialization order or derived-field rules; invalid repair limits reject during preparation ([CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/g1/CONTRACT.md:2)). The state is in memory; `from_saved_config` receives raw configuration, not a serialized Prepared checkpoint requiring reconstruction.

`Prepared.__init__` copies the top-level input dictionary but initializes both derived fields to `None` ([preparation.py:1–5](/tmp/development-review-19-c3/cases/g1/preparation.py:1)). `prepare` checks only the truthiness of raw selection and returns that unfinished value ([preparation.py:7–10](/tmp/development-review-19-c3/cases/g1/preparation.py:7)). Thus the approved owner does not fulfill its own postcondition.

The CLI supplies the missing policy: it deduplicates selection, converts/defaults the repair limit, rejects values below one, and writes both derived fields ([cli.py:3–9](/tmp/development-review-19-c3/cases/g1/cli.py:3)). The resumed entry path simply returns `prepare(raw)` ([resume.py:3–4](/tmp/development-review-19-c3/cases/g1/resume.py:3)). For ordinary accepted input such as `{"selected": ["B", "A", "B"]}`, the resumed result has `selected is None` and `repair_limit is None`, rather than `("B", "A")` and 2. For `{"selected": ["A"], "repair_limit": 0}`, preparation also returns successfully instead of rejecting. These are concrete failures without relying on any ambiguous interpretation of whitespace normalization or exotic input types.

The remedy is to perform the complete selection normalization and repair-limit conversion/default/positive validation inside preparation, constructing a Prepared result only after those decisions succeed. Both CLI and resumed callers should delegate and return/consume it without derived-field assignments. Preserve the input-copy/no-mutation guarantee. The existing code makes a shallow dictionary copy and does not mutate the original; the contract does not independently require h8-style deep alias isolation here, so I do not add that requirement. The precise treatment of selection members beyond the declared normalization should remain governed by the approved input syntax, not a reviewer-invented schema.

Changing the repair-limit default or validation policy should then require one owning implementation change in preparation. Today it requires awareness of CLI behavior and the missing resumed behavior, demonstrating poor locality as well as the observed incomplete result.

### h8 — Owned transitions and isolated observations: no finding

Attempt owns a real lifecycle invariant, so the small class has a purpose: construction initializes two consistent observations, submission requires running status and a nonempty revision, and completion requires submitted status. Callers request operations and receive copied snapshots; caller-owned input dictionaries must not mutate owner state ([CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/h8/CONTRACT.md:2)). There is no persistence, restoration, or concurrency requirement.

Construction deep-copies the identity and then creates an independently copied current observation ([attempt.py:5–7](/tmp/development-review-19-c3/cases/h8/attempt.py:5)). Both public transition operations validate before calling the internal transition, so an invalid submit or complete does not begin mutation ([attempt.py:9–17](/tmp/development-review-19-c3/cases/h8/attempt.py:9)). `_transition` first creates a copied complete updated record and a separate copied current record; only after both copies succeed does it publish them ([attempt.py:19–23](/tmp/development-review-19-c3/cases/h8/attempt.py:19)). With no concurrent observers, the sequential assignments do not expose a partial transition through the supplied interface. Copy failure before publication also leaves both existing views intact.

The revision is copied along with the updated record, so nested mutable dictionaries provided at submission cannot later change stored revision content. Snapshot deep copies protect both the owner and the two returned observations from nested output mutation ([attempt.py:25–26](/tmp/development-review-19-c3/cases/h8/attempt.py:25)). This reasoning includes nested dictionary/list aliases rather than assuming IDs and revisions are always immutable strings. An invalid operation fails before publication regardless of what the caller might subsequently do with its own inputs.

The supplied caller constructs, submits, completes, and reads a snapshot without inspecting or editing internal records ([caller.py:3–7](/tmp/development-review-19-c3/cases/h8/caller.py:3)). It need not coordinate mirror assignments or know transition representation. A new lifecycle operation would belong in Attempt with its guard and the shared publication operation; the caller would only request that operation. There is no concrete need for another abstraction, actor, or externally coordinated state machine.

## Findings

All four findings are open original observations. No repair, independent fix verification, deferral, risk acceptance, amendment, or human decision is supplied. The keys below identify this report's observations; they are not dispositions or integration authorization.

### F1 — Blocking: restore breaks canonical gate identity

- **Full key:** `development-review-19-c3/standards-c3/F1`.
- **Locations:** [a3/CONTRACT.md:3–6](/tmp/development-review-19-c3/cases/a3/CONTRACT.md:3); [a3/run.py:18–27](/tmp/development-review-19-c3/cases/a3/run.py:18); invalidation at [run.py:13–16](/tmp/development-review-19-c3/cases/a3/run.py:13); consumers at [qa.py:1–6](/tmp/development-review-19-c3/cases/a3/qa.py:1).
- **Evidence/consequence:** JSON round-tripping duplicates dictionaries; restore retains those duplicates. After recording A, restoring, then invalidating A, durable reporting says invalid while QA eligibility can still say valid. The required reference identity and source-invalidation guarantee fail.
- **Proportionate remedy:** Reconstruct verified references to canonical restored gates inside Run while preserving the required JSON keys and exact evidence correspondence. Do not move invalidation policy into QA or collapse distinct gates merely by equal source.
- **Focused repair verification:** Through the supplied flow, record/save/restore/invalidate and compare both readers. Include repeated-source evidence where needed to ensure correspondence survives; inspect the actual reference reconstruction as well as values.

### F2 — Blocking: checking writes to the latest attempt instead of the identified owner

- **Full key:** `development-review-19-c3/standards-c3/F2`.
- **Locations:** [c2/CONTRACT.md:2–9](/tmp/development-review-19-c3/cases/c2/CONTRACT.md:2); [c2/checking.py:6–9](/tmp/development-review-19-c3/cases/c2/checking.py:6); [c2/execution.py:13–20](/tmp/development-review-19-c3/cases/c2/execution.py:13).
- **Evidence/consequence:** Start A then B, then receive valid handoff A: `history[-1]` assigns it to B. A self-consistent unknown-ID report also overwrites B rather than rejecting without changes. Checking has become an unauthorized shared-history writer, and read-by-ID consumers observe the wrong decision.
- **Proportionate remedy:** Checking validates/returns report information; execution resolves the report's ID or rejects without mutation; the resolved Attempt owns attachment. Preserve history order and avoid making checking select from history.
- **Focused repair verification:** Use start/receive/decision to cover delayed A after B, unknown IDs with valid-looking payloads, and invalid payloads; verify all unrelated attempts and order remain unchanged. Empty-history rejection is a representative unknown-owner case, not a reason for a large scenario matrix.

### F3 — Blocking: repair duplicates the owner's submission policy and writes

- **Full key:** `development-review-19-c3/standards-c3/F3`.
- **Locations:** [e4/CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/e4/CONTRACT.md:2); owning operation [attempt.py:6–13](/tmp/development-review-19-c3/cases/e4/attempt.py:6); bypass [repair.py:1–8](/tmp/development-review-19-c3/cases/e4/repair.py:1); correct delegation [worker.py:1–2](/tmp/development-review-19-c3/cases/e4/worker.py:1).
- **Evidence/consequence:** Repair independently checks status and edits revision, status, and ticket mirrors. It currently reproduces the owner's successful transition, but violates the explicit owner-only/single-operation contract and requires policy/shape changes to be coordinated across both implementations.
- **Proportionate remedy:** Have `receive_repair` call `attempt.submit(revision)`, just as the normal worker path does. Preserve the allowed read-only reporting access and current owner.
- **Focused repair verification:** Inspect removal of the second writer, then exercise representative running and repeated-submission rejection through both entry paths, checking attempt/ticket coherence. A behavior-only equality test cannot establish the structural single-owner guarantee.

### F4 — Blocking: preparation does not return a complete validated result

- **Full key:** `development-review-19-c3/standards-c3/F4`.
- **Locations:** [g1/CONTRACT.md:2–8](/tmp/development-review-19-c3/cases/g1/CONTRACT.md:2); [preparation.py:1–10](/tmp/development-review-19-c3/cases/g1/preparation.py:1); caller initialization [cli.py:3–9](/tmp/development-review-19-c3/cases/g1/cli.py:3); resumed return [resume.py:3–4](/tmp/development-review-19-c3/cases/g1/resume.py:3).
- **Evidence/consequence:** `prepare` returns `selected=None` and `repair_limit=None` for nonempty valid selections, including on the resumed path. It accepts a zero repair limit. Only CLI knows how to finish initialization and reject invalid limits. Direct consumers cannot rely on the promised Prepared postcondition.
- **Proportionate remedy:** Centralize normalization and positive repair-limit validation/defaulting in preparation, and return only a fully initialized result. Make both callers delegate without writing derived fields; continue copying rather than mutating raw configuration.
- **Focused repair verification:** Compare both entry paths for ordered duplicate selection and the default limit, plus representative explicit-valid, zero, and unparseable limits; ensure preparation itself rejects invalid values and raw configuration remains unchanged. Cover distinct decisions rather than multiplying every entry-path/input combination without purpose.

## Verification scope and evidence limits

The focused repair checks above are coverage recommendations, not claimed test results or a new mandatory testing seam. No tests or coverage map were supplied, and no test files were changed. The supplied test-strategy/testing guidance favors existing public flows and representative failure decisions; it does not justify inventing tests of private methods, imposing a new internal-mock seam, or demanding production CLI/Git checks from these standalone examples. If repairs are later integrated into the actual harness, its approved public-CLI seam and exact-source required completion checks still apply.

The absence of tests here is not itself a finding: REVIEW.md expressly authorizes a standalone source/documentation assessment with no production tests required. Conversely, these findings are not established by a hash or a claimed passing suite. Their evidence is the traced source and contract counterexamples. No unobserved execution is represented as reproduced behavior.

## Checkpoint applicability and progression

The supplied checkpoint guidance requires attention to lifecycle, restoration, shared mutable state, and additional writers. Static source shows relevant responsibilities in a3 (durable gates/reference reconstruction), c2 (attempt history and report attachment), e4 (submission and mirrored observations), g1 (prepared-result initialization across callers), and h8 (owned attempt lifecycle and mirrored snapshots). The additional nonowner writers in c2/e4 and caller initialization in g1 are traced above. b7 and d9 introduce no persistent/shared mutable domain state; f6 explicitly writes a local file but owns no harness lifecycle/checkpoint state.

No before/after ticket revisions were supplied, so I cannot label any of these features historically “new,” attest to ticket-start/post-implementation trigger records, establish the last human-accepted cumulative baseline, or decide whether a real checkpoint gates a particular integration. The complete miniature workflows were inspected without inventing a missing production-package review. The locality/change examples in each case explain where an additional policy or operation would live; they do not authorize an implementation or ownership-contract change.

Four separate status observations are therefore:

1. **This Standards assessment is completed:** every supplied case, contract, source file, and caller was inspected and the original report captured.
2. **Findings are unresolved:** F1–F4 are blocking under their existing case contracts. No disposition or exact-repair verification is claimed. Authorized repairs should be followed by independent review of their exact source; changing/deferring a consequential contract requires the human authority described in the supplied guidance.
3. **Candidate readiness is not assessed:** no production candidate, membership, other-axis report, required-check evidence, or milestone workflow was supplied. Clean individual cases do not establish candidate readiness.
4. **Milestone acceptance is absent:** no human QA decision was supplied; this report grants none.

## Evidence audit

Read-only shell inspections used `rg --files -g '*' /tmp/development-review-19-c3`, `cat` for the initial REVIEW.md, and `nl -ba` for contracts, sources, callers, and supplied guidance. A batched guidance read exceeded its output budget; the report envelope, architecture-checkpoint guidance, and complete design skills were subsequently read separately so their contents were not inferred from truncated output. All 36 supplied files were ultimately inspected.

A Node standard-library-only command enumerated the snapshot's files, sorted their relative paths, computed each file's SHA-256, and computed the SHA-256 of the JSON object mapping paths to digests. Using default-spaced JSON formatting (`": "` and `", "`, no trailing newline in the hashed mapping), the result was:

`b33636d1b8fdcacd572de6c063064afd5068b4e1275c2714bf0091651513b5c4`

This matches the supplied snapshot identity. The separately saved [source manifest](/tmp/development-review-19-standards-c3-source-manifest.json) contains that mapping with a terminal newline; the aggregate above hashes the mapping without that newline. The command also reported 36 files. The compact-JSON variant produced a different digest, as expected; JSON formatting is part of this aggregate identity algorithm.

These observations establish which retained source/instruction bytes were assessed. They do not prove design quality, runtime correctness, actual model delivery, context-limit enforcement, integration eligibility, or human acceptance. No harness/runtime tests were run. Only the original report and disposable evidence outside the snapshot were written. No further scope or assumptions are silently claimed.
