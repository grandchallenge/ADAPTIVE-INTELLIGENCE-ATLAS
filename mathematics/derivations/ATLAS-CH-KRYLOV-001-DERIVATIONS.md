# Iterative Subspace Derivation Packet

## Scope

This packet develops the classical finite-dimensional iterative-subspace substrate used by chapter ATLAS-155. It does not transfer classical convergence guarantees to later learned nonlinear transport.

## D1. Operator-generated subspace

For Ax=b with r0=b-Ax0, define the m-step operator-generated space

K_m(A,r0)=span{r0, A r0, ..., A^(m-1) r0}.

Every correction in this space has the form q_(m-1)(A)r0. Therefore a corresponding residual can be written p_m(A)r0 with p_m(0)=1.

## D2. Arnoldi relation

Starting from v1=r0/||r0||_2, exact Arnoldi repeatedly applies A and orthogonalizes against the current basis. It yields orthonormal V_m and upper-Hessenberg Hbar_m satisfying

A V_m = V_(m+1) Hbar_m.

Basis construction and the reduced projected solve are distinct steps.

## D3. Lanczos specialization

For symmetric or Hermitian A, the projected Arnoldi matrix is both symmetric and upper Hessenberg, hence tridiagonal.

The exact recurrence is

beta_(j-1) v_(j-1) + alpha_j v_j + beta_j v_(j+1) = A v_j.

This short recurrence is an exact-arithmetic structural consequence, not a finite-precision guarantee of perfect orthogonality.

## D4. Galerkin projection

Let xm=x0+V_m y and rm=r0-A V_m y.

The Galerkin condition

V_m^T rm=0

gives

(V_m^T A V_m)y=V_m^T r0.

## D5. Minimum residual

A minimum-residual method instead solves

min_y ||r0-A V_m y||_2.

With the Arnoldi relation and r0=beta v1, this becomes the reduced least-squares problem

min_y ||beta e1-Hbar_m y||_2.

Galerkin orthogonality and minimum-residual projection are not interchangeable.

## D6. Residual versus error

If x* solves Ax*=b and em=x*-xm, then

A em=rm.

For nonsingular A,

em=A^(-1)rm,

so

||em||_2 <= ||A^(-1)||_2 ||rm||_2

and

||rm||_2 <= ||A||_2 ||em||_2.

Residual and error are linked through the operator and norm; they are not the same quantity.

## D7. Exact two-dimensional witness

Take

A=diag(1,2,4),
b=(1,1,1)^T,
x0=0.

Then r0=b and Ab=(1,2,4)^T. Use

V=[b,Ab]=[[1,1],[1,2],[1,4]].

The projected system is

V^T A V = [[7,21],[21,73]],

V^T b=[3,7]^T.

Its solution is

c=[36/35,-1/5]^T.

Therefore

x2=Vc=[29/35,22/35,8/35]^T,

and

r2=b-Ax2=[6,-9,3]^T/35.

Direct checks give

b^T r2=0,

(Ab)^T r2=0,

and

||r2||_2^2=18/175.

The exact solution is

x*=[1,1/2,1/4]^T,

so

e2=[6/35,-9/70,3/140]^T

and A e2=r2.

For this SPD system,

||e2||_A^2=9/140.

## D8. Lanczos replay

Normalize

v1=(1,1,1)^T/sqrt(3).

Then

alpha1=7/3,
beta1=sqrt(14)/3,

and

v2=(-4,-1,5)^T/sqrt(42).

The next diagonal coefficient is

alpha2=59/21.

Thus

T2=[[7/3,sqrt(14)/3],[sqrt(14)/3,59/21]].

Continuing one step gives beta2=3 sqrt(3)/7.

This exhibits the symmetric tridiagonal projected structure.

## D9. Conditioning control

Take

Ac=diag(1,100,10000),
b=(1,1,1)^T,
x0=0.

The one-dimensional SPD Galerkin/conjugate-gradient step uses

alpha=(b^T b)/(b^T Ac b)=1/3367.

Hence

r1=[3366,3267,-6633]^T/3367

and

||r1||_2^2=19602/3367 > 3=||r0||_2^2.

So a valid conjugate-gradient step can increase Euclidean residual norm.

The correct minimization statement concerns the Ac-norm of the error. The initial squared Ac-norm error is 10101/10000, while after the step it is 33980067/33670000, which is smaller.

## D10. Preconditioning

Left preconditioning replaces A by M^(-1)A and b by M^(-1)b.

Right preconditioning solves A M^(-1)y=b and recovers x=M^(-1)y.

The effective operator is changed; preconditioning is not equivalent to merely taking more iterations.

## D11. Matrix-free access

Repeated evaluation of v -> A v is sufficient to generate these subspaces. Explicit dense storage of A is not definitionally required.

## D12. Finite-precision boundary

Exact orthogonality is an algebraic statement. Floating-point implementations can lose orthogonality. Restarting reduces memory but can discard useful directions. Reorthogonalization improves basis quality at additional cost.

## Claim boundary

This packet establishes the classical exact definitions, Arnoldi/Lanczos projected relations, Galerkin/minimum-residual distinction, exact finite witnesses, residual/error boundary, and preconditioning semantics.

It does not establish rapid convergence for arbitrary operators or any classical convergence theorem for later learned nonlinear transport.
