from pathlib import Path
import hashlib, json, os, subprocess, tempfile
rows=[]
with tempfile.TemporaryDirectory(prefix='review19-readonly-') as tmp:
    path=Path(tmp)
    def git(*args): return subprocess.run(['git','-C',str(path),*args],capture_output=True,check=True)
    git('init','--quiet','--initial-branch=main')
    f=path/'tracked';f.write_text('same\n');git('add','tracked');git('-c','user.name=Corpus observation','-c','user.email=corpus@example.invalid','commit','--quiet','-m','initial')
    index=path/'.git/index'
    for flags in [[],['--no-optional-locks']]:
        stat=f.stat();os.utime(f,ns=(stat.st_atime_ns,stat.st_mtime_ns+1000000000))
        before=index.read_bytes()
        out=git(*flags,'status','--porcelain','--untracked-files=all')
        rows.append({'global_flags':flags,'stdout':out.stdout.decode(),'index_changed':before!=index.read_bytes(),'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(index.read_bytes()).hexdigest()})
Path('/tmp/repair19-c5-readonly-observation.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
