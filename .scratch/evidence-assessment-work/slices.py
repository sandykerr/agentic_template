import gzip, json, hashlib
from pathlib import Path
root=Path.cwd()
work=root/'.scratch/evidence-assessment-work'
dest=root/'.scratch/ticket-harness/evidence/historical-evidence-assessment/captures/inventory-root-72f0b403e93345f0a95967f008f9b99a'
p=dest/'inventory-reference.json.gz'
data=json.loads(gzip.decompress(p.read_bytes()))
for low,high in [(1,8),(9,16),(17,24)]:
    prefixes=[f'.scratch/ticket-harness/evidence/ticket-{i:02d}/' for i in range(low,high+1)]
    files=[f for f in data['files'] if any(f['path'].startswith(x) for x in prefixes)]
    names={f['path'] for f in files}
    refs=[r for r in data['references'] if any(t in names for t in r['targets'])]
    value=dict(derived_from=str(p.relative_to(root)), inventory_sha256=hashlib.sha256(p.read_bytes()).hexdigest(), files=files,references=refs,archives=[a for a in data['archives'] if a['path'] in names])
    (work/f'slice-{low:02d}-{high:02d}.json').write_text(json.dumps(value,separators=(',',':')))
old=json.loads(gzip.decompress((root/'.scratch/ticket-harness/evidence/evidence-retention-audit-01/worker-inventory-data.json.gz').read_bytes()))
print('old sample',str(old['files'][0])[:1500],flush=True)
print('summary',json.dumps(dict(inventory_sha256=hashlib.sha256(p.read_bytes()).hexdigest(), files=len(data['files']), evidence=data['evidence_count'], bytes=data['evidence_logical_bytes'],missing_tracked=data['preexisting_tracked_missing'], shared=[f for f in data['files'] if '/evidence/m1-' in f['path'] and f['kind']=='symlink'])),flush=True)
