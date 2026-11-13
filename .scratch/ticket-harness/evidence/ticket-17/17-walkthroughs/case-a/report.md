# Case A — original Standards report

Result: **one blocking finding** in the unchanged urgent submission collaborator. The added cancellation operation satisfies the express scoped writer exception on the inspected valid-capacity state. This is a completed, source-only Standards assessment of the supplied miniature, not an assessment of the ticket harness implementation or a claim of integration or human QA approval.

## Assignment and source identity

- Review ID: `review-ticket17-guidance-case-a`.
- Report ID: `standards-01`; assignment: `/root/implement_17/walkthrough_a`.
- Repository inspected: `/tmp/ticket17-walkthroughs/case-a` only.
- Fixed original baseline: `aa657d7d9496ad25817589bf247501300035a166` (tree `4d913fb11a5984765a620b5cfcca8c5dd14eff1c`).
- Exact assessed committed source: `fb10adac08f6b9661b5bf65029360c4b44923d07` (tree `4f2cb1edf9bf767070dbd1cb0c14326847b7db99`). HEAD matched this candidate and the working tree was clean.
- Fresh assignment settings: the parent confirmed the actual spawn arguments were `fork_turns=none`, `model=gpt-6.1-sol`, `reasoning_effort=high`. These are parent-configured assignment settings, not independently observed provider/backend delivery telemetry. Backend/model delivery telemetry and actual active-context usage were unavailable. The assignment target was at most 250,000 active context tokens; no measured usage or enforced context cap is claimed.
- Supplied prior finding keys, check records, human decisions, repair records and sibling reports: none. No parent repository, other case, sibling report or discussion was accessed. The parent's settings confirmation above concerned assignment configuration only.

## Instruction and contract identities

The task supplied the isolated source and these frozen guidance texts as the applicable context; their linked resources were explicitly not required. I read all three and applied their ownership, record-preservation and deep-module principles. I did not follow links into the parent repository. No repository-local `AGENTS.md` was present among the supplied case files.

| Input path | SHA256 |
| --- | --- |
| `/tmp/ticket17-walkthroughs/guidance/1-ownership-review.md` | `9b76eb5e2b89a4bc6fb5ec07e091321158ff8a628ec70dac257229a8d6098f4d` |
| `/tmp/ticket17-walkthroughs/guidance/2-review-records.md` | `71eff72da027b67a9dc0652bac589d56539678b8405ea48c6435e03229cf480c` |
| `/tmp/ticket17-walkthroughs/guidance/3-SKILL.md` | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` |
| `/tmp/ticket17-walkthroughs/case-a/CONTRACT.md` | `9fa80f8160a2c69038f799d18fd35c172a95cf9252a9a52416ebbdccfed1e604` |
| `/tmp/ticket17-walkthroughs/case-a/capacity.js` | `5507802f6cc9f8dd12e4e12b77343598297fbbbfe903088bd78fa6567c442bc4` |
| `/tmp/ticket17-walkthroughs/case-a/submission.js` | `0d2a8a9c20f7bdeec95b30ad3f0abd7ae9591baffca888b1ffbb95f071017d77` |

The originating task text is retained in this assignment's conversation; it is not a separately supplied file with a file digest. The scope and approved ownership contract are both in `CONTRACT.md`, unchanged from the baseline.

## Inspected and omitted scope

I read every tracked source/contract file at the candidate, the complete baseline-to-candidate diff, and the baseline versions of all three files. The only changed code is `Capacity.cancel` in `capacity.js:8-12`.

The affected flow inspection covered:

- Initialization: `capacity.js:2` writes the initial remaining value.
- Owner operations: reservation validation, capacity comparison, mutation and success/failure at `capacity.js:3-7`; cancellation validation, mutation and success/failure at `capacity.js:8-12`.
- Entry callers and consumers: ordinary submission at `submission.js:1-4` and urgent submission at `submission.js:5-8`, including use of `job.units`, result shapes and all reads/writes of `remaining` in the supplied source.
- Persistence/restoration: `CONTRACT.md:6` explicitly says there is no durable representation or restoration path; none is present in either source file.
- Invalidation/recovery: no invalidation, cache, saved references, asynchronous handoff or recovery operation appears in the supplied source. No such operation is inferred.

Omitted: repository Git internals beyond identity/status/tree inspection; external callers or infrastructure not supplied in this miniature; runtime execution and tests; the parent repository, other cases and linked resources, as required by the assignment. The complete supplied source is small enough to inspect, but that does not establish facts about external code.

## Substantive assessment and original review rationale

`CONTRACT.md:2-5` gives Capacity responsibility for available units, requires nonnegative remaining capacity, and makes reservation validation/mutation one owner operation. Lines 7-9 expressly authorize cancellation as an additional writer and require rejection of nonpositive or noninteger cancellation amounts without mutation. I interpret the specific cancellation exception as amending the earlier reserve-only rule; it does not authorize unrelated writers.

For ordinary submission, the caller supplies `job.units` to `reserve` and reacts to its boolean result. The caller need not duplicate the positive-integer or sufficient-capacity rules. `reserve` returns before mutation on rejection. For cancellation, the new method likewise validates before its one mutation and returns a boolean. Starting from valid nonnegative numeric capacity, a positive integer cancellation cannot make capacity negative. This interface keeps the validation decisions local to Capacity; no additional class, wrapper or file split is justified by this source.

The urgent caller defeats that locality. It accesses the owned state directly, omits the reservation checks, and unconditionally reports acceptance. It therefore forces knowledge of the capacity invariant into a second module while failing to enforce it. Being unchanged does not exempt this flow: the approved contract explicitly applies to all submission modes, and the supplied ownership guidance requires inspection of unchanged collaborators when they defeat the ticket's approved outcome.

I assume construction receives a valid nonnegative numeric limit; the supplied contract does not define constructor rejection behavior. I do not invent a ceiling, outstanding-reservation ledger, per-job cancellation identity, duplicate-cancellation restriction or overflow policy. Those are not explicit requirements here. In particular, accepting a positive cancellation that would exceed an original limit is not independently reported as a breach of a stated upper-bound invariant.

## Findings

### F1 — blocking: urgent submission bypasses Capacity's reservation ownership

Full key: `review-ticket17-guidance-case-a/standards-01/F1`.

**Contract and code evidence:** `CONTRACT.md:2-5` requires nonnegative capacity and validated owner-mediated reservations for all submission modes. Its additional permitted writer is only `Capacity.cancel` (`CONTRACT.md:7-9`). At the exact candidate, unchanged `submission.js:6` performs `capacity.remaining -= job.units` directly, and line 7 reports `{ accepted: true, job }`. Unlike `submission.js:2`, it never invokes `Capacity.reserve`; the checks at `capacity.js:4` are bypassed.

**Concrete consequence:** by source evaluation, `submitUrgent(new Capacity(1), { units: 2 })` changes remaining capacity from 1 to -1 and reports acceptance. This is an illustrative static witness, not an executed test. A zero-unit urgent submission is also accepted, and a negative-unit urgent submission increases available units. Rejection without mutation and positive-integer validation consequently differ by submission mode. An unchanged reservation path can still corrupt the same state that the new cancellation operation is supposed to preserve.

**Proportionate remedy:** route urgent reservations through `capacity.reserve(job.units)` and return the existing rejection shape `{ accepted: false }` when it rejects, as ordinary submission does. Preserve the urgent mode's other responsibilities, if any, without duplicating or moving Capacity's checks. This uses the already approved owner rather than proposing a new owner or a neighboring refactor. A repair should exercise insufficient, zero/negative/noninteger and valid urgent reservations, alongside ordinary reservation and cancellation behavior, and receive exact-source re-review from the original baseline. These are recommended validation cases; no tests were authored or claimed here.

**Disposition and authority:** open; no repair or independent repair verification was supplied. No human risk acceptance or contract amendment was supplied. The finding is blocking under the current explicit contract. If urgent bypass is actually intended product behavior, that conflict requires an explicit human contract decision; a reviewer cannot authorize it by recommendation. No such decision is invented in this report.

No optional findings are raised. The report does not claim universal design approval beyond the inspected scope.

## Mechanical evidence audit and observation limits

Commands inspected the case's full tracked inventory and exact full-ticket diff (`git ls-tree -r`, `git diff BASE CANDIDATE`), baseline file contents (`git show BASE:path`), candidate numbered source (`nl -ba`), definitions/usages (`rg -n` for remaining/reserve/cancel/submit/construction/persistence terms), committed/tree identities (`git rev-parse`), and worktree cleanliness (`git status --short` / `--porcelain=v1`). The candidate tree contains only `CONTRACT.md`, `capacity.js` and `submission.js`. The usage search located four state writes: constructor initialization, reserve, cancel and urgent submission.

`git diff --check BASE CANDIDATE` completed with no diagnostics. SHA256 values above identify the read inputs. Those mechanical observations establish source identity, inventory and whitespace status; they do not establish the substantive ownership conclusion. That conclusion rests on the contract and the actual caller/mutation flow explained above.

No runtime probes, test suite, Python commands, dependency installation or source modifications were performed. No test/check records were supplied, so there is no claim of passing behavior, concurrency coverage or environment compatibility. Only this original report was written, at the authorized output path. No separate finding history, integration decision, milestone assessment or human QA decision was created; any subsequent disposition and exact-source verification must preserve this original observation and use its full finding key.
