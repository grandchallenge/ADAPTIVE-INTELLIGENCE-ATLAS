(* ATLAS-FIG-DYN-001 v0.1.1 — source-native vertical print successor.
   Preserves the original ATLAS-FIG-DYN-001.wl and 1160x400 master.
   Each panel is independently exported as a Wolfram-native vector PDF.
   Assemble with tools/build_dyn_vertical_455.py.
   Plots are finite samples of the exact analytic curves, not experimental data.
*)
stable=Graphics[
 {Black,Table[Line[Table[{t,x0 Exp[-2t]},{t,0,2.2,.22}]],
    {x0,{-3,-1,1,3}}]},
 Axes->True,AxesLabel->{"t","x(t)"},
 PlotRange->{{0,2.2},{-3.3,3.3}},ImageSize->500,
 AspectRatio->.35,PlotLabel->"Exponential attraction"
];
saddle=Graphics[
 {Black,Line[Table[{m,Sqrt[m]},{m,0,4,.2}]],
  Gray,Dashed,Line[Table[{m,-Sqrt[m]},{m,0,4,.2}]],
  Black,Text["stable",{3,1.85}],Text["unstable",{3,-1.85}]},
 Axes->True,AxesLabel->{"mu","x*"},
 PlotRange->{{0,4},{-2.3,2.3}},ImageSize->500,
 AspectRatio->.35,PlotLabel->"Saddle-node equilibria"
];
oscillator=Graphics[
 {Black,AbsoluteThickness[2],Circle[{0,0},1],
  PointSize[.018],Point[{1,0}],Arrow[{{.8,-.45},{.63,-.7}}],
  Text["H = 1/2",{0,-1.16}]},
 Axes->True,AxesLabel->{"q","p"},
 PlotRange->{{-1.3,1.3},{-1.3,1.3}},ImageSize->500,
 AspectRatio->1,PlotLabel->"Exact harmonic oscillator"
];
(* Export each Graphics to figures/derivatives/ATLAS-FIG-DYN-001-v0.1.1-panel-{1,2,3}.pdf
   using the same Wolfram PDF exporter. PDF metadata may vary by run.
   The derived PNG is reproducibly assembled from those three checked-in PDFs. *)
