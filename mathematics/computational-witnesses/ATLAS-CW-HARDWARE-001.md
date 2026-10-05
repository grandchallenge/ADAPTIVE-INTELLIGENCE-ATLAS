# ATLAS-CW-HARDWARE-001 — Equal FLOPs, Different Data Movement

## Purpose

Give one exact finite example in which:

- the mathematical operation is unchanged;
- the declared floating-point operation count is unchanged;
- the declared byte traffic changes because reuse changes;
- the resulting Roofline bandwidth bound changes.

This is an accounting witness, not a benchmark.

## Mathematical operation

Let

\[
A=
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
5&6\\
7&8
\end{pmatrix}.
\]

Then

\[
C=AB
=
\begin{pmatrix}
19&22\\
43&50
\end{pmatrix}.
\]

Under the declared scalar FLOP convention:

- each output uses 2 multiplications and 1 addition;
- there are 4 outputs.

Therefore:

\[
W=12\ \text{FLOPs}.
\]

## Traffic model A — no cross-output input reuse

For each of the four output elements, charge:

- 4 input scalar loads;
- 1 output scalar store.

Total:

\[
16\ \text{input loads}
+
4\ \text{stores}
=
20\ \text{scalar transfers}.
\]

At 4 bytes per FP32 scalar:

\[
Q_A=80\ \text{bytes}.
\]

Therefore:

\[
I_A
=
\frac{12}{80}
=
0.15\ \text{FLOP/byte}.
\]

## Traffic model B — perfect full-input reuse

Charge:

- 4 loads for all entries of \(A\);
- 4 loads for all entries of \(B\);
- 4 stores for all entries of \(C\).

Total:

\[
12\ \text{scalar transfers}.
\]

Therefore:

\[
Q_B=48\ \text{bytes}.
\]

and

\[
I_B
=
\frac{12}{48}
=
0.25\ \text{FLOP/byte}.
\]

## Exact comparison

Both models compute exactly:

\[
AB
=
\begin{pmatrix}
19&22\\
43&50
\end{pmatrix}.
\]

Both charge exactly:

\[
12\ \text{FLOPs}.
\]

But:

\[
Q_A=80\neq48=Q_B.
\]

Therefore:

\[
I_A=0.15
\neq
0.25=I_B.
\]

The intensity improvement is:

\[
\frac{I_B}{I_A}
=
\frac53.
\]

## Hypothetical Roofline replay

Declare:

\[
P_{\max}=10\ \mathrm{TFLOP/s},
\qquad
B=1\ \mathrm{TB/s}.
\]

Then:

\[
P_A
\le
\min(10,0.15)
=
0.15\ \mathrm{TFLOP/s},
\]

while:

\[
P_B
\le
\min(10,0.25)
=
0.25\ \mathrm{TFLOP/s}.
\]

The same exact matrix product and the same declared FLOPs therefore receive different bandwidth-side Roofline bounds under the two declared traffic models.

## What is deliberately excluded

The traffic model does not charge:

- cache-line overfetch;
- write allocate;
- coherence;
- instruction fetch;
- address-generation traffic;
- metadata;
- host-device copies;
- launch overhead;
- synchronization overhead.

It also assumes perfect retention in the reuse case.

Those exclusions are part of the witness definition.

The example therefore should not be compared numerically to measured GPU runtime.

## Claim boundary

This witness proves only the following finite statement under its declared accounting convention:

> identical mathematical work and identical declared FLOP count can coexist with different charged data movement and therefore different arithmetic intensity and Roofline bandwidth bounds.

It does not prove that a particular GPU reaches either bound, that cache behavior realizes either traffic model, or that reuse always improves end-to-end performance by \(5/3\).
