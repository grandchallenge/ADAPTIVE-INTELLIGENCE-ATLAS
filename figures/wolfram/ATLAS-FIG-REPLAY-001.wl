(* ATLAS-FIG-REPLAY-001 — Evidence path and separate authority transition *)
ClearAll["Global`*"];

nodes = {
  {"Source", {0, 1}},
  {"Method", {2, 1}},
  {"Execution", {4, 1}},
  {"Observation", {6, 1}},
  {"Interpretation", {8, 1}},
  {"Claim", {10, 1}},
  {"Review / replay", {10, -1}},
  {"Adjudication", {7, -1}},
  {"Certification", {4, -1}}
};

box[{label_, {x_, y_}}, fill_] := {
  EdgeForm[Black], FaceForm[fill],
  Rectangle[{x - .72, y - .28}, {x + .72, y + .28}],
  Text[Style[label, 12], {x, y}]
};

Graphics[
  {
    Arrowheads[.025],
    Thick,
    Arrow[{{.72, 1}, {1.28, 1}}],
    Arrow[{{2.72, 1}, {3.28, 1}}],
    Arrow[{{4.72, 1}, {5.28, 1}}],
    Arrow[{{6.72, 1}, {7.28, 1}}],
    Arrow[{{8.72, 1}, {9.28, 1}}],
    Directive[GrayLevel[.35], Dashed, Thick],
    Arrow[{{10, .72}, {10, -.72}}],
    Arrow[{{9.28, -1}, {7.72, -1}}],
    Arrow[{{6.28, -1}, {4.72, -1}}],
    Directive[Black],
    Sequence @@ (box[#, White] & /@ Take[nodes, 6]),
    Sequence @@ (box[#, GrayLevel[.9]] & /@ Drop[nodes, 6]),
    Text[Style["evidence / derivation path", 13, Bold], {5, 1.65}],
    Text[
      Style["governed review / authority transitions", 13, Bold, GrayLevel[.3]],
      {7, -1.65}
    ],
    Text[Style["replay ≠ certification", 14, Bold], {1.6, -1}]
  },
  PlotRange -> {{-1, 11}, {-2.1, 2}},
  ImagePadding -> 30,
  ImageSize -> 1100
]
