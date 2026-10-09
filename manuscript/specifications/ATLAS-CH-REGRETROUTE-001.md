# Chapter Specification — ATLAS-CH-REGRETROUTE-001

## Identity

**Title:** Routing as Online Decision Making  
**Part:** Sparse and Conditional Computation  
**Status target:** draft-v0.1  
**Implementation issue:** #259  
**Protected baseline:** 506d2642398330a27bc9b6e6c17ec38969b6f6a0

## Hard prerequisite

### ATLAS-CH-ROUTERDYN-001 / AUDIT-050

May inherit:

- router probabilities and logits as temporal observables;
- preferred-route assignments;
- accepted dispatch after capacity handling;
- realized load;
- route churn;
- probability drift;
- empirical expert-transition operators;
- taxonomy-relative specialization;
- local augmented-state diagnostics.

May not inherit regret, comparator classes, reward/loss timing, feedback semantics, optionality, correction capacity, or nonstationarity theory.

Exact prerequisite/source identities are frozen in:

sources/source-locks/ATLAS-CH-REGRETROUTE-001.yaml

## New primary sources

- Auer, Cesa-Bianchi, Freund, and Schapire (2002): adversarial/nonstochastic bandit action-selection, feedback, and regret framing.
- Herbster and Warmuth (1998): comparison against expert sequences that may switch over time.

The exact finite routing witnesses are Atlas-owned.

## Chapter contract

Treat routing as an online decision problem only after declaring:

1. proposal/preference object;
2. feasible accepted-action set;
3. accepted/executed routing action;
4. capacity/overflow map;
5. loss or reward timing;
6. feedback revealed after the action;
7. comparator class;
8. regret notion;
9. optionality;
10. correction capacity;
11. nonstationarity assumptions.

The chapter must keep distinct:

- probability drift;
- preferred-route churn;
- accepted-dispatch churn;
- load balance;
- specialization;
- regret;
- downstream task loss.

## Preferred route versus accepted dispatch

At round \(t\), let:

\[
p_t
\]

be the router's preferred proposal.

Let:

\[
F_t
\]

be the feasible accepted-dispatch action set after declared availability/capacity constraints.

Let:

\[
a_t\in F_t
\]

be the executed/accepted dispatch.

A declared capacity/overflow map may be written:

\[
a_t=G_t(p_t,\kappa_t),
\]

where \(\kappa_t\) denotes the relevant capacity state.

If capacity never binds, \(a_t=p_t\) may hold.

If capacity binds, preference and execution can differ.

The base regret object in this chapter is accepted dispatch \(a_t\), because that is the executed routing decision that incurs the declared loss.

A counterfactual preferred-route regret may be studied only if labeled separately.

## Loss timing

After accepted action \(a_t\), incur loss:

\[
\ell_t(a_t).
\]

This ordering matters:

1. observe pre-action information/context;
2. propose/choose routing action;
3. enforce feasibility/capacity;
4. execute accepted dispatch;
5. incur loss;
6. reveal feedback according to the declared feedback model.

A chapter must not use future loss information to define the online action unless it is explicitly an oracle/comparator construction.

## Feedback models

### Full information

After round \(t\), reveal:

\[
\{\ell_t(a):a\in F_t\}.
\]

### Bandit feedback

After round \(t\), reveal only:

\[
\ell_t(a_t).
\]

These support different algorithms and guarantees.

The exact finite witness uses full information for replayability.

## Comparator before regret

Regret is not defined until the comparator class is fixed.

For horizon \(T\), accepted-action sequence:

\[
a_{1:T}=(a_1,\ldots,a_T),
\]

and comparator class \(\Pi\), define:

\[
R_T^{\Pi}(a)
=
\sum_{t=1}^T \ell_t(a_t)
-
\min_{u\in\Pi}
\sum_{t=1}^T \ell_t(u_t).
\]

Every comparator sequence must obey the declared feasibility constraints unless a counterfactual oracle class is intentionally used.

## Static comparator

A static comparator class contains constant actions:

\[
\Pi_{\mathrm{static}}
=
\{(A,\ldots,A),(B,\ldots,B),\ldots\}.
\]

Static regret answers:

> how much worse was the online router than the best single fixed route in hindsight?

## Shifting comparator

For switch budget \(S\), define:

\[
\Pi_S(F_{1:T})
=
\left\{
 u_{1:T}:
 u_t\in F_t\quad(\forall t),\qquad
 \sum_{t=2}^T
 \mathbf 1[u_t\neq u_{t-1}]
 \le S
\right\}.
\]

This comparator can track a changing best route up to the declared switch budget and must also obey the same accepted-dispatch feasibility constraints. The class must be nonempty for the displayed minimum to be meaningful. If no fixed route is feasible across all rounds, a feasible static comparator cannot be introduced without modifying the benchmark; an infeasible oracle must be labeled counterfactual.

Herbster and Warmuth motivate this kind of shifting-expert comparison.

## Dynamic/shifting terminology

This chapter uses **shifting-comparator regret** for the exact witness.

It does not silently identify:

- static regret;
- shifting regret;
- path-length dynamic regret;
- variation-budget regret;
- policy regret.

Each requires its own comparator/environment semantics.

## Exact common-frame witness

Use two accepted routing actions:

\[
\mathcal A=\{A,B\}.
\]

Horizon:

\[
T=4.
\]

Feasible sets:

\[
F_t=\{A,B\}
\qquad
\text{for all }t.
\]

Full-information loss vectors are:

\[
\ell_1=(0,1),
\]

\[
\ell_2=(1,0),
\]

\[
\ell_3=(0,1),
\]

\[
\ell_4=(1,0),
\]

where coordinates correspond to \((A,B)\).

Use comparator class:

\[
\Pi_3,
\]

the action sequences with at most three switches.

For four rounds, this permits the fully alternating sequence.

## Optimal shifting comparator

The zero-loss comparator is:

\[
u^\star=(A,B,A,B).
\]

Its cumulative loss is:

\[
L(u^\star)=0.
\]

Hence the minimum comparator loss in \(\Pi_3\) is zero.

## Zero-churn policy

Use:

\[
a^{\mathrm{stay}}=(A,A,A,A).
\]

Accepted-dispatch churn count:

\[
C(a)
=
\sum_{t=2}^4
\mathbf 1[a_t\neq a_{t-1}].
\]

Therefore:

\[
\boxed{C(a^{\mathrm{stay}})=0}.
\]

Cumulative loss:

\[
0+1+0+1=2.
\]

Shifting regret:

\[
\boxed{R_4^{\Pi_3}(a^{\mathrm{stay}})=2}.
\]

Thus zero churn can coexist with positive regret.

## High-churn policy

Use:

\[
a^{\mathrm{track}}=(A,B,A,B).
\]

Churn count:

\[
\boxed{C(a^{\mathrm{track}})=3}.
\]

Cumulative loss:

\[
0+0+0+0=0.
\]

Therefore:

\[
\boxed{R_4^{\Pi_3}(a^{\mathrm{track}})=0}.
\]

Thus maximal round-to-round churn in this four-round witness can coexist with zero shifting regret.

## Exact separation

The two policies use:

- the same horizon;
- the same accepted action set;
- the same feasible sets;
- the same loss sequence;
- the same feedback model;
- the same comparator class.

Yet:

\[
C(a^{\mathrm{stay}})=0
<
3=C(a^{\mathrm{track}}),
\]

while:

\[
R(a^{\mathrm{stay}})=2
>
0=R(a^{\mathrm{track}}).
\]

Therefore:

\[
\boxed{
\text{route churn is not a regret surrogate}.
}
\]

## Why comparator choice matters

Under the same losses, the two fixed actions each have cumulative loss two.

So against the best static comparator:

- stay-on-\(A\) has static regret zero;
- the alternating tracker has cumulative loss zero and therefore beats every static action.

The shifting-comparator result answers a different question.

This is why regret values are uninterpretable without the comparator class.

## Optionality

Define operational optionality:

\[
O_t=|F_t|-1,
\]

the number of feasible accepted alternatives other than the executed action.

In the exact witness:

\[
F_t=\{A,B\},
\]

so:

\[
\boxed{O_t=1}
\]

for every round.

Optionality means an alternative is feasible.

It does not mean the alternative is better.

## Correction capacity

One operational correction-capacity object is remaining switch budget.

Let total allowed switch budget be:

\[
S.
\]

Before round \(t\), define switches already used:

\[
N_t
=
\sum_{s=2}^{t-1}
\mathbf 1[a_s\neq a_{s-1}].
\]

Define remaining switch correction capacity:

\[
\boxed{
K_t=\max(0,S-N_t).
}
\]

In the exact witness:

\[
S=3.
\]

This is only one notion of correction capacity.

Real routers can also be constrained by:

- expert capacity;
- overflow policy;
- availability;
- communication budget;
- latency;
- delayed feedback;
- switching cost.

## Optionality versus correction capacity

A router may have high optionality but low correction capacity.

For example:

- many alternative experts may be feasible;
- switching budget may already be exhausted.

Conversely, switch budget may remain while capacity makes no alternative feasible.

Therefore:

\[
\boxed{
\text{optionality}
\neq
\text{correction capacity}.
}
\]

## Capacity fairness for comparators

If capacity makes route \(B\) unavailable at round \(t\), an ordinary feasible comparator should not be allowed to use \(B\) at that round.

Otherwise online regret mixes routing quality with impossible counterfactual capacity.

A deliberately unconstrained oracle comparator may be useful, but it must be labeled as such.

## Preferred-route regret versus accepted-dispatch regret

Suppose:

\[
p_t=B
\]

but capacity forces:

\[
a_t=A.
\]

Accepted-dispatch regret attributes the incurred decision loss to executed routing.

Preferred-route counterfactual regret asks what would have happened if the proposal could have executed.

These answer different questions.

The chapter's default regret is accepted-dispatch regret.

## Capacity can create churn

Accepted dispatch can change even when preferred route is stable if capacity state changes.

Conversely, preferred route can change while accepted dispatch remains stable because capacity clips both proposals to the same route.

Therefore ROUTERDYN's observables remain necessary.

## Load balance is not regret

Suppose capacity enforces equal expert load.

That can make realized utilization look healthy.

It does not establish that accepted actions minimize the declared loss relative to the comparator.

Thus:

\[
\boxed{
\text{balanced load}
\not\Rightarrow
\text{low regret}.
}
\]

## Specialization is not regret

A taxonomy-relative specialization score asks what kinds of tokens visit an expert.

Regret asks how cumulative loss compares to a declared policy class.

An expert can be strongly specialized and still be a bad action for the current token.

A weakly specialized expert can be regret-optimal under another loss.

## Probability drift is not regret

Router probabilities can change substantially without changing accepted actions.

If accepted actions and losses are unchanged, accepted-dispatch regret can remain unchanged despite probability drift.

Conversely, tiny probability changes near a decision boundary can change accepted route and regret.

## Churn cost can be included explicitly

If switching itself has a cost \(\lambda\), define augmented loss:

\[
\widetilde \ell_t(a_t,a_{t-1})
=
\ell_t(a_t)
+
\lambda\mathbf 1[a_t\neq a_{t-1}].
\]

Then churn affects regret through the declared objective.

Without such a term, churn and regret remain separate.

The exact witness uses zero explicit switching cost.

## Nonstationarity declaration

The exact witness is adversarial/deterministic and nonstationary in the sense that the loss-minimizing action alternates by round.

No stochastic stationarity is assumed.

For larger empirical claims, one must declare whether nonstationarity is represented by:

- comparator switching;
- loss variation budget;
- context distribution drift;
- expert availability drift;
- capacity drift;
- model/optimizer drift.

These are not interchangeable.

## Feedback latency

If loss feedback arrives after delay \(d_t\), the router's correction capacity is operationally weaker because recent errors may not yet be observable.

The exact witness uses immediate post-round full-information feedback.

Delayed-feedback regret requires separate analysis.

## Bandit feedback boundary

Auer et al. establish adversarial bandit methods under partial feedback.

REGRETROUTE uses that source to type the bandit-feedback setting.

The exact witness does not claim an algorithm can know the zero-loss route before acting under bandit feedback.

It only computes realized regret after the loss sequence is specified.

## Online algorithm versus hindsight comparator

The comparator can use the full realized loss sequence in hindsight.

The online policy cannot.

This asymmetry is the point of regret.

A comparator is not evidence that an implementable online router could have selected the same actions prospectively.

## Required non-implications

The manuscript must explicitly reject:

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
\text{probability stability}
\not\Rightarrow
\text{low regret},
\]

\[
\text{high optionality}
\not\Rightarrow
\text{low regret},
\]

\[
\text{low accepted-dispatch regret}
\not\Rightarrow
\text{low downstream task loss without an interface theorem},
\]

and:

\[
\text{observed regret}
\not\Rightarrow
\text{identified causal training mechanism}.
\]

## Reader outcomes

A reader should be able to:

1. distinguish preferred route from accepted dispatch;
2. define feasible-action sets after capacity;
3. state loss and feedback timing;
4. define a comparator class before computing regret;
5. distinguish static and shifting regret;
6. reproduce the four-round zero-churn/positive-regret witness;
7. reproduce the high-churn/zero-regret witness under the same common frame;
8. define optionality and remaining switch correction capacity;
9. explain why comparator feasibility must match capacity semantics;
10. keep load, churn, probability drift, specialization, regret, and downstream loss separate.

## Required artifacts

- source lock;
- bibliography entries;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## References used in this chapter

- [@AuerEtAl2002Nonstochastic]
- [@HerbsterWarmuth1998Tracking]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-REGRETROUTE-001.yaml
