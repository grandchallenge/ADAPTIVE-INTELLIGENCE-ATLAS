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
n_e / sum_j n_j`.

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

## 23. Router collapse

Call **router collapse** a regime where traffic becomes highly concentrated on a small expert subset under a declared statistic and horizon.

Possible symptoms include:

- low accepted-load entropy;
- persistent capacity overflow at a few experts;
- many rarely used experts.

The diagnosis should specify the metric.

"Collapse" without a statistic is too vague.

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

