#!/usr/bin/env python3
"""Inventory figure identities, dimensions, source and published placement."""
from pathlib import Path
from struct import unpack
import sys
import subprocess, yaml, re, html, hashlib

ROOT=Path(__file__).resolve().parent.parent
reg=yaml.safe_load((ROOT/'governance/FIGURE_REGISTER.yaml').read_text())['figures']
rows=[]
html_text=(ROOT/'releases/v0.1.0/atlas-v0.1.0.html').read_text(encoding='utf-8')
imgtags=re.findall(r'<img\b[^>]+>',html_text)
assert len(imgtags)==18,len(imgtags)
html_alts=[html.unescape(re.search(r'\balt="([^"]*)"',tag).group(1)) if re.search(r'\balt="([^"]*)"',tag) else '' for tag in imgtags]
figs_in_tex=re.findall(r'figures/masters/ATLAS-FIG-[A-Z0-9-]+\.png',(ROOT/'manuscript/latex/atlas-v0.1.0.tex').read_text(encoding='utf-8'))
assert len(figs_in_tex)==18,len(figs_in_tex)
assert len(reg)==18
assert len(list((ROOT/'figures/masters').glob('ATLAS-FIG-*.png')))==18
for n,entry in enumerate(reg):
 fid=entry['id']
 manifest=yaml.safe_load((ROOT/f'figures/manifests/{fid}.yaml').read_text())
 assert manifest['figure_id']==fid
 assert manifest['chapter_id']==entry['chapter_id']
 src=ROOT/manifest['generator']['source']
 dest=ROOT/manifest['generator']['rendered']
 assert src.is_file() and dest.is_file()
 assert manifest['generator']['rendered_bytes']==dest.stat().st_size
 def gitblob(p):
  return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
 assert gitblob(src)==manifest['generator']['source_git_blob_sha1']
 assert gitblob(dest)==manifest['generator']['rendered_git_blob_sha1']
 raw=dest.read_bytes()
 assert raw[:8]==bytes.fromhex('89504e470d0a1a0a')
 w,h=unpack('>II',raw[16:24])
 if h>2*w:flag='P1: EXTREME PORTRAIT; inspect and regenerate'
 elif w>4*h:flag='P2: VERY WIDE; check legibility'
 else:flag='VISUAL_REVIEW'
 assert any(fid+'.png' in x for x in figs_in_tex)
 rows.append(dict(id=fid,chapter=entry['chapter_id'],semantics=entry['representation_class'],dimensions=f'{w}x{h}',flag=flag))
print('CHECKED',len(rows),'matched sources, renders, canonical LaTeX 18 placements, HTML 18 images; alt-present',sum(bool(x.strip()) for x in html_alts))
print('WARNINGS',[(r['id'],r['dimensions'],r['flag']) for r in rows if r['flag']!='VISUAL_REVIEW'])
out=ROOT/'governance/editorial/v0.1.0/FIGURE_RECONCILIATION_LEDGER.md'
intro="""# Editorial figure and plot reconciliation — initial inventory

**Scope:** published v0.1.0 (immutable); editorial work for #314, #321, draft #320.
**Disposition:** MECHANICAL INVENTORY ONLY; NO VISUAL OR SEMANTIC APPROVAL.

Automated checks: 18/18 figure-register entries have a manifest, Wolfram generator,
PNG master, expected source and output git-blob SHA-1, and canonical LaTeX
references. The published HTML contains 18 embedded images with 18 nonempty
caption-derived alt attributes. These checks establish identity and cardinality,
not correct geometry, numbers, axes, legends, vector quality, contrast,
accessibility, or accurate rendering within the PDF.

| Figure | Chapter | Class | Raster px | Triage |
|---|---|---|---:|---|
"""
body=''.join(f"| {r['id']} | {r['chapter']} | {r['semantics']} | {r['dimensions']} | {r['flag']} |\n" for r in rows)
tail="""
## Substantive tasks (agent-executable)

1. Compare the 18 figure masters with Wolfram generators, exact source
   manifests, chapter claims and the compiled PDF. Require an explicit
   correct / revision-required / uninspected judgment for each figure.
2. Reconcile numerical labels, axes, ranges, styles, grayscale distinctions,
   mathematical typography and print legibility. Compare literal and
   nonliteral semantics, and the individual manifest claim boundary.
3. Replace insufficient caption-derived HTML alt text with descriptive
   semantics including trend/structure. Check zoom and links.
4. For ATLAS-FIG-OPTBASE-001 master dimensions are **1160x6759**.
   Contact-sheet inspection shows three panels squeezed into a very long
   predominantly empty canvas: confirmed layout defect. Regenerate from
   the pinned Wolfram source or separately document an exact alternative.
   Validate the three components, revise provenance, replay PDF and HTML.
5. Separately attribute an oversized-float warning outside Part I.
6. Harden 17 source Markdown figure paths after verifying rendered figures.
7. Bind reviews to the corrected exact revision; agents may review and fix.
   A separate checker validates results, but no reviewer thereby gains
   authority to promote research claims or publish a release.

**Next statuses:** all 18 figures NEEDS_VISUAL_SEMANTIC_REVIEW; OPTBASE
also requires P1 layout repair. This is an agent work queue, not an
external-human-review waiting room.
"""
if '--check' in sys.argv:
 assert out.read_text(encoding='utf-8') == intro+body+tail, 'ledger outdated'
else:
 out.write_text(intro+body+tail,encoding='utf-8')
print('LEDGER',out,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
