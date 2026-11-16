# Original M1 review-record retention proposal

Actor: `/root/audit_m1_records`, 2026-11-16. Configured model/reasoning: GPT-6.1-Sol / medium per parent assignment; backend delivery telemetry unavailable. This is a read-only retention assessment, not independent source-code review, cleanup approval, deletion execution or new QA.

## Recommendations

Paths below are relative to `.scratch/ticket-harness/`.

| Scoped file | Classification | Concrete reason / prerequisite |
| --- | --- | --- |
| `reviews/M1-architecture-01.md` | **Keep**; shorten mutable duplicated status if desired | The canonical cumulative assessment identifies the accepted baseline for later milestone review (`88e4cd8` plus actual QA decision), distinct first-feature baseline `1a623ba`, original `d02e61e` assessment and renewed all-package High report. It is broadly consumed by tickets 10–24, milestone/feature/review indexes, docs and retained reports. It is a mutable wrapper, not the immutable independent report: much historical pending-state prose can be reduced using links to history and originals. Preserve assessment identity, origin, baseline provenance, source/settings, reports, omissions and accepted-source decision link. Keeping this existing canonical destination avoids unnecessary remapping and supplies the survivor for the two proposed wrapper removals. |
| `reviews/M1-architecture-01-history.md` | **Keep verbatim** | Six append-only events are unique durable finding-disposition provenance. They preserve the original blocking full key, distinct actors/sources, open/pending stages, repair authority, failed/partial verification distinctions, exact repair commit and Event06 independent fixed determination. New clean reports do not replace these events. Event06's then-pending QA describes its date, not present readiness. |
| `reviews/M1-human-readability-01.md` | **Delete after specific navigation update** | Bounded assessment wrapper, not root's original judgment or a human approval. Its substantive content survives in `evidence/m1-human-review-01/root-01.md`, `docs/human_qa/m1_review.md` (repository-relative), `evidence/m1-human-review-01/start.json`, `guidance.json`, `renewed-source.json`, `renewed-suite-result.json`, `renewed-static-results.json`, `worker-evidence.tar.gz`/manifest and history Events02/03. Root original explicitly records review ID, exact uncommitted-source limits, workers/settings, same ownership, inspected flows/omissions, 559/full and statics, observer repair and unresolved historical F1. No unique lasting judgment found in the 24-line wrapper. Replace its maintained index links with root original plus retained M1 assessment and explain this was the bounded historical correction. Remove obsolete present-tense pending-readiness wording from current navigation. Historical reports/history remain unchanged; document old wrapper path → original/root + M1 assessment in `evidence/README.md` historical navigation. |
| `reviews/M1-index-repair-01.md` | **Delete after retention-preserving merge and navigation update** | Wrapper overlaps `evidence/m1-final-review-01/README.md`, independent `spec-01-original.md` / `standards-01-original.md`, cumulative wrapper, worker notes and history Events04–06. Preserve its distinct repair work-item identity, original baseline `e2b0a26`, assessed `88e4cd8`/repair `e06eeaf`, four No triggers, independent axes, and actor/timing progression in a named repair subsection of surviving `reviews/M1-architecture-01.md`. Retain its 2026-11-13/16 assessment-history chronology (registration before readiness, verification completed while independent review pending, both originals collected before source changes, then actual QA acceptance), rather than silently discarding those entries as stale. Fresh reviewer checks merged content and required human merge approval applies under evidence-workflow spec. Redirect maintained repair links to that subsection; preserve report/history bytes and document the retired wrapper's historical mapping. |

No scoped file is recommended for immediate deletion. Two wrappers total 9,087 bytes / 87 lines; this removal is useful only after prerequisites, without adding equivalent extra files. The cumulative wrapper's repeated historical pending-state prose is also a content-reduction opportunity, but its append-only assessment history must survive rather than be casually rewritten.

## Survivors and differences checked

Actual retained original paths, not filename-based assumptions:

- `evidence/m1-qa-01/standards-01-original.md`: original High cumulative judgment introducing F1; immutable source-specific report, 32,129 bytes. Current cumulative wrapper is a different mutable aggregate.
- `evidence/m1-final-review-01/{spec-01-original.md,standards-01-original.md,cumulative-standards-01-original.md}`: distinct independent axes, 15,167 / 18,823 / 39,024 bytes. Read report envelopes and relevant baseline/ownership/inspection sections; originals describe reports' settings and omissions. Preserve all three, even though each has zero new findings.
- `evidence/m1-human-review-01/root-01.md`: original requested root review, 5,365 bytes, different from fresh independent Spec/Standards; preserves source/observer diagnosis/check and scope reasoning rather than just the wrapper's count.
- `evidence/m1-final-review-01/m1-qa-decision.md`, `human-demo-m1-decision.json`, `human-final-demo-and-development-decision.json`, `m1-acceptance-result.json`: actual request-specific approvals, conditional development acceptance and condition results. These survive. QA decision and actual final answer were inspected; a wrapper's acceptance statement cannot replace the approvals.
- `docs/human_qa/m1_review.md`: actual human request plus response and human code/documentation completion, explicitly distinct from candidate QA.

The original cumulative blocker and failed/partial campaigns are not active unresolved issues merely because their historical records say “open.” Current M1 is accepted at `88e4cd8` as recorded by actual QA. Conversely current policy ticket renumbering makes wrapper claims “M2 ticket25 next” obsolete navigation; current evidence-policy amendment has EC1 ticket25 next. Do not rewrite historical originals to fix that.

## Inbound references and preservation conditions

Repo-wide `rg --hidden --no-ignore` search excluded `.git`, `.venv`, `cache` and `__pycache__`; both content hits and filename-only searches were used. Initial normal `rg` respected ignored paths, so it was explicitly repeated with `--no-ignore`. The complete scan found 207 matching lines; huge generated one-line JSON inventories made raw output impractical, so follow-up Markdown search and bounded JSON inspection distinguished real consumers from inventory/status copies.

Maintained references requiring review before wrapper deletion: `reviews/README.md`, `reviews/M1-architecture-01.md`, feature `README.md`, `evidence/README.md`, `evidence/m1-index-repair-01/README.md`. Broad cumulative consumers also include `milestones.md`, issues 10–24 and `docs/ticket-harness/agents.md`. Keep the cumulative path stable.

Historical immutable references to removed wrappers include `M1-architecture-01-history.md` Events03/04/06, fresh Spec/Standards originals, prior retention provenance, repair brief, archived feature README and captured instruction/status/patch material. Leave those bytes unchanged; add explicit historical mapping in maintained evidence navigation. The existing `evidence/README.md` ticket-NN mapping applies to moved ticket artifacts, not M1 wrappers; it alone would not explain these new deletions.

`evidence/m1-index-repair-01/completion-records-check.json` includes repair wrapper in a historical `documents` list; inspection confirms it is a past bookkeeping result, not a current loader/read requirement. Captured `final-implementation.json` mentions review paths in historical Git status. Canonical final source/instruction manifest search found no wrapper path requirement. No active harness run or frozen-reader dependency demonstrated by this lightweight audit; final reviewer must resolve any such dependency discovered before action. A `(deleted)` label alone cannot satisfy a real required reader.

## Inspection provenance and limits

Source HEAD: `febd86321851e2acec994237f9d1a1adea824c55`. Four scoped files were clean tracked files at inspection. Relevant dirty governing inputs: modified `AGENTS.md`, modified `evidence/README.md`, untracked `evidence-workflow-spec.md`; feature README/spec/milestones/issues and archival moves/deletions also dirty from prior work. Untracked review `EC1-capture-architecture-01.md` and `ticket-25.md` are outside assigned scope. No existing dirty file was edited.

Scoped SHA-256:

- history: `e9f30fc7dc43a661035e44a77cb5afcb9958483ba7ea9ae3463264d511f395ad`
- architecture: `af6c9ab0131c8f5c4fbdd667f821e6d90ef2116bbb4ed12e2a39934bd6a42581`
- human readability: `29a63c4a7728edbd4ec96cce5ca8546f4754e53fd039169032a2a724cfe3095d`
- index repair: `6505ff3a101486612d9b246d11fe7ba4fbfd33d226ec318f5cd209f177f4ea93`

Governing dirty SHA-256: AGENTS `f2d28cd8b23a8f52f1478858c249670a7b5b144a5dd8175065e5cc63446e0a98`; workflow spec `39249bcbe071dd4d0f33d59c4b07293b41e2bf029ab28ecdaa54493ae1aa8b39`; evidence README `b9ea7ff44be3a3ef774b125a3fb62524fec2b3a7b7f86e46af28795a9f3639d7`.

Read AGENTS, GLOSSARY, both ADRs, review-records and issue-tracker contracts, complete four wrappers/history, evidence workflow retention/navigation/merge rules, evidence README historical mapping, review index, final and repair evidence indexes, root original and human response. Commands: `git rev-parse HEAD`, `git status --short` (whole checkout and relevant subset), `cat`, `head`, `sed`, `ls -l`, `wc -lc`, `sha256sum`, repo-wide `rg -n/-l --hidden --no-ignore` and scoped bounded `rg` JSON inspection. An ephemeral `/tmp/m1-review-inbound.txt` held search output; no repository evidence or shared JSON was modified.

Omitted: source-code correctness review, full archive extraction, exhaustive traversal of historical raw logs/JSON, runtime loader audit, tests/Python/compute workloads, draft merged file and cleanup execution. No new checks/results were produced. This original proposal is the sole assigned persistent output, created exclusively with shell noclobber; parent owns registration, synthesis and any final actions.
