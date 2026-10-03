(* ATLAS-FIG-DYN-001 — stable flow, saddle-node bifurcation, harmonic oscillator *)

stable=Plot[
 Evaluate@Table[x0 Exp[-2 t],{x0,{-3,-1,1,3}}],
 {t,0,2.2},
 PlotStyle->Table[Directive[Black,If[i==2||i==3,Thick,Thin]],{i,4}],
 AxesLabel->{"t","x(t)"},
 PlotRange->{{0,2.2},{-3.2,3.2}},
 ImageSize->360,
 PlotLabel->Style["Exponential attraction: x'=-2x",14,Bold],
 Epilog->{Text[Style["x(t)=x0 e^(-2t)",11,Italic],{1.45,2.35}]}
];

sn=Show[
 Plot[Sqrt[mu],{mu,0,4},
   PlotStyle->Directive[Black,Thick]],
 Plot[-Sqrt[mu],{mu,0,4},
   PlotStyle->Directive[GrayLevel[.35],Dashed,Thick]],
 Graphics[{
   PointSize[.018],Point[{0,0}],
   Text[Style["stable",11,Bold],{3,1.95}],
   Text[Style["unstable",11,GrayLevel[.3]],{3,-1.95}],
   Text[Style["collision",11],{.45,.3}]
 }],
 Axes->True,
 AxesLabel->{"mu","equilibrium x*"},
 PlotRange->{{-.2,4.2},{-2.35,2.35}},
 ImageSize->360,
 PlotLabel->Style["Saddle-node: x'=mu-x^2",14,Bold]
];

osc=ParametricPlot[
 {Cos[t],-Sin[t]},
 {t,0,2 Pi},
 PlotStyle->Directive[Black,Thick],
 Axes->True,
 AxesLabel->{"q","p"},
 AspectRatio->1,
 PlotRange->{{-1.25,1.25},{-1.25,1.25}},
 ImageSize->360,
 PlotLabel->Style["Exact Hamiltonian orbit",14,Bold],
 Epilog->{
   PointSize[.02],Point[{1,0}],
   Arrow[{{.82,-.45},{.68,-.7}}],
   Text[Style["H=(q^2+p^2)/2=1/2",10,Italic],{0,-1.12}]
 }
];

GraphicsGrid[{{stable,sn,osc}},Spacings->{12,5},ImageSize->1160]
