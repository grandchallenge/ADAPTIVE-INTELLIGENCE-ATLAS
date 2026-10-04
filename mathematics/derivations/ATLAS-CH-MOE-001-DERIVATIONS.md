# ATLAS-CH-MOE-001 — Formal and Derivation Packet

## 1. Token and expert objects

Let token states be:

`h_i in R^d`

for `i=1,...,N`.

Let experts be:

`E_e:R^d->R^d`

for `e=1,...,M`.

A router maps each token to logits:

`z_i in R^M`.

Router probabilities are:

`p_{i,e}=exp(z_{i,e}) / sum_j exp(z_{i,j})`.

They satisfy:

`p_{i,e}>=0`;

`sum_e p_{i,e}=1`.

## 2. Router probability is not dispatch

Define a preferred top-k set:

`P_i=TopK(p_i,k)`.

This is still not a complete executed route.

Capacity and overflow policy can modify the preferred assignment.

Let:

`a_{i,e} in {0,1}`

denote accepted dispatch.

Then:

`a_{i,e}=1`

means expert e actually receives token i under the declared policy.

In general:

`e in P_i`

does not imply:

`a_{i,e}=1`.

## 3. Gate weights

For accepted set:

`A_i={e:a_{i,e}=1}`,

one generic sparse mixture is:

`MoE(h_i)=sum_{e in A_i} alpha_{i,e} E_e(h_i)`.

Possible conventions include:

- use original router probabilities;
- renormalize over accepted experts;
- use a hard unit weight for top-1.

The aggregation convention must be declared.

## 4. Transformer insertion point

TRANSFORMER-001 supplies the standard residual-stream and position-wise feed-forward sublayer.

A common sparse-expert design replaces selected dense feed-forward sublayers with an MoE feed-forward sublayer.

This chapter does not treat attention itself as the expert family unless a different architecture explicitly declares that choice.

## 5. Active versus total capacity

Let each expert contain parameter count `P_e`.

Total expert parameters are:

`P_total=sum_e P_e`.

For one token, active expert parameters depend on accepted route:

`P_active(i)=sum_e a_{i,e} P_e`.

Sparse routing can make:

`P_active(i) << P_total`.

This inherits the active-versus-total-capacity distinction from SPARSE-001.

## 6. Expert token load

Accepted token load for expert e is:

`n_e=sum_i a_{i,e}`.

Normalized accepted load is:

`f_e=n_e / sum_j n_j`

when at least one assignment is accepted.

For top-1 with no dropped tokens:

`sum_e n_e=N`.

With drops:

`sum_e n_e<N`.

## 7. Router probability mass

Define:

`m_e=sum_i p_{i,e}`.

Normalized probability mass is:

`q_e=m_e/N`.

Because:

`sum_e p_{i,e}=1`,

we have:

`sum_e q_e=1`.

But:

`q_e`

need not equal accepted load fraction:

`f_e`.

## 8. Capacity

A nominal capacity rule can be written:

`C=ceil(c_f k N/M)`.

Here:

- `c_f` is a capacity factor;
- `k` is nominal routed experts per token;
- `N` is tokens in the relevant routing group;
- `M` is expert count.

This is a representative formula, not a universal implementation rule.

Capacity granularity may be per batch, device group, expert group, or other declared unit.

## 9. Overload

Preferred top-k demand for expert e is:

`d_e=sum_i 1{e in P_i}`.

Expert e is overloaded when:

`d_e>C`.

Overload is a demand/capacity relation.

It is not the same as:

- high probability mass;
- high utility;
- high compute time;
- expert specialization.

## 10. Overflow policy

Define a capacity operator:

`Cap(P,p,C,pi_overflow)->A`

that turns preferred routes P into accepted routes A.

Different `pi_overflow` produce different A from the same router probabilities.

Therefore executed MoE behavior is a property of:

`(p,k,C,pi_overflow)`

rather than of p alone.

## 11. Drop policy

For top-1, one possible policy is:

- each expert retains at most C preferred tokens;
- excess tokens receive no expert execution.

Then dropped-token indicator is:

`d_i=1{sum_e a_{i,e}=0}`.

Drop rate is:

`D=(1/N) sum_i d_i`.

A nonzero D changes realized computation and possibly model quality.

## 12. Reroute policy

Another policy is:

- retain C highest-preference tokens at overloaded expert;
- send overflow token to its best alternative expert with free capacity;
- repeat until accepted or alternatives exhausted.

This changes actual dispatch away from naive top-1.

A rerouted token can therefore execute an expert that was not its highest-probability choice.

## 13. Load-balance proxy

One simple load imbalance statistic is:

`B_count=sum_e (f_e-1/M)^2`.

It vanishes when accepted counts are exactly equal.

A probability-mass analogue is:

`B_prob=sum_e (q_e-1/M)^2`.

These are different functions.

Zero count imbalance does not imply zero probability-mass imbalance.

## 14. Auxiliary balancing objectives

MoE systems often add auxiliary terms designed to discourage concentrated routing.

Abstractly:

`L_total=L_task+lambda L_balance`.

The balancing term may depend on:

- token fractions;
- router probability mass;
- importance/load proxies;
- z-loss or other router stabilization terms.

The exact source-specific formulas must not be conflated.

The Atlas uses only the general distinction:

`L_balance != L_task`.

## 15. Balance is not specialization

Let expert usefulness under an external evaluation be:

`u_e=sum_{i:a_{i,e}=1} U(i,e)`.

Equal token counts:

`n_1=...=n_M`

do not imply:

`u_1=...=u_M`.

Nor do they prove experts implement different functions.

Specialization is a functional/conditional-performance claim.

## 16. Preferred-route concentration versus accepted-load concentration

Let preferred top-k demand fractions be:

`g_e=d_e/sum_j d_j`.

A preferred-route entropy is:

`H_pref=-sum_e g_e log g_e`.

Accepted-load entropy is separately:

`H_accept=-sum_e f_e log f_e`.

Capacity, rerouting, or dropping can make these diagnostics disagree. In particular, accepted loads can look balanced even when preferred routing is concentrated. A router-collapse claim should therefore state whether it concerns logits/probability mass, preferred routes, or accepted dispatch, together with its horizon and threshold.

## 17. Expert underuse

Expert e is underused relative to a declared horizon if:

`n_e`

or its accumulated training assignments are below a declared threshold.

Underuse can reduce learning signal.

It is distinct from expert functional redundancy.

## 18. Expert redundancy

Experts e and j can be functionally similar even if both are well used.

One possible diagnostic on evaluation distribution `D_eval` is:

`R_{e,j}=E_{h~D_eval}[||E_e(h)-E_j(h)||^2]`.

Small `R_{e,j}` indicates similarity under that metric/distribution.

It does not follow from traffic counts alone.

## 19. Specialization

A specialization claim should name:

- input partition/feature/domain;
- expert identity;
- performance or representation statistic;
- stability horizon;
- comparison baseline.

For example, domain enrichment:

`Pr(domain=d | routed_to=e)`

can show traffic specialization.

It does not automatically show expert e is causally better for domain d.

## 20. Expert parallelism

Let:

`dev(e)`

map expert e to a device.

If token i originates on device:

`src(i)`,

then accepted route `a_{i,e}=1` induces inter-device dispatch when:

`src(i) != dev(e)`.

Communication volume depends on token representation size, routing, placement, batching, and implementation.

## 21. Communication count

A simple dispatch-count proxy is:

`K_comm=sum_{i,e} a_{i,e} 1{src(i)!=dev(e)}`.

Bytes moved can be modeled as:

`B_comm=K_comm * bytes_per_token_state`

only under a fixed-size one-way payload simplification.

Real systems can require gather/scatter, return traffic, metadata, padding, collective overhead, and synchronization.

## 22. Expert compute

If expert e costs:

`c_e`

per accepted token under a declared model, then:

`C_expert=sum_e c_e n_e`.

Even if token counts are balanced, heterogeneous:

`c_e`

can make realized expert compute unbalanced.

Thus count balance is not compute balance.

## 23. Stragglers

Parallel step time can depend on the slowest expert/device path.

A simple idealized lower-level proxy is:

`T_expert=max_e c_e n_e`

plus communication/synchronization costs.

This is not a wall-clock theorem.

It only exposes why average load is insufficient for peak/straggler reasoning.

## 24. Exact witness probability table

Use N=6 tokens and M=3 experts.

Rows are router probabilities:

`t1=(9/10,1/20,1/20)`;

`t2=(4/5,3/20,1/20)`;

`t3=(1/2,1/10,2/5)`;

`t4=(1/20,9/10,1/20)`;

`t5=(1/20,3/4,1/5)`;

`t6=(1/20,1/20,9/10)`.

Each row sums to one.

## 25. Naive top-1 route

Argmax choices are:

- t1 -> E1;
- t2 -> E1;
- t3 -> E1;
- t4 -> E2;
- t5 -> E2;
- t6 -> E3.

Preferred loads:

`d=(3,2,1)`.

With capacity:

`C=2`,

E1 is overloaded by one token.

## 26. Retained E1 tokens

E1 probabilities among its preferred tokens are:

- t1: 9/10;
- t2: 4/5;
- t3: 1/2.

Retaining the top C=2 keeps:

`t1,t2`.

Overflow token is:

`t3`.

## 27. Reroute t3

Alternative probabilities for t3 are:

- E2: 1/10;
- E3: 2/5.

E3 has one free slot.

Therefore the declared policy sends:

`t3->E3`.

Final accepted assignments are:

- E1: t1,t2;
- E2: t4,t5;
- E3: t3,t6.

Final loads:

`n=(2,2,2)`.

No token is dropped.

## 28. Probability masses

Sum E1 probabilities:

`9/10+4/5+1/2+1/20+1/20+1/20
=
47/20`.

Sum E2 probabilities:

`1/20+3/20+1/10+9/10+3/4+1/20
=
2`.

Sum E3 probabilities:

`1/20+1/20+2/5+1/20+1/5+9/10
=
33/20`.

Thus:

`m=(47/20,2,33/20)`.

Normalized:

`q=(47/120,1/3,11/40)`.

Final accepted load fractions are:

`f=(1/3,1/3,1/3)`.

Therefore:

`f != q`.

## 29. Count-balance metrics

For accepted loads:

`B_count=0`.

For probability mass:

`B_prob
=
(47/120-1/3)^2
+
(1/3-1/3)^2
+
(11/40-1/3)^2`.

Simplify:

`47/120-40/120=7/120`.

`11/40-1/3=33/120-40/120=-7/120`.

Therefore:

`B_prob=2*(7/120)^2=49/7200`.

Perfect accepted-count balance coexists with nonzero router-probability imbalance.

## 30. Utility counterexample

On final assignments define toy utility contributions:

- U(t1,E1)=4;
- U(t2,E1)=4;
- U(t4,E2)=2;
- U(t5,E2)=2;
- U(t3,E3)=1;
- U(t6,E3)=1.

Then:

`u=(8,4,2)`.

Counts remain:

`n=(2,2,2)`.

Therefore equal traffic does not imply equal evaluated utility.

## 31. Drop-policy counterfactual

Keep the same router probabilities and C=2.

Under drop-on-overflow:

- retain t1,t2 at E1;
- drop t3;
- keep t4,t5 at E2;
- keep t6 at E3.

Accepted loads:

`n_drop=(2,2,1)`.

Drop rate:

`D=1/6`.

Same router, different overflow policy, different execution.

## 32. Identical-expert compute witness

Assume each expert has equal per-token arithmetic cost:

`c_1=c_2=c_3=c`.

Under reroute final loads:

`C_expert=6c`.

Under drop policy:

`C_expert=5c`.

Thus capacity semantics change realized expert arithmetic even with identical router probabilities.

## 33. Communication boundary

If E1, E2, E3 live on separate devices, the final route can require token exchange.

No conclusion about latency follows from:

`C_expert=6c`

without communication and synchronization terms.

This directly inherits SPARSE-001's resource-vector boundary.

## 34. Training versus serving

During training, routing policy may include:

- auxiliary balance losses;
- noise;
- capacity factors chosen for throughput;
- dropped tokens.

Serving may instead prioritize:

- determinism;
- tail latency;
- replica placement;
- batch composition;
- availability.

Therefore a routing policy must be bound to its execution phase.

## 35. Downstream interface

ROUTERDYN-001 may consume:

- logits/probabilities versus dispatch;
- capacity/overflow semantics;
- load/probability metrics;
- collapse/underuse/redundancy distinctions;
- specialization evidence requirements.

SYSTEMS-001 may consume:

- expert placement;
- dispatch/communication counts;
- expert capacity;
- peak/straggler resource semantics.

Neither may infer performance, stability, or efficient hardware execution from balanced token counts alone.
