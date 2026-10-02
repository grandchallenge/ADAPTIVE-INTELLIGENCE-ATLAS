(* ATLAS-FIG-REP-001 — invariance/equivariance and invertible recoding *)
ClearAll["Global`*"];
g={{-1,0},{0,1}}; x={2,3}; gx=g.x;
left=Graphics[{
  Circle[{0,0},Sqrt[13]],
  Arrow[{{0,0},x}],Arrow[{{0,0},gx}],
  Text[Style["x = (2,3)",12],x+{.45,.2}],
  Text[Style["Gx = (-2,3)",12],gx+{-.65,.2}],
  Text[Style["||x||² = ||Gx||² = 13",13,Bold],{0,-4}],
  Text[Style["equivariant vector / invariant norm",12],{0,-4.5}]
 },Axes->True,PlotRange->{{-5,5},{-5,5}},ImageSize->500,
 PlotLabel->Style["Reflection: invariance and equivariance",15,Bold]];
right=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-3,-.8},{-1,.8}],
  Rectangle[{1,-.8},{3,.8}],
  Arrow[{{-1,0},{1,0}}],
  Text[Style["z = (2,3)",13],{-2,0}],
  Text[Style["Tz = (5,3)",13],{2,0}],
  Text[Style["T",14,Bold],{0,.3}],
  Text[Style["wᵀz = 5",12],{-2,-1.25}],
  Text[Style["(T⁻ᵀw)ᵀ(Tz) = 5",12],{2,-1.25}],
  Text[Style["coordinates change; readout preserved",12,Italic],{0,-1.85}]
 },PlotRange->{{-3.6,3.6},{-2.2,1.4}},ImageSize->500,
 PlotLabel->Style["Invertible recoding",15,Bold]];
GraphicsGrid[{{left,right}},Spacings->{18,5},ImageSize->1100]
