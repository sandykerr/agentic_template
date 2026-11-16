# Actual round1 probe execution

Parent worker executed all three reviewer-authored scripts serially through
retained Forest203 PTY session10089, using checkout-local .venv/bin/python and
executable /dev/shm temporary fixtures. [Same-session context](25-probe-execution-context.txt)
records host, architecture, checkout, source and source-tree status.
All outer script exits were **0**, observed via the terminal's immediate shell
exit-status output. Each script's JSON retains the actual helper exits that
constitute the counterexample; outer0 means the probe completed, not that the
product satisfied the intended guarantee.

- Spec01: spec-01-022e9f1dd5e848898262e2756d5e8cd0/probe.py -> probe-output.json;
  retryA0 after laterB mutation, retryB control1, metadata unchanged.
- Standards01: standards-01-7c21c95b670c413ca133af2548ac8c9b/standards-probe.py ->
  standards-probe-results.json plus probe.stdout/probe.stderr; both independently
  authored counterexamples reproduced.
- Architecture01: architecture-01-0aac4966262540eb9a7774ddd84c56ad/probe.py ->
  probe.json/probe.stderr; empty shared/milestone and retry validation counterexamples.

Exact assessed source3b0c1ab7ec41929d3febab44269f791e55897e70 was unchanged during
all probes. No assessed source, original report or standing review decision was
edited. Public helper calls ran only in disposable real Git repositories.
