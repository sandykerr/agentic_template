# Ticket24 — repeated alias failure diagnosis before another dispatch

Root paused new assignments after round2: `/root/spec24_2` reports `review-ticket-24/spec-02/F1`, a concrete residual of `review-ticket-24/standards-01/F1`; `/root/standards24_2` is independently clean and remains unchanged. Both agree the original recursion key is repaired at564c0a9. Original reports/captures retain differing judgments. Actual full556/static/compatibility passes do not cover the adverse scheduling interval.

Assignments so far: initial Medium worker, first independent High pair (two blockers), one fresh Medium repair, second independent High pair (Spec1 blocker/Standards0). No agreed numeric resource/repair bound exists; all required gates remain. Preparation missed coordination of development topology at automatic feature commit: prechecks and no-dereference of the written name protect static aliases and feature redirects, not a development alias installed before feature advances. Another unlocked precheck is insufficient. No risk acceptance or narrowed contract is authorized.

## Signal and hypotheses

The immutable Spec02 report/audit retains public CLI reproduction on exact564c0a9: pause CLI after its development direct-ref check, install `dev -> integration` without changing OIDs, resume, observe automatic feature write moving development without any QA request/decision, then later rejection. Its source/procedure/outcomes are actual evidence; no new private testing seam is inferred.

Ranked mechanism hypotheses (shown to user before root probes): an unlocked development ref permits the write; a one-shot Git verify might distinguish/refuse symbols; a prepared transaction could hold both ref locks while topology is validated. Root read installed Git2.53.0 primary `git-update-ref(1)` documentation for verify, prepare, commit and abort. Existing harness already uses this transaction API. Git semantics probes are diagnosis, not substitutes for CLI regression coverage.

## Actual bounded probes

[Runnable script](24-diagnosis2-atomic-probe.py) executed through the documented absolute Python; [raw observations](24-diagnosis2-atomic-probe.json). Disposable Git repository only; no production source mutation.

- `verify dev expectedOID` with no-deref plus feature update in one shot still accepts a symbolic dev with the same resolved OID and advances it indirectly. OID verify alone does not fix the reported failure.
- An interactive transaction queues no-deref development verify plus expected-old feature update, then `prepare` locks both refs. While prepared, ordinary Git symbolic-ref mutation returns1 (locked).
- Under those held locks, a direct-ref guard distinguishes a dev alias installed before prepare. Abort preserves both resolved original tips; direct refs instead commit feature only while preserving development. Process EOF without commit aborts by Git contract.

This provides a viable in-scope primitive for a fresh repair: prepare/lock, validate topology while locked, then commit or abort; retain expected-old/no-deref semantics for both automatic integration and milestone promotion. No manual ref-storage lock paths, new persistence schema, recovery feature, external approval authority or minimum-Git change is needed by this mechanism. Worker must still implement bounded child cleanup, reproduce original CLI interleaving red/green, examine related ordering, preserve existing changed-development behavior, and reassess architecture triggers. If an actual consequential incompatibility emerges, expose it rather than waive the contract.

Next assignment has one purpose: complete this atomic coordination repair after the complete diagnosis, with renewed required final-source suite/static/old/new checkpoint evidence and a fresh independent whole-ticket pair from the original baseline. Both prior alias keys remain unresolved; root will append independent verification only at actual new source. M1 cumulative assessment/real QA remain separate unperformed work.
