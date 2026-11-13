"""Observe installed Git no-deref and expected-old semantics in isolated refs."""
import json,subprocess,tempfile
from pathlib import Path
out=Path('.scratch/ticket-harness/evidence');commands=[]
with tempfile.TemporaryDirectory(prefix='ticket24-repair1-git-') as directory:
 repo=Path(directory)
 def git(*args,stdin=None,ok=True):
  command=['git','-C',str(repo),*args]
  result=subprocess.run(command,input=stdin,text=True,capture_output=True)
  commands.append(dict(command=command,stdin=stdin,exit=result.returncode,stdout=result.stdout,stderr=result.stderr))
  if ok:assert result.returncode==0,commands[-1]
  return result
 git('init','-q','-b','main')
 git('-c','user.name=Probe','-c','user.email=probe@example.invalid','commit','--allow-empty','-qm','Baseline')
 old=git('rev-parse','HEAD').stdout.strip()
 new=git('-c','user.name=Probe','-c','user.email=probe@example.invalid','commit-tree','HEAD^{tree}','-p','HEAD','-m','Candidate').stdout.strip()
 git('branch','dev',old);git('branch','feature',old)
 git('symbolic-ref','refs/heads/feature','refs/heads/dev')
 git('update-ref','--no-deref','refs/heads/feature',new,old)
 assert git('rev-parse','refs/heads/dev').stdout.strip()==old
 assert git('rev-parse','refs/heads/feature').stdout.strip()==new
 assert git('symbolic-ref','-q','refs/heads/feature',ok=False).returncode==1
 stale=git('update-ref','--no-deref','refs/heads/feature',old,old,ok=False)
 assert stale.returncode!=0 and git('rev-parse','refs/heads/feature').stdout.strip()==new
 git('symbolic-ref','refs/heads/feature','refs/heads/dev')
 transaction='start\noption no-deref\nupdate refs/heads/feature '+new+' '+old+'\noption no-deref\nupdate refs/heads/dev '+new+' '+old+'\nprepare\ncommit\n'
 git('update-ref','--stdin',stdin=transaction)
 assert git('rev-parse','refs/heads/dev').stdout.strip()==new
 assert git('rev-parse','refs/heads/feature').stdout.strip()==new
 assert git('symbolic-ref','-q','refs/heads/feature',ok=False).returncode==1
(out/'24-repair1-git-probe.json').write_text(json.dumps(dict(commands=commands,observations=dict(no_deref_feature_update_did_not_advance_development_referent=True,matching_symbol_itself_replaced=True,stale_expected_old_rejected=True,two_update_no_deref_transaction_operates_on_named_refs=True),scope='Installed Git primitives only, not private production seam; no atomic direct-ref type locking guarantee'),indent=2)+'\n')
