# Finding history: review-M1-architecture-01

## Event01 — New cumulative blocker opened

**Full key:** `review-M1-architecture-01/standards-01/F1`. **Original classification:** blocking. **Disposition:** open. **Actor:** root preserving the independent fresh High Standards `/root/m1_standards` observation on 2026-11-12. **Exact source:** `d02e61ea27de4febd17e337bd51529d07861226b`; fixed cumulative baseline `1a623bad0b08241367948948b731b9e1f5114671`.

[Original concern](../evidence/m1-qa-01/standards-01-original.md#f1--blocking-inherited-git-index-routing-writes-into-the-callers-index), [assessment](M1-architecture-01.md), [raw reproduction/manifest](../evidence/m1-qa-01/index-routing-repro-01/manifest.json), [readback correction and staged entries](../evidence/m1-qa-01/index-routing-repro-01/readback-01.json), [capture](../evidence/m1-qa-01/capture.json).

The ordinary public CLI inherits `GIT_INDEX_FILE` pointing at the disposable caller's existing index. Harness submission capture stages value2 into it while caller HEAD and working value1 stay unchanged. Later check-ticket rejection invalidates the canonical baseline gate and prevents integration, but the caller index has already been mutated. Paired ordinary-environment control completes and preserves index bytes. This violates the existing caller HEAD/index/work preservation promise, independently of whether ticket24's prior refactor-specific findings remain fixed.

**Next responsible action:** resolve routing consistently within existing Git/process owners before any repository writes, or use an explicit safe preflight rejection; inspect closely related environment routes and preserve intended isolated-merge overrides. A narrow patch to one `add` call is insufficient. The repair workflow must retain the demonstrated red/control observations, test the public CLI/Git outcomes, renew applicable final-source full/static checks and independent exact-source finding/cumulative verification. No repair assignment was launched during this begin-QA task.

**Prior/superseded observation:** none for this new full key. Existing ticket19/ticket24 histories and original classifications remain unchanged. **Repair ticket/commit and independent fixed verification:** absent; pending responsible repair workflow. **Human decision/amendment/deferral:** absent; no risk was accepted. **QA decision:** absent. **Integration/milestone readiness:** held; M2 remains ineligible. Assessment completion does not resolve this finding or accept M1.

## Event02 — Readability correction changes assessed source; revalidation pending

**Full key:** `review-M1-architecture-01/standards-01/F1`. **Original classification:** blocking. **Disposition:** open, pending relevant current-source revalidation. **Actor:** root, 2026-11-12, following the human's [M1 code review](../../../docs/human_qa/m1_review.md). Starting commit remains `d02e61ea27de4febd17e337bd51529d07861226b`; the correction is an uncommitted working-tree implementation identified by [per-file hashes and source archive](../evidence/m1-human-review-01/final-source.json), not a newly assessed commit.

The human requested helper extraction and docstrings, using three fresh Medium GPT-6.1 Sol workers with root reviewing. These edits preserve existing owners and public behavior. They do not address the ambient `GIT_INDEX_FILE` defect: Git executable statements remain unchanged. Root retains the original blocker/report and Event01 without rewriting their source identities. The changed workflow source requires renewed relevant cumulative assessment before readiness; prior clean ticket reports and old fixture candidate cannot authorize acceptance of this implementation.

[Correction source/verification evidence](../evidence/m1-human-review-01/start.json) and the human-review response retain actual checks and their limits. No fixed verification, risk acceptance, blocker deferral, contract amendment, exact candidate approval or M1 acceptance exists. The next responsible workflow must resolve F1 and obtain current-source review/check/candidate evidence before readiness. This event does not launch that repair or later milestone work.

## Event03 — Final correction checks retained; blocker and cumulative renewal remain open

**Full key:** `review-M1-architecture-01/standards-01/F1`. **Original classification:** blocking. **Disposition:** open, pending relevant current-source revalidation. **Actor:** root, 2026-11-12. Following Event02, the required suite exposed an existing external Git-observer race, also reproduced on pre-edit production code. The same three scenarios now use a bounded suite rendezvous and opt-in real Git trace correlation while retaining all authority/ref/lock assertions. Failed/control/timing-only trials and the interrupted campaign remain preserved.

The final uncommitted correction is identified by [renewed source/test hashes](../evidence/m1-human-review-01/renewed-source.json), patch and archive. [559 passed in 968.95 seconds](../evidence/m1-human-review-01/renewed-suite-result.json), strict mypy, Ruff lint/format and whitespace passed with source/test bytes unchanged. [Bounded correction assessment](M1-human-readability-01.md) and [root original report](../evidence/m1-human-review-01/root-01.md) record actual review and omissions. This supplements Event02 with final tested identities; it does not rewrite its earlier observations.

Git executable AST remains unchanged, and no repair of F1 or independent current-source fixed verification is claimed. A fresh High cumulative assessment, appropriate candidate/check renewal and actual human acceptance are still required before M1 readiness/acceptance. No risk waiver, blocker deferral, source-contract amendment, promotion or M2 execution occurred. The human requested a temporary handoff and a new chat; the next session must preserve this unresolved work and the unrelated dirty worktree.

## Event04 — Authorized routing repair claimed; independent verification pending

**Full key:** `review-M1-architecture-01/standards-01/F1`. **Original
classification:** blocking. **Disposition:** open, pending exact-source
independent repair verification. **Actor:** root, 2026-11-13, recording worker
`/root/m1_repair` under the human's continuation request.

The [repair assessment](M1-index-repair-01.md),
[worker ownership/coverage reasoning](../evidence/m1-index-repair-01/worker-notes.md)
and [frozen source identities](../evidence/m1-index-repair-01/final-implementation.json)
identify the bounded Git/process environment correction against fixed repair
baseline `e2b0a260fa192a7b51edc5f4cc5692c6340444c2`. It changes ordinary Git,
prepared ref transactions and configured process launches without changing
saved schemas or caller-preservation requirements. All four architecture
triggers remain No; mandatory M1 cumulative renewal still applies.

The original public-CLI symptom went red before the production edit. Four new
CLI regressions, eight routing observations and 125 affected cases pass on the
claimed repair. The default `/tmp` run exposed a `noexec` environment problem;
failed/partial runs remain retained and separate from executable-TMPDIR results.
The final-source full suite is still running. Worker claims and passing checks
do not independently close F1.

This supplements Event03. No new implementation ticket, contract amendment,
risk acceptance, blocker deferral, human QA acceptance or M2 execution exists.
Repair commit, fresh separate original Spec/Standards, required fresh High
cumulative report and exact candidate preparation remain pending. The next
responsible action is completion of these gates by root and fresh reviewers.

## Event05 — Repair checks completed; independent review still pending

**Full key:** `review-M1-architecture-01/standards-01/F1`. **Original
classification:** blocking. **Disposition:** open, pending exact-source
independent repair verification. **Actor:** root, 2026-11-13.

The human requested source identity verification, then completion of required
checks and persistent documentation/handoff. The repair patch remains byte-identical
to the frozen implementation; all 28 source/test/configuration hashes and 50
instruction hashes match before/after every required check and at completion.
[Verification outcome](../evidence/m1-index-repair-01/verification-completion.md)
retains 563 passing full-suite tests (zero failures/errors/skips) and passing
mypy, lint, format and whitespace gates. An incomplete evidence-plugin attempt
is retained separately from the successful full repeat.

This supplements Event04 without altering its original account. Checks establish
implementation verification only. Repair remains uncommitted against `e2b0a26`;
fresh independent Spec/Standards, required High cumulative renewal, exact candidate
preparation and human acceptance remain pending. No waiver, promotion or M2 work.

## Event06 — Independent exact-source repair verification

| Field | Value |
| --- | --- |
| Finding | `review-M1-architecture-01/standards-01/F1`; [original blocking concern](../evidence/m1-qa-01/standards-01-original.md#f1--blocking-inherited-git-index-routing-writes-into-the-callers-index). |
| Disposition | **fixed**; original classification remains blocking. |
| Actor and role | Root, 2026-11-16, aggregating fresh independent Spec `/root/m1_spec` and Standards `/root/m1_standards`. |
| Affected revision | `88e4cd8aabc78e76e66efc02983fec3900ab0a23`; exact source includes repair `e06eeaf7ae961a927e13b8d330b1675646afe4e2`. |
| Reason and evidence | Shared copied-environment filtering precedes ordinary Git, prepared ref transactions and configured process launches. The intentional isolated merge override stays explicit. Both reviewers trace prevention before any caller-index write, rather than rollback after rejection. [28 source/50 instruction matches](../evidence/m1-final-review-01/source-and-instructions.json) bind current bytes to [563/full and static passes](../evidence/m1-index-repair-01/verification-completion-result.json), four caller regressions and eight retained routing observations. |
| Previous / superseded observation | [Event05](#event05--repair-checks-completed-independent-review-still-pending); earlier reports and events remain immutable historical observations. |
| Repair or implementation ticket | [Authorized bounded cumulative repair](M1-index-repair-01.md), not reopened ticket 24 or a new feature. |
| Repair commit | `e06eeaf7ae961a927e13b8d330b1675646afe4e2`; [scoped committed patch](../evidence/m1-final-review-01/repair.patch). |
| Independent verification | Fresh High Sol [Spec original](../evidence/m1-final-review-01/spec-01-original.md) and [Standards original](../evidence/m1-final-review-01/standards-01-original.md), exact source above, each zero blocking/optional findings. Originals remain separate from root's disposition. |
| Human decision / amendment | No waiver, deferral or contract change needed; existing preservation contract repaired. Human QA acceptance is absent and remains required. |
| Milestone assessment | [Cumulative M1 renewal](M1-architecture-01.md); its independent report/readiness remain separate gates. |
| Next action | Finish required cumulative renewal, prepare fresh exact candidate/request, then record actual human QA observations/decisions. M1 unaccepted; M2 ineligible. |
