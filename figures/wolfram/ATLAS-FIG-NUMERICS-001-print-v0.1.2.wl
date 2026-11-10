(* ATLAS-FIG-NUMERICS-001 — versioned print successor for issue #459.
   Source-native Wolfram construction; original master/source remain unchanged.
   Candidate only: no rendered binary or physical print certification implied.
   Each panel spans the same 1160px output width, stacked vertically.
*)
ClearAll[x,y,h,A,B,ee,ie,err,lie,strang,exact,hs,lieData,strangData];
A={{0,1},{0,0}}; B={{0,0},{1,0}};
lie[t_?NumericQ]:=MatrixExp[t A].MatrixExp[t B];
strang[t_?NumericQ]:=MatrixExp[(t/2) A].MatrixExp[t B].MatrixExp[(t/2) A];
exact[t_?NumericQ]:=MatrixExp[t (A+B)];
hs=N[10.^Range[-3,-.25,.2]];
lieData=Table[{t,Norm[lie[t]-exact[t],"Frobenius"]},{t,hs}];
strangData=Table[{t,Norm[strang[t]-exact[t],"Frobenius"]},{t,hs}];
(* Symbolic leading-order witnesses, independent of the plot raster. *)
If[!TrueQ[Simplify[A.B-B.A=={{1,0},{0,-1}}]],
 Print["FAIL: commutator"]; Abort[]];
If[!TrueQ[Simplify[Series[
 MatrixExp[h A].MatrixExp[h B]-MatrixExp[h(A+B)],{h,0,2}]
 == (h^2/2) (A.B-B.A)+O[h]^3]],
 Print["FAIL: Lie series"]; Abort[]];
ee=RegionPlot[(x+1)^2+y^2<1,{x,-4,2},{y,-3,3},
 Frame->True,FrameLabel->{"Re(z)","Im(z)"},PlotPoints->70,
 BoundaryStyle->Directive[Black,Thick],PlotStyle->GrayLevel[.82],
 ImageSize->1050,ImagePadding->80,
 PlotLabel->Style["Explicit Euler: strict decay |1+z|<1",22,Bold],
 Epilog->{Line[{{0,-3},{0,3}}],Line[{{-4,0},{2,0}}],
 Text[Style["strict decay",18,Bold],{-1,0.4}]}];
ie=RegionPlot[(x-1)^2+y^2>1,{x,-4,2},{y,-3,3},
 Frame->True,FrameLabel->{"Re(z)","Im(z)"},PlotPoints->70,
 BoundaryStyle->Directive[Black,Thick],PlotStyle->GrayLevel[.82],
 ImageSize->1050,ImagePadding->80,
 PlotLabel->Style["Implicit Euler: strict decay |1-z|>1",22,Bold],
 Epilog->{Line[{{0,-3},{0,3}}],Line[{{-4,0},{2,0}}],
 Text[Style["closed left half-plane is non-growing",17,Bold],{-2.1,2.25}]}];
err=ListLogLogPlot[{lieData,strangData},Joined->True,
 PlotMarkers->Automatic,
 PlotStyle->{Directive[Black,Thick],Directive[GrayLevel[.35],Dashed,Thick]},
 Frame->True,FrameLabel->{"h","Frobenius local defect"},
 ImageSize->1050,ImagePadding->80,
 PlotLabel->Style["Split one-step local defect (small-h slopes 2 and 3)",22,Bold],
 PlotLegends->Placed[{"Lie-Trotter","Strang"},{.78,.28}],
 Epilog->{Text[Style["~ h^2",19,Bold],Scaled[{.34,.48}]],
 Text[Style["~ h^3",19,Bold],Scaled[{.52,.25}]]}];
(* A vertically composed master; export only after Wolfram-native replay. *)
GraphicsColumn[{ee,ie,err},Spacings->20,ImageSize->1160]
