#!/usr/bin/env bash
set -u
cd /home/ajkerr1/development/agentic_template || exit 1
log=.scratch/ticket-harness/evidence/19-repair-c5-checks.log
py=/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python
result=0
run() {
  {
    printf '\ncommand:'
    printf ' %q' "$@"
    printf '\n'
  } >> "$log"
  "$@" >> "$log" 2>&1
  code=$?
  printf 'exit=%s\n' "$code" >> "$log"
  if [ "$code" -ne 0 ]; then result=1; fi
}
run date -u +%FT%TZ
run git rev-parse HEAD
run git status --short
run bash -n .scratch/ticket-harness/evidence/19-repair-c5-run-checks.sh
for skill in implement-with-checkboxes create-next-agent-prompt evaluate-reviewers; do
  run env PYTHONPATH=/usr/lib/python3/dist-packages "$py" /home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py ".agents/skills/custom/$skill"
done
run "$py" .scratch/ticket-harness/evidence/19-repair-c5-check.py
saved_capture=.scratch/ticket-harness/evidence/19-evaluation-g3/spec-c3-reviewer-saved.md
# Exact frozen saved report bytes require the previously approved sole EOF allowance.
# Full default failure is captured separately, not represented as an all-path pass.
run git diff --check f2929e79cfd5a68f670862775053ae85ba9582b5 -- . ":(exclude)$saved_capture"
run git -c core.whitespace=-blank-at-eof diff --check f2929e79cfd5a68f670862775053ae85ba9582b5 -- "$saved_capture"
exit "$result"
