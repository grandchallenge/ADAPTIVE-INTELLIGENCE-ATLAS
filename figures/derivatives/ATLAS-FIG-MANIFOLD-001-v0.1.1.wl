(* Editorial derivative v0.1.1: endpoint labels separated; sphere geometry unchanged. *)
(* ATLAS-FIG-MANIFOLD-001
   Geometry of Constrained State Spaces
   Representation class: schematic with exact spherical geometry.
   The sphere, tangent-plane incidence, exponential-map endpoint, retraction
   endpoint, and geodesic are literal. Perspective, label offsets, and patch
   extent are nonliteral.
*)

ClearAll["Global`*"];

x = {0., 0., 1.};
v = {0.8, 0., 0.};
vn = Norm[v];

expPoint = Cos[vn] x + Sin[vn] v/vn;
retPoint = Normalize[x + v];
geodesic[t_] := Cos[t vn] x + Sin[t vn] v/vn;

fig = Show[
  Graphics3D[{
    Opacity[0.10], Sphere[{0, 0, 0}, 1],
    Opacity[0.10], InfinitePlane[{x, {1, 0, 0}, {0, 1, 0}}],
    Opacity[1],
    Thick, Arrow[{x, x + v}],
    Dashed, Line[{x, retPoint}],
    PointSize[0.018], Point[{x, expPoint, retPoint}],
    Directive[GrayLevel[0.3], Thin],
    Line[{expPoint, expPoint + {0.3, -0.3, -0.12}}],
    Line[{retPoint, retPoint + {-0.12, 0.32, 0.30}}],
    Directive[Black],
    Text[Style["x", 14], x + {0, 0, 0.10}],
    Text[Style["Exp_x(v)", 14, Background -> White], expPoint + {0.3, -0.3, -0.12}],
    Text[Style["R_x(v)", 14, Background -> White], retPoint + {-0.12, 0.32, 0.30}],
    Text[Style["tangent step", 13], x + 0.55 v + {0, 0, 0.08}],
    Text[Style["T_x S^2", 13], x + {-0.48, 0.42, 0.02}]
  }],
  ParametricPlot3D[
    geodesic[t], {t, 0, 1},
    PlotStyle -> Directive[Thick]
  ],
  PlotRange -> {{-1.15, 1.35}, {-1.15, 1.15}, {-1.15, 1.35}},
  Boxed -> False,
  Axes -> False,
  ImageSize -> 760,
  ViewPoint -> {2.2, -2.5, 1.6}
];

Export["figures/derivatives/ATLAS-FIG-MANIFOLD-001-v0.1.1.png", fig, "PNG"];
fig
