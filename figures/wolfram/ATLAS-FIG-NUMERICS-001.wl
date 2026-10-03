(* ATLAS-FIG-NUMERICS-001 — stability regions, stiffness, and splitting order *)

explicitRegion=
 RegionPlot[
  (xr+1)^2+yi^2<1,
  {xr,-4,2},{yi,-3,3},
  PlotStyle->GrayLevel[.72],
  BoundaryStyle->Directive[Black,Thick],
  Frame->True,
  FrameLabel->{"Re(z)","Im(z)"},
  PlotPoints->80
 ];

implicitBoundary=
 ContourPlot[
  (xr-1)^2+yi^2==1,
  {xr,-4,2},{yi,-3,3},
  ContourStyle->Directive[GrayLevel[.3],Dashed,Thick]
 ];

stabilityPanel=
 Show[
  explicitRegion,
  implicitBoundary,
  PlotRange->{{-4,2},{-3,3}},
  ImageSize->430,
  PlotLabel->Style["Euler absolute-stability geometry",14,Bold],
  Epilog->{
   Text[Style["explicit stable",11],{-1,0}],
   Text[Style["implicit: all Re(z)<0 stable",10,Italic],{-2.15,2.45}],
   Text[Style["implicit boundary",10,GrayLevel[.25]],{1,1.4}]
  }
 ];

ns=Range[0,7];
exactFast=Table[{n,Exp[-3 n]},{n,ns}];
explicitFast=Table[{n,Abs[(-2)^n]},{n,ns}];
implicitFast=Table[{n,(1/4)^n},{n,ns}];

stiffPanel=
 ListLogPlot[
  {exactFast,explicitFast,implicitFast},
  Joined->True,
  PlotMarkers->Automatic,
  PlotStyle->{
   Directive[Black,Thick],
   Directive[GrayLevel[.35],Dashed,Thick],
   Directive[GrayLevel[.55],DotDashed,Thick]
  },
  PlotLegends->Placed[{"exact","explicit Euler","implicit Euler"},Below],
  Frame->True,
  FrameLabel->{"step n","absolute fast-mode magnitude"},
  PlotRange->All,
  ImageSize->430,
  PlotLabel->Style["Stiff fast mode, h=0.03",14,Bold]
 ];

aa={{0,1},{0,0}};
bb={{0,0},{1,0}};
hs=N[2.^(-Range[2,9])];

lieErr=
 Table[
  With[{hh=h},
   {hh,
    Norm[
     MatrixExp[hh aa].MatrixExp[hh bb]
     -
     MatrixExp[hh(aa+bb)],
     "Frobenius"
    ]}
  ],
  {h,hs}
 ];

strangErr=
 Table[
  With[{hh=h},
   {hh,
    Norm[
     MatrixExp[(hh/2) aa].
     MatrixExp[hh bb].
     MatrixExp[(hh/2) aa]
     -
     MatrixExp[hh(aa+bb)],
     "Frobenius"
    ]}
  ],
  {h,hs}
 ];

splitPanel=
 ListLogLogPlot[
  {lieErr,strangErr},
  Joined->True,
  PlotMarkers->Automatic,
  PlotStyle->{
   Directive[Black,Thick],
   Directive[GrayLevel[.4],Dashed,Thick]
  },
  PlotLegends->Placed[{"Lie defect","Strang defect"},Below],
  Frame->True,
  FrameLabel->{"h","Frobenius local defect"},
  PlotRange->All,
  ImageSize->430,
  PlotLabel->Style["Noncommuting splitting error",14,Bold],
  Epilog->{
   Inset[Style["Lie ~ h^2",10],Scaled[{.28,.72}]],
   Inset[Style["Strang ~ h^3",10],Scaled[{.63,.35}]]
  }
 ];

GraphicsGrid[
 {{stabilityPanel,stiffPanel,splitPanel}},
 Spacings->{12,5},
 ImageSize->1370
]
