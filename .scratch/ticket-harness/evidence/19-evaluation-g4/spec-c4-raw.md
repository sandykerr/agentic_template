# Spec source assessment: development-review-19-c4 / spec-c4-01

Four blocking findings remain open: a3 loses canonical gate references on restoration; c2 attaches a handoff to the latest attempt instead of its identified owner; e4 permits repair code to reproduce an owner-only transition; g1 returns incompletely prepared inputs and bypasses validation through resume. The inspected b7, d9, f6 and h8 flows meet their supplied contracts. There are no optional suggestions.

## Report envelope

| Field | Value |
| --- | --- |
| Assessment | development-review-19-c4, standalone assessment of eight independent miniature snapshots; no originating ticket or milestone supplied. |
| Report identity | spec-c4-01; Spec axis; original assignment/report; reviewer agent /root/repair19/corpus_spec_c4. |
| Assignment settings | Requested GPT-6.1 Sol, High reasoning, fresh fork-none assignment, with an advisory active-context target of at most 250,000 tokens. Actual backend model/reasoning delivery, backend enforcement, context-limit enforcement and active-context usage telemetry are unavailable. Configuration is not proof of runtime delivery or enforcement. |
| Original baseline | The supplied retained snapshot is the fixed starting identity for this whole-source assessment. No earlier Git baseline, diff or accepted milestone baseline was supplied; none is inferred. |
| Assessed source | /tmp/development-review-19-c4; all 36 regular files included in the retained path/digest manifest. Aggregate SHA-256: bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197. |
| Governing instructions | Assignment, REVIEW.md, all eight case CONTRACT.md files, supplied ownership-review.md, review-records.md, architecture-checkpoints.md and report.md envelope. Also read the supplied GLOSSARY.md, both ADRs and testing.md for interpretation and scope. Their exact contents are identified by the retained whole-snapshot manifest. |
| Evidence | This original report: /tmp/development-review-19-spec-c4-report.md. Canonical source/instruction manifest: [development-review-19-spec-c4-source-manifest.json](/tmp/development-review-19-spec-c4-source-manifest.json). No runtime observation logs exist because no runtime checks were performed. |
| Inspected scope | REVIEW.md; all 24 case files, comprising every case contract and every supplied source/caller; the eight guidance documents listed above. Concrete flows are recorded below. |
| Omitted scope | Broader repository, evaluator files, prior/sibling reports, ticket material, absent linked targets, production package, production/harness tests, Git behavior experiments, repairs and integration/QA execution. These are outside the assignment or not supplied. The three hidden supplied skill files are included in the identity manifest; their Standards-only application was not undertaken as this assignment is Spec. |
| Prior observations | None supplied or consulted. No prior finding keys, dispositions, repair claims or human review/QA decisions are available. |
| Review lifecycle | This Spec assignment is completed, with four open blocking findings. Other-axis or aggregate assessment completion is not established by this report. |

The cases have independent contracts. The cross-cutting guidance governs how this assessment traces ownership and records evidence; it does not add another case's behavior to a contract. Source locations below refer to the exact identified snapshot. Examples are reasoned from source and were not executed.

## Substantive assessment

### a3 — restored gates and verified references

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/a3/CONTRACT.md:1), [run.py](/tmp/development-review-19-c4/cases/a3/run.py:1) and [qa.py](/tmp/development-review-19-c4/cases/a3/qa.py:1).

Run owns both durable gate records and the verified references. Initialization creates the two containers at run.py:4–6. The permitted mutations are record, invalidate and reconstruction by restore. record at lines 8–11 appends the same newly created dictionary to both views. invalidate at lines 13–16 updates canonical records in gates. The supplied consumers are read-only: eligible reads the verified view at qa.py:1–3, and report copies each gate into an output dictionary at qa.py:5–6. There is no supplied external writer or concurrent flow.

Before a save/restore boundary, these operations preserve the promised invariant: invalidating a source changes the dictionary visible in both views. JSON serialization at run.py:18–19 preserves values and the two top-level keys, but JSON does not preserve shared object identity between separate occurrences. restore at lines 21–27 installs the separately decoded lists without reconstructing their references. Later invalidate changes only the restored gates dictionaries. QA can therefore retain valid evidence for a source whose durable report is invalid. This violates the explicit restoration and source invalidation guarantees in CONTRACT.md:2–6. See F1.

A proportional repair belongs to Run's restoration logic. The current owner and read-only consumers need not change. A future representation change must preserve the supported saved semantics and canonical reference reconstruction; it cannot rely on JSON values alone to recover aliases. No extra owner, framework or consumer-side invalidation is needed.

### b7 — repository preflight

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/b7/CONTRACT.md:1), [git_ops.py](/tmp/development-review-19-c4/cases/b7/git_ops.py:1) and [caller.py](/tmp/development-review-19-c4/cases/b7/caller.py:1). No Spec finding.

validate owns preflight policy, while the caller supplies the requested checkout and policy inputs. The caller's nested git function at caller.py:6–11 constructs an argument list with git -C, captures both streams, converts captured bytes to strings with os.fsdecode, and returns a CompletedProcess-like result. subprocess.run uses its shell-free default. This satisfies the injected callable's text-output contract without requiring text=True specifically. The caller delegates every repository decision at line 12.

The checked helper at git_ops.py:4–8 rejects every nonzero Git return code as ValueError, which is expressly allowed. The actual validation sequence resolves the top-level path at line 10; obtains symbolic HEAD at line 11, rejecting detached HEAD when that Git command fails; compares the actual and expected branches at lines 12–13; rejects any porcelain status output, explicitly including all untracked files, at lines 14–15; verifies the requested base as a commit at line 16; and requires that base to be an ancestor of HEAD at line 17. Only after those checks does it return the resolved root and verified branch at line 18. The suffix removal retains whitespace within path/branch values rather than indiscriminately trimming them.

No domain state is written, and there is no saved representation, restoration or invalidation lifecycle. Failure stops the return rather than publishing a partial preflight result. The contract assigns no duty to preserve full Git diagnostics and explicitly requires no class or generic validation framework. This cohesive function and small checked helper keep policy in one operation. A changed preflight policy would be implemented in validate, leaving the transport adapter as a caller of that policy. This conclusion rests on tracing the commands and their checked outcomes; it does not claim an observed run against Git.

### c2 — report handoff attribution

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/c2/CONTRACT.md:1), [checking.py](/tmp/development-review-19-c4/cases/c2/checking.py:1) and [execution.py](/tmp/development-review-19-c4/cases/c2/execution.py:1).

The approved owner is the identified Attempt, with Execution responsible for locating that owner. Checking validates report information and must not choose or edit an attempt from history (CONTRACT.md:2–9). Execution initializes the in-memory history and appends Attempt records in start order at execution.py:9–14. Consumers retrieve a handoff by attempt ID through decision at lines 19–20.

validate_handoff at checking.py:1–4 checks that the payload names the supplied attempt ID and contains a decision, then returns a dictionary. That payload validation is not owner lookup. Execution.receive at execution.py:16–17 passes the entire shared history into checking.attach. The latter writes history[-1].handoff at checking.py:8 irrespective of the validated attempt ID. Consequently, a report for an earlier attempt is assigned to a later one, and even an ID absent from a nonempty history can mutate its final attempt. The read-by-ID flow then exposes the incorrect attribution. This is both a directly observable attribution failure and a breach of the expressly divided checking/execution/attempt responsibilities. See F2.

History order itself remains preserved by append; changing that order is not the remedy. There is no durable checkpoint or restore/invalidation path to repair. Execution must locate the requested attempt and reject unknown IDs, Checking must return validated information without choosing or editing history, and the located owner must attach it. A new handoff validation rule belongs in Checking; it should not require that module to know which attempt happens to be last. The contract does not specify duplicate-start-ID policy or an exception class for unknown lookups, and this report does not invent either as an additional finding.

### d9 — immutable plan parsing

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/d9/CONTRACT.md:1) and [plan.py](/tmp/development-review-19-c4/cases/d9/plan.py:1). No caller implementation was supplied. No Spec finding.

parse owns syntax validation and graph validation during a single local transformation. Ticket is a frozen dataclass, its ID is a string and its dependencies are a tuple of strings (plan.py:3–6). Each parse creates its own list and Ticket values, and returns a tuple at line 41. There is no shared mutable state, lifecycle, external resource, save/restore or invalidation path. The stated readiness consumer receives the immutable result; its implementation is outside the supplied case.

Lines 10–18 split declarations, trim IDs, require an ID and colon, represent an empty right side as an empty dependency tuple, trim dependency IDs and reject empty components. Ticket append order and tuple construction preserve declaration and dependency order. The lookup length comparison at lines 19–21 rejects duplicate normalized IDs. The iterative traversal at lines 22–40 uses visiting for the current path and done for fully explored nodes. Unknown references reject at lines 31–32; encountering an active path rejects cycles at lines 33–34. A leaving frame removes a node from visiting and marks it done after its dependencies have been traversed. Reversing only the traversal push order at lines 39–40 does not reorder the stored dependency tuple.

This also handles ordinary overlapping acyclic dependencies: a completed node is skipped, while a still-visiting node represents a back edge. Repeated dependency references are not prohibited by the contract, and the done check does not make them a false cycle. Missing/duplicate IDs, missing dependencies and cycles all reject before a result is returned. No class for parser state is required: the transformation and temporary graph bookkeeping are locally owned. A syntax change would affect this function and its documented consumer contract, without requiring a persistence migration.

### e4 — normal and repair submission paths

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/e4/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-c4/cases/e4/attempt.py:1), [worker.py](/tmp/development-review-19-c4/cases/e4/worker.py:1) and [repair.py](/tmp/development-review-19-c4/cases/e4/repair.py:1).

The consequential state is the Attempt record plus the mirrored current-ticket fields. The contract makes Attempt the sole writer and requires one owning submission operation, shared by both entry paths (CONTRACT.md:2–8). Attempt initializes its running record at attempt.py:2–4. Its submit method checks the running state, then changes revision/status and mirrors attempt ID, revision and submitted status into the ticket at lines 6–13. With the ordinary writable records shown and no concurrent calls, the operation preserves the specified logical transition. It rejects a non-running record before its writes.

The normal worker caller correctly delegates to attempt.submit at worker.py:1–2. The repair caller performs the same check and all five record/ticket writes itself at repair.py:2–8. Its currently equivalent results do not satisfy the explicit single-operation and sole-writer requirements. An approved change to submission policy would require coordinating an owner method and an independent external implementation, with repair able to bypass a change made to the owner. See F3.

The exposed records are deliberately available to read-only reporting, so their visibility alone is not a finding. No reporting source is supplied beyond that stated consumer role. State is in-memory; no serialization, restoration or source invalidation contract exists. The proportional remedy is to have receive_repair delegate to submit, just as receive_worker does. It does not require another class, hiding every record, or a general state machine.

### f6 — local IO primitives

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/f6/CONTRACT.md:1) and [io_ops.py](/tmp/development-review-19-c4/cases/f6/io_ops.py:1). No caller implementation was supplied. No Spec finding.

atomic_write owns a local file replacement operation, not domain records. It creates a named temporary in destination.parent with UTF-8 encoding at io_ops.py:11–12, records the temporary path before writing at lines 13–14, exits the file context before os.replace at line 15, and attempts deletion in finally at lines 16–18. Thus writing or closing failures occur before replacement and preserve the previous destination content. A replace failure also reaches cleanup. On successful replacement, the former temporary pathname is absent and missing_ok permits cleanup to finish. Locating the temporary in the destination directory provides the same-filesystem basis required for replacement. The caller's existing-directory obligation is explicit; no directory creation is promised.

invoke checks a finite timeout at lines 20–26, reducing values that cannot be assessed as finite to ValueError. Its subprocess call at lines 27–28 supplies argv, cwd, text capture, timeout and check=False. It does not enable a shell. Nonzero exits are returned for caller policy and TimeoutExpired is not caught, as required. The contract requires finiteness rather than a positive timeout; imposing a separate positivity rule would be an added requirement.

The only persisted artifact is the explicitly replaced destination file. There is no run, attempt or review state to initialize, mirror or restore, and no domain outcome writer hidden in these primitives. The contract excludes crash durability/fsync and metadata preservation. This review therefore does not object to their absence. It also makes no runtime claim about filesystem faults, process execution or cleanup under external interference. The local functions own the described resource operations without requiring a lifecycle object; caller domain policy remains outside invoke.

### g1 — complete preparation for both entries

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/g1/CONTRACT.md:1), [preparation.py](/tmp/development-review-19-c4/cases/g1/preparation.py:1), [cli.py](/tmp/development-review-19-c4/cases/g1/cli.py:1) and [resume.py](/tmp/development-review-19-c4/cases/g1/resume.py:1).

Preparation is the approved owner of validation, normalized membership and the positive repair limit, with default 2. Every entry must receive a complete result and consumers must not finish initialization in a required order (CONTRACT.md:2–8). Prepared.__init__ copies the raw mapping at preparation.py:3 but initializes both derived fields to None at lines 4–5. prepare checks only selection truthiness and returns that incomplete instance at lines 7–10.

The CLI compensates by deduplicating selected members in first order, converting the repair limit and checking positivity at cli.py:5–8. That caller is performing required preparation work after the preparation operation has returned. The resumed entry at resume.py:3–4 simply returns prepare(raw), so it never receives those fields or validates the repair limit. For example, a resumed selection ["T", "T", "U"] returns selected=None and repair_limit=None rather than ("T", "U") and 2. A resumed configuration with selected=["T"] and repair_limit=0 does not reject during preparation. These examples violate express guarantees without needing an execution consumer or any assumption about whitespace normalization. See F4.

No supplied path mutates the raw mapping during these steps; copying it is an existing correct part of preparation. The contract does not promise a deep immutable copy of every nested raw value, unlike h8's explicit input isolation guarantee, so this report does not add that requirement. There is no durable checkpoint: from_saved_config is an alternative raw-input entry, not a serializer restoring Prepared instances. Fixing the common preparation operation and delegating both entries gives them identical complete results without adding a general framework or moving normalization into execution.

### h8 — owned attempt transitions and snapshots

Inspected [CONTRACT.md](/tmp/development-review-19-c4/cases/h8/CONTRACT.md:1), [attempt.py](/tmp/development-review-19-c4/cases/h8/attempt.py:1) and [caller.py](/tmp/development-review-19-c4/cases/h8/caller.py:1). No Spec finding.

Attempt owns both views and their transition policy. Construction at attempt.py:5–7 deep-copies the input identity into a running record with no revision, then deep-copies that record for current observations. This makes both views consistent while severing caller-owned dictionary aliases. Submission at lines 9–12 requires running state and a nonempty revision before any state changes. Completion at lines 14–17 requires submitted state, again rejecting before mutation.

Both valid operations delegate to _transition. It builds a deep-copied updated record and a second independent current view at lines 20–21 before assigning either owned field at lines 22–23. The supplied no-concurrency setting permits these paired assignments as one logical transition. Caller-provided revision dictionaries are copied; the owner also copies an existing revision when completing. If a required copy fails while preparing the update, the assignments have not occurred. Invalid state/nonempty checks leave both views unchanged.

snapshot at lines 25–26 returns independent deep copies of both views, so mutating either snapshot or the caller's original dictionaries cannot mutate owned state. execute at caller.py:3–7 asks for submit and complete, then returns snapshots; it does not write records. This satisfies the approved running -> submitted -> completed sequence and copied-consumer interface for the explicitly allowed dictionary inputs. No persistence, restoration or invalidation is promised.

The small class has concrete work: it coordinates guards, paired observations and alias isolation. No additional general state-machine framework is needed. A new transition or submission-policy rule would be implemented by this owner, with caller changes only when a caller needs to request a new operation. There is no saved representation to migrate.

## Findings

### F1 — Blocking: restoration breaks canonical gate invalidation

Full key: development-review-19-c4/spec-c4-01/F1. Case: a3. Disposition in this original report: open.

Contract: [a3/CONTRACT.md:2](/tmp/development-review-19-c4/cases/a3/CONTRACT.md:2), especially canonical records and restored source invalidation at lines 3–6. Defect: [a3/run.py:21](/tmp/development-review-19-c4/cases/a3/run.py:21), particularly independent assignments at lines 25–26. Relevant consumers: [a3/qa.py:1](/tmp/development-review-19-c4/cases/a3/qa.py:1).

Concrete source-derived counterexample: record source A; save; restore; invalidate A. The restored gates entry becomes valid=False, while the separately decoded verified entry remains valid=True. eligible(restored, "A") can still return True while report(restored) shows invalid evidence.

Consequence: QA eligibility can use evidence that the owner has invalidated after an expressly supported deliberate-stop restoration.

Remedy: reconstruct verified entries as references to canonical restored gate dictionaries, preserving the JSON keys and supported membership/order semantics. In the supplied owner operations both lists contain the same ordered members, so a small restoration repair can preserve separate containers with shared records. If the representation is later expanded, make reference reconstruction explicit rather than shifting invalidation into readers. No repair or independent verification has been performed.

### F2 — Blocking: handoffs are attached to the latest attempt, including for unknown IDs

Full key: development-review-19-c4/spec-c4-01/F2. Case: c2. Disposition: open.

Contract: [c2/CONTRACT.md:2](/tmp/development-review-19-c4/cases/c2/CONTRACT.md:2), including checker/owner division and unknown-ID rejection at lines 6–9. Defect: [c2/checking.py:6](/tmp/development-review-19-c4/cases/c2/checking.py:6), especially line 8; calling path: [c2/execution.py:16](/tmp/development-review-19-c4/cases/c2/execution.py:16).

Concrete counterexample: start A, then B; receive a payload {"attempt": "A", "decision": "accept"} for A. Validation succeeds, but B receives A's handoff and decision("A") remains None. With that nonempty history, a matching payload for an unknown ID also validates and overwrites B instead of rejecting without mutation.

Consequence: human-decision attribution and read-by-ID behavior are wrong in the explicitly supported delayed-report flow. Checking also writes shared history despite the contract prohibiting that responsibility.

Remedy: keep Checking limited to validation/result production; have Execution locate the requested Attempt and reject absence without writes, then ask that identified owner to attach the validated handoff. Preserve start order. Do not merely check that the payload names its supplied ID or relocate the same history[-1] assignment. No repair or independent verification has been performed.

### F3 — Blocking: repair bypasses the single owning submission operation

Full key: development-review-19-c4/spec-c4-01/F3. Case: e4. Disposition: open.

Contract: [e4/CONTRACT.md:2](/tmp/development-review-19-c4/cases/e4/CONTRACT.md:2), especially single ownership, delegating entry callers and owner-only writes at lines 5–8. Defect: [e4/repair.py:1](/tmp/development-review-19-c4/cases/e4/repair.py:1), lines 2–8. Existing correct owner and caller: [e4/attempt.py:6](/tmp/development-review-19-c4/cases/e4/attempt.py:6) and [e4/worker.py:1](/tmp/development-review-19-c4/cases/e4/worker.py:1).

Evidence: receive_repair reads the transition guard and directly writes the attempt revision/status plus all mirrored ticket fields, duplicating submit. Although its present ordinary successful result matches submit, it is an unauthorized external writer under this case's explicit approved ownership contract.

Consequence: the promised single operation does not own submission policy across both paths; changes in the owner can be bypassed by repair. This is a contract breach rather than a preference for a class or a prediction that the duplicated code already differs.

Remedy: replace the repair-side guard and edits with delegation to attempt.submit(revision). Preserve the deliberate read-only reporting exposure. No ownership change, wider refactor, repair or independent verification is claimed.

### F4 — Blocking: common preparation returns partial, unvalidated results

Full key: development-review-19-c4/spec-c4-01/F4. Case: g1. Disposition: open.

Contract: [g1/CONTRACT.md:2](/tmp/development-review-19-c4/cases/g1/CONTRACT.md:2), lines 2–8. Defect: [g1/preparation.py:1](/tmp/development-review-19-c4/cases/g1/preparation.py:1), especially None fields at lines 4–5 and return at line 10. Entry-path evidence: [g1/cli.py:3](/tmp/development-review-19-c4/cases/g1/cli.py:3) and [g1/resume.py:3](/tmp/development-review-19-c4/cases/g1/resume.py:3).

Concrete counterexamples: from_saved_config({"selected": ["T", "T", "U"]}) returns selected=None and repair_limit=None. from_saved_config({"selected": ["T"], "repair_limit": 0}) returns rather than rejecting the invalid limit. Direct prepare has the same behavior. The CLI's later assignments explain why that entry may appear successful while the shared operation remains incomplete.

Consequence: resumed consumers cannot directly use the promised prepared state, invalid repair policy escapes preparation, and the CLI must know derived-field initialization rules and ordering forbidden by the contract.

Remedy: perform selection normalization, defaulting, limit conversion and positive-limit validation within the owning preparation operation before returning a complete Prepared value; retain the raw mapping copy; have both entry paths delegate without finishing initialization. Do not patch resume with another copy of CLI's edits or defer validation to execution. No repair or independent verification has been performed.

## Checkpoint applicability and limits

This is a complete standalone Spec source assessment, not a cumulative development architecture checkpoint or a promotion decision. No originating ticket start/post-implementation revisions, feature provenance, accepted milestone baseline, membership, exact candidate, prior checkpoint, or QA decision were supplied. Therefore I cannot truthfully decide which lifecycle/writer/persistence path is newly introduced relative to a ticket baseline, establish a required cumulative package inventory, or mark a candidate ready. Their absence is recorded as a limit of this assignment, not invented as another miniature-case defect.

The source does expose the following responsibilities relevant to a real trigger assessment:

| Case | Present state/flow relevant to triggers | Restoration/invalidation |
| --- | --- | --- |
| a3 | Gate registration, shared canonical records, durable save/restore, later source invalidation. | Explicit JSON restoration; F1 breaks subsequent invalidation across views. |
| b7 | Read-only preflight; no domain lifecycle or additional state writer. | None. |
| c2 | Attempt history and report completion after a later attempt starts; an external checking writer. | No durable checkpoint; F2 concerns identity-based ownership. |
| d9 | Local transformation to immutable values; no shared state or lifecycle. | None. |
| e4 | Submission lifecycle and mirrored ticket state with a repair-side writer outside the approved owner. | None; F3 concerns writer/operation ownership. |
| f6 | Explicit local file replacement; subprocess invocation has no domain-state ownership. | File persistence only; no domain reconstruction or invalidation. |
| g1 | Preparation/result initialization shared by two entry paths. | No checkpoint serialization; resume re-enters preparation on raw input. |
| h8 | Owned attempt lifecycle and mirrored observations; copied input/output boundaries. | None. |

The per-case change traces above identify where an approved policy or representation change would belong and which callers/readers would be affected. They do not authorize any change. In an actual ticket/milestone workflow, required broader review, independent axes, finding disposition, current-source revalidation, exact-candidate checks and human QA remain separate obligations under the supplied guidance.

## Evidence audit

1. Read REVIEW.md first, then every case's CONTRACT.md and every source/caller in that directory. Read the supplied ownership, record, checkpoint and report-envelope guidance, plus glossary, ADRs and testing policy. Commands used cat and nl -ba for source inspection.
2. Inventoried with rg --files; corrected the initial hidden-file omission by using rg --files --hidden -a /tmp/development-review-19-c4 | sort. The complete inventory contains 36 files. The three hidden files are the supplied codebase-design, microsoft_oop and test-strategy skill texts. Their contents were hashed for snapshot identity; their Standards-only assessment was not performed by this Spec reviewer.
3. Computed SHA-256 for every inventoried file with sha256sum. Built a mapping keyed by sorted paths relative to the snapshot root, with each value the file's SHA-256; serialized it with default comma/colon spaces and no terminal newline. The resulting retained manifest hashes to bb544f58260e57309be8ffbfb9a2752994b65d8186c899fd7f8ce7e91c33a197, exactly matching the supplied identity. A later parent clarification supplied this enumeration/serialization convention only; it supplied no source changes, classifications or sibling conclusions.
4. The source manifest identifies each contract and supplied guidance file as well as code. A matching manifest establishes the assessed snapshot's content identity. It does not establish correctness, ownership quality, model delivery, test success or integration eligibility.
5. No Python, dependency installation, tests, harness, Git preflight experiment, filesystem/process fault experiment or other runtime scenario was run. The assignment explicitly permits this standalone documentation/source evaluation without those checks. No check result is fabricated. The counterexamples and clean conclusions are source reasoning, with their limits stated above.
6. No snapshot or repository file was modified. The report and identity manifest are disposable outputs outside the snapshot. No sibling was contacted or report consulted, and no broader repository/evaluator/ticket material was read.

## Original result and next action

This Spec assessment is completed for the identified snapshot. F1–F4 remain open blocking findings; there are no optional findings, prior dispositions, verified fixes, deferrals or human risk-acceptance decisions. The responsible implementation workflow should repair each affected case within its approved contract, preserve this original report and full finding keys, and obtain independent verification of the exact repaired source. This report does not mark any finding fixed or grant integration, candidate readiness, milestone acceptance or backend enforcement.

The clean conclusions are limited to the supplied b7, d9, f6 and h8 contracts and inspected flows. Consumer implementations absent from the snapshot were not guessed. Unspecified input policies, hostile custom Python objects, external concurrent interference and additional persistence guarantees were not added as requirements. No unresolved assumption is used to excuse a demonstrated breach of an explicit guarantee.