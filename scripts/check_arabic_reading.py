"""Check Arabic reading surfaces and preserve the underlying publisher wording."""
from pathlib import Path
from html.parser import HTMLParser
import sys,json,re,html
base=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(base))
from arabic_reading import reading,bare
root=Path(sys.argv[1]) if len(sys.argv)>1 else base/'dist'
class Arabic(HTMLParser):
 def __init__(self):super().__init__();self.stack=[];self.blocks=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag not in ['meta','link','input','br','hr','img','path']:self.stack.append((tag,a.get('lang',self.stack[-1][1] if self.stack else '')))
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,s):
  if self.stack and self.stack[-1][1]=='ar':self.blocks.append(s)
count=0
for page in root.rglob('*.html'):
 p=Arabic();p.feed(page.read_text())
 for s in p.blocks:
  for w in re.findall('[\u0621-\u064a\u064b-\u0652]+',s):
   if len(re.sub('[\u064b-\u0652]','',w))>1:assert re.search('[\u064b-\u0652]',w),(page.name,w)
  count+=1
for d in json.loads((root/'content.json').read_text()):
 s=reading(d);assert bare(s)==bare(d['ar'])
 assert html.escape(s,quote=True) in (root/'hadith'/f'{d["slug"]}.html').read_text()
print('PASS:',count,'Arabic text blocks contain reading marks; all 40 narration letter sequences match source.')
