# AUDIT-028 — Conditional Computation

## Disposition

**PASS AFTER TWO PRECISION REPAIRS**

ATLAS-CH-SPARSE-001 remains at `draft-v0.1`.

The chapter correctly separates static sparsity, input-dependent conditional execution, hard versus soft gating, routing cost, token/block selection, average versus peak compute, and arithmetic reduction versus realized hardware performance.

AUDIT-028 found two in-scope precision defects:

1. the specification included a latency proxy as a primitive coordinate in the resource vector, while the derivation/manuscript correctly treated latency as a hardware-dependent modeled or measured output of lower-level resources. The specification now uses `C(x)=(F(x),K(x),M(x),E(x))` and states explicitly that latency/throughput require a declared hardware/software model or measurement;
2. the manuscript reference list used the technical-report-style Roofline title rather than the locked Communications of the ACM article title. The manuscript now matches the source lock and bibliography exactly.

No exact witness value, routing distinction, source authority boundary, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `817cc0267c48235c50024a26f5473e1b4de0f935`;
- implementation PR:
  #114;
- audit issue:
  #115;
- chapter:
  `ATLAS-CH-SPARSE-001`.

## 1. Hard prerequisite

PASS.

The source lock binds exactly:

- DEPTH manuscript blob:
  `9d365778e873217c40604a621dbe9f88ca2153e0`;
- AUDIT-018 blob:
  `0c9f5405bd7d94018d76aa93ebe74ec3e505cabe`;
- DEPTH source-lock blob:
  `b6c18e2e0e3ab82c65d830967e2874bfb41e9bb2`.

The chapter inherits only audited computational-time, hard/soft gating, conditional-execution, stopping, and resource-accounting semantics.

No Mixture-of-Experts manuscript is used as hidden prerequisite authority.

## 2. Source scope

PASS.

The source lock identifies:

- Han, Mao, and Dally (2016), static pruning/compression;
- Figurnov et al. (2017), spatially adaptive computation;
- Wang et al. (2018), input-dependent residual-block skipping;
- Rao et al. (2021), dynamic token sparsification;
- Gale, Elsen, and Hooker (2019), large-scale sparsity evaluation;
- Williams, Waterman, and Patterson (2009), Roofline hardware performance modeling.

Each source is used for a representative mechanism or performance boundary rather than a universal efficiency theorem.

## 3. Typed sparsity object

PASS.

The chapter uses:

`S=(P,A,T,B,D,R)`

for parameter, activation, token, block/module, conditional-depth, and routing coordinates.

The manuscript explicitly states that these coordinates need not agree.

Static parameter sparsity and dynamic input-conditioned execution remain distinct.

## 4. Static versus conditional computation

PASS.

A fixed mask

`W'=M odot W`

represents static sparsity when `M` is fixed across the evaluated execution regime.

Conditional computation instead uses a path or mask that depends on the current input/state.

The chapter does not equate sparsity percentage with dynamic routing.

## 5. Hard versus soft gating

PASS.

For

`x_{k+1}=x_k+g_k(x_k)F_k(x_k)`,

the chapter distinguishes:

- hard `g_k in {0,1}` plus an implementation that skips evaluation of `F_k`;
- relaxed `g_k in [0,1]` where `F_k` may still be evaluated.

A zero or small coefficient is not promoted into skipped hardware work without an execution-semantic bridge.

## 6. Token selection timing

PASS.

The chapter correctly distinguishes:

- removing tokens before a later expensive operator;
- masking them only after dense interactions have already been computed.

The local `n^2 -> m^2` pair-count observation is scoped to the later dense attention score stage and is not promoted into an end-to-end latency theorem.

## 7. Router versus executor

PASS.

The formal packet uses:

`p(x)=Route(x)`;

`y=Execute(p(x),x)`.

Routing cost is included in total cost rather than treated as free.

This is a necessary interface for downstream MoE systems.

## 8. Resource vector

PASS AFTER REPAIR.

Primitive resource accounting is now consistently:

`C(x)=(F(x),K(x),M(x),E(x))`

for arithmetic, launches/dispatches, memory traffic, and energy.

Latency and throughput are hardware-dependent outputs, not universal primitive coordinates.

The chapter preserves the DEPTH-001 rule that unlike resource units must not be silently added without a declared scalarization.

## 9. Average versus peak/tail compute

PASS.

The chapter keeps distinct:

- average cost over a declared workload;
- peak componentwise/scalarized cost;
- tail statistics such as p95/p99.

A low mean is not treated as a provisioning or worst-case guarantee.

## 10. Exact finite witness

PASS.

Fixed baseline:

`C_fixed=(40,1)`.

Conditional workload:

- `(20,3)`;
- `(30,4)`;
- `(20,3)`;
- `(40,5)`.

Independent exact replay gives:

`C_cond_avg=(55/2,15/4)`.

Average arithmetic reduction is:

`5/16=31.25%`.

Peak conditional arithmetic remains:

`40`.

Thus average arithmetic falls while peak arithmetic does not.

## 11. Latency non-identifiability witness

PASS.

For toy scalarization

`T_{alpha,beta}(F,K)=alpha F+beta K`:

### Compute-dominated

`alpha=1,beta=0`.

- fixed: `40`;
- conditional: `55/2`.

Conditional wins.

### Launch-dominated

`alpha=1/10,beta=10`.

- fixed: `14`;
- conditional: `161/4=40.25`.

Fixed wins.

The witness therefore proves that arithmetic count alone does not determine latency.

The audit confirms the Claim boundary correctly states that neither toy scalarization is asserted to be a universal real-hardware latency law.

## 12. Pareto/resource interpretation

PASS.

The fixed average pair

`(40,1)`

and conditional average pair

`(55/2,15/4)`

are incomparable componentwise:

- conditional uses less arithmetic;
- conditional uses more launches.

A scalar efficiency ordering therefore requires a declared cost model or measurement.

## 13. Batching/load imbalance

PASS.

The chapter distinguishes mean active-block count from maximum active-block count.

It correctly notes that synchronous execution can be constrained by the slowest path, while compaction/regrouping may change the hardware outcome.

No universal batching theorem is claimed.

## 14. Training versus inference execution

PASS.

The chapter states that training may use dense/soft/stochastic routing machinery while inference uses hard sparse execution.

Inference sparsity must therefore be measured on the inference graph rather than inferred solely from the training relaxation.

## 15. Hardware-performance boundary

PASS AFTER SOURCE-IDENTITY REPAIR.

The manuscript now cites the locked CACM article title:

*Roofline: An Insightful Visual Performance Model for Multicore Architectures*.

The chapter uses Roofline only for the bounded statement that attainable performance depends on more than operation count, including arithmetic intensity and memory bandwidth.

Conditional-computation-specific routing, launch, batching, and communication effects are presented as additional Atlas accounting dimensions rather than attributed to Roofline.

## 16. Quality-efficiency boundary

PASS.

The chapter requires efficiency claims to be paired with a declared task-quality metric or frontier.

It does not treat reduced compute as success independent of functional degradation.

## 17. Downstream handoff

PASS.

ATLAS-CH-MOE-001 may inherit:

- static versus dynamic sparsity;
- hard versus soft routing;
- route/execute separation;
- total capacity versus active work;
- resource-vector accounting;
- average versus peak/tail compute;
- arithmetic-versus-latency boundary.

It must independently develop expert capacity, balancing, specialization, collapse, communication, and expert parallelism.

## 18. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records SPARSE-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-SPARSE-LOCK-001`.

The bibliography closes all manuscript keys:

- `HanMaoDally2016`;
- `FigurnovEtAl2017`;
- `WangEtAl2018SkipNet`;
- `RaoEtAl2021DynamicViT`;
- `GaleElsenHooker2019`;
- `WilliamsWatermanPatterson2009`.

The exact witness contains an explicit Claim boundary.

No governed figure is required for this tranche.

## 19. Final disposition

AUDIT-028 passes after the two precision repairs.

The durable conditional-computation layer is:

**declare what may be sparse -> declare the input/state-dependent selector -> prove what work is actually skipped -> account for routing and heterogeneous resources -> separate average from peak/tail work -> map resources to hardware latency only through an explicit model or measurement.**
