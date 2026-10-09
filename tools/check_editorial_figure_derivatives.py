from pathlib import Path
import hashlib,struct,subprocess,yaml
root=Path(__file__).resolve().parents[1]
rc2=(root/'manuscript/latex/atlas-v0.1.1-rc.2.tex').read_text()
ids={'MANIFOLD':'GEOM','PSPECTRUM':'NONNORMAL'}
for stem,ch in ids.items():
 fid=f'ATLAS-FIG-{stem}-001'
 prefix=f'{fid}-v0.1.1'
 derivative=root/'figures/derivatives'
 record=yaml.safe_load((derivative/(prefix+'.yaml')).read_text())
 source=derivative/(prefix+'.wl')
 png=derivative/(prefix+'.png')
 old=yaml.safe_load((root/'figures/manifests'/(fid+'.yaml')).read_text())
 assert record['source_figure_id']==fid
 assert record['parameters']==old['parameters']
 assert record['mathematics']==old['mathematics']
 assert record['claim_boundary']==old['claim_boundary']
 assert subprocess.check_output(['git','hash-object',str(root/old['generator']['source'])],text=True).strip()==old['generator']['source_git_blob_sha1']
 assert subprocess.check_output(['git','hash-object',str(root/old['generator']['rendered'])],text=True).strip()==old['generator']['rendered_git_blob_sha1']
 assert record['original_wolfram_provenance']['original_render_git_blob_sha1']==old['generator']['rendered_git_blob_sha1']
 assert record['original_wolfram_provenance']['source_git_blob_sha1']==old['generator']['source_git_blob_sha1']
 assert subprocess.check_output(['git','hash-object',str(source)],text=True).strip()==record['generator']['source_git_blob_sha1']
 data=png.read_bytes()
 assert hashlib.sha256(data).hexdigest()==record['generator']['image_sha256']
 assert data[:8]==bytes.fromhex('89504e470d0a1a0a')
 wh=list(struct.unpack('>II',data[16:24]))
 assert wh==record['generator']['render_pixels'],(fid,wh)
 path=root/'manuscript/parts/02-mathematical-substrate'/f'ATLAS-CH-{ch}-001.md'
 txt=path.read_text()
 if stem=='MANIFOLD':
  assert rc2.count(f'figures/derivatives/{prefix}.png')==0, "old MANIFOLD image still active"
  assert txt.count(f'../../../figures/derivatives/{prefix}.png')==0
 else:
  assert rc2.count(f'figures/derivatives/{prefix}.png')==1
  assert txt.count(f'../../../figures/derivatives/{prefix}.png')==1
 assert f'../../figures/masters/{fid}.png' not in txt
 marker='Line[{expPoint' if stem=='MANIFOLD' else 'solid rings: eps inner to outer'
 assert marker in source.read_text()
 print('FIGURE_REPAIR_VALID',fid,'PNG',wh,'SHA256',record['generator']['image_sha256'])
assert rc2.count('\\includegraphics')==18

# OPTBASE: candidate Wolfram 15.0.1, separately versioned after the Matplotlib alternative.
fid='ATLAS-FIG-OPTBASE-001'
prefix=f'{fid}-v0.1.2'
deriv=root/'figures/derivatives'
record=yaml.safe_load((deriv/(prefix+'.yaml')).read_text())
old=yaml.safe_load((root/'figures/manifests'/(fid+'.yaml')).read_text())
wl=deriv/(prefix+'.wl')
png=deriv/(prefix+'.png')
prev=deriv/(fid+'-v0.1.1.yaml')
assert record['source_figure_id']==fid
assert record['parameters']==old['parameters']
assert record['literal_semantics']==old['literal_semantics']
assert record['claim_boundary']==old['claim_boundary']
assert record['original_wolfram_provenance']['source_git_blob_sha1']==old['generator']['source_git_blob_sha1']
assert record['original_wolfram_provenance']['original_render_git_blob_sha1']==old['generator']['rendered_git_blob_sha1']
assert record['predecessor_editorial_derivative']['image_sha256']==yaml.safe_load(prev.read_text())['generator']['image_sha256']
assert subprocess.check_output(['git','hash-object',str(root/old['generator']['source'])],text=True).strip()==old['generator']['source_git_blob_sha1']
assert subprocess.check_output(['git','hash-object',str(root/old['generator']['rendered'])],text=True).strip()==old['generator']['rendered_git_blob_sha1']
assert subprocess.check_output(['git','hash-object',str(wl)],text=True).strip()==record['generator']['source_git_blob_sha1']
assert hashlib.sha256(png.read_bytes()).hexdigest()==record['generator']['image_sha256']
data=png.read_bytes()
assert data[:8]==bytes.fromhex('89504e470d0a1a0a')
wh=list(struct.unpack('>II',data[16:24]))
assert wh==record['generator']['render_pixels']==[700,990]
txt=wl.read_text()
assert '183/100-181/100==1/50' in txt
assert 'gc=={6/5,8/5}' in txt
assert 'Norm[g]==5 && Norm[gc]==2' in txt
assert 'Abs[1-a]' in txt and '0 < a < 2: contractive' in txt
assert 'Inset[gd' in txt and 'Inset[decay' in txt
assert rc2.count('figures/derivatives/'+prefix+'.png')==0, 'preserve predecessor v0.1.2 but do not typeset it'
ch=(root/'manuscript/parts/05-optimization/ATLAS-CH-OPTBASE-001.md').read_text()
assert ch.count('../../../figures/derivatives/'+prefix+'.png')==0
assert rc2.count('\\includegraphics')==18
print('FIGURE_REPAIR_VALID',fid,'PNG',wh,'SHA256',record['generator']['image_sha256'])
print('FIGURE_REPAIR_PASS 3 candidate Wolfram-native derivatives, 18 plates, original masters unchanged')

# TRANSFER: candidate print-legible vertical Wolfram-native schematic.
fid='ATLAS-FIG-TRANSFER-001'
prefix=f'{fid}-v0.1.1'
deriv=root/'figures/derivatives'
record=yaml.safe_load((deriv/(prefix+'.yaml')).read_text())
old=yaml.safe_load((root/'figures/manifests'/(fid+'.yaml')).read_text())
wl=deriv/(prefix+'.wl')
png=deriv/(prefix+'.png')
assert record['source_figure_id']==fid
assert record['parameters']==old['parameters']
assert record['literal_semantics']==old['literal_semantics']
assert record['claim_boundary']==old['claim_boundary']
assert record['original_wolfram_provenance']['source_git_blob_sha1']==old['generator']['source_git_blob_sha1']
assert record['original_wolfram_provenance']['original_render_git_blob_sha1']==old['generator']['rendered_git_blob_sha1']
assert subprocess.check_output(['git','hash-object',str(root/old['generator']['source'])],text=True).strip()==old['generator']['source_git_blob_sha1']
assert subprocess.check_output(['git','hash-object',str(root/old['generator']['rendered'])],text=True).strip()==old['generator']['rendered_git_blob_sha1']
assert subprocess.check_output(['git','hash-object',str(wl)],text=True).strip()==record['generator']['source_git_blob_sha1']
data=png.read_bytes()
assert hashlib.sha256(data).hexdigest()==record['generator']['image_sha256']
assert data[:8]==bytes.fromhex('89504e470d0a1a0a')
wh=list(struct.unpack('>II',data[16:24]))
assert wh==record['generator']['render_pixels']==[700,760]
txt=wl.read_text()
assert 'Inset[left' in txt and 'Inset[right' in txt
assert 'Subscript["z","s"]' in txt and 'Subscript["z","t"]' in txt
for item in ['(4,2)','(6,1/2)','r=(3,1)','D','P(r)=1','(1,0)','(1,1)']:
 assert item in txt,item
assert rc2.count('figures/derivatives/'+prefix+'.png')==0, 'keep v0.1.1 predecessor but use v0.1.2'
chapter=(root/'manuscript/parts/03-representation-learning/ATLAS-CH-TRANSFER-001.md').read_text()
assert chapter.count('../../../figures/derivatives/'+prefix+'.png')==0
assert rc2.count(r'\includegraphics')==18
print('FIGURE_REPAIR_VALID',fid,'PNG',wh,'SHA256',record['generator']['image_sha256'])
print('FIGURE_REPAIR_PASS 4 candidate Wolfram-native derivatives, 18 plates, original masters unchanged')

# All previous exact Wolfram masters and source-hashed v0.1.1 / v0.1.2
# derivatives remain intact. The corrected publication candidate uses
# later separately source-locked Wolfram 15.0.1 native derivative versions.
successors=[
 ('MANIFOLD','v0.1.2','manuscript/parts/02-mathematical-substrate/ATLAS-CH-GEOM-001.md'),
 ('TRANSFER','v0.1.2','manuscript/parts/03-representation-learning/ATLAS-CH-TRANSFER-001.md'),
 ('OPTBASE','v0.1.3','manuscript/parts/05-optimization/ATLAS-CH-OPTBASE-001.md')]
for stem,version,chapter_path in successors:
 fid=f'ATLAS-FIG-{stem}-001'
 m=yaml.safe_load((root/'figures/manifests'/f'{fid}-{version}.yaml').read_text())
 old=yaml.safe_load((root/'figures/manifests'/f'{fid}.yaml').read_text())
 src=root/m['successor_source']
 png=root/m['rendered_derivative']
 assert m['original_source_git_blob_sha1']==old['generator']['source_git_blob_sha1']
 assert subprocess.check_output(['git','hash-object',str(root/m['original_source'])],text=True).strip()==m['original_source_git_blob_sha1']
 assert subprocess.check_output(['git','hash-object',str(src)],text=True).strip()==m['successor_source_git_blob_sha1']
 assert subprocess.check_output(['git','hash-object',str(png)],text=True).strip()==m['rendered_derivative_git_blob_sha1']
 b=png.read_bytes()
 assert b[:8]==bytes.fromhex('89504e470d0a1a0a')
 assert len(b)==m['rendered_derivative_bytes']
 assert hashlib.sha256(b).hexdigest()==m['rendered_derivative_raw_sha256']
 wh=list(struct.unpack('>II',b[16:24]))
 assert wh==m['rendered_derivative_dimensions_px']
 assert rc2.count('figures/derivatives/'+fid+'-'+version+'.png')==1
 assert (root/chapter_path).read_text().count('../../../figures/derivatives/'+fid+'-'+version+'.png')==1
 print('NATIVE_PRINT_SUCCESSOR_PASS',fid,version,wh,m['rendered_derivative_raw_sha256'])
assert rc2.count(r'\includegraphics')==18
print('FIGURE_REPAIR_PASS: old masters locked; 18 placements; three source-native print successors; no predecessor alias overwrite')
