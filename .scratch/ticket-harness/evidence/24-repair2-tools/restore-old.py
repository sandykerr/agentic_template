"""Restore immutable pre-refactor stopped bytes at their genuine absolute paths."""
import hashlib,json,tarfile
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence/24-repair2-checkpoint');out.mkdir()
old=out.parent/'24-checkpoint';producer=json.loads((old/'producer.json').read_text());home=Path(producer['home']);retained=Path('/tmp/ticket24-repair1-completed-retained2')
assert not retained.exists()
prior=json.loads((home/'run/run.json').read_text());assert prior['outcome']=='completed'
home.rename(retained)
archive=old/'stopped-live.tar.gz'
with tarfile.open(archive,'r:gz') as stream:
 assert all(m.name=='tmp/'+home.name or m.name.startswith('tmp/'+home.name+'/') for m in stream.getmembers())
 stream.extractall('/',filter='data')
assert json.loads((home/'run/run.json').read_text())==producer['record']
r=dict(original_producer=str(old/'producer.json'),original_stopped_archive=str(archive),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),repair1_completed_live_retained=str(retained),restored_absolute_home=str(home),restored_record_equals_genuine_producer=True)
(out/'restore.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
