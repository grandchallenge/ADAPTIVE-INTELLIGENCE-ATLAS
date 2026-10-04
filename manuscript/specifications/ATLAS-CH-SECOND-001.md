# Chapter Specification — ATLAS-CH-SECOND-001

## Identity

**Title:** Curvature and Second-Order Structure  
**Part:** Optimization  
**Status:** specification-ready.  
**Epistemic class:** audited optimization/geometry prerequisites + classical second-order sources + Atlas synthesis.

## Contract

Develop Hessians, Newton and damped Newton methods, Fisher information, natural gradient, quasi-Newton methods, trust regions, matrix-free Hessian-vector products, and proximal structure.

## Hard prerequisites

- ATLAS-CH-OPTBASE-001
- ATLAS-CH-GEOM-001

## Required distinctions

1. gradient magnitude vs curvature;
2. positive-definite vs semidefinite vs indefinite Hessian;
3. Hessian vs Fisher information;
4. Euclidean gradient vs natural gradient;
5. exact Newton vs damped/regularized Newton;
6. exact Hessian vs quasi-Newton approximation;
7. unconstrained Newton vs trust-region subproblem;
8. explicit Hessian vs Hessian-vector products;
9. smooth second-order methods vs proximal nonsmooth structure;
10. local second-order information vs global guarantees.

## Newton model

For twice-differentiable f near x,

m_x(p)=f(x)+g^T p + 1/2 p^T H p,

with g=grad f(x), H=Hess f(x).

If H is nonsingular, the stationary Newton step solves

H p_N = -g.

If H is positive definite, p_N is a descent direction whenever g != 0 because

g^T p_N = -g^T H^{-1} g < 0.

This implication must not be stated for indefinite H.

## Exact SPD witness

Let

H=diag(1,4),
b=(1,1)^T,
f(x)=1/2 x^T H x - b^T x,
x0=0.

Then

g0=-b=(-1,-1)^T

and

p_N=H^{-1}b=(1,1/4)^T.

The step reaches the unique minimizer exactly:

x*=p_N.

Objective values:

f(0)=0,
f(x*)=-5/8.

## Indefinite control

Let

f(x,y)=1/2(x^2-y^2)

at

x0=(0,1)^T.

Then

g=(0,-1)^T,
H=diag(1,-1).

The raw Newton equation gives

p_N=(0,-1)^T.

But

g^T p_N = 1 > 0,

so it is an ascent direction.

Indeed,

f(0,1)=-1/2,
f(0,0)=0.

For trust-region radius Delta=1, the model is minimized at

p_TR=(0,1)^T,

giving

f(0,2)=-2.

Use this only as a local exact control showing why indefinite curvature needs globalization/regularization logic.

## Natural gradient witness

For metric

G=diag(1,4)

and Euclidean gradient

g=(1,1)^T,

the natural-gradient direction is

-G^{-1}g=(-1,-1/4)^T.

This is metric-dependent steepest descent.

Do not call it a Newton step unless the metric is separately identified with the Hessian under explicit assumptions.

## Quasi-Newton

State the secant condition

B_{k+1}s_k=y_k

for Hessian approximation B, with

s_k=x_{k+1}-x_k,
y_k=grad f(x_{k+1})-grad f(x_k).

Explain that BFGS-type methods update an approximation from gradient differences rather than recomputing the exact Hessian.

## Trust regions

Define

min_p g^T p + 1/2 p^T B p
subject to ||p|| <= Delta.

The radius is part of the algorithmic state controlling model validity.

Trust regions are not merely step clipping.

## Matrix-free curvature

Use Hessian-vector products Hv as the operative primitive for large problems when explicit H is too costly.

Do not imply that H need be stored.

## Proximal witness

For

h(x)=lambda |x|

the proximal operator at v is

prox_{alpha h}(v)
=
sign(v) max(|v|-alpha lambda,0).

Use v=3, alpha lambda=1 to get prox=2.

Use v=1/2 to get prox=0.

This distinguishes a nonsmooth implicit subproblem from ordinary gradient scaling.

## Failure boundaries

- indefinite Newton can be ascent;
- Hessian != Fisher in general;
- natural gradient != Newton in general;
- quasi-Newton != exact Hessian;
- trust-region != clipping;
- proximal operator != generic regularization label;
- HVP access != explicit Hessian formation;
- positive local curvature != global convexity;
- local quadratic accuracy != global optimality.

## Downstream handoff

Direct consumer:

- ATLAS-CH-MATRIXOPT-001.

MATRIXOPT may inherit curvature/preconditioning language, matrix-free action, and exact-vs-approximate distinctions. It must independently justify Shampoo, polar, orthogonalized, Muon-like, and rectangular-matrix claims.

## Sources

- [@NocedalWright2006]
- [@Amari1998NaturalGradient]
- [@Pearlmutter1994Hessian]
- [@ParikhBoyd2014Proximal]

Source lock:

sources/source-locks/ATLAS-CH-SECOND-001.yaml
