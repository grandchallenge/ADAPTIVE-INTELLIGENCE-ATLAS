# ATLAS-CW-ARCHHIST-001 — Architecture Structure Witness

**Chapter:** \`ATLAS-CH-ARCHHIST-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay three exact structural claims:

1. cyclic convolution commutes with cyclic translation;
2. a linear recurrent state has the declared closed form;
3. a residual linear block has Jacobian \(I+A\) and becomes exact identity when its branch vanishes.

## Circular convolution witness

Use

\[
S=
\begin{pmatrix}
0&0&0&1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix},
\]

and

\[
C=I+2S.
\]

Then

\[
CS-SC=0.
\]

For

\[
x=(1,2,3,4),
\]

Wolfram gives

\[
CSx=SCx=(10,9,4,7).
\]

## Recurrent witness

Use

\[
a=\frac12,
\quad
b=2,
\quad
h_0=1,
\quad
(x_0,x_1,x_2)=(3,-1,4).
\]

Direct recurrence gives

\[
\left(
h_0,h_1,h_2,h_3
\right)
=
\left(
1,
\frac{13}{2},
\frac54,
\frac{69}{8}
\right).
\]

The closed form independently gives

\[
h_3=\frac{69}{8}.
\]

## Highway witness

Use scalar state

\[
x=2,
\qquad
H(x)=5.
\]

With tied transform/carry gates

\[
T=\frac14,
\qquad
C=1-T=\frac34,
\]

the layer returns

\[
y
=
T H(x)+C x
=
\frac{11}{4}.
\]

The exact carry limit

\[
T=0,
\qquad
C=1
\]

returns

\[
y=x=2.
\]

The exact transform limit

\[
T=1,
\qquad
C=0
\]

returns

\[
y=H(x)=5.
\]

## Residual witness

For

\[
A=
\begin{pmatrix}
1&2\\
-1&3
\end{pmatrix},
\]

the residual block

\[
x\mapsto x+Ax
\]

has exact Jacobian

\[
I+A
=
\begin{pmatrix}
2&2\\
-1&4
\end{pmatrix}.
\]

With zero residual branch,

\[
A=0,
\]

the Jacobian is exactly

\[
I.
\]

## Replay expression

\`\`\`wolfram
ss={{
  0,0,0,1
 },{
  1,0,0,0
 },{
  0,1,0,0
 },{
  0,0,1,0
}};

cc=IdentityMatrix[4]+2 ss;
xx={1,2,3,4};

a=1/2;
b=2;
h0=1;
xs={3,-1,4};

hs=
 FoldList[
  a #1+b #2&,
  h0,
  xs
 ];

closed=
 FullSimplify[
  a^Length[xs] h0
  +
  b Sum[
    a^(Length[xs]-1-j)
    xs[[j+1]],
    {j,0,Length[xs]-1}
  ]
 ];

xHighway=2;
hHighway=5;
tGate=1/4;
cGate=1-tGate;
highway=tGate hHighway+cGate xHighway;
highwayCarry=0 hHighway+1 xHighway;
highwayTransform=1 hHighway+0 xHighway;

aa={{
  1,2
 },{
  -1,3
}};

{
 cc.ss-ss.cc,
 cc.ss.xx,
 ss.cc.xx,
 hs,
 closed,
 highway,
 highwayCarry,
 highwayTransform,
 IdentityMatrix[2]+aa,
 IdentityMatrix[2]
}
\`\`\`

## Claim boundary

The convolution witness is for periodic circular convolution.

The recurrence witness is one scalar linear state model.

The residual witness establishes identity transport and \(I+A\) algebra only.

None of these finite witnesses establishes universal training superiority or the full behavior of practical CNNs, LSTMs, encoder-decoders, or ResNets.
