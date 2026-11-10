# Review assessment: {{review ID}}

Template: copy into the feature's reviews directory and complete using the
[record contract](../../agents/review-records.md). Placeholders are authoring
instructions, not claims. Use relative links for saved records.

**Review lifecycle:** {{planned | in progress | completed}}

| Field | Value |
| --- | --- |
| Identity, purpose and scope | {{review ID; ticket assessment or cross-ticket assessment; purpose}} |
| Origin | {{ticket link(s), approved plan/version and milestone link}} |
| Fixed baseline | {{original full Git commit or immutable source identity}} |
| Checkpoint trigger and gate | {{start/post-implementation trigger observations and integration/QA gate, or not applicable for routine assessment}} |
| Cumulative baseline provenance | {{last accepted milestone with decision link, or first feature revision with provenance; not applicable for routine assessment}} |
| Assessed source | {{exact revision(s); report-to-revision mapping}} |
| Reviewer assignments | {{axis; assignment ID; actual model/reasoning/context settings, or unavailable}} |
| Instructions | {{supplied ticket/spec/guidance paths and revision/digests or snapshot manifest link}} |
| Inspected scope | {{files/flows, report links}} |
| Omitted scope and assumptions | {{scope, reason, unresolved assumptions or explicit none}} |
| Reports and evidence | {{immutable report links with IDs, attempts, source and digest manifest}} |
| History and decisions | {{finding history and human decision links}} |
| Milestone assessment | {{link or pending/not yet performed}} |

For cumulative work, complete the checkpoint fields using
[architecture checkpoints](../../agents/architecture-checkpoints.md); the fixed
ticket baseline and cumulative baseline have different purposes.

## Current findings

Mutable summary derived from append-only history. Include unresolved findings and
stale evidence even when the assessment is completed.

| Full finding key and concern link | Original classification | Current disposition / source | Latest history event | Next action |
| --- | --- | --- | --- | --- |
| {{review/report/local ID + report anchor}} | {{blocking / optional}} | {{disposition; revision; revalidation status}} | {{history link}} | {{repair, decision or follow-up; link}} |

**Unresolved findings:** {{full keys or explicit none; include deferred work}}

**Integration/milestone eligibility:** {{separate observation with evidence;
pending gates; no authority inferred from review completion}}

## Assessment history

Append source/report/lifecycle changes with actor, reason and evidence. Refresh
the current summary while retaining original reports and history events.

- {{event identity; actor; source; lifecycle; reason; report/history links}}
