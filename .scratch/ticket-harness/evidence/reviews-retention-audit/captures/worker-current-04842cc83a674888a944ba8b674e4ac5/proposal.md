# Current review-record retention proposal

Original worker proposal; assessment only, no deletions or shared metadata changes.
Configured worker: GPT-6.1-Sol, medium reasoning, as assigned by parent. Backend enforcement and measured context telemetry are unavailable; these are configuration facts, not independent delivery measurements.

## Classification

| Scoped file | Recommendation | Concrete reason / prerequisite |
| --- | --- | --- |
| `reviews/README.md` | **Keep** | This is the maintained feature review index required by `docs/agents/review-records.md`, linked by feature README and retained M1 QA/review material. It is navigation/current summary, not an original independent report. It is the natural survivor for a consolidation that actually removes wrapper files. Its historical ticket rows must retain their historical milestone scope; the accepted M1 row/decision governs present M1 outcome. |
| `reviews/ticket-25.md` | **Delete after a retention-preserving merge and navigation repair; keep now** | A mutable assessment wrapper, not an independent review report. Preserve its distinct assessment ID, fixed baseline, origin, four triggers, gate, settings/limits, scope/omissions, reports, and initial `T25-E01` event before removal. Open findings, active fresh review and immutable inbound links prevent immediate deletion. |
| `reviews/EC1-capture-architecture-01.md` | **Delete after a retention-preserving merge and navigation repair; keep now** | Another mutable wrapper, not the original broader reviewer report. Preserve distinct assessment ID, ticket baseline versus accepted-M1 cumulative provenance, gate, settings/limits, all-package scope and omissions, original results, and `CAP-ARCH-E01` event. It remains required early triggered work, distinct from future full EC1 milestone assessment. |

No scoped file qualifies for delete now. The two conditional removals save two files / 7,742 bytes before merged text; no independent report, human decision or finding history needs removal to achieve that reduction.

## Exact surviving content and consolidation

Use anchored assessments inside `reviews/README.md` (`#review-ticket-25` and `#review-ec1-capture-architecture-01`) while preserving two work-item identities and separate routine/broader scope. A compact row alone is insufficient: retain required assessment fields or explicit links supplying them. Move the original initial events `T25-E01` and `CAP-ARCH-E01` verbatim into an append-only section of `evidence/ticket-25/25-finding-history.md`, or preserve them verbatim under the merged index assessments; retain attribution and source. They are history embedded in otherwise mutable wrappers. Do not replace them with an invented present-day event.

Retain these existing authoritative survivors unchanged:

- `evidence/ticket-25/captures/spec-01-022e9f1dd5e848898262e2756d5e8cd0/report.md` — original Spec judgment, one blocker.
- `evidence/ticket-25/captures/standards-01-7c21c95b670c413ca133af2548ac8c9b/report.md` — independent Standards judgment, two blockers.
- `evidence/ticket-25/captures/architecture-01-0aac4966262540eb9a7774ddd84c56ad/report.md` — independent broader High Standards judgment, two blockers, all-eleven-package/affected-guidance scope.
- `evidence/ticket-25/25-finding-history.md` — five distinct full keys, original blocking classifications, open dispositions, affected source, owner-local repair authority and pending independent verification; shared symptoms do not collapse independent keys.
- `evidence/ticket-25/25-review-round1-digests.sha256`, retained report probes/observations, and `25-review-spec-01-envelope.md` — original identity and corrected navigation without rewriting the Spec original.
- `evidence/ticket-25/25-evidence-index.md`, `25-review-context.md`, `25-review-round2-context.md`, `25-repair1-assignment.md` and their linked retained inputs/checks — canonical source, repair and current review context.
- `evidence/m1-final-review-01/m1-qa-decision.md` and linked actual human-decision records — actual M1 authority at `88e4cd8aabc78e76e66efc02983fec3900ab0a23`, not authority for EC1 acceptance.

The wrappers largely repeat the canonical index, original reports and finding history. Unique structured work-item metadata and their two initial events are the loss risk, rather than unique independent reasoning. Their initial tables still say reports are pending/no findings although appended round1 sections record completed inspections and five open blocking keys. Consolidation should present current summary separately from retained initial events. The canonical index now identifies repair HEAD `febd86321851e2acec994237f9d1a1adea824c55`, actual 589/full result with interrupted/recovered remaining checks, and pending fresh exact-source review. This audit does not verify those check claims or mark original findings fixed. Historical round1 assessed source is `3b0c1ab7ec41929d3febab44269f791e55897e70`.

## Inbound consumers and removal conditions

Repo-wide hidden-file searches found actual wrapper links in all three original reports, `25-finding-history.md` (five EC1 links), `25-review-spec-01-envelope.md`, and the ticket wrapper's links to EC1. Source/instruction manifests and inventory/proposal data also mention both paths; these identify historical states, not necessarily live readers. The Spec original has a known relative-link typo already corrected by its envelope.

Keep immutable original reports, snapshots, manifests and history events unchanged. Before removal, add an explicit historical wrapper-path-to-surviving-anchor mapping to the existing `evidence/README.md` historical-navigation section, and update mutable navigation/envelopes with exact surviving anchors when authorized. Existing ticket01–24 relocation rules do **not** cover these review wrappers. Existing original references then remain historical and have a documented resolution path. Do not claim all original links remain directly usable after deleting their target. If a live/frozen consumer requires exact wrapper bytes/path, defer removal until that dependency ends; a mapping cannot satisfy a required machine-readable/frozen-path dependency.

Current fresh-review context says product source is frozen pending routine axes and tells reviewers to read original reports/history. This does not establish a running harness or prove the wrapper paths are frozen inputs. Inspect current allocations/assignments and captured input identities before changing tracker/navigation; uncertainty means keep now, not automatic permanent retention. Prefer consolidation after active review bookkeeping can be changed without invalidating supplied identities. Required same-source independent review and future EC1 QA remain separate gates.

## Inspection identity, commands and limits

HEAD observed: `febd86321851e2acec994237f9d1a1adea824c55`.
Scoped input SHA256 / bytes:

- `reviews/README.md`: `9de156da950a535203f7280e73e73a60d54b26b4d0bdf49fd1693541ffdc8a0c`, 6572.
- `reviews/ticket-25.md`: `ea38d9bf9e22781ee1ce8f5f0de7c97d7c6bf9ce25b463edf4ed35f4b4d9c036`, 4005.
- `reviews/EC1-capture-architecture-01.md`: `6311bd5568936f616999533c067b575abe0748512829ed2be6cb0f5da81ebc69`, 3737.

`git status --short` showed both current wrappers untracked; feature/evidence/archive README, spec/milestones, AGENTS and planning/handoff files modified; workflow spec, ticket25 evidence and replacement ticket bundle untracked; earlier planning files removed. Thus HEAD alone does not preserve scoped wrappers or current approved inputs. No claim of recoverability from Git is made.

Read AGENTS, GLOSSARY, both ADRs, review-records and issue-tracker guidance, evidence-workflow retention/navigation clauses, full evidence README historical mapping, three scoped files, original report envelopes/findings/substantive portions, ticket25 finding history, canonical index, original/round2 contexts, repair assignment, Spec correction envelope and actual M1 decision. Used `cat`, `sed`, `git rev-parse HEAD`, `git status --short`, `wc -c`, `sha256sum`, and repo-wide `rg --hidden` references excluding `.git`, `.venv`, cache directories. First broad `rg -n` output was enormous/truncated because captured JSON embeds prior content; repeated with filename-only search and bounded Markdown lines, including captures, to identify concrete consumers. Original combined report output also exceeded output budget; assessment relies on observed envelopes, relevant findings and histories rather than claiming every report word was independently reread. No tests, Python, source-code review, deletion, source edits, sibling proposal reads or shared JSON writes. No claim of exhaustive arbitrary path-alias detection or active/frozen-input verification; those remain explicit execution prerequisites. Scope excludes the other thirteen review files and retirement of linked evidence.
