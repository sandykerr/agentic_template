"""One-off descriptive assessment consolidation, with no retirement operations."""
import collections
import copy
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile

HERE = Path(__file__).parent
FEATURE = Path('.scratch/ticket-harness')
EVIDENCE = FEATURE / 'evidence'
CAPTURES = HERE.parent
REVIEW = 'historical-evidence-review-20261116-fresh-01'
INV = CAPTURES / 'inventory-root-72f0b403e93345f0a95967f008f9b99a/inventory-reference.json.gz'
INV_SHA = 'f8aa9c90b82bcc4e34205c8159af1f38469d65e37a8e706836c9c90986124919'
GLOBAL = EVIDENCE / 'historical-evidence-assessment/evidence-review.json'
def load(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return os.path.relpath(p,FEATURE)
def canonical(p): return p if p.startswith('.scratch/') else str(FEATURE / p)
def identity(p): return {'path':rel(p),'size':p.stat().st_size,'sha256':sha(p)}
comparison = load(HERE / 'comparison-results.json')
assert comparison['inventory_sha256'] == INV_SHA and len(comparison['checks']) == 11
bound = {x['path']:x['inventory'] for x in comparison['identities']}
proposals = sorted(CAPTURES.glob('assessor-*/proposal.json')) + [INV.parent / 'shared-proposal.json']
settings = {'configured_model':'gpt-6.1-sol','configured_reasoning':'High','fresh_assignment':True,'context_target':250000,'context_enforcement':'advisory; no hard-enforcement telemetry','backend_delivery_telemetry':'unavailable','occupied_context_telemetry':'unavailable'}
common = {'review_id':REVIEW,'reviewer':'/root/fresh_evidence_review','settings':settings,'report':identity(HERE/'original-review.md'),'comparison':identity(HERE/'comparison-results.json'),'inventory':{'path':rel(INV),'sha256':INV_SHA,'path_root':'repository-relative file identities; authority paths feature-relative'},'format':'descriptive historical assessment v1; no delivered retirement execution schema','execution_support':'unsupported: capture helper only implements allocate/register','execution':{'attempted':False,'removed_paths':[]},'software_acceptance':'unchanged; no QA or ticket acceptance authority'}
batches = collections.defaultdict(list)
approvals = collections.defaultdict(list)
decision_snapshot = []
seen = set()
for proposal in proposals:
    document = load(proposal)
    for g in document['groups']:
        gid = g.get('group_id',g.get('id'))
        if 'folder' in g: folder = g['folder']
        else: folder = 'evidence/ticket-' + g['ticket'].split('/')[-1]
        authority = FEATURE / folder / 'evidence-review.json'
        files = []
        for f in g['files']:
            path = canonical(f['path']);assert path not in seen;seen.add(path)
            original = bound[path]
            item = {k:copy.deepcopy(v) for k,v in original.items() if k in ('path','kind','size','sha256','mode','nlink','target','target_sha256')}
            item['path'] = rel(Path(path))
            if item['path'].endswith('/evidence-review.json'):
                item['identity_scope'] = 'inventory-time mutable capture/review authority; authorized consolidation changes bytes; never approved for deletion'
            if item.get('kind') == 'symlink':
                target = Path(path).parent / item['target']
                item['protected_target'] = {**bound[str(target)], 'path':rel(target)}
            files.append(item)
        action = g['proposed_action']
        decision = {'keep':'keep','delete':'approve routine retirement assessment','merge proposed':'candidate checked; await human merge decision'}[action]
        final = {'decision':decision,'review_id':REVIEW,'deletion_approved':action=='delete','human_decision':{'status':'pending','authority':'actual human only'} if action=='merge proposed' else {'status':'not required for this keep/routine decision'},'execution_eligibility':'blocked; guarded retirement executor and capture/retirement guidance reconciliation absent','future_execution_checks':['exact current identities and unchanged proposal','required retained results/source remain available','actual remaining active/frozen/continuation readers resolved','all current required approvals and policy conditions','guarded Python execution and actual navigation/result recording'],'execution_attempted':False}
        if action == 'keep': final['execution_eligibility'] = 'protected; no deletion proposal approved'
        entry = {'group_id':gid,'files':files,'inventory_binding':common['inventory'],'evidence_type':g['evidence_type'],'proposed_action':action,'reason_codes':g.get('reason_codes',[]),'supporting_facts':g.get('supporting_facts',[])[:3],'remaining_uses':g.get('remaining_uses',[]),'retained_results_and_source':g.get('retained_source_and_results',g.get('retained_results_and_source',g.get('retained_results',[]))),'worker_proposal':{'path':rel(proposal),'sha256':sha(proposal),'group_id':gid,'reference_report':'shared inventory/reference report and immutable proposal contain lexical reader candidates; absence of matches is not absence of use'},'final_review':final}
        if 'exact_source' in g: entry['exact_source'] = g['exact_source']
        loss = g.get('information_loss',g.get('loss',g.get('information_loss_if_deleted')))
        if loss is not None: entry['information_loss'] = loss
        if g.get('replacement_candidate'):
            entry['replacement_candidate'] = identity(Path(g['replacement_candidate']))
            entry['replacement_candidate']['derived_from'] = files
            entry['replacement_review'] = {'status':'checked against originals; human pending','scope':'original-review.md proposed-replacements section and comparison-results.json','originals_retained':True,'renew_on_change':True}
        uncertain = any('UNCERTAIN' in code for code in g.get('reason_codes',[]))
        if g.get('reassessment') is not None:
            original = g['reassessment']
            trigger = original.get('trigger_ticket',original.get('triggering_ticket'))
            entry['reassessment'] = {'trigger_ticket':trigger,'next_human_qa':'ticket-harness/EC1','remaining_use':g.get('remaining_uses',[]),'condition':'Reaching trigger requires reassessment before completion bookkeeping; it does not authorize deletion. Unresolved or no usable trigger goes to next EC1 human evidence QA.','worker_route':original}
        elif uncertain or action != 'keep':
            entry['reassessment'] = {'trigger_ticket':'ticket-harness/26','next_human_qa':'ticket-harness/EC1','remaining_use':g.get('remaining_uses',[]),'condition':'Keep until recorded uncertainty resolved; unresolved choices go to next EC1 human evidence QA.'}
        if uncertain: entry['reassessment']['uncertainty'] = 'Unique historical source/instructions/results or helper/frozen-reader use not cleared; see supporting facts and immutable worker proposal.'
        batches[authority].append(entry)
        if action == 'delete':
            approvals[authority].append({'review_id':REVIEW,'group_id':gid,'actor':'/root/fresh_evidence_review','role':'fresh High evidence reviewer','decision':'approved','action':'delete','authority_scope':'policy judgment for these exact identities only; descriptive record is not an executable schema','files':files,'proposal':identity(proposal),'inventory_sha256':INV_SHA,'human_merge_required':False,'execution':'blocked and unattempted; no guarded executor or capture/retirement guidance reconciliation','conditions':final['future_execution_checks']})
        decision_snapshot.append({'group_id':gid,'authority':rel(authority),'proposed_action':action,'reviewer_decision':decision,'file_count':len(files)})
assert len(seen) == 3286 and len(decision_snapshot) == 116
issues = {p.name[:2]:rel(p) for p in (FEATURE/'issues').glob('[0-9][0-9]-*.md')}
def new_authority(path):
    folder = rel(path.parent)
    return {'schema_version':1,'folder':folder,'scope':{'tickets':[{'id':f'{i:02}','issue':issues[f'{i:02}']} for i in range(1,25)],'shared':path.parent.name,'milestone':None},'captures':[],'shared_records':[],'assessments':[],'approvals':[],'execution_results':[]}
def save(path, value):
    fd,temp = tempfile.mkstemp(prefix='.evidence-review-assessment-',dir=path.parent)
    with os.fdopen(fd,'w') as out:
        json.dump(value,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
    os.replace(temp,path)
shared = sorted(p for p in batches if not p.parent.name.startswith('ticket-'))
all_authorities = sorted(batches)
directory_fd = os.open(EVIDENCE,os.O_RDONLY | os.O_DIRECTORY)
try:
    fcntl.flock(directory_fd,fcntl.LOCK_EX)
    # Validate every existing authority before any replacement. Preserve unknown keys.
    records = {}
    for path in all_authorities+[GLOBAL]:
        d = load(path) if path.exists() else new_authority(path)
        assert d['schema_version'] == 1 and d['folder'] == rel(path.parent)
        assert not any(a.get('review_id') == REVIEW for a in d['assessments']), path
        for key in ('captures','shared_records','assessments','approvals','execution_results'): assert isinstance(d[key],list)
        records[path] = d
    for path,groups in batches.items():
        d = records[path]
        d['assessments'].append({**common,'groups':groups})
        d['approvals'].extend(approvals[path])
        # Tickets link shared authorities, rather than copying their decisions.
        if path.parent.name.startswith('ticket-'):
            ticket = path.parent.name[-2:]
            relevant = shared if int(ticket) >= 10 else [p for p in shared if p.parent.name=='evidence-retention-audit-01']
            for target in relevant:
                if rel(target) not in d['shared_records']: d['shared_records'].append(rel(target))
        save(path,d)
    d = records[GLOBAL]
    d['assessments'].append({**common,'purpose':'consolidation index only; decisions live in corresponding ticket/shared authorities','authorities':[rel(p) for p in all_authorities],'proposals':[identity(p) for p in proposals],'preexisting_missing':identity(INV.parent/'preexisting-missing.json'),'summary':dict(collections.Counter(x['proposed_action'] for x in decision_snapshot))})
    for path in shared:
        if rel(path) not in d['shared_records']: d['shared_records'].append(rel(path))
    save(GLOBAL,d)
finally:
    os.close(directory_fd)
snapshot = {'kind':'original fresh reviewer decision snapshot; current authority remains at linked per-folder records','review_id':REVIEW,'settings':settings,'policy':'.scratch/ticket-harness/evidence-workflow-spec.md evidence-policy-1','inventory':common['inventory'],'source_head':'3b0c1ab7ec41929d3febab44269f791e55897e70','dirty_source_identity':identity(INV.parent/'checkout-dirty.patch'),'report':common['report'],'comparison':common['comparison'],'groups':decision_snapshot,'execution':{'attempted':False,'removed':[],'blocker':'no guarded retirement executor; no shell fallback; capture-only helper cannot retire evidence'},'human_merge_approval':'none; all four proposals route to EC1 human evidence QA','calibration':'No hidden current human labels, repeat trials or backend delivery enforcement telemetry supplied; no calibration/consistency claim','authority_mutation':'Exclusive flock on feature evidence directory descriptor; atomic replacement per authority, preserve all existing keys/captures/shared_records/approval/outcome data','consolidated_at':datetime.now(timezone.utc).isoformat()}
with (HERE/'reviewer-decisions.json').open('x') as out: json.dump(snapshot,out,indent=2);out.write('\n')
print('CONSOLIDATED',len(all_authorities),'folder authorities plus global index;',len(decision_snapshot),'groups;',sum(len(x) for x in approvals.values()),'reviewer approvals; zero execution attempts')
