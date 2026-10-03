(* ATLAS-FIG-RESIDUAL-001 — nuisance orbits and reconstruction after recoding *)

left=Graphics[{
  Directive[GrayLevel[.65],Dashed,Thick],
  Line[{{-2,-3},{-2,6}}],
  Line[{{0,-3},{0,6}}],
  Line[{{2,-3},{2,6}}],
  Directive[Black,Thick],
  Arrow[{{2,5},{2,2}}],
  PointSize[.02],
  Point[{{2,5},{2,2}}],
  Text[Style["x=(2,5)",11,Bold],{2.55,5}],
  Text[Style["g_-3(x)=(2,2)",11,Bold],{2.7,2}],
  Text[Style["same Residual: s=2",12,Italic],{0.9,.5}],
  Text[Style["nuisance orbits",12],{-1.2,5.5}],
  Arrow[{{-2,-2.4},{-2,-2.9}}],
  Arrow[{{0,-2.4},{0,-2.9}}],
  Arrow[{{2,-2.4},{2,-2.9}}],
  Text[Style["collapse each orbit to its s value",11],{0,-3.35}]
 },
 Axes->True,AxesLabel->{"signal s","nuisance n"},
 PlotRange->{{-3.4,3.6},{-3.8,6.3}},
 ImageSize->520,
 PlotLabel->Style["Invariant across nuisance orbits",15,Bold]];

right=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-4,.6},{-1.5,1.8}],
  Rectangle[{-.6,.6},{1.9,1.8}],
  Rectangle[{2.8,.6},{5.3,1.8}],
  Text[Style["x=(s,n)=(2,5)",12,Bold],{-2.75,1.2}],
  Text[Style["z=T x=(7,-3)",12,Bold],{.65,1.2}],
  Text[Style["R=(z1+z2)/2=2",12,Bold],{4.05,1.2}],
  Arrow[{{-1.5,1.2},{-.6,1.2}}],
  Arrow[{{1.9,1.2},{2.8,1.2}}],
  Text[Style["invertible recoding T",11],{-.05,2.15}],
  Text[Style["reconstruct",11],{2.35,2.15}],
  Text[Style["surface coordinates change; declared capability survives",11,Italic],{.65,-.1}]
 },
 PlotRange->{{-4.5,5.8},{-.6,2.7}},
 ImageSize->520,
 PlotLabel->Style["Residual after representation change",15,Bold]];

GraphicsGrid[{{left,right}},Spacings->{18,5},ImageSize->1120]
