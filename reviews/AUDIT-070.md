# AUDIT-070 — Scaling, Parallelism, and Serving

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-SYSTEMS-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, parallelism-typing, communication-semantics, topology, training/serving, benchmark-boundary, or repository defect requiring repair.

## Audited implementation

- implementation issue: #281
- implementation PR: #282
- exact validated implementation head: caae4650644c4677d312dcdd1ce31b30e9daeb41
- implementation GitHub Actions run: 37600790372
- implementation merge / audited protected baseline: 397682b86648cf53c775cb5912ab4201390fbd6f
- audit issue: #283
- audit branch: audit/a283
- chapter: ATLAS-CH-SYSTEMS-001

Protected implementation artifact identities:

- specification: b61e466116747a2a405df0cb457ea893e1147d98
- derivation packet: 6689d993ba888f89cdf35cbe592e203daacad16e
- computational witness: 33e06c5f988d7d9a607021d246fa4be0c8d5d501
- reader manuscript: 0e2c1e948e462cc6e068e741653dac5294c2afa7
- source lock: b2366df7956ead690789814b8fe06912f99c9f24
- Chapter Ledger: 63fe65293efe4f39343f74fa4254473b196a3b30
- Source Register: 0fc5f52912c037e5e5e0af4dbea1a3924fe015df
- transaction receipt: cdd688337a24e008e9b5d1ff036782ebb6e26627

The protected implementation merge has zero file differences from the exact validated implementation head. The additional commit is the merge topology only; the validated file tree is exactly the protected implementation tree.

## 1. Hard prerequisites

PASS.

HARDWARE-001 is bound exactly:

- manuscript 2ce486d4cce53a5f5194241ce3bb1c0f40c7c895
- source lock 98d783c072fa28d784991617af49329259ba0b8e
- AUDIT-044 2c53ff24db17895ff9feba5f0f2854fdaa1e5c9b

MOE-001 is bound exactly:

- manuscript 5281e3bc0721681c630c56057cf478311e96662d
- source lock 75d5b04a90794b7543c70414ec9e2be59c9af7ed
- AUDIT-033 261e63f7853c359460bd76302ddfaeed576892cb

No hidden prerequisite is used.

The inherited boundaries are preserved:

- FLOPs are not time;
- peak throughput is not attained throughput;
- single-device hardware reasoning does not establish distributed-system performance;
- router preference, accepted dispatch, capacity, expert placement, communication proxy, and straggler behavior remain distinct.

## 2. External source scope

PASS.

New external systems authority is limited to four primary references needed beyond the audited prerequisites:

- Narayanan et al. (2021), Megatron-LM, for composed data/tensor/pipeline training and measured large-cluster trade-offs in that system;
- Huang et al. (2019), GPipe, for microbatch pipeline parallelism and pipeline scheduling/utilization mechanisms;
- Yu et al. (2022), Orca, for iteration-level scheduling and selective batching in autoregressive Transformer serving;
- Kwon et al. (2023), PagedAttention/vLLM, for KV-cache memory-management pressure and measured serving behavior in the reported system.

No one parallelism decomposition, collective, topology, scheduler, placement, cache manager, scaling law, or performance multiplier is promoted to universal authority.

The exact collective equations, byte accounting, and placement control are Atlas-owned finite constructions rather than externally attributed theorems.

## 3. Parallelism typing

PASS.

The chapter keeps separately typed:

- data parallelism;
- tensor parallelism;
- pipeline parallelism;
- expert parallelism.

Each is described through its own state partition and synchronization/communication semantics.

The chapter does not infer one communication pattern from a parallelism degree alone.

## 4. Data-parallel boundary

PASS.

For synchronous data parallelism the declared gradient aggregate is

\[
\bar g=\frac1p\sum_{r=0}^{p-1}g_r.
\]

The reader explicitly limits the statement to the declared synchronous synchronization/update semantics.

It does not identify data parallelism with optimizer-state sharding, ring all-reduce, tree all-reduce, communication overlap, or one physical placement.

## 5. Tensor-parallel boundary

PASS.

Tensor parallelism is represented as a partition of one operator plus an explicitly required combination operation.

The chapter correctly requires the partition dimension, local partial computation, reconstitution communication, and replicated state to be declared.

It does not treat tensor-parallel degree as sufficient to determine communication volume or collective type.

## 6. Pipeline-parallel boundary

PASS.

Pipeline execution is typed by:

- stage partition;
- microbatch schedule;
- fill/drain;
- activation/gradient transfers;
- idle bubble;
- stage imbalance.

The chapter correctly treats the bubble as schedule- and dependency-relative rather than as a property of stage count alone.

## 7. Expert-parallel boundary

PASS.

The reader preserves the full chain:

\[
\text{router preference}
\neq
\text{accepted dispatch}
\neq
\text{expert placement}
\neq
\text{physical network path}.
\]

This is consistent with AUDIT-033.

Sparse expert arithmetic is not promoted into cheap communication or lower latency.

## 8. Collective semantics

PASS.

The chapter separately defines result semantics for:

- all-reduce;
- reduce-scatter;
- all-gather;
- all-to-all.

It then explicitly separates those semantic contracts from ring, tree, hierarchical, topology-aware, and implementation-specific realization choices.

No collective result semantic is treated as a performance theorem.

## 9. Logical and physical topology

PASS.

The chapter distinguishes:

- logical rank/collective topology;
- physical devices/nodes;
- physical links/fabric;
- logical-to-physical placement.

This distinction is exercised, rather than merely stated, by the exact finite witness.

## 10. Exact ring byte accounting

PASS.

Declared witness:

- rank count: p=4;
- vector length: n=8 FP32 scalars;
- vector size: S=32 bytes;
- chunk size: S/p=8 bytes;
- reduce-scatter steps: 3;
- all-gather steps: 3.

Therefore each rank sends:

\[
2(p-1)S/p
=
2(3)(32)/4
=
48\ \text{bytes}.
\]

Each rank receives the same amount.

Independent audit replay confirms these values exactly.

## 11. Exact reduction arithmetic

PASS.

Each chunk contains:

\[
n/p=2
\]

scalars.

Each rank performs one two-scalar chunk reduction in each of three reduce-scatter steps:

\[
3\cdot2=6
\]

scalar additions per rank.

Aggregate reduction additions are:

\[
4\cdot6=24.
\]

Independent audit replay confirms both counts.

## 12. Grouped placement

PASS.

Physical nodes:

- node A: A_0,A_1;
- node B: B_0,B_1.

Grouped logical ring:

\[
A_0\to A_1\to B_0\to B_1\to A_0.
\]

Exactly two directed ring edges cross the node cut.

Every ring edge carries 48 bytes over the complete collective.

Therefore:

\[
Q_{\mathrm{cut}}^G=2\cdot48=96\ \text{bytes}.
\]

## 13. Interleaved placement

PASS.

Interleaved ring:

\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]

All four directed ring edges cross the node cut.

Therefore:

\[
Q_{\mathrm{cut}}^I=4\cdot48=192\ \text{bytes}.
\]

## 14. Equal-work control

PASS.

Both placements retain exactly:

- 6 additions per rank;
- 24 aggregate additions;
- 48 bytes sent per rank;
- 48 bytes received per rank;
- identical all-reduce value semantics.

But:

\[
Q_{\mathrm{cut}}^I=2Q_{\mathrm{cut}}^G.
\]

The required control is therefore established:

\[
\boxed{
\text{equal arithmetic and equal per-rank collective bytes}
\not\Rightarrow
\text{equal physical cross-cut traffic}.
}
\]

## 15. Toy cut-capacity lower bound

PASS.

Under the explicitly hypothetical shared-cut capacity

\[
B_{\mathrm{cut}}=16\ \text{bytes/time-unit},
\]

the chapter computes:

\[
T_G\ge96/16=6,
\]

\[
T_I\ge192/16=12.
\]

The manuscript, derivation packet, witness, and receipt all identify these as accounting/cut-capacity lower bounds rather than hardware measurements.

No runtime oracle is implied.

## 16. Modeled versus measured performance

PASS.

The chapter explicitly distinguishes:

- byte/message accounting;
- lower bounds;
- asymptotic/critical-path models;
- concrete benchmark measurements.

Protocol overhead, launch overhead, synchronization, overlap, routing, congestion, software queues, and device execution remain outside the toy lower bound unless separately modeled or measured.

## 17. Training scaling

PASS.

The chapter defines a scoped strong-scaling-style efficiency statistic:

\[
\eta_p=
\frac{\mathrm{throughput}(p)}
{p\,\mathrm{throughput}(1)}.
\]

It requires workload and measurement protocol to be declared and warns that batch, sequence length, precision, checkpointing, optimizer semantics, and partition changes can change the comparison.

It does not claim linear speedup.

## 18. Training versus serving

PASS.

Training efficiency and serving efficiency remain separate objects.

The serving layer introduces request arrivals, evolving autoregressive state, scheduling, cache residency, latency distributions, throughput/goodput, and service objectives.

No training throughput result is used to infer serving latency or tail behavior.

## 19. Latency, throughput, and goodput

PASS.

Request latency is defined from arrival to completion.

Throughput units are explicitly declared rather than collapsed across requests/s, output tokens/s, and total tokens/s.

A service-level goodput example is separately defined as requests meeting a declared latency objective per unit time.

The chapter correctly preserves:

\[
\text{raw throughput}\neq\text{SLO goodput}.
\]

## 20. Tail behavior

PASS.

Mean latency and percentile/tail latency are kept distinct.

The chapter does not infer p99 from a mean.

Benchmark discipline explicitly requires latency percentiles when tail claims matter.

## 21. Serving scheduling

PASS.

Orca is used as a primary example of iteration-level scheduling and selective batching.

The Atlas imports the mechanism and measured-example status, not a universal speedup constant.

Batch size remains a scheduling/resource variable rather than an unconditional proxy for serving quality.

## 22. KV-cache boundary

PASS.

The chapter uses generic cache accounting:

\[
M_i=\ell_i b_i,
\qquad
M_{\mathrm{KV}}=\sum_iM_i,
\]

with b_i explicitly model-, precision-, layout-, and sharding-dependent.

PagedAttention/vLLM is used as a primary example of KV-cache memory-management pressure and one mitigation design.

No implementation-specific cache layout or performance multiplier is promoted to a universal law.

## 23. Utilization and useful work

PASS.

The reader explicitly blocks the identification:

\[
\text{utilization}=\text{useful-work efficiency}.
\]

Padding, SLO-missing work, recomputation, synchronization, and discarded speculative work are given as reasons the quantities can diverge.

## 24. Benchmark discipline

PASS.

Training records require model/workload, batch semantics, precision, update semantics, device count/type, topology, parallelism degrees, sharding, warmup/measurement region, throughput unit, and scaling baseline.

Serving records require model/precision, device/topology, request/input-length distribution, output-length distribution, concurrency/arrival process, scheduler/batching, KV-cache policy, latency percentiles, throughput/goodput definition, SLO, and duration.

This preserves the source lock's rule that measured results remain scoped to concrete conditions.

## 25. Receipt provenance

PASS.

Every implementation artifact identity recorded in governance/tranches/ATLAS-CH-SYSTEMS-001.md matches the protected implementation tree.

The receipt itself is bound at:

cdd688337a24e008e9b5d1ff036782ebb6e26627.

## 26. Chapter Ledger and Source Register

PASS.

The Chapter Ledger records SYSTEMS-001 at draft-v0.1 with specification, manuscript, derivation, source-lock, and computational-witness paths.

The Source Register contains ATLAS-SRC-SYSTEMS-LOCK-001.

No governed figure is required by this chapter.

## 27. Repository integrity

PASS subject to audit-PR validation.

The implementation exact head caae4650644c4677d312dcdd1ce31b30e9daeb41 passed the full repository validator in GitHub Actions run 37600790372.

The protected implementation merge 397682b86648cf53c775cb5912ab4201390fbd6f is byte/tree-equivalent to the validated implementation head: the exact commit comparison reports zero file differences.

Independent post-merge audit replay returned:

SYSTEMS_AUDIT_WITNESS_OK.

The audit record itself must now pass the full repository validator on its own exact head before protected merge.

## Final disposition

AUDIT-070 passes with no repair, subject to exact-head audit-PR validation.

The durable systems rule is:

**distributed execution must be described through typed parallelism, communication semantics, physical placement/topology, memory, scheduling, and declared measurements together; equal arithmetic work does not imply equal communication or latency cost, and training efficiency does not determine serving efficiency.**
