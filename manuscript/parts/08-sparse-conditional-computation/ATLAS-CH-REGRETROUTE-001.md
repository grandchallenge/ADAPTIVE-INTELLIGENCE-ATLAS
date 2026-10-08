# Routing as Online Decision Making
<!-- ATLAS-CH-REGRETROUTE-001 -->

**Epistemic status:** audited Router Dynamics substrate + primary adversarial-bandit/shifting-expert authority + Atlas-owned exact finite routing witnesses.  
**Specification:** manuscript/specifications/ATLAS-CH-REGRETROUTE-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-REGRETROUTE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-REGRETROUTE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-REGRETROUTE-001.yaml

A sparse router changes over time.

That does not yet make it an online decision problem.

To speak about regret, one must say:

- what action was actually taken;
- what actions were feasible;
- when loss was incurred;
- what feedback arrived;
- what comparator is allowed;
- what kind of nonstationarity is being measured.

The governing rule is:

\[
\boxed{
\text{diagnose routing first; define regret only after the decision problem is explicit.}
}
\]

## 1. Router dynamics are not regret theory

Router Dynamics already distinguished:

\[
\text{probability}
\to
\text{preference}
\to
\text{dispatch}
\to
\text{load}.
\]

It also showed that:

- stable load need not mean stable token assignment;
- zero preferred-route churn need not mean zero probability drift;
- equal singular spectra need not mean equal dynamics.

Those are temporal diagnostics.

Regret asks a different question:

> how much cumulative loss did the routing decisions incur relative to a declared comparator class?

## 2. Preferred route is not always the executed action

Let:

\[
p_t
\]

be the preferred route proposed by the router.

Let:

\[
F_t
\]

be the set of dispatch actions that remain feasible after capacity and availability constraints.

Let:

\[
a_t\in F_t
\]

be the accepted/executed dispatch.

When capacity binds:

\[
a_t\neq p_t
\]

can occur.

That distinction matters because the executed action is the one that actually consumes capacity and incurs the declared decision loss.

## 3. Capacity is part of the decision semantics

Write:

\[
a_t=G_t(p_t,\kappa_t),
\]

where \(\kappa_t\) contains the relevant capacity/overflow state.

The map \(G_t\) can:

- accept the proposal;
- reroute it;
- reject it;
- defer it;
- send it to overflow capacity.

The online problem is underspecified until this behavior is declared.

## 4. Loss happens after the accepted action

Use the ordering:

1. observe the pre-action context;
2. propose a route;
3. enforce feasibility/capacity;
4. execute accepted dispatch;
5. incur loss;
6. reveal feedback.

Denote the accepted-action loss by:

\[
\ell_t(a_t).
\]

If future losses are used to choose \(a_t\), the object is an oracle or hindsight construction, not an ordinary online policy.

## 5. Feedback must be named

Under full information, after round \(t\) the learner receives:

\[
\{\ell_t(a):a\in F_t\}.
\]

Under bandit feedback, it receives only:

\[
\ell_t(a_t).
\]

Auer, Cesa-Bianchi, Freund, and Schapire treat adversarial/nonstochastic multi-armed bandits under partial feedback [@AuerEtAl2002Nonstochastic].

That distinction changes what an online router can infer and guarantee.

## 6. Comparator comes before regret

Let:

\[
\Pi
\]

be a declared class of comparison policies or action sequences.

Then define:

\[
R_T^{\Pi}(a)
=
\sum_{t=1}^T\ell_t(a_t)
-
\min_{u\in\Pi}
\sum_{t=1}^T\ell_t(u_t).
\]

Without \(\Pi\), “regret” is incomplete.

## 7. Static regret asks one question

A static comparator uses one fixed route for every round, restricted here to routes in \(\bigcap_{t=1}^T F_t\). If the intersection is empty, a feasible static comparator does not exist and a different comparator or an expressly labeled counterfactual benchmark is needed.

It asks:

> how much worse was the router than the best single fixed expert in hindsight?

That is useful when one expert should remain globally best.

It is not the only plausible sparse-routing benchmark.

## 8. Shifting regret asks another question

Suppose which expert is best changes over time.

Let:

\[
\Pi_S(F_{1:T})
=
\left\{
 u_{1:T}:
 u_t\in F_t\ \text{for every }t,\quad
 \sum_{t=2}^T\mathbf 1[u_t\neq u_{t-1}]
 \le S
\right\}.
\]

Now the comparator may switch at most \(S\) times **while respecting the same declared feasible accepted-dispatch sets**. This version assumes the comparator class is nonempty; otherwise the minimum in the regret definition is not defined without an additional convention. A comparator allowed to use capacity-infeasible actions is a different, explicitly counterfactual benchmark.

Herbster and Warmuth study tracking a best expert that can change over segments [@HerbsterWarmuth1998Tracking].

This is the comparator style used in the exact witness.

## 9. One common finite routing problem

Take two accepted actions:

\[
A,\ B.
\]

Use four rounds.

Both routes remain feasible every round:

\[
F_t=\{A,B\}.
\]

Use losses:

\[
\begin{array}{c|cc}
 t&A&B\\
\hline
1&0&1\\
2&1&0\\
3&0&1\\
4&1&0
\end{array}
\]

The loss-minimizing route alternates every round.

## 10. The shifting comparator

Allow up to three switches:

\[
\Pi_3.
\]

The unique zero-loss comparator is:

\[
(A,B,A,B).
\]

So the hindsight comparator loss is:

\[
0.
\]

## 11. A perfectly stable route can regret its stability

Consider:

\[
a^{\mathrm{stay}}=(A,A,A,A).
\]

Its accepted-dispatch churn is:

\[
0.
\]

Its cumulative loss is:

\[
0+1+0+1=2.
\]

Therefore its shifting regret is:

\[
\boxed{2}.
\]

The route is maximally stable.

It is not regret-optimal for the shifting comparator.

## 12. A maximally churning route can be regret-optimal

Now use:

\[
a^{\mathrm{track}}=(A,B,A,B).
\]

Its switch count is:

\[
3.
\]

Its cumulative loss is:

\[
0.
\]

Therefore its shifting regret is:

\[
\boxed{0}.
\]

The route churns every possible time.

It is nevertheless comparator-optimal.

## 13. Churn is not a regret surrogate

The two policies use the same:

- action space;
- feasible sets;
- horizon;
- losses;
- feedback;
- comparator class.

Yet:

\[
0<3
\]

for churn, while:

\[
2>0
\]

for regret.

So:

\[
\boxed{
\text{low churn}
\not\Rightarrow
\text{low regret}
}
\]

and:

\[
\boxed{
\text{high churn}
\not\Rightarrow
\text{high regret}.
}
\]

## 14. Static regret tells a different story

The fixed action \(A\) loses two.

The fixed action \(B\) also loses two.

So best static comparator loss is two.

Against that comparator:

- stay-on-\(A\) has regret zero;
- the alternating tracker has regret \(-2\).

The numbers changed because the question changed.

Comparator choice is part of the meaning of regret.

## 15. Negative static regret is not an error

The alternating route beats every fixed comparator.

Therefore static regret can be negative for a realized sequence under this definition.

That simply means the policy outperformed the restricted comparator class.

It does not invalidate the calculation.

## 16. Optionality is feasible choice

Define:

\[
O_t=|F_t|-1.
\]

This counts feasible accepted alternatives other than the executed action.

In the exact witness:

\[
O_t=1
\]

for every round.

Both routes have the same optionality.

Their regret differs.

So optionality is not regret either.

## 17. Correction capacity is ability to change course

One operational form is remaining switch budget.

Let allowed switch count be \(S\).

Before round \(t\), let:

\[
N_t
=
\sum_{s=2}^{t-1}
\mathbf1[a_s\neq a_{s-1}].
\]

Define:

\[
K_t=\max(0,S-N_t).
\]

This says how many further route changes the controller may still make under the declared switch budget.

## 18. Optionality and correction capacity are distinct

A router can have many feasible alternatives but no remaining switching budget.

Or it can have switching budget but only one feasible action because capacity is saturated.

Thus:

\[
\boxed{
\text{available alternatives}
\neq
\text{ability to correct}.
}
\]

## 19. The stay policy preserves correction capacity

In the exact witness, \(S=3\).

The stay route uses no switches.

Its remaining switch budget remains high.

Yet it accumulates regret two.

Preserving correction capacity is not automatically the same as using it well.

## 20. The tracking policy spends correction capacity

The alternating route consumes switch budget.

Its remaining correction capacity falls over time.

But it obtains zero shifting regret.

Again, correction capacity is a resource, not a performance score.

## 21. Capacity should constrain the comparator too

Suppose expert \(B\) is full at round \(t\).

Then \(B\notin F_t\).

A feasible comparator should normally obey the same restriction.

Otherwise the regret gap mixes online routing quality with access to an impossible action.

An unconstrained oracle comparator can still be informative, but it must be labeled as counterfactual.

## 22. Preferred-route regret is a separate counterfactual

Suppose the router prefers \(B\), but capacity sends the token to \(A\).

One can measure:

- accepted-dispatch regret;
- preferred-route counterfactual regret.

They answer different questions.

The default REGRETROUTE object is accepted-dispatch regret.

## 23. Capacity can hide or create churn

Changing capacity can make accepted dispatch move even while preference remains fixed.

It can also make accepted dispatch remain fixed while preference changes.

Therefore ROUTERDYN's typed observables are required even after regret enters the analysis.

## 24. Load balance is not online optimality

A capacity mechanism can enforce balanced load.

Balanced load can be operationally valuable.

But it does not imply that accepted decisions minimize cumulative routing loss.

So:

\[
\boxed{
\text{balanced load}
\not\Rightarrow
\text{low regret}.
}
\]

## 25. Specialization is not regret

A specialization statistic asks which token classes or features tend to use an expert.

Regret asks how losses compare to a benchmark.

An expert can be highly specialized and still be wrong for the current token.

A broad expert can be the regret-minimizing action under another objective.

## 26. Probability drift is not regret

Router probabilities can drift substantially while the accepted route remains unchanged.

Then accepted-dispatch regret can remain identical.

Conversely, tiny probability movement near a routing threshold can change the accepted action and cumulative regret.

## 27. If switching is costly, put it in the loss

Suppose switching has penalty \(\lambda\).

Use:

\[
\widetilde\ell_1=\ell_1(a_1),
\qquad
\widetilde\ell_t
=
\ell_t(a_t)
+
\lambda\mathbf1[a_t\neq a_{t-1}]
\quad(t=2,\ldots,T).
\]

This convention charges only switches **between** the \(T\) executed actions; there is no undeclared \(a_0\) or first-round switching penalty. A deployment that charges initialization or migration from a pre-existing route must declare that initial route and charge separately.

Now churn enters the decision objective directly.

For the alternating route, three switches contribute:

\[
3\lambda.
\]

A large enough switching cost can make stability preferable.

That is not a contradiction.

It is a different objective.

## 28. Nonstationarity must be typed

The exact witness has changing roundwise losses.

But empirical router nonstationarity can come from:

- changing contexts;
- changing expert parameters;
- changing capacity;
- optimizer-state drift;
- changing token mix;
- reward-model drift.

Those mechanisms can produce different regret problems.

## 29. Bandit feedback changes the online problem

Under bandit feedback, the router sees only the loss of the accepted action.

It does not immediately know whether another expert would have been better.

This is why exploration matters in adversarial bandits [@AuerEtAl2002Nonstochastic].

The exact witness computes realized regret after the loss table is fixed; it does not claim the online policy knows the hindsight-optimal route.

## 30. Delayed feedback weakens correction

If routing loss arrives late, the controller can spend several rounds without seeing a mistake.

That changes the operational value of correction capacity.

The exact witness uses immediate post-round feedback.

Delayed-feedback guarantees require separate analysis.

## 31. Hindsight comparator is not an executable oracle

The comparator may use the full realized sequence to define the benchmark.

The online router cannot.

Regret measures the gap to hindsight performance.

It does not prove the comparator was available as a real-time policy.

## 32. Downstream task loss is still separate

Routing loss can be defined from:

- latency;
- communication;
- expert quality;
- capacity violation;
- token-level prediction loss;
- a weighted combination.

A low routing regret under one declared loss does not automatically imply low end-to-end task loss under another metric.

An interface theorem or empirical relation is needed.

## 33. A practical routing-decision record

A regret-bearing routing experiment should record at least:

- context/token identity or sampling rule;
- router probability/logit state;
- preferred route;
- feasible action set;
- capacity/overflow state;
- accepted dispatch;
- incurred loss/reward;
- feedback revealed;
- comparator class;
- switch/churn metric;
- optionality;
- correction-capacity state;
- regret notion;
- downstream task metric separately.

Without these fields, “router regret” is underspecified.

## 34. Durable non-implications

REGRETROUTE rejects:

\[
\text{low churn}
\not\Rightarrow
\text{low regret},
\]

\[
\text{high churn}
\not\Rightarrow
\text{high regret},
\]

\[
\text{balanced load}
\not\Rightarrow
\text{low regret},
\]

\[
\text{stable probabilities}
\not\Rightarrow
\text{low regret},
\]

\[
\text{high optionality}
\not\Rightarrow
\text{low regret},
\]

and:

\[
\text{low routing regret}
\not\Rightarrow
\text{low downstream task loss without an explicit bridge}.
\]

## 35. Closing view

A router has dynamics before it has regret.

Once routing is treated as online decision making, the burden becomes explicit:

- name the executed action;
- constrain the feasible set;
- state when loss arrives;
- state what feedback is revealed;
- define the comparator;
- define optionality and correction capacity;
- state what kind of nonstationarity is allowed.

The four-round witness then gives the smallest useful lesson:

\[
(A,A,A,A)
\]

has zero churn but regret two, while:

\[
(A,B,A,B)
\]

has three switches but regret zero under the same common frame.

So the right conclusion is not “stable routing is good” or “adaptive routing is good.”

It is:

\[
\boxed{
\text{routing quality is comparator-, loss-, feedback-, feasibility-, and capacity-relative.}
}
\]

## References used in this chapter

- [@AuerEtAl2002Nonstochastic]
- [@HerbsterWarmuth1998Tracking]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-REGRETROUTE-001.yaml
