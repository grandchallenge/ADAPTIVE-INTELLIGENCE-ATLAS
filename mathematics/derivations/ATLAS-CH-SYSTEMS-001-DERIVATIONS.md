# ATLAS-CH-SYSTEMS-001 — Derivation Packet

## D1. Typed distributed system

Write

\[
\mathcal S=(R,\Pi,\Gamma,\mathcal C,\mathcal M,\mathcal Q,\mathcal P).
\]

The coordinates respectively denote ranks/devices, typed parallelism, physical topology, communication semantics, memory state, scheduling/request state, and measurement protocol.

They are not interchangeable.

## D2. Synchronous data-parallel update

For ranks \(r=0,\ldots,p-1\), let \(g_r\) be each local gradient.

A declared average-gradient synchronization is

\[
\bar g=\frac1p\sum_r g_r.
\]

If every replica begins from the same parameter state and applies the same deterministic update from \(\bar g\), replica equality is preserved for that step.

This statement depends on the declared synchronization/update semantics. It is not a statement about asynchronous data parallelism.

## D3. Tensor-parallel interface

Let one operator \(F\) be decomposed into local pieces

\[
F(x)=\operatorname{Combine}(F_0(x_0),\ldots,F_{p-1}(x_{p-1})).
\]

The partition \(x\mapsto(x_0,\ldots,x_{p-1})\), the local maps, and Combine must all be declared.

Therefore a tensor-parallel degree alone does not determine communication.

## D4. Pipeline state

Let stages be \(S_1,\ldots,S_k\) and microbatches \(m_1,\ldots,m_b\).

A schedule is a partial order over stage/microbatch execution events plus required activation/gradient transfers.

The pipeline bubble is idle stage-time induced by fill, drain, dependencies, or imbalance under that schedule.

Hence stage count alone does not determine utilization.

## D5. Expert-parallel interface

From MOE-001:

- \(p_{i,e}\): router probability;
- \(P_i\): preferred route;
- \(a_{i,e}\): accepted dispatch;
- \(\operatorname{dev}(e)\): expert placement.

SYSTEMS adds physical path

\[
\operatorname{path}(\operatorname{src}(i),\operatorname{dev}(e);\Gamma).
\]

Thus routing preference, accepted dispatch, placement, and network path are four distinct objects.

## D6. Collective semantics

For rank-local vectors \(x_r\), all-reduce with sum returns

\[
y_r=\sum_j x_j
\]

to every rank \(r\).

Reduce-scatter returns a declared partition of the reduced vector.

All-gather returns all declared partitions to every rank.

All-to-all maps rank-specific payloads \(x_{r\to s}\) from every source \(r\) to every destination \(s\).

These equalities specify result semantics, not the communication algorithm.

## D7. Ring all-reduce byte accounting

Let:

- rank count \(p=4\);
- vector length \(n=8\) FP32 scalars;
- total vector bytes \(S=4n=32\).

Split the vector into \(p\) equal chunks.

Chunk bytes:

\[
S/p=8.
\]

A ring reduce-scatter uses \(p-1=3\) communication steps.

A ring all-gather uses another \(3\) steps.

Each rank sends one chunk each step, therefore:

\[
Q_{\mathrm{send/rank}}
=
2(p-1)S/p
=
2(3)(32)/4
=
48\ \text{bytes}.
\]

The same amount is received.

## D8. Ring reduction arithmetic

Each rank reduces one received chunk in each of the three reduce-scatter steps.

Each chunk contains

\[
n/p=2
\]

scalars.

Thus additions per rank are

\[
(p-1)n/p=3\cdot2=6.
\]

Aggregate reduction additions are

\[
4\cdot6=24.
\]

The all-gather adds no reduction arithmetic.

## D9. Grouped physical placement

Place \(A_0,A_1\) on node A and \(B_0,B_1\) on node B.

Logical ring:

\[
A_0\to A_1\to B_0\to B_1\to A_0.
\]

Cross-node edges are:

\[
A_1\to B_0,
\qquad
B_1\to A_0.
\]

Every directed ring edge carries 48 bytes over the complete collective.

Therefore:

\[
Q_{\mathrm{cut}}^G=2\cdot48=96\ \text{bytes}.
\]

## D10. Interleaved physical placement

Logical ring:

\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]

Every ring edge crosses the node cut.

Therefore:

\[
Q_{\mathrm{cut}}^I=4\cdot48=192\ \text{bytes}.
\]

## D11. Equal arithmetic control

Both placements have exactly:

- 6 additions per rank;
- 24 aggregate additions;
- 48 bytes sent per rank;
- 48 bytes received per rank.

Yet:

\[
Q_{\mathrm{cut}}^I=2Q_{\mathrm{cut}}^G.
\]

Therefore:

\[
\boxed{
\text{equal arithmetic and equal per-rank bytes}
\not\Rightarrow
\text{equal physical-cut traffic}.
}
\]

## D12. Modeled cut-capacity lower bound

Assume only for the toy model that all cross-node ring traffic shares a cut with aggregate capacity

\[
B_{\mathrm{cut}}=16\ \text{bytes/time-unit}.
\]

Any execution must satisfy:

\[
T\ge Q_{\mathrm{cut}}/B_{\mathrm{cut}}.
\]

Hence:

\[
T_G\ge96/16=6,
\]

\[
T_I\ge192/16=12.
\]

This is a lower bound induced by the declared cut model.

It is not measured wall-clock time and does not include launch, synchronization, overlap, protocol, routing, or device effects.

## D13. Scaling efficiency

For a fixed declared workload family and measurement protocol, define:

\[
\eta_p=
\frac{\mathrm{throughput}(p)}
{p\,\mathrm{throughput}(1)}.
\]

Values below one can reflect communication, idle time, imbalance, memory effects, or other overhead.

A change in global batch size or task semantics changes the comparison and must be disclosed.

## D14. Latency and throughput

For request \(i\):

\[
L_i=t_i^{\mathrm{complete}}-t_i^{\mathrm{arrival}}.
\]

System throughput over interval \([0,T]\) may be reported as completed requests or generated tokens divided by \(T\).

Neither quantity determines the other without workload/scheduling assumptions.

## D15. Tail behavior

Given latencies \(L_1,\ldots,L_N\), a percentile such as \(L_{0.99}\) is an order statistic.

The mean

\[
\bar L=\frac1N\sum_i L_i
\]

does not determine \(L_{0.99}\).

Thus average-latency claims cannot stand in for tail-latency claims.

## D16. Goodput

For service-level objective \(\tau\), one possible request goodput is

\[
G_\tau=
\frac{|\{i:L_i\le\tau\}|}{T}.
\]

High raw throughput can coexist with lower \(G_\tau\) if many requests miss the declared objective.

The exact goodput definition must be stated.

## D17. Generic KV-cache accounting

Let request \(i\) retain \(\ell_i\) token positions and let the implementation require \(b_i\) bytes of cache state per retained position.

Then:

\[
M_i=\ell_i b_i.
\]

Total retained cache is:

\[
M_{\mathrm{KV}}=\sum_i M_i.
\]

The value \(b_i\) depends on model architecture, precision, sharding, layout, and implementation.

## D18. Scheduling boundary

Autoregressive serving repeatedly revisits active requests as new tokens are generated.

A scheduler can choose which active requests participate in each iteration.

This creates a systems decision distinct from the model's arithmetic definition.

Orca is used only as a primary example of iteration-level scheduling and selective batching in one measured system.

## D19. Cache-management boundary

PagedAttention/vLLM is used as a primary example showing that KV-cache allocation/fragmentation can limit batch capacity and that a different memory-management design can improve measured serving performance in the reported setup.

No universal vLLM performance multiplier is imported into the Atlas.

## D20. Training versus serving

Training commonly optimizes sustained update throughput under declared synchronization and memory constraints.

Serving commonly optimizes a vector containing request/token throughput, latency distributions, SLO goodput, memory pressure, and availability.

Therefore:

\[
\boxed{
\text{training efficiency}
\neq
\text{serving efficiency}.
}
\]

## Durable propositions

1. Data, tensor, pipeline, and expert parallelism have distinct state/communication semantics.
2. Collective result semantics do not determine collective implementation.
3. Logical placement can alter physical cross-cut communication without changing arithmetic or per-rank communication volume.
4. A cut-capacity calculation is a model lower bound, not a runtime prediction.
5. Training scaling efficiency does not determine serving latency/throughput/tail behavior.
6. Router preference, accepted dispatch, physical placement, and network path are distinct.
7. KV-cache memory and scheduling are first-class serving-system state.
8. Benchmark claims require explicit workload, hardware, topology, policy, and metric scope.

## Claim boundary

This packet establishes only the declared definitions and finite accounting witness. It does not prove linear scaling, universal optimality of any parallelism decomposition, universal superiority of any collective algorithm, topology, serving scheduler, or KV-cache manager, or hardware-independent latency predictions.
