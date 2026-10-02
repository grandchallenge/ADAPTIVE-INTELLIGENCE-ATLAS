(* ATLAS-FIG-REPLAY-001 — Evidence path and separate authority transition *)
ClearAll["Global`*"];

evidenceNodes = {
  "Source", "Method", "Execution", "Observation", "Interpretation", "Claim"
};
evidenceEdges = Thread[
  DirectedEdge[evidenceNodes[[;; -2]], evidenceNodes[[2 ;;]]]
];
authorityNodes = {"Review / replay", "Adjudication", "Certification"};
authorityEdges = {
  DirectedEdge["Claim", "Review / replay"],
  DirectedEdge["Review / replay", "Adjudication"],
  DirectedEdge["Adjudication", "Certification"]
};

coords = <|
  "Source" -> {0, 1},
  "Method" -> {2, 1},
  "Execution" -> {4, 1},
  "Observation" -> {6, 1},
  "Interpretation" -> {8, 1},
  "Claim" -> {10, 1},
  "Review / replay" -> {10, -1},
  "Adjudication" -> {7, -1},
  "Certification" -> {4, -1}
|>;

ev = Graph[
  Join[evidenceNodes, authorityNodes],
  Join[evidenceEdges, authorityEdges],
  VertexCoordinates -> coords,
  VertexLabels -> Placed["Name", Center],
  VertexShapeFunction -> "Rectangle",
  VertexSize -> {0.18, 0.09},
  EdgeStyle -> Join[
    Thread[evidenceEdges -> Directive[Black, Thick]],
    Thread[authorityEdges -> Directive[GrayLevel[0.35], Dashed, Thick]]
  ],
  VertexStyle -> {
    "Source" -> White, "Method" -> White, "Execution" -> White,
    "Observation" -> White, "Interpretation" -> White, "Claim" -> White,
    "Review / replay" -> GrayLevel[0.9],
    "Adjudication" -> GrayLevel[0.9],
    "Certification" -> GrayLevel[0.9]
  },
  GraphLayout -> "None",
  ImagePadding -> 35,
  PlotRangePadding -> Scaled[0.08],
  ImageSize -> 1100
];

Labeled[
  ev,
  Style[
    "Solid arrows: evidence / derivation path     Dashed arrows: governed review / authority transitions",
    14
  ],
  Bottom
]
