(* ATLAS-FIG-NORMREP-001 — radial/tangent normalization and chord/geodesic geometry *)

u={3/5,4/5};
that={-4/5,3/5};

left=Graphics[{
  Thick,Circle[{0,0},1],
  Arrow[{{0,0},u}],
  Text[Style["u = (3/5,4/5)",12,Bold],u+{.35,.18}],
  Directive[GrayLevel[.45],Dashed,Thick],
  Arrow[{u,1.55 u}],
  Text[Style["radial direction",11,GrayLevel[.35]],1.35 u+{.25,-.1}],
  Directive[Black,Thick],
  Arrow[{u,u+.55 that}],
  Text[Style["tangent direction",11],u+.65 that+{-.12,.18}],
  PointSize[.018],Point[u],
  Text[Style["normalization removes radial scale",12,Italic],{0,-1.35}]
 },
 Axes->True,PlotRange->{{-1.55,1.8},{-1.55,1.55}},ImageSize->500,
 PlotLabel->Style["Radial versus tangential information",15,Bold]];

a={1,0};
b={1/2,Sqrt[3]/2};
s={Sqrt[3]/2,1/2};
arc=ParametricPlot[{Cos[t],Sin[t]},{t,0,Pi/3},
 PlotStyle->Directive[Black,Thick]];
right=Show[
 Graphics[{
   Circle[{0,0},1],
   Directive[GrayLevel[.5],Dashed,Thick],Line[{a,b}],
   Directive[Black,Thick],
   Arrow[{{0,0},a}],Arrow[{{0,0},b}],
   PointSize[.018],Point[{a,b,s}],
   Text[Style["a",12,Bold],a+{.12,-.12}],
   Text[Style["b",12,Bold],b+{.08,.12}],
   Text[Style["SLERP midpoint",11],s+{.2,.05}],
   Text[Style["chord = 1",11,GrayLevel[.35]],{.78,.46}],
   Text[Style["angle = Pi/3",11],{.45,.18}]
  }],
 arc,
 Axes->True,PlotRange->{{-1.2,1.35},{-1.2,1.35}},ImageSize->500,
 PlotLabel->Style["Chord, arc, and SLERP",15,Bold]
];

GraphicsGrid[{{left,right}},Spacings->{18,5},ImageSize->1100]
