(* ATLAS-FIG-INFO-001 — exact binary dependence witness *)
ClearAll["Global`*"];
p={{3/8,1/8},{1/8,3/8}};
mi=N[Sum[If[p[[i,j]]==0,0,p[[i,j]] Log[2,p[[i,j]]/((Total[p,{2}][[i]])(Total[p,{1}][[j]]))]],{i,2},{j,2}],16];
cells=Flatten@Table[
 {EdgeForm[Black],FaceForm[GrayLevel[1-N[p[[i,j]]]]],
  Rectangle[{j-1,2-i},{j,3-i}],
  Text[Style[ToString[TraditionalForm[p[[i,j]]]],14],{j-.5,2.5-i}]},
 {i,2},{j,2}];
Graphics[{
 cells,
 Text[Style["Y=0",12],{.5,2.25}],
 Text[Style["Y=1",12],{1.5,2.25}],
 Text[Style["X=0",12],{-.28,1.5}],
 Text[Style["X=1",12],{-.28,.5}],
 Text[Style["marginals: (1/2, 1/2)",13],{1,-.35}],
 Text[Style[Row[{"I(X;Y) = ",NumberForm[mi,{6,4}]," bits"}],14,Bold],{1,-.72}],
 Text[Style["dependence, not causal direction",12,Italic],{1,-1.08}]
 },PlotRange->{{-.7,2.7},{-1.35,2.55}},ImagePadding->25,ImageSize->700]
