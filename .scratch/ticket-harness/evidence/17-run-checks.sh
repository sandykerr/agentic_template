#!/usr/bin/env bash
# Retain commands/exits for the standalone guidance implementation.
set -u
cd /home/ajkerr1/development/agentic_template || exit 1
log=.scratch/ticket-harness/evidence/17-checks.log
P=/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python
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
run git rev-parse HEAD
run git status --short
run bash -n .scratch/ticket-harness/evidence/17-run-checks.sh
for skill in implement-with-checkboxes create-next-agent-prompt review-architecture; do
  run env PYTHONPATH=/usr/lib/python3/dist-packages "$P" /home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py ".agents/skills/custom/$skill"
done
run "$P" .scratch/ticket-harness/evidence/17-check.py
run git diff --check c82b15f504c29a69e8fb708e10568574150e80d3
exit "$result"
