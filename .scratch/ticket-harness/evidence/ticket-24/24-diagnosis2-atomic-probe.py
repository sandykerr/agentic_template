import json,pathlib,subprocess,tempfile
results=[]
with tempfile.TemporaryDirectory(prefix='ticket24-atomic-') as tmp:
 p=pathlib.Path(tmp)
 def git(*a):return subprocess.check_output(['git','-C',tmp,*a],text=True).strip()
 git('init','-q');git('config','user.name','Probe');git('config','user.email','probe@example.invalid');(p/'v').write_text('base');git('add','.');git('commit','-qm','base');old=git('rev-parse','HEAD');new=git('commit-tree','HEAD^{tree}','-p','HEAD','-m','next')
 for symbolic in [False,True]:
  git('update-ref','--no-deref','refs/heads/feature',old);git('update-ref','--no-deref','refs/heads/dev',old)
  if symbolic:git('symbolic-ref','refs/heads/dev','refs/heads/feature')
  payload=f'start\noption no-deref\nverify refs/heads/dev {old}\noption no-deref\nupdate refs/heads/feature {new} {old}\nprepare\ncommit\n'
  r=subprocess.run(['git','-C',tmp,'update-ref','--stdin'],input=payload,text=True,capture_output=True)
  results.append(dict(kind='one-shot',symbolic=symbolic,exit=r.returncode,stdout=r.stdout,stderr=r.stderr,dev=git('rev-parse','dev'),new=new))
 for symbolic in [False,True]:
  git('update-ref','--no-deref','refs/heads/feature',old);git('update-ref','--no-deref','refs/heads/dev',old)
  if symbolic:git('symbolic-ref','refs/heads/dev','refs/heads/feature')
  child=subprocess.Popen(['git','-C',tmp,'update-ref','--stdin'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
  child.stdin.write(f'start\noption no-deref\nverify refs/heads/dev {old}\noption no-deref\nupdate refs/heads/feature {new} {old}\nprepare\n');child.stdin.flush()
  start=child.stdout.readline();prepared=child.stdout.readline()
  direct=not bool(git('for-each-ref','--format=%(symref)','refs/heads/dev'))
  attempt=subprocess.run(['git','-C',tmp,'symbolic-ref','refs/heads/dev','refs/heads/feature'],capture_output=True,text=True)
  child.stdin.write('commit\n' if direct else 'abort\n');child.stdin.flush();child.stdin.close();child.stdin=None;stdout,stderr=child.communicate(timeout=5)
  results.append(dict(kind='prepared-guard',symbolic=symbolic,start=start,prepared=prepared,direct=direct,concurrent_alias_exit=attempt.returncode,concurrent_alias_stderr=attempt.stderr,child_exit=child.returncode,stdout=stdout,stderr=stderr,dev=git('rev-parse','dev'),feature=git('rev-parse','feature'),old=old,new=new))
pathlib.Path('/tmp/ticket24-atomic-probe.json').write_text(json.dumps(results,indent=2)+'\n')
for x in results:print({k:x[k] for k in x if k in ['kind','symbolic','exit','direct','concurrent_alias_exit','child_exit','dev','feature','old','new']})
