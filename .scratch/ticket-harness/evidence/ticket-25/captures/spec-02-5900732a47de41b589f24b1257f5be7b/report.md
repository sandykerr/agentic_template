# Review report: review-ticket-25 / spec-02

| Field | Value |
| --- | --- |
| Assessment | `review-ticket-25`; [ticket assessment](../../../../reviews/ticket-25.md), routine whole-ticket Spec review after bounded repair 1 |
| Report identity | `spec-02`, Spec, round 2; assignment and actor `/root/spec25_round2`; fresh independent assessment |
| Actual settings | Requested GPT-6.1 Sol, High reasoning, active-context target <=250000. Backend model/reasoning enforcement and measured active-context telemetry are unavailable to this reviewer; requested settings are not proof of delivery. |
| Original baseline | `2c01fe9fe04c78fa10a2dac11e94826876467562`, fixed across repair |
| Assessed source | `febd86321851e2acec994237f9d1a1adea824c55`. Checkout HEAD independently matched; relevant committed source/test/guidance worktree diff against it was empty. Supplied dirty AGENTS/planning inputs remain separately identified. |
| Supplied instructions | Parent assignment; [canonical evidence index](../../25-evidence-index.md), [round 2 context](../../25-review-round2-context.md), current ticket/spec/workflow spec/milestones; AGENTS, GLOSSARY, both ADRs, review-record/report/testing contracts, test-strategy and capture/environment guidance. Exact identities are recorded below and in the [committed binding](../../25-repair1-committed-source-binding.json) and [current instruction snapshots](../../instructions-current/). The assignment is delivered conversation text; no backend delivery attestation is available. |
| Original output/evidence | This exclusively created original `report.md` in the [allocated producer directory](allocation.json). Parent owns subsequent registration and external report digest; none is embedded in the hashed report. Reused check allocations and prior originals are linked below with their original scope. No new executable probe was needed. |
| Inspected scope | Complete whole-ticket baseline-to-assessed-source change set: new capture module and tests; capture/helper documentation; implementation/testing/review routing; ADAPT skill and both references. Traced CLI allocation/registration, ticket normalization, source/result/file identities, shared routing/references, metadata ownership/initialization/reload/save, protections/aliases, derivation, original checking, idempotence and failure paths. Inspected unchanged `inputs.identifier`/`unique_object`, packaging configuration and runtime public CLI for integration/compatibility boundaries. All seven ticket criteria and all supplied prior findings were evaluated. |
| Omitted scope | No sibling round 2 report read. No new runtime capture adoption, cleanup/deletion implementation, active harness run, EC1 human acceptance, real-agent calibration or live Slurm workload assessed. Unchanged runtime internals were not re-reviewed as an all-package cumulative architecture assessment; that separately assigned checkpoint remains required. No adversarial concurrent filesystem replacement or arbitrary crash-recovery promise is inferred. No tests/Python/SSH were run by this reviewer on the login node or elsewhere. |
| Prior observations | Independently revalidated `review-ticket-25/spec-01/F1` at the exact assessed repair. Also checked `review-ticket-25/standards-01/F1`, `review-ticket-25/standards-01/F2`, `review-EC1-capture-architecture-01/standards-01/F1` and `review-EC1-capture-architecture-01/standards-01/F2` against that source. [Original finding history](../../25-finding-history.md), [original digests](../../25-review-round1-digests.sha256), [Spec navigation correction](../../25-review-spec-01-envelope.md) and original reports remain preserved. This report supplies revalidation observations, not edits to dispositions. |

## Substantive assessment

The whole ticket meets the independently usable development-capture scope at the assessed revision. I found no blocking defect or optional suggestion in the inspected scope. This conclusion follows the contract-to-operation traces below; matching hashes and passing checks alone would not justify it.

The governing contract is ticket 25 and the capture/placement/structured-record portions of the supplied evidence-policy-1 workflow spec, together with the shared implementation/ownership contract. The supplied planning bundle is uncommitted input, not silently part of the implementation commit. The current navigation rename is explained in [the instruction refresh](../../25-instruction-refresh.md); the reviewed capture requirements are unchanged. The expressly authorized persistent-compute follow-up is documented in [its original account](../../25-compute-guidance-update.md). Neither the review nor capture supplies QA acceptance or promotion authority, consistently with ADR-0001 and ADR-0002.

### Allocation, ownership and shared records

The standalone `python -m ticket_harness.evidence` CLI creates a `CaptureStore` and invokes allocation or registration. The helper owns deterministic path selection and capture metadata; a producer owns only its allocated payloads. Existing `ticket-harness` run/status/stop/continue dispatch remains separate. The module adds no runtime call or run/attempt/QA schema mutation.

Construction discovers and resolves the existing checkout, requires the `.scratch/FEATURE` shape with `issues/`, and limits output to its evidence tree. `inputs.identifier` normalizes positive numeric aliases such as `25` and `025`; `_ticket` requires exactly one matching issue. Duplicate normalized ticket selections fail. No issue or spec body is written.

`allocate` distinguishes an absent optional name (`None`) from a supplied value throughout validation, routing and linking. One ticket chooses `evidence/ticket-ID`. A genuinely shared allocation requires at least two tickets, a validated descriptive shared name outside the reserved `ticket-` namespace, and an optional validated milestone. Shared records hold the capture/decision copy; ticket artifacts hold `shared_records` references. Existing folder/scope disagreement fails rather than changing ownership silently. The same scope can be reused by later producers, while changed membership requires another descriptive destination.

All capture metadata transitions occur under the feature evidence-directory descriptor lock. Allocation validates the relevant records and destination before writing metadata, creates a UUID directory with exclusive creation, writes its receipt, saves the authoritative folder artifact, and then updates ticket references. Independent producers receive distinct payload directories and do not edit consolidated JSON. Existing specialized folders, original reports and embedded historical paths stay in place.

A new artifact explicitly separates `captures`, `shared_records`, `assessments`, `approvals` and `execution_results`. Existing records preserve review arrays and unknown fields; incompatible schema/folder/scope or non-list namespaces are rejected. Capture does not interpret an approval as applying to a new UUID or copy approvals into new captures. The later review/execution owners must bind their decisions to exact identities and use the same documented lock. This ticket establishes that coordination contract without speculatively implementing cleanup authority.

### Registration, originals, aliases and failures

`register` restores scope, destination and persisted protected paths from the receipt, combines newly supplied freezes, and verifies receipt/destination/folder identity. `_within` rejects absolute and parent-traversing payload paths and keeps files inside their producer destination. `_safe` checks path components for symlinks and rejects hard-linked files; receipt metadata is explicitly excluded from payload registration, including its normalized `./allocation.json` alias. Duplicate normalized file paths fail. Regular files are read for size and SHA256; payloads are never rewritten by registration.

Source version, actual activity and observed result are required producer statements. They can explicitly say `unknown`; hashing does not certify their truth. Original and derived entries are distinct, and a derived entry requires retained original paths whose identities are captured. Derivation alone grants no replacement or deletion approval.

At lines 301–304 of the assessed module, a complete loop checks every existing capture's file identities. Only a second loop at lines 305–311 can return an identical existing capture. Thus both new append and healthy retry require all prior payloads to pass validation. A changed payload, missing file, prohibited alias or changed existing capture facts causes a visible nonzero result before a metadata save. Healthy identical retry returns the same record without appending; changed facts for an existing capture require another allocation. These rules preserve original evidence and its attributed result rather than refreshing history.

Declared protected roots are resolved and checked for relevant writes. Receipt protections persist to registration; a new freeze must be supplied then, as the contract says. A freeze of an unrelated ticket subtree permits capture elsewhere, while a protected target artifact/destination blocks its operation. This is operator-supplied development output protection, with exclusive producer creation and assignment duties, rather than automatic detection of arbitrary external runs. The guidance directs active-run evidence to its authorized output outside approved/frozen inputs. I did not narrow a promised guarantee by assuming adversarial replacement cannot happen: concurrent adversarial replacement and arbitrary crash recovery are explicitly excluded, while ordinary preexisting aliases and changed originals are covered by actual checks.

Each metadata replacement uses a unique temporary sibling, flush/fsync and atomic replacement. Shared-link allocation spans several files, so partial filesystem failure can leave incomplete links or an unregistered directory, with nonzero diagnostics. The documented same-scope allocation retry can complete missing references while preserving captures/decisions; it allocates another UUID rather than claiming transactional recovery. Registration validates before its single artifact save. An unregistered payload remains unreviewed, and no success, failure or schema validity confers deletion eligibility.

### Independent prior-finding revalidation

**`review-ticket-25/spec-01/F1` is corrected at `febd86321851e2acec994237f9d1a1adea824c55`.** I read its original report and actual original A/B counterexample. In the repaired source, retrying A after later registered B changes cannot reach the identical-ID return: the first loop visits B and raises before the second loop starts. If B is missing, file identity acquisition raises before that return; a symlink/hardlink is rejected on the same path. Existing record bytes are not saved on these failures. The new public regression at `tests/test_evidence.py:241` registers A/B, changes B, retries A, requires a nonzero original-change diagnostic and byte-identical artifact. The exact-source full suite includes it. The same source reasoning independently supports correction of the duplicate concerns `review-ticket-25/standards-01/F2` and `review-EC1-capture-architecture-01/standards-01/F2`; these remain distinct full keys.

**The empty-name concerns are also corrected at this revision.** Lines 170, 175 and 184 use supplied-value presence consistently. `--shared ''` reaches `_slug` and fails before entering evidence ownership or creating output; a supplied empty milestone follows the same validation. A milestone without shared scope fails the initial scope condition. A valid shared name still enters linking, so a two-ticket request cannot fall into a reserved single-ticket destination. The two new cases at test lines 405–406 require no evidence root after failure; valid ticket/shared/milestone cases remain covered. This revalidates `review-ticket-25/standards-01/F1` and `review-EC1-capture-architecture-01/standards-01/F1` without rewriting their original classifications or history.

These are owner-local ordering/presence repairs. Receipt format, schema, lock owner, namespace owners and runtime responsibilities remain unchanged; all four recorded architecture triggers still apply. I identified no consequential ownership decision or ADR conflict requiring a human decision.

### Acceptance and guidance coverage

| Ticket acceptance criterion | Independent assessment |
| --- | --- |
| Repo capture skill identifies ticket/purpose and delegates to Python | Met. The skill asks for feature/tickets, purpose and producer first, delegates allocation/registration, and links existing environment/testing/test-strategy/review contracts instead of copying their obligations. |
| Ticket/shared/milestone placement and one authoritative shared copy | Met by normalized scope routing and references; the retained EC1 shared artifact is linked from tickets 25 and 26. |
| Source/activity/result/file identity, originals/derived distinction, facts only | Met by attributed facts, byte identities, derivation metadata and preserved originals; there is no retention/deletion/acceptance operation. |
| Parallel destinations, consolidated registration, no overwrite/inherited approval | Met by exclusive UUID destinations, one locking owner, complete prior-identity validation, same-ID comparison and preservation of distinct review namespaces. |
| JSON artifact per applicable folder, capture separated from later decisions/results | Met by schema namespaces and shared references; capture cannot make later approvals or outcomes. |
| Applicable development routing and protected boundaries; separate runtime adoption/history | Met in implementation/testing/review wrappers and the helper/skill contract. Runtime adoption remains separate and historical paths are not moved. |
| Actual skill-guided capture with provenance/protected originals/shared links | Met by retained public CLI/filesystem/JSON observations, current installed CLI allocation/registration and actual shared EC1 guidance capture. No cleanup or human EC1 approval is inferred. |

The ADAPT guidance explicitly prefers retained suitable Forest terminals and compatible live Slurm allocations/compute shells, rechecking capacity, source, job state, resource fit and remaining time. It distinguishes SSH from reservation, avoids duplicate work and retains outputs before release. Its executable temporary-storage advice is tied to observed noexec mounts and requires host/capacity rechecking. This is the authorized guidance follow-up; it does not change the harness scheduler/backend or claim live Slurm execution.

## Evidence audit

I used lightweight local source/document/Git inspection only. `hostname -s` returned `adaptlogin202`. I read the ADAPT/environment guidance, opened no SSH session and ran no Python or tests. The proposed verification scope reused existing required observations, as directed by testing/test-strategy; no missing fact justified another probe or a passing-suite replay.

I examined `git diff BASE...febd863`, its whole changed-source/guidance contents, and `git log BASE..febd863`. The three commits are the authorized compute guidance, original capture implementation and bounded repair. HEAD returned the exact assessed revision. A relevant worktree-vs-assessed-commit path diff was empty. The supplied dirty work remains untouched.

The [post-commit binding](../../25-repair1-committed-source-binding.json), observed SHA256 `6e7ffe08d383fdeda9b28f2e2ba375de033675913fcdf881fbbf5c902304a463`, distinguishes committed product hashes and supplied uncommitted input hashes. Current `evidence.py` is `8040d512b43380678f4c6baae419ab37763c468c0190ac08dd7be3b1f04d7187`; `test_evidence.py` is `3aa908b3c9c50ef5f490196d9a69f1fb5e54d8e0822a9de79a6c898acd5545ac`. Both match the tested/bound repair identities.

I read actual full-run stdout under [verification-71288fc1a1da4058830978bc454711dc](../verification-71288fc1a1da4058830978bc454711dc/allocation.json), ending **589 passed in 813.40s**, with successful mypy (11 files) and lint outputs. The original formatting interruption remains an interruption. The separate [recovery results](../verification-resume-44c46221b60444d4b2ff2512e4603e48/check-results.json) and [reuse provenance](../verification-resume-44c46221b60444d4b2ff2512e4603e48/reuse-provenance.json) reuse only those three actual passes after exact source/input hash comparison, and record successful format, whitespace, capture-skill validation, isolated wheel/install, installed helper/harness help, installed allocation/registration, installed-module identity and unchanged-source checks. I inspected installed registration's actual payload identity. These are retained Forest203 x86_64 observations with one-thread/executable scratch constraints, not checks executed by this reviewer.

The [repair allocation](../repair1-bba5aa58e72645abb32a2860b4a4e8b0/allocation.json) retains distinct red/green source snapshots and results. Its observed green outputs are 10 selected scope cases and 26 capture-family cases passed. The full suite's exact source includes the three new regression cases. The tests use the approved subprocess/real-Git/filesystem/JSON seam with distinct failure decisions, including concurrency, original/derived identity, changed metadata/originals, scope ambiguity, aliases, malformed metadata and freezes. I found no concrete need for another scenario matrix.

The actual [shared guidance capture](../../../evidence-capture-workflow/EC1/evidence-review.json) contains one authoritative capture and empty decision namespaces. The ticket-26 artifact references it; the canonical index/ticket-25 artifact record the other reference. The guidance driver records 37 path/anchor/routing checks, zero failures and successful registration. Existing original round-1 reports/full finding history and original probe semantics were read without sibling round-2 material. Earlier failed/interrupted campaigns retain their own identities and are not treated as current passes.

Instruction identity observations from `sha256sum`:

| Instruction path | SHA256 |
| --- | --- |
| `AGENTS.md` | `f2d28cd8b23a8f52f1478858c249670a7b5b144a5dd8175065e5cc63446e0a98` |
| `GLOSSARY.md` | `4b45856348181d3383d3b2416d56eb0261243ddab8507fb869dd4bdee39bdefc` |
| `docs/adr/0001-reusable-harness-and-local-integration.md` | `6e4adc64a9a454d00ca4d16649796daf525783e554d1dc892bd0654b5990e603` |
| `docs/adr/0002-human-qa-gates-feature-promotion.md` | `7f9ef955940b6a4315d9a5fc7c7279cc367043310ebd4575cee450dffd0e4982` |
| `docs/agents/review-records.md` | `0c8bc5ddb426626d9ad416de1305d9ce6625ea3ccff5a11841b18dfc4d9a369f` |
| `docs/templates/reviews/report.md` | `9164c2267b27fd6ee89d09bb9d056b07bf07a682d0dc556e3e6b6f62c9bb3afc` |
| `docs/agents/testing.md` | `74ffea4ad8ec54713f5918b8e749283edacb249b9910912edbc7e053b6d57745` |
| `.agents/skills/custom/test-strategy/SKILL.md` | `0a399ca1988a324a970af94d6440544e4c2ba9760f197b97d6f96d758edd20ac` |
| `.agents/skills/custom/capture-evidence/SKILL.md` | `d4d9d316179b1e19128782315bb46418e92d0e399148c204e264c67e277fa568` |
| `docs/agents/evidence-capture.md` | `a9ab1e1f39d61a9a91cbdd3b6fa7d910dd307afadc54c373853bb61fe8255f72` |
| `docs/agents/python-environment.md` | `15b6945af7cf5781d7aba17d47dd98263c1ab82930bc6deb8298b2051cb9a85f` |
| Current ticket 25 | `f10111d8436ac8e2fdfb7c23b1528335f5270d980052002cc4e6ee6b2b116ed2` |
| Current feature `spec.md` | `74121d0d71f0954c0c93c1d9e3fcf5ae874c7d5c53a73b97886fa8594b5fe20d` |
| Current `evidence-workflow-spec.md` | `39249bcbe071dd4d0f33d59c4b07293b41e2bf029ab28ecdaa54493ae1aa8b39` |
| Current `milestones.md` | `9f33c783ba7c2b8f48ee8cb5087b2b1412f38b53fb1d5fda304ad5b065d3e6d0` |
| Round 2 context | `b75b1110c274d23fcaefa41024823825148b9b268143e2d29ed2489c10cbdcbe` |

Committed guidance is identified by the assessed revision; supplied current AGENTS/ticket/planning files retain the separate current-snapshot/binding provenance above. ADAPT skill/Forest/Slurm digests observed were respectively `87933e16880129303d7be5e8f757a407d67c36bc352e98bbf07da5b3fb8b338b`, `f08efb2a74665096acebad9dd64a75e79ea06ca830210582e8988dcc017ab332` and `c64dc72cd23bb77323fba39ef6200bca20292ab2d96380fde9e3db4e2f2cba6b`. These identify read instructions, not proof of model delivery, actual scheduler behavior or design correctness.

## Findings

No new blocking findings or optional suggestions in the inspected whole-ticket Spec scope. Prior full keys are independently revalidated as described above; the parent must append exact-source disposition evidence without altering original reports.

## Assessment result

**Assessment complete; clean Spec result at `febd86321851e2acec994237f9d1a1adea824c55`: zero new blocking findings, zero optional suggestions.** The original Spec blocker and the other supplied prior concerns are corrected at this exact source on independent source revalidation with retained behavioral evidence.

No unresolved assumption defeats the inspected promise. Explicit limits remain: producer statements require substantive review, operators supply freezes and honor exclusive payload ownership, future writers obey the common lock/identity contract, and runtime adoption/cleanup/QA acceptance remain separate work. This report neither substitutes for the separately required Standards/broader assessments nor declares integration readiness, ticket Done or EC1 acceptance.
