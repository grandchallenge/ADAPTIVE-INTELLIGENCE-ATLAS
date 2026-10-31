(* ATLAS-FIG-MANIFOLD-001 v0.1.3 — native Wolfram figure label-separation repair.
   Preserve original and v0.1.2 sources; exact unit-sphere geometry unchanged.
   Endpoint labels moved into a separated two-item legend; marker colors and
   solid/dashed curves identify Exp_x(v) and R_x(v) at print scale. *)
ClearAll["Global`*"];
x={0,0,1}; v={4/5,0,0}; vn=Sqrt[v.v];
expPoint=Cos[vn] x+Sin[vn] v/vn;
retPoint=(x+v)/Sqrt[(x+v).(x+v)];
geodesic[t_]:=Cos[t vn] x+Sin[t vn] v/vn;
expColor=RGBColor[.04,.31,.62]; retColor=RGBColor[.67,.27,.05];
spherePlot=Show[
 Graphics3D[{
  Directive[Opacity[.19],GrayLevel[.72]],Sphere[{0,0,0},1],
  Directive[Opacity[.22],GrayLevel[.48]],InfinitePlane[{x,{1,0,0},{0,1,0}}],
  Directive[Black,Thick],Arrow[{x,x+v}],
  Directive[retColor,Dashed,Thick],Line[{x,retPoint}],
  Directive[Black,PointSize[.018]],Point[x],
  Directive[expColor,PointSize[.029]],Point[expPoint],
  Directive[retColor,PointSize[.029]],Point[retPoint],
  Text[Style[TraditionalForm[x],18,Bold],x+{0,0,.13}],
  Text[Style["tangent step",15,Bold],x+.55 v+{0,0,.12}],
  Text[Style[Row[{Subscript["T","x"],Superscript["S",2]}],16,Bold],x+{-.48,.42,.04}]
 }],
 ParametricPlot3D[geodesic[t],{t,0,1},PlotStyle->Directive[expColor,Thick]],
 PlotRange->{{-1.15,1.35},{-1.15,1.15},{-1.15,1.35}},
 Boxed->False,Axes->False,ImageSize->760,ViewPoint->{2.2,-2.5,1.6},
 Background->White
];
fig=Legended[spherePlot,Placed[
 SwatchLegend[{expColor,retColor},
  {Row[{Subscript["Exp","x"],"(v): spherical exponential (solid arc)"}],
   Row[{Subscript["R","x"],"(v): normalized retraction (dashed chord)"}]},
  LabelStyle->Directive[Black,16],LegendLayout->"Column"],Below]];
fig
