(* ATLAS OPTBASE editorial v0.1.2 Wolfram derivative.
   Bounded layout repair, exact mathematical inputs unchanged. *)
g={3,4}; tau=2; gc=(tau/Norm[g]) g;
If[!(gc=={6/5,8/5} && Norm[g]==5 && Norm[gc]==2 &&
     183/100-181/100==1/50),Abort[]];

gd=Plot[Abs[1-a],{a,0,3},
 PlotRange->{{0,3},{0,2.1}},PlotStyle->Directive[Black,Thick],
 Frame->True,Axes->False,LabelStyle->Directive[FontSize->14],FrameLabel->{"a = ηλ","|1 − a|"},
 ImageSize->350,PlotLabel->Style["A. Quadratic stability",17,Bold],
 Prolog->{Directive[GrayLevel[.93]],Rectangle[{0,0},{2,2.1}]},
 Epilog->{Directive[GrayLevel[.55],Dashed],Line[{{0,1},{3,1}}],
 Directive[GrayLevel[.5],Dotted],Line[{{2,0},{2,2.1}}],
 Directive[Black],Text[Style["0 < a < 2: contractive",14],{1,1.55}],
 Text[Style["boundary",12],{2.25,1.15}]}];

clip=Graphics[{
 {GrayLevel[.5],Thick,Dashed,Circle[{0,0},2]},
 {Black,Thick,Arrow[{{0,0},{3,4}}]},
 {GrayLevel[.5],Thick,Arrow[{{0,0},gc}]},
 {Black,PointSize[.018],Point[{{3,4},gc}]},
 Text[Style["g=(3,4), ‖g‖=5",14],{2.15,4.55}],
 Text[Style["clipped=(6/5,8/5)",14],{2.45,2.55}],
 Text[Style["τ=2",14],{-1.3,-2.35}]},
 Frame->True,Axes->False,LabelStyle->Directive[FontSize->14],FrameLabel->{"g₁","g₂"},
 PlotRange->{{-2.5,5},{-3,5}},AspectRatio->.85,ImageSize->350,
 PlotLabel->Style["B. Norm clipping",17,Bold]];

decay=Graphics[{
 {GrayLevel[.35],Thick,Line[{{181/100,0},{183/100,0}}]},
 {Black,PointSize[.025],Point[{181/100,0}]},
 {GrayLevel[.25],PointSize[.025],Point[{183/100,0}]},
 {GrayLevel[.3],Thin,
   Line[{{181/100,0},{1.804,-.33}}],
   Line[{{183/100,0},{1.838,.29}}]},
 Text[Style["decoupled 181/100",14],{1.807,-.46}],
 Text[Style["coupled 183/100",14],{1.832,.45}],
 Text[Style["difference = 1/50",14],{1.82,.77}]},
 Frame->True,Axes->False,LabelStyle->Directive[FontSize->14],FrameLabel->{"next θ",""},
 FrameTicks->{{None,None},{{1.80,"1.80"},{1.81,"1.81"},
    {1.82,"1.82"},{1.83,"1.83"},{1.84,"1.84"}},None},
 PlotRange->{{1.795,1.845},{-.7,.94}},AspectRatio->.85,
 ImageSize->350,PlotLabel->Style["C. Adaptive decay",17,Bold]];

fig=Graphics[{Inset[gd,{350,825},Center,{610,280}],
 Inset[clip,{350,495},Center,{610,280}],
 Inset[decay,{350,165},Center,{610,280}]},
 PlotRange->{{0,700},{0,990}},ImageSize->{700,990},ImagePadding->0];

Export["figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.2.png",fig,"PNG"];
fig
