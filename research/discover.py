import subprocess,concurrent.futures,json,pathlib
root=pathlib.Path(__file__).parent
def get(c):
 p=root/f'category-{c}.json'
 if not p.exists():subprocess.run(['curl','-fsSL','--max-time','35',f'https://hadeethenc.com/api/v1/hadeeths/list/?language=en&category_id={c}&page=1&per_page=300','-o',str(p)],check=True)
 x=json.loads(p.read_text());return c,x['data']
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for c,ds in ex.map(get,[314,282,313,280]):
  print('\nCATEGORY',c,flush=True)
  for d in ds:print(d['id'],d['title'][:160],flush=True)
