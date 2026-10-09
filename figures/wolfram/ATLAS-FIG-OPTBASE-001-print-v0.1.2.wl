(* ATLAS-FIG-OPTBASE-001 v0.1.2 publication portrait derivative.
   Exact original mathematical data retained from source blob 61123040326f80ec73a170778ba1140ef3f8fcb9;
   3 stacked panels preserve strict GD |1-a|<1 iff 0<a<2,
   gradient (3,4) with threshold 2, and updates 181/100 and 183/100.
   Panel arrangement and math-label typesetting are editorial. *)
(* ATLAS-FIG-OPTBASE-001 — quadratic stability, clipping, and decay *)

gd=Plot[
 Abs[1-a],
 {a,0,3},
 PlotStyle->Directive[Black,Thick],
 AxesLabel->{"eta lambda","|1-eta lambda|"},
 PlotRange->{{0,3},{0,2.1}},
 ImageSize->360,
 PlotLabel->Style["Quadratic GD amplification",14,Bold],
 Epilog->{
   Directive[GrayLevel[.85],Opacity[.5]],
   Rectangle[{0,0},{2,1}],
   Directive[Black],
   Line[{{0,1},{3,1}}],
   Text[Style["asymptotic convergence",10,Italic],{1,.35}],
   Text[Style["boundary",10],{2.12,1.12}]
 }
];

clip=Graphics[{
  Thick,
  Arrow[{{0,0},{3,4}}],
  Directive[GrayLevel[.45],Thick],
  Arrow[{{0,0},{6/5,8/5}}],
  PointSize[.018],
  Point[{3,4}],
  Point[{6/5,8/5}],
  Text[Style["g=(3,4), ||g||=5",13,Bold],{2.1,4.35}],
  Text[Style[Row[{Subscript["g","clip"],"=(6/5,8/5)"}],13,Bold],{1.8,.7}],
  Circle[{0,0},2],
  Text[Style[Row[{"threshold ",Style["[Tau]",Italic],"=2"}],13],{-.65,2.25}]
 },
 Axes->True,
 AxesLabel->{"g1","g2"},
 PlotRange->{{-2.4,4.4},{-2.4,4.8}},
 AspectRatio->1,
 ImageSize->360,
 PlotLabel->Style["Clipping changes magnitude, not direction",14,Bold]
];

decay=Graphics[{
  Thick,
  Line[{{181/100,0},{183/100,0}}],
  PointSize[.025],
  Point[{181/100,0}],
  Point[{183/100,0}],
  Text[Style["decoupled = 181/100",13,Bold],{181/100,-.30}],
  Text[Style["coupled = 183/100",13,Bold],{183/100,.35}],
  Text[Style["difference = 1/50",12,Italic],{182/100,.65}]
 },
 Axes->True,
 AxesLabel->{"next theta",""},
 PlotRange->{{1.79,1.85},{-.6,.8}},
 ImageSize->360,
 PlotLabel->Style["Adaptive decay is not equivalent",14,Bold]
];

fig=GraphicsGrid[{{gd},{clip},{decay}},Spacings->{18,12},ImageSize->{700,990}];
fig
