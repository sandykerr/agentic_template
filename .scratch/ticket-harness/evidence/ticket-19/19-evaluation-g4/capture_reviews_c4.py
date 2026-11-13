"""Capture actual isolated review evidence at new paths; never overwrite originals."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

OUT = Path(__file__).resolve().parent
LOGS = Path('/home/ajkerr1/.codex/sessions/2026/11/10')
OWN = LOGS / 'rollout-2026-11-10T11-43-32-01a1c657-e8c7-7561-b2e1-72cba6b15731.jsonl'
CHILD = {
    'spec-c4': LOGS / 'rollout-2026-11-10T12-12-36-01a1c672-84aa-77f2-9728-c0d79c6e1027.jsonl',
    'standards-c4': LOGS / 'rollout-2026-11-10T12-12-47-01a1c672-ae8d-7510-b06a-35cfc6d3c656.jsonl',
}
def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines()]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def create(path, value):
    data = json.dumps(value,indent=2)+'\n'
    if path.exists():
        assert path.read_text() == data, f'preserved evidence differs: {path}'
    else:
        path.write_text(data)

assignments = []
for row in rows(OWN):
    p = row['payload']
    if row['type'] != 'response_item' or p.get('type') != 'function_call' or p.get('name') != 'spawn_agent':
        continue
    args = json.loads(p['arguments'])
    if args.get('task_name') not in ['corpus_spec_c4','corpus_standards_c4']:
        continue
    label = args['task_name'].removeprefix('corpus_').replace('_','-')
    create(OUT/(label+'-dispatch.json'),row)
    prompt = OUT/(label+'-input.txt')
    assignments.append({'label':label,'assignment':'/root/repair19/'+args['task_name'],
        'timestamp':row['timestamp'],'settings':{k:args[k] for k in ['fork_turns','model','reasoning_effort']},
        'active_context_target':250000,'dispatch_path':label+'-dispatch.json',
        'dispatch_sha256':sha(OUT/(label+'-dispatch.json')),
        'known_readable_prompt_path':prompt.name,'known_readable_prompt_sha256':sha(prompt),
        'prompt_origin':'Exact known author text saved before dispatch, then passed as spawn message; serialized message may be encrypted. Not independent decrypted-delivery proof.'})
assert len(assignments) == 2
create(OUT/'assignments.json',{'assignments':assignments,'limits':'Configured settings and advisory context target; backend telemetry, measured context/hard enforcement unavailable; workspace isolation advisory.'})
followups = []
for row in rows(OWN):
    p = row['payload']
    if row['type'] == 'response_item' and p.get('type') == 'function_call' and p.get('name') == 'send_message':
        args = json.loads(p['arguments'])
        if args.get('target') in ['corpus_spec_c4','corpus_standards_c4']:
            followups.append(row)
assert len(followups) == 2
ids = {row['payload']['call_id'] for row in followups}
receipts = [row for row in rows(OWN) if row['type'] == 'response_item'
            and row['payload'].get('type') == 'function_call_output'
            and row['payload'].get('call_id') in ids]
assert len(receipts) == 2
create(OUT/'followup-dispatches.json',{'original_calls':followups,'original_receipts':receipts,
    'known_readable_author_text_path':'audit-clarification.txt',
    'known_readable_author_text_sha256':sha(OUT/'audit-clarification.txt'),
    'scope':'Same pre-saved neutral all-file/hidden-file aggregate clarification sent to both axes; no key, prior/sibling findings, source change or re-review. Saved text has a terminal newline; sent message omits that file terminator.'})
if '--final' in sys.argv:
    provenance = {}
    for label,path in CHILD.items():
        selected, final = [], []
        for row in rows(path):
            p = row['payload']
            if row['type'] == 'session_meta':
                source = p.get('source',{})
                assert source['subagent']['thread_spawn']['agent_path'] == '/root/repair19/corpus_'+label.replace('-','_')
                selected.append({'timestamp':row['timestamp'],'type':'session_identity','id':p['id'],'cwd':p['cwd'],'source':source,'model_provider':p.get('model_provider')})
            elif row['type'] == 'turn_context':
                selected.append({'timestamp':row['timestamp'],'type':'observed_turn_settings','settings':{k:p[k] for k in ['model','effort','reasoning_effort','model_provider','cwd'] if k in p}})
            elif row['type'] == 'response_item' and p.get('type') in ['function_call','function_call_output','custom_tool_call','custom_tool_call_output','agent_message']:
                selected.append(row)
            elif row['type'] == 'response_item' and p.get('type') == 'message' and p.get('role') == 'assistant' and p.get('phase') == 'final_answer':
                final.append('\n'.join(x['text'] for x in p.get('content',[]) if x.get('type') == 'output_text'))
        assert len(final) == 1, (label,'expected exactly one original full-corpus assessment')
        raw = OUT/(label+'-raw.md')
        if raw.exists():
            assert raw.read_text() == final[0]
        else:
            raw.write_text(final[0])
        create(OUT/(label+'-source-records.json'),selected)
        axis = label.removesuffix('-c4')
        original = Path('/tmp')/f'development-review-19-{axis}-c4-report.md'
        preserved = OUT/(label+'-reviewer-saved.md')
        if preserved.exists():
            assert preserved.read_bytes() == original.read_bytes()
        else:
            preserved.write_bytes(original.read_bytes())
        provenance[label] = {'session_path':str(path),'original_final_count':len(final),
            'raw_report_origin':'Exact first plaintext assistant final_answer from verified child session',
            'raw_report_sha256':sha(raw),'reviewer_saved_sha256':sha(preserved),
            'saved_byte_match':raw.read_bytes() == preserved.read_bytes(),
            'saved_match_ignoring_terminal_newline':raw.read_text().rstrip('\n') == preserved.read_text().rstrip('\n'),
            'known_prompt_origin':'Known plaintext author input pre-saved before dispatch; no encrypted-log recovery required',
            'source_records_sha256':sha(OUT/(label+'-source-records.json')),
            'limits':'Opaque received task serialization is retained; pre-saved readable input does not establish backend instruction effectiveness. No re-review or report-preservation followup.'}
    create(OUT/'capture-provenance.json',provenance)
    names = [p for p in OUT.iterdir() if p.is_file() and (p.name.endswith(('-raw.md','-source-records.json','-dispatch.json','-input.txt','-reviewer-saved.md')) or p.name in ['assignments.json','capture-provenance.json','audit-clarification.txt','followup-dispatches.json'])]
    create(OUT/'review-capture.json',{'sha256':{p.name:sha(p) for p in sorted(names)},'origin':'Actual child session settings, calls/outputs/received messages and exact original plaintext final; known readable prompts predate dispatch.'})
print('Captured C4 assignments'+(' and both original reports/source records' if '--final' in sys.argv else ''))
