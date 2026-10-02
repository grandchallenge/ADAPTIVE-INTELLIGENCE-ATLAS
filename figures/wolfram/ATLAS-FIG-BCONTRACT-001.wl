(* ATLAS-FIG-BCONTRACT-001 — Boundary contract + exact sensitivity inset *)
ClearAll["Global`*"];
cc = {{2, 1/2}, {0, 1}};
sigma = Max[SingularValueList[N[cc, 30]]];

contractPanel = Graphics[
  {
    EdgeForm[Black], FaceForm[White],
    Rectangle[{-4, -1}, {-2, 1}],
    Rectangle[{2, -1}, {4, 1}],
    Rectangle[{-1.2, -1.8}, {1.2, 1.8}],
    Arrow[{{-2, 0}, {-1.2, 0}}],
    Arrow[{{1.2, 0}, {2, 0}}],
    Text[Style["upstream f", 15], {-3, 0}],
    Text[Style["downstream g", 15], {3, 0}],
    Text[Style["BOUNDARY CONTRACT", 15, Bold], {0, 1.35}],
    Text[Style["semantic", 13], {0, 0.65}],
    Text[Style["geometric", 13], {0, 0.2}],
    Text[Style["differential", 13], {0, -0.25}],
    Text[Style["numerical", 13], {0, -0.7}],
    Text[Style["JVP  →", 12], {-1.55, 0.28}],
    Text[Style["←  VJP", 12], {1.55, -0.28}]
  },
  PlotRange -> {{-4.3, 4.3}, {-2.1, 2.1}},
  ImageSize -> 520,
  PlotLabel -> Style["Interface obligations", 16, Bold]
];

circle = ParametricPlot[
  {Cos[t], Sin[t]}, {t, 0, 2 Pi},
  PlotStyle -> Directive[GrayLevel[0.55], Dashed, Thick]
];
ellipse = ParametricPlot[
  cc . {Cos[t], Sin[t]}, {t, 0, 2 Pi},
  PlotStyle -> Directive[Black, Thick]
];
sensitivityPanel = Show[
  circle, ellipse,
  Axes -> True,
  AspectRatio -> 1,
  PlotRange -> {{-2.4, 2.4}, {-2.4, 2.4}},
  PlotLabel -> Style[
    Row[{"Local sensitivity:  ||C||_2 = ", NumberForm[sigma, {6, 4}]}],
    16, Bold
  ],
  Epilog -> {
    Text[Style["unit perturbations", 12, GrayLevel[0.35]], {-0.95, -1.25}],
    Text[Style["C · perturbations", 12, Black], {1.25, 1.55}],
    Inset[Style["C = [[2, 1/2], [0, 1]]", 12], {0, -2.05}]
  },
  ImageSize -> 520
];

GraphicsGrid[
  {{contractPanel, sensitivityPanel}},
  Spacings -> {20, 5},
  ImageSize -> 1100
]
