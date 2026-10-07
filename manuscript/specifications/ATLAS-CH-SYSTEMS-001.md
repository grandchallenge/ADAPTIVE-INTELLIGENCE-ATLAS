# Chapter Specification — ATLAS-CH-SYSTEMS-001

## Identity

**Title:** Scaling, Parallelism, and Serving  
**Part:** Agents, Polities, Hardware, and Systems  
**Status:** specification-ready.  
**Epistemic class:** audited Hardware and MoE prerequisites + primary distributed-training/serving systems sources + Atlas synthesis + exact finite communication witness.

## Contract

Develop the system layer between one-device execution and a deployed multi-device training or serving service.

The chapter must separately type:

- data parallelism;
- tensor parallelism;
- pipeline parallelism;
- expert parallelism;
- collective communication semantics;
- physical placement/topology;
- training efficiency;
- serving efficiency.

It must keep model arithmetic, communication, memory, scheduling, latency, throughput, utilization, and tail behavior separate.

## Hard prerequisites

- ATLAS-CH-HARDWARE-001.
- ATLAS-CH-MOE-001.

Exact prerequisite identities and source scopes are locked in:

sources/source-locks/ATLAS-CH-SYSTEMS-001.yaml

## Required distinctions

1. model FLOPs versus wall-clock time;
2. local arithmetic versus bytes communicated;
3. collective semantics versus collective algorithm;
4. logical parallelism topology versus physical network topology;
5. data versus tensor versus pipeline versus expert parallelism;
6. router preference versus accepted expert dispatch versus physical placement;
7. per-device bytes versus cross-cut bytes;
8. average latency versus tail latency;
9. throughput versus request latency;
10. utilization versus useful work;
11. training throughput/scaling efficiency versus serving efficiency;
12. model memory versus activation/KV-cache/runtime memory;
13. modeled communication lower bounds versus measured time;
14. batch size versus scheduling policy;
15. prefill-style work versus iterative decode-style work.

## Core objects

Let the distributed execution system be

\[
\mathcal S=(R,\Pi,\Gamma,\mathcal C,\mathcal M,\mathcal Q,\mathcal P).
\]

Here:

- \(R\) is the rank/device set;
- \(\Pi\) is a typed parallelism decomposition;
- \(\Gamma\) is the physical communication topology;
- \(\mathcal C\) is the collective/point-to-point communication semantics;
- \(\mathcal M\) is memory state and placement;
- \(\mathcal Q\) is the scheduling/request state;
- \(\mathcal P\) is the measurement protocol.

No coordinate is inferred from another.

## Data parallelism

For synchronous data parallelism with \(p\) replicas:

- each rank holds a declared parameter replica;
- each rank processes a declared data shard;
- each rank forms a local gradient \(g_r\);
- a synchronization operation forms a declared aggregate, for example

\[
\bar g=\frac1p\sum_{r=0}^{p-1}g_r;
\]

- replicas apply the same declared update after synchronization.

Parameter/optimizer sharding is an additional memory-layout choice and must not be silently identified with data parallelism itself.

## Tensor parallelism

A single operator is partitioned across ranks.

The specification must state:

- which tensor dimensions are partitioned;
- what local partial results are computed;
- what collective or point-to-point operation reconstitutes the next required state;
- where replicated state remains.

A tensor-parallel split can reduce per-rank model memory while increasing synchronization.

## Pipeline parallelism

An ordered computation is partitioned into stages.

Microbatches may occupy different stages concurrently.

The chapter must distinguish:

- stage partition;
- microbatch count;
- schedule;
- pipeline fill/drain;
- idle bubble;
- activation/gradient transfers;
- stage imbalance.

Pipeline utilization is schedule- and partition-dependent.

## Expert parallelism

Inherit from MOE-001:

- router probabilities/preferences;
- accepted dispatch;
- expert capacity;
- expert placement;
- communication proxies;
- straggler boundaries.

SYSTEMS adds physical topology and measured/modeled cost.

The chapter must preserve:

\[
\text{preferred route}
\neq
\text{accepted dispatch}
\neq
\text{physical path}.
\]

## Collective semantics

Define at minimum:

- all-reduce: every rank receives the reduction across all ranks;
- reduce-scatter: the reduction result is partitioned across ranks;
- all-gather: all partitions are gathered to every rank;
- all-to-all: each rank sends rank-specific payloads to other ranks.

These are value-movement semantics.

Ring, tree, hierarchical, topology-aware, and implementation-specific algorithms are separate choices.

## Topology

The chapter must name:

- nodes;
- devices/ranks;
- links or fabrics;
- bandwidth/latency model if one is used;
- contention/shared-cut assumptions;
- logical-to-physical placement.

A topology model is not a claim about one vendor interconnect unless a vendor source is explicitly locked.

## Training efficiency

Possible declared quantities include:

\[
\mathrm{throughput}(p)
\]

and strong-scaling efficiency

\[
\eta_p=
\frac{\mathrm{throughput}(p)}
{p\,\mathrm{throughput}(1)}.
\]

The baseline workload, batch semantics, precision, optimizer, hardware, and measurement region must remain fixed or the comparison must disclose the change.

## Serving efficiency

Serving requires separately declared:

- arrival process/workload;
- prompt/input length;
- generated/output length;
- batching/scheduling policy;
- KV-cache policy;
- replica/model placement;
- latency statistic;
- throughput or goodput definition;
- service-level objective if any.

The chapter must distinguish request latency from token throughput and average from tail behavior.

## KV-cache boundary

For a request \(i\), use a generic declared cache accounting model

\[
M_i=\ell_i b_i,
\]

where \(\ell_i\) is retained sequence state length and \(b_i\) is declared bytes of retained cache per token under the implementation.

The exact value of \(b_i\) is model-, precision-, layout-, and sharding-dependent.

The chapter must not universalize one implementation's cache layout.

## Exact finite placement/communication witness

Use four ranks:

\[
A_0,A_1,B_0,B_1
\]

with \(A_0,A_1\) on node A and \(B_0,B_1\) on node B.

Each rank begins an all-reduce over an 8-element FP32 vector:

\[
S=32\ \text{bytes}.
\]

Use a ring reduce-scatter plus all-gather with \(p=4\):

- chunk size \(S/p=8\) bytes;
- \(p-1=3\) reduce-scatter steps;
- \(p-1=3\) all-gather steps;
- 6 sends per rank;
- 48 bytes sent per rank;
- 48 bytes received per rank;
- 6 scalar additions per rank during reduce-scatter.

Compare two logical ring placements.

Grouped:

\[
A_0\to A_1\to B_0\to B_1\to A_0.
\]

Only two ring edges cross the node cut, so total directed cross-cut traffic over the full collective is

\[
Q_{\mathrm{cut}}^{G}=2\cdot48=96\ \text{bytes}.
\]

Interleaved:

\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]

All four ring edges cross the node cut, so:

\[
Q_{\mathrm{cut}}^{I}=4\cdot48=192\ \text{bytes}.
\]

Arithmetic and per-rank total collective bytes are unchanged.

Under a hypothetical shared node-cut bandwidth

\[
B_{\mathrm{cut}}=16\ \text{bytes/time-unit},
\]

the cut-capacity lower bounds are:

\[
T_G\ge 6,
\qquad
T_I\ge 12.
\]

This is an accounting/lower-bound witness, not a runtime prediction.

## Reader spine

1. The distributed system boundary.
2. Why more devices do not automatically mean proportionate speed.
3. Data parallelism.
4. Tensor parallelism.
5. Pipeline parallelism.
6. Expert parallelism.
7. Collective semantics.
8. Topology and placement.
9. Exact ring-placement witness.
10. Memory and communication.
11. Training scaling metrics.
12. Serving as a different systems problem.
13. Iterative scheduling and batching.
14. KV-cache pressure and memory management.
15. Latency, throughput, goodput, utilization, and tails.
16. Benchmark discipline.
17. Failure boundaries.

## Benchmark discipline

Training claims should identify at least:

- model/workload;
- global and per-device batch semantics;
- precision;
- optimizer/update semantics;
- device count/type;
- topology;
- parallelism degrees;
- activation/parameter/optimizer sharding;
- warmup and measurement window;
- throughput definition;
- scaling baseline;
- failure/restart behavior if relevant.

Serving claims should identify at least:

- model and precision;
- device count/type and topology;
- request length distribution;
- output length distribution;
- concurrency/arrival process;
- batch/scheduler;
- KV-cache policy;
- latency percentiles;
- throughput/goodput definition;
- service-level objective;
- measurement duration.

## Failure boundaries

- More devices do not imply linear speedup.
- Equal FLOPs do not imply equal communication.
- Equal total communicated bytes do not imply equal cross-cut traffic.
- Equal average latency does not imply equal tail latency.
- High throughput does not imply low request latency.
- High utilization does not imply useful-work efficiency.
- A collective semantic does not determine its algorithm or topology cost.
- Sparse expert arithmetic does not imply cheap expert communication.
- Training scaling results do not imply serving efficiency.
- Modeled communication cost is not measured runtime.
- A benchmark result is not a universal systems law.

## Sources

New primary systems sources are limited to:

- Narayanan et al. (2021), *Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM*.
- Huang et al. (2019), *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*.
- Yu et al. (2022), *Orca: A Distributed Serving System for Transformer-Based Generative Models*.
- Kwon et al. (2023), *Efficient Memory Management for Large Language Model Serving with PagedAttention*.

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-SYSTEMS-001.yaml
