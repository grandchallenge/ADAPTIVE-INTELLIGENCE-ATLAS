# Chapter Specification — ATLAS-CH-HARDWARE-001

## Identity

**Title:** The Machine Under the Mathematics  
**Part:** Agents, Polities, Hardware, and Systems  
**Status:** specification-ready.  
**Epistemic class:** audited Linear Algebra prerequisite + classical Roofline performance model + current authoritative CUDA documentation + Atlas synthesis.

## Contract

Develop the physical execution substrate behind the Atlas's mathematical objects:

- GPU-style parallel execution;
- memory hierarchy;
- matrix/tensor acceleration;
- arithmetic intensity;
- bandwidth;
- numerical precision;
- kernels and fusion;
- occupancy/resource constraints;
- benchmark methodology.

The chapter must explain why mathematically identical work can have materially different execution cost without turning vendor-specific implementation details into universal hardware laws.

## Hard prerequisite

- ATLAS-CH-LINALG-001.

Exact prerequisite identities and source scopes are locked in:

sources/source-locks/ATLAS-CH-HARDWARE-001.yaml

## Required distinctions

1. abstract operation count versus wall-clock time;
2. latency versus throughput;
3. compute throughput versus memory bandwidth;
4. arithmetic intensity versus raw FLOP count;
5. global/device memory versus cache/shared/register locality;
6. mathematical matrix multiplication versus hardware-supported matrix tiles;
7. precision format versus numerical accuracy;
8. occupancy/resource residency versus useful work;
9. kernel fusion versus semantic equivalence;
10. single-device kernel behavior versus downstream distributed-system behavior.

## Core objects

Let:

\[
W
\]

be a declared count of floating-point operations for a computation.

Let:

\[
Q_M
\]

be bytes transferred across a declared memory boundary \(M\).

Define arithmetic intensity at that boundary as

\[
I_M = \frac{W}{Q_M}.
\]

The subscript is mandatory when multiple hierarchy levels matter.

For a declared peak compute rate \(P_{\max}\) and bandwidth \(B_M\), the classical one-level Roofline bound is presented as

\[
P_{\mathrm{attainable}}
\le
\min(P_{\max}, B_M I_M).
\]

This is a performance upper-bound model, not a guarantee of attained runtime.

The balance point is

\[
I^\star_M = \frac{P_{\max}}{B_M}.
\]

Below that point the one-level model is bandwidth-limited; above it the model's compute roof is lower.

## Memory hierarchy

The reader chapter must distinguish conceptually:

- registers / thread-local fast storage;
- shared/on-chip programmer-managed storage where available;
- caches;
- device/global memory;
- host/system memory and transfer boundaries.

CUDA names are used only as a concrete programming-model example.

Claims about latency, bandwidth, exact capacities, or hierarchy shape must remain architecture-specific unless stated qualitatively.

## Parallel execution

The chapter may use CUDA warps/SIMT to explain:

- groups of threads executing one kernel;
- divergence and lane utilization;
- coalesced memory access;
- block-level shared memory;
- resource limits that influence resident work.

It must not equate SIMT with all GPU execution models.

## Matrix/tensor acceleration

The chapter must explain that specialized matrix hardware accelerates supported matrix-multiply-accumulate patterns under declared:

- tile shapes;
- operand/accumulator types;
- layouts;
- synchronization/execution conditions.

It must block the inference:

\[
\text{matrix operation}
\Rightarrow
\text{peak matrix-unit throughput}.
\]

## Precision

The chapter must separate:

- storage width;
- arithmetic format;
- accumulator format;
- rounding;
- overflow/underflow;
- numerical error.

A smaller format may improve storage or throughput and still be unacceptable for a declared numerical objective.

No universal accuracy ordering beyond the cited arithmetic setting is claimed.

## Kernel fusion

Fusion may reduce:

- launches;
- intermediate materialization;
- bytes moved across selected memory boundaries.

But fusion is only valid when the fused kernel preserves the declared semantics to the required numerical tolerance.

## Occupancy/resource constraints

Occupancy is treated as one resource-residency metric.

Higher occupancy does not imply higher useful throughput in every workload.

Register pressure, shared-memory use, dependency chains, memory latency, instruction mix, and data movement can change the relation.

## Exact finite witness

Use the same exact \(2\times2\) matrix product under two declared traffic models.

FLOP convention:

- 8 scalar multiplications;
- 4 scalar additions;
- \(W=12\) FLOPs.

FP32 traffic models:

A. no cross-output input reuse:
- 16 input scalar loads + 4 output scalar stores;
- \(20\) scalar transfers;
- \(Q_A=80\) bytes;
- \(I_A=12/80=3/20\) FLOP/byte.

B. perfect full-input reuse:
- 8 input scalar loads + 4 output scalar stores;
- \(12\) scalar transfers;
- \(Q_B=48\) bytes;
- \(I_B=12/48=1/4\) FLOP/byte.

Same mathematical map. Same declared FLOP count. Different declared data movement and arithmetic intensity.

Under a hypothetical one-level machine with

\[
P_{\max}=10\ \mathrm{TFLOP/s},
\qquad
B=1\ \mathrm{TB/s},
\]

the Roofline bounds are:

\[
0.15\ \mathrm{TFLOP/s}
\]

and

\[
0.25\ \mathrm{TFLOP/s}.
\]

The witness is an accounting example, not a hardware benchmark.

## Reader spine

1. Why FLOPs are not time.
2. Where data lives.
3. Arithmetic intensity and the Roofline bound.
4. The memory wall as a movement problem.
5. Parallel execution and resource residency.
6. Matrix/tensor units and tile constraints.
7. Precision formats and numerical consequences.
8. Kernels, reuse, and fusion.
9. Exact finite traffic witness.
10. Benchmarking without fooling oneself.
11. What belongs downstream in Systems.

## Benchmark discipline

A performance claim should identify at least:

- device / architecture;
- software stack and relevant version;
- precision/data types;
- input shapes;
- warmup and synchronization method;
- repetitions/statistics;
- bytes/FLOPs convention;
- whether transfers are included;
- kernel-only versus end-to-end timing.

Peak vendor specifications and measured sustained performance are separate objects.

## Failure boundaries

- FLOP count != runtime.
- peak FLOP/s != attained FLOP/s.
- arithmetic intensity without a declared memory boundary is underspecified.
- bandwidth-bound/compute-bound is model- and boundary-relative.
- equal matrix algebra != equal kernel cost.
- tensor hardware support != arbitrary shape/type acceleration.
- lower precision != acceptable error.
- occupancy != performance.
- fusion != semantic equivalence by default.
- one-device kernel reasoning != distributed-systems reasoning.

## Downstream handoff

Direct consumer:

- ATLAS-CH-SYSTEMS-001.

SYSTEMS may inherit:

- memory hierarchy and bandwidth language;
- arithmetic-intensity/Roofline discipline;
- precision and hardware-scope discipline;
- benchmark methodology;
- distinction between mathematical and physical work.

SYSTEMS must independently establish communication, collective, multi-device, parallelism, serving, batching, latency, and KV-cache claims.

## Sources

- [@WilliamsWatermanPatterson2009]
- [@NVIDIACUDAProgrammingGuide2026]
- [@NVIDIACUDABestPractices2026]

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-HARDWARE-001.yaml
