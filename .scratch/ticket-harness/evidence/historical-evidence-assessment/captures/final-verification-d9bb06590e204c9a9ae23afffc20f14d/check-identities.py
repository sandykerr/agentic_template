"""One-off read-only evidence identity/navigation check; no retirement operations."""
import gzip
import hashlib
import json
import os
import stat
import subprocess
from pathlib import Path

root=Path.cwd()
feature=root/'.scratch/ticket-harness'
capture=feature/'evidence/historical-evidence-assessment/captures/final-verification-d9bb06590e204c9a9ae23afffc20f14d'
inventory_path=feature/'evidence/historical-evidence-assessment/captures/inventory-root-72f0b403e93345f0a95967f008f9b99a/inventory-reference.json.gz'
inv=json.loads(gzip.decompress(inventory_path.read_bytes()))
def sha(data):return hashlib.sha256(data).hexdigest()
missing=[]; changed=[]; metadata=[]; unchanged=0
mutable_authorities={f'.scratch/ticket-harness/evidence/ticket-{i:02d}/evidence-review.json' for i in range(1,25)}
for item in inv['files']:
    path=root/item['path']
    if not path.exists() and not path.is_symlink():
        missing.append(item['path']);continue
    actual_kind='symlink' if path.is_symlink() else 'regular' if path.is_file() else 'other'
    data=os.readlink(path).encode() if actual_kind=='symlink' else path.read_bytes() if actual_kind=='regular' else b''
    if sha(data)!=item['sha256'] or actual_kind!=item['kind']:
        change=dict(path=item['path'],before=item['sha256'],after=sha(data),before_kind=item['kind'],after_kind=actual_kind)
        if item['path'] in mutable_authorities:metadata.append(change)
        else:changed.append(change)
    else:unchanged+=1
authorities=[]; captured=[]
pending=list((feature/'evidence').glob('*/evidence-review.json')); seen=set()
while pending:
    p=pending.pop()
    if p in seen:continue
    seen.add(p)
    value=json.loads(p.read_text())
    assert value['schema_version']==1,p
    assert value['folder']==str(p.parent.relative_to(feature)),p
    for ticket in value['scope']['tickets']:
        assert (feature/ticket['issue']).is_file(),(p,ticket)
    for field in ['captures','shared_records','assessments','approvals','execution_results']:assert isinstance(value[field],list),(p,field)
    for reference in value['shared_records']:
        assert (feature/reference).is_file(),(p,reference)
        pending.append(feature/reference)
    for receipt in value['captures']:
        for item in receipt['files']:
            source=feature/item['path']
            assert source.is_file() and not source.is_symlink(),source
            assert source.stat().st_size==item['size'] and sha(source.read_bytes())==item['sha256'],source
            captured.append(item['path'])
    authorities.append(dict(path=str(p.relative_to(feature)),captures=len(value['captures']),assessments=len(value['assessments']),approvals=len(value['approvals']),execution_results=len(value['execution_results'])))
current_deleted=subprocess.check_output(['git','ls-files','--deleted','-z']).decode().split('\0')
current_deleted=sorted(p for p in current_deleted if p)
assert current_deleted==sorted(inv['preexisting_tracked_missing']),'New tracked deletion or changed preexisting missing set'
assert not missing,missing
head=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()
head_binding=[]
if head!=inv['head']:
    advanced_paths=subprocess.check_output(['git','diff','--name-only',inv['head'],head]).decode().splitlines()
    assert set(advanced_paths)=={'ticket_harness/evidence.py','tests/test_evidence.py'},advanced_paths
    initial_by_path={item['path']:item for item in inv['files']}
    for path in advanced_paths:
        blob=subprocess.check_output(['git','show',head+':'+path])
        actual=(root/path).read_bytes()
        assert sha(blob)==sha(actual)==initial_by_path[path]['sha256'],path
        head_binding.append(dict(path=path,inventory_sha256=initial_by_path[path]['sha256'],current_git_blob_sha256=sha(blob),current_working_file_sha256=sha(actual)))
outside_working_paths={'.scratch/ticket-harness/evidence/ticket-25/'+p for p in ['25-evidence-index.md','25-repair1-current-inputs-driver.log','captures/verification-71288fc1a1da4058830978bc454711dc/pytest.stdout','evidence-review.json']}
outside_changes=[c for c in changed if c['path'] in outside_working_paths]
unexpected=[c for c in changed if c['path']!='.scratch/ticket-harness/evidence/README.md' and '/__pycache__/' not in c['path'] and c['path'] not in outside_working_paths]
assert not unexpected,unexpected
link=feature/'evidence/ticket-17/17-walkthroughs/case-c/case-c-report.md'
assert link.is_symlink() and os.readlink(link)=='report.md'
nav=(feature/'evidence/README.md').read_text()
assert '(historical-evidence-assessment/evidence-review.json)' in nav
assert 'no removals executed' in nav
assert (feature/'evidence/historical-evidence-assessment/evidence-review.json').is_file()
result=dict(head=head,host=os.uname().nodename,architecture=os.uname().machine,inventory_sha256=sha(inventory_path.read_bytes()),unchanged_files=unchanged,missing_survivors=missing,allowed_navigation_changes=changed,expected_authority_metadata_changes=metadata,preexisting_tracked_missing_count=len(current_deleted),new_tracked_missing=[],removed_this_task=[],symlink_target='report.md',capture_file_identities_verified=len(captured),authorities=authorities,checks={'baseline_survivors':'pass','protected_source_instructions_reviews_approvals':'pass; all inventoried survivors unchanged except maintained index and authority metadata','current_navigation':'pass; new target exists and explicitly says no removal','affected_readers':'pass for current authority/capture/shared links; original historical paths preserved; runtime completed_runs/frozen QA/restore readers inspected, never executed','summary_comparison':'separate fresh High reviewer comparison-results.json and original-review.md','runtime_replay':'not performed'},execution_gap='No guarded evidence retirement executor; all removals unattempted. Approval cannot substitute for immediate guarded identity/consumer/protection recheck.',limits=['Existing 5815 missing historical mapped paths and45 tracked missing are baseline observations, not removals by this task.','Lexical search does not establish no consumers; deferred groups remain protected.','No external run registry/intent discovery or live continuation validation was performed.'])
result['inspection_tool_identities']=[dict(path=str(p.relative_to(root)),sha256=sha(p.read_bytes())) for p in sorted((root/'.scratch/evidence-assessment-work').glob('*.py'))]
result['outside_scope_working_changes_preserved']=outside_changes
result['head_at_inventory']=inv['head']
result['concurrent_head_binding']=head_binding
result['commit_by_this_task']=False
result['allowed_navigation_changes']=[c for c in changed if c not in outside_changes]
result['checks']['protected_source_instructions_reviews_approvals']='pass for all assessed historical originals, source and instructions; expected authority/index updates separated from explicitly reported concurrent ticket25 working outputs'
result['verification_history']=['Initial final-check attempt treated archived nested test-fixture registries as live authorities and stopped on their different feature root; checker narrowed to current top-level authorities and shared-record closure. Fixture bytes were neither changed nor reinterpreted.','Next attempt detected concurrent ticket25 index/driver/unregistered pytest stdout changes. Preserve them, record their observed identities separately, renew relevant consumer assessment with fresh High reviewer; never present their589pass runtime result as a cleanup execution.']
if head_binding:result['verification_history'].append('Concurrent ticket25 repair committed the two files already dirty at inventory, advancing HEAD to '+head+'. Exact Git blobs, current working bytes and original inventory hashes match for both; original review provenance remains at original HEAD plus dirty identities. No commit was made by this cleanup.')
(capture/'identity-navigation-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(result='pass',unchanged=unchanged,metadata_changed=len(metadata),navigation_or_cache_changes=len(changed),authorities=len(authorities),captures_verified=len(captured),missing_survivors=len(missing))),flush=True)
