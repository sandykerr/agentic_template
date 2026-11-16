# Development M1 QA decision — accepted 2026-11-16

**Decision:** accepted. **Plan:** oop-v2 / review-process-1. **Milestone:** M1,
required tickets 10–24. **Development QA request:**
`41a556a9352d44a3922a9c41f30f36af`.
**Accepted harness source:** `88e4cd8aabc78e76e66efc02983fec3900ab0a23`, repair
`e06eeaf7ae961a927e13b8d330b1675646afe4e2`, exact manifest identified in the
[development request](development-m1-request.json). This accepts the assessed
harness increment; later milestones and the whole feature remain incomplete.

## Actual human decisions and conditions

The human earlier completed code/documentation review, recorded 2026-11-13.
After being presented the current guide, exact candidate and evidence, the human
selected **“Approve this exact demo request”** for first fixture request
`af4eea6758044990a06aa5c1504d98d0`, candidate
`088f10a7e174fd644b53fa71d9252fe732465474`.
[Actual statement and complete request](human-demo-m1-decision.json).
This first reply explicitly accepted only that fixture step.

After its exact promotion, second-group execution, separate passing regression
and clean stop at the final request, the human selected **“Approve final demo
and conditionally accept development M1”**. The question identified final fixture
request `ca4bffef76d14545869e525dd842fdc5`, candidate
`2338f88cce672b05ca2fb44127f35ce3659a8cfa`, and the separate development M1
request/source above. The explicit condition required final promotion of both
demo refs to that candidate, exit0/completed/true, and no replay.
[Actual statement and complete final fixture request](human-final-demo-and-development-decision.json).
The two decisions remain distinct despite sharing a reply.

## Condition fulfilled and observed outcomes

[Acceptance result](m1-acceptance-result.json) records every condition true:

- Both disposable `dev` and `integration` refs equal the final exact candidate.
- Final continuation exited 0, outcome completed, feature_complete true.
- Agent-launch bytes, attempts and gates are unchanged; baseline count stays one.
- Both exact human fixture decisions are consumed and every fixture ticket is Done.

[Completed runtime record](demo-completed-record.json),
[final stdout](demo-final-continue.stdout),
[completed archive/digest](demo-completed-archive.json).
Earlier evidence retains first-group feature integration, unchanged development
before acceptance, rejected stale/replayed decisions and deliberate stop/new-process
continuation without replay. Both tickets Done at the final wait still had
feature_complete false; only final acceptance changed completion to true.
The completed demo is no longer a stopped continuable run.

## Required technical and human evidence

All fifteen M1 implementation tickets remain verified complete. Original cumulative
caller-index F1 is independently fixed at the accepted source, with original
classification/history preserved. Fresh High Spec, Standards and cumulative
all-package Standards each report zero new blocking or optional findings.
[Reports and external digests](capture.json), [cumulative assessment](../../reviews/M1-architecture-01.md).

All 28 source/test/configuration hashes match the actual retained 563/full and
strict type/lint/format/whitespace verification; no executable source changed.
[Source/instruction identity](source-and-instructions.json),
[required check provenance](../m1-index-repair-01/verification-completion-result.json).
The reviewed instruction snapshot remains preserved; later milestone-status
bookkeeping changes no approved behavioral contract.

The human was presented the planned concern-to-repair trace, all declared finite
G2/C5 cases/limits, cumulative ownership/prior findings and current exact demo,
invalid-input/failed-baseline/canonical-restored-invalidation observations in the
[QA guide](qa-guide.md). The explicit development decision above accepts that
source/evidence subject to the condition now fulfilled. Mechanical observations
are attributed to this agent's commands; no unprovided step-by-step human notes
or broader runtime-model guarantees are invented.

## Progression

M1 accepted; M2 ticket25 is the next eligible implementation under the approved
order. This decision starts no M2 work, accepts no M2/M3/M4 candidate, and does
not complete the entire feature. The exact promotion demonstrated here is within
the disposable target; no development-checkout ref was promoted or pushed.
