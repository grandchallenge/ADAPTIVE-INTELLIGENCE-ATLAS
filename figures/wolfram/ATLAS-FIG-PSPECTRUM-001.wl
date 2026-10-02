(* ATLAS-FIG-PSPECTRUM-001
   Normality, Pseudospectra, and Transient Growth
   Exact 2x2 Jordan-like example:
      A = {{a, K}, {0, a}},  a = 4/5, K = 4
      N = a IdentityMatrix[2]
   Spectral/operator 2-norm throughout.
*)

ClearAll["Global`*"];

a = 4/5;
K = 4;
A = {{a, K}, {0, a}};
Nmat = a IdentityMatrix[2];

ks = Range[0, 20];
gainA = Norm[MatrixPower[A, #], 2] & /@ ks;
gainN = Norm[MatrixPower[Nmat, #], 2] & /@ ks;

transient = ListLinePlot[
  {
    Transpose[{ks, gainA}],
    Transpose[{ks, gainN}]
  },
  PlotLegends -> {"non-normal A", "normal a I"},
  PlotMarkers -> Automatic,
  Frame -> True,
  FrameLabel -> {"step k", "||A^k||_2"},
  PlotRange -> All,
  ImageSize -> 520,
  GridLines -> Automatic
];

epsilons = {0.01, 0.03, 0.1, 0.3};
rNon[eps_] := Sqrt[eps (eps + K)];
rNormal[eps_] := eps;

pseudo = Graphics[
  {
    Thick,
    Table[Circle[{a, 0}, rNon[eps]], {eps, epsilons}],
    Dashed,
    Table[Circle[{a, 0}, rNormal[eps]], {eps, epsilons}],
    PointSize[0.018], Point[{a, 0}],
    Text[Style["eigenvalue a", 13], {a + 0.15, 0.08}],
    Text[Style["solid: non-normal", 12], {-0.7, 1.0}],
    Text[Style["dashed: normal", 12], {-0.7, 0.82}],\n    Table[\n      Text[Style["eps=" <> ToString[eps], 10],\n        {a, 0} + 1.06 rNon[eps] {Cos[0.45], Sin[0.45]}],\n      {eps, epsilons}\n    ]
  },
  Frame -> True,
  FrameLabel -> {"Re z", "Im z"},
  PlotRange -> {{-1.2, 2.8}, {-1.6, 1.6}},
  AspectRatio -> 0.8,
  ImageSize -> 520
];

fig = GraphicsRow[
  {transient, pseudo},
  Spacings -> 20,
  ImageSize -> 1100
];

Export["figures/masters/ATLAS-FIG-PSPECTRUM-001.png", fig, "PNG"];
fig
