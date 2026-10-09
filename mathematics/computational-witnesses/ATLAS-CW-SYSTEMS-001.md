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

## W10. Constructive ring collective and placement replay

The earlier replay checks aggregate formulas. This control also executes the
actual **six synchronous ring communication steps**, including integer
reduce-scatter additions and all-gather copies. It checks that every rank
recovers the same eight-element sum under either logical ring order, while
computing cross-node traffic from the ordered directed messages rather than
from pre-entered edge counts.

Each rank's input depends on its fixed *name*, not its position in the ring.
The example uses exact integers so floating-point reassociation and rounding
cannot affect the logical collective test. All messages are assumed reliably
delivered in each synchronous step; this is **not** a network performance
simulation.

    from collections import defaultdict
    from fractions import Fraction

    names = ("A0", "A1", "B0", "B1")
    inputs = {
        name: tuple(100 * rank + j for j in range(8))
        for rank, name in enumerate(names)
    }
    expected = tuple(sum(inputs[name][j] for name in names)
                     for j in range(8))
    assert expected == (600, 604, 608, 612, 616, 620, 624, 628)

    def replay_ring(ring):
        p = len(ring)
        n = len(inputs[ring[0]])
        assert p == 4 and n == 8 and n % p == 0
        chunk_scalars = n // p
        chunk_bytes = 4 * chunk_scalars
        state = [
            [list(inputs[name][c * chunk_scalars:(c + 1) * chunk_scalars])
             for c in range(p)]
            for name in ring
        ]
        sent = [0] * p
        received = [0] * p
        additions = [0] * p
        traffic = defaultdict(int)

        for phase in ("reduce_scatter", "all_gather"):
            for step in range(p - 1):
                before = [[chunk[:] for chunk in row] for row in state]
                for rank in range(p):
                    prev = (rank - 1) % p
                    send_chunk = ((rank - step) % p
                                  if phase == "reduce_scatter"
                                  else (rank + 1 - step) % p)
                    recv_chunk = ((rank - step - 1) % p
                                  if phase == "reduce_scatter"
                                  else (rank - step) % p)
                    assert (prev - step) % p == recv_chunk if phase == "reduce_scatter" else (prev + 1 - step) % p == recv_chunk
                    arriving = before[prev][recv_chunk]
                    if phase == "reduce_scatter":
                        state[rank][recv_chunk] = [
                            x + y for x, y
                            in zip(before[rank][recv_chunk], arriving)
                        ]
                        additions[rank] += chunk_scalars
                    else:
                        state[rank][recv_chunk] = arriving[:]
                    sent[rank] += chunk_bytes
                    received[rank] += chunk_bytes
                    traffic[(ring[rank], ring[(rank + 1) % p])] += chunk_bytes

        result = [tuple(v for chunk in row for v in chunk) for row in state]
        assert all(row == expected for row in result)
        assert sent == received == [48, 48, 48, 48]
        assert additions == [6, 6, 6, 6]
        assert sum(traffic.values()) == 192
        assert len(traffic) == 4
        assert all(v == 48 for v in traffic.values())
        crossing = sum(
            byte_count for (src, dst), byte_count in traffic.items()
            if src[0] != dst[0]
        )
        return crossing, result

    grouped_cross, grouped_values = replay_ring(
        ("A0", "A1", "B0", "B1")
    )
    interleaved_cross, interleaved_values = replay_ring(
        ("A0", "B0", "A1", "B1")
    )
    assert grouped_values == interleaved_values
    assert (grouped_cross, interleaved_cross) == (96, 192)
    assert (Fraction(grouped_cross, 16),
            Fraction(interleaved_cross, 16)) == (6, 12)
    print("SYSTEMS_CONSTRUCTIVE_RING_REPLAY_OK")

Expected output:

    SYSTEMS_CONSTRUCTIVE_RING_REPLAY_OK

The modeled cut-capacity lower bounds remain **6 and 12 time units**.
Correct logical all-reduce values and per-edge byte counts do not establish
observed device latency, a real network topology, or fault tolerance.

## Claim boundary

This witness proves only exact arithmetic and byte accounting for the declared four-rank ring model and its two placements. The bandwidth calculation is a toy cut-capacity lower bound, not measured latency. It does not model protocol overhead, bidirectional link details, overlap, congestion control, routing, synchronization, device kernels, or vendor interconnect behavior.
