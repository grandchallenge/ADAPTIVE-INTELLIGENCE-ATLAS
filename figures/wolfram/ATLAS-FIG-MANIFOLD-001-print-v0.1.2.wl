(* ATLAS-FIG-MANIFOLD-001 v0.1.2 — native Wolfram publication renderer.
   Source successor of locked original blob 16cfefd6fe09a01b425dd463a75ed08dd47379f1.
   Original source retained unchanged; this fixes an unparseable literal escaped newline.
   Mathematical object: exact unit sphere x=(0,0,1), tangent v=(4/5,0,0),
   spherical exponential, normalized retraction, geodesic.
   Label and opacity changes are presentational, not new mathematical claims. *)
ClearAll["Global`*"];
x={0,0,1};
v={4/5,0,0};
vn=Sqrt[v.v];
expPoint=Cos[vn] x+Sin[vn] v/vn;
retPoint=(x+v)/Sqrt[(x+v).(x+v)];
geodesic[t_]:=Cos[t vn] x+Sin[t vn] v/vn;
fig=Show[
 Graphics3D[{
  Directive[Opacity[.19],GrayLevel[.72]],Sphere[{0,0,0},1],
  Directive[Opacity[.22],GrayLevel[.48]],InfinitePlane[{x,{1,0,0},{0,1,0}}],
  Directive[Opacity[1],Black,Thick],Arrow[{x,x+v}],
  Directive[Black,Dashed,Thick],Line[{x,retPoint}],
  PointSize[.022],Point[{x,expPoint,retPoint}],
  Text[Style[TraditionalForm[x],18,Bold],x+{0,0,.13}],
  Text[Style[Row[{Subscript["Exp","x"],"(v)"}],17,Bold],expPoint+{.13,0,.06}],
  Text[Style[Row[{Subscript["R","x"],"(v)"}],17,Bold],retPoint+{.16,0,-.05}],
  Text[Style["tangent step",15,Bold],x+.55 v+{0,0,.12}],
  Text[Style[Row[{Subscript["T","x"],Superscript["S",2]}],16,Bold],x+{-.48,.42,.04}]
 }],
 ParametricPlot3D[geodesic[t],{t,0,1},PlotStyle->Directive[Black,Thick]],
 PlotRange->{{-1.15,1.35},{-1.15,1.15},{-1.15,1.35}},
 Boxed->False,Axes->False,ImageSize->760,ViewPoint->{2.2,-2.5,1.6},
 Background->White
];
fig
