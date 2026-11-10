"""Retain selected real assignment evidence; do not copy unrelated session context."""
from pathlib import Path
import hashlib
import json
import shutil

OUT = Path(__file__).resolve().parent
LOGS = Path('/home/ajkerr1/.codex/sessions/2026/11/10')
OWN = LOGS / 'rollout-2026-11-10T11-19-06-01a1c641-8953-7482-bf78-307a87fa5e90.jsonl'
CHILD = {
    'spec-g1': LOGS / 'rollout-2026-11-10T11-22-35-01a1c644-ba92-7cd2-bd18-6ffce685a704.jsonl',
    'standards-g1': LOGS / 'rollout-2026-11-10T11-22-48-01a1c644-ec26-74a0-ac6a-7655f53ee9bc.jsonl',
}

def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines()]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def create(path, value):
    data = json.dumps(value, indent=2) + '\n'
    if path.exists():
        assert path.read_text() == data, f'original evidence changed: {path}'
    else:
        path.write_text(data)

own = rows(OWN)
assignments = []
for row in own:
    p = row['payload']
    if row['type'] != 'response_item' or p.get('type') != 'function_call' or p.get('name') != 'spawn_agent':
        continue
    args = json.loads(p['arguments'])
    if args['task_name'] not in ['corpus_spec_g1', 'corpus_standards_g1']:
        continue
    label = args['task_name'].removeprefix('corpus_').replace('_', '-')
    create(OUT / (label + '-assignment.json'), {'timestamp': row['timestamp'], 'call_id': p['call_id'], 'arguments': args})
    assignments.append({'label': label, 'assignment': '/root/implement_19/' + args['task_name'],
                        'timestamp': row['timestamp'], 'settings': {k:args[k] for k in ['fork_turns', 'model', 'reasoning_effort']},
                        'active_context_target': 250000,
                        'prompt_path': label + '-assignment.json',
                        'prompt_sha256': sha(OUT / (label + '-assignment.json'))})
assert len(assignments) == 2
create(OUT / 'assignments.json', {'assignments': assignments, 'limits': 'Configured arguments only. Backend telemetry and hard active-context enforcement unavailable; filesystem isolation advisory.'})

# --final runs only once both independent assignments have finished.
import sys
if '--final' in sys.argv:
    provenance = {}
    for label, path in CHILD.items():
        selected, final = [], []
        for row in rows(path):
            p = row['payload']
            if row['type'] == 'session_meta':
                source = p.get('source', {})
                assert source.get('subagent', {}).get('thread_spawn', {}).get('agent_path') == '/root/implement_19/corpus_' + label.replace('-', '_')
                selected.append({'timestamp': row['timestamp'], 'type': 'session_identity', 'id':p['id'], 'cwd':p['cwd'], 'source':source, 'model_provider':p.get('model_provider')})
            elif row['type'] == 'turn_context':
                selected.append({'timestamp':row['timestamp'], 'type':'observed_turn_settings', 'settings':{k:p[k] for k in ['model','effort','reasoning_effort','model_provider','cwd'] if k in p}})
            elif row['type'] == 'response_item' and p.get('type') in ['function_call', 'function_call_output']:
                selected.append(row)
            elif row['type'] == 'response_item' and p.get('type') == 'message' and p.get('role') == 'assistant' and p.get('phase') == 'final_answer':
                final.append('\n'.join(x['text'] for x in p.get('content', []) if x.get('type') == 'output_text'))
        assert len(final) == 2, (label, 'original plus preservation attestation not available')
        create(OUT / (label + '-tool-evidence.json'), selected)
        raw = OUT / (label + '-raw.md')
        if raw.exists():
            assert raw.read_text() == final[0]
        else:
            raw.write_text(final[0])
        axis = label.removesuffix('-g1')
        input_file = Path('/tmp') / f'development-review-19-{axis}-g1-input.txt'
        preserved = Path('/tmp') / f'development-review-19-{axis}-g1.md'
        for original, target in [(input_file, OUT/(label+'-input.txt')), (preserved, OUT/(label+'-reviewer-preserved.md'))]:
            if target.exists():
                assert target.read_bytes() == original.read_bytes()
            else:
                shutil.copyfile(original, target)
        # Retain original session final even if a preservation transcription differs.
        create(OUT/(label+'-preservation-attestation.json'), {'original_followup_final':final[1]})
        provenance[label] = {'raw_report_origin':'exact first plaintext assistant final_answer from verified child session',
                             'raw_report_sha256':sha(raw),
                             'reviewer_preserved_sha256':sha(preserved),
                             'preservation_byte_match':raw.read_bytes() == preserved.read_bytes(),
                             'preservation_matches_after_terminal_newline':raw.read_text().rstrip('\n') == preserved.read_text().rstrip('\n'),
                             'readable_input_origin':'reviewer-attested verbatim transcription of actually received initial assignment; dispatch log message is opaque',
                             'readable_input_sha256':sha(input_file),
                             'limits':'Readable input is attested, not byte-verified against decrypted dispatch. No backend enforcement or instruction effectiveness proof.'}
    create(OUT/'capture-provenance.json', provenance)
    followups = []
    for row in own:
        p = row['payload']
        if row['type'] == 'response_item' and p.get('type') == 'function_call' and p.get('name') in ['send_message','followup_task']:
            args = json.loads(p['arguments'])
            if args.get('target') in ['corpus_spec_g1','corpus_standards_g1']:
                followups.append(row)
    create(OUT/'capture-followups.json', {'original_serialized_records':followups, 'purpose':'Evidence-only report/input preservation; no key or reassessment. Message values may be opaque.'})
    files = sorted(p for p in OUT.iterdir() if p.is_file() and (p.name.endswith('-raw.md') or p.name.endswith('-assignment.json') or p.name.endswith('-tool-evidence.json') or p.name.endswith('-input.txt') or p.name.endswith('-reviewer-preserved.md') or p.name.endswith('-preservation-attestation.json') or p.name in ['assignments.json','capture-provenance.json','capture-followups.json']))
    create(OUT / 'review-capture.json', {'sha256':{p.name:sha(p) for p in files}, 'source':'selected original Codex session records; raw.md is exact assistant final content, without envelope or appended newline'})
    # Supplement the first narrow collector rather than rewriting its saved outputs.
    # functions.exec uses custom_tool_call, and delivered tasks use agent_message.
    supplement = {}
    for label, path in CHILD.items():
        records = [row for row in rows(path) if row['type'] == 'response_item'
                   and row['payload'].get('type') in ['custom_tool_call','custom_tool_call_output','agent_message']]
        create(OUT/(label+'-source-records.json'), records)
        received = [row for row in records if row['payload']['type'] == 'agent_message'][0]
        text = '\n'.join(part['text'] for part in received['payload']['content'] if part['type'] == 'input_text')
        payload = text.split('\nPayload:\n', 1)[1]
        readable = (OUT/(label+'-input.txt')).read_text()
        opaque = any(part['type'] == 'encrypted_content' for part in received['payload']['content'])
        matched = None if opaque else payload.rstrip('\n') == readable.rstrip('\n')
        supplement[label] = {'original_received_agent_message':received,
                             'source_records_path':label+'-source-records.json',
                             'source_records_sha256':sha(OUT/(label+'-source-records.json')),
                             'received_payload_has_encrypted_content':opaque,
                             'preserved_input_matches_original_received_payload_except_terminal_newline':matched,
                             'custom_tool_call_count':sum(row['payload']['type']=='custom_tool_call' for row in records),
                             'custom_tool_output_count':sum(row['payload']['type']=='custom_tool_call_output' for row in records)}
    create(OUT/'review-capture-supplement.json', {'supersedes_limit':'Initial collector omitted custom_tool_call/output and agent_message items. Original saved records remain unchanged.', 'axes':supplement, 'limits':'Received task wrappers are plaintext but payloads are encrypted; readable input remains reviewer-attested. Original tool observations are retained. No backend enforcement or instruction effectiveness proof.'})
print('Captured actual assignments' + (' and both original finals/tool evidence' if '--final' in sys.argv else ' only'))
