# The Machine Under the Mathematics
<!-- ATLAS-CH-HARDWARE-001 -->

**Epistemic status:** audited Linear Algebra prerequisite + classical Roofline performance model + current CUDA programming/best-practices documentation + Atlas synthesis + exact finite traffic witness.  
**Specification:** manuscript/specifications/ATLAS-CH-HARDWARE-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-HARDWARE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-HARDWARE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-HARDWARE-001.yaml

## 1. Mathematics does not run in zero time

A mathematical chapter can write

\[
C=AB.
\]

The hardware must still:

- obtain the inputs;
- schedule the work;
- move values through a memory hierarchy;
- perform arithmetic in some format;
- synchronize where required;
- place the result somewhere.

Those operations consume physical resources.

The central boundary of this chapter is therefore:

\[
\boxed{
\text{mathematical work}
\neq
\text{physical execution cost}.
}
\]

Two programs can implement the same map and take different time.

Two programs can execute the same nominal number of floating-point operations and move different numbers of bytes.

Two kernels can move the same bytes and expose different amounts of parallel work.

Hardware is not an implementation footnote.

It is part of the effective computational system.

## 2. The linear map survives; the implementation changes

The Linear Algebra chapter distinguished an abstract linear map from one coordinate representation.

Hardware adds another distinction.

Even after the matrix representation has been fixed, there can be many physical implementations of the same matrix operation.

For example, a matrix product can differ in:

- blocking;
- tile order;
- data layout;
- precision;
- reuse;
- kernel fusion;
- memory placement;
- scheduling.

The output may represent the same mathematical operator.

The execution path need not be the same.

This is why algorithmic complexity, FLOP count, and runtime should not be collapsed.

## 3. FLOPs are an accounting convention

A floating-point operation count is useful only after its convention is declared.

This chapter's finite witness counts:

- one scalar multiplication as one FLOP;
- one scalar addition as one FLOP.

Under that convention, a \(2\times2\) matrix product requires:

\[
8
\]

multiplications and

\[
4
\]

additions, for a total of:

\[
12\ \text{FLOPs}.
\]

Other performance conventions may count fused multiply-add differently.

The point is not that one convention is universally correct.

The point is that comparisons must use one declared convention consistently.

## 4. Throughput is not latency

A machine can sustain a high rate of completed operations while one individual dependency chain still takes significant time.

These are different quantities.

Latency asks:

> How long does one operation or dependency chain take?

Throughput asks:

> How much work can the machine complete per unit time when enough parallel work is available?

Modern accelerators are often designed to tolerate latency by maintaining many independent operations in flight.

That strategy works only when the workload exposes enough usable parallelism.

## 5. Data movement can dominate arithmetic

Suppose a kernel performs very little arithmetic on each loaded value.

The arithmetic units may spend much of their time waiting for data.

Suppose instead the same loaded values are reused many times before eviction.

Then much more arithmetic can be performed per byte transferred.

The relevant quantity is **arithmetic intensity**.

For a declared memory boundary \(M\), let:

\[
W
\]

be the declared FLOP count and

\[
Q_M
\]

the bytes moved across that boundary.

Then:

\[
\boxed{
I_M=\frac{W}{Q_M}.
}
\]

The subscript matters.

The same computation can have different intensities relative to:

- a host-device link;
- device DRAM;
- an on-chip cache;
- programmer-managed shared memory.

Arithmetic intensity is therefore not a property of source code alone.

It is a property of work together with a declared data-movement boundary and implementation.

## 6. The Roofline idea

Williams, Waterman, and Patterson introduced the Roofline model as a visual upper-bound model connecting computational throughput, memory bandwidth, and arithmetic intensity. [@WilliamsWatermanPatterson2009]

In its simplest one-level form:

\[
P_{\mathrm{attainable}}
\le
\min(P_{\max},B_M I_M).
\]

Here:

- \(P_{\max}\) is a declared peak compute rate;
- \(B_M\) is a declared bandwidth across memory boundary \(M\);
- \(I_M\) is arithmetic intensity at that boundary.

The first term gives a compute roof.

The second gives a bandwidth roof.

The crossover occurs at:

\[
I^\star_M
=
\frac{P_{\max}}{B_M}.
\]

Below this point, the bandwidth-side roof is lower.

Above it, the compute roof is lower.

This does not mean an implementation will reach the roof.

It means the implementation should not be expected to exceed the declared bound.

## 7. A roof is not a prediction

Real performance can fall below a Roofline bound because of:

- dependencies;
- poor memory access;
- insufficient parallel work;
- instruction mix;
- synchronization;
- divergence;
- launch overhead;
- cache effects;
- resource constraints;
- implementation quality.

So the safe statement is:

\[
\boxed{
\text{Roofline}
=
\text{upper-bound diagnostic},
}
\]

not:

\[
\text{Roofline}
=
\text{runtime oracle}.
\]

The model helps ask whether improving arithmetic throughput is even relevant before doing so.

## 8. The memory hierarchy

The current CUDA programming model exposes several physically and logically distinct storage levels, including thread-local registers, shared memory associated with blocks, caches, and global/device memory. [@NVIDIACUDAProgrammingGuide2026]

The CUDA Best Practices Guide emphasizes that these memory spaces differ in scope, latency, bandwidth, and intended use. [@NVIDIACUDABestPractices2026]

The exact hierarchy is architecture-specific.

The general systems lesson is not:

> every accelerator has this exact hierarchy.

It is:

> locality has levels, and moving data between levels has different costs.

A kernel that repeatedly fetches the same value from a distant level can behave very differently from one that reuses a nearby copy.

## 9. Registers and local state

Registers are fast, thread-local storage in CUDA's programming model. [@NVIDIACUDAProgrammingGuide2026]

They are finite.

A kernel that requires more per-thread state can reduce the number of simultaneously resident threads or spill values into slower storage.

So a transformation that appears to "save memory traffic" can still create another bottleneck if it requires too much local state.

Hardware optimization is usually a trade among constrained resources.

## 10. Shared memory and reuse

CUDA shared memory is an on-chip, programmer-managed storage region shared among threads in a block. [@NVIDIACUDAProgrammingGuide2026]

The Best Practices Guide uses shared-memory examples to show why staging data near the compute units can:

- enable coalesced access;
- reduce redundant global-memory loads;
- improve reuse.

It also documents bank conflicts as one way shared-memory access can lose effective bandwidth. [@NVIDIACUDABestPractices2026]

The general lesson is that "on chip" does not mean "free."

Access pattern still matters.

## 11. Global memory and bandwidth

Device/global memory is large relative to on-chip storage and visible across the device in the CUDA model. [@NVIDIACUDAProgrammingGuide2026]

Its capacity is useful.

Its distance from execution units makes repeated traffic expensive relative to reusing data already nearby.

This motivates three recurring questions:

1. How many bytes must cross the boundary?
2. How often are the same values reused?
3. Can the implementation rearrange work to increase locality?

These questions can matter more than shaving a small number of arithmetic instructions.

## 12. Warps and SIMT

CUDA groups threads into warps of 32 threads in its current programming model and describes execution using SIMT semantics. [@NVIDIACUDAProgrammingGuide2026]

Threads execute the same kernel but may follow different control-flow paths.

Divergence can reduce useful lane utilization.

Memory access patterns across a warp also affect how efficiently global-memory transactions are formed.

These are CUDA-specific execution facts.

They should not be silently promoted into universal laws of all accelerators.

## 13. Parallelism is a resource, not a synonym for speed

A workload can contain many operations and still expose limited parallelism because of dependencies.

Another workload can expose enormous parallelism but become bandwidth-limited.

A third can expose both parallelism and reuse but be constrained by register or shared-memory requirements.

So the Atlas separates:

- work count;
- available parallelism;
- resource residency;
- achieved throughput.

These are related.

They are not identical.

## 14. Occupancy

In GPU performance discussions, occupancy usually refers to resident active warps or threads relative to a hardware limit.

It can help hide latency.

It is not itself the objective.

Higher occupancy can coexist with lower performance if, for example:

- each thread does less useful work;
- memory access worsens;
- instruction-level reuse is lost;
- more efficient kernels need more registers or shared memory.

The safe rule is:

\[
\boxed{
\text{occupancy}
\neq
\text{performance}.
}
\]

Occupancy is one diagnostic among several.

## 15. Matrix and tensor hardware

Modern NVIDIA GPUs expose warp-level matrix multiply-accumulate operations that can use Tensor Cores for supported matrix problems of the form:

\[
D=AB+C.
\]

The programming guide documents tile shapes, supported data types, fragment layouts, synchronization requirements, and architecture-dependent restrictions. [@NVIDIACUDAProgrammingGuide2026]

This creates a strong distinction between:

\[
\text{abstract matrix multiplication}
\]

and

\[
\text{matrix multiplication mapped efficiently to specialized hardware}.
\]

A matrix expression does not automatically achieve the device's peak matrix-unit throughput.

Shapes, layouts, types, alignment, data movement, and surrounding operations matter.

## 16. Tiles connect algebra to hardware

Large matrix products are decomposed into smaller tiles.

Tiling can improve reuse because a loaded block participates in many multiply-accumulate operations before replacement.

This is the physical counterpart of a simple algebraic fact:

one matrix entry can contribute to several output entries.

The optimization opportunity comes from arranging the implementation so the hardware retains that value long enough to reuse it.

The mathematics supplies reuse potential.

The implementation determines whether the machine realizes it.

## 17. Precision is several questions

"FP16," "BF16," "FP32," and other format names describe representation and arithmetic choices.

They do not by themselves answer:

- what error accumulates;
- where rounding occurs;
- what the accumulator format is;
- whether overflow or underflow occurs;
- whether the final task tolerates the resulting perturbation.

The CUDA Best Practices Guide explicitly separates numerical accuracy/precision concerns and notes that results can differ across floating-point precisions because representation and rounding differ. [@NVIDIACUDABestPractices2026]

So the Atlas separates:

\[
\text{smaller format}
\]

from

\[
\text{acceptable numerical error}.
\]

The first is a storage/arithmetic choice.

The second is a property that must be checked relative to the computation and task.

## 18. Mixed precision

Specialized matrix hardware often supports mixed input and accumulator formats.

This can be valuable because:

- narrower inputs reduce storage and traffic;
- wider accumulation can reduce some forms of accumulation error.

But "mixed precision" is not one universal numerical scheme.

The actual behavior depends on the supported operation and formats.

The correct question is always:

> Which values are represented in which format at which stage?

## 19. Kernels are physical programs

A mathematical operator can be implemented by one kernel or several.

Kernel boundaries matter because intermediate values may need to be materialized in memory.

A fused implementation can sometimes keep intermediates closer to the arithmetic units.

That can reduce:

- launches;
- synchronization;
- intermediate stores;
- intermediate reloads.

But a fused kernel is useful only if it preserves the required semantics and numerical tolerance.

Performance transformation does not exempt the implementation from correctness.

## 20. Fusion can change the traffic graph

Consider:

\[
y=f(x),
\qquad
z=g(y).
\]

An unfused implementation may write \(y\) to global memory and later read it back.

A fused implementation may retain \(y\) in registers or another nearer storage level.

The mathematical composition remains:

\[
z=(g\circ f)(x).
\]

The physical data-movement graph changes.

This is one reason equal high-level operation graphs can produce different runtime.

## 21. Exact finite witness

Let:

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

Then:

\[
AB=
\begin{pmatrix}
19&22\\
43&50
\end{pmatrix}.
\]

Under the chapter convention:

\[
W=12\ \text{FLOPs}.
\]

### No cross-output reuse

Charge:

- 16 input scalar loads;
- 4 output scalar stores.

With 4-byte FP32 scalars:

\[
Q_A=80\ \text{bytes}.
\]

Therefore:

\[
I_A=\frac{12}{80}=0.15\ \text{FLOP/byte}.
\]

### Perfect full-input reuse

Charge:

- 8 total input scalar loads;
- 4 output scalar stores.

Then:

\[
Q_B=48\ \text{bytes},
\]

and:

\[
I_B=\frac{12}{48}=0.25\ \text{FLOP/byte}.
\]

Same exact matrix product.

Same exact declared FLOP count.

Different charged data movement.

## 22. The bound moves even when the mathematics does not

For a hypothetical one-level machine:

\[
P_{\max}=10\ \mathrm{TFLOP/s},
\qquad
B=1\ \mathrm{TB/s}.
\]

The Roofline bounds become:

\[
P_A\le0.15\ \mathrm{TFLOP/s},
\]

and:

\[
P_B\le0.25\ \mathrm{TFLOP/s}.
\]

The example does not predict a measured GPU speedup.

It proves a narrower point:

\[
\boxed{
\text{same map + same FLOPs}
\not\Rightarrow
\text{same bandwidth-side performance bound}.
}
\]

## 23. The witness is intentionally idealized

The finite witness does not charge:

- cache-line overfetch;
- write allocate;
- instruction traffic;
- coherence;
- host-device movement;
- launch overhead;
- synchronization.

The perfect-reuse model also assumes the inputs remain available for the full tiny product.

These are not omissions to hide.

They are part of the declared witness.

A useful performance model states what it counts.

## 24. Benchmarking can create false conclusions

Hardware benchmarks are easy to misread.

A measured number depends on choices such as:

- device model;
- driver/runtime/library versions;
- data type;
- shape;
- warmup;
- synchronization;
- repetitions;
- timing region;
- transfer inclusion;
- compiler options;
- clock/power state;
- kernel selection.

A number without this context can be precise and still be uninterpretable.

## 25. Peak versus sustained performance

A vendor peak rate is a hardware specification under declared operation/type assumptions.

A measured kernel rate is an empirical observation under a workload and software stack.

An application end-to-end rate includes more than a kernel.

These three quantities should not be mixed.

The safest comparison names which one is being reported.

## 26. FLOP/s can reward doing more work

A kernel can report more FLOP/s simply because it performs extra arithmetic that the hardware handles efficiently.

That does not necessarily make the computation finish sooner.

Time-to-solution, energy, memory use, accuracy, and throughput answer different questions.

A metric is useful only when it matches the declared objective.

## 27. Hardware-aware mathematics

Hardware considerations can feed back into algorithm design.

One method may use more arithmetic but less memory traffic.

Another may trade recomputation for storage.

A third may select a structured factorization because it maps naturally to matrix units.

The correct scientific question is not:

> Is hardware corrupting the mathematics?

It is:

> Which mathematically acceptable representation exposes the physical resources the machine can use efficiently?

This is a design problem across abstraction levels.

## 28. What belongs downstream

This chapter is deliberately single-device and kernel-centric.

It does not develop:

- data parallelism;
- tensor parallelism;
- pipeline parallelism;
- expert parallelism;
- collective communication;
- interconnect topology;
- distributed KV caches;
- serving/batching systems;
- multi-device throughput/latency tradeoffs.

Those belong in:

**Scaling, Parallelism, and Serving — ATLAS-CH-SYSTEMS-001.**

Hardware-001 supplies the substrate that Systems will need:

- bandwidth;
- locality;
- arithmetic intensity;
- precision;
- resource constraints;
- benchmark discipline.

## 29. Durable boundaries

The chapter leaves the reader with nine distinctions:

1. FLOPs are not time.
2. Throughput is not latency.
3. Equal FLOPs do not imply equal bytes.
4. Arithmetic intensity needs a declared memory boundary.
5. Peak throughput is not attained throughput.
6. Occupancy is not performance.
7. Matrix algebra is not guaranteed matrix-unit efficiency.
8. Smaller precision is not guaranteed acceptable error.
9. Kernel optimization is not distributed-system optimization.

These boundaries are more useful than memorizing one accelerator's specification sheet.

## References used in this chapter

- [@WilliamsWatermanPatterson2009]
- [@NVIDIACUDAProgrammingGuide2026]
- [@NVIDIACUDABestPractices2026]

Exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-HARDWARE-001.yaml
