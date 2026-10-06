# ATLAS-CH-LATENTTIME-001 — Derivation Packet

## Scope

This packet proves the finite dynamic-time-warping witness used by LATENTTIME-001.

It does not establish a uniquely true physical clock, causal direction, or continuous-time dynamics.

## D1. Admissible paths

Let

\[
X=(x_1,\dots,x_n),
\qquad
Y=(y_1,\dots,y_m).
\]

An admissible path is

\[
P=((i_1,j_1),\dots,(i_L,j_L))
\]

with:

\[
(i_1,j_1)=(1,1),
\qquad
(i_L,j_L)=(n,m),
\]

and local increments in:

\[
\{(1,0),(0,1),(1,1)\}.
\]

Thus indices never decrease.

## D2. Local and total cost

Use:

\[
c(i,j)=(x_i-y_j)^2.
\]

Then:

\[
C(P)=\sum_{(i,j)\in P}c(i,j).
\]

Define:

\[
\operatorname{DTW}(X,Y)
=
\min_{P}C(P).
\]

## D3. Dynamic-programming recurrence

Let \(D(i,j)\) be minimum accumulated cost of an admissible path from \((1,1)\) to \((i,j)\).

Then:

\[
D(1,1)=c(1,1),
\]

and for interior cells:

\[
\boxed{
D(i,j)
=
c(i,j)
+
\min
\{
D(i-1,j),
D(i,j-1),
D(i-1,j-1)
\}.
}
\]

Unavailable predecessors are treated as infeasible.

This recurrence is exact for the declared step set.

## D4. Path-count recurrence

Let \(N(i,j)\) be the number of admissible paths from \((1,1)\) to \((i,j)\).

Then:

\[
N(1,1)=1
\]

and:

\[
\boxed{
N(i,j)
=
N(i-1,j)
+
N(i,j-1)
+
N(i-1,j-1)
}
\]

with out-of-range terms equal to zero.

## D5. Warped witness path count

For \(n=3,m=4\), the path-count table is:

\[
\begin{array}{c|cccc}
 & j=1&j=2&j=3&j=4\\
\hline
i=1&1&1&1&1\\
i=2&1&3&5&7\\
i=3&1&5&13&25
\end{array}
\]

Therefore:

\[
\boxed{
|\mathcal P_{3,4}|=25.
}
\]

## D6. Warped witness

Use:

\[
X=(0,1,2),
\qquad
Y=(0,0,1,2).
\]

The local-cost matrix is:

\[
C=
\begin{pmatrix}
0&0&1&4\\
1&1&0&1\\
4&4&1&0
\end{pmatrix}.
\]

All entries are nonnegative.

Therefore any zero-cost path can visit only zero-cost cells.

## D7. Zero-cost cells

The zero-cost cells are exactly:

\[
(1,1),
\quad
(1,2),
\quad
(2,3),
\quad
(3,4).
\]

No other cell has zero cost.

Any zero-cost path must:

- start at \((1,1)\);
- end at \((3,4)\);
- use only these four cells;
- respect the declared local steps.

The only admissible chain through them is:

\[
\boxed{
P^\star
=
((1,1),(1,2),(2,3),(3,4)).
}
\]

Hence:

\[
C(P^\star)=0.
\]

Since every other path visits at least one positive-cost cell:

\[
C(P)>0
\]

for every:

\[
P\neq P^\star.
\]

Therefore:

\[
\boxed{
\operatorname{DTW}(X,Y)=0
}
\]

and the optimum is unique.

## D8. Dynamic-programming table

The exact accumulated-cost table is:

\[
D=
\begin{pmatrix}
0&0&1&5\\
1&1&0&1\\
5&5&1&0
\end{pmatrix}.
\]

Thus the terminal optimum is:

\[
D(3,4)=0.
\]

Backtracking through zero-cost predecessors returns \(P^\star\).

## D9. Alignment-coordinate interpretation

The path positions:

\[
\ell=1,2,3,4
\]

carry pairs:

\[
(1,1),
(1,2),
(2,3),
(3,4).
\]

The first sequence index stays fixed while the second advances from \(1\) to \(2\).

Therefore:

\[
j=2
\]

in the observed \(Y\) stream aligns to:

\[
i=1
\]

in \(X\), not to \(i=2\).

Hence:

\[
\boxed{
\text{observed index}
\neq
\text{inferred alignment coordinate}.
}
\]

The path supplies an ordered common phase coordinate, not a physical clock theorem.

## D10. Identity-control path count

Use:

\[
X_0=(0,1,2),
\qquad
Y_0=(0,1,2).
\]

For \(n=m=3\), the path-count table is:

\[
\begin{array}{c|ccc}
 & j=1&j=2&j=3\\
\hline
i=1&1&1&1\\
i=2&1&3&5\\
i=3&1&5&13
\end{array}
\]

Therefore:

\[
\boxed{
|\mathcal P_{3,3}|=13.
}
\]

## D11. Identity-control cost matrix

The local-cost matrix is:

\[
C_0=
\begin{pmatrix}
0&1&4\\
1&0&1\\
4&1&0
\end{pmatrix}.
\]

The only zero-cost cells are:

\[
(1,1),(2,2),(3,3).
\]

The unique admissible zero-cost path is:

\[
\boxed{
P_0^\star
=
((1,1),(2,2),(3,3)).
}
\]

Thus:

\[
\boxed{
\operatorname{DTW}(X_0,Y_0)=0
}
\]

with no warp.

## D12. Identity control matters

The warped witness shows that the optimal alignment can depart from equal observed indices.

The identity control shows that the formalism does not force departure when the observations already align diagonally.

Together:

\[
\boxed{
\text{warping is data/cost/constraint dependent, not automatic}.
}
\]

## D13. Multimodal extension

For heterogeneous modalities define representations:

\[
\phi_X:\mathcal X\to\mathcal Z,
\qquad
\phi_Y:\mathcal Y\to\mathcal Z
\]

and local discrepancy:

\[
c(i,j)
=
d_{\mathcal Z}
(
\phi_X(x_i),
\phi_Y(y_j)
).
\]

The exact DP recurrence is unchanged once the local cost matrix is declared.

What changes is the semantics and provenance of the cost.

A good alignment under one representation need not remain optimal under another.

## D14. Alignment is model-relative

The optimum depends on:

\[
(X,Y,c,\mathcal P).
\]

Changing the local metric or admissible paths can change:

- optimal cost;
- optimal path;
- uniqueness.

Therefore:

\[
\boxed{
\text{unique optimal path}
\not\Rightarrow
\text{unique true latent time}.
}
\]

## D15. Positional frequency is not latent time

A relative-position operator can have Fourier modes or periodic structure.

Those modes describe an operator over sequence indices or feature rotations.

They do not by themselves determine the path:

\[
P^\star
\]

between asynchronous observations.

Hence:

\[
\boxed{
\text{periodic positional structure}
\not\Rightarrow
\text{latent temporal alignment}.
}
\]

## D16. Discrete path is not continuous flow

A DTW path is a finite sequence of grid cells.

A continuous-time flow is generated by a law of motion and carries states continuously under its own hypotheses.

Therefore:

\[
\boxed{
P^\star
\not\equiv
\Phi_t.
}
\]

A continuous-time interpretation would require an explicit interpolation/dynamical model and new assumptions.

## D17. Alignment is not causality

Even if two modalities admit a unique low-cost path, the result identifies correspondence under the declared cost.

It does not identify:

- causal direction;
- mechanism;
- common cause;
- intervention effect.

Thus:

\[
\boxed{
\text{temporal alignment}
\not\Rightarrow
\text{causal direction}.
}
\]

## D18. Alignment cost is not semantic identity

A low cost can arise because chosen features align numerically.

That does not establish semantic equivalence.

Conversely, semantically corresponding signals can require a modality-specific representation before low-cost alignment is possible.

## Durable propositions

1. The declared \(3\times4\) witness has exactly 25 admissible paths.
2. Its unique zero-cost path is \((1,1),(1,2),(2,3),(3,4)\).
3. The path explicitly separates observed index from inferred alignment coordinate.
4. The \(3\times3\) identity control has exactly 13 admissible paths.
5. Its unique zero-cost optimum is the diagonal.
6. DTW optimality is relative to observations, cost, and path constraints.
7. Multimodal alignment requires an explicit comparison representation or metric.
8. Positional periodicity does not identify latent time.
9. A discrete warping path is not automatically a continuous-time flow.
10. Alignment does not establish causality or semantic identity.

## Claim boundary

This packet proves the finite path counts, costs, and unique optima for the declared witness and control. It does not prove that the induced alignment coordinate is a uniquely true clock, that the duplicated phase has one particular physical cause, or that discrete alignment recovers an underlying continuous dynamical trajectory.
