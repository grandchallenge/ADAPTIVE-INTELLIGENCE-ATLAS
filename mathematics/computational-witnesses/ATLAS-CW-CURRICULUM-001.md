# Computational Witness — ATLAS-CW-CURRICULUM-001

## Purpose

Replay the finite state-dependent curriculum separation used by ATLAS-CH-CURRICULUM-001.

The witness is exact and finite.

It is not a neural-network experiment.

## State space

\[
s=(e,h)\in\{0,1,2\}^2.
\]

Actions:

\[
\mathcal A=\{E,H\}.
\]

Nominal difficulty:

\[
d(E)=1,
\qquad
d(H)=2.
\]

Aggregate toy score:

\[
M(e,h)=e+h.
\]

## Transition table

Easy action:

\[
T_E(e,h)=(\min(2,e+1),h).
\]

Hard action:

\[
T_H(e,h)=
\begin{cases}
(e,\min(2,h+1)),&e\ge1,\\
(e,h),&e=0.
\end{cases}
\]

One-step progress:

\[
R(s,a)=M(T_a(s))-M(s).
\]

## Exact checkpoint A

At

\[
s_A=(0,0):
\]

\[
T_E(s_A)=(1,0),
\qquad
R(s_A,E)=1;
\]

\[
T_H(s_A)=(0,0),
\qquad
R(s_A,H)=0.
\]

The unique one-step progress maximizer is \(E\).

## Exact checkpoint B

At

\[
s_B=(2,0):
\]

\[
T_E(s_B)=(2,0),
\qquad
R(s_B,E)=0;
\]

\[
T_H(s_B)=(2,1),
\qquad
R(s_B,H)=1.
\]

The unique one-step progress maximizer is \(H\).

## Separation

A state-independent rule choosing \(E\) first is suboptimal at \(s_B\).

A state-independent rule choosing \(H\) first is suboptimal at \(s_A\).

Therefore no single state-independent deterministic first action is one-step progress-optimal for both states.

The fixed nominal ranking

\[
d(E)<d(H)
\]

does not change between states.

## Equal two-transition budget

Start from

\[
s_B=(2,0).
\]

Fixed easy-then-hard:

\[
(2,0)
\xrightarrow{E}
(2,0)
\xrightarrow{H}
(2,1).
\]

Cumulative progress:

\[
1.
\]

State-aware immediate-progress policy:

\[
(2,0)
\xrightarrow{H}
(2,1)
\xrightarrow{H}
(2,2).
\]

Cumulative progress:

\[
2.
\]

Both policies execute exactly two learner transitions.

## Exhaustive table

For completeness:

| State \(s\) | \(R(s,E)\) | \(R(s,H)\) |
| --- | ---: | ---: |
| \((0,0)\) | 1 | 0 |
| \((0,1)\) | 1 | 0 |
| \((0,2)\) | 1 | 0 |
| \((1,0)\) | 1 | 1 |
| \((1,1)\) | 1 | 1 |
| \((1,2)\) | 1 | 0 |
| \((2,0)\) | 0 | 1 |
| \((2,1)\) | 0 | 1 |
| \((2,2)\) | 0 | 0 |

This table also shows that the state-aware policy can face ties and saturation.

A tie-breaking rule is therefore part of any fully specified deterministic policy.

## Minimal replay pseudocode

Define:

- states as integer pairs in \(\{0,1,2\}^2\);
- \(M(e,h)=e+h\);
- \(T_E\) and \(T_H\) exactly as above;
- \(R(s,a)=M(T_a(s))-M(s)\).

Enumerate all nine states and both actions.

Verify the table, the two unique-maximizer checkpoints, and the two-step trajectories.

## Claim boundary

This witness proves only a finite control separation:

> a fixed static difficulty ranking does not determine a one-step progress-optimal action uniformly across the declared learner states.

It does not prove that:

- real models have two mastery coordinates;
- harder examples become useful after an easy prerequisite;
- immediate learning progress should be maximized;
- curriculum learning improves generalization;
- state-aware controllers are cheaper or more robust.
