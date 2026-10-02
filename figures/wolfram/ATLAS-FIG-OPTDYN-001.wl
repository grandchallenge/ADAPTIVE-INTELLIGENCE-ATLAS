(* ATLAS-FIG-OPTDYN-001
   Optimizer-State Dynamics
   Momentum on the one-dimensional quadratic L(theta)=h theta^2/2.
   beta=9/10, eta=1/10, h=1.
   State ordering: z=(theta,v).
*)

ClearAll["Global`*"];

beta = 9/10;
eta = 1/10;
h = 1;
J = {{1 - eta h, -eta beta}, {h, beta}};

starts = {{2, 0}, {0, 2}, {-2, 1}};
trajs = NestList[J.# &, #, 18] & /@ starts;

phase = ListLinePlot[
  trajs,
  PlotStyle -> {
    Directive[Thick],
    Directive[Thick, Dashed],
    Directive[Thick, Dotted]
  },
  PlotMarkers -> Automatic,
  Frame -> True,
  FrameLabel -> {"theta", "velocity state v"},
  PlotRange -> All,
  AspectRatio -> 1,
  ImageSize -> 350,
  PlotLabel -> Style["Coupled optimizer-state trajectories", 14, Bold]
];

ev = N[Eigenvalues[J], 12];
eigplot = Graphics[
  {
    Thick, Circle[{0, 0}, 1],
    PointSize[0.025],
    Point[{Re[#], Im[#]} & /@ ev],
    Table[
      Text[
        Style[NumberForm[ev[[i]], {4, 2}], 11],
        {Re[ev[[i]]], Im[ev[[i]]]} + {0.15, 0.08}
      ],
      {i, Length[ev]}
    ]
  },
  Frame -> True,
  FrameLabel -> {"Re lambda", "Im lambda"},
  PlotRange -> {{-1.15, 1.15}, {-1.15, 1.15}},
  AspectRatio -> 1,
  ImageSize -> 350,
  PlotLabel -> Style["Eigenvalues inside unit circle", 14, Bold]
];

ks = Range[0, 20];
gain = N[Norm[MatrixPower[J, #], 2] & /@ ks, 12];
peak = First@MaximalBy[Transpose[{ks, gain}], Last];

gainplot = ListLinePlot[
  Transpose[{ks, gain}],
  PlotStyle -> Thick,
  PlotMarkers -> Automatic,
  Frame -> True,
  FrameLabel -> {"step k", "||J^k||_2"},
  PlotRange -> All,
  ImageSize -> 350,
  Epilog -> {
    PointSize[0.025], Point[peak],
    Text[
      Style[
        "peak " <> ToString[NumberForm[peak[[2]], {4, 2}]] <>
        " at k=" <> ToString[peak[[1]]], 11, Bold
      ],
      peak + {2, 0.12}
    ]
  },
  PlotLabel -> Style["Finite-horizon amplification", 14, Bold]
];

fig = GraphicsRow[
  {phase, eigplot, gainplot},
  Spacings -> 18,
  ImageSize -> 1120
];

Export["figures/masters/ATLAS-FIG-OPTDYN-001.png", fig, "PNG"];
fig
