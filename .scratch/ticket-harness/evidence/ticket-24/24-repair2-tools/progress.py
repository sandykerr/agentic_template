"""Bounded non-mutating progress/host-pressure sample while final gates run."""
import json,os,time
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence');samples=out/'24-repair2-progress.json'
r=dict(utc=time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),host_load=Path('/proc/loadavg').read_text().strip(),cpu_count=os.cpu_count(),pressure={n:Path('/proc/pressure',n).read_text() for n in ('cpu','io','memory')},phases={})
for phase in ('focused','final'):
 raw=Path('/tmp/ticket24-repair2-'+phase+'-raw');files=list(raw.glob('*/observations.json'));latest=max(files,key=lambda p:p.stat().st_mtime)
 r['phases'][phase]=dict(captured=len(files),last_capture_utc=time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(latest.stat().st_mtime)),scenario=json.loads(latest.read_text())['scenario'])
r['recent_records']=[]
for p in Path('/tmp').glob('ticket-harness-test-*/run/run.json'):
 if time.time()-p.stat().st_mtime<1200:
  try:
   v=json.loads(p.read_text());r['recent_records'].append(dict(path=str(p),outcome=v.get('outcome'),stage=v.get('gates',[{}])[-1].get('stage'),gates=len(v.get('gates',[])),age_seconds=round(time.time()-p.stat().st_mtime,2)))
  except (ValueError,IndexError):pass
existing=json.loads(samples.read_text()) if samples.exists() else []
existing.append(r);samples.write_text(json.dumps(existing,indent=2)+'\n');print(json.dumps(r))
