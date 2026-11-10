#!/usr/bin/env bash
set -eu
cd /home/ajkerr1/development/agentic_template
ticket16_evidence=.scratch/ticket-harness/evidence
ticket16_python=/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python
ticket16_log="$ticket16_evidence/16-checks.log"
run_check() {
  printf '\ncommand:' >> "$ticket16_log"
  printf ' %q' "$@" >> "$ticket16_log"
  printf '\n' >> "$ticket16_log"
  local check_exit=0
  "$@" >> "$ticket16_log" 2>&1 || check_exit=$?
  printf 'exit=%s\n' "$check_exit" >> "$ticket16_log"
  if [ "$check_exit" -ne 0 ]; then
    tail -35 "$ticket16_log"
    return "$check_exit"
  fi
}
run_check git rev-parse HEAD
run_check git status --short
run_check bash -n "$ticket16_evidence/16-run-checks.sh"
for ticket16_skill in implement-with-checkboxes create-next-agent-prompt; do
  run_check env PYTHONPATH=/usr/lib/python3/dist-packages "$ticket16_python" \
    /home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
    ".agents/skills/custom/$ticket16_skill"
done
if [ "${1:-}" = --build ]; then
  run_check "$ticket16_python" "$ticket16_evidence/16-check.py" --build
  cp "$ticket16_evidence/16-check-results.json" "$ticket16_evidence/16-build-results.json"
else
  run_check "$ticket16_python" "$ticket16_evidence/16-check.py"
fi
run_check git diff --check
printf 'All standalone checks passed. See %s\n' "$ticket16_log"
