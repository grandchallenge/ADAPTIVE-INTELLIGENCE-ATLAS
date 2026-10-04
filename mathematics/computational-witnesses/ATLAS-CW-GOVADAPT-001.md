# Computational Witness — ATLAS-CW-GOVADAPT-001

## Purpose

Replay the finite governed-adaptation separation used by ATLAS-CH-GOVADAPT-001.

This is a finite symbolic witness, not evidence about a deployed autonomous system.

## Hidden condition

\[
\Theta=\{N,D\},
\qquad
b(N)=b(D)=1/2.
\]

Interpretation:

- \(N\): no later defect is discovered;
- \(D\): a later defect is discovered.

## Candidate revisions

Two candidates:

\[
A,\quad B.
\]

Let \(x_0\) be the common protected reference state. Candidate \(A\) leads to \(x_A\), and candidate \(B\) leads to \(x_B\).

Define

\[
\Delta U(q)=U(x_q)-U(x_0).
\]

Then

\[
\Delta U(A)=1,
\qquad
\Delta U(B)=1.
\]

Thus an immediate-utility-only comparison ties.

## Shared gate inputs

Both candidates satisfy:

| Predicate | A | B |
| --- | ---: | ---: |
| exact parent | 1 | 1 |
| required evidence | 1 | 1 |
| execution authority | 1 | 1 |
| separation predicate | 1 | 1 |
| immediate invariant | 1 | 1 |
| immediate utility threshold | 1 | 1 |

The witness differs only in future correction structure.

## Candidate A

| Hidden condition | Correction feasible at tolerance 0? |
| --- | ---: |
| \(N\) | 1 |
| \(D\) | 1 |

Therefore:

\[
CC_{h,0}(x_A;b)
=
\frac12+\frac12
=
1.
\]

## Candidate B

| Hidden condition | Correction feasible at tolerance 0? |
| --- | ---: |
| \(N\) | 1 |
| \(D\) | 0 |

Therefore:

\[
CC_{h,0}(x_B;b)
=
\frac12.
\]

## Utility-only gate

Define

\[
G_U(q)=\mathbf 1\{\Delta U(q)\ge1\}.
\]

Then:

\[
G_U(A)=1,
\qquad
G_U(B)=1.
\]

The utility-only gate admits both.

## Correction-aware gate

Let the declared floor be

\[
\kappa=1.
\]

Define

\[
G_C(q)
=
G_U(q)
\mathbf 1\{CC_{h,0}(x_q;b)\ge\kappa\}.
\]

Then:

\[
G_C(A)=1,
\qquad
G_C(B)=0.
\]

## Transition picture

Protected state:

\[
g_0.
\]

Candidate A:

\[
g_0\xrightarrow{A}g_A.
\]

If \(D\) is revealed:

\[
g_A
\xrightarrow{authorized\ recovery}
g_0.
\]

Candidate B:

\[
g_0\xrightarrow{B}g_B.
\]

If \(D\) is revealed, there is no authorized path of length at most \(h\) to the declared recovery target.

## Raw action-count control

Assume both \(g_A\) and \(g_B\) expose two command labels:

\[
\{continue,rollback\}.
\]

For \(g_A\), rollback is authorized and target-reaching.

For \(g_B\), rollback is not a feasible authorized target-reaching path.

Both raw command counts equal two.

Correction capacity still differs.

## Exact-target evidence control

Let validation object \(e_1\) target revision \(r_1\).

Repair produces \(r_2\neq r_1\).

Then:

\[
Binds(e_1,r_2)=0.
\]

Fresh validation \(e_2\) targets \(r_2\):

\[
Binds(e_2,r_2)=1.
\]

This confirms only the identity-binding rule.

## Safety-without-liveness control

Suppose every candidate fails a required gate.

The canonical state remains:

\[
g_0.
\]

The invariant can remain true forever while no promotion occurs.

## Claim boundary

This witness proves only that, in the declared finite model:

1. equal immediate utility can coexist with unequal correction capacity;
2. a utility-only threshold cannot distinguish the two candidates;
3. a declared correction-capacity floor can distinguish them;
4. raw command count does not determine governed recoverability;
5. evidence for one exact revision is stale after a material revision change;
6. fail-closed safety does not imply liveness.

It does not prove that the chosen correction-capacity floor is universally appropriate or that any real system is safe.
