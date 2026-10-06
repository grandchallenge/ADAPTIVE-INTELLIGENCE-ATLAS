# Chapter Specification — ATLAS-CH-LATENTTIME-001

## Identity

**Title:** Latent Clocks  
**Part:** Attention, Sequence, and Position  
**Status target:** draft-v0.1  
**Implementation issue:** #247  
**Protected baseline:** c550463eb448e41c2493747a6ed6ad83e34b24dc

## Hard prerequisites

### ATLAS-CH-RPO-001 / AUDIT-051

May inherit:

- relative-position operators on declared spaces;
- sequence-index Fourier/DC decomposition;
- low-mode truncation language;
- head-specific positional-mode profiles;
- the explicit distinction between observed position and latent time.

May not inherit a claim that relative-position structure already identifies a temporal clock.

### ATLAS-CH-DYN-001 / AUDIT-008 + AUDIT-008A

May inherit:

- state/trajectory/flow distinctions;
- local linearization boundaries;
- continuous-versus-discrete dynamics discipline.

May not call a discrete alignment path an exact continuous-time flow without an explicit bridge.

Exact source identities are frozen in:

sources/source-locks/ATLAS-CH-LATENTTIME-001.yaml

## New primary sources

- Sakoe and Chiba (1978): dynamic-programming time normalization / DTW and warping constraints.
- Zhou and De la Torre (2012): generalized time warping for multimodal temporal alignment.

## Core distinction

Observed sequence index and inferred latent alignment coordinate are different objects.

For two observed sequences

\[
X=(x_1,\dots,x_n),
\qquad
Y=(y_1,\dots,y_m),
\]

the indices \(i\) and \(j\) are positions in their respective observed streams.

A warping path establishes an alignment relation between those positions.

That relation is not automatically physical time.

## Admissible warping path

A path is an ordered sequence

\[
P=((i_1,j_1),\dots,(i_L,j_L))
\]

subject to:

### Boundary

\[
(i_1,j_1)=(1,1),
\qquad
(i_L,j_L)=(n,m).
\]

### Monotonicity

Indices never decrease.

### Local steps

Use the standard finite witness step set:

\[
(1,0),\quad(0,1),\quad(1,1).
\]

This permits one observation in one stream to align with multiple consecutive observations in the other.

## Local cost and total cost

For the exact witness use squared scalar discrepancy:

\[
c(i,j)=(x_i-y_j)^2.
\]

Path cost:

\[
C(P)=\sum_{(i,j)\in P} c(i,j).
\]

Define:

\[
\boxed{
\mathrm{DTW}(X,Y)=\min_{P\in\mathcal P_{n,m}} C(P).
}
\]

The cost is exact only relative to:

- the observations;
- the chosen local discrepancy;
- the admissible step/path set.

## Dynamic-programming recurrence

For the declared step set, define accumulated cost:

\[
D(i,j)
=
c(i,j)
+
\min
\{
D(i-1,j),
D(i,j-1),
D(i-1,j-1)
\}
\]

with appropriate boundary initialization.

The terminal value:

\[
D(n,m)
\]

is the exact optimal path cost for this finite problem.

## Exact warped witness

Use:

\[
X=(0,1,2),
\]

\[
Y=(0,0,1,2).
\]

Observed indices differ in length:

\[
n=3,\qquad m=4.
\]

The unique zero-cost path is:

\[
\boxed{
P^\star
=
((1,1),(1,2),(2,3),(3,4)).
}
\]

Its cost is:

\[
0+0+0+0=0.
\]

This path aligns:

- \(x_1=0\) with \(y_1=0\);
- \(x_1=0\) again with \(y_2=0\);
- \(x_2=1\) with \(y_3=1\);
- \(x_3=2\) with \(y_4=2\).

Thus the second observed index of \(Y\) does not correspond to the second observed index of \(X\).

## Exhaustive witness fact

Under the declared endpoints and local steps there are exactly:

\[
25
\]

admissible paths for the warped witness.

Only \(P^\star\) has total cost zero.

Therefore the optimum is unique.

## Latent alignment coordinate

The path induces an ordered common alignment coordinate:

\[
\ell=1,\dots,L.
\]

At each alignment position \(\ell\), the path records:

\[
(i_\ell,j_\ell).
\]

This coordinate can be interpreted as an inferred shared phase index for the declared alignment problem.

The chapter must not silently rename \(\ell\) as physical time.

## Identity / no-warp control

Use:

\[
X_0=(0,1,2),
\qquad
Y_0=(0,1,2).
\]

There are:

\[
13
\]

admissible monotone paths under the same local-step rule.

The unique zero-cost optimum is:

\[
\boxed{
P_0^\star=((1,1),(2,2),(3,3)).
}
\]

Thus when observed indices already agree with the phase sequence, the exact optimum is the no-warp diagonal.

## Why this is a latent-clock witness

The warped case demonstrates:

\[
\text{observed index}
\neq
\text{optimal alignment coordinate}.
\]

The identity control demonstrates that the machinery does not force a warp when none is needed.

Together they establish only the mechanics of inferring an ordered alignment coordinate.

## Asynchronous sampling interpretation

The duplicated zero in \(Y\) can represent:

- a slower local progression;
- repeated sampling of one phase;
- a plateau;
- asynchronous observation cadence.

The exact witness does not distinguish among those physical explanations.

Therefore alignment alone cannot identify the mechanism producing the asynchronous record.

## Multimodal extension

For heterogeneous modalities, raw values may not share a meaningful discrepancy.

Introduce declared representation maps:

\[
\phi_X:\mathcal X\to\mathcal Z,
\qquad
\phi_Y:\mathcal Y\to\mathcal Z,
\]

and a common-space discrepancy:

\[
c(i,j)
=
d_{\mathcal Z}
\left(
\phi_X(x_i),
\phi_Y(y_j)
\right).
\]

Generalized time-warping methods motivate this broader alignment setting.

The Atlas does not claim one representation map or metric is universally correct.

## Alignment score versus clock truth

A unique optimal path under a declared cost proves:

\[
\text{unique optimizer of that alignment problem}.
\]

It does not prove:

\[
\text{unique true latent time}.
\]

Different:

- observation features;
- representation maps;
- costs;
- path constraints;
- boundary assumptions

can induce different alignments.

## Positional periodicity versus latent time

RPO can reveal:

- periodic relative-position structure;
- Fourier modes;
- DC components;
- head-specific frequency profiles.

Those are properties of positional operators.

A periodic positional mode does not by itself establish:

- elapsed time;
- event phase;
- asynchronous correspondence;
- a physical clock.

LATENTTIME must keep those objects separate.

## Discrete warping versus continuous dynamics

The DTW path is a discrete combinatorial object.

Dynamics uses trajectories and flows with explicit laws of motion.

Therefore:

\[
\boxed{
\text{warping path}
\not\Rightarrow
\text{continuous-time trajectory}.
}
\]

A continuous-time interpretation requires an explicit interpolation/model and its own assumptions.

## Non-uniqueness boundary

Some alignment problems can have multiple optimal paths.

When the optimum is non-unique, the chapter must report:

- the set or count of optima when tractable;
- tie-breaking rules if one representative is selected;
- uncertainty about the induced alignment.

The exact witness avoids this ambiguity only because its zero-cost optimum is unique.

## Local path constraints are modeling assumptions

Changing the step set or slope/window constraint can change:

- feasible alignments;
- optimal cost;
- path uniqueness.

Therefore constraints are part of the model, not implementation trivia.

## Alignment and causality

Suppose two modalities align tightly after warping.

This supports correspondence under the declared representation/cost.

It does not establish that one modality causes the other.

Thus:

\[
\boxed{
\text{temporal alignment}
\not\Rightarrow
\text{causal direction}.
}
\]

## Alignment and semantics

Two sequences can align in shape while differing semantically.

Conversely, semantically corresponding events can require a modality-specific representation before low-cost alignment is possible.

Therefore low alignment cost is not a universal semantic-equivalence test.

## Missing data and partial alignment

The core finite witness assumes complete endpoint-to-endpoint alignment.

Real asynchronous systems can require:

- subsequence alignment;
- missing-event handling;
- partial matching;
- open-begin/open-end paths.

Those are extensions and must be declared explicitly.

## Computational complexity boundary

The standard unconstrained dynamic program over an \(n\times m\) grid uses a quadratic-size table in the two sequence lengths.

Constraints or specialized methods can alter practical or asymptotic cost.

This chapter does not make a universal runtime claim beyond its finite exact witness.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{observed position}
\not\Rightarrow
\text{latent time},
\]

\[
\text{unique optimal alignment}
\not\Rightarrow
\text{unique true clock},
\]

\[
\text{periodic positional mode}
\not\Rightarrow
\text{temporal clock},
\]

\[
\text{alignment}
\not\Rightarrow
\text{causality},
\]

\[
\text{discrete warping path}
\not\Rightarrow
\text{continuous-time flow},
\]

and:

\[
\text{low alignment cost}
\not\Rightarrow
\text{semantic identity}.
\]

## Reader outcomes

A reader should be able to:

1. distinguish observed index from inferred alignment coordinate;
2. define the admissible DTW path class;
3. derive the dynamic-programming recurrence;
4. reproduce all 25 warped-witness paths by exhaustive enumeration;
5. identify the unique zero-cost warped path;
6. reproduce the 13-path identity control and unique diagonal optimum;
7. explain why the path defines an alignment coordinate but not a physical clock;
8. state why multimodal alignment requires a declared common comparison structure;
9. distinguish positional Fourier structure from latent time;
10. distinguish discrete warping from continuous dynamics.

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

## Downstream handoff

Later sequence, multimodal, agent-memory, and temporal-reasoning chapters may inherit:

- observed-index versus latent-alignment distinction;
- admissible monotone path formalism;
- exact DTW recurrence;
- multimodal common-space alignment interface;
- identity/no-warp control discipline;
- clock-truth and causality firewalls.

They may not inherit a claim that a warping optimum is a uniquely true physical time coordinate.

## References used in this chapter

- [@SakoeChiba1978DTW]
- [@ZhouDeLaTorre2012GTW]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-LATENTTIME-001.yaml
