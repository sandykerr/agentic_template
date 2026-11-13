import hashlib, json, re, subprocess
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
for name in ('23-review-packet.md','23-implementation-report.md'):
    p=out/name
    s=p.read_text()
    for old,new in [('in706','in 706'),('exit0','exit 0'),('wrapper706','wrapper 706'),('all26','all 26'),('success,10','success, 10'),('format:24','format: 24'),('exit3','exit 3'),('mypy1.19.1/Ruff0.14.10','mypy 1.19.1 / Ruff 0.14.10'),('capture:544','capture: 544'),('observations,10,446','observations, 10,446'),('files,3,977,366','files, 3,977,366'),('checked335/593','checked 335 / 593'),('json):544','json): 544'),('cases /10,446','cases / 10,446')]:
        s=s.replace(old,new)
    p.write_text(s)
identity=json.loads((out/'23-final-source.json').read_text())
assert all(hashlib.sha256(Path(n).read_bytes()).hexdigest()==d for n,d in identity['source_hashes'].items())
assert json.loads((out/'23-final-suite-result.json').read_text())['exit']==0
assert [v['exit'] for v in json.loads((out/'23-final-check-results.json').read_text())]==[3,0,0,0,0,0]
links=[]
for name in ('23-criterion-evidence.md','23-review-packet.md','23-implementation-report.md'):
    p=out/name
    for target in re.findall(r'\[[^]]*\]\(([^)]+)\)',p.read_text()):
        assert (p.parent/target.split('#')[0]).exists(),(name,target)
        links.append((name,target))
index=json.loads((out/'23-observation-index.json').read_text())
assert len(index)==544 and len(set(v['scenario'] for v in index))==544
assert len(json.loads((out/'23-raw-manifest.json').read_text()))==10446
print(json.dumps(dict(frozen_identities=len(identity['source_hashes']),validated_document_links=len(links),unique_scenarios=len(index),checks='full suite plus all five static/whitespace gates pass; initial capture import failure retained')))
