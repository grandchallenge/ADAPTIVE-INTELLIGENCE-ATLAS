#!/usr/bin/env python3
"""Compose Wolfram-native vector panels into a print-width 2+1 figure.

The two stability discs occupy a side-by-side row at ~2.3 inches each;
the error-scaling panel spans the entire ~4.8-inch printed text width.
This avoids a vertically stacked image exceeding the physical page height.
"""
import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
DER=ROOT/'figures/derivatives'
P='ATLAS-FIG-NUMERICS-001-v0.1.1'
OUT=DER/(P+'.png')

def build(target):
    with tempfile.TemporaryDirectory(prefix='atlas-num459-') as tmp:
        panels=[]
        for i in (1,2,3):
            dest=Path(tmp)/f'{i}.png'
            subprocess.run(['gs','-q','-dNOPAUSE','-dBATCH','-sDEVICE=png16m','-r240',f'-sOutputFile={dest}',str(DER/f'{P}-panel-{i}.pdf')],check=True)
            panels.append(Image.open(dest).convert('RGB'))
        width=1200; gap=18
        half=(width-gap)//2
        upper=[]
        for panel in panels[:2]:
            height=round(panel.height*half/panel.width)
            upper.append(panel.resize((half,height),Image.Resampling.LANCZOS))
        bottom=panels[2].resize((width,round(panels[2].height*width/panels[2].width)),Image.Resampling.LANCZOS)
        top_height=max(p.height for p in upper)
        canvas=Image.new('RGB',(width,top_height+gap+bottom.height),'white')
        canvas.paste(upper[0],(0,(top_height-upper[0].height)//2))
        canvas.paste(upper[1],(half+gap,(top_height-upper[1].height)//2))
        canvas.paste(bottom,(0,top_height+gap))
        target.parent.mkdir(parents=True,exist_ok=True)
        canvas.save(target,optimize=True,dpi=(250,250))
        return canvas.size

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            t=Path(tmp)/OUT.name;size=build(t)
            assert t.read_bytes()==OUT.read_bytes(),'stale NUMERICS figure'
    else:size=build(OUT)
    print('NUMERICS_PRINT_459_PASS',size,hashlib.sha256(OUT.read_bytes()).hexdigest())
if __name__=='__main__':main()
