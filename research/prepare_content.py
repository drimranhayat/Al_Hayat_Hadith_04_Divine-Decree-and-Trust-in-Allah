from pathlib import Path
import json,re,shutil
b=Path(__file__).resolve().parent.parent
ids=json.loads((b/'research/selected-ids.json').read_text())
t=[x.split('|') for x in (b/'research/editorial_titles.txt').read_text().splitlines()];assert len(t)==45
(b/'card_titles.py').write_text('"""Fully vocalized editorial headings, separate from narration text."""\nSECTIONS='+repr([(a,u) for e,a,u in t[:5]])+'\nTITLES='+repr([(a,u) for e,a,u in t[5:]])+'\n')
subtitles=['Knowledge, writing, divine will and human responsibility','Use lawful means while relying upon Allah','Prayer for guidance, protection and a sound heart','Faithful responses to pain, bereavement and delay','Sincere purpose, contentment and helping others']
secs=[{'title':e,'subtitle':subtitles[i],'icon':['spark','book','heart','shield','leaf'][i]} for i,(e,a,u) in enumerate(t[:5])]
routes='muslim:2653b abudawud:4700 muslim:2655 bukhari:7454 muslim:2647a muslim:2652a abudawud:4699 muslim:2654 muslim:2664 tirmidhi:2516 tirmidhi:2344 bukhari:5728 bukhari:5707 bukhari:6133 bukhari:2291 bukhari:1429 muslim:2717 bukhari:6347 muslim:2739 muslim:2720 muslim:2722 muslim:2721 muslim:2877 muslim:2675 muslim:2999 bukhari:1284 bukhari:5645 muslim:2576 bukhari:5641 bukhari:1469 bukhari:3150 bukhari:3612 ahmad:17217 muslim:1909 muslim:1911 bukhari:6446 muslim:2965 abudawud:5074 tirmidhi:2140 muslim:2699'.split();assert len(routes)==40
names={'muslim':'Sahih Muslim','bukhari':'Sahih al-Bukhari','abudawud':'Sunan Abi Dawud','tirmidhi':'Jami at-Tirmidhi','ahmad':'Musnad Ahmad'}
entries=[]
for i,(id,route) in enumerate(zip(ids,routes)):
 d=json.loads((b/f'source-data/{id}-en.json').read_text());ur=json.loads((b/f'source-data/{id}-ur.json').read_text());assert d['id']==ur['id'];assert 'authentic' in d['grade'].lower()
 narrator=d['hadeeth'].split(' reported')[0].split('(may Allah')[0].strip();narrator={'5954':'Ubayy ibn Kab, Abdullah ibn Masud, Hudhayfah ibn al-Yaman and Zayd ibn Thabit, through Ibn al-Daylami','65039':'Abdullah ibn Umar, through Tawus','4557':'Jabir ibn Abdullah and Anas ibn Malik'}.get(id,narrator)
 coll,num=route.split(':');entries.append((id,t[i+5][0],names[coll]+' '+num,route,narrator))
(b/'topic_config.py').write_text('SECTIONS='+repr(secs)+'\nENTRIES='+repr(entries)+'''\nids=[x[0] for x in ENTRIES];titles=[x[1] for x in ENTRIES];refs={x[0]:(x[2],x[3]) for x in ENTRIES};NARRATORS=[x[4] for x in ENTRIES]\nassert len(ids)==len(set(ids))==40\n''')
# Keep the publisher metadata exactly; add evidence for reference routes separately.
pr=json.loads((b/'research/references.json').read_text());pr['3701']={'url':'https://hadeethenc.com/en/browse/hadith/3701','properties':{'Hadith source':'[Sahih al-Bukhari - 5641]'}};pr.pop('65772',None)
(b/'reference-provenance.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2))
notes=[x.split('|') for x in (b/'research/study_notes.txt').read_text().splitlines()];assert [x[0] for x in notes]==ids
bank=[]
for z in notes:
 assert len(z)==12,(z[0],len(z))
 id,q,a,proof,q2,a2,proof2,m,correct,w1,w2,w3=z
 def item(q,a,p):
  kind,anchor=p.split(':',1);return {'q':q,'a':a,'basis':kind,'anchor':anchor}
 one=item(q,a,proof);two=item(q2,a2,proof2)
 # The answer-choice explanation addresses the question itself and cites both notes.
 mc=item(m,correct,proof if id not in ['5979','6331','5737','8318','6040','5878','3596','3779','3636','4967','3743','5545','4801'] else proof2)
 mc.update(wrong=[w1,w2,w3],why=a+' '+a2,hint='Read the narration and its explanation, then compare the distinction in each option.')
 bank.append({'qa':[one,two],'mcq':[mc]})
for line in (b/'research/additional_practice.txt').read_text().splitlines():
 id,q,a,w1,w2,w3,p=line.split('|');kind,anchor=p.split(':',1)
 d=json.loads((b/f'source-data/{id}-en.json').read_text());text=d['hadeeth'] if kind=='T' else d['explanation']
 import unicodedata
 norm=lambda v: ''.join(c for c in unicodedata.normalize('NFKD',v.casefold()) if not unicodedata.combining(c))
 assert norm(anchor) in norm(text),(id,anchor)
 bank[ids.index(id)]['mcq'].append({'q':q,'a':a,'wrong':[w1,w2,w3],'basis':kind,'anchor':anchor,'why':a+'. Compare the cited source passage and the explanation above.','hint':'Identify the condition or distinction stated in the linked report.'})
(b/'learning_content.py').write_text('"""Original editorial questions; each cites a checked publisher passage."""\nBANK='+repr(bank)+'\n')
print('Prepared 40 records, 80 Q&A and',sum(len(x['mcq']) for x in bank),'MCQs.')
