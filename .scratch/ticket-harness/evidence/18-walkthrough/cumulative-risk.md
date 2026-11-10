# Original cumulative Standards report: isolated risk fixture

| Field | Value |
| --- | --- |
| Review work / report | `review-18-fixture-cumulative` / `standards-risk-01`, original cumulative Standards assignment |
| Assignment / actor | `/root/implement18/fixture_cumulative_risk`, fresh reviewer delegated by `/root/implement18`; substantive source review, not a scripted reviewer |
| Settings | Requested fresh GPT-6.1 Sol, High reasoning, active-context target ≤250k. Actual runtime model, reasoning configuration, measured context allocation and token telemetry are unavailable to this reviewer. Requested settings do not independently attest delivery. |
| Cumulative baseline | `36772524659032570d018cc164c5aa4e90068edf`, initial fixture feature commit; no prior human-accepted milestone exists |
| Exact assessed source | `e65723747cf4029c1829209da9f333ca17d87989`, complete [risk snapshot](risk/), ten files byte-verified against [source.bundle](source.bundle) |
| Integration source | `97176da382659153165d84c0f76ade21903dfc38`, ticket B, retained bundle's `refs/heads/integration`; risk C remains unintegrated |
| Guidance checkout | `02d76205a1c40e45c607ef2a5d11ec282393edcd`; applicable working-copy guidance identities below, including uncommitted guidance |
| Approved miniature contract | [CONTRACT.md](risk/CONTRACT.md), [A](risk/ticket-A.md), [B](risk/ticket-B.md), [C](risk/ticket-C.md); supplied review assignment and repository AGENTS instructions |
| Prior observations | Read original [A Spec](a-spec.md), [A Standards](a-standards.md), [B Spec](b-spec.md), [B Standards](b-standards.md) as earlier scope. They report no findings at their own revisions. No prior unresolved keys, repair verification, risk acceptance or scope amendment was supplied. |
| Original evidence | [Fresh identity and observation capture](cumulative-risk-observations.json); this original report's digest belongs in an external capture manifest |

## Inspected and omitted scope

Inspected every file in the exact risk source: empty `ticket_harness/__init__.py`, `run.py`, `checks.py`, `approval.py`, `restore.py`, `observe.py`, `CONTRACT.md`, and tickets A/B/C. Read the whole cumulative baseline-to-source diff and the unchanged owner/consumers. Searched all gate definitions and usages, then followed initialization, recording, reads, restoration and revocation. There is no omitted file in the assessed source.

Excluded the real harness implementation/CLI/suite, real M1 assessment, future runtime checkpoint enforcement, malformed-input/concurrency policies and external clients absent from the fixture. This tiny fixture has no serializer, filesystem persistence, repair-policy engine or additional review-stage implementation to inspect; their absence is explicit rather than assumed coverage. No clean snapshot or clean report was opened. Shared manifest/reference metadata exposed later revision identities. Reading fixture-builder provenance incidentally exposed its later repair-generation block; that later code was not assessed, executed or used as evidence of a repair here. This report's defect and remedy follow directly from the risk source and existing contract.

## Substantive assessment

The contract puts canonical gate truth in Run and requires later revocation to reach every consumer. Ticket A preserves the existing dictionary interface; B adds readiness as current checks AND approval; C specifically requires one authoritative restored gates mapping shared by run and review consumers. This is a concrete ownership contract, rather than a preference for a class layout.

The existing [Run](risk/ticket_harness/run.py) owns fresh initialization (`__init__`, lines 2–3), recording (`record`, lines 5–6), and invalidation (`revoke`, lines 8–10). Each operation acts on one gates dictionary. The only committed entry caller, [observe.py](risk/observe.py), creates Run, records booleans through its operation, invokes revocation and reads through both consumers. [checks_ready](risk/ticket_harness/checks.py:1) and [candidate_ready](risk/ticket_harness/approval.py:1) read their supplied object's current dictionary on each call; neither caches truth, writes it, accepts a milestone or promotes source. This remains a small, useful interface for ordinary live Runs, consistent with the earlier A/B assessments and ADR-0002.

[Restoration](risk/ticket_harness/restore.py:4) breaks that ownership. It reads the saved-shaped `data["gates"]` mapping, copies it into a new namespace, then copies that namespace's dictionary into another namespace. Thus restoration is an additional initialization writer outside Run and creates two independently writable representations. Neither returned value has Run's recording/revocation operations. No stored owner identifier, reference reconstruction, synchronization operation or later invalidation propagation joins those copies. A caller must know to invoke an unbound Run method or mutate dictionaries directly even to invalidate the first value, and must separately coordinate the other copy. That interface leaks the invariant's implementation to callers and loses locality.

The consumer functions are unchanged and correctly return the current dictionary they receive; they cannot tell that the review dictionary has become stale. Calling `Run.revoke(run)` mutates every first-dictionary entry to false, while both review consumers still return true. This produces false candidate readiness after canonical revocation and defeats both C's explicit sharing requirement and the overarching contract. The passing local A/B observer cannot disprove it because it never calls restore. This is the single blocking finding F1 below; missing owner operations and copied review truth are related manifestations of that restoration breach, not separate repair demands.

There is no durable save operation in this source. The only supplied representation is `{"gates": {"checks": bool, "approval": bool}}`, passed to restore by the external observation. Its copy from the input mapping may legitimately separate saved data from live mutations; the defect is the second live truth source and failure to reconstruct the named owner. The fixture specifies no general schema rejection or partial-restore failure policy. I do not introduce such a requirement or claim missing malformed-input tests as another blocker. In the observed valid-input flow, restoration returns both values normally and records no failure; later revocation silently leaves the review copy ready.

### Trigger and change-locality assessment

At C start, persistence/restoration **yes** and shared mutable gate state **yes** are established by ticket C and its required identity reconstruction. A new restore/reconstruction lifecycle **yes** and an additional initializer/writer **yes** follow from adding that path to existing Run-owned state. After implementation, all remain **yes**: `restore.py:5–6` initializes independently mutable gate dictionaries and bypasses Run initialization. The shared-state trigger describes the affected responsibility even though the implementation incorrectly splits its identity. Ordinary A/B review remains independent; C's broader checkpoint gates integration. The fixed first-feature baseline comes from the root commit, its explicit contract, builder initialization provenance and A→B→C ancestry, not an inferred accepted milestone or an arbitrary repository root.

For a plausible added review gate `security_review`, the present contract would require coordinated concrete edits: Run's initialization must establish the new gate false; the responsible stage caller must record its result through Run; `candidate_ready` must require it alongside checks/approval, while `checks_ready` retains its narrower question. Any save producer must include the new gate in the saved mapping, and restore must reconstruct its value into the same canonical owner observed by both returned consumers. No save producer exists here, so one must be identified if the feature is actually extended; inventing a serializer is not part of this review. Compatibility for an older representation lacking the new gate needs an approved decision (for example fail closed or reject), rather than accidental lookup behavior.

Invalidation already loops over all current Run keys, so a properly initialized additional gate is revoked without a new invalidation path. Under the risk design, changing only the readiness expression is insufficient: restoration still forks every gate and invalidation still misses review state. Regression observations should cover restored pending/passed new-stage values and successful readiness followed by revocation through the existing owner operations, checking both returned consumers. Existing A/B ordinary-Run observations should remain. A change to repair policy that invalidates only some outcomes would likewise belong in an explicit Run operation, with callers invoking it and restored consumers seeing the same transition, rather than each caller editing its own copy. This trace explains why retaining a single owner gives locality and why a general adapter hierarchy or wholesale consumer rewrite is unnecessary.

## Evidence audit

Commands inspected the retained bundle through an isolated bare clone `/tmp/fixture-cumulative-risk-review.git`:

```text
git clone --bare --quiet .scratch/ticket-harness/evidence/18-walkthrough/source.bundle /tmp/fixture-cumulative-risk-review.git
git --git-dir=/tmp/fixture-cumulative-risk-review.git log --format='%H %P %s' BASELINE..SOURCE
git --git-dir=/tmp/fixture-cumulative-risk-review.git rev-list --parents -n 1 BASELINE
git --git-dir=/tmp/fixture-cumulative-risk-review.git diff BASELINE SOURCE
rg -n 'gates|record|revoke|restore|ready' .scratch/ticket-harness/evidence/18-walkthrough/risk
```

All succeeded. BASELINE/SOURCE are the full identities above. The baseline has no parent; source ancestry is baseline→A (`5fa532d42205f6569918f7584cc2f6c3e52be603`)→B→risk C. The bundle advertises integration at B. The identity driver compared the complete ten-file snapshot inventory and each file's bytes with `git show SOURCE:path`, then checked every SHA-256 against the risk entry in `sources.json`; all matched. The manifest's risk entry plus retained observation JSON records each source file digest. These checks establish source identity, not architecture quality.

Read Python environment and testing policy before execution. Used the documented shared environment's absolute `bin/python`, `-B`, fixture cwd and explicit fixture `PYTHONPATH` for the restoration observations. [Captured commands, cwd, environment, exits, stdout and stderr](cumulative-risk-observations.json) show:

| Observation | Result | Meaning |
| --- | --- | --- |
| Risk source `observe.py` | Exit 0; A/B PASS | Existing direct-Run transitions remain valid; no restore coverage |
| External `observe-risk.py` against risk | Exit 1; review check/readiness both true after canonical false | Reproduces stale restored readiness, ending at its expected revocation assertion |
| Fresh inline owner/consumer diagnostic | Exit 0; `run_is_Run`, shared gates, record/revoke methods all false; first owner false/review true after revocation | Corroborates actual identity, operation loss and the unchanged readers' behavior |

The first audit-driver attempt failed its own expected exit-vector assertion before saving evidence: its inline diagnostic used repository-root cwd, allowing current-directory import shadowing. Repeated all commands with fixture cwd and retained the successful capture; no source was changed. A separate direct run of the supplied risk observer also reproduced its assertion failure. A later digest command mistakenly requested nonexistent `observe-risk.md`; that path typo did not affect source or observation results.

No source or tests were modified. Focused observations at the miniature's existing callable/observer surface are appropriate for this review; this does not replace the real harness's approved CLI testing seam or any implementation completion gate. No full harness suite, packaging, strict-type, concurrency or production-checkpoint result is claimed. Hashes and passing earlier observers do not supply the substantive ownership conclusion above.

Guidance read-content SHA-256 identities at the recorded checkout:

```text
ade77403240a3a8b863ab1740b01e2e6ef12234b08b0d4f87a83897d72269876  docs/agents/domain.md
7bef209024464c7ce7b0d3ebcfc8f2707d2309efef50b79bb7d5cc589ab1aa56  docs/agents/ownership-review.md
7371c706ba48a09ba2f69750dab8f60c5c6892bdfb0ecb35f5f9ada7e502d49d  docs/agents/review-records.md
e81bfaff325e069ee3b8c73a8a4d2028e06a871dcf94f6045377585a5d1e3d8f  docs/agents/architecture-checkpoints.md
6b6b498a718205bb5fd1f0b12410623807e708f784e7d09a4bd72343b229a4ff  docs/agents/testing.md
dc357dd6bf10406d9a16b3beb40455f9262a7d3922fa4f1e138a6547a45efd8d  docs/agents/python-environment.md
4b45856348181d3383d3b2416d56eb0261243ddab8507fb869dd4bdee39bdefc  GLOSSARY.md
6e4adc64a9a454d00ca4d16649796daf525783e554d1dc892bd0654b5990e603  docs/adr/0001-reusable-harness-and-local-integration.md
7f9ef955940b6a4315d9a5fc7c7279cc367043310ebd4575cee450dffd0e4982  docs/adr/0002-human-qa-gates-feature-promotion.md
2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2  .agents/skills/matt-pocock/codebase-design/SKILL.md
3a0a0f667aaa65ae8a74b2c7f3ab0e24517e756ed1a5663f35623bc46c8fc816  .agents/skills/custom/test-strategy/SKILL.md
```

Bundle SHA-256: `5c8626d8074871fee2e7bdb37d13bb1628af36f535d93404341d499be457531e`. Source-manifest SHA-256: `03d363e16858a504c189dbf029300b5549e777b141bd7fa8c4661246f6cb85c7`. Observation-capture SHA-256: `bca5bb0d17d8edc9061cde50fb1a36cd48193267f486413bbaf6e2cc2afd7c98`. Assignment prompt has no separately retained snapshot; actor/task identity identifies delivery context without inventing a prompt digest.

## Findings

### F1 — blocking: restoration forks canonical gate truth and drops owner operations

Full key: `review-18-fixture-cumulative/standards-risk-01/F1`.

At [restore.py:5](risk/ticket_harness/restore.py:5) and line 6, independent `dict` calls create detached live mappings under namespaces. This contradicts [ticket C:2](risk/ticket-C.md:2) and [CONTRACT.md:2](risk/CONTRACT.md:2). The Run-owned invalidation operation at [run.py:8](risk/ticket_harness/run.py:8) changes only the first mapping when explicitly applied; the unchanged checks/readiness readers subsequently report true from the second. The fresh retained observation demonstrates that exact consequence, and the namespace return also removes ordinary `run.record`/`run.revoke` operations from the restored value.

Proportionate remedy within the existing ownership contract: reconstruct a real Run through its initialization/recording operations, and supply the restored run/review consumers the same authoritative gate state with owner operations retained. Keep the existing read-only consumer functions unless a demonstrated requirement changes them. Do not synchronize copied dictionaries at each reader or introduce another owner. Extend the focused restore observation to revoke through the restored owner's normal operation and assert both check status and candidate readiness become false from both returned references. Preserve the ordinary A/B observer, and independently review the repaired exact revision from the same original baseline. Saved input should remain detached from live state; sharing is required between live consumers. This report authorizes no ownership-contract amendment and asserts no repair has occurred.

Optional suggestions: none. Finding is open in this original observation; no consequential risk acceptance, blocker deferral or human decision was supplied.

## Assessment result

This cumulative Standards assessment is **completed**, with one unresolved blocking finding. Defined source inspection and original report are finished; assessment completion does not resolve F1. C integration/readiness remains blocked pending an authorized repair and independent exact-source verification, or the applicable explicit human decision/amendment. Integration remains at B. No candidate is declared ready for human QA, no milestone is accepted, and no real M1 architecture assessment or acceptance is performed by this isolated fixture review.
