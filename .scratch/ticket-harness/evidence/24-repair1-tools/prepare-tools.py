"""Version existing capture tooling without overwriting original evidence paths."""
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence')
source=out/'24-tools'
target=out/'24-repair1-tools'
text=(source/'capture24.py').read_text().replace('TICKET24_RAW','TICKET24REPAIR1_RAW')
(target/'capture24repair1.py').write_text(text)
text=(source/'checks.py').read_text().replace("24-final-source.json","24-repair1-final-source.json").replace("'/tmp/ticket24-'","'/tmp/ticket24-repair1-'").replace("{out/'24-tools'}","{out/'24-repair1-tools'}").replace('TICKET24_RAW','TICKET24REPAIR1_RAW').replace("'capture24'","'capture24repair1'").replace("f'24-{mode}","f'24-repair1-{mode}")
(target/'checks.py').write_text(text)
text=(source/'archive.py').read_text().replace('/tmp/ticket24-final-raw','/tmp/ticket24-repair1-final-raw').replace("out/'24-","out/'24-repair1-")
(target/'archive.py').write_text(text)
