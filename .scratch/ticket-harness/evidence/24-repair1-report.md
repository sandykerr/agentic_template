# Ticket 24 repair 1 — implementation and verification packet

Actor `/root/repair24_1`, configured fresh GPT-6.1 Sol Medium; advisory active-context target <=250000. Actual backend delivery/enforcement and active-context telemetry are unavailable. Fixed whole-ticket baseline `ed017ae0c2b96769f31c710cfb4ff4708989b446`; rejected implementation `65951f6db43fbd2299aa105f3f409eaacd85ec24`. This packet claims bounded repairs; it does not independently verify findings or mark them fixed. Root owns fresh whole-ticket Spec/Standards reviews, dispositions, completion and handoff.

## Governing findings and scope

Both immutable originals and own audits were read before repair: [Spec](24-review-spec-01.md), [Spec audit](24-review-spec-01-audit.json), [Standards](24-review-standards-01.md), [Standards audit](24-review-standards-01-audit.json), [capture](24-review-round1-capture.json), [append-only history](24-finding-history.md). [Repair context identities](24-repair1-start.json) independently match the four original digests. The start capture was made during repair and explicitly records the then-current dirty tree; it is not misrepresented as a pre-edit capture. Individual red/green manifests retain actual phase bytes. The original fixed baseline remains unchanged.

- `review-ticket-24/spec-01/F1`: catch `RecursionError` only in milestone review's existing decision validation/rejection operation, around decoding, shape/exact-approval checks and request serialization/comparison. The existing observation artifact, diagnostic, rejected status, persistence, indefinite wait and later approval remain authoritative. No run-wide recovery catch is added.
- `review-ticket-24/standards-01/F1`: require direct feature/development branch destinations before baseline/ticket work, at automatic integration, fresh/restored review preparation, post-regression readiness, clean stop, restoration and milestone promotion. Existing Git primitives own the shared direct-ref validation and expected-old writes. `--no-deref` is applied to the single automatic feature update and separately to each ref in the human-approved two-ref transaction. Ticket execution supplies its already-approved development name to feature integration; it receives no development-write authority.

Approved direct-ref configurations, expected-old commit validation, checkpoint version 1, filenames and JSON representations remain unchanged. No new Git abstraction/framework, lifecycle, persistence schema, checker, approval authority, dependency, installed entry point or package change is introduced. Packaging checks are therefore omitted under testing policy. Future background/correction/runtime features, actual M1 cumulative assessment and actual human QA are omitted as unauthorized scope. No consequential missing human-owned scope decision was found.

## Ownership and affected flows

| Responsibility | Owner and repair effect |
| --- | --- |
| Public start/continue/status/stop entry | `__main__.py` unchanged; real public CLI remains the behavioral seam. |
| Branch/baseline establishment | `_Run.execute` still owns it; Git now rejects symbolic destinations before baseline or ticket assignments. |
| Automatic ticket integration | `_TicketExecution.execute` still owns the attempt/candidate/integration sequence; it supplies the development destination from the approved config so Git can validate separation before advancing feature. Integration failure still blocks without a repair. |
| Git refs and expected-old writes | `git.py` functions remain the only production ref writers; validation is shared there, and writes explicitly avoid dereferencing. Existing expected-old OID checks and atomic two-ref promotion remain. |
| QA decision/evidence lifecycle | `MilestoneReview` still owns observation, rejection, wait, tested request and exact approval. Only its validation catch is extended; command/check/source-invalidating authority stays with the run. |
| Save/restore/check invalidation | Existing version-1 persistence and review restoration remain. Shared request validation adds destination-type rejection. `_Run.restore_checks` and canonical gate/source invalidation are unchanged. No new saved state or alias is introduced. |
| Requirement/config normalization | `PreparedInputs` and `plans` remain unchanged; distinct feature/development names are already validated. Runtime Git now enforces their actual destination type. |

Inspected definitions/callers and actual flows in `__main__.py`, `runner.py`, `tickets.py`, `qa.py`, `git.py`, `inputs.py`, `plans.py`, `records.py` and `agents.py`; relevant public fixtures/tests and the baseline checkpoint producer/consumer were inspected. The earlier refactor owners and all unchanged record/gate/input/attempt/process protection remain in place. Initialization, restored verification references and source invalidation remain run-owned. There is no second ref writer or parallel approval path.

The decision investigation traced bytes → `json.loads` with duplicate-key validation → exact field/decision checks → JSON request serialization/comparison → consumed-request check. `UnicodeDecodeError` is already a `ValueError`; malformed syntax/duplicate keys and wrong shapes use existing rejection. A 2000-level request probe parses and serializes safely under this Python and was already rejected as mismatched; that redundant added parameter was removed rather than claiming it reproduced a second bug. The remaining new deep case reproduces the actual decoder failure. The bounded catch also covers recursion from comparison serialization without extending arbitrary crash recovery to the run or checkpoint lifecycle.

The Git investigation traced both alias directions and feature→bridge→development chains; expected-ref reads; setup; both writers; request preparation after regression; clean stop; durable restore; and promotion. A direct-ref check rejects same-OID symbolic replacements that ordinary commit comparison misses. Git's documented and locally observed `--no-deref` semantics update only the named ref: a symbol introduced after validation cannot redirect the write to its referent. Such a last-moment external symbol may itself be replaced by Git when its resolved OID matches; this repair does not claim a transaction-wide branch-type lock against arbitrary external mutation. Expected-old commit movement still fails safely; no hostile-environment or arbitrary interruption guarantee is invented.

## Start/final risk triggers

| Trigger | Repair start | Final implementation | Reason |
| --- | --- | --- | --- |
| New lifecycle | No | No | Same setup, ticket execution, review wait/reject, stop, continue and promotion phases. |
| New persistence/restoration path | No | No | Same version-1 envelope/archives and canonical gate restore; only an existing validation path gains a direct-ref guard. |
| New shared mutable state | No | No | No additional store, shared alias or durable field. Development name is copied from existing approved configuration. |
| Additional writer | No | No | Existing Git and QA writers are constrained; run/attempt/check writers and human authority are unchanged. |

These observations do not trigger a third affected-workflow assessment. They do not perform the separate M1 cumulative all-package High assessment or supply M1 acceptance.

## Coverage selection and red/green evidence

Existing tests already cover ordinary direct-ref exact promotion and replay (`test_two_foreground_milestones_require_exact_acceptance_and_consume_each_decision`), malformed/type/duplicate/missing decisions (`test_invalid_decisions_keep_waiting_without_repairs_or_authority_from_incidental_text`), source/evidence/ref movement and checked-out branches (`test_acceptance_revalidates_the_exact_candidate_evidence_and_both_refs`), clean new-process continuation, restored canonical gate invalidation, checkpoint/evidence tampering, repeated stop lineage and transaction expected-old movement. Those scenarios are retained; no internal-class tests or mocks were added.

Twelve distinct additional public CLI/scripted-process/real isolated Git scenarios cover the previously unobserved failures:

| Added coverage | Distinct failure and evidence |
| --- | --- |
| Deep invalid decision (1) | Decoder recursion ends QA rather than rejecting; observes rejection/artifact, unchanged refs/attempts/later work, later exact approval and clean stop. [Red](24-repair1-red-decision.log), [green](24-repair1-green-decision.log). The first red trial also had one already-safe request-depth parameter; the log faithfully reports 1 failed/1 passed. |
| Pre-work destination aliases (3) | Development→feature, feature→development and chained feature alias could write development before human approval. [Red](24-repair1-red-alias-setup.log), [green](24-repair1-green-alias-setup.log). |
| Aliases introduced during ticket work (2) | Either direction bypasses initial-only validation; rejects at integration with refs unchanged. [Bounded red](24-repair1-red-alias-transitions-bounded.log), [green](24-repair1-green-alias-transitions.log). |
| Same-tip symbols at promotion/restore and stop (5) | Matching commit identity is insufficient; two promotion and two continuation variants extend existing scenarios, one clean-stop scenario ensures no checkpoint is written. Same bounded red/green links. |
| Replacement during milestone regression (1) | Pre-candidate validation alone permits an unsafe QA request; post-check readiness now refuses it. [Red](24-repair1-red-alias-readiness.log), [green](24-repair1-green-alias-readiness.log). |

The first transition red run used the existing synchronous continuation helper and hung waiting under unrepaired code. It was interrupted with exit 130; its partial [log](24-repair1-red-alias-transitions.log) is retained and is not a completed result. The new continuation variants were corrected to the existing bounded foreground seam; all seven then failed for the intended accepted-alias behavior, and all seven passed after repair. Every repository remains fixture-owned and isolated; the foreground helper reaps owned processes. No production seam was widened.

[Development check records](24-repair1-development-checks.json) retain commands, exits and phase manifests. A first direct static invocation found Ruff absent from the reusable interpreter. The retained existing `/tmp/ticket23-tools` pinned modules are used through `PYTHONPATH` for required final static checks, as in the original capture tooling; no environment installation/change was made.

## Exact-source final checks and compatibility

Final result: **556 passed in 842.52s**; strict mypy passed on 10 source files; Ruff lint passed and format checked 24 files; both whitespace commands exited 0. All six command results passed with frozen bytes unchanged.

[Final source freeze](24-repair1-final-source.json) identifies all 27 runtime/test/example/config/wayfinding files. [Final command records](24-repair1-final-check-results.json) retain commands, exits, elapsed time and logs; the wrapper asserts frozen bytes before and after each command. The final full suite includes both legacy cases and all twelve additions, and preserves actual CLI/status/Git/record artifacts through a versioned copy of the existing fixture-cleanup capture plugin. [Observation index](24-repair1-observation-index.json), [raw manifest](24-repair1-raw-manifest.json), [stream archive audit](24-repair1-capture-audit.json), [raw archive](24-repair1-final-raw.tar.gz) retain that execution. Test assertions establish their observed behavior; source hashes and a passing suite do not establish architecture correctness or independently dispose findings.

The genuine pre-refactor producer is unchanged in [original producer](24-checkpoint/producer.json), with every producer source compared to original baseline Git blobs by the consumer. [Restore provenance](24-repair1-checkpoint/restore.json) records moving the original completed live fixture aside and restoring its genuine stopped archive at original absolute paths. [Versioned consumer](24-repair1-tools/continue-old.py), [consumer log](24-repair1-checkpoint/continue-final.log) and [consumer record](24-repair1-checkpoint/continuation-final.json) prove continuation with the frozen repaired source: success exit 0/completed, unchanged previous attempt/gate prefixes, one baseline, two exact consumed approvals, four total assignments and both final refs aligned to the second tested candidate. The completed repair fixture is separately archived and verified in [compatibility audit](24-repair1-checkpoint/audit.json). The original producer, stopped/continued archives and initial consumer evidence remain unchanged. Full-suite clean continuation/repeated-stop/invalidation cases also verify checkpoints written by new code.

[Post-commit source audit](24-repair1-committed-source.json) binds these exact tested bytes to the repair commit; no code is changed after final verification. G2/final C5 remains finite historical reviewer evaluation (`332ddabe972f596d86cd09eda809bd2f93d1f57602f01d75ed9f39f2b182510d`), not a review of this source, detection guarantee or runtime enforcement proof. Root must obtain fresh whole-ticket axes from the original fixed baseline and independently verify both claimed fixes before disposition/completion. No promotion, push, actual QA acceptance, ticket/header/index or next-agent handoff update is performed here.
