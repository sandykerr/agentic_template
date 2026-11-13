from ticket_harness.run import Run
from ticket_harness.checks import checks_ready
r = Run()
assert not checks_ready(r)
r.record("checks", True)
assert checks_ready(r)
r.revoke()
assert not checks_ready(r)
print("A check status and revocation: PASS")
from ticket_harness.approval import candidate_ready
r.record("checks", True)
assert not candidate_ready(r)
r.record("approval", True)
assert candidate_ready(r)
r.revoke()
assert not candidate_ready(r)
print("B checks plus approval and revocation: PASS")
