(* ATLAS-FIG-MANIFOLD-001 v0.1.3 — source-native Wolfram print revision.
   Historical v0.1.2 and original master remain unchanged.
   Exact sphere x=(0,0,1), tangent v=(4/5,0,0).
   Callout leaders and opposing lateral offsets separate Exp_x(v) and R_x(v)
   at actual book print size; these are presentational, not new claims. *)
ClearAll[x,v,vn,expPoint,retPoint,geodesic,expLabel,retLabel,fig];
x={0,0,1};v={4/5,0,0};vn=Sqrt[v.v];
expPoint=Cos[vn] x+Sin[vn] v/vn;
retPoint=(x+v)/Sqrt[(x+v).(x+v)];
geodesic[t_]:=Cos[t vn] x+Sin[t vn] v/vn;
expLabel=expPoint+{.16,-.72,.30};
retLabel=retPoint+{.10,.72,-.26};
fig=Show[
 Graphics3D[{
  Directive[Opacity[.19],GrayLevel[.72]],Sphere[{0,0,0},1],
  Directive[Opacity[.22],GrayLevel[.48]],InfinitePlane[{x,{1,0,0},{0,1,0}}],
  Directive[Opacity[1],Black,Thick],Arrow[{x,x+v}],
  Directive[Black,Dashed,Thick],Line[{x,retPoint}],
  PointSize[.022],Point[{x,expPoint,retPoint}],
  Directive[GrayLevel[.2],AbsoluteThickness[1.8]],
  Line[{expPoint,expLabel}],Line[{retPoint,retLabel}],
  Text[Style[TraditionalForm[x],18,Bold],x+{0,0,.13}],
  Text[Style[Row[{Subscript["Exp","x"],"(v)"}],18,Bold,Background->White],expLabel],
  Text[Style[Row[{Subscript["R","x"],"(v)"}],18,Bold,Background->White],retLabel],
  Text[Style["tangent step",15,Bold],x+.55 v+{0,0,.12}],
  Text[Style[Row[{Subscript["T","x"],Superscript["S",2]}],16,Bold],x+{-.48,.42,.04}]
 }],
 ParametricPlot3D[geodesic[t],{t,0,1},PlotStyle->Directive[Black,Thick]],
 PlotRange->{{-1.15,1.35},{-1.15,1.15},{-1.15,1.35}},
 Boxed->False,Axes->False,ImageSize->760,ViewPoint->{2.2,-2.5,1.6},
 Background->White
];
fig
