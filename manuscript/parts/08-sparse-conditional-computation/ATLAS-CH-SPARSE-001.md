# Conditional Computation
<!-- ATLAS-CH-SPARSE-001 -->

**Epistemic status:** established sparse/conditional-computation mechanisms + audited Depth prerequisite + Atlas synthesis + exact finite resource witness.  
**Specification:** manuscript/specifications/ATLAS-CH-SPARSE-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-SPARSE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-SPARSE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-SPARSE-001.yaml

A sparse model is not one thing.

A matrix can contain many zeros.

A network can skip whole blocks.

A transformer can drop tokens.

A router can select only part of a module family.

An adaptive-depth system can stop early.

These mechanisms can all reduce some notion of work.

They do not reduce the same resource, and they do not imply the same hardware behavior.

The governing rule of this chapter is:

> conditional computation is about which computation actually executes for a particular input or state; sparsity alone does not determine realized cost.

## 1. From computational depth to conditional paths

The Depth chapter established that execution depth need not equal architectural depth.

A network can:

- recur;
- halt early;
- solve toward an equilibrium;
- skip blocks;
- allocate different numbers of updates to different inputs.

Conditional computation broadens that idea.

Instead of asking only:

> how many steps execute?

ask:

> which parts of the available computation execute, for which input, under which routing rule, and at what resource cost?

That question covers depth, width, token count, modules, and sparse parameter structure.

## 2. A typed sparsity object

Use

`S=(P,A,T,B,D,R)`.

Here:

- `P` is parameter sparsity;
- `A` is activation sparsity;
- `T` is token or item sparsity;
- `B` is block, module, or expert sparsity;
- `D` is conditional execution depth;
- `R` is the routing or selection rule.

These coordinates are not interchangeable.

A network can be highly sparse in parameters while executing the same sparse graph for every input.

Another network can have dense parameters but execute only two of eight blocks for one input and all eight for another.

The first is sparse.

The second is conditional.

A system can be both.

## 3. Static parameter sparsity

A simple static pruning model is

`W'=M odot W`

with fixed binary mask `M`.

The zeros remain in the same positions across evaluated inputs.

Han, Mao, and Dally's Deep Compression is a representative pruning/compression lineage [@HanMaoDally2016].

Static parameter sparsity can reduce:

- storage;
- nonzero arithmetic;
- memory movement;

if the implementation and hardware exploit the structure.

It does not require a per-input router.

## 4. Sparsity ratio is not execution semantics

Suppose 90 percent of matrix entries are zero.

A dense kernel may still multiply through the zeros.

In that implementation:

- the representation is sparse;
- the mathematical operator has many zeros;
- the hardware execution may remain dense.

Therefore:

> stored zero structure is not enough to establish skipped physical work.

The execution path must be inspected.

## 5. Conditional computation

Conditional computation makes the active graph depend on the current input or state.

Write:

`p(x)=Route(x)`

and

`y=Execute(p(x),x)`.

The path `p(x)` may specify:

- which blocks execute;
- which tokens survive;
- which modules activate;
- how long computation continues.

The router and executor are separate objects.

That separation matters because routing costs work.

## 6. Hard block skipping

For residual-style branch `F_k`, write

`x_{k+1}=x_k+g_k(x_k)F_k(x_k)`.

If

`g_k(x_k) in {0,1}`

and the implementation avoids evaluating `F_k` when the gate is zero, the branch is genuinely skipped.

SkipNet gives a concrete learned example of input-dependent residual-block skipping [@WangEtAl2018SkipNet].

The important mechanism is not merely that a coefficient becomes zero.

The block is bypassed.

## 7. Soft gates are not automatically sparse execution

Suppose instead

`g_k in [0,1]`.

If the system computes

`F_k(x_k)`

and only afterward multiplies by a small or zero coefficient, the expensive branch has already run.

So:

`g_k=0`

does not by itself prove:

`cost(F_k)=0`.

A differentiable training relaxation can therefore describe a sparse intent without producing sparse execution.

This boundary was already present in DEPTH-001 and remains load-bearing here.

## 8. Spatially adaptive computation

Conditional computation need not apply uniformly across one input.

Figurnov et al. allocate different computation to different spatial positions in residual networks [@FigurnovEtAl2017].

This introduces a finer distinction:

- input-level conditional computation;
- region- or token-level conditional computation.

Two examples can execute different paths.

Two positions inside one example can also receive different computation.

The execution graph can vary within the input.

## 9. Token sparsity

A transformer-like system processes a set or sequence of tokens.

Let active tokens before stage `k` be `X_k`.

A selector produces

`A_k=Select_k(X_k)`.

Later computation can run only on `A_k`.

DynamicViT is a concrete example of progressive, input-dependent token sparsification in vision transformers [@RaoEtAl2021DynamicViT].

The crucial implementation question is:

> at what point does the dropped token stop participating in expensive computation?

## 10. Masking after dense work is not the same as removing before it

Suppose attention over `n` tokens constructs an `n x n` score matrix.

If all `n^2` pair interactions are computed and some outputs are masked afterward, the score-matrix work was not saved.

If selection reduces the active token count to `m<n` before the later attention stage, the later dense pair count becomes `m^2`.

That arithmetic distinction is exact.

Whether it becomes a wall-clock speedup depends on the execution system.

## 11. Structural sparsity and dynamic sparsity

A useful taxonomy is:

### Structural/static

The sparse pattern is known before seeing the particular input.

Examples:

- fixed pruning mask;
- fixed block-sparse matrix;
- fixed local attention window.

### Dynamic/input-dependent

The sparse pattern depends on the current input or state.

Examples:

- block routing;
- token dropping;
- early exit;
- adaptive spatial computation.

The same mathematical zero pattern can have different engineering implications depending on when it becomes known.

## 12. Why when matters

Static structure can often be compiled, fused, packed, or scheduled ahead of time.

Dynamic structure may require:

- a router;
- synchronization;
- variable shapes;
- irregular memory access;
- dynamic batching.

So dynamic sparsity can reduce arithmetic while increasing control overhead.

Conditional computation is not free selection.

## 13. Parameter count and active parameter count

A conditionally executed model may contain many parameters while using only a subset per input.

Therefore distinguish:

- total parameter capacity;
- active parameters per input;
- arithmetic operations per input;
- memory residency;
- parameter communication.

A model can have large total capacity without evaluating all parameters on every example.

The downstream Mixture-of-Experts chapter will develop this in the expert-routing setting.

## 14. Routing is a computation

A router can be:

- a small neural network;
- a confidence threshold;
- a heuristic;
- a learned policy;
- a top-k selector.

Whatever its form, its cost belongs in the resource ledger.

Write, in one resource unit,

`C_total(x)
=
C_route(x)
+
C_exec(p(x),x)`.

A system should not report only the work after routing and pretend selection was free.

## 15. Resource vectors

One scalar rarely captures conditional-computation cost.

Use a resource vector such as

`C(x)=(F(x),K(x),M(x),E(x))`,

with:

- arithmetic/FLOPs `F`;
- launches or dispatches `K`;
- memory traffic `M`;
- energy `E`.

Other deployments may add:

- communication volume;
- synchronization;
- sequential depth;
- accelerator occupancy.

Do not add unlike units without a declared scalarization.

## 16. Average cost

Conditional computation is often motivated by easy and hard inputs.

For input distribution `X`, average cost is

`E[C(X)]`.

On a finite benchmark it is the empirical mean.

This quantity answers:

> what does a typical input cost under the evaluation distribution?

It does not answer:

> how much capacity is required for the worst input?

## 17. Peak and tail cost

A service may care about:

- maximum active blocks;
- p95 latency;
- p99 communication;
- worst-case memory;
- deadline misses.

These are tail or peak questions.

A low mean can coexist with a dense worst-case path.

So reports should separate:

- average compute;
- peak compute;
- tail latency.

## 18. Exact witness: fixed baseline

Consider four sequential blocks.

Each contributes ten arithmetic units.

Assume the fixed implementation fuses them into one launch.

Its resource pair is

`C_fixed=(40,1)`.

The coordinates are:

- arithmetic units;
- launches.

Every input receives the same computation.

## 19. Exact witness: conditional paths

Now use four input-dependent paths:

- `x_1:{1,4}`;
- `x_2:{1,2,4}`;
- `x_3:{1,4}`;
- `x_4:{1,2,3,4}`.

Assume:

- one router launch;
- one launch for each active block.

The resource pairs are:

- `x_1:(20,3)`;
- `x_2:(30,4)`;
- `x_3:(20,3)`;
- `x_4:(40,5)`.

## 20. Average arithmetic falls

Average arithmetic is

`(20+30+20+40)/4
=
55/2
=
27.5`.

Compared with fixed arithmetic 40, the reduction is

`1-(55/2)/40
=
5/16
=
31.25%`.

The conditional system therefore performs less arithmetic on average under this finite workload.

That claim is exact.

## 21. Peak arithmetic does not fall

The fourth input executes all four blocks.

So:

`F_peak_cond=40`.

The fixed baseline also uses 40.

Thus:

- average arithmetic drops;
- peak arithmetic is unchanged.

If hardware must provision for the worst path, the mean alone is insufficient.

## 22. Launch count gets worse

Average conditional launches are

`(3+4+3+5)/4
=
15/4
=
3.75`.

The fixed path uses one.

So the conditional system is better in one coordinate and worse in another:

`(40,1)`

versus

`(55/2,15/4)`.

Neither dominates componentwise.

## 23. Hardware assumptions determine the ordering

Define a toy scalar cost

`T_(alpha,beta)(F,K)
=
alpha F+beta K`.

This is not claimed to be a realistic universal latency model.

It is a proof device.

If

`alpha=1,beta=0`,

then only arithmetic matters:

- fixed = 40;
- conditional = 27.5.

Conditional wins.

If

`alpha=1/10,beta=10`,

then launches are expensive:

- fixed = 14;
- conditional = 40.25.

Fixed wins.

The same execution traces support opposite latency conclusions under different hardware cost models.

## 24. FLOPs do not determine latency

The witness proves a structural point:

> fewer arithmetic operations do not uniquely determine lower latency.

Real hardware adds further effects:

- memory bandwidth;
- cache behavior;
- kernel launch overhead;
- vectorization;
- occupancy;
- synchronization;
- batching;
- communication.

The Roofline model makes one part of this explicit by relating attainable performance to arithmetic intensity, memory bandwidth, and compute capability [@WilliamsWatermanPatterson2009].

FLOPs are one coordinate.

They are not the clock.

## 25. Dynamic irregularity can cost efficiency

Hardware often prefers regular work.

A dense matrix operation can be highly optimized.

A dynamically sparse workload may introduce:

- tiny kernels;
- irregular memory reads;
- divergent branches;
- underfilled accelerators;
- fragmented batches.

Therefore a method can report strong nominal arithmetic reduction and weak realized speedup.

That is not necessarily an implementation failure.

It may be the consequence of the hardware/software cost structure.

## 26. Static sparsity can also fail to accelerate

Parameter pruning creates zeros.

But unstructured zeros only help execution if the kernels and hardware exploit them.

Gale, Elsen, and Hooker's large-scale sparsity study reinforces the need to evaluate sparsification methods at scale rather than treating sparsity ratio itself as a complete performance metric [@GaleElsenHooker2019].

The Atlas conclusion is broader:

> sparsity percentage is not a hardware benchmark.

## 27. Conditional depth

One form of conditional computation is to vary execution depth.

Easy input:

`tau(x)=2`.

Hard input:

`tau(x)=8`.

DEPTH-001 already supplied the stopping semantics.

SPARSE-001 adds the resource question:

- what work disappears when execution stops?
- what routing/halting overhead remains?
- what are average and tail depths?
- what hardware can exploit the variable path?

## 28. Early exit versus block skipping

Early exit stops the remaining suffix of a network.

Block skipping can omit internal blocks while later blocks still execute.

These are different path families.

For an eight-block network:

early exit might produce

`{1,2,3}`.

Skipping might produce

`{1,3,4,7,8}`.

Both are conditional.

Their scheduling and representation behavior can differ.

## 29. Token dropping versus conditional depth

Token dropping changes active width.

Conditional depth changes the number or identity of sequential transformations.

A system can do both.

For example:

- prune tokens at stage 3;
- skip block 5;
- stop at block 7.

One scalar called "sparsity" hides these distinctions.

The typed sparsity object keeps them visible.

## 30. Training-time execution can be denser

Discrete routing creates optimization difficulties.

Training may therefore use:

- continuous gates;
- straight-through estimators;
- stochastic sampling;
- auxiliary losses;
- policy gradients;
- dense masking.

Inference may use hard decisions.

The training graph and inference graph can therefore have different cost.

Do not infer inference sparsity directly from the training relaxation.

## 31. Compute and quality form a joint claim

Skipping computation changes the function executed.

So an efficiency report should pair compute with quality.

At minimum report:

`(Q,C)`

for task quality `Q` and cost `C`.

A method that cuts computation in half and destroys task performance is not a successful efficiency result under most objectives.

The acceptable frontier is application-dependent.

## 32. Dynamic computation can specialize effort

The attraction of conditional computation is simple:

> not every input may need the same amount or kind of processing.

Easy examples may need less work.

Hard examples may need more.

Some tokens may be redundant.

Some spatial locations may be uninformative.

This creates an allocation problem.

The system spends compute where the router expects it to matter.

## 33. The router can be wrong

A conditional system introduces a new failure surface.

The router can:

- drop useful tokens;
- skip necessary blocks;
- stop too early;
- over-compute easy inputs;
- under-compute hard inputs;
- become unstable under distribution shift.

A dense baseline does not have exactly the same failure mode.

Efficiency comes with a control problem.

## 34. Routing confidence is not correctness

A router may emit a high confidence score.

That does not prove the skipped computation was unnecessary.

The same epistemic boundary from DEPTH-001 applies:

> a learned halting or routing signal is not automatically a calibrated error estimator.

If one wants guaranteed error-controlled adaptation, a separate theorem or calibration layer is required.

## 35. Batching changes the economics

Suppose active-block counts in a batch are

`2,3,2,4`.

The mean is

`11/4`.

But a synchronous implementation may effectively wait for the four-block path.

Then wall-clock behavior tracks something closer to the maximum.

Dynamic batching, compaction, or regrouping can recover efficiency.

Those mechanisms add overhead of their own.

Average path length is not enough to predict batch latency.

## 36. Communication can dominate arithmetic

In distributed conditional systems, selecting a remote module can require communication.

Then total cost can contain:

- local compute;
- routing;
- all-to-all exchange;
- synchronization;
- imbalance.

A method that reduces local arithmetic can still slow down if communication grows.

This becomes central in Mixture-of-Experts systems.

SPARSE-001 establishes the accounting discipline before that chapter.

## 37. Capacity and active work can decouple

Conditional execution allows a model to possess more total components than one input uses.

This can increase representational capacity without proportional per-input arithmetic.

But total capacity still affects:

- storage;
- loading;
- communication;
- optimizer state during training;
- deployment footprint.

"Only k modules active" is not the same as "only k modules exist."

## 38. Static compression and conditional capacity are different strategies

Static pruning asks:

> which structure can be removed for all evaluated inputs?

Conditional computation asks:

> which structure can be omitted for this input?

The former reduces a model globally.

The latter selects among available computation dynamically.

Combining them is possible.

Conflating them obscures the design space.

## 39. Token sparsity can alter later complexity superlinearly

If a later dense attention stage has pairwise score cost proportional to `n^2`, reducing token count from `n` to `m` can reduce that score-matrix arithmetic roughly from `n^2` to `m^2`.

But end-to-end speedup also depends on:

- selector cost;
- projection cost;
- memory movement;
- fixed layers;
- implementation shape efficiency.

The local arithmetic saving is not the whole pipeline.

## 40. Measured speedup is contextual evidence

DynamicViT reports both FLOP reduction and measured throughput improvement on its evaluated systems [@RaoEtAl2021DynamicViT].

That is stronger evidence than FLOPs alone for those experiments.

It remains contextual:

- device;
- software;
- batch;
- model;
- implementation.

A measured speedup should not be promoted to a hardware-independent theorem.

## 41. Conditional computation is an allocation policy

Viewed abstractly, the router allocates a compute budget.

For input `x`, it chooses path `p(x)`.

The execution then spends resources according to that path.

This suggests three separate questions:

1. **selection:** which path is chosen?
2. **execution:** what work does that path perform?
3. **valuation:** was the saved work worth the quality change?

These questions should be evaluated separately.

## 42. Failure modes

### Sparsity/FLOP conflation

Treat sparse weights as proof of skipped arithmetic.

### FLOP/latency conflation

Treat fewer operations as proof of faster execution.

### Soft/hard conflation

Treat a relaxed gate as actual skipped hardware work.

### Mean/peak conflation

Report low average compute while hiding dense worst-case paths.

### Router-free accounting

Count only selected computation and omit selection overhead.

### Training/inference conflation

Measure soft training sparsity and claim hard inference savings.

### Capacity/active-work conflation

Treat inactive modules as if they do not consume storage or training resources.

### Quality omission

Report compute savings without the associated task-performance change.

## 43. A practical conditional-compute ledger

Before accepting an efficiency claim, record:

| Field | Question |
|---|---|
| sparse object | Parameters, activations, tokens, blocks, experts, depth? |
| static/dynamic | Fixed structure or input-dependent path? |
| selector | What chooses the active work? |
| hard/soft | Is work physically skipped or merely weighted? |
| training graph | What executes during training? |
| inference graph | What executes during deployment? |
| average work | Mean over which workload? |
| peak/tail work | Worst case or declared quantile? |
| arithmetic | How many operations are avoided? |
| memory | What traffic/storage changes? |
| launches | Does execution become more fragmented? |
| communication | Is data routed across devices? |
| hardware | Which machine/software/batch regime? |
| quality | What performance change accompanies the saving? |

This ledger prevents "sparse" from becoming an untyped efficiency claim.

## 44. What the exact witness establishes

The companion witness establishes:

- fixed baseline resource pair `(40,1)`;
- conditional average pair `(55/2,15/4)`;
- exact average arithmetic reduction `5/16=31.25%`;
- unchanged peak arithmetic `40`;
- compute-dominated toy cost favors conditional execution;
- launch-dominated toy cost favors fixed execution.

The witness does not claim either toy cost model is a real accelerator.

It proves only that arithmetic count does not uniquely identify latency.

## 45. Downstream handoff

**Mixture-of-Experts Systems — ATLAS-CH-MOE-001** may now assume:

- static versus conditional sparsity;
- hard versus soft routing;
- routing versus execution cost;
- parameter capacity versus active work;
- average versus peak/tail compute;
- resource-vector accounting;
- arithmetic-versus-latency boundary;
- hardware-context dependence of measured speedup.

The downstream chapter must independently develop:

- expert routing;
- capacity factors;
- load balancing;
- specialization;
- collapse;
- expert parallelism;
- communication structure.

Conditional computation supplies the grammar.

Mixture-of-Experts will supply the system.

## References used in this chapter

- Han, Mao, and Dally, *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding* [@HanMaoDally2016].
- Figurnov et al., *Spatially Adaptive Computation Time for Residual Networks* [@FigurnovEtAl2017].
- Wang et al., *SkipNet: Learning Dynamic Routing in Convolutional Networks* [@WangEtAl2018SkipNet].
- Rao et al., *DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification* [@RaoEtAl2021DynamicViT].
- Gale, Elsen, and Hooker, *The State of Sparsity in Deep Neural Networks* [@GaleElsenHooker2019].
- Williams, Waterman, and Patterson, *Roofline: An Insightful Visual Performance Model for Multicore Architectures* [@WilliamsWatermanPatterson2009].

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-SPARSE-001.yaml
