"""Index retained manual TDD command logs and observed tool-session exits."""
import json,sys
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
rows=[]
for phase,selection,files,exit_code,observation in [
('red-decision','deep_invalid',['tests/test_qa_promotion.py'],1,'1 failed/1 passed; decoder failure reproduced, safe request-depth parameter later removed'),
('green-decision','deep_invalid',['tests/test_qa_promotion.py'],0,'1 passed'),
('red-alias-setup','symbolic_milestone_destinations',['tests/test_milestones.py'],1,'3 failed'),
('green-alias-setup','symbolic_milestone_destinations',['tests/test_milestones.py'],0,'3 passed'),
('red-alias-transitions','aliased_during_work or symbolic_destination or symbolic-dev or symbolic-feature',['tests/test_milestones.py','tests/test_qa_promotion.py','tests/test_continuation.py'],130,'Interrupted unbounded synchronous continuation wait; partial log only, not completed red run'),
('red-alias-transitions-bounded','aliased_during_work or symbolic_destination or symbolic-dev or symbolic-feature',['tests/test_milestones.py','tests/test_qa_promotion.py','tests/test_continuation.py'],1,'7 failed; existing bounded foreground seam'),
('green-alias-transitions','aliased_during_work or symbolic_destination or symbolic-dev or symbolic-feature',['tests/test_milestones.py','tests/test_qa_promotion.py','tests/test_continuation.py'],0,'7 passed'),
('red-alias-readiness','regression_cannot_present',['tests/test_milestones.py'],1,'1 failed'),
('green-alias-readiness','regression_cannot_present',['tests/test_milestones.py'],0,'1 passed'),
]:
 rows.append(dict(command=[sys.executable,'-m','pytest','-q',*files,'-k',selection],exit=exit_code,observation=observation,log=f'24-repair1-{phase}.log',source=f'24-repair1-{phase if phase != "red-alias-transitions" else "red-alias-transitions"}-source.json'))
assert all((out/r['log']).exists() and (out/r['source']).exists() for r in rows)
(out/'24-repair1-development-checks.json').write_text(json.dumps(rows,indent=2)+'\n')
