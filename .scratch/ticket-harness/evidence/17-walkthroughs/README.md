# Four isolated ownership-review walkthroughs

These are actual fresh development reviewer assignments against representative
Git sources, not generated reports or runtime harness agent calls. Each evaluator
received only its own isolated repository/contract, fixed baseline/candidate,
three frozen guidance texts and the generic retained assignment. The parent
prepared the fixtures from ticket17's four required scenarios, kept the ticket,
spec/case descriptions and expected outcomes out of evaluator context, and did
not supply sibling conclusions. No guidance revision or trial was discarded. Initial D exposed a real sparse-array
contract bug in the intended acceptable fixture; it is retained unchanged. The
fixture-only correction is assessed in a fifth fresh assignment, D2, with the
original D baseline and the same guidance.

## Identity and independence

[Source manifest](sources.json) retains full Git identities and source/diff/bundle
hashes; each `source.bundle` contains the baseline/candidate history. Baseline and
candidate snapshots support inspection without restoring the bundle. All contracts
are explicitly representative approved contracts within their fixture, not new
human decisions for this repository. [Guidance manifest](guidance-identities.json)
identifies the actual frozen content delivered. Snapshots preserve the exact
original bytes, including relative links from their original locations; reviewers
were instructed to use the supplied texts without following those links. The live
originals supply navigable links and are checked by the document audit.

Each `assignment.json` retains the exact initial `spawn_agent` fields and prompt;
`assignment.txt` is its readable message. All five initial assignments used `fork_turns=none`, model
`gpt-6.1-sol`, reasoning `high`, context target <=250000. These are actual parent
spawn configurations, not independent provider/backend telemetry, which was
unavailable. Each reviewer reports its own observed source, scope and input hashes.
The assignment/report capture manifest is [capture.json](capture.json).

A/B launched first in separate slots; C launched after A's finished report, D after
B's. Every assignment excluded other cases, parent sources and sibling reports.
The [follow-up messages](followups.json) retain administrative confirmations and
separately identified post-report supplemental requests. Initial assignments
supplied no expected source findings. C’s later proposal classification was
requested after preserving its initial independent assessment. Each original report was written outside its source
repository, copied verbatim after completion, then hashed externally. D contains
Markdown hard-break trailing spaces: its exact original bytes are retained in
[report.raw.md.gz](case-d/report.raw.md.gz), with an explicitly labeled normalized
display at report.md. Decompression identity is checked; semantic content is
unchanged. All other initial report.md files preserve original output bytes. Aggregation
below followed report capture. Source repositories remained unchanged/clean.
These Standards walkthroughs are separate from the final whole-ticket
independent High Spec and Standards implementation reviews.

## Observations and criterion mapping

| Required walkthrough | Original assignment/report and source | Actual observation |
| --- | --- | --- |
| Unchanged caller hiding a second writer | [A assignment](case-a/assignment.txt), [contract](case-a/candidate/CONTRACT.md), [diff](case-a/change.diff), [original report](case-a/report.md) | F1 blocking: unchanged urgent submission edits owned capacity directly and can make it negative, despite the owner-mediated ordinary path and correct new cancellation operation. Report traces all writers and distinguishes the expressly authorized cancel exception. |
| Restore/invalidation outside the diff | [B assignment](case-b/assignment.txt), [contract](case-b/candidate/CONTRACT.md), [diff](case-b/change.diff), [original report](case-b/report.md) | F1 blocking: unchanged restore spreads canonical records into detached verified copies, so source replacement leaves readiness stale. F2 blocking: unresolved verified IDs restore without rejection. Both are concrete contract breaches with scoped remedies. |
| Ownership breach versus optional design suggestion | [C assignment](case-c/assignment.txt), [contract](case-c/candidate/CONTRACT.md), [diff](case-c/change.diff), [original report](case-c/report.md) | C F1 blocking: the new caller writes completion status without the required event. A separate [proposal assessment](case-c/proposal-assessment.md) classifies private lifecycle storage/read-only observations as an evidence-supported optional suggestion, not a required correction or added finding. Original report remains unchanged; a filename alias preserves its raw supplemental link. |
| Justified clean long cohesive function | Original [D assignment](case-d/assignment.txt), [raw/report display](case-d/report.md); repaired [D2 assignment](case-d2/assignment.txt), [contract](case-d2/candidate/CONTRACT.md), [diff](case-d2/change.diff), [independent original report](case-d2/report.md) | Initial D found a real sparse-array defect, not a length/style issue. The 79-line function remains cohesive after its narrow correction; fresh D2 records zero blocking/optional findings and explains the single pure validation responsibility, local scratch ownership, independent outputs and caller contract. |

D’s original finding and fixture-only correction are connected through its
[append-only history](case-d/history.md); supplemental exact-source verification
follows the preserved independent D2 report. No guidance change was needed.

The A/B/C concern findings are intentionally retained in representative sources; this
read-only walkthrough authorized neither fixture repairs nor acceptance of risk.
Their report-local/full keys and open classifications remain in the original
reports, with no claimed fixed/deferred/accepted disposition or exact-source repair
verification. They are not real unresolved harness findings or an M1 assessment.
Any future fixture change would need independent exact-source revalidation before
reusing a report as current evidence. No actual human QA decision was authored.

The finite observations demonstrate this guidance's use on these inputs. Broad
calibration, a fixed concern/control corpus and repeated evaluation are ticket19;
runtime capture/enforcement and real backend delivery remain later work. No claim
of guaranteed future reviewer detection or runtime effectiveness is made.
