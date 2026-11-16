# Ticket 25 finding history

Append-only events; original reports and classifications remain preserved. Routine and
broader findings retain distinct full keys even where one repair addresses both.

## T25-R1-E01

| Field | Value |
| --- | --- |
| Finding | [review-ticket-25/spec-01/F1](captures/spec-01-022e9f1dd5e848898262e2756d5e8cd0/report.md#f1--blocking-an-identical-retry-bypasses-validation-of-later-registered-originals) |
| Disposition | open; original classification blocking |
| Actor and role | Parent implementation worker /root, consolidating independent original round1 reports |
| Affected revision | 3b0c1ab7ec41929d3febab44269f791e55897e70 |
| Reason and evidence | Earlier retry skips later original validation; original report/probe linked above, [actual execution](25-probe-execution-results.md) |
| Previous / superseded observation | Initial observation; none superseded |
| Repair or implementation ticket | [Ticket25](../../issues/25-guide-ticket-and-shared-evidence-creation.md), fresh bounded repair assignment repair25_1 |
| Repair commit | Pending; no source fix or independent verification claimed |
| Independent verification | Pending fresh current-source Spec/Standards and relevant renewed broader assessment |
| Human decision / amendment | Not required: owner-local corrections to the approved input-validation/integrity contracts, no scope/ownership change |
| Milestone assessment | [Triggered work](../../reviews/EC1-capture-architecture-01.md); full EC1 checkpoint after26 remains pending |
| Next action | Fresh Medium repair, focused red/green regressions, affected/full required checks, checkpoint commit and fresh whole-ticket reviews |

## T25-R1-E02

| Field | Value |
| --- | --- |
| Finding | [review-ticket-25/standards-01/F1](captures/standards-01-7c21c95b670c413ca133af2548ac8c9b/report.md#f1--reject-empty-optional-names-before-selecting-a-destination) |
| Disposition | open; original classification blocking |
| Actor and role | Parent implementation worker /root, consolidating independent original round1 reports |
| Affected revision | 3b0c1ab7ec41929d3febab44269f791e55897e70 |
| Reason and evidence | Empty optional names mis-scope authoritative records; original report/probe linked above, [actual execution](25-probe-execution-results.md) |
| Previous / superseded observation | Initial observation; none superseded |
| Repair or implementation ticket | [Ticket25](../../issues/25-guide-ticket-and-shared-evidence-creation.md), fresh bounded repair assignment repair25_1 |
| Repair commit | Pending; no source fix or independent verification claimed |
| Independent verification | Pending fresh current-source Spec/Standards and relevant renewed broader assessment |
| Human decision / amendment | Not required: owner-local corrections to the approved input-validation/integrity contracts, no scope/ownership change |
| Milestone assessment | [Triggered work](../../reviews/EC1-capture-architecture-01.md); full EC1 checkpoint after26 remains pending |
| Next action | Fresh Medium repair, focused red/green regressions, affected/full required checks, checkpoint commit and fresh whole-ticket reviews |

## T25-R1-E03

| Field | Value |
| --- | --- |
| Finding | [review-ticket-25/standards-01/F2](captures/standards-01-7c21c95b670c413ca133af2548ac8c9b/report.md#f2--finish-original-validation-before-returning-an-idempotent-registration) |
| Disposition | open; original classification blocking |
| Actor and role | Parent implementation worker /root, consolidating independent original round1 reports |
| Affected revision | 3b0c1ab7ec41929d3febab44269f791e55897e70 |
| Reason and evidence | Earlier retry skips later original validation; original report/probe linked above, [actual execution](25-probe-execution-results.md) |
| Previous / superseded observation | Initial observation; none superseded |
| Repair or implementation ticket | [Ticket25](../../issues/25-guide-ticket-and-shared-evidence-creation.md), fresh bounded repair assignment repair25_1 |
| Repair commit | Pending; no source fix or independent verification claimed |
| Independent verification | Pending fresh current-source Spec/Standards and relevant renewed broader assessment |
| Human decision / amendment | Not required: owner-local corrections to the approved input-validation/integrity contracts, no scope/ownership change |
| Milestone assessment | [Triggered work](../../reviews/EC1-capture-architecture-01.md); full EC1 checkpoint after26 remains pending |
| Next action | Fresh Medium repair, focused red/green regressions, affected/full required checks, checkpoint commit and fresh whole-ticket reviews |

## T25-R1-E04

| Field | Value |
| --- | --- |
| Finding | [review-EC1-capture-architecture-01/standards-01/F1](captures/architecture-01-0aac4966262540eb9a7774ddd84c56ad/report.md#f1--present-but-empty-scope-names-bypass-validation-and-poison-authoritative-folder-scope) |
| Disposition | open; original classification blocking |
| Actor and role | Parent implementation worker /root, consolidating independent original round1 reports |
| Affected revision | 3b0c1ab7ec41929d3febab44269f791e55897e70 |
| Reason and evidence | Empty shared and milestone names mis-scope authoritative records; original report/probe linked above, [actual execution](25-probe-execution-results.md) |
| Previous / superseded observation | Initial observation; none superseded |
| Repair or implementation ticket | [Ticket25](../../issues/25-guide-ticket-and-shared-evidence-creation.md), fresh bounded repair assignment repair25_1 |
| Repair commit | Pending; no source fix or independent verification claimed |
| Independent verification | Pending fresh current-source Spec/Standards and relevant renewed broader assessment |
| Human decision / amendment | Not required: owner-local corrections to the approved input-validation/integrity contracts, no scope/ownership change |
| Milestone assessment | [Triggered work](../../reviews/EC1-capture-architecture-01.md); full EC1 checkpoint after26 remains pending |
| Next action | Fresh Medium repair, focused red/green regressions, affected/full required checks, checkpoint commit and fresh whole-ticket reviews |

## T25-R1-E05

| Field | Value |
| --- | --- |
| Finding | [review-EC1-capture-architecture-01/standards-01/F2](captures/architecture-01-0aac4966262540eb9a7774ddd84c56ad/report.md#f2--identical-retry-returns-before-validating-later-registered-originals) |
| Disposition | open; original classification blocking |
| Actor and role | Parent implementation worker /root, consolidating independent original round1 reports |
| Affected revision | 3b0c1ab7ec41929d3febab44269f791e55897e70 |
| Reason and evidence | Earlier retry skips later original validation; original report/probe linked above, [actual execution](25-probe-execution-results.md) |
| Previous / superseded observation | Initial observation; none superseded |
| Repair or implementation ticket | [Ticket25](../../issues/25-guide-ticket-and-shared-evidence-creation.md), fresh bounded repair assignment repair25_1 |
| Repair commit | Pending; no source fix or independent verification claimed |
| Independent verification | Pending fresh current-source Spec/Standards and relevant renewed broader assessment |
| Human decision / amendment | Not required: owner-local corrections to the approved input-validation/integrity contracts, no scope/ownership change |
| Milestone assessment | [Triggered work](../../reviews/EC1-capture-architecture-01.md); full EC1 checkpoint after26 remains pending |
| Next action | Fresh Medium repair, focused red/green regressions, affected/full required checks, checkpoint commit and fresh whole-ticket reviews |



## Repair1 exact-source revalidation events (2026-11-16)

Actor: parent implementation worker `/root`. Affected source and authorized repair:
ticket25 commit `febd86321851e2acec994237f9d1a1adea824c55` (previous rejected source
`3b0c1ab7ec41929d3febab44269f791e55897e70`, original baseline unchanged).
Reason/evidence: [repair report](25-repair1-report.md), retained red/green cases,
[exact-source binding](25-repair1-committed-source-binding.json) and
[current verification](25-evidence-index.md#current-repaired-checkpoint-and-verification-recovery).
Each concern retains its original **blocking** classification and stays open pending
the named fresh independent assignment. No worker claim supplies a fixed disposition.
No human amendment/decision is needed for these owner-local corrections. Future full
EC1 milestone assessment after26 remains pending; the early triggered assessment is
[linked separately](../../reviews/EC1-capture-architecture-01.md).

| Event | Full finding key | Prior observation | Disposition / independent verification / next action |
| --- | --- | --- | --- |
| T25-R2-P01 | review-ticket-25/spec-01/F1 | T25-R1-E01 | open; pending exact-source `/root/spec25_round2` |
| T25-R2-P02 | review-ticket-25/standards-01/F1 | T25-R1-E02 | open; pending exact-source `/root/standards25_round2` |
| T25-R2-P03 | review-ticket-25/standards-01/F2 | T25-R1-E03 | open; pending exact-source `/root/standards25_round2` |
| T25-R2-P04 | review-EC1-capture-architecture-01/standards-01/F1 | T25-R1-E04 | open; pending exact-source `/root/architecture25_round2` |
| T25-R2-P05 | review-EC1-capture-architecture-01/standards-01/F2 | T25-R1-E05 | open; pending exact-source `/root/architecture25_round2` |

## Repair1 independently verified fixed events (2026-11-16)

Actor: parent implementation worker `/root`, recording independent reviewer results.
Affected source/authorized ticket25 repair commit:
`febd86321851e2acec994237f9d1a1adea824c55`. Each original classification remains
**blocking**. The source correction and current full/static/installed/skill checks
are linked by the [canonical index](25-evidence-index.md); original report bytes
and all earlier events are preserved. External [round2 identities](25-review-round2-digests.sha256)
and [registration](25-review-round2-registration.json) identify the independent originals.
No human decision/amendment or risk acceptance is needed for these local fixes.
The [early triggered assessment](../../reviews/EC1-capture-architecture-01.md) is
renewed; future full EC1 cumulative assessment after26 remains pending.

| Event | Full finding key | Superseded pending observation | Disposition / independent verification / reason |
| --- | --- | --- | --- |
| T25-R2-F01 | review-ticket-25/spec-01/F1 | T25-R2-P01 | fixed; [/root/spec25_round2 original Spec02](captures/spec-02-5900732a47de41b589f24b1257f5be7b/report.md): complete prior-identity loop precedes retry success, so later changed/missing originals cannot be skipped |
| T25-R2-F02 | review-ticket-25/standards-01/F1 | T25-R2-P02 | fixed; [/root/standards25_round2 original Standards02](captures/standards-02-fb83db1963cc4831bb95ec2576576f03/report.md): supplied empty scope names reach validation before ownership/output, preserving valid routing |
| T25-R2-F03 | review-ticket-25/standards-01/F2 | T25-R2-P03 | fixed; [original Standards02](captures/standards-02-fb83db1963cc4831bb95ec2576576f03/report.md): all original checking finishes under lock before matching-ID return, preserving metadata on failure |
| T25-R2-F04 | review-EC1-capture-architecture-01/standards-01/F1 | T25-R2-P04 | fixed; [/root/architecture25_round2 original broader Standards02](captures/architecture-02-4332dc4df4614538b4444cf6a932e3db/report.md): scope presence/validation/routing/linking agree before writes |
| T25-R2-F05 | review-EC1-capture-architecture-01/standards-01/F2 | T25-R2-P05 | fixed; [original broader Standards02](captures/architecture-02-4332dc4df4614538b4444cf6a932e3db/report.md): complete identity checking precedes both success paths; owner/schema/lock unchanged |

Next action for all five events: no further repair; reconcile verified ticket25
completion. No deferred finding, pending human review decision or required
report remains at this assessed source. Later code changes require relevant renewed
independent revalidation before these fixes can be cited as current.
