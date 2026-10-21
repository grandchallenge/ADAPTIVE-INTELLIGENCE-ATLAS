#!/usr/bin/env python3
"""Bounded source-lock, PDF and HTML evidence; never infers chapter approval."""
import hashlib,json,re,subprocess
from pathlib import Path
import yaml,pymupdf
from bs4 import BeautifulSoup
R=Path.cwd()
HEAD="9b7206c4a59583e3099abbcda310ebaa962aad0e"
BOOK="/home/jim/GCL/ATLAS-405-WORK-20261021/combined-render/atlas-v0.1.1-rc.2."
PAGES={'THESIS':(69,77),'MAP':(79,84),'OBJECTS':(85,95),'EVIDENCE':(97,109)}
ANCHORS={'THESIS':'the-adaptive-system-thesis','MAP':'how-to-read-a-mathematical-atlas','OBJECTS':'states-operators-flows-and-interfaces','EVIDENCE':'claims-evidence-and-computational-witnesses'}
FINDINGS={
 'THESIS':[{'id':'ER-P1-01','severity':'P1','location':'§8','status':'UNRESOLVED','finding':'Keystone drafting history remains reader-facing prose.'},{'id':'ER-P1-02','severity':'P2','location':'§3,7,9','status':'PARTIAL','finding':'Repeated editorial-shift guidance; compress.'}],
 'MAP':[],
 'OBJECTS':[{'id':'ER-P1-06','severity':'P1','location':'§3–19','status':'UNRESOLVED','finding':'19 sections fragment four role definitions and examples.'},{'id':'ER-P1-07','severity':'P2','location':'§6,8','status':'RESOLVED','finding':'Global flow/semiflow/local-flow domains now differentiated.'}],
 'EVIDENCE':[]}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],text=True).strip()
def verify_exact_examples():
 from fractions import Fraction as F
 # MAP/EVIDENCE: stable-spectrum upper-triangular counterexample.
 A=((F(4,5),F(4)),(F(0),F(4,5)))
 assert A[0][0]==A[1][1] and A[1][0]==0
 ae2=(A[0][1],A[1][1])
 assert ae2==(F(4),F(4,5)) and sum(v*v for v in ae2)==F(416,25)>1
 # EVIDENCE: 21 finite cases and separately valid universal parity proof.
 assert list(range(-10,11))==[n for n in range(-10,11) if n*(n-1)%2==0]
 assert all((n%2==0) or ((n-1)%2==0) for n in range(-200,201))
 # OBJECTS: normalized state forfeits amplitude; zero is excluded.
 assert F(3)**2+F(4)**2==25 and (F(3,5)**2+F(4,5)**2)==1
 return {'map_exact_norm_squared':'416/25','parity_finite_cases':21,'objects_norm_input':5,'objects_norm_output':1}
def main():
 if git('rev-parse','HEAD')!=HEAD:raise ValueError('candidate HEAD changed')
 reg=json.loads((R/'governance/CHAPTER_LEDGER.yaml').read_text())
 pdf_path=Path(BOOK+'pdf');html_path=Path(BOOK+'html')
 pdf=pymupdf.open(pdf_path);html=BeautifulSoup(html_path.read_text(),'html.parser')
 titles={e.get('id'):e for e in html.find_all('h1') if e.get('id')}
 rows=[]
 for tag,(start,end) in PAGES.items():
  cid=f'ATLAS-CH-{tag}-001'
  item=next(x for x in reg['chapters'] if x['id']==cid)
  path=R/item['manuscript_path'];source=path.read_text()
  lockpath=R/f'sources/source-locks/{cid}.yaml';lock=yaml.safe_load(lockpath.read_text())
  locks=[]
  for item2 in lock.get('sources',lock.get('atlas_sources',[])):
   raw=git('ls-tree',item2['commit'],'--',item2['path'])
   blob=raw.split()[2] if raw else None
   locks.append({'source_id':item2['id'],'blob':blob,'matches_lock':blob==item2['git_blob_sha1']})
  if not all(x['matches_lock'] for x in locks):raise ValueError(cid+' source-lock mismatch')
  pages=[]
  for n in range(start,end+1):
   pg=pdf[n-1];blocks=pg.get_text('dict')['blocks'];txt=pg.get_text()
   spans=[s for b in blocks if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
   edge=sum(s['bbox'][0]<18 or s['bbox'][2]>pg.rect.width-18 or s['bbox'][1]<18 or s['bbox'][3]>pg.rect.height-18 for s in spans)
   if len(txt)<250 or edge:raise ValueError(f'{cid} PDF page {n} defect')
   pages.append({'physical_page':n,'text_chars':len(txt),'spans':len(spans),'near_edge':edge})
  h=titles[ANCHORS[tag]];html_sections=[]
  for node in h.next_elements:
   if getattr(node,'name',None)=='h1':break
   if getattr(node,'name',None)=='h2':html_sections.append(node.get('id'))
  source_headings=re.findall(r'(?m)^## (?!#)',source)
  if len(html_sections)!=len(source_headings):raise ValueError(cid+' HTML outline differs')
  state='REPAIR_REQUIRED' if tag in ('THESIS','OBJECTS') else 'CRITIC_PENDING'
  rows.append({'chapter_id':cid,'source_path':item['manuscript_path'],'source_blob_sha1':git('hash-object',str(path)),
    'source_lock':str(lockpath.relative_to(R)),'source_lock_sha256':sha(lockpath),
    'historical_source_lock_checks':locks,'pdf_pages':[start,end],'pdf_page_checks':pages,
    'html_heading_id':ANCHORS[tag],'source_h2':len(source_headings),'html_h2':len(html_sections),
    'producer_issue':412,'producer_run_id':'a0412e5cf0f04b2fb2c3d0e91a814e75',
    'producer_status':state,'critically_accepted':False,'findings':FINDINGS[tag]})
 out={'type':'ATLAS_P01_PRODUCER/1','source_head':HEAD,'pdf_sha256':sha(pdf_path),'html_sha256':sha(html_path),
 'pdf_page_count':len(pdf),'rows':rows,'final_accept_count':0,'role':'PRODUCER','example_witnesses':verify_exact_examples()}
 target=R/'governance/editorial/v0.1.1/P01_PRODUCER_001.json'
 target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('PART_I',[(x['chapter_id'],x['producer_status'],x['pdf_pages']) for x in rows])
if __name__=='__main__':main()
