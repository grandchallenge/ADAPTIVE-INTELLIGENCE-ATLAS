# ATLAS-CH-GEOM-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm/inner product:** Euclidean unless explicitly generalized  
**Source lock:** `sources/source-locks/ATLAS-CH-GEOM-001.yaml`

This packet contains Atlas-owned derivations used by the chapter. Source references establish the surrounding theory and terminology; the calculations below are reproduced explicitly so the manuscript does not ask the reader to trust an unexpanded citation.

## D1. Tangent space of the unit sphere

Let

[
S^{d-1}={xinmathbb R^d:x^	op x=1}.
]

Define (F(x)=x^	op x-1). A differentiable curve (gamma(t)in S^{d-1}) with (gamma(0)=x) and (dotgamma(0)=v) satisfies

[
F(gamma(t))=0.
]

Differentiate at (t=0):

[
0=rac{d}{dt}gamma(t)^	opgamma(t)igg|_{t=0}
=2x^	op v.
]

Hence every tangent vector obeys (x^	op v=0). Conversely, for any (vperp x), the great-circle curve

[
gamma(t)=cos(|v|t)x+sin(|v|t)rac{v}{|v|}
]

lies on the sphere and has (gamma(0)=x,dotgamma(0)=v). Therefore

[
oxed{T_xS^{d-1}={vinmathbb R^d:x^	op v=0}.}
]

## D2. Normalized first-order retraction

For (vin T_xS^{d-1}), define

[
R_x(v)=rac{x+v}{|x+v|}.
]

The two defining properties of a retraction at (x) are

[
R_x(0)=x
]

and

[
D R_x(0)[v]=v
qquad
	ext{for }vin T_xS^{d-1}.
]

The first is immediate. For the second, set

[
r(t)=rac{x+t v}{|x+t v|}.
]

Using (|x|=1),

[
rac{d}{dt}|x+t v|igg|_{t=0}
=
x^	op v.
]

Therefore

[
r'(0)=v-x(x^	op v).
]

Because (vin T_xS^{d-1}), (x^	op v=0), so

[
oxed{r'(0)=v.}
]

Thus normalization is a valid first-order retraction on the sphere wherever (x+v
eq0).

### Retraction is not the exponential map

On the unit sphere,

[
operatorname{Exp}_x(v)
=
cos(|v|)x
+
sin(|v|)rac{v}{|v|}
]

for nonzero (vin T_xS^{d-1}), whereas

[
R_x(v)=rac{x+v}{sqrt{1+|v|^2}}
]

because (x^	op v=0).

Their Taylor expansions agree to first order but not globally:

[
operatorname{Exp}_x(v)
=
x+v-rac{|v|^2}{2}x+O(|v|^3),
]

[
R_x(v)
=
x+v-rac{|v|^2}{2}x-rac{|v|^2}{2}v+O(|v|^4).
]

The retraction is therefore a locally faithful return map, not a synonym for geodesic motion.

## D3. Great-circle interpolation / SLERP

Let (x,yin S^{d-1}) with

[
x^	op y=cos	heta,
qquad
0<	heta<pi.
]

Define

[
operatorname{SLERP}(x,y;t)
=
rac{sin((1-t)	heta)}{sin	heta}x
+
rac{sin(t	heta)}{sin	heta}y,
qquad
tin[0,1].
]

Let

[
alpha=rac{sin((1-t)	heta)}{sin	heta},
qquad
eta=rac{sin(t	heta)}{sin	heta}.
]

Then

[
|alpha x+eta y|^2
=
alpha^2+eta^2+2alphaetacos	heta.
]

The trigonometric identity

[
sin^2((1-t)	heta)+sin^2(t	heta)
+2sin((1-t)	heta)sin(t	heta)cos	heta
=
sin^2	heta
]

gives

[
oxed{|operatorname{SLERP}(x,y;t)|=1.}
]

The curve lies on the two-plane (operatorname{span}{x,y}), follows the shorter great-circle arc, and has angular progress (t	heta).

### Boundary cases

- As (	heta	o0), the formula has a removable singularity and tends to normalized/ordinary interpolation locally.
- At (	heta=pi), the shortest geodesic is not unique; an additional tangent direction is required. The denominator (sin	heta) correctly signals this ambiguity.

## D4. Tangent space of the Stiefel manifold

For (Xinmathbb R^{n	imes p}),

[
operatorname{St}(n,p)
=
{X:X^	op X=I_p}.
]

Let (X(t)inoperatorname{St}(n,p)) be differentiable with (X(0)=X) and (dot X(0)=Z). Differentiate the constraint:

[
rac{d}{dt}left(X(t)^	op X(t)ight)igg|_{t=0}
=
Z^	op X+X^	op Z
=
0.
]

Hence

[
oxed{
T_Xoperatorname{St}(n,p)
=
{Z:X^	op Z+Z^	op X=0}.
}
]

This is the matrix analogue of “velocity must be orthogonal to the constraint normal.”

## D5. Stiefel versus Grassmann

A Stiefel point (Xinoperatorname{St}(n,p)) is an ordered orthonormal frame. Multiplying by (Qin O(p)) changes the frame:

[
Xmapsto XQ,
]

but does not change the subspace spanned by its columns:

[
operatorname{span}(XQ)=operatorname{span}(X).
]

The Grassmann manifold identifies all such frames:

[
oxed{
operatorname{Gr}(n,p)
cong
operatorname{St}(n,p)/O(p).
}
]

Thus the Stiefel manifold retains basis orientation inside the subspace, while the Grassmann manifold quotients that basis choice away.

## D6. Computational witness identities

The Wolfram source `figures/wolfram/ATLAS-FIG-MANIFOLD-001.wl` uses

[
x=(0,0,1),qquad v=(0.8,0,0)
]

and computes:

[
operatorname{Exp}_x(v)
=
cos(0.8)x+sin(0.8)rac{v}{0.8},
]

[
R_x(v)=rac{x+v}{|x+v|}.
]

The corresponding rendered witness is

`figures/masters/ATLAS-FIG-MANIFOLD-001.png`.

The geometry shown is exact for this unit-sphere example. Perspective and label placement are not mathematical data.

## Source boundary

- General differential-geometry definitions: `GEOM-LEE-2018`.
- Retraction and matrix-manifold optimization language: `GEOM-ABSIL-MAHONY-SEPULCHRE-2008`.
- Stiefel/Grassmann algorithmic geometry: `GEOM-EDELMAN-ARIAS-SMITH-1998`.
- Historical SLERP attribution: `GEOM-SHOEMAKE-1985`.

No claim about learned representations being spherical follows from these derivations.
