# Derivations — ATLAS-CH-SECOND-001

## Scope

This packet develops exact local second-order identities used by the chapter. It does not establish global convergence on arbitrary nonconvex objectives.

## D1. Quadratic model

For twice-differentiable f at x,

m_x(p)=f(x)+g^T p + 1/2 p^T H p,

where

g=grad f(x),
H=Hess f(x).

The stationary point of the model satisfies

H p = -g.

If H is nonsingular, the formal Newton step is

p_N=-H^{-1}g.

## D2. Positive-definite descent

If H is positive definite and g != 0,

g^T p_N
=
-g^T H^{-1} g
<
0.

Therefore the Newton direction is a descent direction under this condition.

Positive definiteness is load-bearing.

## D3. Exact SPD quadratic

Let

H=diag(1,4),
b=(1,1)^T,

and

f(x)=1/2 x^T H x-b^T x.

Then

grad f(x)=Hx-b.

At x0=0,

g0=(-1,-1)^T.

The Newton equation gives

p_N=-H^{-1}g0=H^{-1}b=(1,1/4)^T.

At

x*=p_N,

H x*-b=0,

so x* is the exact minimizer.

The objective value is

f(x*)
=
1/2[(1)^2+4(1/4)^2] - [1+1/4]
=
1/2[1+1/4] - 5/4
=
5/8-10/8
=
-5/8.

## D4. Indefinite Newton direction can be ascent

Let

f(x,y)=1/2(x^2-y^2).

At

z0=(0,1)^T,

g=(0,-1)^T,

H=diag(1,-1).

Since H^{-1}=H,

p_N=-H^{-1}g
=
(0,-1)^T.

Then

g^T p_N
=
1
>
0.

So p_N is an ascent direction.

The full Newton step reaches

z0+p_N=(0,0),

and

f(0,1)=-1/2,

f(0,0)=0.

The objective increases.

## D5. Trust-region control on the same model

At z0=(0,1), the exact quadratic model equals the objective difference because f itself is quadratic.

With trust-region radius Delta=1,

minimize
q(p)=g^T p + 1/2 p^T H p

subject to

p_1^2+p_2^2 <= 1.

Here

q(p)= -p_2 + 1/2 p_1^2 - 1/2 p_2^2.

For any fixed p_2, the p_1 term is minimized by p_1=0.

Then minimize

q(0,p_2)= -p_2 - 1/2 p_2^2

over |p_2|<=1.

Its derivative is

-1-p_2,

which is nonpositive on [-1,1] and zero only at p_2=-1.

Hence the minimum over the interval occurs at p_2=1:

p_TR=(0,1)^T.

Then

q(p_TR)=-3/2.

The new point is

(0,2)^T,

where

f(0,2)=-2.

Thus the trust-region subproblem selects the negative-curvature boundary rather than the raw Newton stationary point.

## D6. Damping

A damped/regularized Newton system has form

(H+lambda I)p=-g

for declared lambda.

For sufficiently large lambda, an indefinite H+lambda I can become positive definite.

This changes the local model and must not be described as the exact Newton step.

## D7. Hessian-vector products

For scalar f and vector v,

H v
=
d/d epsilon [ grad f(x+epsilon v) ] at epsilon=0.

This directional derivative identity allows curvature action to be computed without materializing the dense Hessian.

Pearlmutter's R-operator construction provides an exact implementation route in the cited neural-computation setting.

## D8. Fisher metric and natural gradient

Let G(theta) be a positive-definite metric.

The steepest-descent direction under the local quadratic norm

||delta||_G^2=delta^T G delta

with a fixed first-order decrease constraint is proportional to

-G^{-1}g.

For the Fisher information metric F(theta), this becomes the natural gradient

-F(theta)^{-1} grad L(theta),

when the inverse exists or an appropriate regularized/pseudoinverse form is declared.

This is a metric statement.

It is not a generic identity between F and the Hessian of L.

## D9. Exact metric witness

Let

G=diag(1,4),
g=(1,1)^T.

Euclidean steepest descent points along

-g=(-1,-1)^T.

Metric steepest descent points along

-G^{-1}g=(-1,-1/4)^T.

The directions differ because the metric changes the unit ball.

## D10. Quasi-Newton secant structure

Let

s_k=x_{k+1}-x_k,

y_k=g_{k+1}-g_k.

A Hessian approximation B_{k+1} can be required to satisfy

B_{k+1}s_k=y_k.

This secant condition matches observed gradient change along the latest displacement.

It does not imply B_{k+1}=H(x_{k+1}) globally or in all directions.

## D11. BFGS positivity boundary

For the standard BFGS Hessian update, if B_k is positive definite and

y_k^T s_k > 0,

then the updated B_{k+1} is positive definite.

The curvature condition is therefore load-bearing for the usual positivity guarantee.

The chapter uses this only as a structural boundary, not as a universal convergence theorem.

## D12. Proximal operator

For a proper declared function h and alpha>0,

prox_{alpha h}(v)
=
argmin_x [
h(x)+1/(2 alpha)||x-v||_2^2
].

For

h(x)=lambda |x|,

the scalar minimizer is soft thresholding:

prox_{alpha lambda |.|}(v)
=
sign(v) max(|v|-alpha lambda,0).

For alpha lambda=1:

v=3 -> 2,

v=1/2 -> 0.

The zero result arises from the nonsmooth implicit subproblem, not from clipping a gradient.

## D13. Proximal-gradient split

For composite objective

F(x)=f(x)+h(x)

with differentiable f and proximable h,

x_{k+1}
=
prox_{alpha h}
(
x_k-alpha grad f(x_k)
).

This separates the smooth explicit gradient step from the nonsmooth implicit proximal step.

## D14. Local versus global structure

A positive-definite Hessian at one point gives local curvature information.

It does not imply that the entire objective is globally convex.

Likewise, an exact Newton step solves the stationary condition of the local quadratic model, not necessarily the original global optimization problem.

## Claim boundary

Established here:

- Newton stationary equation;
- positive-definite Newton descent identity;
- exact SPD quadratic witness;
- exact indefinite Newton-ascent witness;
- exact trust-region boundary solution for the chosen control;
- Hessian-vector directional derivative identity;
- metric natural-gradient direction;
- quasi-Newton secant relation;
- scalar soft-threshold proximal witness.

Not established here:

- global convergence for arbitrary nonconvex objectives;
- generic Fisher=Hessian identity;
- universal superiority of natural gradient;
- exactness of quasi-Newton approximations;
- universal efficacy of one trust-region or damping policy.
