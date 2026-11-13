# Review report envelope: {{review ID}} / {{report ID}}

Template: [record contract](../../agents/review-records.md). Preserve original
reviewer output verbatim at a unique evidence path; store this envelope alongside
it if the report lacks metadata. Record envelope/output digests in the assessment
or manifest after capture, outside the hashed file itself.

| Field | Value |
| --- | --- |
| Assessment | {{review ID and work item link}} |
| Report identity | {{report ID, axis, attempt, assignment and actor identity}} |
| Actual settings | {{model, reasoning, context target/observed setting or unavailable}} |
| Original baseline | {{full source identity}} |
| Assessed source | {{exact full revision or retained snapshot identity}} |
| Supplied instructions | {{paths, revision and digests/snapshot manifest; missing delivery evidence explicit}} |
| Original output/evidence | {{immutable relative links and capture manifest}} |
| Inspected scope | {{files/flows}} |
| Omitted scope | {{scope and reasons; unresolved assumptions}} |
| Prior observations | {{superseded/reopened full keys and links or none}} |

## Substantive assessment

{{Approved behavior/ownership contract; traced callers, writers, persistence/restore
and invalidation; reasoning about invariant preservation, including a justified
clean conclusion when appropriate. Apply the shared
[scope contract](../../agents/ownership-review.md#report-substantive-reasoning).}}

## Evidence audit

{{Commands/observations and identity checks, results and limits; distinguish these
from the substantive design conclusion.}}

## Findings

Use a heading per report-local ID. Preserve the reviewer's classification,
concern, source location/evidence, consequence and proposed remedy. Dispositions
belong in the separate append-only history, linked by the full compound key.

### {{local ID}}

{{Classification; concern; exact source/evidence; consequence; remedy; full key}}

## Assessment result

{{Assessment complete/incomplete; unresolved assumptions; original result.
This snapshot is not a mutable current-disposition summary.}}
