(* ATLAS-FIG-TRANSFORMER-001 — baseline block, causal mask, topology families *)

block=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{0,.3},{1.1,1.15}],
  Rectangle[{1.8,.3},{3.0,1.15}],
  Rectangle[{3.7,.3},{5.1,1.15}],
  Rectangle[{5.8,.3},{7.0,1.15}],
  Rectangle[{7.7,.3},{9.1,1.15}],
  Text[Style["H",12,Bold],{.55,.72}],
  Text[Style["LN",11,Bold],{2.4,.72}],
  Text[Style["MHA",11,Bold],{4.4,.72}],
  Text[Style["LN",11,Bold],{6.4,.72}],
  Text[Style["FFN",11,Bold],{8.4,.72}],
  Arrow[{{1.1,.72},{1.8,.72}}],
  Arrow[{{3.0,.72},{3.7,.72}}],
  Arrow[{{5.1,.72},{5.8,.72}}],
  Arrow[{{7.0,.72},{7.7,.72}}],
  Arrow[{{9.1,.72},{9.75,.72}}],
  Arrow[{{.55,1.15},{.55,1.75},{5.45,1.75},{5.45,.72}}],
  Arrow[{{5.45,.72},{5.45,-.35},{9.55,-.35},{9.55,.72}}],
  Text[Style["residual add",10],{5.45,2.02}],
  Text[Style["residual add",10],{7.5,-.62}],
  Text[Style["pre-LN block",12,Italic],{4.7,-1.02}]
 },PlotRange->{{-.4,10.1},{-1.25,2.35}},ImageSize->450,
 PlotLabel->Style["Residual stream anatomy",15,Bold]];

cells=Flatten@Table[
 {
  EdgeForm[Black],
  FaceForm[If[j<=i,White,GrayLevel[.9]]],
  Rectangle[{j-1,3-i},{j,4-i}],
  Text[
   Style[
    If[j<=i,
      Which[i==1&&j==1,"1",i==2,"1/2",i==3,"1/3"],
      "0"
    ],
    12,
    If[j>i,GrayLevel[.4],Black]
   ],
   {j-.5,3.5-i}
  ]
 },
 {i,1,3},{j,1,3}
];

mask=Graphics[{
  cells,
  Text[Style["query row i",10],{-1.0,1.5}],
  Text[Style["key/value column j",10],{1.5,3.45}],
  Text[Style["future entries exactly zero",11,Italic],{1.5,-.45}],
  Text[Style["A =",12,Bold],{-.55,1.5}]
 },PlotRange->{{-1.55,3.35},{-.8,3.8}},ImageSize->360,
 PlotLabel->Style["Ideal causal mixing matrix",15,Bold]];

topology=Graphics[{
  EdgeForm[Black],FaceForm[White],
  Rectangle[{0,2.2},{2.3,3.2}],
  Text[Style["Encoder-only",11,Bold],{1.15,2.7}],
  Text[Style["self-attention",9],{1.15,2.42}],
  Rectangle[{0,.6},{2.3,1.6}],
  Text[Style["Decoder-only",11,Bold],{1.15,1.1}],
  Text[Style["causal self-attention",9],{1.15,.82}],
  Rectangle[{4,2.2},{6.2,3.2}],
  Rectangle[{4,.6},{6.2,1.6}],
  Text[Style["Encoder",11,Bold],{5.1,2.7}],
  Text[Style["Decoder",11,Bold],{5.1,1.1}],
  Arrow[{{5.1,2.2},{5.1,1.6}}],
  Text[Style["cross-attention memory",9],{5.1,1.9}],
  Text[Style["three topology families",11,Italic],{3.05,-.05}]
 },PlotRange->{{-.4,6.6},{-.4,3.6}},ImageSize->380,
 PlotLabel->Style["Transformer topologies",15,Bold]];

GraphicsGrid[{{block,mask,topology}},Spacings->{14,5},ImageSize->1240]
