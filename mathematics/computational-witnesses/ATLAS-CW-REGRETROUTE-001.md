# ATLAS-CW-REGRETROUTE-001 — Exact Churn/Regret Separation Witness

**Chapter:** ATLAS-CH-REGRETROUTE-001  
**Purpose:** exact replay of a common-frame separation between accepted-route churn and shifting-comparator regret.

## W1. Common frame

Accepted actions:

\[
\mathcal A=\{A,B\}.
\]

Horizon:

\[
T=4.
\]

Feasible set each round:

\[
F_t=\{A,B\}.
\]

Loss table:

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

Feedback mode: full information after each accepted dispatch.

Comparator class:

\[
\Pi_3
=
\{u_{1:4}\in\{A,B\}^4:C(u)\le3\}.
\]

## W2. Comparator optimum

The unique zero-loss sequence is:

\[
\boxed{(A,B,A,B)}.
\]

Comparator loss:

\[
\boxed{0}.
\]

## W3. Zero-churn route

\[
a^{\mathrm{stay}}=(A,A,A,A).
\]

Switch count:

\[
\boxed{0}.
\]

Cumulative loss:

\[
\boxed{2}.
\]

Shifting regret:

\[
\boxed{2}.
\]

## W4. High-churn route

\[
a^{\mathrm{track}}=(A,B,A,B).
\]

Switch count:

\[
\boxed{3}.
\]

Cumulative loss:

\[
\boxed{0}.
\]

Shifting regret:

\[
\boxed{0}.
\]

Thus:

\[
0<3
\]

for churn, while:

\[
2>0
\]

for regret.

## W5. Static comparator control

Both fixed actions have cumulative loss two.

Therefore best static comparator loss is two.

The same routes have:

\[
R_{\mathrm{static}}(A,A,A,A)=0,
\]

and:

\[
R_{\mathrm{static}}(A,B,A,B)=-2.
\]

This control demonstrates that regret cannot be interpreted without naming the comparator class.

## W6. Optionality

Because both actions are feasible every round:

\[
O_t=|F_t|-1=1.
\]

Both routes have identical optionality despite different churn and shifting regret.

## W7. Remaining correction capacity

Use switch budget:

\[
S=3.
\]

Before round \(t\):

\[
K_t=\max\left(0,S-\sum_{s=2}^{t-1}\mathbf1[a_s\neq a_{s-1}]\right).
\]

For stay route:

\[
(K_1,K_2,K_3,K_4)=(3,3,3,3).
\]

For tracking route:

\[
(K_1,K_2,K_3,K_4)=(3,3,2,1).
\]

More preserved switch budget does not imply lower regret in this witness.

## W8. Minimal exact replay code

    from itertools import product

    actions = ("A", "B")
    losses = (
        {"A": 0, "B": 1},
        {"A": 1, "B": 0},
        {"A": 0, "B": 1},
        {"A": 1, "B": 0},
    )

    def churn(seq):
        return sum(seq[t] != seq[t-1] for t in range(1, len(seq)))

    def cumulative_loss(seq):
        return sum(losses[t][a] for t, a in enumerate(seq))

    comparator = [seq for seq in product(actions, repeat=4) if churn(seq) <= 3]
    best_loss = min(cumulative_loss(seq) for seq in comparator)
    best = [seq for seq in comparator if cumulative_loss(seq) == best_loss]

    assert best_loss == 0
    assert best == [("A", "B", "A", "B")]

    stay = ("A", "A", "A", "A")
    track = ("A", "B", "A", "B")

    assert churn(stay) == 0
    assert cumulative_loss(stay) == 2
    assert cumulative_loss(stay) - best_loss == 2

    assert churn(track) == 3
    assert cumulative_loss(track) == 0
    assert cumulative_loss(track) - best_loss == 0

    static = [("A",) * 4, ("B",) * 4]
    static_best = min(cumulative_loss(seq) for seq in static)
    assert static_best == 2
    assert cumulative_loss(stay) - static_best == 0
    assert cumulative_loss(track) - static_best == -2

    optionality = [1, 1, 1, 1]
    assert optionality == [1] * 4

    print("REGRETROUTE_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only the exact finite comparison under the declared accepted-action, loss, feasibility, feedback, and shifting-comparator semantics.

It does not establish:

- a regret bound for a learned router;
- that high churn is generally beneficial;
- that low churn is generally harmful;
- that regret equals downstream task loss;
- that a router can know the best shifting comparator online;
- that capacity-free witness behavior transfers unchanged when overflow reroutes proposals.
