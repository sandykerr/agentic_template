# Review-folder deletion audit

2026-11-16. User objective: fewer files and less repeated content. All 16 files in
`.scratch/ticket-harness/reviews` assessed: 862 lines, 93,190 bytes. Root reviewed
three independent GPT-6.1-Sol Medium worker proposals against scoped files and
retained evidence. This is an audit recommendation, not deletion/merge approval,
a source-code review, finding resolution or milestone acceptance. Nothing deleted.

## Recommended batch

**Eleven files are conditional removal candidates; five should stay. No file is
ready for blind deletion with its current references unchanged.** Gross candidate
content is 54,825 bytes / 533 lines; net savings depend on preserved merged text.

| Files in reviews/ | Recommendation | What must survive / happen first |
| --- | --- | --- |
| `ticket-24.md` | First removal candidate | Results, all three review rounds, original full keys and exact fixes already survive in `evidence/ticket-24/24-completion.md`, original reports/captures and `24-finding-history.md`. Redirect maintained assessment links to the surviving ticket evidence index/completion; retain a compact assessment-ID/source/report entry in the review index. |
| `M1-human-readability-01.md` | First removal candidate | Original judgment already survives in `evidence/m1-human-review-01/root-01.md`; human request/response in `docs/human_qa/m1_review.md`; source/settings/check records and M1 history Events02–03 retain scope and limits. Keep a compact assessment entry and redirect maintained navigation. |
| `ticket-16.md`, `ticket-17.md`, `ticket-18.md`, `ticket-19.md`, `ticket-20.md`, `ticket-21.md`, `ticket-22.md`, `ticket-23.md` | Remove after merging unique material | Preserve their numbered A-events verbatim in existing `evidence/ticket-NN/README.md` files, labelled historical assessment history. Retain identity/baseline/source/report/settings/omission pointers so each distinct assessment remains navigable. Independent originals and finding histories remain in place. |
| `M1-index-repair-01.md` | Remove after merging unique material | Preserve distinct repair assessment ID/baseline/source/axes and dated assessment-history entries in a named subsection of `M1-architecture-01.md`. Keep the cumulative baseline distinct from the repair baseline. Redirect maintained repair links there. |
| `README.md` | Keep | One maintained review index. Shorten repetitive status prose; link to original reports/completion records rather than adding new summaries. |
| `M1-architecture-01.md` | Keep | Canonical cumulative work item, accepted-source/baseline provenance, report links and exact human QA decision. Repeated historical pending-state narration is a further shortening opportunity; retain unique history and provenance. |
| `M1-architecture-01-history.md` | Keep verbatim | Unique append-only full-key disposition history, Events01–06. Later clean reports do not replace it. |
| `ticket-25.md`, `EC1-capture-architecture-01.md` | Keep for this batch | Active repair/fresh reviews, open keys and distinct routine/broader gates. Initial tables and later appended outcomes describe different stages. Consolidation can be reconsidered after current review bookkeeping is settled. |

That batch reduces the reviews folder from 16 files to 5, using existing destination
files. It creates no new permanent per-ticket replacement documents. The first two
candidates total 7,175 bytes / 45 lines; the nine merge-dependent candidates total
47,650 bytes / 488 lines. These are removal sizes, not promised net content savings.

## Reviewer checks and boundaries

The ticket assessments are aggregate wrappers, not the original independent
judgments. Original Spec/Standards reports, M1 cumulative judgment, actual human
approvals, finding histories, unresolved failures and unique uncommitted-source
identities remain protected. Historical “M1 pending” text is not a current blocker:
M1 acceptance at `88e4cd8` is recorded in the actual QA decision. Preserve historical
scope when condensing navigation.

Before removals, compare the concrete merged output to originals and obtain any
required human merge approval. Update maintained feature/review/evidence indexes
and `next_agent_prompt.md` links. Add explicit old-wrapper-to-survivor mappings in
the existing `evidence/README.md`; its ticket-evidence relocation rule does not
cover these wrapper deletions. Preserve immutable report/history bytes rather than
rewriting historical links. A path mapping cannot satisfy an active exact-path or
frozen-input reader: confirm those dependencies have ended before executing.

No merged replacement was written or approved in this audit. The guarded retirement
executor is not available as a demonstrated implemented workflow here. This report
confers no execution approval and changes no authoritative assessment/approval
arrays. It does not require weakening the evidence policy to recommend
consolidation; preserving distinct review IDs does not require separate files.

## Evidence and inspected limits

Original worker proposals, unchanged:

- [Tickets 16–24](../worker-tickets-ccaaf69841234580b2ffb1410bd7bd9d/proposal.md).
- [M1 assessments/history](../worker-m1-b8c733c9cb87435998c8616f75d3c24d/proposal.md).
- [Index and active ticket25/EC1](../worker-current-04842cc83a674888a944ba8b674e4ac5/proposal.md).

Root independently read all 16 scoped files, governing review/retention guidance,
ADRs/glossary, ticket16/24 evidence navigation and completion, M1 original root
review and final review navigation, and actual human-request/response excerpts.
Compared all worker recommendations to these survivors. Accepted their conditional
classifications; excluded workers' long-term ticket25/EC1 consolidation from this
batch because those records are active. Exact independent report bodies/archives
were not exhaustively reread or extracted. This is retention analysis, not renewed
implementation verification. Broad reference scans have limits noted by workers;
root independently checked named maintained and historical consumers. No tests
were warranted for the audit; no source, existing review, history or approval was edited.

[Source/instruction manifest](source-manifest.sha256), SHA256
`4078ab7e1734a652863048168fe2b11c35285aa0438e58f3d9eeca6605ca9e5f`,
binds the dirty working-tree review files separately from HEAD. All 22 manifest
entries rechecked unchanged after worker review. Checkout HEAD moved from
`3b0c1ab7ec41929d3febab44269f791e55897e70` to
`febd86321851e2acec994237f9d1a1adea824c55` during this audit due to other work;
scoped file identities stayed unchanged. Worker model/reasoning were explicitly
configured as requested; backend delivery/context telemetry unavailable. Root is
the parent reviewer; no independently measured root settings claimed.
