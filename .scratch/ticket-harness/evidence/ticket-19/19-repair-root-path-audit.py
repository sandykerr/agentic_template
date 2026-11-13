from pathlib import Path
import subprocess,tempfile,json
base=Path(tempfile.mkdtemp(prefix='ticket19-root-path-audit-')); root=base/'repo\rname';root.mkdir()
subprocess.run(['git','init','--quiet',str(root)],check=True)
raw=subprocess.run(['git','-C',str(root),'rev-parse','--show-toplevel'],capture_output=True,check=True)
textual=subprocess.run(['git','-C',str(root),'rev-parse','--show-toplevel'],capture_output=True,text=True,check=True)
result={'root':str(root),'raw_stdout':raw.stdout.decode(),'text_stdout':textual.stdout,'normalization_changed_path':raw.stdout.decode()!=textual.stdout}
(base/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
