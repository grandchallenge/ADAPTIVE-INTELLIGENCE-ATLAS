(* ATLAS-FIG-ARCHHIST-001 — structural lineage from layered composition to residual transport *)

panel1=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Table[Rectangle[{i*1.6,0},{i*1.6+1.1,1}],{i,0,3}],
  Arrow[{{1.1,.5},{1.6,.5}}],
  Arrow[{{2.7,.5},{3.2,.5}}],
  Arrow[{{4.3,.5},{4.8,.5}}],
  Text[Style["x0",11,Bold],{.55,.5}],
  Text[Style["F0",11,Bold],{2.15,.5}],
  Text[Style["F1",11,Bold],{3.75,.5}],
  Text[Style["F2",11,Bold],{5.35,.5}],
  Text[Style["composition",11,Italic],{2.95,-.45}]
 },PlotRange->{{-.25,6.2},{-.8,1.5}},ImageSize->350,
 PlotLabel->Style["Layered maps",14,Bold]];

panel2=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Table[Rectangle[{i*.95,0},{i*.95+.65,.65}],{i,0,4}],
  Table[Text[Style[ToString[i],10],{i*.95+.325,.325}],{i,0,4}],
  Directive[Black,Thick],
  Line[{{.2,1.25},{3.9,1.25}}],
  Table[Line[{{i*.95+.325,.65},{i*.95+.325,1.25}}],{i,0,4}],
  Text[Style["same local kernel reused",11,Italic],{2.1,1.58}],
  Text[Style["translation-structured operator",11],{2.1,-.42}]
 },PlotRange->{{-.3,4.55},{-.75,1.9}},ImageSize->350,
 PlotLabel->Style["Convolution",14,Bold]];

panel3=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{1.3,.1},{3.3,1.25}],
  Text[Style["state h_t",12,Bold],{2.3,.68}],
  Arrow[{{3.3,.68},{4.2,.68},{4.2,1.75},{2.3,1.75},{2.3,1.25}}],
  Arrow[{{.2,.68},{1.3,.68}}],
  Text[Style["x_t",11],{.05,.95}],
  Text[Style["shared F(theta)",11],{2.3,-.35}],
  Text[Style["persistent notebook",11,Italic],{2.3,2.05}]
 },PlotRange->{{-.35,4.65},{-.7,2.35}},ImageSize->350,
 PlotLabel->Style["Recurrence",14,Bold]];

panel4=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{0,.2},{1.5,1.2}],
  Rectangle[{2.2,.2},{3.4,1.2}],
  Rectangle[{4.1,.2},{5.6,1.2}],
  Text[Style["Encoder",11,Bold],{.75,.7}],
  Text[Style["z",13,Bold],{2.8,.7}],
  Text[Style["Decoder",11,Bold],{4.85,.7}],
  Arrow[{{1.5,.7},{2.2,.7}}],
  Arrow[{{3.4,.7},{4.1,.7}}],
  Text[Style["bounded interface",11,Italic],{2.8,-.32}]
 },PlotRange->{{-.3,5.9},{-.65,1.55}},ImageSize->350,
 PlotLabel->Style["Encoder-decoder",14,Bold]];

panel5=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{.2,.15},{1.3,1.0}],
  Rectangle[{3.8,.15},{5.0,1.0}],
  Text[Style["x",12,Bold],{.75,.58}],
  Text[Style["y",12,Bold],{4.4,.58}],
  Arrow[{{1.3,.75},{2.3,.75},{2.3,1.45},{3.8,1.45},{3.8,.8}}],
  Arrow[{{1.3,.35},{2.15,.35},{2.15,-.55},{3.8,-.55},{3.8,.3}}],
  Text[Style["T H(x)",10],{2.95,1.68}],
  Text[Style["C x",10],{2.95,-.78}],
  Text[Style["learned carry / transform gates",11,Italic],{2.6,-1.18}]
 },PlotRange->{{-.2,5.4},{-1.45,2.05}},ImageSize->350,
 PlotLabel->Style["Highway layer",14,Bold]];

panel6=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{.2,.15},{1.3,1.0}],
  Rectangle[{3.8,.15},{5.0,1.0}],
  Text[Style["x_k",12,Bold],{.75,.58}],
  Text[Style["x_{k+1}",12,Bold],{4.4,.58}],
  Arrow[{{1.3,.58},{3.8,.58}}],
  Arrow[{{1.3,.58},{2.3,1.45},{3.1,1.45},{3.8,.58}}],
  Text[Style["identity path",10],{2.55,.34}],
  Text[Style["F_k(x_k)",10],{2.7,1.72}],
  Text[Style["state + learned increment",11,Italic],{2.6,-.42}]
 },PlotRange->{{-.2,5.4},{-.75,2.05}},ImageSize->350,
 PlotLabel->Style["Residual block",14,Bold]];

GraphicsGrid[
 {{panel1,panel2,panel3},{panel4,panel5,panel6}},
 Spacings->{10,12},
 ImageSize->1120
]
