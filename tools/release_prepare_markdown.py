from pathlib import Path

raw=Path("/tmp/atlas-rc.md").read_text(encoding="utf-8")
marker="<!-- ATLAS_CHAPTER 01 "
raw=raw[raw.index(marker):]
raw=raw.replace("](../../figures/", "](figures/")
raw=raw.replace("# From Readability to Functional Evidence", "# Interlude: From Readability to Functional Evidence", 1)
raw=raw.replace("\nAlongrightarrow B.\n", "\nA \\longrightarrow B.\n")
raw=raw.replace("\nAleftrightarrow B.\n", "\nA \\leftrightarrow B.\n")
raw=raw.replace(r"\nRightarrow", r"\not\Rightarrow")
meta="---\ntitle: A Mathematical Atlas of Adaptive Intelligence\nauthor: Grand Challenge Labs\ndate: 2026-10-07\nversion: 0.1.0-rc.1\n---\n\n"
lines=(meta+raw).splitlines()

# Normalize paired legacy standalone [ ... ] TeX displays.
stack=None; bracket_pairs=[]
for i,line in enumerate(lines):
    t=line.strip()
    if t=="[" and stack is None:
        stack=i
    elif t=="]" and stack is not None:
        bracket_pairs.append((stack,i)); stack=None
for a,b in bracket_pairs:
    lines[a]="```{=latex}\n\\["; lines[b]="\\]\n```"

# Exact false-Setext headings observed under Pandoc 3.9.
false_by_chapter={
 "Depth as Computational Time": ["x_L","tau","x_{k+1}","x_{k+1}-2","x_k","|x_k-2|","tau(epsilon)","C(x_0)","C_vec","x_{k+1}","A(x_0)","C_block(x_0)"],
 "Reinforcement Learning and Control": ["G_t","V^pi(s)","Q^pi(s,a)","V^pi(s)","V^pi(s1)","V^pi(s0)","0 + (1/2)4","Q^pi(s0,b)","2 + (1/2)V^pi(s0)","V(s0)","2 + (1/2)V(s0)","(TV)(s)","b_t(s)"],
 "Evidence Exchange and Zero-Context Work": ["Contract_A(D,H1)"],
}
h1=[i for i,x in enumerate(lines) if x.startswith("# ")]
fixed=0
wrapped_ranges=[]
for pos,start in enumerate(h1):
    title=lines[start][2:]
    wanted=list(false_by_chapter.get(title,[]))
    if not wanted:
        continue
    end=h1[pos+1] if pos+1<len(h1) else len(lines)
    cursor=start+1
    eq_hits=[]
    for target in wanted:
        found=None
        for i in range(cursor+1,end):
            if lines[i].strip()=="=" and lines[i-1].strip()==target:
                found=i
                break
        if found is None:
            raise SystemExit(f"could not neutralize {title}: {target}")
        eq_hits.append(found)
        fixed+=1
        cursor=found+1
    ranges=set()
    for eq in eq_hits:
        a=eq-1
        while a>start+1 and lines[a-1].strip()!="":
            a-=1
        b=eq+1
        while b<end and lines[b].strip()!="":
            b+=1
        ranges.add((a,b))
    for a,b in sorted(ranges, reverse=True):
        lines[a]="```text\n"+lines[a]
        lines[b-1]=lines[b-1]+"\n```"
        wrapped_ranges.append((title,a,b))

out="\n".join(lines)+"\n"
Path("/tmp/atlas-rc-release-clean.md").write_text(out,encoding="utf-8")
print("legacy_display_pairs",len(bracket_pairs),"false_setext_fixed",fixed,"explicit_h1",sum(1 for x in lines if x.startswith("# ")))