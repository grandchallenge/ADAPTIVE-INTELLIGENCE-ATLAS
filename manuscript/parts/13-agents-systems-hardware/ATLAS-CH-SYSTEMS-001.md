# Scaling, Parallelism, and Serving
<!-- ATLAS-CH-SYSTEMS-001 -->

**Epistemic status:** audited Hardware and Mixture-of-Experts prerequisites + primary distributed-training/serving systems sources + Atlas synthesis + exact finite placement/communication witness.  
**Specification:** manuscript/specifications/ATLAS-CH-SYSTEMS-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-SYSTEMS-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-SYSTEMS-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-SYSTEMS-001.yaml

A model that fits and runs efficiently on one accelerator is not yet a distributed system.

Once computation crosses devices, several new objects appear:

- replicas and shards;
- stage boundaries;
- collectives;
- physical links;
- synchronization;
- queues;
- request schedulers;
- distributed memory state;
- stragglers;
- service-level metrics.

The governing rule is:

\[
\boxed{
\text{distributed execution cost is a property of computation, communication, placement, scheduling, and measurement together.}
}
\]

This chapter develops that boundary without turning one training stack or serving system into a universal law.

## 1. From hardware to systems

HARDWARE-001 established that:

- FLOPs are not time;
- bytes moved matter;
- arithmetic intensity is boundary-relative;
- peak throughput is not attained throughput;
- latency and throughput are distinct;
- benchmark scope must be declared.

Those rules continue to hold across devices.

Distributed execution adds another layer: values may have to move between devices, and the path itself can become load-bearing.

The same mathematical model can therefore differ in:

- partition;
- placement;
- collective algorithm;
- topology;
- schedule;
- memory replication;
- request batching.

Equal model arithmetic does not erase these differences.

## 2. A typed systems object

Write:

\[
\mathcal S=(R,\Pi,\Gamma,\mathcal C,\mathcal M,\mathcal Q,\mathcal P).
\]

Here:

- \(R\): ranks/devices;
- \(\Pi\): typed parallelism decomposition;
- \(\Gamma\): physical communication topology;
- \(\mathcal C\): collective/point-to-point semantics;
- \(\mathcal M\): memory state and placement;
- \(\mathcal Q\): scheduling/request state;
- \(\mathcal P\): measurement protocol.

A claim about one coordinate does not automatically determine the others.

For example:

\[
\text{tensor-parallel degree}=4
\]

does not tell us:

- which tensor dimension is split;
- which collective follows;
- whether links are intra-node or inter-node;
- how much overlap occurs;
- what latency is measured.

## 3. Parallelism is not one thing

Large-model systems commonly combine several different decompositions.

The Atlas keeps four separate:

1. data parallelism;
2. tensor parallelism;
3. pipeline parallelism;
4. expert parallelism.

Narayanan et al. describe composing data, tensor, and pipeline parallelism in Megatron-LM and report measured large-cluster trade-offs in that system.

The Atlas uses that paper as primary evidence that these modes can be composed and have materially different scaling behavior.

It does not treat the reported configuration as universal.

## 4. Data parallelism

In synchronous data parallelism, parameter replicas process different data shards.

Let rank \(r\) compute local gradient:

\[
g_r.
\]

One declared synchronization rule is:

\[
\bar g=\frac1p\sum_{r=0}^{p-1}g_r.
\]

Replicas then apply the same update from \(\bar g\).

The communication is not optional if exact replica synchronization under this rule is required.

But data parallelism does not by itself specify:

- ring versus tree all-reduce;
- gradient bucketing;
- optimizer-state sharding;
- communication overlap;
- physical placement.

Those are additional systems choices.

## 5. Tensor parallelism

Tensor parallelism divides one operator across ranks.

For example, a matrix operation can be partitioned by rows, columns, heads, or another declared dimension.

Each rank computes a partial result.

The next layer may then require:

- all-reduce;
- all-gather;
- reduce-scatter;
- point-to-point exchange;
- no communication until a later boundary.

The exact pattern depends on the partition and surrounding operators.

So:

\[
\boxed{
\text{tensor parallelism}
\neq
\text{one fixed communication pattern}.
}
\]

Megatron-LM is a primary example of practical tensor-parallel Transformer training.

## 6. Pipeline parallelism

Pipeline parallelism divides an ordered network into stage groups.

If stages are:

\[
S_1,S_2,\ldots,S_k,
\]

a microbatch flows through them in order.

Different microbatches can occupy different stages concurrently.

GPipe is a primary example of microbatch pipeline parallelism.

The key systems quantities include:

- stage partition;
- microbatch count;
- fill time;
- drain time;
- idle bubbles;
- activation transfers;
- backward transfers during training;
- stage imbalance.

More stages can reduce per-stage model memory.

They can also create more communication boundaries and more sensitivity to imbalance.

## 7. A pipeline bubble is schedule-relative

Suppose one stage finishes while the next required dependency has not arrived.

That stage is idle.

This idle period belongs to the schedule and dependency graph.

It is not a new mathematical layer in the model.

Pipeline utilization therefore depends on how microbatches are ordered through stages.

A stage count alone cannot determine it.

## 8. Expert parallelism

MOE-001 established a chain:

\[
\text{router probabilities}
\to
\text{preferred routes}
\to
\text{capacity/overflow}
\to
\text{accepted dispatch}
\to
\text{expert execution}.
\]

Expert parallelism adds physical placement.

Let:

\[
\operatorname{dev}(e)
\]

be the device hosting expert \(e\).

If token \(i\) originates elsewhere, accepted dispatch induces communication.

SYSTEMS adds one further object:

\[
\operatorname{path}(\operatorname{src}(i),\operatorname{dev}(e);\Gamma).
\]

Hence:

\[
\boxed{
\text{preference}
\neq
\text{dispatch}
\neq
\text{placement}
\neq
\text{network path}.
}
\]

This distinction prevents a routing diagram from pretending to be a systems benchmark.

## 9. Collective semantics

A collective says what distributed values must become.

It does not by itself say how the network achieves that state.

For rank-local values \(x_r\):

### All-reduce

Every rank receives the reduction:

\[
y_r=\sum_j x_j.
\]

### Reduce-scatter

The values are reduced, and declared partitions of the result are distributed across ranks.

### All-gather

Declared partitions are gathered so every rank receives the whole collection.

### All-to-all

Each source rank sends destination-specific payloads to every destination rank.

These are semantic contracts.

Ring, tree, hierarchical, topology-aware, and implementation-specific algorithms are ways to realize them.

## 10. Logical topology and physical topology

A ring all-reduce has a logical neighbor order.

A cluster has a physical topology.

They are not the same object.

A logical neighbor pair might map to:

- two devices on one board;
- two devices in one node;
- two nodes in one rack;
- two nodes across a slower shared fabric.

Placement can therefore change which physical links carry the same logical collective.

## 11. Exact four-rank witness

Use four ranks:

\[
A_0,A_1,B_0,B_1.
\]

Place:

- \(A_0,A_1\) on node A;
- \(B_0,B_1\) on node B.

Each rank begins with an 8-element FP32 vector.

Thus:

\[
S=8\cdot4=32\ \text{bytes}.
\]

The collective is sum all-reduce implemented as ring reduce-scatter plus ring all-gather.

## 12. Per-rank ring accounting

With:

\[
p=4,
\]

each vector is split into four 8-byte chunks.

Reduce-scatter requires three ring steps.

All-gather requires three more.

Each rank sends one chunk per step.

Therefore each rank sends:

\[
6\cdot8=48\ \text{bytes}
\]

and receives 48 bytes.

During reduce-scatter, each rank reduces three 2-scalar chunks:

\[
3\cdot2=6
\]

scalar additions.

The two placements below have exactly the same values.

## 13. Grouped placement

Use logical ring:

\[
A_0\to A_1\to B_0\to B_1\to A_0.
\]

Only two directed ring edges cross between nodes:

\[
A_1\to B_0,
\qquad
B_1\to A_0.
\]

Each ring edge carries 48 bytes over the complete collective.

Therefore:

\[
Q_{\mathrm{cut}}^G
=
2\cdot48
=
96\ \text{bytes}.
\]

## 14. Interleaved placement

Now use:

\[
A_0\to B_0\to A_1\to B_1\to A_0.
\]

Every ring edge crosses the node boundary.

Therefore:

\[
Q_{\mathrm{cut}}^I
=
4\cdot48
=
192\ \text{bytes}.
\]

Nothing changed in the reduction arithmetic.

Nothing changed in per-rank total communication volume.

Only logical-to-physical placement changed.

## 15. Equal arithmetic does not imply equal physical communication

Both cases have:

- 6 additions per rank;
- 24 aggregate additions;
- 48 bytes sent per rank;
- 48 bytes received per rank.

Yet:

\[
Q_{\mathrm{cut}}^I
=
2Q_{\mathrm{cut}}^G.
\]

Therefore:

\[
\boxed{
\text{equal arithmetic and equal per-rank bytes}
\not\Rightarrow
\text{equal cross-cut traffic}.
}
\]

This is the chapter's exact finite control.

## 16. A lower bound is not a latency measurement

Suppose, only for the toy model, that all cross-node traffic shares aggregate cut capacity:

\[
B_{\mathrm{cut}}
=
16\ \text{bytes/time-unit}.
\]

Then any execution must satisfy:

\[
T\ge
\frac{Q_{\mathrm{cut}}}{B_{\mathrm{cut}}}.
\]

So:

\[
T_G\ge6,
\qquad
T_I\ge12.
\]

This does not say a real machine takes 6 or 12 units.

Real time can include:

- protocol overhead;
- launch overhead;
- synchronization;
- bidirectional behavior;
- overlap;
- routing;
- congestion;
- software queues;
- device-kernel time.

The witness proves an accounting distinction, not a benchmark.

## 17. Communication can hide behind computation

Distributed systems often overlap communication with local arithmetic.

If a communication step lies off the critical path, some of its time can be hidden.

But hidden is not free.

The bytes still occupy links, buffers, and collective state.

A competing transfer can expose the cost again.

So a serious claim should distinguish:

- communication volume;
- communication duration;
- exposed communication time;
- total step time.

## 18. Stragglers

A synchronized step often waits for the slowest required participant.

That participant may be slow because of:

- more work;
- slower hardware;
- slower link path;
- cache/memory effects;
- queueing;
- transient interference;
- expert imbalance.

Average rank time can therefore fail to predict synchronized step time.

The MoE straggler boundary is a special case of this broader rule.

## 19. Training scaling

For a fixed declared workload and measurement protocol, define throughput at \(p\) devices:

\[
\mathrm{Th}(p).
\]

A strong-scaling-style efficiency statistic is:

\[
\eta_p=
\frac{\mathrm{Th}(p)}
{p\,\mathrm{Th}(1)}.
\]

The statistic is meaningful only if the comparison states what was held fixed.

Changing:

- global batch size;
- sequence length;
- precision;
- activation checkpointing;
- optimizer semantics;
- model partition;

can change the task being compared.

## 20. More devices can reduce efficiency

Additional devices can provide:

- more memory;
- more compute;
- more concurrency.

They can also introduce:

- more synchronization;
- more communication;
- more idle imbalance;
- more failure surface.

So:

\[
\boxed{
p\uparrow
\not\Rightarrow
\eta_p\uparrow.
}
\]

Nor does low \(\eta_p\) alone identify the cause.

## 21. Training and serving optimize different state

Training repeatedly performs forward work, backward work, gradient synchronization, and parameter updates.

Serving receives requests from outside the system.

Autoregressive generation then creates a new state variable: each active request has a current generated prefix and must be revisited for further tokens.

The scheduler therefore becomes part of the mechanism.

## 22. Request latency

For request \(i\):

\[
L_i=
t_i^{\mathrm{complete}}
-
t_i^{\mathrm{arrival}}.
\]

Different serving questions may care about:

- time to first token;
- time per output token;
- end-to-end completion latency;
- p50 latency;
- p95/p99 tail latency.

One number cannot stand for all of them.

## 23. Throughput

Serving throughput can be measured as:

- requests per second;
- output tokens per second;
- total processed tokens per second.

Those are different denominators and can rank systems differently.

A throughput claim must say which one is meant.

## 24. Goodput

Suppose requests have latency objective \(\tau\).

One possible request goodput is:

\[
G_\tau
=
\frac{|\{i:L_i\le\tau\}|}{T}.
\]

A system can increase raw throughput while violating more latency objectives.

Thus:

\[
\boxed{
\text{throughput}
\neq
\text{SLO goodput}.
}
\]

## 25. Average latency and tail latency

Mean latency is:

\[
\bar L=
\frac1N\sum_i L_i.
\]

A p99 statistic is an order statistic.

The mean does not determine p99.

A system can improve the average while making rare long waits worse.

Tail behavior therefore requires its own evidence.

## 26. Iteration-level scheduling

Autoregressive requests can have different remaining lengths.

A rigid batch can force completed or short requests to wait behind longer work, depending on system semantics.

Orca introduced iteration-level scheduling, with scheduling decisions at model-iteration granularity, and selective batching in its reported system.

The Atlas imports the mechanism and the measured-example status.

It does not import Orca's reported speedup as a universal constant.

## 27. Batching is a scheduling policy

Batching can increase arithmetic efficiency and throughput by presenting more parallel work.

It can also increase waiting time before service.

The relevant trade depends on:

- arrival pattern;
- batch formation;
- request lengths;
- device occupancy;
- memory capacity;
- service objectives.

Therefore:

\[
\boxed{
\text{larger batch}
\not\Rightarrow
\text{better serving under every metric}.
}
\]

## 28. KV-cache state

During autoregressive Transformer serving, previously computed key/value state can be retained so later token steps do not recompute the entire prefix attention state.

For request \(i\), use generic accounting:

\[
M_i=\ell_i b_i,
\]

where:

- \(\ell_i\) is retained sequence length;
- \(b_i\) is implementation-specific cache bytes per retained position.

Then:

\[
M_{\mathrm{KV}}=\sum_i M_i.
\]

The value \(b_i\) depends on architecture, precision, sharding, and layout.

## 29. Cache allocation can limit concurrency

Even if model weights fit, active-request cache state can constrain how many requests remain resident.

Fragmentation and duplication can further reduce usable capacity.

Kwon et al. identify KV-cache memory-management inefficiency as a serving bottleneck and introduce PagedAttention/vLLM as one design for mitigating it.

Their measured gains are evidence about the reported implementation and workloads.

They are not a hardware-independent theorem.

## 30. Prefill and decode are not the same workload

Processing an input prompt can expose substantial parallel work over many token positions.

Autoregressive decode advances one or a small number of positions per active request per iteration.

The arithmetic shape, memory behavior, and batching opportunity can differ.

A serving benchmark that reports only one aggregate throughput number can hide this difference.

## 31. Utilization

A device can be highly utilized while doing work that is not useful under the service objective.

Examples include:

- padded work;
- work for requests that miss an SLO;
- excess recomputation;
- synchronization overhead;
- speculative work later discarded.

Utilization is a resource-activity metric.

It is not automatically useful-work efficiency.

## 32. Communication and memory interact

Tensor or expert parallelism can reduce per-device parameter memory.

That can permit a larger model or larger request batch.

But it can also increase communication.

Conversely, replication can reduce communication on one path while consuming more memory.

Systems design is therefore multi-objective.

## 33. Placement is an optimization variable

Placement decides where shards, stages, experts, replicas, and cache state live.

The exact ring witness showed that placement alone can change cross-cut bytes.

In larger systems, placement can interact with:

- heterogeneous links;
- shared switches;
- NUMA effects;
- rack boundaries;
- expert traffic;
- request locality.

The Atlas does not prescribe one placement algorithm.

It requires the placement to be part of the claim.

## 34. Measured versus modeled performance

A model may predict:

- bytes;
- message count;
- lower bounds;
- asymptotic scaling;
- critical-path structure.

A benchmark measures a concrete realization.

A mismatch is not automatically a failure of arithmetic.

It may reveal omitted effects.

The correct response is to name those effects rather than quietly relabel a model as a measurement.

## 35. Training benchmark record

A serious training record should identify:

- model/workload;
- batch semantics;
- precision;
- optimizer/update;
- hardware count/type;
- topology;
- parallelism degrees;
- sharding;
- warmup;
- measurement interval;
- throughput unit;
- scaling baseline.

Without these, "X% scaling efficiency" is underspecified.

## 36. Serving benchmark record

A serious serving record should identify:

- model and precision;
- device count/type and topology;
- request/input-length distribution;
- output-length distribution;
- concurrency or arrival process;
- scheduler/batching;
- KV-cache policy;
- latency percentiles;
- throughput/goodput definition;
- SLO if used;
- measurement duration.

Without these, "requests per second" cannot be interpreted safely.

## 37. What the sources establish

Narayanan et al. provide primary evidence for composed data/tensor/pipeline training and their measured trade-offs in Megatron-LM.

Huang et al. provide primary evidence for microbatch pipeline execution in GPipe.

Yu et al. provide primary evidence for iteration-level scheduling/selective batching in Orca.

Kwon et al. provide primary evidence for KV-cache memory-management pressure and PagedAttention/vLLM.

These sources demonstrate representative mechanisms.

They do not close the design space.

## 38. The systems layer is not one scalar

A distributed system can be described by a resource/performance vector such as:

\[
K=
(
W,
Q_{\mathrm{local}},
Q_{\mathrm{net}},
M,
L_{50},
L_{99},
\mathrm{Th},
G,
U
).
\]

Here the entries might denote arithmetic work, local bytes, network bytes, memory, median/tail latency, throughput, goodput, and utilization.

The exact vector depends on the task.

Collapsing it to one score requires a declared objective.

## 39. Failure boundaries

The durable non-implications are:

\[
\text{more devices}
\not\Rightarrow
\text{linear speedup},
\]

\[
\text{equal FLOPs}
\not\Rightarrow
\text{equal communication},
\]

\[
\text{equal per-rank bytes}
\not\Rightarrow
\text{equal cross-cut traffic},
\]

\[
\text{high throughput}
\not\Rightarrow
\text{low latency},
\]

\[
\text{low average latency}
\not\Rightarrow
\text{low tail latency},
\]

\[
\text{high utilization}
\not\Rightarrow
\text{high useful-work efficiency},
\]

\[
\text{training efficiency}
\not\Rightarrow
\text{serving efficiency}.
\]

These are not pessimistic slogans.

They are type checks for systems claims.

## 40. Systems reasoning

The chapter's systems method is:

1. name the computation;
2. name the partition;
3. name the communication semantics;
4. name the physical placement/topology;
5. account for bytes and memory;
6. name the schedule;
7. define latency/throughput/tail metrics;
8. distinguish models from measurements;
9. preserve the workload and benchmark boundary;
10. compare alternatives only under declared objectives.

That method scales better than treating "distributed" as a performance adjective.

## References used in this chapter

- Deepak Narayanan et al. (2021), *Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM*, arXiv:2104.04473.
- Yanping Huang et al. (2019), *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*, arXiv:1811.06965.
- Gyeong-In Yu et al. (2022), *Orca: A Distributed Serving System for Transformer-Based Generative Models*, OSDI 22, pp. 521–538.
- Woosuk Kwon et al. (2023), *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv:2309.06180.

Exact source identities, inherited prerequisite authority, and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-SYSTEMS-001.yaml
