> Readable display of the original report. Only Markdown trailing spaces were
> normalized for the Git whitespace check; semantic content is unchanged.
> [Exact raw output](report.raw.md.gz) is retained byte-for-byte after decompression;
> original SHA-256: `05d5d9b7a0cc53bf1d00bd694370834b174dcd6c8d83abbedaf49b592b0f8517`.

# Case D: original independent Standards review

Review ID: `walkthrough-case-d`
Report ID: `standards-01`
Assignment: `/root/implement_17/walkthrough_d`
Axis: Standards development review
Lifecycle: completed for this assignment; one unresolved blocking finding
Date: 2026-11-10

## Assignment and identity

Reviewed only the isolated Git repository `/tmp/ticket17-walkthroughs/case-d` and the three supplied frozen guidance texts. Fixed original baseline: `49ae60016d513a35c22f7139994da144929cdf88`. Exact assessed candidate: `8647da4cd28a01ea060027df087554df3bf73161`, also the observed `HEAD`. The worktree was clean before and after the read-only inspection and runtime probes. The complete baseline-to-candidate diff changes only `validator.js`: 79 additions and one deletion, replacing the unimplemented operation. `CONTRACT.md` and `cli.js` are unchanged.

Fresh assignment settings were explicitly requested as `gpt-6.1-sol`, High reasoning, active context target at most 250,000 tokens. The assigning parent reported its actual spawn arguments as `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. Those are observed parent-configured settings, not provider/backend telemetry. Backend delivery, actual reasoning configuration, and active-context token measurements are unavailable to this reviewer. This is a fresh independent source assessment; no sibling reports, other cases, parent repository, or discussions were read. The parent's configuration message was administrative metadata, not another assessment.

The approved scoped request and ownership contract are `CONTRACT.md:2-11`: implement the missing public pure `validatePlan` behind the existing caller; own scratch state per call; preserve raw input; return accumulated failures or an independently normalized successful plan. No class/file arrangement is prescribed. No prior finding keys, repair source, approved amendment, human decision, or pre-existing check records were supplied. This report records observations; it grants no integration or human QA approval.

### Instruction identities

Supplied instruction text and contract SHA256 values:

| Path | SHA256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |
| `/tmp/ticket17-walkthroughs/case-d/CONTRACT.md` | `a3eaf6f98273016ec553632ebbc6842c95a275e80eec49b95424717e4ea3fb59` |

Applied the supplied codebase-design vocabulary and ownership/review record requirements directly. Referenced but unsupplied guidance/templates were not fetched: the assignment explicitly makes these three frozen texts and isolated source the supplied context. The isolated Git tree contains exactly `CONTRACT.md`, `cli.js`, and `validator.js`; no repository-local AGENTS, domain, Python, or testing documents exist in that tree. No Python, dependency installation, source edits, or added test files were used. The report is the only written artifact.

## Inspected and omitted scope

Read every line of all three isolated files at the candidate, the complete implementation diff, and the baseline validator and caller. Traced these affected flows:

- `cli.js:2-5`: public `prepare(raw)` invokes validation, returns exit `2` with errors on rejection, and exit `0` with the normalized value on success. It performs no independent content validation.
- `validator.js:2-14`: root checks and per-call initialization of errors, ID set, and normalized tickets.
- `validator.js:15-52`: every ticket field read, duplicate-ID handling, optional dependency default, acceptance validation, and construction of independent ticket/dependency/acceptance data.
- `validator.js:53-73`: graph construction, dependency readers, unknown/self/duplicate dependency handling, and call-local visiting/done sets for cycle detection.
- `validator.js:74-78`: success/failure publication, including the copied output that the unchanged caller exposes.
- Initialization, all relevant writers, and invalidation: scratch sets/arrays are created inside `validatePlan`; only that invocation mutates them; they become unreachable after the invocation except the normalized output intentionally returned. There is no durable representation, restoration path, shared identity requirement, or persistent invalidation operation in the supplied source or approved contract.

Omitted: other cases and the parent project (explicit assignment exclusion); harness implementation (explicit exclusion); nonexistent storage/recovery consumers; unavailable test suites and linked resources; third-party production integrations; adversarial getters/proxies, performance/load limits, and unbounded graph-depth behavior. No claim of whole-codebase or exhaustive JavaScript-input review is made.

Assumptions/limits: the two supported status spellings are inferred from `validator.js:30` (`ready-for-agent`, `needs-info`), because the supplied contract specifies their number but does not list their names. No independent source for those spellings was supplied. The contract does not restrict the public `raw` input to JSON-decoded data or require dense arrays. The finding below therefore uses an ordinary JavaScript object passed directly through the supplied public caller; accepting only JSON-produced dense arrays would be an additional contract restriction, not an approval this reviewer may invent. Exact diagnostic text and exhaustive reporting of every independent error on malformed tickets are not specified; early skips are not separately reported as defects.

## Substantive assessment and review rationale

The overall responsibility placement is appropriate. `validatePlan` is a deep module with one small external interface: callers pass a raw plan and inspect a discriminated result. Root/field checks, identity collection, normalized copying, reference checks, and graph traversal are cohesive parts of this one operation. Its internal `visit` helper owns traversal state through the enclosing invocation; callers do not coordinate traversal or validation ordering. Creating a class or dividing the operation into files would not itself fix an identified coordination problem. The function's length is not a finding.

For the ordinary dense-array inputs inspected, local ownership and isolation hold: the graph points to arrays already copied into the local normalized tickets, the input arrays are not mutated, primitives are copied by value, and failure does not publish partial normalized state. The caller correctly relies on the single owner to decide success. Local `done`/`visiting` sets implement the necessary traversal ordering without shared mutable state. Optional dependencies become independent empty arrays. Duplicate IDs and dependencies, missing targets, self edges, and cycles feed the common error result.

There is nevertheless one concrete acceptance-invariant breach at the owner's validation/copy seam. The input check and output construction disagree about sparse acceptance arrays, letting a success result contain a non-string acceptance entry. Because `prepare` trusts this success result, this is observable through the unchanged collaborator rather than a merely internal representation concern.

### F1 — sparse acceptance array is accepted and normalized to an invalid entry

Full key: `walkthrough-case-d/standards-01/F1`
Classification: **blocking**, narrow correctness/contract defect
Disposition: **open**; authorized repair remains implementation of the existing validation contract, with independent exact-source revalidation pending. No human decision, repair commit, or verification of a repaired source exists.

**Contract:** `CONTRACT.md:4` requires nonempty acceptance strings; `CONTRACT.md:6-7` requires normalized independent acceptance arrays on success. The public pure operation is defined at `CONTRACT.md:2`, and no dense-array/JSON restriction is stated.

**Code:** `validator.js:41-43` rejects an empty array or entries found by `ticket.acceptance.some(...)`. JavaScript `.some()` skips absent array slots. A one-slot hole therefore has nonzero length and supplies no value to the predicate. `validator.js:50` subsequently spreads the array, materializing that hole as `undefined`. There are no remaining errors, so `validator.js:74-77` publishes success. `cli.js:4-5` then returns exit `0` and that value.

**Concrete reproduction against the exact candidate:**

```js
const raw = {
  version: 'v1',
  tickets: [{
    id: 'a', title: 'A', status: 'ready-for-agent',
    dependencies: [], acceptance: Array(1),
  }],
};
const result = validatePlan(raw);
// Observed: result.ok === true
// Observed: result.value.tickets[0].acceptance.length === 1
// Observed: result.value.tickets[0].acceptance[0] === undefined
// Observed: Object.hasOwn(result.value.tickets[0].acceptance, 0) === true
// Observed: Object.hasOwn(raw.tickets[0].acceptance, 0) === false
// Observed: prepare(raw).exit === 0
```

All six observations were asserted in an executed Node probe. JSON output displays the returned `undefined` entry as `null`; the direct assertion above establishes that its actual in-memory value is `undefined`. The raw input remains unmodified, so this concerns validation of published output rather than input mutation.

**Consequence:** a ticket with no actual acceptance requirement is admitted as a successful prepared plan, violating the invariant the caller delegates to this owner. The defect applies to direct JavaScript inputs with sparse acceptance arrays; ordinary JSON parsing cannot produce this hole, and no such production input path beyond the supplied direct caller was established.

**Proportionate remedy:** validate each logical acceptance position, including holes, before success—for example, use a local iteration that visits every index/value, or validate a densely copied acceptance array. Retain the existing owner, result shape, independent copies, and accumulated-error behavior. A focused rejection check for this input is sufficient to verify the repair alongside the affected ordinary success path. No new owner, class, persistence scheme, or scope expansion is proposed. If the intended domain is exclusively JSON-produced dense arrays, that restriction needs actual authoritative contract evidence; it is absent here.

No optional layout findings are raised. Empty additional findings do not attest to uninspected input classes or production integrations.

## Mechanical evidence audit

Identity/source commands run in `/tmp/ticket17-walkthroughs/case-d`:

- `git status --short`, `git rev-parse HEAD`, `git log -2 --oneline`.
- `git diff --stat <baseline> <candidate>`, `git diff <baseline> <candidate> -- validator.js`, `git ls-tree -r --name-only <candidate>`.
- `git show <baseline>:validator.js`, `git show <baseline>:cli.js`.
- `nl -ba CONTRACT.md`, `nl -ba cli.js`, `nl -ba validator.js`; full reads of all supplied guidance; `sha256sum` of contract/guidance/source.

Observed source SHA256 values:

| Candidate file | SHA256 |
| --- | --- |
| `cli.js` | `0433e43678cd9b88e030f67f2c52201d86c0643d9383a908c143340f09e45bf0` |
| `validator.js` | `0f9a4407567f042990dd0a0ae80ab844f269a09b26bb93539b07d5352b5351b6` |

Runtime: `node --version` returned `v24.22.0`. Two `node --input-type=module` stdin probes used only built-in `node:assert/strict` and the two local modules; both exited `0`. No suite exists in the supplied tree, and these are reviewer probes, not a claim of required CI completion.

The first probe passed frozen-input preservation, output ticket/array identity separation, safe mutation of returned acceptance without changing input, repeat-call independence, omitted-dependency defaulting, both status spellings, caller success/failure mapping, and 17 rejection cases: invalid root/version/ticket shape/ID/title/status, empty/blank/non-string acceptance, non-string dependencies, duplicate ID/dependency, unknown/self dependency, and a three-ticket cycle. A mixed-invalid plan returned the five observed diagnostics for missing version/title, invalid status, empty acceptance, and unknown dependency. That probe then printed the sparse-input success. The second probe directly asserted the six F1 observations, including the materialized undefined value and unchanged raw hole, and confirmed the worktree remained clean.

These observations support their specific input cases only. Passing probes and matching digests do not establish the design conclusion; the responsibility assessment above follows the actual call/data flow and approved contract. The source remains the original assessed candidate. No repair or human decision was created, and the outstanding finding requires disposition/revalidation by the responsible follow-up assignment.
