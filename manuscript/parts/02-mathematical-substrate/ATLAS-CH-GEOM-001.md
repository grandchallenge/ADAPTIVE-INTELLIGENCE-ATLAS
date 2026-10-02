# Geometry of Constrained State Spaces
<!-- ATLAS-CH-GEOM-001 -->

**Epistemic status:** mathematical exposition with source-locked standard results and Atlas-owned derivations.  
**Primary figure:** `ATLAS-FIG-MANIFOLD-001`  
**Derivation packet:** `mathematics/derivations/ATLAS-CH-GEOM-001-DERIVATIONS.md`

## 1. The map and the mountain

A vector of numbers can describe a state without telling us which changes of that state are admissible.

That distinction is easy to miss because ordinary neural-network notation is usually written in an ambient Euclidean space. Hidden states are vectors in (mathbb R^d). Weight matrices are arrays in (mathbb R^{m	imes n}). Gradients are represented by vectors of partial derivatives. In that coordinate language, every sufficiently small Euclidean displacement appears legal.

But many computational objects carry constraints that make most ambient displacements wrong.

A normalized representation may be required to stay on a unit sphere. An orthogonal matrix must remain orthogonal. A matrix whose columns form an orthonormal frame must satisfy (X^	op X=I). A subspace is unchanged when we rotate the basis used to represent it. In each case the coordinates live in a larger space than the object itself.

The useful allegory is a cartographer standing before a mountain. A flat map gives coordinates for the mountain, but a straight line drawn through the paper need not correspond to a walk on the surface. The map is not false. It is simply larger than the set of physically admissible motions.

The correspondence is:

- the map coordinates are the **ambient space**;
- the mountain surface is the **admissible state space**;
- a locally flat patch is the **tangent space**;
- a shortest admissible route is a **geodesic**;
- a rule that takes a tangent step and returns us to the surface is a **retraction**.

The limit of the allegory matters. A mathematical manifold need not be a visible surface embedded in three-dimensional space. Many important manifolds are spaces of matrices or equivalence classes. A retraction is not literally a projection performed by gravity. The image teaches one structural fact only: coordinates can permit motions that the object itself does not.

That fact will recur throughout this Atlas.

## 2. Ambient space versus admissible space

Let (M) denote a smooth state space embedded in an ambient Euclidean space (mathbb R^N). A point (xin M) is represented by (N) coordinates, but those coordinates may satisfy constraints.

The first geometric object we need is the tangent space (T_xM). Informally, it contains the instantaneous velocities of curves that remain in (M).

If (gamma:(-epsilon,epsilon)	o M) is differentiable and (gamma(0)=x), then

[
dotgamma(0)in T_xM.
]

The crucial move is that (T_xM) is linear even when (M) is curved. We replace a curved state space locally by a linear space of legal first-order motions.

This gives a recurring pattern:

[
	ext{constrained object}
longrightarrow
	ext{tangent linearization}
longrightarrow
	ext{legal local update}
longrightarrow
	ext{return to the constraint}.
]

Later chapters will specialize this pattern to manifold optimization, normalized representations, positional geometry, and transport.

For now, the unit sphere gives the cleanest complete example.

## 3. The unit sphere

Define

[
S^{d-1}
=
{xinmathbb R^d:|x|_2=1}.
]

The sphere is an admissible state space cut out of (mathbb R^d) by the constraint

[
x^	op x=1.
]

Take a differentiable curve (gamma(t)in S^{d-1}) with (gamma(0)=x) and velocity (v=dotgamma(0)). Because the curve stays on the sphere,

[
gamma(t)^	opgamma(t)=1.
]

Differentiating at (t=0),

[
2x^	op v=0.
]

Therefore

[
oxed{
T_xS^{d-1}
=
{vinmathbb R^d:x^	op v=0}.
}
]

The tangent space is exactly the hyperplane orthogonal to (x).

This is already enough to expose the difference between an ambient gradient and a geometric direction. If an unconstrained update proposes a vector (ginmathbb R^d), the component parallel to (x) tries to change the radius. The tangent component is

[
g_{mathrm{tan}}
=
g-(x^	op g)x.
]

That is a legal first-order direction on the sphere.

The phrase **first-order** is important. The point (x+g_{mathrm{tan}}) does not generally lie on the sphere. Tangency constrains velocity, not finite displacement.

## 4. Retraction: step locally, return globally

A retraction is a controlled way to convert a tangent displacement into a new point on the manifold. In the optimization-oriented formulation used by Absil, Mahony, and Sepulchre, a retraction locally agrees with the manifold at the base point and has the identity as its first derivative on the tangent space [@AbsilMahonySepulchre2008].

For the unit sphere, the simplest useful retraction is normalization:

[
R_x(v)
=
rac{x+v}{|x+v|},
qquad
vin T_xS^{d-1}.
]

It obviously returns a unit vector. More importantly,

[
R_x(0)=x
]

and

[
D R_x(0)[v]=v.
]

The derivation is short enough that there is no reason to hide it.

Let

[
r(t)
=
rac{x+t v}{|x+t v|}.
]

Then

[
r'(0)
=
v-x(x^	op v).
]

For tangent (v), (x^	op v=0), so

[
r'(0)=v.
]

Thus normalization preserves the intended tangent direction to first order.

This is the first place where geometric language earns its keep. “Normalize after every step” can sound like an implementation trick. “Use a retraction on the sphere” says what structural property the operation has: it is a local approximation to legal manifold motion.

## 5. Exponential map versus retraction

A retraction should not be confused with exact geodesic motion.

On the unit sphere, for nonzero tangent (v),

[
operatorname{Exp}_x(v)
=
cos(|v|)x
+
sin(|v|)rac{v}{|v|}.
]

This point lies on the great circle determined by (x) and (v), at geodesic distance (|v|) from (x).

By contrast,

[
R_x(v)
=
rac{x+v}{sqrt{1+|v|^2}},
]

where the denominator simplifies because (x^	op v=0).

For small (|v|), both maps agree to first order. They are not globally identical.

That difference is visible in the first Wolfram plate:

![ATLAS-FIG-MANIFOLD-001](../../figures/masters/ATLAS-FIG-MANIFOLD-001.png)

The figure is generated from the exact unit-sphere formulas in `figures/wolfram/ATLAS-FIG-MANIFOLD-001.wl`. The sphere, tangent plane, tangent vector, exponential-map endpoint, normalized-retraction endpoint, and great-circle arc carry literal mathematical meaning. Perspective, opacity, plane extent, and label placement do not.

The distinction will matter later. A retraction is often cheaper than an exponential map and may be entirely adequate for an optimization method. But replacing one by the other changes the finite step.

## 6. Spherical interpolation

Suppose (x,yin S^{d-1}) are unit vectors with

[
x^	op y=cos	heta,
qquad
0<	heta<pi.
]

The shorter great-circle interpolation is

[
operatorname{SLERP}(x,y;t)
=
rac{sin((1-t)	heta)}{sin	heta}x
+
rac{sin(t	heta)}{sin	heta}y,
qquad
0le tle1.
]

The acronym comes from spherical linear interpolation, historically associated with Shoemake's quaternion interpolation work [@Shoemake1985]. The geometry itself is broader than quaternions.

The important property is not that the coefficients look elegant. It is that the interpolation remains on the sphere.

Writing

[
alpha
=
rac{sin((1-t)	heta)}{sin	heta},
qquad
eta
=
rac{sin(t	heta)}{sin	heta},
]

we have

[
|alpha x+eta y|^2
=
alpha^2+eta^2+2alphaetacos	heta
=
1.
]

The path therefore preserves unit norm exactly.

At (	heta=0), the apparent singularity is removable: the endpoints coincide. At (	heta=pi), the singularity expresses a genuine geometric ambiguity. Antipodal points have infinitely many shortest great-circle connections. The formula cannot choose a direction that the data did not specify.

This is a useful example of a broader lesson: singular formulas are not always numerical defects. Sometimes they faithfully report that the underlying object is not uniquely determined.

## 7. From spheres to orthonormal frames

The sphere constrains one vector. Many learning systems constrain several vectors or matrix columns simultaneously.

The real Stiefel manifold is

[
operatorname{St}(n,p)
=
{Xinmathbb R^{n	imes p}:X^	op X=I_p}.
]

Its points are ordered orthonormal (p)-frames in (mathbb R^n). When (p=1), the Stiefel manifold reduces to a sphere.

Let (X(t)inoperatorname{St}(n,p)) be differentiable with (X(0)=X) and (dot X(0)=Z). Differentiate the constraint:

[
X(t)^	op X(t)=I_p.
]

At (t=0),

[
Z^	op X+X^	op Z=0.
]

Thus

[
oxed{
T_Xoperatorname{St}(n,p)
=
{Z:X^	op Z+Z^	op X=0}.
}
]

This condition says that (X^	op Z) must be skew-symmetric.

The result is the matrix analogue of the sphere condition (x^	op v=0). In both cases, differentiating the constraint reveals the legal first-order directions.

The geometry and algorithms of Stiefel and Grassmann manifolds are developed in detail by Edelman, Arias, and Smith [@EdelmanAriasSmith1998], and by Absil, Mahony, and Sepulchre [@AbsilMahonySepulchre2008]. The Atlas will use only the portion needed for learning systems: what the object is, what counts as a legal direction, how redundant coordinates arise, and how an update can respect those structures.

## 8. Frames are not subspaces

A point (Xinoperatorname{St}(n,p)) carries more information than the subspace spanned by its columns.

For any orthogonal (Qin O(p)),

[
(XQ)^	op(XQ)
=
Q^	op X^	op XQ
=
I,
]

so (XQ) is another Stiefel point. But

[
operatorname{span}(XQ)
=
operatorname{span}(X).
]

If the problem depends only on the subspace, then (X) and (XQ) represent the same mathematical object.

That object belongs to the Grassmann manifold:

[
operatorname{Gr}(n,p)
cong
operatorname{St}(n,p)/O(p).
]

This quotient is not cosmetic notation. It changes what counts as a meaningful displacement.

Imagine describing a plane through the origin using two orthonormal basis vectors. Rotating those two basis vectors within the plane changes the frame but not the plane. If an objective depends only on the plane, movement corresponding purely to basis rotation is representational redundancy.

This is the first bridge to quotient geometry, which later chapters will develop explicitly.

## 9. Coordinates, objects, and redundancy

The Atlas repeatedly asks whether a difficult learning problem is difficult because the underlying object is difficult, or because the coordinates used to represent it introduce unnecessary degrees of freedom.

Geometry gives a disciplined way to ask that question.

Three spaces may need to be distinguished:

1. the **ambient coordinate space** in which we store numbers;
2. the **constraint manifold** describing admissible states;
3. a possible **quotient space** identifying coordinates that represent the same semantic object.

For a unit vector, the first two are enough:

[
mathbb R^d
supset
S^{d-1}.
]

For an orthonormal frame representing only a subspace, all three appear:

[
mathbb R^{n	imes p}
supset
operatorname{St}(n,p)
	o
operatorname{Gr}(n,p).
]

The move from parameters to geometry is therefore not “replace vectors by manifolds everywhere.” It is:

> identify the actual object, then choose mathematics that respects the object's admissible motions and equivalences.

Sometimes the actual object really is Euclidean. The geometric treatment should then reduce to ordinary linear algebra and calculus.

## 10. Why this matters for adaptive intelligence

The immediate machine-learning consequence is not that every hidden state should be normalized.

It is that architectural constraints create geometry whether or not the implementation acknowledges it.

If a state is constrained to unit norm, radial motion is not part of the represented degree of freedom. If a weight matrix is orthogonal, an unconstrained gradient contains components that attempt to leave the orthogonal group or Stiefel manifold. If several parameterizations encode the same function or subspace, Euclidean distance in parameter coordinates may measure representational redundancy rather than semantic change.

This changes how we should interpret optimization.

A generic Euclidean update is

[
x_{t+1}=x_t-eta g_t.
]

A geometry-aware update separates three operations:

[
	ext{ambient signal}
longrightarrow
	ext{tangent direction}
longrightarrow
	ext{manifold-respecting finite step}.
]

On the sphere, a simple version is

[
g_t^{mathrm{tan}}
=
g_t-(x_t^	op g_t)x_t,
]

followed by

[
x_{t+1}
=
R_{x_t}(-eta g_t^{mathrm{tan}}).
]

Later chapters will ask whether such geometry is merely a constraint-handling device or whether it can provide a better inductive organization for representation learning itself.

That is a research question, not a theorem of this chapter.

## 11. Four mistakes to avoid

### Mistake 1: “A tangent step stays on the manifold.”

No. A tangent vector is an infinitesimal direction. The finite point (x+v) generally leaves the manifold.

### Mistake 2: “Retraction means exponential map.”

No. A retraction matches the manifold locally to the required order. The exponential map follows geodesics exactly.

### Mistake 3: “An embedded manifold is globally flat because every tangent space is linear.”

No. Tangent spaces are local linear models. Curvature appears precisely in how those local models change and fail to identify globally.

### Mistake 4: “A matrix representation is the object.”

Not always. On the Grassmannian, many Stiefel frames represent the same subspace. Similar quotient phenomena recur throughout learning systems.

These mistakes are worth stating explicitly because later chapters will use the geometric vocabulary compactly.

## 12. What the figure establishes

The Wolfram witness in this chapter is deliberately modest.

It establishes, for a specific unit-sphere example, that:

- the tangent vector lies in the tangent plane;
- the spherical exponential map follows the great circle;
- normalization yields a different finite endpoint;
- both endpoints remain on the sphere.

It does not establish that a neural hidden state empirically lies on a sphere, that normalization is always beneficial, or that a specific optimizer should use the exponential map.

The figure carries geometry, not architectural advocacy.

## 13. Atlas connections

This chapter supplies the mathematical language for several later moves.

**Normalized representations.**  
If hidden states are constrained to (S^{d-1}), angular information and tangent transport become primary objects.

**Quotient geometry.**  
The Stiefel/Grassmann distinction provides the first concrete example of coordinate redundancy being removed by an equivalence relation.

**Positional geometry.**  
Rotary and spherical positional mechanisms act through structured transformations whose geometry matters.

**Manifold optimization.**  
Gradients, retractions, and transport will later be used algorithmically rather than merely descriptively.

**Representation as transport.**  
A layer can be viewed not only as a function evaluation but as movement through a structured state space.

The point is not that geometry replaces neural computation. The point is that once the computational state has structure, geometry tells us which changes are meaningful.

## 14. Closing coordinate change

The Euclidean picture asks:

> In which direction should this vector move?

The geometric picture asks three questions:

> What object does this vector represent?

> Which infinitesimal motions are legal for that object?

> How should a finite computation realize such a motion without destroying the constraint?

That is a small change in wording and a large change in architecture.

The map was never the mountain. But a good map tells us how to walk on it.

## References used in this chapter

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@EdelmanAriasSmith1998]
- [@Shoemake1985]

See `sources/source-locks/ATLAS-CH-GEOM-001.yaml` for exact source identities and claim scope.
