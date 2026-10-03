# Normalized and Hyperspherical Representations
<!-- ATLAS-CH-NORMREP-001 -->

**Epistemic status:** Established Theory + Atlas Derivation + Source-Scoped Research Evidence  
**Specification:** manuscript/specifications/ATLAS-CH-NORMREP-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-NORMREP-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-NORMREP-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-NORMREP-001.yaml

## 1. Normalization is a modeling decision

A vector

\[
x\in\mathbb R^d
\]

contains at least two kinds of Euclidean information:

- direction;
- norm.

The normalization map

\[
N(x)
=
\frac{x}{\|x\|_2}
\]

keeps the first and removes the second.

This is often useful.

It is never neutral.

If two vectors lie on the same positive ray,

\[
x_2=cx_1,
\qquad
c>0,
\]

then

\[
N(x_2)=N(x_1).
\]

After normalization, positive radial scale has become an invariance.

The central question of this chapter is therefore not:

> Why is normalization good?

It is:

> What mathematical structure do we create when we deliberately remove radial freedom?

## 2. Direction without volume

The useful allegory is an arrow whose length has been erased.

Before normalization, the arrow has:

- a direction;
- a magnitude.

After normalization, only direction remains.

The structural correspondence is:

- direction ↔ angular information;
- arrow length ↔ radial information;
- tangent step ↔ change of direction;
- renormalization ↔ return to the sphere.

The limit is essential.

Length is not noise by definition.

A task may depend on:

- magnitude;
- confidence encoded in norm;
- energy;
- count;
- scale;
- uncertainty.

Normalization should therefore be understood as a declared invariance, not an automatic improvement.

## 3. The unit hypersphere

For unit vectors,

\[
u\in S^{d-1}
=
\{u\in\mathbb R^d:\|u\|_2=1\}.
\]

The Geometry chapter established the tangent space

\[
T_uS^{d-1}
=
\{\xi:u^\top\xi=0\}.
\]

Once representations are constrained to the sphere, legal first-order motion is tangential.

This changes the meaning of an update.

An unconstrained Euclidean step can point partly:

- along the sphere;
- away from the sphere.

Only the first component changes direction to first order.

## 4. The normalization map

For

\[
x\neq0,
\]

define

\[
u=N(x)
=
\frac{x}{\|x\|_2}.
\]

Let

\[
r=\|x\|_2.
\]

Then

\[
N(x)=r^{-1}x.
\]

Differentiating gives

\[
\boxed{
J_N(x)
=
\frac{1}{\|x\|_2}
\left(
I-uu^\top
\right).
}
\]

The matrix

\[
I-uu^\top
\]

is the Euclidean projector onto the tangent space at \(u\).

Normalization therefore has a clean local interpretation:

> project away the radial differential component, then scale the tangent component by \(1/\|x\|_2\).

## 5. Radial and tangential decomposition

Any perturbation

\[
\delta\in\mathbb R^d
\]

can be decomposed as

\[
\delta
=
(uu^\top)\delta
+
(I-uu^\top)\delta.
\]

The first term is radial.

The second is tangent.

Applying the normalization Jacobian gives

\[
J_N(x)\delta
=
\frac{1}{\|x\|_2}
(I-uu^\top)\delta.
\]

The radial term vanishes.

This is not metaphorical.

It is the differential of the normalization map.

## 6. Exact witness at \((3,4)\)

Take

\[
x=(3,4).
\]

Then

\[
\|x\|_2=5,
\]

and

\[
u=(3/5,4/5).
\]

The normalization Jacobian is

\[
J_N(x)
=
\begin{pmatrix}
16/125&-12/125\\
-12/125&9/125
\end{pmatrix}.
\]

The exact computational witness verifies

\[
J_N(x)x=0.
\]

The radial direction disappears to first order.

Now take

\[
t=(-4,3).
\]

Since

\[
x^\top t=0,
\]

this is tangent to the radius through \(x\).

The witness verifies

\[
J_N(x)t
=
(-4/5,3/5).
\]

The direction survives.

Its scale changes by \(1/5\).

![A unit-circle figure showing the normalized direction (3/5,4/5), a radial direction removed by normalization, an orthogonal tangent direction, and a second panel comparing the chord, great-circle arc, and SLERP midpoint for two unit vectors separated by pi over three.](../../figures/masters/ATLAS-FIG-NORMREP-001.png)

## 7. A singularity at zero

Normalization is undefined at

\[
x=0.
\]

This is not a minor implementation detail.

The map

\[
x\mapsto\frac{x}{\|x\|_2}
\]

has no direction to preserve at the origin.

Practical systems may:

- add an epsilon;
- avoid zero states by construction;
- use guarded normalization;
- switch to another chart or convention.

Each choice changes the exact mathematical object.

The Atlas will therefore distinguish idealized normalization from epsilon-regularized implementations where the difference matters.

## 8. Norm erasure is information erasure

Take

\[
x_1=(1,0),
\qquad
x_2=(2,0).
\]

Then

\[
N(x_1)=N(x_2)=(1,0).
\]

Suppose the target is

\[
y=\|x\|_2.
\]

Before normalization,

\[
y_1=1,
\qquad
y_2=2.
\]

After normalization, the two states are identical.

No downstream function of the normalized representation alone can recover which norm was present.

This is the smallest counterexample to the idea that norm is always redundant.

## 9. Angular similarity

For unit vectors \(u,v\),

\[
u^\top v
=
\cos\theta,
\]

where \(\theta\) is the angle between them.

Thus cosine similarity reduces to the dot product.

This is one reason normalized representations are attractive:

scale no longer contaminates angular comparison.

But the statement should be read literally.

Normalization makes the comparison scale-invariant because scale has been removed.

It does not prove that scale was irrelevant to the original task.

## 10. Chord distance and angle

For unit vectors,

\[
\begin{aligned}
\|u-v\|_2^2
&=
(u-v)^\top(u-v)\\
&=
\|u\|_2^2+\|v\|_2^2-2u^\top v\\
&=
2-2\cos\theta.
\end{aligned}
\]

Therefore

\[
\boxed{
\|u-v\|_2^2
=
2-2\cos\theta.
}
\]

Chord distance and angular distance are monotonically related for

\[
0\le\theta\le\pi.
\]

They remain different metrics.

The Geometry chapter's geodesic distance on the unit sphere is

\[
d_{\rm geo}(u,v)=\theta.
\]

The ambient chord distance is

\[
d_{\rm chord}(u,v)
=
\sqrt{2-2\cos\theta}.
\]

## 11. Sixty-degree witness

Take

\[
a=(1,0),
\]

and

\[
b=
\left(
\frac12,
\frac{\sqrt3}{2}
\right).
\]

Then

\[
a^\top b=\frac12,
\]

so

\[
\theta=\frac{\pi}{3}.
\]

The chord length is

\[
\|a-b\|_2=1.
\]

The geodesic distance is

\[
\frac{\pi}{3}.
\]

One pair of unit vectors therefore carries at least two natural distances.

Which one matters depends on the problem.

## 12. SLERP

For non-antipodal unit vectors \(a,b\), with

\[
\theta=\arccos(a^\top b),
\]

spherical linear interpolation is

\[
\operatorname{SLERP}(a,b;t)
=
\frac{\sin((1-t)\theta)}{\sin\theta}a
+
\frac{\sin(t\theta)}{\sin\theta}b.
\]

For the sixty-degree witness at

\[
t=\frac12,
\]

the exact midpoint is

\[
\left(
\frac{\sqrt3}{2},
\frac12
\right).
\]

It remains unit norm.

It also lies halfway along the great-circle arc.

Straight interpolation in ambient coordinates does not generally do that.

## 13. Retraction

The Geometry chapter introduced the normalized sphere retraction

\[
R_u(\xi)
=
\frac{u+\xi}{\|u+\xi\|_2},
\]

for tangent

\[
u^\top\xi=0.
\]

This provides a simple update pattern:

1. compute a tangent direction;
2. take an ambient step;
3. renormalize.

The result stays on the sphere.

A retraction approximates the manifold exponential map locally.

It is not generally identical to the exponential map.

## 14. Angular learning rate

Once a state lives on a sphere, raw Euclidean step norm is no longer the only natural update magnitude.

A more intrinsic quantity is angular displacement.

If unit states \(u\) and \(u'\) satisfy

\[
u^\top u'=\cos\theta,
\]

then

\[
\theta
\]

directly measures rotational change.

This makes “learning rate” interpretable in angular units when the update rule is explicitly designed that way.

The public GCL MODULUS Hyperball module implements this kind of machinery:

- optional tangent projection;
- target angular/update scaling;
- normalization-based retraction;
- norm control.

Its source explicitly describes the module as designed for “nGPT / MODULUS-style training.”

That is a real public implementation connection.

It is not evidence of a separate public GCL nGPT repository.

## 15. Hyperspherical contrastive representations

Normalized features also appear outside Transformer architectures.

Wang and Isola analyze contrastive representations in terms of:

- alignment of positive pairs;
- uniformity of normalized features on the hypersphere [@WangIsola2020Hypersphere].

This provides a peer-reviewed example in which hyperspherical geometry is not decorative.

The distribution of normalized features on the sphere becomes part of the analysis.

The result is still setting-specific.

It does not establish that every useful representation should be uniformly distributed on a hypersphere.

## 16. nGPT

The nGPT paper proposes a normalized Transformer with representation learning on the hypersphere [@LoshchilovEtAl2024nGPT].

The paper's central architectural move is to constrain major representation and parameter vectors to unit-norm geometry and interpret layerwise changes as movement on the hypersphere.

A later preprint develops a practical training recipe and reports scaling experiments on larger hybrid architectures [@LoshchilovGinsburg2026TrainingNGPT].

These are important examples because they make the geometry operational.

The Atlas keeps three levels separate:

1. sphere geometry is established mathematics;
2. nGPT is a specific research architecture and empirical programme;
3. broader claims that normalized Transformers are universally superior remain unsupported.

## 17. Geometry does not choose the task for us

Suppose two hidden states differ only in norm.

On the unit sphere they are identified.

This can be desirable when the system should care only about direction.

It can be harmful when norm encodes:

- evidence strength;
- uncertainty;
- frequency;
- value magnitude;
- resource level.

The right representation geometry therefore depends on what distinctions the downstream task should preserve.

## 18. Normalization can relocate information

Removing norm from one representation does not necessarily remove magnitude from the whole system.

A model may reintroduce scale through:

- separate scalar channels;
- learned temperatures;
- biases;
- logits;
- gating coefficients;
- residual amplitudes;
- external metadata.

This leads to a more useful question:

> Where should radial information live?

A normalized architecture may be best understood not as destroying all scale, but as assigning scale to explicit channels rather than letting it remain entangled with direction.

That is an architectural hypothesis.

It must be tested system by system.

## 19. Collapse on the sphere

Unit norm does not prevent representational collapse.

Every input can map to the same unit vector.

Then

\[
\|r(x)\|_2=1
\]

for all \(x\), yet the representation preserves no input distinctions.

Normalization controls radius.

It does not guarantee:

- diversity;
- separability;
- identifiability;
- useful semantics.

This is why hyperspherical representation objectives often care about angular distribution as well as norm.

## 20. Antipodal ambiguity

SLERP has a special case when

\[
a=-b.
\]

Then

\[
\theta=\pi,
\]

and there are infinitely many great circles connecting the antipodal points.

The interpolation path is not uniquely determined by the endpoints alone.

This is another reminder that normalization simplifies one degree of freedom without making all geometry trivial.

## 21. Five failure modes

### Radial information assumed irrelevant

Normalization removes a quantity the task needed.

### Unit norm mistaken for non-collapse

All states can collapse to one point on the sphere.

### Cosine similarity mistaken for complete similarity

Angular proximity can ignore task-relevant scale or other structure.

### Retraction mistaken for exponential map

The normalized update is a local manifold-compatible device, not exact geodesic flow in general.

### nGPT evidence overgeneralized

Paper-scoped empirical results are promoted into a universal architectural law.

## 22. Atlas connections

**Representation.**  
Normalization declares positive radial scaling an invariance.

**Geometry.**  
The sphere supplies tangent spaces, geodesics, retractions, and SLERP.

**Optimization.**  
Updates can be measured by angular displacement and projected tangentially.

**Attention.**  
Normalized queries, keys, values, or parameter vectors alter the scale/angular decomposition of attention computations.

**Position.**  
Spherical geometry provides a natural substrate for directional or harmonic positional constructions.

**Quotient thinking.**  
Removing radial scale can be understood as identifying states along positive rays, though the precise quotient and sphere cross-section should not be conflated automatically.

## 23. Closing view

Normalization changes the question a representation can answer.

Before normalization, a vector can say:

> where am I pointing, and how large am I?

After normalization, it can say only:

> where am I pointing?

That trade is sometimes exactly what we want.

It exposes clean angular geometry.

It makes tangent motion and spherical interpolation natural.

It can stabilize or clarify specific architectures.

But it is still a trade.

The correct mathematical stance is not to celebrate norm removal.

It is to account for what has been removed, what structure has been gained, and where the missing information must go if the system still needs it.

## References used in this chapter

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@WangIsola2020Hypersphere]
- [@LoshchilovEtAl2024nGPT]
- [@LoshchilovGinsburg2026TrainingNGPT]

See \`sources/source-locks/ATLAS-CH-NORMREP-001.yaml\` for exact source roles, the public GCL MODULUS implementation-context object, and claim scope.
