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
  Axes->False
},
 PlotRange->{{-0.5,4.2},{-0.5,4.8}},
 ImageSize->360,
 PlotLabel->Style["Global norm clipping",14,Bold]
];

clip=Graphics[{
  Thick,
  Arrow[{{0,0},{3,4}}],
  Directive[GrayLevel[.45],Thick],
  Arrow[{{0,0},{6/5,8/5}}],
  PointSize[.018],
  Point[{3,4}],
  Point[{6/5,8/5}],
  Text[Style["g=(3,4), ||g||=5",10,Bold],{3.1,4.25}],
  Text[Style["g_clip=(6/5,8/5), ||g_clip||=2",10],{1.75,1.35}],
  Circle[{0,0},2],
  Text[Style["tau=2",10,Italic],{-.05,2.18}]
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
  Text[Style["decoupled = 181/100",10,Bold],{181/100,-.22}],
  Text[Style["coupled = 183/100",10,Bold],{183/100,.22}],
  Text[Style["difference = 1/50",10,Italic],{182/100,.55}]
 },
 Axes->True,
 AxesLabel->{"next theta",""},
 PlotRange->{{1.79,1.85},{-.6,.8}},
 ImageSize->360,
 PlotLabel->Style["Adaptive decay is not equivalent",14,Bold]
];

GraphicsGrid[{{gd,clip,decay}},Spacings->{12,5},ImageSize->1160]
