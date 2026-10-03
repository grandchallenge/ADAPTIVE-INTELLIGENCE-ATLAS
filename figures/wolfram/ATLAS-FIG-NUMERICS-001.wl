(* ATLAS-FIG-NUMERICS-001 — Euler stability regions and split local-defect scaling *)

ee=RegionPlot[
 (x+1)^2+y^2<1,
 {x,-4,2},{y,-3,3},
 Frame->True,
 FrameLabel->{"Re(z)","Im(z)"},
 PlotPoints->70,
 BoundaryStyle->Directive[Black,Thick],
 PlotStyle->GrayLevel[.82],
 ImageSize->350,
 PlotLabel->Style["Explicit Euler: |1+z|<1",14,Bold],
 Epilog->{
  Line[{{0,-3},{0,3}}],
  Line[{{-4,0},{2,0}}],
  Text[Style["stable",11,Bold],{-1,0.4}]
 }
];

ie=RegionPlot[
 (x-1)^2+y^2>1,
 {x,-4,2},{y,-3,3},
 Frame->True,
 FrameLabel->{"Re(z)","Im(z)"},
 PlotPoints->70,
 BoundaryStyle->Directive[Black,Thick],
 PlotStyle->GrayLevel[.82],
 ImageSize->350,
 PlotLabel->Style["Implicit Euler: |1-z|>1",14,Bold],
 Epilog->{
  Line[{{0,-3},{0,3}}],
  Line[{{-4,0},{2,0}}],
  Text[Style["left half-plane included",10,Bold],{-2.1,2.25}]
 }
];

A={{0,1},{0,0}};
B={{0,0},{1,0}};
lie[h_?NumericQ]:=MatrixExp[h A].MatrixExp[h B];
strang[h_?NumericQ]:=
 MatrixExp[(h/2) A].MatrixExp[h B].MatrixExp[(h/2) A];
exact[h_?NumericQ]:=MatrixExp[h(A+B)];
hs=N[10.^Range[-3,-.25,.2]];
lieData=Table[{h,Norm[lie[h]-exact[h],"Frobenius"]},{h,hs}];
strangData=Table[{h,Norm[strang[h]-exact[h],"Frobenius"]},{h,hs}];

err=ListLogLogPlot[
 {lieData,strangData},
 Joined->True,
 PlotMarkers->Automatic,
 PlotStyle->{Directive[Black,Thick],Directive[GrayLevel[.35],Dashed,Thick]},
 Frame->True,
 FrameLabel->{"h","local defect norm"},
 ImageSize->390,
 PlotLabel->Style["Split local-defect scaling",14,Bold],
 PlotLegends->Placed[{"Lie-Trotter","Strang"},{.72,.25}],
 Epilog->{
  Text[Style["~ h^2",11,Bold],Scaled[{.34,.48}]],
  Text[Style["~ h^3",11,Bold],Scaled[{.52,.25}]]
 }
];

GraphicsGrid[{{ee,ie,err}},Spacings->{10,5},ImageSize->1160]
