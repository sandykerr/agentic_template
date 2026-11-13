from pathlib import Path
import datetime
import hashlib
import json
import subprocess

root=Path('/home/ajkerr1/development/agentic_template')
out=Path('/tmp/ticket19-review')
base='f2929e79cfd5a68f670862775053ae85ba9582b5'
head='e90abb64ab95c5b15cdb0949b03c6a948365339b'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
instructions = [
 'AGENTS.md','GLOSSARY.md','docs/agents/domain.md','docs/agents/python-environment.md',
 'docs/agents/testing.md','docs/agents/issue-tracker.md','docs/agents/ownership-review.md',
 'docs/agents/review-records.md','docs/agents/architecture-checkpoints.md','docs/templates/reviews/report.md',
 'docs/adr/0001-reusable-harness-and-local-integration.md','docs/adr/0002-human-qa-gates-feature-promotion.md',
 '.agents/skills/custom/test-strategy/SKILL.md','.agents/skills/matt-pocock/codebase-design/SKILL.md',
 '.agents/skills/matt-pocock/writing-for-agents/SKILL.md','.agents/skills/matt-pocock/writing-for-agents/SKILL-MECHANICS.md',
 '.agents/skills/microsoft/microsoft_oop/SKILL.md','.agents/skills/matt-pocock/code-review/SKILL.md',
 '.agents/skills/matt-pocock/implement/SKILL.md','.agents/skills/custom/grill-to-tickets/SKILL.md',
 '.scratch/ticket-harness/spec.md','.scratch/ticket-harness/issues/19-evaluate-reviewers-on-known-and-acceptable-designs.md']
changed=subprocess.check_output(['git','-C',str(root),'diff','--name-only',base+'...'+head],text=True).splitlines()
collaborators=['.scratch/ticket-harness/README.md','.scratch/ticket-harness/approval.md',
 '.scratch/ticket-harness/milestones.md','.scratch/ticket-harness/reviews/ticket-17.md',
 '.scratch/ticket-harness/reviews/ticket-18.md','.scratch/ticket-harness/evidence/16-check.py']
paths=sorted(set(instructions+changed+collaborators))
external=[Path('/home/ajkerr1/.codex/skills/.system/skill-creator/SKILL.md'),out/'standards-assignment.txt',out/'common.txt']
audit_paths=[out/'standards-audit.py',out/'standards-audit.json',out/'standards-parent-provenance.json',out/'standards-check-history.json']
failed=[
 {'command':'rg headings in spec && rg --files for standards files under .agents docs .scratch/ticket-harness && cat declaration/capture/manifest/README',
  'exit':1,'observation':'No matching AGENTS/CODING_STANDARDS/CONTRIBUTING in searched subdirectories stopped the && chain. Required files were reread explicitly; later full hidden-file search found only root AGENTS.md.'},
 {'command':'Python read prior 19-check-results-*.json using data[group] for retained_evidence_identities',
  'exit':1,'observation':"KeyError: 'retained_evidence_identities'. The first historical check schema lacks that later-added group. Corrected audit uses data.get(group, {}) and preserves history in standards-check-history.json; this was reviewer audit assumption, not a source failure."}]
commands=[
 {'command':'cat /tmp/ticket19-review/standards-assignment.txt /tmp/ticket19-review/common.txt','exit':0},
 {'command':'pwd; git status --short; git diff --stat '+base+'...'+head,'exit':0},
 {'command':'cat/nl/bounded sed of instruction_sources, changed_paths and collaborators below','exit':0,'limits':'Combined tool output sometimes truncated; bounded rereads supplied the required policy/source. File digests pin bytes; they do not prove substantive reading.'},
 {'command':str(root/'.micromamba/envs/dev/bin/python')+' /tmp/ticket19-review/standards-audit.py','exit':0,'evidence':'standards-audit.json','limits':'Output included long preservation patches and was truncated; bounded follow-up printed source-reading calls without patch bodies. Complete extracted inputs remain in JSON.'},
 {'command':'Python bounded source-session call inventory from standards-audit.json excluding report-preservation patch bodies','exit':0},
 {'command':'Python selected original implement_19 session declaration/spawn provenance extraction','exit':0,'evidence':'standards-parent-provenance.json'},
 {'command':'Python historical check manifest comparison with optional group handling','exit':0,'evidence':'standards-check-history.json'},
 {'command':'git diff --check '+base+'...'+head,'exit':0},
 {'command':'bash -n .scratch/ticket-harness/evidence/19-run-checks.sh','exit':0},
 {'command':'git log --oneline '+base+'..'+head+'; git status --short; rg --files --hidden -g AGENTS.md -g CODING_STANDARDS.md -g CONTRIBUTING.md -g !.git -g !.micromamba','exit':0,'observation':'One implementation commit, clean worktree, only root AGENTS.md; no CODING_STANDARDS.md or CONTRIBUTING.md.'},
 {'command':'git merge-base '+base+' '+head,'exit':0,'stdout':base}]
value={'review_id':'review-ticket-19','report_id':'standards-01','actor':'/root/standards19',
 'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'baseline':base,'assessed_source':head,'diff_command':'git diff '+base+'...'+head,
 'configuration':{'requested_model':'gpt-6.1-sol','requested_reasoning':'high','fresh_assignment_requested':True,'active_context_target':250000,
  'limits':'Independent backend model/reasoning enforcement and measured active-context telemetry unavailable to this reviewer; parent configuration and current supplied assignment establish intended settings only.'},
 'instruction_sources':{str(root/name):sha(root/name) for name in instructions},
 'external_instruction_sources':{str(path):sha(path) for path in external},
 'changed_paths':{str(root/name):sha(root/name) for name in changed},
 'collaborators':{str(root/name):sha(root/name) for name in collaborators},
 'audit_artifacts':{str(path):sha(path) for path in audit_paths},
 'commands':commands,'failed_audits_and_corrections':failed,
 'scope_limits':['Spec.md read in scoped relevant sections; unrelated runtime requirements omitted.',
  '16-check.py inspected imports, anchor/link helpers and guarded main; fixture-building body not reviewed in full or executed.',
  'Snapshot guidance is byte-identical to substantively read current/baseline sources; duplicate snapshots need no second content interpretation.',
  'Mirror reviewer reports verified against raw originals; raw originals substantively read.',
  'All corpus sources, builders, collectors and new helper read; JSON/source session artifacts parsed and inspected as evidence.',
  'Original corpus parent/child sessions accessed only for selected declaration/dispatch/settings/source-tool/final comparisons. No sibling actual ticket19 review inspected.',
  'No runtime package source/tests, harness run, human QA, code/dependency/config mutation or historical evidence writer execution.']}
(out/'standards-identities.json').write_text(json.dumps(value,indent=2)+'\n')
print(json.dumps({'path':str(out/'standards-identities.json'),'source_files':len(paths),'sha256':sha(out/'standards-identities.json')},indent=2))
