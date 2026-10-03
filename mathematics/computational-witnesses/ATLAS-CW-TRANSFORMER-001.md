# ATLAS-CW-TRANSFORMER-001 — Transformer Baseline Witness

**Chapter:** \`ATLAS-CH-TRANSFORMER-001\`  
**Runtime:** Wolfram Language service, 2026-10-03

## Purpose

Replay three exact architectural claims:

1. ideal causal masking removes future-value dependence;
2. two head outputs concatenate and recombine exactly through \(W_O\);
3. a zero residual branch leaves the residual-stream state unchanged.

## Causal witness

Use exact ideal causal mixing matrix

\[
A
=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
1/3&1/3&1/3
\end{pmatrix}.
\]

Original values:

\[
V=(2,5,11)^\top.
\]

Modified future value:

\[
V'=(2,5,101)^\top.
\]

Then

\[
AV
=
(2,7/2,6)^\top,
\]

and

\[
AV'
=
(2,7/2,36)^\top.
\]

The first two outputs are identical exactly.

## Multi-head output witness

Take

\[
O_1=(1,2),
\qquad
O_2=(3,4).
\]

Concatenation:

\[
C=(1,2,3,4).
\]

Let

\[
W_O
=
\begin{pmatrix}
1&0\\
0&1\\
1&1\\
2&-1
\end{pmatrix}.
\]

Then

\[
CW_O
=
(12,1).
\]

## Residual identity witness

Let

\[
H=(2,-1,3).
\]

With zero sublayer output,

\[
S(H)=(0,0,0),
\]

the residual update gives

\[
H+S(H)=H.
\]

## Replay expression

\`\`\`wolfram
a={{
  1,0,0
 },{
  1/2,1/2,0
 },{
  1/3,1/3,1/3
}};

v={2,5,11};
vp={2,5,101};

o1={1,2};
o2={3,4};
c=Join[o1,o2];

wo={{
  1,0
 },{
  0,1
 },{
  1,1
 },{
  2,-1
}};

h={2,-1,3};
zero={0,0,0};

{
 a.v,
 a.vp,
 Take[a.v,2],
 Take[a.vp,2],
 c.wo,
 h+zero
}
\`\`\`

Expected exact output:

\[
\{
(2,7/2,6),
(2,7/2,36),
(2,7/2),
(2,7/2),
(12,1),
(2,-1,3)
\}.
\]

## Claim boundary

The causal witness assumes the exact ideal mask and equal unmasked logits.

The multi-head witness checks concatenation/output projection only.

The residual witness checks the exact zero-branch identity limit only.

These finite witnesses do not establish training quality, semantic head specialization, or universal Transformer behavior.
