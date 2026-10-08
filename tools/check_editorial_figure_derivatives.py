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
 assert rc2.count(f'figures/derivatives/{prefix}.png')==1
 path=root/'manuscript/parts/02-mathematical-substrate'/f'ATLAS-CH-{ch}-001.md'
 txt=path.read_text()
 assert txt.count(f'../../../figures/derivatives/{prefix}.png')==1
 assert f'../../figures/masters/{fid}.png' not in txt
 marker='Line[{expPoint' if stem=='MANIFOLD' else 'solid rings: eps inner to outer'
 assert marker in source.read_text()
 print('FIGURE_REPAIR_VALID',fid,'PNG',wh,'SHA256',record['generator']['image_sha256'])
assert rc2.count('\\includegraphics')==18
print('FIGURE_REPAIR_PASS 2 candidate Wolfram-native derivatives, 18 plates, original masters unchanged')
