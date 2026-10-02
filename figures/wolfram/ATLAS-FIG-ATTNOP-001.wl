(* ATLAS-FIG-ATTNOP-001
   Attention as an Operator
   Exact toy system with d_k = 2.
   Numeric cell labels make color redundant.
*)

ClearAll["Global`*"];

Q = {{1, 0}, {0, 1}, {1, 1}};
K = Q;
V = {{1, 0}, {0, 1}, {1, -1}};

S = N[Q.Transpose[K]/Sqrt[2], 8];
A = N[Map[Exp[#]/Total[Exp[#]] &, S], 8];
Y = N[A.V, 8];

panel[m_, title_] := Module[
  {nr = Length[m], nc = Length[First[m]], lo = Min[Flatten[m]],
   hi = Max[Flatten[m]], cf},
  cf[z_] := GrayLevel[0.92 - 0.55 If[hi == lo, 0.5, (z - lo)/(hi - lo)]];
  Graphics[
    {
      Table[
        {
          cf[m[[i, j]]],
          Rectangle[{j - 1, nr - i}, {j, nr - i + 1}],
          Black, Thickness[0.002],
          Line[{{j - 1, nr - i}, {j, nr - i}, {j, nr - i + 1},
                {j - 1, nr - i + 1}, {j - 1, nr - i}}],
          Text[Style[NumberForm[m[[i, j]], {4, 2}], 12, Bold],
               {j - 0.5, nr - i + 0.5}]
        },
        {i, nr}, {j, nc}
      ]
    },
    PlotRange -> {{0, nc}, {0, nr}},
    Axes -> False, Frame -> False, ImageSize -> 220,
    PlotLabel -> Style[title, 14, Bold]
  ]
];

fig = GraphicsRow[
  {
    panel[S, "scores S"],
    panel[A, "mixing operator A"],
    panel[V, "values V"],
    panel[Y, "output Y = A V"]
  },
  Spacings -> 15,
  ImageSize -> 1000
];

Export["figures/masters/ATLAS-FIG-ATTNOP-001.png", fig, "PNG"];
fig
