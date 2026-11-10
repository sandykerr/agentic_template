# Finding history: {{review ID}}

Template: [record contract](../../agents/review-records.md). Append events;
preserve prior entries. Keep current dispositions in the assessment summary.
Use one event per full key; connect superseding/reopened report observations.

## {{unique event ID}}

| Field | Value |
| --- | --- |
| Finding | {{review/report/local ID; original report anchor}} |
| Disposition | {{open / fixed / deferred to linked ticket / accepted with reason / awaiting human decision}} |
| Actor and role | {{actual actor/assignment or attributed human, event context/time if known}} |
| Affected revision | {{exact source; old verification stale/pending if changed}} |
| Reason and evidence | {{reason, source/evidence links; retain original blocking/optional classification}} |
| Previous / superseded observation | {{event/report full-key link or initial observation}} |
| Repair or implementation ticket | {{link or explicit absence/reason}} |
| Repair commit | {{full commit and retained evidence link or pending/not applicable}} |
| Independent verification | {{reviewer identity; exact verified revision; report/evidence link, or pending}} |
| Human decision / amendment | {{explicit decision and approved amendment links when required; otherwise why not required or pending}} |
| Milestone assessment | {{link or pending/not yet performed}} |
| Next action | {{responsible actor/workflow; remaining concern or verification}} |
