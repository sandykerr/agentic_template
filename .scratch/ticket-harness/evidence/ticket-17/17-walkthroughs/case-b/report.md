# Case B — independent Standards report

**Result:** blocking findings F1 and F2; the scoped change does not satisfy the approved restored-state contract. Review lifecycle: completed. Findings remain open; no repair, independent repair verification, human risk acceptance, or integration decision is recorded by this report.

## Identity and limits

- Review ID: `walkthrough-case-b`; report ID: `standards-01`; assignment: `/root/implement_17/walkthrough_b`.
- Repository: `/tmp/ticket17-walkthroughs/case-b` only.
- Fixed original baseline: `7bfdd3366171d7c7de6abccf3f07a4a8fb48efa5`.
- Exact assessed candidate/observed HEAD: `ef95dd524dfb2b7e6084ddf402b35010b37b83d7`.
- Axis: fresh independent Standards assessment of the whole scoped ticket and relevant collaborators, not the surrounding harness implementation.
- Parent confirmed actual spawn arguments: `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. These are parent-configured assignment settings; provider/backend delivery telemetry is unavailable to this reviewer. Active-context target: at most 250,000 tokens; actual active-context usage/peak is unavailable. No claim of backend measurement is made.
- Only the three supplied frozen guidance texts and isolated repository were used. Parent repository, other cases, sibling reports, and sibling discussions were not accessed. No prior finding reports were supplied or consulted.
- The supplied snapshot links were explicitly unnecessary for this assignment. No external linked domain documents, report templates, skill resources, or tracker records were accessed. The isolated tree has no `AGENTS.md`, domain/testing guidance, package metadata, or tests. No source or test was changed and no Python, dependency installation, or runtime test was run.
- This is an original report with substantive review rationale and source observations. It records conclusions and their supporting reasoning, not private internal chain-of-thought. No later aggregation has altered it.

## Instruction and input identities

SHA-256 values were read with `sha256sum`; paths identify the actual supplied content, rather than the differently named destinations of links within the snapshots.

| Input | SHA-256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` (Codebase Design) | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |
| `/tmp/ticket17-walkthroughs/case-b/CONTRACT.md` | `e5043a12fe73dd2768ae5ab44622c182f2ba183590aa35785479f1750e70fbc4` |
| `/tmp/ticket17-walkthroughs/case-b/gates.js` | `7b2c985536fe4065040e157993d540fbd7f524b37786e547668efaa669bdd02e` |
| `/tmp/ticket17-walkthroughs/case-b/checkpoint.js` | `a3a5b5e6350533cadf0539d5f7bb3bbc49fb3f1083433f9a4b1fd5abf1a530b0` |

The originating assignment is the parent task message, with the model-setting confirmation supplied separately by the parent. Those messages have no locally supplied immutable snapshot/digest; this report does not invent one. The contract is unchanged between baseline and candidate. No human amendment or approval beyond the supplied approved contract was observed.

## Inspected scope and substantive review notes

All three tracked files at the baseline and candidate were inspected in full. The entire ticket diff adds only `Gates.replaceSource` in `gates.js:11–13`. The inspection followed unchanged collaborators because the new operation must invalidate evidence visible to verified consumers after restoration.

| Flow | Inspected source | Assessment |
| --- | --- | --- |
| Initialization and record creation | `gates.js:2–6` | `record` initializes validity and returns the exact object added to owner records. A verified consumer holding that returned object can observe later owner invalidation. |
| Source replacement and invalidation | `gates.js:8–13` | The new method delegates to the existing owner operation. Every record whose source differs is set invalid; matching-source records are left unchanged. The delegation itself is appropriately small and keeps the invalidation decision in Gates. |
| Saved representation | `checkpoint.js:2–4` | Saves records and verified IDs under the existing `gates` and `verifiedIds` keys. No shape change occurs in this diff. A JSON round trip is the relevant persisted representation described by the contract; no disk adapter is present. |
| Restoration, including identity | `checkpoint.js:5–8` | Creates owner records, then creates separate spread copies for verified references. This separates the validity read by consumers from the validity written by the owner (F1). |
| Restoration failure | `checkpoint.js:7–8` | Looks up IDs without checking the result. An unresolved ID is spread into an empty object and restoration returns normally (F2). |
| Consumer readiness | `checkpoint.js:10` | Reads only the verified objects' `valid` properties; it does not consult owner records. This makes the restored-object separation consequential. |

Definitions and all usages in the complete tracked tree were searched. There are no further entry callers, writers, consumers, persistence adapters, or invalidation operations in the supplied source. Public exported functions are the available entry points; unseen integrations are outside the evidence. No whole-product or whole-codebase approval is claimed.

The affected state contract is explicit: Gates owns durable records and validity; verified objects must be canonical, including after restoration; source changes must reach all verified consumers; unresolved IDs must reject restoration; checkpoint shape must remain compatible. The candidate preserves owner delegation and serialization shape, but unchanged restoration defeats the promised behavior. These are contract-based findings, not preferences about classes, method count, function length, or file layout. A small interface can have good depth here when it hides canonical lookup and invalidation; callers should not need to repair references or coordinate invalidation themselves.

Omitted: real filesystem persistence, concurrency, external input schemas, external callers, harness scheduling, broader architectural gates, and other cases. None is present in the supplied tree or needed to establish these findings. The contract does not define ID uniqueness, every malformed-checkpoint schema case, or the error type/message; this review does not invent those requirements. No runtime execution confirms the examples below; they are direct traces of the inspected JavaScript operations.

## Findings

### F1 — blocking: restored verified consumers retain stale validity after source replacement

**Key:** `walkthrough-case-b/standards-01/F1`. **Status:** open.

**Contract:** `CONTRACT.md:2–5` requires the verified reference to be the same canonical object as its gate record after restoration, and every verified consumer to observe source invalidation. `CONTRACT.md:8–9` scopes `replaceSource` through the existing owner while preserving readiness behavior.

**Evidence:** `checkpoint.js:6` creates the records held by Gates. At `checkpoint.js:7`, the spread surrounding `gates.records.find(...)` produces another object, even when the lookup succeeds. `gates.js:9` and the new `gates.js:11–12` mutate only the owner records. `checkpoint.js:10` reads the detached verified copies.

**Concrete trace:** Start with saved JSON `{ gates: [{ id: 'g1', source: 'old', valid: true }], verifiedIds: ['g1'] }`. Restoration produces one owner record and one separate verified object, each initially valid. Calling the restored owner's `replaceSource('new')` sets the owner record's validity to false. The verified object remains true, so `ready(restored.verified)` remains true. Even before invalidation, the contract's required object identity is already false.

**Consequence:** readiness can continue to accept evidence from an old source following checkpoint restoration. Gates cannot maintain its approved invariant for those consumers without external coordination, despite correct invalidation inside the newly added method. This defect predates the diff but directly defeats the ticket's approved source-replacement outcome, so it is in scope and blocking under the supplied ownership guidance.

**Proportionate remedy:** restore verified entries as the canonical restored Gates records, using checked ID resolution rather than copies, while retaining the existing checkpoint JSON shape. Keep the owner as the validity writer; do not require callers to synchronize detached copies. Verify both object identity after a round trip and readiness becoming false after replacing the restored source. This recommendation authorizes no edits in this read-only assignment and proposes no new owner or contract amendment.

### F2 — blocking: restoration does not reject a missing verified ID

**Key:** `walkthrough-case-b/standards-01/F2`. **Status:** open.

**Contract:** `CONTRACT.md:6–7` explicitly requires invalid/missing gate IDs to reject restoration.

**Evidence:** `checkpoint.js:7` has no validation after `find`. For `{ gates: [], verifiedIds: ['missing'] }`, `find` returns `undefined`; JavaScript object spread over that result creates `{}`. At `checkpoint.js:8`, restoration returns `{ gates, verified: [{}] }` normally. There is no rejection path or failure result for the missing reference. The same unchecked restoration also returns a reference to an existing record whose validity is false; no separate validity validation occurs.

**Consequence:** callers receive an apparently restored state with an unresolved verified reference, contrary to the approved failure behavior. For the missing-ID example, `ready` currently evaluates to a falsy value rather than true; the observed breach is acceptance of restoration, not a claim that this particular malformed input already establishes readiness. F1 independently demonstrates incorrect readiness for a valid saved reference after source change.

**Proportionate remedy:** explicitly reject an unresolved verified ID before exposing a restored result, and implement any approved invalid-ID checks at the same resolution step. Preserve the saved key/array shape. The contract does not prescribe exception class or text, so those remain routine implementation choices. Verify rejection for a missing reference; no broad new checkpoint schema or neighboring refactor is needed.

F1 and F2 share a lookup line but cover different obligations: F1 needs canonical identity for a successful resolution; F2 needs rejection when resolution fails. Both must be checked after any repair. No optional style findings are raised.

## Mechanical evidence audit

This section establishes source identity and inspection coverage separately from the design conclusions above.

- `git rev-parse HEAD` returned `ef95dd524dfb2b7e6084ddf402b35010b37b83d7`.
- `git status --short` and final `git status --porcelain=v1` returned no entries. The working tree was clean during inspection.
- `git ls-tree -r --name-only ef95dd524dfb2b7e6084ddf402b35010b37b83d7` listed exactly `CONTRACT.md`, `checkpoint.js`, and `gates.js`.
- `git diff 7bfdd3366171d7c7de6abccf3f07a4a8fb48efa5 ef95dd524dfb2b7e6084ddf402b35010b37b83d7 --` showed only the three-line `replaceSource` addition to `gates.js`. The baseline was not moved.
- `git show <baseline>:CONTRACT.md`, `:gates.js`, and `:checkpoint.js` established that the contract and restoration defects are already present in the baseline. Candidate files were read in full with line numbers.
- `rg -n 'Gates|record|valid|verified|save|restore|ready|replaceSource|invalidate' CONTRACT.md gates.js checkpoint.js` enumerated the relevant definitions, writers and consumers; each was traced in the substantive assessment.
- `sha256sum` produced the input/content identities recorded above.
- `git diff --check <baseline> <candidate>` exited successfully with no output. That is whitespace evidence only.
- No runtime test or repository test suite was run, and no test result is claimed. Static tracing is sufficient to identify the separate object allocations and missing rejection; runtime/platform behavior and external integrations remain unobserved.

The only written artifact is this report, outside the isolated source repository. Its own digest is intentionally not embedded in itself. Any later disposition, repair, or revalidation must preserve this original report and identify both full finding keys and the exact new source. No consequential human decision is needed to understand these findings; no such decision has been inferred or fabricated. Repair authority and eventual integration eligibility must be handled by the parent workflow.
