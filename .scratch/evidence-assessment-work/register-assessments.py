"""Register original observations and separately labeled derived assessment packages."""
import json, subprocess
from pathlib import Path
feature=Path('.scratch/ticket-harness')
base=feature/'evidence/historical-evidence-assessment/captures'
inventory='evidence/historical-evidence-assessment/captures/inventory-root-72f0b403e93345f0a95967f008f9b99a/inventory-reference.json.gz'
for name in ['inventory-root-72f0b403e93345f0a95967f008f9b99a','assessor-01-08-ec3c831ecd3a4c4c91e28c138129a678','assessor-09-16-d100832579c14d66a22bc1bce5de27b3','assessor-17-24-36f6eadbac774680a069d5cdfff8758f']:
    folder=base/name
    cmd=['.venv/bin/python','-m','ticket_harness.evidence','--feature',str(feature),'register','--allocation',str(folder.absolute()/'allocation.json'),'--source-version','HEAD 3b0c1ab7ec41929d3febab44269f791e55897e70 plus checkout-dirty.patch and shared per-file identities; historical sources remain separately attributed','--activity','Historical inventory/reference inspection and content/use assessment under evidence-policy-1; no runtime replay','--result','Assessment/proposals only; no deletion, human merge approval or milestone acceptance']
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.name!='allocation.json':cmd+=['--file',p.name]
    if not name.startswith('inventory-root'):
        cmd+=['--kind','derived','--derived-from',inventory]
    result=subprocess.run(cmd,text=True,capture_output=True)
    if result.returncode:raise RuntimeError(result.stderr)
    value=json.loads(result.stdout)
    print(json.dumps(dict(actor=name,capture_id=value['capture']['id'],kind=value['capture']['kind'],files=len(value['capture']['files']))),flush=True)
