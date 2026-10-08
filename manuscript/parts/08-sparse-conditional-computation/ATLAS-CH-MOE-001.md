# Mixture-of-Experts Systems
<!-- ATLAS-CH-MOE-001 -->

**Epistemic status:** established sparse-expert mechanisms + audited Conditional Computation and Transformer prerequisites + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-MOE-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-MOE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MOE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MOE-001.yaml

A mixture-of-experts model can contain far more parameters than it executes for one token.

That is its central architectural attraction.

It is also the source of several confusions.

A router emits probabilities.

A capacity rule accepts or rejects assignments.

A distributed runtime moves tokens between devices.

Experts receive different training signals.

An auxiliary loss pushes traffic toward a target distribution.

These are related operations.

They are not the same object.

The governing rule of this chapter is:

> an MoE system is defined by router scores, discrete dispatch, capacity semantics, expert computation, and distributed execution together—not by the router probabilities alone.

## 1. From conditional computation to experts

SPARSE-001 established the broad conditional-computation picture:

- a model can expose more capacity than it executes for one input;
- hard and soft gating must be distinguished;
- routing overhead counts;
- arithmetic reduction does not automatically imply latency reduction.

Mixture-of-experts systems instantiate that idea with a family of alternative expert modules.

For each token, only a subset is selected.

## 2. Where experts enter a Transformer

TRANSFORMER-001 established the standard Transformer block:

- residual-stream state;
- attention;
- position-wise feed-forward transformation;
- residual paths;
- normalization.

A common sparse-expert Transformer replaces selected dense feed-forward sublayers with expert families.

Attention still performs token mixing.

The expert layer performs conditionally selected token-wise transformation.

Other designs are possible, but this is the baseline used here.

## 3. Expert family

Let a token state be:

`h_i in R^d`.

Let expert e be:

`E_e:R^d->R^d`.

There are:

`e=1,...,M`

experts.

Total expert parameter capacity can grow with M even if each token visits only one or a few experts.

That decoupling between total capacity and active work is a defining sparse-expert property.

## 4. Router logits

A router maps token state to scores:

`z_i in R^M`.

The scores can be arbitrary real values.

By themselves they do not specify which experts execute.

They are preferences or routing evidence.

## 5. Router probabilities

A common transformation is:

`p_{i,e}
=
exp(z_{i,e})
/
sum_j exp(z_{i,j})`.

Then:

`p_{i,e}>=0`

and:

`sum_e p_{i,e}=1`.

These probabilities are useful for ranking and weighting.

They are still not the executed route.

## 6. Preferred top-k route

Let:

`P_i=TopK(p_i,k)`.

For top-1:

`|P_i|=1`

before capacity handling.

For top-2 or larger k, several experts are preferred.

The word **preferred** matters.

Capacity can prevent a preferred route from executing.

## 7. Accepted dispatch

Define:

`a_{i,e} in {0,1}`.

Here:

`a_{i,e}=1`

means token i is actually dispatched to expert e after capacity and overflow policy.

This is the first object that directly describes expert execution.

A router probability can be nonzero while:

`a_{i,e}=0`.

## 8. Gate weights

Suppose token i is accepted by expert set:

`A_i={e:a_{i,e}=1}`.

A generic sparse mixture writes:

`MoE(h_i)
=
sum_(e in A_i)
alpha_{i,e} E_e(h_i)`.

The weights `alpha` might be:

- original router probabilities;
- probabilities renormalized over accepted experts;
- hard unit weights;
- another declared convention.

Dispatch and aggregation weighting are separate design choices.

## 9. Top-1 is simpler, not trivial

Switch Transformer popularized a particularly simple routing case: one expert per token.

This reduces some communication and combination complexity.

But even top-1 requires decisions about:

- capacity;
- overflow;
- balancing;
- dropped tokens;
- expert placement;
- batch composition.

One selected expert does not mean one simple system.

## 10. Capacity is not a probability threshold

Suppose an expert can process at most C routed tokens in the current routing group.

Capacity constrains:

`a_{i,e}`.

It does not change the fact that the router may assign high probability to more than C tokens.

Thus:

> capacity acts on accepted assignments, not on the probability simplex.

This distinction is load-bearing.

## 11. Nominal capacity

A common nominal form is:

`C
=
ceil(c_f k N/M)`.

Here:

- N is token count in the routing group;
- M is expert count;
- k is nominal experts per token;
- `c_f` is a capacity factor.

The exact formula and routing group are implementation choices.

The Atlas does not promote one capacity formula into a universal definition.

## 12. Demand versus accepted load

Preferred demand for expert e is:

`d_e
=
sum_i 1{e in P_i}`.

Accepted token load is:

`n_e
=
sum_i a_{i,e}`.

When capacity or overflow changes routing:

`d_e != n_e`

can occur.

This is the first reason a router histogram can differ from executed expert load.

## 13. Overflow needs policy

If:

`d_e>C`,

something must happen.

Possible policies include:

- drop overflow tokens;
- reroute them;
- send them through a fallback dense path;
- expand effective capacity;
- buffer work.

The router probabilities do not answer this question.

The overflow policy is part of the model's operational semantics.

## 14. Dropping changes the computation

If a token is dropped from the expert layer, then the executed computation differs from the nominal top-k design.

The token may:

- skip the expert transform;
- continue through a residual path;
- use some fallback;
- be handled differently by implementation.

Therefore drop rate belongs in both model-quality and systems accounting.

## 15. Rerouting changes the meaning of top-1

Suppose a token's preferred expert is full.

A reroute policy may send it to its second choice.

Then the executed expert is not the argmax expert.

This is not a contradiction.

It means:

> preferred route and accepted route are different objects.

Any analysis of router behavior should state which one it studies.

## 16. Expert token load

Define normalized accepted load:

`f_e
=
n_e / sum_j n_j`, **provided at least one expert assignment was accepted**, so \(\sum_jn_j>0\). If every token is dropped (or there are no dispatched tokens), the normalized accepted-load vector is undefined; record an empty-dispatch state and the absolute loads rather than divide by zero or claim balanced traffic.

If all top-1 tokens are accepted:

`sum_e n_e=N`.

If some are dropped:

`sum_e n_e<N`.

A load-balancing plot should therefore state its denominator.

## 17. Router probability mass

Define:

`m_e=sum_i p_{i,e}`

and normalized mass:

`q_e=m_e/N`.

Because each probability row sums to one:

`sum_e q_e=1`.

But there is no general identity:

`q_e=f_e`.

One measures soft router preference.

The other measures accepted discrete traffic.

## 18. Balance has multiple meanings

"Balanced experts" can mean several different things:

- equal token counts;
- equal router probability mass;
- equal arithmetic work;
- equal bytes communicated;
- equal device time;
- equal training signal;
- equal utility.

These are not interchangeable.

The word **balance** is incomplete without the quantity being balanced.

## 19. Auxiliary balancing objectives

Sparse expert systems often add an auxiliary objective:

`L_total
=
L_task
+
lambda L_balance`.

Different systems use different proxies and stabilizers.

The important structural point is:

`L_balance != L_task`.

A router can become more balanced under its proxy while the main task becomes worse.

Or the reverse.

## 20. Balance is a systems pressure

Why balance at all?

If one expert receives nearly every token while others sit idle:

- capacity is wasted;
- one device can become a straggler;
- communication patterns become uneven;
- underused experts may receive little training signal.

So load balancing often serves utilization and optimization stability.

It is not evidence that every expert should receive exactly the same semantic workload.

## 21. Specialization is a different claim

An expert is specialized when its behavior or performance differs systematically on some class of inputs.

Evidence might include:

- domain enrichment;
- conditional accuracy;
- feature selectivity;
- stable functional differences;
- systematic output differences.

Traffic imbalance alone does not prove any of these.

A popular expert may simply be a routing attractor.

## 22. Equal traffic does not prove equal usefulness

Two experts can each receive 10,000 tokens.

One can be critical.

The other can be nearly redundant.

Traffic counts measure use frequency.

They do not directly measure value.

This distinction will appear exactly in the finite witness.

## 23. Preferred-router collapse versus accepted-load concentration

Call **preferred-router collapse** a regime where router probability mass or preferred routes concentrate on a small expert subset under a declared statistic and horizon.

Accepted dispatch is a different object. Capacity, rerouting, or dropping can make accepted loads look more balanced than the underlying preferences.

Useful diagnostics therefore distinguish:

- probability-mass concentration;
- preferred-route concentration;
- accepted-load concentration;
- persistent overflow at particular experts.

"Collapse" without naming the object and statistic is too vague.

## 24. Expert underuse

An expert can receive so few tokens that it gets little training signal.

That is underuse.

It may be caused by:

- router bias;
- initialization;
- data distribution;
- capacity interactions;
- optimization dynamics.

Underuse is not the same thing as two experts learning the same function.

## 25. Expert redundancy

Two experts can both be heavily used and still implement similar functions.

A functional comparison might evaluate:

`E[||E_e(h)-E_j(h)||^2]`

under a declared input distribution.

Low functional distance is one possible redundancy signal.

It says something traffic counts cannot.



## 26. Capacity overload is different again

A routing system can repeatedly demand more slots than an expert is allowed to serve.

That is a capacity/overflow problem.

It may co-occur with router concentration.

But the concepts differ:

- preferred-router collapse concerns where router preferences concentrate;
- accepted-load concentration concerns executed traffic after capacity handling;
- capacity overload concerns preferred demand relative to an execution limit.

Keeping them separate helps identify the correct repair.

## 27. Expert parallelism

Large expert families are often partitioned across devices.

Let:

`dev(e)`

denote the device hosting expert e.

A routed token may originate elsewhere.

Then conditional computation becomes a distributed-systems problem.

The expert computation may be sparse while token movement is expensive.

## 28. Dispatch communication

If token i starts on:

`src(i)`

and is accepted by expert e, inter-device movement occurs when:

`src(i) != dev(e)`.

A simple communication-count proxy is:

`K_comm
=
sum_(i,e)
a_{i,e}
1{src(i)!=dev(e)}`.

This is only a count.

Actual cost depends on:

- representation size;
- collective implementation;
- batching;
- topology;
- return traffic;
- synchronization.

## 29. All-to-all is not free

Expert-parallel systems often group tokens by destination expert, exchange them, compute expert outputs, and return results.

This can require collective communication.

Therefore:

> low active arithmetic can coexist with high communication cost.

GShard and Switch make this systems issue central to large sparse-expert execution.

## 30. Stragglers matter

Suppose expert computation is parallel.

Step completion can depend on the slowest device/expert path.

Even if average load is good, one overloaded expert can dominate latency.

This is another reason average token count is not enough.

Peak and tail behavior matter.

## 31. Equal token counts need not mean equal compute

If every expert has the same architecture and input shape, equal accepted counts can equalize one arithmetic proxy.

But experts may differ in:

- size;
- precision;
- hardware placement;
- kernel efficiency;
- input shape;
- cache locality.

Then:

`n_e=n_j`

does not imply:

`C_e=C_j`.

The load unit must match the cost question.

## 32. Training and serving need not use the same routing semantics

During training, the system may tolerate:

- router noise;
- auxiliary balance pressure;
- higher capacity factors;
- token dropping;
- larger batches.

Serving may prioritize:

- determinism;
- tail latency;
- replica placement;
- availability;
- bounded communication.

A routing analysis should therefore state the execution phase.

## 33. The exact witness: six tokens

Use six tokens and three experts.

The router probabilities are:

| token | E1 | E2 | E3 |
|---|---:|---:|---:|
| t1 | 9/10 | 1/20 | 1/20 |
| t2 | 4/5 | 3/20 | 1/20 |
| t3 | 1/2 | 1/10 | 2/5 |
| t4 | 1/20 | 9/10 | 1/20 |
| t5 | 1/20 | 3/4 | 1/5 |
| t6 | 1/20 | 1/20 | 9/10 |

Every row sums to one.

## 34. Naive top-1 preferences

The preferred experts are:

- t1 -> E1;
- t2 -> E1;
- t3 -> E1;
- t4 -> E2;
- t5 -> E2;
- t6 -> E3.

So preferred loads are:

`(3,2,1)`.

Let capacity be:

`C=2`.

E1 is overloaded.

## 35. Keep the strongest E1 assignments

For E1:

- t1 has probability 9/10;
- t2 has probability 4/5;
- t3 has probability 1/2.

The declared overflow policy retains the two highest E1 preferences:

`t1,t2`.

Token t3 becomes overflow.

## 36. Reroute the overflow token

For t3:

- E2 probability is 1/10;
- E3 probability is 2/5.

E3 has one spare slot.

Therefore:

`t3:E1->E3`.

Final accepted assignments are:

- E1: t1,t2;
- E2: t4,t5;
- E3: t3,t6.

Accepted loads are:

`(2,2,2)`.

## 37. Accepted load is perfectly balanced

Accepted load fractions are:

`f=(1/3,1/3,1/3)`.

For the squared count-imbalance statistic:

`B_count
=
sum_e(f_e-1/3)^2`,

we get:

`B_count=0`.

By this metric, routing is perfectly balanced.

## 38. Router probability mass is not balanced

Summing probabilities over all six tokens gives:

`m=(47/20,2,33/20)`.

Normalize by six:

`q=(47/120,1/3,11/40)`.

This is not uniform.

Therefore:

`f != q`.

Balanced accepted counts have not made the router's soft preference distribution uniform.

## 39. Exact probability-imbalance value

The offsets from uniform are:

`47/120-1/3=7/120`;

`1/3-1/3=0`;

`11/40-1/3=-7/120`.

Therefore:

`B_prob
=
2(7/120)^2
=
49/7200`.

So the exact witness has:

`B_count=0`

but:

`B_prob>0`.

The two balance notions disagree.

## 40. Equal traffic still does not imply equal usefulness

Now attach a toy post-routing utility diagnostic.

Let final assignment utilities be:

- E1 on t1: 4;
- E1 on t2: 4;
- E2 on t4: 2;
- E2 on t5: 2;
- E3 on t3: 1;
- E3 on t6: 1.

Expert totals are:

`(8,4,2)`.

Traffic remains:

`(2,2,2)`.

Equal counts do not imply equal evaluated utility.

## 41. The utility numbers are not router scores

This distinction matters.

The router probability says:

> how strongly did the router prefer this expert?

The toy utility says:

> under a separate evaluation, how much value did this accepted expert assignment contribute?

These need not match.

Indeed, one research question in MoE systems is whether the router reliably sends inputs to experts that are actually useful for them.

## 42. Drop instead of reroute

Now keep the same probability table and same capacity.

Change only the overflow policy.

Drop t3 instead of rerouting it.

Then accepted loads become:

`(2,2,1)`.

Drop rate is:

`1/6`.

The router has not changed.

The executed MoE has.

## 43. Overflow policy changes arithmetic

Assume identical expert cost c per accepted token.

Under rerouting:

`C_expert=6c`.

Under dropping:

`C_expert=5c`.

Thus capacity semantics alter realized expert arithmetic even with identical router probabilities.

This is a concrete version of the SPARSE-001 distinction between routing logic and executed work.

## 44. Balanced counts do not settle communication

Suppose E1, E2, and E3 live on different devices.

Even with:

`(2,2,2)`

accepted token counts, the communication pattern depends on where the tokens originated.

One routing assignment can be local.

Another can require extensive cross-device exchange.

Count balance is therefore not a communication theorem.

## 45. Shazeer et al.: sparse gating and balancing

Shazeer et al. introduced a sparsely gated MoE layer at large scale, with a trainable gating network selecting a sparse combination of experts.

Their work also makes balancing pressure explicit because highly uneven expert use creates practical problems.

The Atlas uses this as a primary historical mechanism.

It does not treat the original routing loss or expert layout as universally canonical.

## 46. GShard: capacity meets distributed execution

GShard places sparse MoE computation inside a large Transformer and combines it with automatic sharding.

That makes two facts impossible to ignore:

- routing creates per-expert capacity constraints;
- experts distributed over accelerators create communication and placement problems.

The Atlas uses GShard to connect algorithmic routing to expert-parallel execution.

## 47. Switch: top-1 simplifies one axis

Switch Transformer reduces the number of selected experts per token to one.

This can simplify routing and communication relative to multi-expert mixtures.

It does not remove:

- capacity;
- balancing;
- training instability;
- distributed communication.

The important lesson is that simplification of one routing axis leaves a multi-layer system.

## 48. ST-MoE: stability and transfer remain system properties

ST-MoE studies sparse expert design with emphasis on training stability and downstream transfer.

That matters because an MoE system cannot be judged from parameter count or routing sparsity alone.

Useful questions include:

- does training remain stable?
- do experts receive enough signal?
- does specialization persist?
- does sparse pretraining transfer?

These questions belong downstream of the basic routing semantics established here.

## 49. A practical MoE ledger

Before accepting an MoE result, record:

| Field | Question |
|---|---|
| tokens | What is the routing group and token count? |
| experts | How many, and what does each expert compute? |
| router | Which logits/probabilities are produced? |
| top-k | How many experts are preferred per token? |
| gate weights | How are accepted expert outputs weighted? |
| capacity | Which unit and formula set expert capacity? |
| overflow | Drop, reroute, fallback, buffer, or other? |
| accepted load | How many assignments actually execute per expert? |
| probability mass | What soft router mass goes to each expert? |
| auxiliary loss | Which balance/stability proxy is optimized? |
| drops | Which tokens receive no expert execution? |
| specialization | What functional evidence supports the claim? |
| redundancy | How are expert functions compared? |
| placement | Which device hosts each expert? |
| communication | Which token/activation bytes move? |
| phase | Training or inference/serving? |
| quality boundary | What does balance not prove? |

This ledger turns "MoE routing" into an auditable system description.

## 50. Failure modes

### Probability-equals-dispatch

Soft router mass is treated as executed expert traffic.

### Top-k-equals-execution

Preferred experts are reported without capacity/overflow semantics.

### Balanced-counts-equals-specialization

Equal traffic is used as evidence that experts learned distinct useful functions.

### Balanced-counts-equals-cheap

Equal accepted loads are treated as proof of equal latency or communication.

### Collapse-as-one-word

Preferred-router concentration, accepted-load concentration, underuse, redundancy, and capacity overload are conflated.

### Auxiliary-loss-equals-task-objective

A balancing proxy is treated as if it directly measures task quality.

### Sparse-parameters-equals-sparse-system-cost

Active expert arithmetic is counted while router, communication, padding, and synchronization are ignored.

## 51. What the exact witness establishes

The companion witness proves:

- naive top-1 demand is `(3,2,1)`;
- capacity is 2;
- t3 is the lowest-confidence E1 token;
- its best available alternative is E3;
- rerouting t3 yields accepted loads `(2,2,2)`;
- probability mass is `(47/20,2,33/20)`;
- normalized mass is `(47/120,1/3,11/40)`;
- count imbalance is 0;
- probability-mass imbalance is `49/7200`;
- toy utility totals are `(8,4,2)`;
- drop-on-overflow instead yields `(2,2,1)` and drop rate `1/6`;
- under equal expert token cost, reroute and drop policies use expert arithmetic `6c` and `5c`.

No universal routing optimum is inferred.

## 52. Downstream handoff: Router Dynamics

**ATLAS-CH-ROUTERDYN-001** may now assume:

- logits/probabilities versus accepted dispatch;
- capacity and overflow semantics;
- count-load versus probability-mass diagnostics;
- preferred-router concentration versus accepted-load concentration versus underuse versus redundancy;
- explicit evidence requirements for specialization.

It must independently develop temporal churn, instability, commutators, spectral diagnostics, and route evolution.

## 53. Downstream handoff: Systems

**ATLAS-CH-SYSTEMS-001** may now assume:

- expert placement;
- dispatch communication;
- capacity;
- accepted per-expert work;
- active versus total expert capacity;
- straggler boundaries.

It must independently develop hardware/system cost models, communication topology, serving constraints, and measured efficiency.

The MoE lesson is:

> sparse experts create conditional capacity, not free capacity. The router proposes; the capacity policy dispatches; the experts compute; the network moves data; and each layer needs its own evidence.

## References used in this chapter

- Noam Shazeer et al., *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*, 2017, arXiv:1701.06538.
- Dmitry Lepikhin et al., *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding*, 2020, arXiv:2006.16668.
- William Fedus, Barret Zoph, and Noam Shazeer, *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*, Journal of Machine Learning Research 23(120), 1–39, 2022.
- Barret Zoph et al., *ST-MoE: Designing Stable and Transferable Sparse Expert Models*, 2022, arXiv:2202.08906.

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-MOE-001.yaml
