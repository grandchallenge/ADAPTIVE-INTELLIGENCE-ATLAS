# HARDWARE-001 Derivations — Work, Data Movement, and Roofline Bounds

## 1. Declared FLOP count

Consider

\[
C=AB
\]

for two \(2\times2\) matrices.

Each of the four output entries is

\[
c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}.
\]

Under the chapter's declared scalar-operation convention, each output uses:

- two multiplications;
- one addition.

Therefore

\[
W
=
4(2+1)
=
12
\]

FLOPs.

This convention is deliberately explicit.

Other performance literature may count fused multiply-add instructions differently. The chapter does not mix conventions within one comparison.

## 2. Traffic model A: no cross-output input reuse

Assume:

- each output entry loads the four scalar input values it needs;
- no input load is reused across different outputs;
- each output scalar is stored once;
- no write-allocate, cache-line overfetch, metadata, instruction fetch, or coherence traffic is charged;
- every scalar is FP32, so each charged scalar transfer is \(4\) bytes.

For four outputs:

- input loads:
  \[
  4\ \text{outputs}\times4\ \text{scalars}
  =
  16;
  \]
- output stores:
  \[
  4.
  \]

Total charged scalar transfers:

\[
20.
\]

Therefore

\[
Q_A
=
20\times4
=
80
\]

bytes.

Arithmetic intensity is

\[
I_A
=
\frac{12}{80}
=
\frac{3}{20}
=
0.15
\]

FLOP/byte.

## 3. Traffic model B: perfect full-input reuse

Now assume:

- each of the four entries of \(A\) is loaded once;
- each of the four entries of \(B\) is loaded once;
- all loaded values remain available while all four outputs are computed;
- each output scalar is stored once;
- the same exclusions as in model A apply.

Then:

- input loads:
  \[
  4+4=8;
  \]
- output stores:
  \[
  4.
  \]

Total charged scalar transfers:

\[
12.
\]

Therefore

\[
Q_B
=
12\times4
=
48
\]

bytes.

Arithmetic intensity is

\[
I_B
=
\frac{12}{48}
=
\frac14
=
0.25
\]

FLOP/byte.

## 4. Same mathematics, different intensity

The matrix product \(C=AB\) and the declared arithmetic work \(W=12\) are identical in both cases.

Only the declared data-movement model changes.

Yet

\[
I_B>I_A.
\]

Specifically,

\[
\frac{I_B}{I_A}
=
\frac{1/4}{3/20}
=
\frac53.
\]

Thus perfect reuse raises arithmetic intensity by a factor of \(5/3\) under this accounting model.

This establishes the finite chapter claim:

\[
\boxed{
\text{same map + same FLOP count}
\not\Rightarrow
\text{same bytes moved}
}
\]

and therefore does not imply the same Roofline bandwidth bound.

## 5. Hypothetical Roofline machine

Declare a hypothetical machine with:

\[
P_{\max}
=
10\ \mathrm{TFLOP/s},
\]

and

\[
B
=
1\ \mathrm{TB/s}.
\]

The one-level Roofline bound is

\[
P
\le
\min(P_{\max},BI).
\]

The machine balance point is

\[
I^\star
=
\frac{P_{\max}}{B}
=
\frac{10\ \mathrm{TFLOP/s}}
{1\ \mathrm{TB/s}}
=
10\ \mathrm{FLOP/byte}.
\]

Both toy intensities are below \(10\), so both are on the bandwidth side of this declared one-level model.

For model A:

\[
BI_A
=
1\ \mathrm{TB/s}\times0.15\ \mathrm{FLOP/byte}
=
0.15\ \mathrm{TFLOP/s}.
\]

Therefore

\[
P_A
\le
0.15\ \mathrm{TFLOP/s}.
\]

For model B:

\[
BI_B
=
1\ \mathrm{TB/s}\times0.25\ \mathrm{FLOP/byte}
=
0.25\ \mathrm{TFLOP/s}.
\]

Therefore

\[
P_B
\le
0.25\ \mathrm{TFLOP/s}.
\]

No runtime is predicted.

The witness shows only that the bound changes when charged data movement changes.

## 6. Memory-bound versus compute-bound is boundary-relative

Let \(Q_M\) denote bytes crossing memory boundary \(M\).

Then

\[
I_M=\frac{W}{Q_M}.
\]

A cache, device-memory, or host-device boundary can produce different \(Q_M\) values for the same computation.

Therefore a workload can have different intensities at different hierarchy levels.

The statement

> this kernel is bandwidth-bound

is incomplete unless the model and relevant bandwidth boundary are identified.

## 7. Fusion accounting

Consider two elementwise maps:

\[
y=f(x),
\qquad
z=g(y).
\]

An unfused implementation may materialize \(y\) in a slower memory space.

A fused implementation may keep the intermediate in a register or another nearer storage level.

The mathematical composition remains

\[
z=(g\circ f)(x)
\]

only if the fused implementation preserves the declared semantics and required numerical tolerance.

Thus reduced traffic is a performance opportunity, not a proof of equivalence.

## 8. Precision accounting

Changing from a \(b_1\)-bit storage format to a \(b_2\)-bit format changes charged payload bytes in a declared storage model.

It does not by itself establish:

- an accuracy bound;
- a stability bound;
- an overflow/underflow bound;
- equivalence of accumulation behavior.

Those require numerical assumptions beyond byte count.

## 9. Scope

These derivations establish only:

- declared work/traffic accounting;
- arithmetic intensity;
- the classical one-level Roofline upper-bound algebra;
- exact separation between mathematical work and charged data movement.

They do not establish measured GPU performance, a universal memory hierarchy, or a universal kernel-optimization theorem.
