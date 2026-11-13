# Standards report: development-review-19-g1 / standards-original-01

Assessment complete. Four blocking findings affect a3, c2, e4 and g1. No supported blocking findings were identified in b7, d9, f6 or h8 within the scope and assumptions below. No optional refactors are recommended.

## Report envelope

| Field | Recorded value |
|---|---|
| Assessment | `development-review-19-g1`; eight independent miniature cases |
| Report identity | `standards-original-01`; Standards; original independent assessment |
| Assignment / actor | `/root/implement_19/corpus_standards_g1` |
| Requested settings | `gpt-6.1-sol`, High reasoning, active-context target ≤250000 tokens |
| Actual settings | Backend model selection, reasoning setting, actual context setting and enforcement are unavailable to this reviewer. Requested settings are not delivery evidence. |
| Original baseline | `f2929e79cfd5a68f670862775053ae85ba9582b5`, supplied provenance; no baseline checkout or diff inspected |
| Assessed source | `/tmp/development-review-19-g1` |
| Verified source identity | `ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23` |
| Guidance identity | Frozen G1 files retained inside the snapshot; individual digests below |
| Prior observations / decisions | None supplied or consulted |
| Original output | This complete final report; parent captures it verbatim. No report file was written by this reviewer. |
| Scope | Every supplied source file, caller and contract in all eight cases, plus every supplied guidance file |
| Isolation limits | Reads were confined to this snapshot. No sibling reports, repository source, external ticket/spec passages or other agents were consulted. Ordinary tool access does not prove enforced isolation. |

I applied the supplied ownership-review contract, report envelope, review-record and checkpoint guidance, codebase-design skill, microsoft_oop skill, test-strategy skill, testing policy, glossary and ADRs. The case contracts govern each independent case; requirements were not transferred between cases.

## Substantive assessment

### a3 — Blocking: restoration disconnects the verified view from its owner’s canonical records

**Inspected flow:** `Run.__init__` → `record` → `save` → `restore` → `invalidate`; both QA consumers in `qa.py`.

**Owner and writers:** The contract assigns durable gates and verified references to `Run` (`cases/a3/CONTRACT.md:2–7`). The supplied writers are construction, `record`, restoration and invalidation. `eligible` and `report` are read-only consumers.

Before serialization, `record` creates one gate dictionary and appends that same object to both lists (`cases/a3/run.py:8–11`). `invalidate` changes canonical entries in `gates` (`:13–16`), so the verified view observes invalidation while these references remain shared.

The saved representation contains two arrays (`:18–19`). JSON preserves values rather than Python reference identity. Restoration assigns the independently decoded arrays directly (`:23–26`). Consequently, the restored verified dictionaries are different objects from the restored gate dictionaries.

After the expressly permitted restore-then-invalidate flow, `report` reads the invalidated gate while `eligible` continues reading the unchanged verified dictionary (`cases/a3/qa.py:1–6`). The failure lies in restoration of an owner-maintained invariant, not in either consumer.

**Finding A3-F1 — Blocking**

- **Locations:** `cases/a3/run.py:23–26`; invalidation at `:13–16`; eligibility consumer at `cases/a3/qa.py:1–3`.
- **Approved requirement:** Canonical shared gate records must underpin both views after restoration (`cases/a3/CONTRACT.md:3–6`).
- **Consequence:** Source A can remain QA-eligible after its durable gate has been invalidated.
- **Proportionate remedy:** Reconstruct `verified` using references to the restored canonical `gates` records, retaining the existing JSON keys. In the valid representation produced by this implementation, `record` appends every gate to both lists in the same order, so restoring that correspondence does not require a general persistence framework.
- **Full key:** `development-review-19-g1/standards-original-01/A3-F1`.

A change to gate invalidation policy should remain local to `Run`; teaching QA consumers to compensate for broken restoration would distribute the invariant.

### b7 — Clean within the supplied contract

**Inspected flow:** `caller.preflight` → injected Git callable → `git_ops.validate` and its `checked` helper.

**Owner and collaborators:** `validate` owns preflight decisions. The caller supplies checkout context and selects `expected_branch` and `base`; its injected callable only executes argument lists using captured text output (`cases/b7/caller.py:4–8`).

The implementation keeps related decisions together:

- `checked` rejects nonzero command results (`cases/b7/git_ops.py:4–8`).
- Root resolution occurs at `:10`.
- `symbolic-ref` failure rejects detached HEAD through `checked`; the explicit comparison rejects another branch (`:11–13`).
- Porcelain status includes untracked files (`:14–15`).
- Commit resolution rejects an absent/non-commit base, and the ancestor command rejects a non-ancestor (`:16–17`).

The caller does not reproduce those decisions. This is a useful small interface with cohesive implementation: deleting `validate` would push its policy into callers. Its nested helper and procedural form do not justify a class or validation framework.

There are no record writers, saved representations, restoration paths or invalidation paths. The Git commands are read-only. No finding.

### c2 — Blocking: checking chooses the latest attempt instead of the identified owner

**Inspected flow:** `Execution.start` → `Execution.receive` → checking validation/attachment → `Execution.decision`.

**Owner and writers:** `Execution` maintains ordered history. The contract requires it to locate the identified attempt and ask that owner to attach the validated handoff; checking must validate and return report information without editing shared history (`cases/c2/CONTRACT.md:2–9`).

`start` appends attempts in order (`cases/c2/execution.py:13–14`). `receive` passes the entire mutable history to checking (`:16–17`). Checking validates that the payload names the supplied ID, then writes `history[-1].handoff` irrespective of that ID (`cases/c2/checking.py:6–9`).

For history `[A, B]`, a valid late report for A is attached to B. The consumer reads by ID (`cases/c2/execution.py:19–20`), so A has no decision and B exposes A’s handoff. A syntactically valid payload for an unknown ID also overwrites the latest attempt rather than rejecting without mutation.

**Finding C2-F1 — Blocking**

- **Locations:** `cases/c2/execution.py:16–17`; `cases/c2/checking.py:6–9`; affected consumer `cases/c2/execution.py:19–20`.
- **Approved requirement:** Checking must not choose or edit an attempt; execution must locate the identified owner; unknown IDs must reject without mutation (`cases/c2/CONTRACT.md:5–9`).
- **Consequence:** Ordinary delayed report completion corrupts attempt ownership, and unknown-ID input can mutate an unrelated attempt.
- **Proportionate remedy:** Let checking return validated report information. Have execution resolve the requested ID, reject absence before mutation, and invoke an attachment operation on that attempt. Do not make the checker search and mutate history: that would retain the prohibited responsibility.
- **Full key:** `development-review-19-g1/standards-original-01/C2-F1`.

There is no durable checkpoint or restoration path. Starting a later attempt must not invalidate or redirect earlier report ownership; the current `history[-1]` selection incorrectly does so.

### d9 — Clean within the supplied contract

**Inspected flow:** Entire `plan.py`: frozen `Ticket` values, parsing, identifier indexing and dependency traversal.

The parser owns temporary construction and validation state. Ticket identifiers are trimmed and missing declaration identifiers are rejected (`cases/d9/plan.py:10–14`). Dependencies become ordered tuples, and tickets remain in declaration order (`:15–16`, `:35`). Duplicate ticket IDs are detected through index cardinality (`:17–19`).

The traversal distinguishes the current recursion path from completed work (`:20–32`). A missing dependency rejects at `:22–23`; an edge back into the active path rejects at `:24–25`. Completed dependencies can be reused by other tickets without a false cycle finding. Each declared ticket is visited (`:33–34`).

All mutable collections are local to one parse invocation. The returned tuple contains frozen tickets whose dependency collections are tuples. No external writer, shared lifecycle, saved representation, restoration or invalidation operation is supplied or required. Readiness consumers can consume this immutable result without completing its initialization.

The ordinary functional transformation fits both the contract and the supplied OO guidance. A stateful parser class would add no demonstrated invariant ownership. No finding.

### e4 — Blocking: repair is an additional writer that duplicates the owner’s submission operation

**Inspected flow:** Attempt construction; normal worker entry → `Attempt.submit`; repair entry → direct record writes.

**Owner and permitted operations:** The contract explicitly gives submission and the mirrored current-ticket observation to `Attempt`. Both entry paths must delegate to one owning operation; exposed records are for read-only reporting (`cases/e4/CONTRACT.md:2–8`).

`Attempt.submit` checks running status, then updates revision/status and the ticket’s corresponding fields (`cases/e4/attempt.py:6–13`). The normal worker delegates correctly (`cases/e4/worker.py:1–2`).

Repair instead repeats both the eligibility rule and all five assignments (`cases/e4/repair.py:2–8`). It currently mirrors the owner’s implementation, so I am not claiming an existing difference in those assignments. The supported blocker is the explicitly prohibited writer and duplicated policy.

**Finding E4-F1 — Blocking**

- **Locations:** `cases/e4/repair.py:2–8`; owning operation `cases/e4/attempt.py:6–13`; compliant caller `cases/e4/worker.py:1–2`.
- **Approved requirement:** Submission policy has one owning operation; entry callers delegate; only the owner writes the exposed records (`cases/e4/CONTRACT.md:5–8`).
- **Consequence:** Submission policy must be maintained in two places. A change to the owner’s validation or mirrored observations can leave repair submissions following stale rules or producing inconsistent observations.
- **Proportionate remedy:** Replace the repair entry’s record manipulation with `attempt.submit(revision)`, as the worker entry already does. No new class, hierarchy or state-machine framework is needed.
- **Full key:** `development-review-19-g1/standards-original-01/E4-F1`.

State is in memory. There is no persistence, restoration or concurrency to coordinate. Read-only reporting exposure alone is not a finding; the repair caller’s actual writes are.

### f6 — Clean within the supplied contract

**Inspected flow:** Both complete primitives in `io_ops.py`. No caller file is supplied.

`atomic_write` creates its temporary file in `destination.parent`, placing it on the destination filesystem (`cases/f6/io_ops.py:10–12`). It writes UTF-8 text and exits the file context before replacement (`:13–14`). Thus a write/close exception before replacement does not first overwrite existing destination content. The `finally` block removes a remaining temporary path; after successful replacement, `missing_ok=True` accommodates the path having moved (`:15–17`).

`invoke` passes the supplied argument vector directly to `subprocess.run`, with cwd, captured text output, timeout and `check=False` (`:19–21`). It uses no shell and leaves nonzero exits to callers. It does not catch `TimeoutExpired`.

These functions own local IO mechanics, not run, attempt or review policy. There is no domain record mutation to move into a domain owner. The written file is the only persistence; no reconstruction or approval-invalidation responsibility is supplied. Crash durability, fsync and metadata preservation are explicitly excluded by the contract.

No finding. This conclusion assumes callers supply the documented existing directory and a finite timeout; arbitrary malformed arguments and filesystem failure models beyond the contract were not added as requirements.

### g1 — Blocking: preparation exposes partially initialized results and makes the CLI own derived rules

**Inspected flow:** `prepare` and `Prepared` construction; CLI initialization; resumed configuration entry.

**Owner and writers:** Preparation owns configuration validation and normalization. Both entry paths must receive complete results, and callers must not know derived-field rules or initialization ordering (`cases/g1/CONTRACT.md:2–8`).

`Prepared.__init__` copies the raw mapping but initializes both required derived fields to `None` (`cases/g1/preparation.py:2–5`). `prepare` checks only whether selection is truthy, then returns that incomplete result (`:7–10`).

The CLI finishes initialization by deduplicating selection, converting/defaulting the repair limit, and validating positivity (`cases/g1/cli.py:4–8`). Resumed configuration returns `prepare(raw)` directly (`cases/g1/resume.py:3–4`).

Consequently, callers encounter different readiness and rejection behavior depending on entry path. A resumed configuration with nonempty selection returns `selected=None` and `repair_limit=None`; an invalid repair limit is not rejected during preparation.

**Finding G1-F1 — Blocking**

- **Locations:** `cases/g1/preparation.py:2–10`; caller-owned initialization at `cases/g1/cli.py:4–8`; incomplete resumed return at `cases/g1/resume.py:3–4`.
- **Approved requirement:** Both entry paths return complete prepared state, with unique ordered membership and a positive repair limit defaulting to 2; invalid limits reject during preparation (`cases/g1/CONTRACT.md:2–8`).
- **Consequence:** Resumed execution receives unusable derived fields and deferred invalid configuration, while every additional caller must learn a hidden initialization protocol.
- **Proportionate remedy:** Perform normalization, defaulting, conversion and positivity validation inside preparation before returning a complete `Prepared`. Both entry functions should delegate to that operation. Retain the raw-copy behavior and avoid mutating input.
- **Full key:** `development-review-19-g1/standards-original-01/G1-F1`.

There is no checkpoint serialization. The resumed entry receives raw configuration; it does not establish a separate approved restoration model that would excuse incomplete initialization.

### h8 — Clean for the supplied operation flow, with value-type assumption recorded

**Inspected flow:** Construction → submit → complete → snapshot; all transition and rejection branches.

`Attempt` owns a real coupled invariant. Construction creates consistent record/current dictionaries (`cases/h8/attempt.py:2–4`). Submission checks both state and nonempty revision before mutation (`:6–9`); completion checks submitted state before mutation (`:11–14`). Both use `_transition`, which constructs the updated record and its mirrored current observation (`:16–19`).

Invalid operations raise before either view changes. The caller requests operations and returns snapshots without touching records (`cases/h8/caller.py:3–7`). `snapshot` copies both top-level dictionaries (`cases/h8/attempt.py:21–22`), preventing consumers from replacing their status or revision fields through returned record dictionaries.

This small class earns its interface: it hides transition ordering and mirrored writes from callers. Moving the decisions into `execute`, adding setters or introducing a generic framework would weaken or complicate that ownership.

There is no persistence, restoration or concurrency. Valid later operations replace both observations together; no separate cache invalidation path is needed.

**Assumption and limit:** Identifiers and revisions are treated as ordinary immutable domain values. Their accepted Python types are not explicitly declared. The copies are shallow, so this assessment does not establish isolation for arbitrary nested mutable objects supplied as an identifier or revision. No such input flow is supplied. If the contract intends arbitrary dictionary-valued identifiers/revisions, that interpretation needs clarification and the shallow-copy conclusion needs reassessment. I have not converted that unspecified input interpretation into a blocker.

## Scope, assumptions and omissions

- All 36 supplied files were inspected. Every executable case file and supplied caller was read in full.
- Cases are independent. No runtime package, production callers or requirements from another case were inferred.
- External links whose targets were absent from the snapshot were not followed. These include domain guidance, Python environment guidance, harness commands, TDD/deepening/design alternatives, additional record templates and tracker/ticket material. Their absence does not authorize repository reads.
- No Python, dependency installation, harness, production tests or synthetic execution were run. The assignment expressly permits a standalone source assessment and forbids a harness run. No executable files or tests were changed.
- No test suite, coverage map or prior check evidence was supplied. There is therefore no evidence for claims about runtime pass rates, redundancy, fixture cost or test reliability. Missing production test execution is not classified as a blocker for this assessment.
- Input values are assessed within their stated domain roles, rather than against arbitrary Python objects. The material h8 shallow-copy limitation is recorded explicitly above.
- No prior findings, dispositions, repairs, human decisions or milestone acceptance evidence were supplied. This report makes none.
- Checkpoint guidance informs the breadth of ownership inspection. This miniature assessment does not establish real ticket integration eligibility or milestone readiness.

## Evidence audit

All commands ran with working directory `/tmp/development-review-19-g1`.

1. `cat REVIEW.md` established the supplied assessment instructions.
2. `rg --files -g '*'` inventoried the snapshot, including hidden guidance directories.
3. `nl -ba`, `cat` and bounded `sed -n` reads inspected every listed file. Large combined guidance output was supplemented with bounded rereads of the design skills, record tail and full checkpoint contract.
4. `sha256sum` produced individual file digests over the sorted inventory.
5. Aggregate hashing independently reproduced the supplied source identity. The matching representation is a JSON object mapping relative paths to their SHA-256 digests, with paths sorted using `LC_ALL=C`, separators `", "` and `": "`, and no terminal newline:
   `ebf72b6255ad6c2c6365990f4479c11ddfc52113d13b57f02a4c584119401c23`.
6. Two alternative encodings were also observed: tab-separated lines yielded `6edc596b96076fa9e479b6217a2109504f96bfb2f12af33416e3d963b7f8915b`; compact JSON yielded `bac46bc59ae4de991852e60c0f7edda9dfc4d6213ada8f97b5b3683fa0185312`. These are encoding differences, not source discrepancies.

The matching aggregate proves correspondence to the supplied content identity under that serialization. It does not prove correctness, baseline provenance, backend settings or enforced isolation. Findings above are based on source and contract reasoning, not hash agreement.

### Complete inspected-file manifest

Paths are relative to `/tmp/development-review-19-g1`. Digests are SHA-256.

```text
REVIEW.md
  8e37866b20decc67802e6e5d65a2a1cf469505ead6cde6c930adce387e828310
cases/a3/CONTRACT.md
  86ae2893359f38a9242200c1e444169053653149431e957993f419fe2805ba49
cases/a3/qa.py
  3e847eb9d49c0f801c897e31172ab8a3aa7a8fec1bb39791affc43b71c44d3e3
cases/a3/run.py
  f74ad5e6516582a51b0df51c3cf3c9895ca0372bfb493faa565d40fb4f75987b
cases/b7/CONTRACT.md
  a8cb890bbac9e40b5b0e7a409e89899ad878943bc0198f81d10e7157dce701f4
cases/b7/caller.py
  1fcd0c97ab007c142d687910d6d93f4a9665338cb6780d8ec63e9a6a671f18d7
cases/b7/git_ops.py
  28378efa194e419dac686c298cc8577bffbc7409dddd2ef6c8d746b6a291ccda
cases/c2/CONTRACT.md
  1f4f63540674fa6cd9dd279f641d4dccce8c0b8cb3f20114ee115adc43e1640f
cases/c2/checking.py
  7e72511e7644a34c0a438cc6bd02dec3fdee78812424913ee05bc7723ab55d42
cases/c2/execution.py
  20fafa2092522e8d30372c80ec54a20e710e44f0e1f8b23b6039f24fd694230e
cases/d9/CONTRACT.md
  18aa280aab8b202636580bcbfcfc34cd3ff5901c57b2f499e4ba06fa6303ecec
cases/d9/plan.py
  04d5ade095ebfc947f8b769b4d1db409d92787aa81c8b4424b41e0beb295c3a9
cases/e4/CONTRACT.md
  5363f847f3397e013d5a0bdc54a7f40e11a3fb498dfe4b5bc42566bd66591c32
cases/e4/attempt.py
  3ca2f272b86e8bb2742691872917be4fef815344e030716e46e70c07743c22c7
cases/e4/repair.py
  dd2d751350b88db2adc49b63bde1b8ff47cdef07bf64fedea754c1fd1470cb9c
cases/e4/worker.py
  bafed6633fd5879fd43da4cb010204e77cb30c70c8f1027f7f194b998a654f2c
cases/f6/CONTRACT.md
  82b5d53b1ac036441f4a7f367655a11e9a408b55351439fbb31661aa31fe11b1
cases/f6/io_ops.py
  ae3bd8b46ed253896dc4cf662fbd64dade68cea16a24d82f81d8bc94f2d6a9b0
cases/g1/CONTRACT.md
  3bb604e93fe600fb914497cc091618c2dc6d4bb5d6af8f5950b5f52e5ebe9b73
cases/g1/cli.py
  4f902d5fb4a997fe8a1e18f1977ee689f2606bf9df6ece37949db8c3031b99af
cases/g1/preparation.py
  5def9b498f24bbab4f1cf4e02398c8d94ade995911243e21ca73a1970ac71bb0
cases/g1/resume.py
  e91ae0907e36ee9de97edb1f1e9ed32a12b70f30c65ac0600f09f5a56e763c9a
cases/h8/CONTRACT.md
  fc6dff5ba70d3e8dd747e564dda85e9e7569465670b8686b7a8f881b1224b666
cases/h8/attempt.py
  f001a6ec434251e1dbd649ad383474ec795022b3397ca226fab3dce8b14676a3
cases/h8/caller.py
  8c7a89afa9f83a3a89c80832f7e274b96280a08a2f2c28483772ba361d2a2c1c
guidance/.agents/skills/custom/test-strategy/SKILL.md
  3a0a0f667aaa65ae8a74b2c7f3ab0e24517e756ed1a5663f35623bc46c8fc816
guidance/.agents/skills/matt-pocock/codebase-design/SKILL.md
  2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2
guidance/.agents/skills/microsoft/microsoft_oop/SKILL.md
  7d9fb19811bc83bffa964746e70e1b85757773576b5a5373ffa6edbd8ae5e481
guidance/GLOSSARY.md
  4b45856348181d3383d3b2416d56eb0261243ddab8507fb869dd4bdee39bdefc
guidance/docs/adr/0001-reusable-harness-and-local-integration.md
  6e4adc64a9a454d00ca4d16649796daf525783e554d1dc892bd0654b5990e603
guidance/docs/adr/0002-human-qa-gates-feature-promotion.md
  7f9ef955940b6a4315d9a5fc7c7279cc367043310ebd4575cee450dffd0e4982
guidance/docs/agents/architecture-checkpoints.md
  e81bfaff325e069ee3b8c73a8a4d2028e06a871dcf94f6045377585a5d1e3d8f
guidance/docs/agents/ownership-review.md
  7bef209024464c7ce7b0d3ebcfc8f2707d2309efef50b79bb7d5cc589ab1aa56
guidance/docs/agents/review-records.md
  7371c706ba48a09ba2f69750dab8f60c5c6892bdfb0ecb35f5f9ada7e502d49d
guidance/docs/agents/testing.md
  6b6b498a718205bb5fd1f0b12410623807e708f784e7d09a4bd72343b229a4ff
guidance/docs/templates/reviews/report.md
  bb0c4613964f1dc60f4ee7a618119997cf96ac3fafc3b810ed95002b2f787e76
```

## Assessment result

The defined source assessment is complete. A3-F1, C2-F1, E4-F1 and G1-F1 remain open blocking findings against this exact snapshot. No fixes, independent fix verification, dispositions or human risk decisions occurred during this assessment. The clean conclusions for the other cases are limited to the inspected contracts, flows and recorded assumptions.