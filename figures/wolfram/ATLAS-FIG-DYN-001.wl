(* ATLAS-FIG-DYN-001 — pitchfork bifurcation and harmonic oscillator phase flow *)

originStable=Plot[0,{mu,-2,0},
 PlotStyle->Directive[Black,Thick]];
originUnstable=Plot[0,{mu,0,2},
 PlotStyle->Directive[GrayLevel[.45],Dashed,Thick]];
upper=Plot[Sqrt[mu],{mu,0,2},
 PlotStyle->Directive[Black,Thick]];
lower=Plot[-Sqrt[mu],{mu,0,2},
 PlotStyle->Directive[Black,Thick]];

left=Show[
 originStable,originUnstable,upper,lower,
 Axes->True,
 AxesLabel->{"mu","equilibrium x*"},
 PlotRange->{{-2,2},{-1.7,1.7}},
 ImageSize->520,
 PlotLabel->Style["Supercritical pitchfork",15,Bold],
 Epilog->{
  Text[Style["stable",11],{-1.25,.16}],
  Text[Style["unstable",11,GrayLevel[.35]],{1.15,.16}],
  Text[Style["stable branches",11],{1.15,1.25}],
  PointSize[.018],Point[{0,0}]
 }
];

field=StreamPlot[{p,-q},{q,-2,2},{p,-2,2},
 StreamStyle->GrayLevel[.65],
 StreamPoints->Fine,
 Frame->True,
 FrameLabel->{"q","p"},
 PlotRange->{{-2,2},{-2,2}}
];

circle=ParametricPlot[{Cos[t],-Sin[t]},{t,0,2 Pi},
 PlotStyle->Directive[Black,Thick]];

right=Show[
 field,circle,
 PlotRange->{{-2,2},{-2,2}},
 ImageSize->520,
 PlotLabel->Style["Harmonic oscillator phase flow",15,Bold],
 Epilog->{
  PointSize[.018],Point[{1,0}],
  Arrow[{{1,0},{.92,-.32}}],
  Text[Style["H=(q^2+p^2)/2 conserved",11,Italic],{0,-1.65}]
 }
];

GraphicsGrid[{{left,right}},Spacings->{18,5},ImageSize->1120]
