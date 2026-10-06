# Latent Clocks
<!-- ATLAS-CH-LATENTTIME-001 -->

**Epistemic status:** audited Relative-Position Operators and Dynamics substrates + primary time-warping sources + Atlas-owned exact finite alignment witness.  
**Specification:** manuscript/specifications/ATLAS-CH-LATENTTIME-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-LATENTTIME-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-LATENTTIME-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-LATENTTIME-001.yaml

Sequence position is observed.

Time can be inferred.

Those statements are not the same.

A token, frame, sensor sample, or event has an index in an observed stream. But two streams can progress through the same underlying phase at different rates, with pauses, duplicates, missing samples, or modality-specific distortions.

This chapter asks:

> when should observed offsets be replaced by an inferred alignment coordinate?

The governing distinction is:

\[
\boxed{
\text{observed sequence index}
\neq
\text{latent temporal alignment}.
}
\]

And the governing caution is:

\[
\boxed{
\text{optimal alignment}
\neq
\text{proof of a uniquely true physical clock}.
}
\]

## 1. The handoff from positional operators

Relative-Position Operators already separates:

- feature-space RoPE rotations;
- sequence-index relative-position kernels;
- Fourier modes over positional operators;
- DC structure;
- low-dimensional positional approximations.

Those are positional objects.

They can tell us that a model treats certain offsets as:

- similar;
- periodic;
- slowly varying;
- high-frequency.

They do not by themselves tell us that two asynchronous streams are at the same latent phase.

LATENTTIME adds that inference problem.

## 2. The handoff from Dynamics

Dynamics already separates:

- state;
- trajectory;
- vector field;
- flow;
- discrete update.

That distinction matters because time-warping produces a discrete correspondence path.

A correspondence path is not automatically a trajectory of a continuous dynamical system.

The chapter therefore keeps:

\[
\text{alignment}
\]

separate from:

\[
\text{law of motion}.
\]

## 3. Two observed streams

Let:

\[
X=(x_1,\dots,x_n),
\]

\[
Y=(y_1,\dots,y_m).
\]

The indices:

\[
i=1,\dots,n,
\qquad
j=1,\dots,m
\]

refer to positions in different observed sequences.

There is no reason in general to assume:

\[
i=j
\]

means “same latent time.”

## 4. Dynamic time warping

Dynamic time warping searches over monotone correspondences between two ordered streams.

For the finite Atlas formalism, an admissible path is:

\[
P=((i_1,j_1),\dots,(i_L,j_L))
\]

with:

\[
(i_1,j_1)=(1,1),
\]

\[
(i_L,j_L)=(n,m),
\]

and local increments:

\[
(1,0),
\quad
(0,1),
\quad
(1,1).
\]

These steps allow one observed sample in one stream to align with more than one consecutive sample in the other.

## 5. The path is monotone

Indices never move backward.

This encodes an ordering assumption:

> later aligned observations cannot be matched to earlier positions after the path has passed them.

That is already a modeling choice.

A system with genuine temporal reversals or reordering would need a different alignment object.

## 6. A local discrepancy

For scalar witness sequences use:

\[
c(i,j)
=
(x_i-y_j)^2.
\]

The cost of a path is:

\[
C(P)
=
\sum_{(i,j)\in P}
c(i,j).
\]

The optimal path solves:

\[
\boxed{
\operatorname{DTW}(X,Y)
=
\min_{P\in\mathcal P_{n,m}}
C(P).
}
\]

The optimum is relative to the declared cost and path class.

## 7. Dynamic programming

Let:

\[
D(i,j)
\]

be the minimum cost of an admissible path ending at \((i,j)\).

Then:

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
\}.
\]

This is the recursive structure behind the finite alignment problem.

The terminal value:

\[
D(n,m)
\]

is the exact optimum.

## 8. The exact warped witness

Use:

\[
X=(0,1,2),
\]

\[
Y=(0,0,1,2).
\]

The first stream has three observations.

The second has four.

The second stream repeats the initial value.

That duplicate can represent many things:

- slower local progress;
- repeated sampling;
- a plateau;
- asynchronous acquisition.

The witness does not choose among those explanations.

## 9. The local-cost matrix

The exact squared-distance matrix is:

\[
\begin{pmatrix}
0&0&1&4\\
1&1&0&1\\
4&4&1&0
\end{pmatrix}.
\]

The zero-cost cells are exactly:

\[
(1,1),
(1,2),
(2,3),
(3,4).
\]

## 10. There are 25 admissible paths

Under the declared endpoint and step constraints, exhaustive enumeration gives:

\[
\boxed{25}
\]

admissible paths from:

\[
(1,1)
\]

to:

\[
(3,4).
\]

The path-count recurrence is:

\[
N(i,j)
=
N(i-1,j)
+
N(i,j-1)
+
N(i-1,j-1).
\]

The terminal count is:

\[
N(3,4)=25.
\]

## 11. The unique zero-cost alignment

Because every local cost is nonnegative, a zero-cost path can use only zero-cost cells.

Only one admissible chain connects all required endpoints through those cells:

\[
\boxed{
P^\star
=
((1,1),(1,2),(2,3),(3,4)).
}
\]

Thus:

\[
\boxed{
\operatorname{DTW}(X,Y)=0.
}
\]

And the optimum is unique.

## 12. Observed index has separated from alignment phase

The first two observations of \(Y\):

\[
y_1=0,
\qquad
y_2=0
\]

both align to:

\[
x_1=0.
\]

Then:

\[
y_3=1
\]

aligns to:

\[
x_2=1,
\]

and:

\[
y_4=2
\]

aligns to:

\[
x_3=2.
\]

Therefore:

\[
j=2
\]

in one stream does not correspond to:

\[
i=2
\]

in the other.

This is the smallest exact latent-clock lesson.

## 13. A common alignment coordinate

Index the path itself by:

\[
\ell=1,\dots,L.
\]

Each latent alignment position carries a pair:

\[
(i_\ell,j_\ell).
\]

This gives a common ordered phase coordinate.

It is useful to call this a latent alignment coordinate.

It is not yet justified to call it physical time.

## 14. Why “clock” is a dangerous word

A clock suggests something stronger than alignment.

It can suggest:

- elapsed physical duration;
- causal progression;
- an intrinsic phase variable;
- a unique temporal parameterization.

DTW alone gives none of those automatically.

It gives an optimizer of an alignment objective.

The chapter therefore uses “latent clock” as an inference object whose epistemic status must remain explicit.

## 15. Identity/no-warp control

Now use:

\[
X_0=(0,1,2),
\qquad
Y_0=(0,1,2).
\]

The two streams have equal length and already progress in the same observed order.

There are:

\[
\boxed{13}
\]

admissible paths under the same rule.

## 16. The diagonal is uniquely optimal

The local-cost matrix is:

\[
\begin{pmatrix}
0&1&4\\
1&0&1\\
4&1&0
\end{pmatrix}.
\]

The only zero-cost cells are diagonal.

Therefore the unique zero-cost path is:

\[
\boxed{
((1,1),(2,2),(3,3)).
}
\]

So:

\[
\operatorname{DTW}(X_0,Y_0)=0
\]

without any warp.

## 17. The control prevents a false lesson

The warped witness alone could tempt us to think that latent-time machinery always invents a nontrivial warp.

The control shows otherwise.

When observed indices already match the phase structure, the exact optimum is the identity alignment.

Thus:

\[
\boxed{
\text{warping is inferred when supported by the declared data and cost, not imposed by default}.
}
\]

## 18. Constraints are part of the model

Changing the allowed local steps changes the feasible path set.

Adding a slope band or window can also change:

- the optimum;
- its cost;
- uniqueness.

Therefore path constraints are not implementation details.

They are assumptions.

Sakoe and Chiba's classical formulation makes time-normalization and slope constraints part of the alignment problem [@SakoeChiba1978DTW].

## 19. A unique optimum is still model-relative

The finite witness has a unique optimum.

But that means only:

> there is one best path under this observation space, squared cost, endpoint rule, and step set.

Change any of those, and the optimum may change.

Therefore:

\[
\boxed{
\text{unique optimum}
\not\Rightarrow
\text{unique true time}.
}
\]

## 20. Multimodal alignment changes the comparison problem

Suppose one stream is:

- video;

and another is:

- motion capture;
- audio;
- physiology;
- text events.

The raw coordinates are not generally comparable.

A reasonable framework needs representation maps:

\[
\phi_X:\mathcal X\to\mathcal Z,
\]

\[
\phi_Y:\mathcal Y\to\mathcal Z.
\]

Then local cost can be computed in the comparison space:

\[
d_{\mathcal Z}
(
\phi_X(x_i),
\phi_Y(y_j)
).
\]

## 21. Generalized time warping

Zhou and De la Torre explicitly treat multimodal temporal alignment and allow richer monotonic warping structure [@ZhouDeLaTorre2012GTW].

That is useful precedent for LATENTTIME because the inferred clock need not be tied to one raw sensor space.

But the Atlas does not inherit a universal multimodal representation.

The representation and discrepancy remain part of the declared model.

## 22. Asynchrony is not one phenomenon

Two streams can become misaligned because of:

- different sampling rates;
- missing observations;
- duplicated observations;
- variable execution speed;
- buffering;
- latency;
- sensor-specific preprocessing;
- genuinely different event timing.

A low-cost warp cannot by itself identify which explanation is correct.

## 23. Positional frequency is not a clock

RPO can expose a strong low-frequency positional mode.

That can mean the operator varies slowly with sequence offset.

It does not imply that the same mode tracks:

- elapsed time;
- behavioral phase;
- event age;
- causal stage.

Thus:

\[
\boxed{
\text{positional Fourier structure}
\not\Rightarrow
\text{latent temporal coordinate}.
}
\]

## 24. RoPE frequency is not elapsed time either

A RoPE frequency describes rotation in feature coordinates as position changes.

Its phase is an algebraic function of positional offset.

That does not automatically make it a physical or semantic clock.

The same word “phase” can describe different mathematical objects.

LATENTTIME keeps them typed.

## 25. Discrete alignment is not a continuous trajectory

The DTW path is:

\[
((i_1,j_1),\dots,(i_L,j_L)).
\]

This is a finite combinatorial object.

A continuous trajectory is something like:

\[
t\mapsto x(t)
\]

generated under an explicit dynamical model.

Those objects can be related only after adding:

- interpolation;
- parameterization;
- regularity assumptions;
- possibly a law of motion.

Therefore:

\[
\boxed{
\text{DTW path}
\not\Rightarrow
\text{continuous-time flow}.
}
\]

## 26. Continuous-time latent clocks require more structure

If a model claims a scalar latent time:

\[
\tau
\]

with continuous evolution, it should specify how:

\[
i\mapsto\tau_i
\]

or:

\[
j\mapsto\tau_j
\]

is obtained.

It should also specify whether \(\tau\) is:

- merely monotone;
- metrically meaningful;
- differentiable;
- dynamically generated.

A monotone ordering alone does not give a metric clock.

## 27. Alignment is not causality

Suppose audio and video align tightly under a learned warp.

That supports temporal correspondence under the model.

It does not prove:

- audio causes video;
- video causes audio;
- one latent system drives both.

Thus:

\[
\boxed{
\text{alignment}
\not\Rightarrow
\text{causal direction}.
}
\]

## 28. Low cost is not semantic identity

Two sequences can be numerically easy to align while representing different semantics.

Conversely, semantically corresponding events can look very different in raw modalities.

So:

\[
\boxed{
\text{low alignment cost}
\not\Rightarrow
\text{semantic identity}.
}
\]

## 29. Non-unique alignments should stay non-unique

Some data admit multiple optimal paths.

A responsible system should not silently pretend one arbitrary tie-break is the discovered clock.

It should report:

- multiplicity;
- tie-breaking;
- alignment uncertainty;
- downstream sensitivity where relevant.

The exact Atlas witness avoids this only because the optimum happens to be unique.

## 30. Partial and missing-data alignment

The core witness uses full endpoint-to-endpoint matching.

Real streams may require:

- subsequence matching;
- open-begin or open-end paths;
- partial matching;
- missing-event models.

Those are different problem definitions.

They should be declared rather than smuggled into “DTW.”

## 31. A useful latent-clock protocol

For two asynchronous streams:

1. define the observed streams;
2. define any representation maps;
3. define the local discrepancy;
4. define endpoints and path constraints;
5. compute the optimal path;
6. test an identity/no-warp control where possible;
7. inspect uniqueness or multiplicity;
8. report the induced alignment coordinate;
9. keep physical-clock claims separate;
10. test downstream usefulness independently.

## 32. When the alignment coordinate is useful

An inferred alignment coordinate can support:

- cross-modal fusion;
- event matching;
- phase-normalized comparison;
- memory alignment;
- asynchronous agent communication;
- trajectory comparison.

Its usefulness can be empirical even when it is not a uniquely true physical time variable.

## 33. Atlas non-implications

The chapter rejects:

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

## 34. Atlas connections

**Relative-Position Operators.**  
RPO supplies operator/frequency structure over observed position; LATENTTIME adds alignment inference across asynchronous indices.

**Dynamics.**  
Dynamics supplies the distinction between sampled states, trajectories, and flows; LATENTTIME keeps discrete warping separate from continuous-time laws.

**Multimodal systems.**  
A shared alignment coordinate can organize observations from heterogeneous sensors or representations.

**Agent systems.**  
Different agents can observe related events on different local clocks; alignment can provide a common phase coordinate without assuming synchronized wall time.

**Memory.**  
Episodes with different sampling density can be compared after an explicit alignment transformation.

## 35. Closing view

Position is cheap to observe.

Time is often not.

A sequence index tells us where a sample sits in a record.

It does not necessarily tell us where that sample sits in a shared process.

The exact witness shows the smallest nontrivial case:

\[
X=(0,1,2),
\qquad
Y=(0,0,1,2).
\]

The second stream lingers on one phase.

The optimal correspondence therefore repeats one alignment state:

\[
(1,1)\to(1,2)\to(2,3)\to(3,4).
\]

The identity control shows the same machinery leaves already aligned streams unwarped.

The right conclusion is:

\[
\boxed{
\text{latent time is an inferred correspondence structure whose meaning depends on the declared alignment model.}
}
\]

It can be useful without being a metaphysical clock.

## References used in this chapter

- [@SakoeChiba1978DTW]
- [@ZhouDeLaTorre2012GTW]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-LATENTTIME-001.yaml
