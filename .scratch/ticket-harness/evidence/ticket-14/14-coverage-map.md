# Ticket 14 coverage map

Approved seam: public CLI, external scripted processes, isolated real Git repositories,
observable refs/status/requests/decisions. Preparation tests now bound an active wait
and terminate/reap the runner; their successful status exit is not a run completion.

- Existing milestone tests retain request/regression/source/merge/branch preservation coverage.
- Existing dependency, transaction, repairs, reports and integrity cases retain ticket gates,
  expected-old integration, unchanged inputs, bounded repair and legacy plan-free behavior.
- New two-milestone foreground scenario: stale candidate rejected; no later attempts;
  exact acceptance promotes; feature aligned before next worker; consumed decision retained;
  replay rejected; all Done still waits; final acceptance completes; unique artifacts.
- Further slices add strict malformed/incidental identity rejection, indefinite observable wait,
  worker artifact authority, and changed source/evidence/input/ref rejection at consumption.

Each fixture owns its repository and runner; fixture deadlines do not impose runtime QA deadlines.
Required final gates: full pytest suite, strict mypy, Ruff lint/format, whitespace.
Packaging/entrypoint files are unchanged.

New executable cases and distinct failures:

- `test_invalid_decisions_keep_waiting_without_repairs_or_authority_from_incidental_text`:
  one isolated run exercises exact schema/value/identity/duplicate-key rejection,
  absence, malformed artifact shape and waiting longer than all configured timeouts.
- `test_acceptance_revalidates_the_exact_candidate_evidence_and_both_refs`:
  separate QA-time dev/feature movements exercise both transaction predicates;
  candidate/prior-source mutations exercise applicable source invalidation;
  input/request/log mutations exercise independent approval authority and evidence;
  checked-out dev/feature protect both caller branches/worktrees.
- `test_implementation_and_repair_cannot_write_qa_authority`: initial and repaired
  assignments exercise protected authority paths at both process-boundary roles.
- `test_later_milestone_eligibility_is_validated_before_execution`: later human-ready
  tickets and unavailable outside-plan dependencies cannot silently execute.

Test cleanup captures own descendant process groups before terminating/reaping
foreground runners. Raw fixture observations include run commands/exits, explicit
fixture termination, actual status CLI, refs/history, requests/decision artifacts,
assignments, output and source identities. Successful status does not claim that
an intentionally terminated runner completed or accepted a milestone.

The invalid-decision sequence also rejects a boolean substituted for numeric
regression exit_code (strict JSON value types). A FIFO artifact exercises the
separate blocking-read failure: it must be reported unreadable before any read.
Its regression was observed red before adding regular-file validation.
