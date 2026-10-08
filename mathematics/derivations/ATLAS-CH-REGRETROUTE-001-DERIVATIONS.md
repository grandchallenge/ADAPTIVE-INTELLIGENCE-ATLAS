# ATLAS-CH-REGRETROUTE-001 — Derivation Packet

## Scope

This packet proves the exact four-round separation between accepted-route churn and shifting-comparator regret used by REGRETROUTE-001.

It does not prove a general online-learning regret bound for sparse routers.

## D1. Accepted action space

Use two accepted routing actions:

\[
\mathcal A=\{A,B\}.
\]

For every round:

\[
F_t=\{A,B\}.
\]

Thus both actions are feasible after capacity enforcement in the exact witness.

## D2. Horizon and losses

Let:

\[
T=4.
\]

The full-information loss table is:

\[
\begin{array}{c|cc}
 t & \ell_t(A)&\ell_t(B)\\
\hline
1&0&1\\
2&1&0\\
3&0&1\\
4&1&0
\end{array}
\]

The loss-minimizing action alternates by round.

## D3. Churn count

For action sequence \(a_{1:4}\), define accepted-dispatch churn:

\[
C(a)
=
\sum_{t=2}^{4}
\mathbf 1[a_t\neq a_{t-1}].
\]

This is a temporal routing statistic.

It is not regret.

## D4. Shifting comparator class

Use switch budget:

\[
S=3.
\]

Define:

\[
\Pi_3
=
\left\{
 u_{1:4}\in\{A,B\}^4:
 C(u)\le3
\right\}.
\]

Because a length-four binary sequence can switch at most three times **and both accepted routes are feasible on all four rounds**, \(\Pi_3\) contains every binary action sequence of length four. This equivalence is specific to the witness. In the general capacity-constrained problem, the shifting comparator class must also impose \(u_t\in F_t\) for every \(t\), and be nonempty; otherwise the regret minimum is undefined or may benchmark an infeasible oracle. A feasible static benchmark analogously requires an action in \(\bigcap_t F_t\).

## D5. Shifting regret

Define:

\[
R_4^{(3)}(a)
=
\sum_{t=1}^{4}\ell_t(a_t)
-
\min_{u\in\Pi_3}
\sum_{t=1}^{4}\ell_t(u_t).
\]

The comparator is hindsight-defined.

The online policy is not assumed to know future losses.

## D6. Comparator optimum

Consider:

\[
u^\star=(A,B,A,B).
\]

Its cumulative loss is:

\[
0+0+0+0=0.
\]

All losses are nonnegative.

Therefore no comparator can have loss below zero.

Hence:

\[
\boxed{
\min_{u\in\Pi_3}
\sum_t\ell_t(u_t)=0.
}
\]

Moreover \(u^\star\) is the unique zero-loss sequence because each round has exactly one zero-loss action.

## D7. Zero-churn route

Let:

\[
a^{\mathrm{stay}}=(A,A,A,A).
\]

Then:

\[
C(a^{\mathrm{stay}})=0.
\]

Its cumulative loss is:

\[
L(a^{\mathrm{stay}})
=0+1+0+1
=2.
\]

Thus:

\[
\boxed{
R_4^{(3)}(a^{\mathrm{stay}})=2.
}
\]

This gives an exact low-churn / positive-regret case.

## D8. High-churn route

Let:

\[
a^{\mathrm{track}}=(A,B,A,B).
\]

Then:

\[
C(a^{\mathrm{track}})=3.
\]

Its cumulative loss is zero.

Therefore:

\[
\boxed{
R_4^{(3)}(a^{\mathrm{track}})=0.
}
\]

This gives an exact high-churn / zero-regret case.

## D9. Common-frame separation theorem

Both routes are evaluated under identical:

- horizon;
- action set;
- feasible sets;
- loss table;
- feedback model;
- comparator class.

Yet:

\[
C(a^{\mathrm{stay}})=0<3=C(a^{\mathrm{track}}),
\]

while:

\[
R_4^{(3)}(a^{\mathrm{stay}})=2>0=R_4^{(3)}(a^{\mathrm{track}}).
\]

Therefore:

\[
\boxed{
C(a)
\text{ is not an order-preserving surrogate for }
R_4^{(3)}(a).
}
\]

In particular, neither low churn nor high churn determines regret.

## D10. Static comparator calculation

The fixed action \(A\) has cumulative loss:

\[
2.
\]

The fixed action \(B\) also has cumulative loss:

\[
2.
\]

Thus the best static comparator loss is:

\[
2.
\]

For the stay policy:

\[
R_4^{\mathrm{static}}(a^{\mathrm{stay}})=2-2=0.
\]

For the tracking policy:

\[
R_4^{\mathrm{static}}(a^{\mathrm{track}})=0-2=-2.
\]

This arithmetic is not a contradiction with D7-D8.

It shows that comparator choice changes the regret object.

## D11. Optionality

Define:

\[
O_t=|F_t|-1.
\]

Since:

\[
F_t=\{A,B\},
\]

we obtain:

\[
\boxed{O_t=1}
\]

for every round and either executed action.

Both policies have identical optionality.

Their regrets differ.

Therefore optionality alone does not determine regret.

## D12. Remaining switch correction capacity

Let allowed switch budget be:

\[
S=3.
\]

Before round \(t\), define:

\[
N_t
=
\sum_{s=2}^{t-1}
\mathbf 1[a_s\neq a_{s-1}].
\]

Define:

\[
K_t=\max(0,S-N_t).
\]

For the stay policy:

\[
(N_1,N_2,N_3,N_4)=(0,0,0,0),
\]

so:

\[
(K_1,K_2,K_3,K_4)=(3,3,3,3).
\]

For the tracking policy:

\[
(N_1,N_2,N_3,N_4)=(0,0,1,2),
\]

so:

\[
(K_1,K_2,K_3,K_4)=(3,3,2,1).
\]

The tracking policy uses more correction budget while achieving lower shifting regret in this witness.

Thus preserved correction budget is not automatically low regret either.

## D13. Capacity semantics

Let router proposal be \(p_t\).

Let capacity state be \(\kappa_t\).

Let accepted dispatch be:

\[
a_t=G_t(p_t,\kappa_t).
\]

If:

\[
a_t\neq p_t,
\]

then preferred-route churn and accepted-dispatch churn can differ.

Any regret computed on \(a_t\) is therefore an executed-action regret, not a preferred-route counterfactual regret.

## D14. Comparator feasibility

Suppose an action \(B\) is not in \(F_t\).

Then a comparator sequence using \(B\) at round \(t\) is infeasible under the same capacity semantics.

A fair feasible comparator class requires:

\[
u_t\in F_t
\]

for every round.

An unconstrained oracle can be defined, but it measures a different gap.

## D15. Full information versus bandit feedback

The exact witness reveals the entire loss vector after each action.

This makes replay deterministic.

Under bandit feedback, only \(\ell_t(a_t)\) is revealed.

The realized regret is still mathematically definable after the full loss process is fixed, but the information available to the online algorithm differs.

Therefore:

\[
\boxed{
\text{same regret definition}
\not\Rightarrow
\text{same learnability/guarantee under different feedback}.
}
\]

## D16. Adding explicit switch cost

If route switching itself is costly, define:

\[
\widetilde\ell_t
=
\ell_t(a_t)
+
\lambda\mathbf 1[a_t\neq a_{t-1}].
\]

Then churn enters the objective explicitly.

For the exact witness, if \(\lambda>0\), the tracking policy's total augmented loss becomes:

\[
3\lambda.
\]

The stay policy remains at base loss two.

Thus a sufficiently large switch penalty can reverse the ranking.

This reinforces that churn becomes decision-theoretic only through the declared objective.

## D17. Metric separation

The following are distinct:

- router-probability drift;
- preferred-route churn;
- accepted-dispatch churn;
- load balance;
- specialization score;
- regret;
- downstream task loss.

The exact witness proves only a separation between accepted-dispatch churn and shifting regret.

No formula in the witness equates regret with downstream task loss.

## Durable propositions

1. The exact loss process has unique zero-loss shifting comparator \((A,B,A,B)\).
2. The stay policy has churn zero and shifting regret two.
3. The tracking policy has churn three and shifting regret zero.
4. Churn is not a regret surrogate under the common frame.
5. Static and shifting comparator classes produce different regret values on the same routes.
6. Both routes have optionality one at every round.
7. Remaining switch budget and achieved regret are distinct objects.
8. Comparator feasibility should match accepted-dispatch feasibility unless a counterfactual oracle is explicitly declared.
9. Preferred-route and accepted-dispatch regret are different if capacity changes execution.
10. Full-information and bandit feedback provide different online information even when regret is evaluated against the same realized loss table.

## Claim boundary

This packet proves only exact finite arithmetic for the declared four-round online-routing problem. It does not establish a regret rate for a learned sparse router, optimality of a particular router algorithm, or a causal relation between router churn and downstream loss.
