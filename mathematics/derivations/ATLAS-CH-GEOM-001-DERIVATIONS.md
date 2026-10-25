# ATLAS-CH-GEOM-001 — Derivation Packet

**Status:** source-checked producer revision for issue #443; editorial critic pending  
**Source lock:** \`sources/source-locks/ATLAS-CH-GEOM-001.yaml\`

## D1. Tangent space of the unit sphere

Let

\[
S^{d-1}
=
\{x\in\mathbb R^d:x^\top x=1\}.
\]

Take a differentiable curve \(\gamma(t)\in S^{d-1}\) with

\[
\gamma(0)=x,
\qquad
\dot\gamma(0)=v.
\]

Because

\[
\gamma(t)^\top\gamma(t)=1,
\]

differentiation at \(t=0\) gives

\[
0
=
\frac{d}{dt}
\left(
\gamma(t)^\top\gamma(t)
\right)\Big|_{t=0}
=
2x^\top v.
\]

Hence

\[
\boxed{
T_xS^{d-1}
=
\{v\in\mathbb R^d:x^\top v=0\}.
}
\]

Conversely, every \(v\perp x\) is realized as the initial velocity of the great-circle curve

\[
\gamma(t)
=
\cos(\|v\|t)x
+
\sin(\|v\|t)\frac{v}{\|v\|}.
\]

## D2. Normalized sphere retraction

For \(v\in T_xS^{d-1}\), define

\[
R_x(v)
=
\frac{x+v}{\|x+v\|}.
\]

Clearly,

\[
R_x(0)=x.
\]

Now let

\[
r(t)
=
\frac{x+tv}{\|x+tv\|}.
\]

Using \(\|x\|=1\),

\[
\frac{d}{dt}
\|x+tv\|\Big|_{t=0}
=
x^\top v.
\]

Therefore

\[
r'(0)
=
v-x(x^\top v).
\]

Since \(v\in T_xS^{d-1}\),

\[
x^\top v=0,
\]

and hence

\[
\boxed{r'(0)=v.}
\]

So normalization is a valid first-order retraction.

## D3. Exponential map versus normalized retraction

For nonzero \(v\in T_xS^{d-1}\),

\[
\operatorname{Exp}_x(v)
=
\cos(\|v\|)x
+
\sin(\|v\|)
\frac{v}{\|v\|}.
\]

Because \(x^\top v=0\),

\[
R_x(v)
=
\frac{x+v}{\sqrt{1+\|v\|^2}}.
\]

Both satisfy the same first-order condition at \(v=0\), but they are different finite maps.

For a unit tangent \(u\), let \(v=tu\) with \(t\to0\). In the orthonormal plane spanned by \(x,u\),

\[
\operatorname{Exp}_x(tu)=\cos(t)x+\sin(t)u,
\qquad
R_x(tu)=\frac{x+tu}{\sqrt{1+t^2}}.
\]

Use the exact Taylor coefficients

\[
\sin t=t-\frac{t^3}{6}+O(t^5),
\quad\frac{t}{\sqrt{1+t^2}}=t-\frac{t^3}{2}+O(t^5),
\]

\[
\cos t=1-\frac{t^2}{2}+\frac{t^4}{24}+O(t^6),
\quad\frac{1}{\sqrt{1+t^2}}=1-\frac{t^2}{2}+\frac{3t^4}{8}+O(t^6).
\]

Subtracting yields

\[
\boxed{\operatorname{Exp}_x(tu)-R_x(tu)=\frac{t^3}{3}u-\frac{t^4}{3}x+O(t^5).}
\]

Consequently \(\lim_{t\to0}u^\top(\operatorname{Exp}_x(tu)-R_x(tu))/t^3=1/3\). For \(0<t<\pi\), the endpoint angles \(t\) and \(\arctan t\) differ. At the plate's rational tangent \(v=(4/5,0,0)\), \(R_x(v)=(4,0,5)/\sqrt{41}\), while \(\operatorname{Exp}_x(v)=(\sin(4/5),0,\cos(4/5))\). The nonzero angular gap \(4/5-\arctan(4/5)\) is an analytic witness, not a floating-point inference.

## D4. SLERP remains on the sphere

Let \(x,y\in S^{d-1}\) satisfy

\[
x^\top y=\cos\theta,
\qquad
0<\theta<\pi.
\]

Define

\[
\operatorname{SLERP}(x,y;t)
=
\alpha x+\beta y,
\]

with

\[
\alpha
=
\frac{\sin((1-t)\theta)}{\sin\theta},
\qquad
\beta
=
\frac{\sin(t\theta)}{\sin\theta}.
\]

Then

\[
\|\alpha x+\beta y\|^2
=
\alpha^2+\beta^2+2\alpha\beta\cos\theta.
\]

The trigonometric identity

\[
\sin^2((1-t)\theta)
+
\sin^2(t\theta)
+
2\sin((1-t)\theta)\sin(t\theta)\cos\theta
=
\sin^2\theta
\]

implies

\[
\boxed{
\|\operatorname{SLERP}(x,y;t)\|=1.
}
\]

Thus the interpolation remains on the sphere.

Boundary cases:

- \(\theta\to0\): removable singularity;
- \(\theta=\pi\): shortest geodesic not unique.

## D5. Tangent space of the Stiefel manifold

For integers \(n\ge p\ge1\),

\[
\operatorname{St}(n,p)
=
\{X\in\mathbb R^{n\times p}:X^\top X=I_p\},
\]

let

\[
X(t)\in\operatorname{St}(n,p),
\qquad
X(0)=X,
\qquad
\dot X(0)=Z.
\]

Differentiate the constraint:

\[
\frac{d}{dt}
\left(
X(t)^\top X(t)
\right)\Big|_{t=0}
=
Z^\top X+X^\top Z
=
0.
\]

Hence

\[
\boxed{
T_X\operatorname{St}(n,p)
=
\{Z:X^\top Z+Z^\top X=0\}.
}
\]

The converse follows locally from the polar/QR retraction: if \(X^\top Z+Z^\top X=0\), then \((X+tZ)[(X+tZ)^\top(X+tZ)]^{-1/2}\) has initial derivative \(Z\). The symmetric constraint contributes \(p(p+1)/2\) independent equations, so \(\dim\operatorname{St}(n,p)=np-p(p+1)/2\).

## D6. Grassmann quotient structure

A Stiefel point \(X\) is an ordered orthonormal frame.

For any orthogonal matrix \(Q\in O(p)\),

\[
(XQ)^\top(XQ)
=
Q^\top X^\top XQ
=
I_p,
\]

and

\[
\operatorname{span}(XQ)
=
\operatorname{span}(X).
\]

Thus frames related by the right action of \(O(p)\) represent the same subspace. The Grassmannian is therefore the quotient

\[
\boxed{
\operatorname{Gr}(n,p)
\cong
\operatorname{St}(n,p)/O(p).
}
\]

As \(\dim O(p)=p(p-1)/2\), the quotient has dimension \(np-p(p+1)/2-p(p-1)/2=p(n-p)\). When \(p=n\), all frames span the same ambient subspace and the quotient is one point.

## D7. Chord versus geodesic distance

For unit vectors separated by angle \(\theta\),

\[
d_S(x,y)=\theta,
\]

whereas

\[
\|x-y\|
=
\sqrt{2-2\cos\theta}
=
2\sin\frac{\theta}{2}.
\]

The distance formula also holds at \(\theta=\pi\); only the minimizing geodesic is nonunique there. As \(\theta\to0\),

\[
2\sin\frac{\theta}{2}
=
\theta+O(\theta^3).
\]

Local Euclidean distance therefore approximates geodesic distance without making the sphere globally flat.

## D8. When tangent projection is a gradient

For the induced metric \(g_x(u,v)=u^\top v\) on an embedded manifold, the projected ambient vector \(\operatorname{Proj}_{T_xM}\nabla\bar f(x)\) satisfies \(g_x(\operatorname{Proj}\nabla\bar f,v)=df_x(v)\) for every tangent \(v\). Thus it is the Riemannian gradient. For another positive-definite metric \(g_x\), the tangent gradient is instead the unique tangent vector \(w\) satisfying \(g_x(w,v)=df_x(v)\); Euclidean projection alone need not produce \(w\).

## Claim boundary

These derivations establish standard finite-dimensional sphere, Stiefel, and Grassmann facts used by the Atlas. They do not define a complete Riemannian-geometry curriculum and do not imply that any particular neural representation empirically lies on one of these manifolds.
