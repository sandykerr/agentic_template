# Retention decisions from the human

These decisions continue the M1 human QA planning discussion. They establish the
direction of the proposed retention policy; they do not publish a revised spec,
implement a skill, or record that cleanup has happened. Read the
[cases and tradeoffs](README.md#concrete-cases-for-choosing-retention) with the
[runtime dependency audit](worker-runtime.md).

## Scope and purpose

The human agreed to simplify navigation and reduce future GitHub repository
growth, covering both development evidence and harness-run evidence. Removing
existing Git history remains a separate decision. Lasting decisions and development
directions should be recorded; command noise, unnecessary run records and old bug
reports may be removed. Handling should depend on the kind of evidence and its
actual uses, with standing rules suitable for an autonomous harness.

## Decisions on the ten cases

| Case | Human decision | Meaning for the proposed policy |
| --- | --- | --- |
| C1: caches and temporary tools | Agrees with the assessment; caches are usually easily recreated. | Generated caches may be removed when no longer in use. For authored scripts, first preserve reusable logic or useful results and finish any remaining uses. |
| C2: passing command output | Agrees; exact output is usually unnecessary after success. Explicit preference: delete after the ticket finishes. | Save the useful result and code identity, then delete routine output at verified ticket completion. How to reconcile this timing with current QA/checkpoint dependencies remains a design question. |
| C3: interrupted/environment failures | Agrees; once a run succeeds and useful persistent information has been recorded, failed-run details are normally unnecessary. | Remove resolved failed-attempt details after the needed successful check and knowledge capture. Unexplained failures and unresolved bugs are still handled as open work. |
| C4: bug reports and repairs | Agrees with the assessment. | After independent verification of the fix, preserve the corrected requirement, lasting decision and useful regression protection. Remove old report/repair details after their remaining review/QA uses finish. |
| C5: repeated test observations | Logs of the same suite are not useful after the full suite completes; keep only essential elements. | Retain essential verification results and observations still needed for unresolved issues or acceptance. Avoid retaining every intermediate run or a complete raw final-run archive by default. |
| C6: compatibility examples/packages | Favors removing compatibility wrappers. Intended audience is almost exclusively the work team; extended development and thorough public maintenance are not intended. | Reduce backward-compatibility obligations. This introduces a software-support decision beyond evidence retention; the scope of removed wrappers, formats and old stopped-run support remains to be clarified. Treatment of tested package copies is not separately resolved by this statement. |
| C7: reviewer/agent evaluations | Agrees with the assessment. | Preserve useful guidance changes, limitations and relied-on results. Remove superseded original reports/transcripts after their conclusions are recorded and their remaining uses finish; retain reusable evaluation examples only when future evaluation needs them. |
| C8: operational run/QA files | Agrees with the assessment. | Preserve files needed by active or deliberately continuable runs, plus completion records still read by later runs. Remove working files when those uses end, keeping the agreed completion and actual approval records. |
| C9: code/instruction copies | Agrees with the assessment. | Prefer a verified Git reference to an extra copy where it preserves the required version. Protect the only copy of uncommitted or external content until its uses finish or the necessary content is saved elsewhere. |
| C10: lasting decisions/directions | Agrees with the assessment. | Record decisions, reasons, authority, scope, exceptions and unresolved follow-up in maintained documents or the tracker. Old surrounding reports/transcripts need not remain once their other uses finish. |

Rerunning a command can produce a new observation. It does not recover its exact
historical output. The policy deliberately accepts losing that historical detail
where the retained useful result is sufficient.

## Remaining decisions

- What compatibility support should actually be removed, and what must continue
  to work within the current supported version?
- How should the runtime permit C2's ticket-completion cleanup without breaking
  C8's active QA and continuation needs?
- What should autonomous cleanup do when it cannot establish that deletion is
  allowed, and who checks that lasting knowledge was recorded accurately?
- Where should the evidence skill be invoked, which existing guidance should it
  replace or share, and how should runtime enforcement be scoped?
- Which milestone should deliver these changes, and what human QA demonstrates
  the result?
- Should any retained bulk material be compressed or stored outside Git, and how
  should existing evidence be migrated under the new policy?

Approved oop-v2 / review-process-1 inputs remain in place. This note records human
choices and open questions so the next draft can reconcile the retention clauses,
compatibility clauses, tickets, skill routes and QA expectations together.
