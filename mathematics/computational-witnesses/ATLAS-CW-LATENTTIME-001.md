# ATLAS-CW-LATENTTIME-001 — Exact Latent-Alignment Witness

**Chapter:** ATLAS-CH-LATENTTIME-001  
**Purpose:** exact replay of a finite DTW alignment where observed index differs from inferred alignment coordinate, plus an identity/no-warp control.

## W1. Admissible path class

For sequences of lengths \(n,m\), paths:

- start at \((1,1)\);
- end at \((n,m)\);
- use only increments \((1,0),(0,1),(1,1)\);
- never decrease either index.

Local cost:

\[
c(i,j)=(x_i-y_j)^2.
\]

Path cost:

\[
C(P)=\sum_{(i,j)\in P}c(i,j).
\]

## W2. Warped witness

\[
X=(0,1,2),
\qquad
Y=(0,0,1,2).
\]

Exact local-cost matrix:

\[
\begin{pmatrix}
0&0&1&4\\
1&1&0&1\\
4&4&1&0
\end{pmatrix}.
\]

There are exactly:

\[
\boxed{25}
\]

admissible paths.

The unique zero-cost path is:

\[
\boxed{
((1,1),(1,2),(2,3),(3,4)).
}
\]

Thus:

\[
\boxed{\mathrm{DTW}(X,Y)=0}.
\]

The second observed point of \(Y\) aligns to the first point of \(X\), so observed index is not identical to the inferred alignment coordinate.

## W3. Identity control

\[
X_0=Y_0=(0,1,2).
\]

There are exactly:

\[
\boxed{13}
\]

admissible paths.

The unique zero-cost path is:

\[
\boxed{
((1,1),(2,2),(3,3)).
}
\]

Thus the same path formalism returns the no-warp diagonal when observed indices already match.

## W4. Minimal exact replay code

    from functools import lru_cache

    STEPS = ((1,0),(0,1),(1,1))

    def enumerate_paths(n, m):
        @lru_cache(None)
        def rec(i, j):
            if (i, j) == (n-1, m-1):
                return (((i, j),),)
            out = []
            for di, dj in STEPS:
                ni, nj = i + di, j + dj
                if ni < n and nj < m:
                    for tail in rec(ni, nj):
                        out.append(((i, j),) + tail)
            return tuple(out)
        return rec(0, 0)

    def cost(path, X, Y):
        return sum((X[i] - Y[j]) ** 2 for i, j in path)

    X = (0,1,2)
    Y = (0,0,1,2)

    paths = enumerate_paths(len(X), len(Y))
    assert len(paths) == 25

    scored = [(cost(p, X, Y), p) for p in paths]
    best_cost = min(c for c, _ in scored)
    best = [p for c, p in scored if c == best_cost]

    assert best_cost == 0
    assert best == [((0,0),(0,1),(1,2),(2,3))]

    X0 = (0,1,2)
    Y0 = (0,1,2)

    paths0 = enumerate_paths(3, 3)
    assert len(paths0) == 13

    scored0 = [(cost(p, X0, Y0), p) for p in paths0]
    best0_cost = min(c for c, _ in scored0)
    best0 = [p for c, p in scored0 if c == best0_cost]

    assert best0_cost == 0
    assert best0 == [((0,0),(1,1),(2,2))]

    print("LATENTTIME_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only the exact finite path counts, costs, and unique optima under the declared local metric and path constraints.

It does not prove:

- that the optimal path is a uniquely true physical clock;
- that the duplicated zero in \(Y\) has one particular causal explanation;
- that low cost implies semantic identity;
- that a discrete path is an exact continuous-time trajectory;
- that a representation suitable for one modality pair is universally suitable for another.
