# ATLAS-CW-SYSTEMS-001 — Exact Placement and Communication Witness

**Chapter:** ATLAS-CH-SYSTEMS-001

## W1. Declared system

Ranks:

\[
R=\{A_0,A_1,B_0,B_1\}.
\]

Physical nodes:

- node A contains \(A_0,A_1\);
- node B contains \(B_0,B_1\).

Each rank holds an 8-element FP32 vector.

Declared vector bytes:

\[
S=8\cdot4=32.
\]

The collective is sum all-reduce implemented by a four-rank ring reduce-scatter followed by ring all-gather.

## W2. Collective semantics

For local vectors \(x_r\), every rank must finish with:

\[
y=\sum_{r\in R}x_r.
\]

The witness compares physical placements of the same ring algorithm.

It does not compare mathematical outputs.

## W3. Per-rank communication

Number of ranks:

\[
p=4.
\]

Chunk bytes:

\[
S/p=8.
\]

Ring phases:

- reduce-scatter: \(p-1=3\) sends;
- all-gather: \(p-1=3\) sends.

Therefore each rank sends:

\[
6\cdot8=48\ \text{bytes}
\]

and receives the same amount.

## W4. Reduction arithmetic

Chunk scalars:

\[
8/4=2.
\]

Each rank reduces one chunk in each of three reduce-scatter steps:

\[
3\cdot2=6
\]

scalar additions per rank.

Aggregate:

\[
4\cdot6=24
\]

scalar additions.

## W5. Grouped ring

Logical ring:

\[
A_0\to A_1\to B_0\to B_1\to A_0.
\]

Cross-node directed edges:

- \(A_1\to B_0\);
- \(B_1\to A_0\).

Each ring edge carries 48 bytes over the full collective.

Therefore:

\[
Q_{\mathrm{cut}}^G=96\ \text{bytes}.
\]

## W6. Interleaved ring

Logical ring:

\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]

All four directed ring edges cross the node cut.

Therefore:

\[
Q_{\mathrm{cut}}^I=192\ \text{bytes}.
\]

## W7. Equal-work control

Both placements have exactly:

- 6 additions/rank;
- 24 aggregate additions;
- 48 bytes sent/rank;
- 48 bytes received/rank;
- identical all-reduce result semantics.

But:

\[
Q_{\mathrm{cut}}^I/Q_{\mathrm{cut}}^G=2.
\]

Thus equal arithmetic and equal per-rank byte volume do not imply equal physical cross-cut traffic.

## W8. Toy latency lower bound

Declare a shared cross-node cut capacity:

\[
B_{\mathrm{cut}}=16\ \text{bytes/time-unit}.
\]

Then:

\[
T_G\ge96/16=6,
\]

\[
T_I\ge192/16=12.
\]

These are cut-capacity lower bounds under the toy model.

They are not hardware measurements.

## W9. Minimal replay code

    p = 4
    n = 8
    scalar_bytes = 4
    S = n * scalar_bytes
    chunk = S // p
    phases = 2 * (p - 1)
    bytes_per_rank = phases * chunk
    adds_per_rank = (p - 1) * (n // p)

    grouped_cross_edges = 2
    interleaved_cross_edges = 4

    q_grouped = grouped_cross_edges * bytes_per_rank
    q_interleaved = interleaved_cross_edges * bytes_per_rank

    assert S == 32
    assert chunk == 8
    assert phases == 6
    assert bytes_per_rank == 48
    assert adds_per_rank == 6
    assert p * adds_per_rank == 24
    assert q_grouped == 96
    assert q_interleaved == 192
    assert q_interleaved == 2 * q_grouped

    B_cut = 16
    t_grouped_lb = q_grouped / B_cut
    t_interleaved_lb = q_interleaved / B_cut

    assert t_grouped_lb == 6
    assert t_interleaved_lb == 12

    print("SYSTEMS_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only exact arithmetic and byte accounting for the declared four-rank ring model and its two placements. The bandwidth calculation is a toy cut-capacity lower bound, not measured latency. It does not model protocol overhead, bidirectional link details, overlap, congestion control, routing, synchronization, device kernels, or vendor interconnect behavior.
