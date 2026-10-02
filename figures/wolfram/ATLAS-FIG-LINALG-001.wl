(* ATLAS-FIG-LINALG-001 — singular-value geometry and conditioning *)
ClearAll["Global`*"];
aa={{1,1},{0,1}};
sv=SingularValueList[aa];
circle=ParametricPlot[{Cos[t],Sin[t]},{t,0,2 Pi},
 PlotStyle->Directive[GrayLevel[.55],Dashed,Thick]];
ellipse=ParametricPlot[aa.{Cos[t],Sin[t]},{t,0,2 Pi},
 PlotStyle->Directive[Black,Thick]];
left=Show[circle,ellipse,Axes->True,AspectRatio->1,
 PlotRange->{{-2,2},{-2,2}},
 PlotLabel->Style["One-step geometry of A",15,Bold],
 Epilog->{
  Text[Style["unit circle",11,GrayLevel[.35]],{-1.1,-1.25}],
  Text[Style["A · unit circle",11],{1.15,1.45}],
  Inset[Style[Row[{"singular values = ",NumberForm[sv,{5,3}]}],11],{0,-1.75}]
 }];
dd={{1,0},{0,1/100}};
right=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-1,-1},{1,1}],
  Arrow[{{-1.4,0},{-1.05,0}}],
  Arrow[{{1.05,0},{1.4,0}}],
  Text[Style["input",12],{-1.7,0}],
  Text[Style["output",12],{1.7,0}],
  Text[Style["D = diag(1, 1/100)",13,Bold],{0,.45}],
  Text[Style["σmax = 1",12],{0,.1}],
  Text[Style["σmin = 1/100",12],{0,-.2}],
  Text[Style["κ₂(D) = 100",13,Bold],{0,-.55}]
 },PlotRange->{{-2.1,2.1},{-1.3,1.3}},ImageSize->500,
 PlotLabel->Style["Conditioning",15,Bold]];
GraphicsGrid[{{left,right}},Spacings->{18,5},ImageSize->1100]
