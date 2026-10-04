# Computational Witness — ATLAS-CW-SECOND-001

## Purpose

Replay exact finite second-order calculations used by ATLAS-CH-SECOND-001.

This is a mathematical witness, not a benchmark of optimizer performance on trained neural networks.

## W1. Positive-definite Newton step

Use

H=diag(1,4),
b=(1,1)^T,

and

f(x)=1/2 x^T H x-b^T x.

At x0=(0,0)^T,

g0=Hx0-b=(-1,-1)^T.

Solve

H p=-g0.

Because

H^{-1}=diag(1,1/4),

p_N=(1,1/4)^T.

The new gradient is

H p_N-b=(0,0)^T.

Thus one exact Newton step reaches the quadratic minimizer.

Objective replay:

f(x0)=0,

f(p_N)=-5/8.

Directional check:

g0^T p_N
=
-1-1/4
=
-5/4
<
0.

## W2. Indefinite Newton ascent

Use

f(x,y)=1/2(x^2-y^2)

at

z0=(0,1)^T.

Then

g=(0,-1)^T,

H=diag(1,-1).

The Newton equation

H p=-g

gives

p_N=(0,-1)^T.

Directional derivative:

g^T p_N=1>0.

Objective replay:

f(0,1)=-1/2,

f((0,1)+(0,-1))
=
f(0,0)
=
0.

So the full Newton step increases the objective.

## W3. Trust-region control

At the same point, use radius

Delta=1.

The quadratic model increment is

q(p)
=
-p_2
+
1/2 p_1^2
-
1/2 p_2^2.

Over

p_1^2+p_2^2<=1,

the exact minimizer is

p_TR=(0,1)^T.

Then

q(p_TR)=-3/2.

The new point is

(0,2)^T,

and

f(0,2)=-2.

So the trust-region subproblem chooses a negative-curvature boundary step rather than the raw Newton stationary point.

## W4. Natural-gradient metric

Let

G=diag(1,4),

g=(1,1)^T.

Euclidean steepest-descent direction:

d_E=(-1,-1)^T.

Metric/natural-gradient direction:

d_G=-G^{-1}g=(-1,-1/4)^T.

The directions differ.

Metric norms:

||d_E||_G^2
=
1+4
=
5.

||d_G||_G^2
=
1+4(1/16)
=
5/4.

The witness shows that changing the metric changes the steepest direction.

It does not identify G with the Hessian.

## W5. Hessian-vector product

For

H=diag(1,4)

and

v=(2,-1)^T,

H v=(2,-4)^T.

For the quadratic gradient

grad f(x)=Hx-b,

the directional difference is

[grad f(x+epsilon v)-grad f(x)]/epsilon
=
Hv

for every nonzero epsilon.

This is exact because the gradient is affine.

## W6. Secant replay

For the same SPD quadratic, choose displacement

s=(1,2)^T.

Then exact gradient change is

y=Hs=(1,8)^T.

A quasi-Newton approximation satisfying

B s=y

matches curvature action along s.

That single secant equation does not determine the full exact Hessian uniquely.

## W7. Proximal soft threshold

Let

h(x)=lambda |x|

with

alpha lambda=1.

Then

prox(v)
=
sign(v) max(|v|-1,0).

Cases:

v=3 -> 2,

v=-3 -> -2,

v=1/2 -> 0.

This is the exact scalar proximal map.

## Replay table

| Check | Exact result |
| --- | --- |
| SPD Newton step | (1,1/4)^T |
| SPD objective after step | -5/8 |
| SPD directional derivative | -5/4 |
| indefinite Newton direction | (0,-1)^T |
| indefinite Newton directional derivative | 1 |
| indefinite objective after Newton step | 0 |
| trust-region step, Delta=1 | (0,1)^T |
| trust-region model decrease | -3/2 |
| natural-gradient direction | (-1,-1/4)^T |
| H(2,-1)^T | (2,-4)^T |
| secant pair | s=(1,2)^T, y=(1,8)^T |
| prox(3), threshold 1 | 2 |
| prox(1/2), threshold 1 | 0 |

## Claim boundary

This witness proves only the finite arithmetic and mechanism separations declared above.

It does not prove global convergence, empirical neural-network superiority, Fisher/Hessian equality, or universal trust-region/proximal performance.
