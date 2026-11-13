from ticket_harness.run import Run
from ticket_harness.restore import restore
from ticket_harness.checks import checks_ready
from ticket_harness.approval import candidate_ready
run, review = restore({"gates": {"checks": True, "approval": True}})
assert candidate_ready(review)
Run.revoke(run)
print({"canonical": run.gates, "review": review.gates,
       "checks_ready_after_revoke": checks_ready(review),
       "candidate_ready_after_revoke": candidate_ready(review)})
assert not candidate_ready(review), "restored review readiness survives canonical revocation"
