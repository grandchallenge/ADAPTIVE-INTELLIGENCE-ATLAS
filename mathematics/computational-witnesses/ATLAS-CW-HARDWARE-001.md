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

## Executable independent traffic/roofline replay

The following exact-rational Python replay computes the matrix product,
enumerates a naive *load trace* for all four output entries, counts unique
input locations under the declared ideal-reuse model, and checks bytes,
intensity and Roofline bandwidth-side upper bounds. A load-trace count is
an accounting model, not a hardware cache-traffic measurement.

    from fractions import Fraction as F

    A = ((1, 2), (3, 4))
    B = ((5, 6), (7, 8))
    product = tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(2))
              for j in range(2)) for i in range(2)
    )
    assert product == ((19, 22), (43, 50))

    a_reads = tuple(("A", i, k)
                    for i in range(2) for j in range(2) for k in range(2))
    b_reads = tuple(("B", k, j)
                    for i in range(2) for j in range(2) for k in range(2))
    all_reads = a_reads + b_reads
    output_stores = 4
    assert len(all_reads) == 16
    assert len(set(all_reads)) == 8
    assert output_stores == 4

    # Each of four outputs uses two multiplies and one addition.
    flops = 4 * (2 + 1)
    scalar_bytes = 4
    q_no_reuse = scalar_bytes * (len(all_reads) + output_stores)
    q_full_reuse = scalar_bytes * (len(set(all_reads)) + output_stores)
    assert (flops, q_no_reuse, q_full_reuse) == (12, 80, 48)

    i_no_reuse = F(flops, q_no_reuse)
    i_full_reuse = F(flops, q_full_reuse)
    assert i_no_reuse == F(3, 20)
    assert i_full_reuse == F(1, 4)
    assert i_full_reuse / i_no_reuse == F(5, 3)

    # TFLOP/s and TB/s units are consistent (both powers of 10^12).
    compute_roof = F(10)
    bandwidth = F(1)
    roof_a = min(compute_roof, bandwidth * i_no_reuse)
    roof_b = min(compute_roof, bandwidth * i_full_reuse)
    assert roof_a == F(3, 20)
    assert roof_b == F(1, 4)

    print("HARDWARE_EXACT_TRAFFIC_REPLAY_OK")

Expected output:

    HARDWARE_EXACT_TRAFFIC_REPLAY_OK

The computation verifies the declared **FLOP/byte accounting**, not actual
memory requests, device-cache behavior, measured kernel throughput or latency.

## Claim boundary

This witness proves only the following finite statement under its declared accounting convention:

> identical mathematical work and identical declared FLOP count can coexist with different charged data movement and therefore different arithmetic intensity and Roofline bandwidth bounds.

It does not prove that a particular GPU reaches either bound, that cache behavior realizes either traffic model, or that reuse always improves end-to-end performance by \(5/3\).
