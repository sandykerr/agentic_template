# Ticket 18: actual isolated cumulative review observations

This is a finite development walkthrough over a real disposable Git repository,
not the real harness, broad reviewer calibration, runtime enforcement or M1 QA.
The source [bundle](source.bundle), complete snapshots and [manifest](sources.json)
retain all commits, Python files and content identities. Recreate an object
repository with `git clone --no-checkout source.bundle /tmp/a-new-fixture-repo`
from this directory; inspect exact source with `git show REV:path`. Do not rerun
the [single-use builder](../18-build-fixture.py) over saved evidence. Its output
asserts empty destinations; final audits are [read-only](../18-check.py) except
for their own current result file. Fixture observers exercise illustrative source,
not the real CLI or a replacement behavioral testing seam.

## Source and independent assignments

Fixture initial feature revision is `36772524659032570d018cc164c5aa4e90068edf`:
root commit establishes Run/CONTRACT, followed by A→B→risk C→clean repair. No
accepted milestone exists in this isolated feature; the root is chosen because
it explicitly starts this feature, not merely because it is a repository root.
This cumulative baseline stays fixed. Routine B's ticket baseline is A, showing
why ticket and cumulative baselines differ. The real ticket 18 baseline is
`02d76205a1c40e45c607ef2a5d11ec282393edcd`, a separate repository/source identity.

| Assessment | Exact source | Original report / outcome |
| --- | --- | --- |
| A Spec | `5fa532d42205f6569918f7584cc2f6c3e52be603` | [a-spec](a-spec.md): no findings |
| A Standards | same A source | [a-standards](a-standards.md): no findings |
| B Spec | `97176da382659153165d84c0f76ade21903dfc38` | [b-spec](b-spec.md): no findings |
| B Standards | same B source | [b-standards](b-standards.md): no findings |
| C risk cumulative Standards | `e65723747cf4029c1829209da9f333ca17d87989` | [standards-risk-01](cumulative-risk.md): blocking F1 |
| C clean cumulative Standards and independent F1 verification | `8078239cfc1062acbf8e3f59ac2392925da4586a` | [standards-clean-01](cumulative-clean.md): exact fix verified; no new findings |

[Actual assignment arguments and prompt snapshots](assignments.json) retain six
fresh fork-none GPT-6.1 Sol High assignments and the 250K active-context target.
Reports expose unavailable independent model/reasoning/context telemetry. The
[guidance identities](guidance-identities.json), report-local identities and
[capture digests](capture.json) identify evidence without claiming runtime delivery
enforcement. Prompt snapshots were captured by the worker after delivery, leaving
original reports' earlier snapshot-absence statements intact. Original reports
are unchanged. Initial axes exclude their sibling output; cumulative risk receives
completed A/B history and clean receives risk/F1. Neither uses scripted verdicts.
Risk's report discloses incidental visibility of the builder's later repair block;
its conclusion remains based on the risk source and failing observation.

All five fixture Python files are inventoried and inspected by cumulative reviewers:
`__init__.py`, `run.py`, `checks.py`, `approval.py`, `restore.py`. Contract,
tickets and observation caller complete the ten-file source. Reports explain
unchanged writers/readers, restoration, revocation, and concrete changes for an
additional review stage/repair policy, rather than treating hashes as design proof.

## What accumulated and what the evidence establishes

A adds a direct current-state check consumer; B adds a second cross-module
readiness consumer. Both independently reviewed ticket sources are correct:
all writes/revocation belong to Run, and readers observe that same owner. C adds
a restore path that produces two detached mutable representations. Those existing
consumers jointly become stale after canonical revocation. This is an accumulating
workflow/ownership failure across A, B and C, not a claim A/B reviewers missed code
that did not exist in their source. C is caught at its risk-triggered checkpoint
before integration. Integration remains B in the retained bundle; clean repair
is a candidate, not an integrated/accepted milestone.

[Actual process observations](command-observations.json) show A/B local checks
pass on both earlier sources and on the risk source. The cumulative restored
revocation observation fails on risk (review remains true) and passes on clean
(both roles share the actual Run). Original cumulative reviewers retain their
own command captures too. These finite observations show how ticket passes alone
cannot authorize later cumulative readiness; they do not establish general
reviewer detection rates or guarantee every distributed ownership flaw is found.

## Work item, history and progression

The [cumulative assessment](assessment.md) links source, complete scope, reports,
trigger, [full-key append-only history](finding-history.md) and exact fix. The
[pre-assessment capture](pre-assessment-observation.json) observes reports missing
while the integration ref stays B. [Manual guidance decisions](readiness-observations.json)
retain seven distinct progression states: missing work; completed assessment with
blocker; stale-source rejection; actual human authority absent; fictional
disposition/deferred handoff; exact clean checkpoint; and QA acceptance absent.
They are the implementation worker's actual application of the guidance to the
saved inputs. They are not an automatic runtime gate or simulated reviewer judgment.

The [example human statement](example-human-decision.md),
[example amendment](example-amendment.md) and [deferred follow-up D](deferred-D.md)
are **synthetic**. Their separate [handoff](deferred-handoff.md) preserves deferred
work and missing renewed scope review. They grant no actual human authority and
never resolve the original-contract blocker. The independent clean review instead
verifies the existing-contract repair without relying on a human scope change.
No candidate, QA request, human acceptance, promotion or next-milestone execution
is created in either branch. New source cannot reuse old report completion to
claim readiness; old reports/history remain intact.

## Real feature boundary

[Real package inventory](real-package-inventory.json) retains all ten
`ticket_harness` Python files at the real baseline, **inventory only**. Real M1
cumulative assessment is unperformed and must eventually inspect all of them on
its then-current source, with genuine cumulative baseline provenance and carried
findings. [Git provenance observations](../18-provenance.json) distinguish initial
spec/package history from accepted-milestone authority. Remaining 19–24 and actual
human QA are required; these fixture reviews cannot satisfy real M1 or accept it.
