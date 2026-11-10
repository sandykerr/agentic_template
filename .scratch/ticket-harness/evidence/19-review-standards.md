# Standards report: review-ticket-19 / standards-01

**Result: assessment completed; 0 blocking findings, 0 optional findings.** The committed change meets the inspected development standards. The evaluation supplies finite evidence of actual reviewer judgment on the declared cases, and its authoring routes can carry that evidence into the five refactors. It does not establish package architecture quality, unrestricted input isolation, runtime enforcement, or milestone acceptance.

## Report envelope

| Field | Value |
| --- | --- |
| Assessment / report | `review-ticket-19` / `standards-01`; original independent Standards assessment |
| Assignment / actor | `/root/standards19`; supplied `/tmp/ticket19-review/standards-assignment.txt` and `common.txt` |
| Requested configuration | Fresh GPT-6.1 Sol High; 250,000 active-context advisory target |
| Observed configuration limits | I received this independent assignment without the sibling implementation report. Independent backend model/reasoning enforcement and measured active-context telemetry are unavailable; the requested settings are not enforcement evidence. |
| Fixed original baseline | `f2929e79cfd5a68f670862775053ae85ba9582b5` |
| Exact assessed source | `e90abb64ab95c5b15cdb0949b03c6a948365339b`; clean worktree, all changed file bytes verified against this commit |
| Diff / commits | `git diff f2929e79cfd5a68f670862775053ae85ba9582b5...e90abb64ab95c5b15cdb0949b03c6a948365339b`; one commit, `e90abb6 Evaluate development reviewers on a declared blinded corpus` |
| Instructions / source identities | [standards-identities.json](standards-identities.json): path/content SHA-256 identities for instructions, all 77 changed files, inspected collaborators, original assignment files and audit artifacts |
| Original output | This file; parent must preserve it verbatim and record its digest externally |
| Prior observations | Actual ticket 17/18 assessments report no unresolved actual finding, missing report, relevant pending revalidation or required human decision. Frozen fixture findings retain their separate original scopes. No earlier actual ticket-19 finding was supplied. |

I applied AGENTS/domain/glossary/ADRs, testing/test-strategy, ownership scope, review records, architecture checkpoints, report-envelope requirements, codebase-design, writing-for-agents/skill-creator, the scoped approved spec/ticket contracts, and the supplied smell baseline. No `CODING_STANDARDS.md` or `CONTRIBUTING.md` was found; a hidden-file search found only root `AGENTS.md` among those instruction filenames. Documented project contracts override general design heuristics.

## Inspected scope and substantive assessment

### Guidance ownership and instruction consumers

I read the complete changed planning reference, implementation wrapper, handoff wrapper and new evaluation reference, plus their unchanged consumers: `grill-to-tickets`, upstream implementation/code-review instructions, the feature worker-handoff contract, review-record contract, ownership contract and architecture-checkpoint contract. I followed the selection, implementation, repair, review, reconciliation and both handoff branches rather than limiting inspection to the added paragraphs.

The responsibilities remain coherent:

- `ownership-review.md` owns substantive inspection of actual operations, callers, writers, readers, save/restore and invalidation. The new reference points to it rather than introducing a competing ownership policy.
- `review-records.md` owns assessment/report identities, immutable originals, append-only full-key finding history and decision authority. The new evaluation files are instances of that existing evidence responsibility. Reviewer report IDs remain their original values instead of being rewritten to resemble actual ticket reviews.
- `architecture-checkpoints.md` still determines when broader assessment gates integration or milestone readiness. The new document makes no unconditional third reviewer or new scheduler.
- `reviewer-evaluation.md` owns the G1 evidence pointer and finite interpretation. Planning carries its identity and limits into implementation/review context. The implementation wrapper places it before fresh assignments; the unchanged repair loop retains original baseline, fresh workers/axes and renewed checks. The handoff wrapper places it in common gathering before either the implementation branch or M1 QA/waiting branch.

This is appropriate progressive disclosure: short conditional pointers enter established workflows; one reference carries the evidence and limits. The three pointers serve different actual consumers and do not duplicate the full policy. Upstream skills are unchanged. The wrappers explicitly retain whole-ticket review and sufficient reasoning over the upstream hunk-only/400-word briefs.

There is no new executable owner, writer, runtime schema, dependency, configuration, package behavior or production test. The new collector/builder/check helper author finite evidence under existing author/reviewer/evaluator roles; they do not mutate runtime lifecycle records or confer integration authority. Frozen snapshots and original reports are durable evidence, not executable restored approval state. Mutable indexes cite immutable identities. A changed guidance version cannot inherit G1's judgment evidence; changed actual source still needs relevant exact-source review under existing contracts.

For a plausible future substantive instruction change, the author must version the guidance and retain G1, preserve prior trials, and obtain complete declared-corpus evaluation before claiming that corrected guidance passed. Planning and both handoff paths then carry the new identity and limits. A new actual refactor still supplies its own ticket baseline/source and actual findings. Neither operation requires a production checkpoint/schema change in this ticket. This localizes the evidence interpretation without distributing reviewer policy across callers.

The four start/post triggers recorded **No** are justified. This work adds observations and references using the existing assessment/report/finding lifecycle, existing persistence form and author roles. It introduces no new lifecycle, restore protocol, shared mutable workflow state or additional writer of existing state, including guidance state. The deliberately broken fixture designs are inputs, not new production responsibilities. Real M1 feature-start provenance, all-package cumulative assessment and human QA remain explicitly unperformed; their absence is not an additional ticket-19 completion prerequisite.

### Corpus judgment, controls and classification

I read all eight `CONTRACT.md` files, every source/caller in their directories, both complete original raw reports, the pre-assignment key, evaluator adjudication and full-key fixture history. The following conclusions come from source/contract reasoning, not matching counts or hashes:

| Case | Independent source assessment and actual relevant-axis judgment |
| --- | --- |
| a3 | `record` shares one gate between both lists; JSON restoration assigns separately decoded arrays (`run.py:23–26`), and invalidation updates only durable gates. QA reads the detached verified view. Spec F1 correctly blocks stale eligibility and asks Run to rebuild canonical references while retaining schema. Standards independently agrees. |
| b7 | The caller injects Git execution mechanics and passes policy values; `validate/checked` owns command failure, root, branch, dirty/untracked, commit resolution and ancestry decisions. Its cohesive functional interface removes caller coordination. Both reports correctly avoid a class/framework or richer-diagnostic requirement. |
| c2 | Checking validates an ID but writes `history[-1]` (`checking.py:8`); execution passes mutable history and reads decisions by ID. Delayed A-after-B and unknown IDs therefore misattach decisions. Spec F2 correctly requires checking to return validation and execution/the identified attempt to own attachment; merely searching by ID inside checking would retain the contract breach. |
| d9 | `parse` owns invocation-local construction/DFS state, detects duplicate IDs, missing dependencies and cycles, preserves declaration/dependency order, and returns a tuple of frozen values. Both reports reasonably keep this a pure transformation, without inferring a shared lifecycle or parser-object requirement. |
| e4 | Repair repeats the guard and all owner-controlled attempt/current-ticket writes while normal workers call `Attempt.submit`. Standards E4-F1 correctly distinguishes current matching behavior from the explicit single-owner violation and future policy propagation risk. Delegating repair to the existing operation is proportionate. Spec independently agrees. |
| f6 | The same-directory temporary file, close-before-replace and `finally` cleanup preserve the stated pre-replace failure behavior. The subprocess primitive forwards argv/cwd/capture/timeout and nonzero results, leaving domain decisions outside. Both reports properly respect the existing-directory/finite-timeout assumptions and explicit fsync/metadata exclusions. |
| g1 | Preparation returns `None` derived fields; CLI alone normalizes/defaults/validates, while resume directly returns the incomplete result. Standards G1-F1 correctly identifies both hidden initialization protocol and unusable resumed state, with completion inside Preparation as the bounded remedy. Spec independently agrees. |
| h8 | Attempt owns construction, guarded transitions and mirrored updates; its caller requests operations and top-level copied snapshots resist top-level field replacement. Both reports support this actual invariant owner and disclose the scalar-value assumption. The shallow-copy limitation is material and assessed below. |

All four seeded required concerns were detected on their declared axes with source-specific blocking classifications and bounded remedies. Cross-axis agreement is supplementary, not a substitute for the required axis. None of the controls received an unsupported blocker; neither report manufactures optional refactors. The blockers in e4/g1 reflect approved responsibility contracts and concrete caller/change effects, not a general preference for objects. The controls demonstrate that cohesive functions and small state-owning classes can both be acceptable. No smell heuristic justifies an additional implementation finding here.

**h8 limitation:** `CONTRACT.md:5–6` uses broad copied-snapshot/caller-owned-dictionary language, while accepted identity/revision value types are unspecified. The code only copies top-level records (`attempt.py:3–4,16–22`). My disposable observation confirmed that scalar values and top-level returned-field writes are isolated, but dictionary-valued identities/revisions and mutations through nested returned values remain aliased. Thus G1 does **not** establish arbitrary nested-input isolation. I accept the reports' narrow scalar interpretation as a reasonable finite assessment of IDs/revisions in the supplied operation flow: no record-dictionary initialization API or nested-payload flow is supplied, both reviewers state the assumption, and the evaluator/published reference preserve it instead of claiming a deep-copy guarantee. I do not infer generic dictionary-valued domain inputs solely from Python's untyped call surface. If a subsequent target contract permits mutable identity/revision payloads, that target needs a new judgment and suitable copying/rejection; G1's clean h8 result is insufficient evidence for it. The ambiguity remains a disclosed evaluation limit, not a retroactive waiver of a demonstrated required seeded miss.

### Evidence production, preservation and authority

`build_corpus.py` constructs source/contracts and copies scoped baseline guidance; it refuses an existing snapshot. Its answer key/builder remains outside the reviewer snapshot. `REVIEW.md` requests evidence-based per-case reasoning without supplying expected classifications; outgoing absent links are explicitly out of scope, preventing the shared spec's evaluator key from being pulled into reviewer input.

The original parent-session declaration-write record precedes both actual `spawn_agent` records. Both dispatches specify `fork_turns: none`, `gpt-6.1-sol`, High independently. The child sessions record the requested model/High settings and actual source-reading commands for the eight cases. Neither source-tool inventory shows key/build/spec/sibling reads. The reports also explicitly attest their scope. This supports actual fresh independent development assignments, while remaining short of backend isolation or hidden instruction-effectiveness proof.

The complete raw reports are real original assistant `final_answer` content. I independently compared them with their known original child sessions, and compared the retained custom-tool/received-message records with the corresponding original session records. Both matched exactly. Reviewer-preserved copies match apart from terminal newline and remain separate. Readable initial inputs are reviewer-attested transcriptions; original dispatch and received payloads remain encrypted, so byte-exact plaintext delivery cannot be independently established. The repository correctly describes this distinction instead of relabeling ciphertext or a preservation copy as original plaintext dispatch evidence.

The collector refuses changed existing captures; its later supplement preserves missing original record types alongside earlier captures. Its failed plaintext comparison and correction remain in `collector-history.json`, with the actual limit stated. These are collection failures/followups, not deleted judgment trials or additional evaluation repetitions. One original full-corpus assignment per axis is retained; no script emits reviewer findings or mechanically establishes judgment quality.

`finding-history.md` retains all eight full keys as open at the intentionally defective fixture source. It supplies actor, reason, exact source identity, original report links and explicit non-applicability of repair/decision links. It does not mark seeds fixed, treat them as actual harness blockers, or assume human authority. Prior ticket-17/18 fixture histories and actual clean assessments are preserved unchanged.

## Verification and audit

The coverage map in `19-implementation-report.md` distinguishes six failure modes: undeclared/cherry-picked corpus, canned/leaked/non-independent review, unsupported classification, discarded failed trial, lost handoff context and runtime-development confusion. The actual work addresses them with declaration/source snapshots, real assignments/raw reports, substantive per-case adjudication, preserved collector/trial history and conditional routing. These are meaningful observations for standalone documentation/skills/evaluation changes. No production runtime code/test/config/dependency change warrants replaying the CLI suite, install checks or private-module tests. Existing public CLI/real-Git requirements remain intact for later executable refactors.

The final implementation log records successful official validation of both changed skills, shell syntax, whitespace and the standalone audit. The final result names pre-checkpoint HEAD plus exact source/helper/evidence hashes, rather than pretending uncommitted work was already that HEAD. I independently matched all final recorded hashes to the exact implementation commit; its 93 recorded local links and 36-file manifest retain their actual scope. Earlier 87/88-link check snapshots remain historical and differ where collector/evidence text evolved; they are not offered as final-source results.

Independent audit results are retained in [standards-audit.json](standards-audit.json), [standards-parent-provenance.json](standards-parent-provenance.json) and [standards-check-history.json](standards-check-history.json), with script/content identities and command exits in [standards-identities.json](standards-identities.json). These confirm:

- Clean exact committed source; merge-base equals the fixed baseline; only the four intended authoring paths and new ticket-19 evidence paths changed.
- All frozen corpus bytes and guidance digests match the declaration; guidance also matches its baseline and current substantive sources.
- Both original corpus finals/source-tool records match actual known sessions, with no rewrite of original outputs.
- Final retained capture/check identities match; Python evidence files parse without executing the writers; independent `git diff --check` and `bash -n` pass.

Two reviewer audit assumptions failed and were corrected without source changes: a no-match `rg` exit stopped an `&&` read chain, so required files were subsequently read explicitly; a comparison initially assumed the earliest check JSON contained a later-added identity group and raised `KeyError`, so the corrected comparison handles that schema difference. Combined output truncation was addressed with bounded rereads/call inventories; complete audit data remains in the linked JSON. These failures are retained in the identities file and are not attributed to the implementation.

## Findings

None within the inspected scope. No full actual ticket-19 finding key is issued. h8 value-type ambiguity, the Spec aggregate encoding mismatch, opaque input provenance and unavailable backend enforcement are preserved limitations with bounded claims, not omitted evidence or invented approvals.

## Scope omissions and result limits

I did not assess unchanged production package architecture, run the runtime suite/harness, execute historical builders/collectors/check writers, perform M1 cumulative review, accept QA, alter source, reconcile ticket completion or generate the next prompt. Those operations are outside this independent review. Scoped spec sections and relevant unchanged guidance consumers were inspected; unrelated runtime features and historical fixture-building bodies were omitted. Hash-equal duplicate snapshot guidance/report copies did not require duplicate substantive readings.

The missing post-review completion records and generated handoff at this checkpoint are expected parent work. The inspected routing can support that later handoff, including G1 identity/original reports/finite limits and required new refactor reviews. This Standards assessment is complete; ticket bookkeeping, sibling review aggregation, actual later refactors, M1 readiness and human acceptance remain separate responsibilities.
