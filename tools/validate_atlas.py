#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
ledger=yaml.safe_load((ROOT/'governance/CHAPTER_LEDGER.yaml').read_text(encoding='utf-8'))
figs=yaml.safe_load((ROOT/'governance/FIGURE_REGISTER.yaml').read_text(encoding='utf-8'))
sources=yaml.safe_load((ROOT/'governance/SOURCE_REGISTER.yaml').read_text(encoding='utf-8'))
errors=[]
chapters=ledger.get('chapters',[])
ids=[c.get('id') for c in chapters]
if len(ids)!=len(set(ids)): errors.append('duplicate chapter IDs')
known=set(ids)
for c in chapters:
    for dep in c.get('dependencies') or []:
        if dep not in known: errors.append(f"unresolved dependency {dep} from {c.get('id')}")
fig_ids=[]
classes=set(figs.get('representation_classes') or [])
for f in figs.get('figures',[]):
    fig_ids.append(f.get('id'))
    if f.get('chapter_id') not in known: errors.append(f"figure {f.get('id')} has unknown chapter")
    if f.get('representation_class') not in classes: errors.append(f"figure {f.get('id')} has invalid representation class")
    for req in ('literal_semantics','nonliteral_semantics','support_role','generator'):
        if req not in f: errors.append(f"figure {f.get('id')} missing {req}")
if len(fig_ids)!=len(set(fig_ids)): errors.append('duplicate figure IDs')
src_ids=[s.get('id') for s in sources.get('sources',[])]
if len(src_ids)!=len(set(src_ids)): errors.append('duplicate source IDs')
if not (60 <= len(chapters) <= 80): errors.append(f"chapter count {len(chapters)} outside architecture target")
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(f"OK: {len(chapters)} chapters, {len(fig_ids)} registered figures, {len(src_ids)} sources")
