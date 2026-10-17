import pathlib,subprocess,json,concurrent.futures,shutil
root=pathlib.Path(__file__).resolve().parent.parent;out=root/'source-data';out.mkdir(exist_ok=True)
ids='65038 5979 65039 65037 8869 8317 5954 6331 5493 4811 4721 5737 3407 4928 8318 3599 3598 6040 5488 5482 5878 3596 3779 3636 3298 3290 4204 3160 3701 4967 3743 4246 11203 3157 4557 3852 5545 5485 3142 4801'.split()
(root/'research/selected-ids.json').write_text(json.dumps(ids))
def get(t):
 id,l=t;p=out/f'{id}-{l}.json'
 for r in [pathlib.Path('/workspace/sites')/n/'source-data' for n in ['hadith-revelation','hadith-faith','hadith-tawhid']]+[pathlib.Path('/workspace/scratch/b7333478de38/hadith-research/raw')]:
  if (r/p.name).exists():shutil.copy2(r/p.name,p);break
 if not p.exists():
  for i in range(3):
   r=subprocess.run(['curl','-fsSL','--max-time','35',f'https://hadeethenc.com/api/v1/hadeeths/one/?language={l}&id={id}','-o',str(p)],capture_output=True)
   if not r.returncode:break
  if r.returncode:return id,l,'ERROR'
 try:
  d=json.loads(p.read_text());return id,l,d.get('grade'),d.get('attribution')
 except:return id,l,'BAD JSON'
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for a in ex.map(get,[(i,l) for i in ids for l in ['en','ur']]):print(*a,flush=True)
