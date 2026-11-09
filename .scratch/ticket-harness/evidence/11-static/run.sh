#!/usr/bin/env bash
set -u
cd /home/ajkerr1/development/agentic_template
ticket11_evidence=.scratch/ticket-harness/evidence/11-static
ticket11_python=/home/ajkerr1/development/agentic_template/.micromamba/envs/dev/bin/python
run_check() {
  local check_name=$1
  shift
  printf '%q ' "$@" >> "$ticket11_evidence/commands.log"
  printf '\n' >> "$ticket11_evidence/commands.log"
  "$@" > "$ticket11_evidence/$check_name.log" 2>&1
  local check_exit=$?
  printf 'exit=%s log=%s\n' "$check_exit" "$ticket11_evidence/$check_name.log" >> "$ticket11_evidence/commands.log"
  cat "$ticket11_evidence/$check_name.log"
  return "$check_exit"
}
: > "$ticket11_evidence/commands.log"
run_check starting-head git rev-parse HEAD || exit $?
run_check worktree git status --short || exit $?
for ticket11_skill in implement-with-checkboxes create-next-agent-prompt; do
  run_check "$ticket11_skill-validation" env PYTHONPATH=/usr/lib/python3/dist-packages "$ticket11_python" /home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py ".agents/skills/custom/$ticket11_skill" || exit $?
done
run_check documents "$ticket11_python" "$ticket11_evidence/check_documents.py" || exit $?
run_check whitespace git diff --check -- .agents/skills/custom/implement-with-checkboxes/SKILL.md .agents/skills/custom/create-next-agent-prompt/SKILL.md || exit $?
run_check identities sha256sum .agents/skills/custom/implement-with-checkboxes/SKILL.md .agents/skills/custom/create-next-agent-prompt/SKILL.md .agents/skills/custom/references/planning.md docs/agents/issue-tracker.md /home/ajkerr1/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$ticket11_evidence/check_documents.py" "$ticket11_evidence/run.sh" || exit $?
run_check implementation-diff git diff 5af3b343ad962b05ce44e359b791b65a8865f05a -- .agents/skills/custom/implement-with-checkboxes/SKILL.md .agents/skills/custom/create-next-agent-prompt/SKILL.md || exit $?
