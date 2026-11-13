"""Preserve completed evaluator preparation/mutation/audit command records once."""
from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parents[3];EV=ROOT/'.scratch/ticket-harness/evidence'
LOG=Path('/home/ajkerr1/.codex/sessions/2026/11/10/rollout-2026-11-10T12-33-59-01a1c686-1785-7f11-b1b0-fafc5e4158f3.jsonl')
rows=[json.loads(x) for x in LOG.read_text().splitlines()]
calls={r['payload']['call_id']:r for r in rows if r['type']=='response_item' and r['payload'].get('type')=='custom_tool_call' and r['payload'].get('name')=='exec' and 'c5' in r['payload'].get('input','').lower()}
outputs={r['payload']['call_id']:r for r in rows if r['type']=='response_item' and r['payload'].get('type')=='custom_tool_call_output'}
complete=set(calls)&set(outputs)
selected=[r for r in rows if r['type']=='response_item' and r['payload'].get('call_id') in complete]
out=EV/'19-repair-c5-workflow-command-records.json';assert not out.exists()
out.write_text(json.dumps({'captured_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_session':str(LOG),'scope':'Completed C5 evaluator preparation/mutation/audit calls and exact outputs, including initial reserved-word SyntaxError and correction. Final standalone commands have their separate exact log; actual reviewer/source records have separate immutable captures. This is command provenance, not judgment scoring.','completed_call_count':len(complete),'records':selected},indent=2)+'\n')
print(json.dumps({'output':str(out.relative_to(ROOT)),'completed_calls':len(complete)},indent=2))
