# Exact Replay — Iterative Subspace Methods

## Purpose

Replay the finite arithmetic used by Atlas chapter 155.

This is a classical linear-algebra witness, not a learned-model experiment.

## Primary system

A=diag(1,2,4),

b=(1,1,1)^T,

x0=0.

The first two generated directions are

b=(1,1,1)^T

and

Ab=(1,2,4)^T.

Use the two-column basis

V=[[1,1],[1,2],[1,4]].

## Reduced system

Compute

V^T A V=[[7,21],[21,73]],

V^T b=[3,7]^T.

The exact coefficient vector is

c=[36/35,-1/5]^T.

Therefore

x2=[29/35,22/35,8/35]^T,

and

r2=[6,-9,3]^T/35.

## Orthogonality replay

Check

b^T r2=0,

and

(Ab)^T r2=0.

Therefore

V^T r2=0.

The squared residual norm is

||r2||_2^2=18/175.

## Error replay

The exact solution is

x*=[1,1/2,1/4]^T.

Thus

e2=[6/35,-9/70,3/140]^T.

Direct multiplication gives

A e2=r2.

The squared energy norm is

e2^T A e2=9/140.

## Orthonormal symmetric replay

Set

v1=(1,1,1)^T/sqrt(3).

Then

alpha1=7/3,

beta1=sqrt(14)/3,

v2=(-4,-1,5)^T/sqrt(42),

and

alpha2=59/21.

Therefore the two-dimensional projected symmetric matrix is

T2=[[7/3,sqrt(14)/3],[sqrt(14)/3,59/21]].

Continuing one step gives

beta2=3 sqrt(3)/7.

## Conditioning control

Use

Ac=diag(1,100,10000),

with the same b and x0.

The one-dimensional SPD Galerkin/conjugate-gradient coefficient is

alpha=1/3367.

The residual is

r1=[3366,3267,-6633]^T/3367.

Therefore

||r1||_2^2=19602/3367,

which is larger than

||r0||_2^2=3.

The squared energy error changes from

10101/10000

to

33980067/33670000,

which is smaller.

## Claim boundary

This artifact proves only the declared finite arithmetic and the separation between Euclidean residual behavior and SPD energy-norm minimization.

It does not prove rapid convergence for arbitrary matrices or any guarantee for later learned nonlinear transport.
