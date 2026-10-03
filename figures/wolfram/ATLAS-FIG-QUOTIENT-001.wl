(* ATLAS-FIG-QUOTIENT-001 — distinct parameter representatives, identical function *)

boxes=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{-4,1.3},{-1.5,2.5}],
  Rectangle[{-4,-.3},{-1.5,.9}],
  Rectangle[{-4,-1.9},{-1.5,-.7}],
  Text[Style["theta0",13,Bold],{-3.65,2.18}],
  Text[Style["W1=(1,2), W2=(3,4)",11],{-2.7,1.7}],
  Text[Style["P theta0",13,Bold],{-3.55,.58}],
  Text[Style["W1=(2,1), W2=(4,3)",11],{-2.7,.1}],
  Text[Style["D theta0",13,Bold],{-3.55,-1.02}],
  Text[Style["W1=(2,2/3), W2=(3/2,12)",11],{-2.7,-1.5}],
  Arrow[{{-1.5,1.9},{.1,.55}}],
  Arrow[{{-1.5,.3},{.1,.35}}],
  Arrow[{{-1.5,-1.3},{.1,.15}}],
  Text[Style["same function",13,Bold],{.9,.35}]
 },
 PlotRange->{{-4.4,1.8},{-2.2,2.8}},ImageSize->530,
 PlotLabel->Style["One equivalence class, three representatives",15,Bold]];

curve=Plot[11 Max[0,x],{x,-2,2},
 PlotStyle->Directive[Black,Thick],
 AxesLabel->{"x","f(x)"},
 PlotRange->{{-2,2},{-1,23}},
 ImageSize->500,
 PlotLabel->Style["f(x)=11 max(0,x)",15,Bold],
 Epilog->{
  Text[Style["original = permuted = rescaled",12,Italic],{.6,4}]
 }];

GraphicsGrid[{{boxes,curve}},Spacings->{18,5},ImageSize->1100]
