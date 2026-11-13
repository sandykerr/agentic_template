"""Index real exploratory outcomes without relabeling them as final-source gates."""
import json,sys
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
original='tests/test_milestones.py::test_development_alias_after_validation_cannot_follow_automatic_integration'
selection=[original,'tests/test_milestones.py::test_changed_development_base_is_combined_with_feature_using_a_clean_same_file_merge','tests/test_qa_promotion.py::test_deep_invalid_decision_is_rejected_and_later_approval_can_promote']
rows=[]
for phase,tests,code,meaning in [
 ('red-original',[original],1,'Observer setup failure: vanished proc entry; no regression conclusion'),
 ('red-original-trial2',[original],1,'Original rejected Git source permits unauthorized development advancement'),
 ('green-original',selection,1,'Local stdin/EOF sequencing failure and optional-record-key assertion error; not green'),
 ('green-original-trial2',selection,0,'3 passed after correcting EOF sequencing and assertion'),
]:
 rows.append(dict(phase=phase,command=[sys.executable,'-m','pytest','-q',*tests],exit=code,log=f'24-repair2-{phase}.log',observation=meaning,source_limit='Actual executed commands/terminal outcomes; early development source hashes were not retained'))
for phase in ('red-captured','green-captured'):
 r=json.loads((out/f'24-repair2-{phase}.json').read_text());rows.append(dict(phase=phase,command=r['command'],exit=r['exit'],log=r['log'],record=f'24-repair2-{phase}.json',source_limit='Initial snapshot only for green-captured: annotation edited/restored during exploratory execution; final wrappers freeze/check actual source'))
rows.append(dict(phase='focused',command=[sys.executable,'-m','pytest','-q','tests/test_milestones.py','tests/test_qa_promotion.py','tests/test_continuation.py','tests/test_transaction.py','-p','capture24repair2'],exit=130,completed=False,passing_gate=False,observation='Root directed ending optional broad replay after targeted5pass; session Ctrl-C succeeded',log='24-repair2-focused-check-0.log',record='24-repair2-focused-raw-audit.json'))
(out/'24-repair2-development-checks.json').write_text(json.dumps(rows,indent=2)+'\n')
