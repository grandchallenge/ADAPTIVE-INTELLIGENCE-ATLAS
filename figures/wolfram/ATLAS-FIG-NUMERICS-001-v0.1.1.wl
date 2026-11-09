(* ATLAS-FIG-NUMERICS-001 v0.1.1: exact Wolfram vector-print successor.
   Original Wolfram generator and public master remain immutable.
   Export each labelled Graphics as PDF with the native Wolfram exporter.
   tools/build_numerics_print_459.py places the three vector-derived panels.
*)
explicit=Graphics[
 {GrayLevel[.85],Disk[{-1,0},1],Black,AbsoluteThickness[1.8],Circle[{-1,0},1]},
 Axes->True,AxesLabel->{"u","v"},PlotRange->{{-3,1},{-2,2}},
 AspectRatio->1,ImageSize->500];
implicit=Graphics[
 {GrayLevel[.85],Rectangle[{-3,-2},{2,2}],White,Disk[{1,0},1],
  Black,AbsoluteThickness[1.8],Circle[{1,0},1]},
 Axes->True,AxesLabel->{"u","v"},PlotRange->{{-3,2},{-2,2}},
 AspectRatio->.8,ImageSize->500];
A={{0,1},{0,0}};
B={{0,0},{1,0}};
hs=N[10.^Range[-3,-.25,.2]];
d1=Table[{Log10[h],Log10[Norm[
 MatrixExp[h A].MatrixExp[h B]-MatrixExp[h(A+B)],"Frobenius"]]},{h,hs}];
d2=Table[{Log10[h],Log10[Norm[
 MatrixExp[(h/2)A].MatrixExp[h B].MatrixExp[(h/2)A]-MatrixExp[h(A+B)],
 "Frobenius"]]},{h,hs}];
defect=Graphics[
 {Black,AbsoluteThickness[2],Line[d1],GrayLevel[.35],Dashed,
  AbsoluteThickness[2],Line[d2]},Axes->True,
 AxesLabel->{"log10 h","log10 error"},PlotRange->{{-3,-.2},{-11,-.5}},
 AspectRatio->.6,ImageSize->500];
(* Vector exports:
 Export["...-panel-1.pdf", explicit, "PDF"];
 Export["...-panel-2.pdf", implicit, "PDF"];
 Export["...-panel-3.pdf", defect, "PDF"];
 PDF export metadata is runtime-dependent; versioned PDF bytes are hash-pinned.
*)
