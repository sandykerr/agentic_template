"""Validate QA bookkeeping and preserved current/initial evidence, without resuming."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess
import tarfile

root=Path.cwd()
out=root/'.scratch/ticket-harness/evidence/m1-qa-01'
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
start=json.loads((out/'start.json').read_text())
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==start['starting_head']
assert all(digest(root/p)==h for p,h in start['source_files'].items())
with tarfile.open(out/'instruction-snapshot.tar.gz') as tar:
    for name, expected in start['instructions'].items():
        raw=tar.extractfile(name).read()
        assert hashlib.sha256(raw).hexdigest()==expected
        current=(root/name).read_bytes()
        # Only navigation was appended after initial capture; requirements stay exact.
        assert current==raw or current.startswith(raw),name
for p in out.glob('*.py'):
    ast.parse(p.read_text(),filename=str(p))
location=json.loads((out/'demo-location.json').read_text())
run=Path(location['run'])
record=json.loads((run/'run.json').read_text())
request=json.loads((run/'qa-request.json').read_text())
assert record['outcome']=='stopped_at_qa' and not record.get('qa_decisions')
assert request==json.loads((out/'human-checkpoint-request.json').read_text())
assert record==json.loads((out/'human-checkpoint-record.json').read_text())
assert request['request_id']==location['request_id']
assert request['candidate_revision']==location['candidate']
assert record['tickets']['01']['state']=='Done' and record['tickets']['02']['attempt']==0
assert record['feature_complete'] is False
assert sum(g['stage']=='baseline' for g in record['gates'])==1
assert all(g['passed'] for g in record['gates'])
for branch,key in [('dev','development'),('integration','feature')]:
    actual=subprocess.check_output(['git','-C',location['target'],'rev-parse',branch],text=True).strip()
    assert actual==location[key]
assert (Path(location['candidate_worktree'])/'value.txt').read_text()=='2\n'
assert not (Path(location['candidate_worktree'])/'work-02').exists()
archive=json.loads((out/'demo-archive.json').read_text())
assert digest(out/archive['archive'])==archive['sha256']
with tarfile.open(out/archive['archive']) as tar:
    archived={m.name.lstrip('./'):tar.extractfile(m).read() for m in tar.getmembers() if m.isfile()}
    assert archived['run/run.json']==(run/'run.json').read_bytes()
    assert archived['run/qa-request.json']==(run/'qa-request.json').read_bytes()
    assert archived['run/qa-checkpoint.json']==(run/'qa-checkpoint.json').read_bytes()
    archive_count=len(archived)
links=[]
for file in [out/'qa-guide.md',root/'next_agent_prompt.md',root/'.scratch/ticket-harness/reviews/M1-architecture-01.md',out/'standards-01-envelope.md']:
    if not file.exists():
        continue
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        path=link.split('#')[0]
        if path:
            target=file.parent/path
            assert target.exists(),(str(file.relative_to(root)),link)
            links.append((str(file.relative_to(root)),link))
report=out/'standards-01-original.md'
assert report.exists(),'Required original report absent'
report_sha=digest(report)
assert 'review-M1-architecture-01/standards-01/F1' in report.read_text()
for ticket in sorted((root/'.scratch/ticket-harness/issues').glob('*.md')):
    if 10<=int(ticket.name[:2])<=24:
        assert '../reviews/M1-architecture-01.md' in ticket.read_text()
whitespace=subprocess.run(['git','diff','--check'],capture_output=True,text=True)
assert whitespace.returncode==0,whitespace.stdout+whitespace.stderr
result=dict(source=start['starting_head'],cumulative_baseline=start['cumulative_baseline'],runtime_test_example_packaging_files_unchanged=len(start['source_files']),original_instruction_files_preserved=len(start['instructions']),script_syntax='passed',links_checked=len(links),archived_demo_files_readback=archive_count,stopped_live_request_and_refs='verified',gates_passed=len(record['gates']),consumed_approvals=0,full_suite='Retained original ab08f7f provenance; not rerun for bookkeeping',focused_current_checks=json.loads((out/'check-results.json').read_text()),report_sha256=report_sha,whitespace_exit=whitespace.returncode,milestone_accepted=False,readiness='held: review-M1-architecture-01/standards-01/F1')
(out/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
