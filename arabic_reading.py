"""Editorial reading marks kept separate from unchanged publisher data."""
import json,re
from pathlib import Path
BASE=Path(__file__).parent
READINGS=dict(x.split('|',1) for x in (BASE/'research/vocalized_readings.txt').read_text().splitlines())
def bare(s):return re.sub(r'[\u064b-\u065f\u0670\u06d6-\u06ed\s\W_]','',s,flags=re.U)
def reading(d):
 s=READINGS.get(d['id'],d['ar'])
 if d['id']=='4811':s=s.replace('عن ابن عباس','عَنِ ابْنِ عَبَّاسٍ').replace(' قال:', ' قَالَ:')
 if d['id']=='3160':s=s.replace('أنَّهُ','أَنَّهُ').replace('لعَطَاءِ','لِعَطَاءِ')
 if d['id']=='3157':s=s.replace('عَن سَهْلِ','عَنْ سَهْلِ')
 if d['id']=='5485':s=s.replace('عَنِ ابنِ','عَنِ ابْنِ').replace('-أَو:', '-أَوْ:')
 for a,b in [('رضي الله عنهما','رَضِيَ اللَّهُ عَنْهُمَا'),('رضيَ اللهُ عنهما','رَضِيَ اللَّهُ عَنْهُمَا'),('رضي الله عنه','رَضِيَ اللَّهُ عَنْهُ'),('رَضيَ اللهُ عنهُ','رَضِيَ اللَّهُ عَنْهُ'),('رَضيَ اللهُ عنه','رَضِيَ اللَّهُ عَنْهُ'),('صلى الله عليه وسلم','صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ')]:s=s.replace(a,b)
 # Complete the divine name's internal reading marks without changing its case ending.
 s=re.sub(r'(?<![\u0621-\u064a\u064b-\u065f])الله([\u064b-\u0652])',r'اللَّه\1',s)
 assert bare(s)==bare(d['ar']),(d['id'],'Arabic letters changed')
 return s
if __name__=='__main__':
 for p in sorted((BASE/'source-data').glob('*-en.json')):
  d=json.loads(p.read_text());s=reading({'id':str(d['id']),'ar':d['hadeeth_ar']})
  missing=[w for w in re.findall('[\u0621-\u064a\u064b-\u0652]+',s) if len(re.sub('[\u064b-\u0652]','',w))>1 and not re.search('[\u064b-\u0652]',w)]
  if missing:print(d['id'],missing)
