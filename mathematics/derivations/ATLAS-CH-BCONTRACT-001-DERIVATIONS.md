# ATLAS-CH-BCONTRACT-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm convention:** spectral/operator \(2\)-norm where a matrix norm is used  
**Source lock:** \`sources/source-locks/ATLAS-CH-BCONTRACT-001.yaml\`

## D1. Provisional Atlas boundary-contract object

For a component

\[
f:\mathcal X\to\mathcal Y,
\]

the Atlas uses the provisional explanatory object

\[
\boxed{
C_f=
(\mathcal X,\mathcal Y,\Sigma,\mathcal I,\mathcal S,\mathcal E).
}
\]

The fields mean:

- \(\mathcal X\): admissible input domain;
- \(\mathcal Y\): admissible output domain;
- \(\Sigma\): semantic declaration: what the boundary state means;
- \(\mathcal I\): invariants/geometric obligations;
- \(\mathcal S\): differential sensitivity information or admissible perturbation behavior;
- \(\mathcal E\): numerical error, precision, or conditioning obligations.

This tuple is an Atlas explanatory device, not a universal standard.

## D2. Shape compatibility is weaker than semantic compatibility

Define

\[
f:\mathbb R^2\setminus\{0\}\to S^1,
\qquad
f(x)=\frac{x}{\|x\|_2}.
\]

Its output semantics are **direction only**.

Now define

\[
g:\mathbb R^2\to\mathbb R,
\qquad
g(y)=\|y\|_2,
\]

and suppose the downstream component interprets \(\|y\|_2\) as amplitude.

The tensor shapes compose:

\[
\mathbb R^2
\xrightarrow{f}
\mathbb R^2
\xrightarrow{g}
\mathbb R.
\]

But

\[
g(f(x))=1
\]

for every nonzero \(x\).

For

\[
x=(3,4),
\]

the original magnitude is \(5\), while the composed downstream observation is \(1\).

Thus shape compatibility does not establish semantic compatibility.

## D3. Chain-rule boundary sensitivity

Let

\[
f(x)=Ax,
\qquad
A=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\]

and

\[
g(y)=By,
\qquad
B=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
\]

Then

\[
g\circ f(x)
=
BAx,
\]

with

\[
\boxed{
C=BA=
\begin{pmatrix}
2&1/2\\
0&1
\end{pmatrix}.
}
\]

The chain rule gives

\[
J_{g\circ f}(x)
=
J_g(f(x))J_f(x)
=
BA.
\]

Since the maps are linear, this Jacobian is constant.

## D4. JVP and VJP

For a perturbation direction \(v\),

\[
\operatorname{JVP}_{g\circ f}(v)
=
Cv.
\]

For an output cotangent \(u\),

\[
\operatorname{VJP}_{g\circ f}(u)
=
C^\top u.
\]

For example, with

\[
v=
\begin{pmatrix}
1\\
-1
\end{pmatrix},
\]

\[
Cv
=
\begin{pmatrix}
3/2\\
-1
\end{pmatrix}.
\]

With

\[
u=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\]

\[
C^\top u
=
\begin{pmatrix}
2\\
3/2
\end{pmatrix}.
\]

These are exact directional forward and reverse sensitivities. Automatic differentiation computes such products without requiring an explicitly materialized dense Jacobian in the general case [@BaydinEtAl2018].

## D5. Exact local amplification

For

\[
C=
\begin{pmatrix}
2&1/2\\
0&1
\end{pmatrix},
\]

\[
C^\top C
=
\begin{pmatrix}
4&1\\
1&5/4
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_{\pm}
=
\frac{21\pm\sqrt{185}}{8}.
\]

Therefore

\[
\boxed{
\|C\|_2
=
\sqrt{\frac{21+\sqrt{185}}8}
\approx
2.079707626949502.
}
\]

This says that, at this boundary and in this norm, some infinitesimal input direction can be amplified by about \(2.08\).

It does not say that an arbitrary nonlinear composition is globally \(2.08\)-Lipschitz.

## D6. Power iteration estimates the dominant local gain

Power iteration on

\[
M=C^\top C
\]

uses

\[
v_{k+1}
=
\frac{Mv_k}{\|Mv_k\|_2}.
\]

The Rayleigh quotient estimates the largest eigenvalue:

\[
\mu_k
=
\frac{v_k^\top Mv_k}{v_k^\top v_k},
\]

so

\[
\sqrt{\mu_k}
\]

estimates \(\|C\|_2\).

Starting from the normalized vector proportional to \((1,1)\), Wolfram replay gives spectral-norm estimates

\[
1.9039433,\;
2.0701070,\;
2.0792647,\;
2.0796874,\;
2.0797067,\;
2.0797076,\ldots
\]

converging to the exact value

\[
2.079707626949502\ldots
\]

The estimator is useful only when its convergence assumptions and target quantity are explicit.

## D7. Submultiplicative bound

The chain rule and induced norm give

\[
\|J_gJ_f\|_2
\le
\|J_g\|_2\|J_f\|_2.
\]

This is a local composition bound.

It does not imply that the full nonlinear system has a global stability guarantee unless suitable uniform bounds and additional hypotheses hold over the entire relevant state region.

## D8. Separator information can be insufficient

Suppose a boundary compiler retains only

\[
s(y)=y_1.
\]

Let the downstream behavior depend on

\[
h(y)=y_2.
\]

The states

\[
y=(0,1),
\qquad
y'=(0,2)
\]

have the same summary

\[
s(y)=s(y')=0,
\]

but

\[
h(y)\neq h(y').
\]

A low-order separator can therefore preserve some interface information while erasing information that later composition needs.

The burden is to justify that the retained separator variables are sufficient for the property being claimed.

## D9. Local-to-global warning

A boundary contract resembles local compatibility data: it states what neighboring components are permitted to assume about one another.

Sheaf language is useful here because sheaves formalize compatibility and gluing of local data [@Curry2013Sheaves].

The Atlas does not claim that every learned-system boundary contract is literally a sheaf, nor that local agreement automatically yields a desired global system property.

## Claim boundary

This packet establishes exact finite-dimensional sensitivity calculations and one semantic incompatibility example. It defines an Atlas boundary-contract object for exposition. It does not prove a universal composition theorem, global safety, or the existence of the remembered GCL MODULUS BoundaryContract/SeparatorCompiler implementation in the current public MODULUS repository.
