(* Corrected-edition Wolfram transfer diagram: vertical print layout and typeset symbols; exact finite witnesses unchanged. *)
(* ATLAS-FIG-TRANSFER-001 — exact common-Residual transfer and lossy bottleneck failure *)

left=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-5,1.2},{-2.6,2.4}],
  Rectangle[{-5,-1.0},{-2.6,.2}],
  Rectangle[{-1.2,.1},{1.2,1.3}],
  Rectangle[{2.6,1.2},{5,2.4}],
  Rectangle[{2.6,-1.0},{5,.2}],
  Text[Style[Row[{"source ", Subscript["z","s"], "=(4,2)"}],13,Bold],{-3.8,1.8}],
  Text[Style[Row[{"target ", Subscript["z","t"], "=(6,1/2)"}],13,Bold],{-3.8,-.4}],
  Text[Style["Residual r=(3,1)",14,Bold],{0,.7}],
  Text[Style[Row[{Subscript["D","1"], "=4"}],13,Bold],{3.8,1.8}],
  Text[Style[Row[{Subscript["D","2"], "=5"}],13,Bold],{3.8,-.4}],
  Arrow[{{-2.6,1.8},{-1.2,.95}}],
  Arrow[{{-2.6,-.4},{-1.2,.45}}],
  Arrow[{{1.2,.95},{2.6,1.8}}],
  Arrow[{{1.2,.45},{2.6,-.4}}],
  Text[Style[Subscript["C","s"],13],{-1.9,1.55}],
  Text[Style[Subscript["C","t"],13],{-1.9,-.05}],
  Text[Style[Subscript["D","1"],13],{1.9,1.55}],
  Text[Style[Subscript["D","2"],13],{1.9,-.05}],
  Text[Style["different coordinates, same reconstructive core",11,Italic],{0,-1.55}]
 },
 PlotRange->{{-5.5,5.5},{-2,2.8}},
 ImageSize->560,
 PlotLabel->Style["Common-Residual reconstruction certificate",15,Bold]];

right=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-4.3,1.2},{-2.2,2.3}],
  Rectangle[{-4.3,-.7},{-2.2,.4}],
  Rectangle[{-1,.25},{1,1.35}],
  Rectangle[{2.1,1.2},{4.3,2.3}],
  Rectangle[{2.1,-.7},{4.3,.4}],
  Text[Style[Row[{Subscript["r","A"], "=(1,0)"}],13,Bold],{-3.25,1.75}],
  Text[Style[Row[{Subscript["r","B"], "=(1,1)"}],13,Bold],{-3.25,-.15}],
  Text[Style["P(r)=1",14,Bold],{0,.8}],
  Text[Style[Row[{Subscript["D","2"], "(",Subscript["r","A"],")=2"}],13,Bold],{3.2,1.75}],
  Text[Style[Row[{Subscript["D","2"], "(",Subscript["r","B"],")=1"}],13,Bold],{3.2,-.15}],
  Arrow[{{-2.2,1.75},{-1,.98}}],
  Arrow[{{-2.2,-.15},{-1,.57}}],
  Arrow[{{1,1.0},{2.1,1.75}}],
  Arrow[{{1,.55},{2.1,-.15}}],
  Text[Style["same bottleneck",11,Italic],{0,-1.25}],
  Text[Style["one decoder cannot output both",11,Italic],{3.1,-1.25}]
 },
 PlotRange->{{-4.8,4.8},{-1.7,2.7}},
 ImageSize->520,
 PlotLabel->Style["Lossy bottleneck destroys task sufficiency",15,Bold]];

fig=Graphics[{Inset[left,{350,560},Center,{650,315}],Inset[right,{350,195},Center,{650,315}]},PlotRange->{{0,700},{0,760}},ImageSize->{700,760},ImagePadding->0];
Export["figures/derivatives/ATLAS-FIG-TRANSFER-001-v0.1.1.png",fig,"PNG"];
fig
