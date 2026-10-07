# ATLAS-CH-SPECTRALDIAG-001 — Derivations

## Claim boundary
These derivations certify the finite exact examples and definitions below. They do not establish that any one spectral diagnostic is sufficient for learned-system behavior or mechanism identification.

## D1. Named operator first
For a square matrix or linear operator A, the eigenvalue spectrum is

\[
\sigma(A)=\{\lambda:\det(A-\lambda I)=0\}.
\]

For a finite matrix A, the singular values are the nonnegative square roots of the eigenvalues of A^*A.

These are different summaries. Neither definition supplies a causal interpretation.

## D2. Pseudospectrum
Using the inherited spectral 2-norm convention,

\[
\Lambda_\varepsilon(A)=\{z:\sigma_{\min}(zI-A)\le \varepsilon\}.
\]

Outside the spectrum this is equivalent to a resolvent threshold through

\[
\|(zI-A)^{-1}\|_2=\sigma_{\min}(zI-A)^{-1}.
\]

The audited NONNORMAL packet governs the exact scope of this equivalence and its transient-growth interpretation.

## D3. Equal eigenvalues do not fix finite response
Let

\[
D=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix},\qquad
N=\begin{pmatrix}1/2&2\\0&1/2\end{pmatrix}.
\]

Both are triangular with diagonal entries 1/2, hence

\[
\sigma(D)=\sigma(N)=\{1/2,1/2\}.
\]

For

\[
e_2=(0,1)^\top,
\]

we have

\[
De_2=(0,1/2)^\top,
\]

so

\[
\|De_2\|_2^2=1/4.
\]

But

\[
Ne_2=(2,1/2)^\top,
\]

so

\[
\|Ne_2\|_2^2=4+1/4=17/4.
\]

Therefore

\[
\boxed{\|Ne_2\|_2=\sqrt{17}/2>1}
\]

while

\[
\boxed{\|De_2\|_2=1/2}.
\]

Equal eigenvalue multisets do not determine finite-horizon response.

## D4. Equal singular and eigenvalue multisets do not fix interface response
Let

\[
A=\operatorname{diag}(2,1/2),\qquad
B=\operatorname{diag}(1/2,2).
\]

Both matrices have eigenvalue multiset

\[
\{2,1/2\}
\]

and singular-value multiset

\[
\{2,1/2\}.
\]

For the fixed interface vector

\[
e_1=(1,0)^\top,
\]

\[
Ae_1=(2,0)^\top,
\qquad
Be_1=(1/2,0)^\top.
\]

Hence

\[
\boxed{\|Ae_1\|_2=2},
\qquad
\boxed{\|Be_1\|_2=1/2}.
\]

The global spectral multisets agree, but their orientation relative to the declared interface does not.

Thus a relative-position diagnostic requires vectors/subspaces/interfaces in addition to operator-intrinsic spectral summaries.

## D5. Zero spectral drift can coexist with interface drift
Suppose time t uses A and time t+1 uses B from D4. Any drift metric that depends only on the sorted eigenvalue multiset or sorted singular-value multiset returns zero.

Yet for fixed e1 the response norm changes by

\[
2-1/2=3/2.
\]

Therefore

\[
\boxed{\text{zero spectral-summary drift}\not\Rightarrow\text{zero interface-response drift}}.
\]

## D6. Local Jacobian spectrum does not determine nonlinear transport
Define

\[
F(x)=\frac12x,
\qquad
G(x)=\frac12x+x^2.
\]

At x0=0,

\[
F'(0)=G'(0)=1/2.
\]

So the one-dimensional Jacobian spectra agree exactly at the reference state.

But at x=1/2,

\[
F(1/2)=1/4,
\]

while

\[
G(1/2)=1/4+1/4=1/2.
\]

Thus

\[
\boxed{J_F(0)=J_G(0)\not\Rightarrow F=G\text{ near or away from }0}.
\]

A Jacobian diagnostic must always carry its reference state.

## D7. Hessian spectrum does not determine stationarity
Define

\[
f(x,y)=x^2+y^2,
\]

\[
g(x,y)=x^2+y^2+x.
\]

Both Hessians are

\[
H_f=H_g=2I.
\]

At the origin, both Hessian spectra are

\[
\{2,2\}.
\]

But

\[
\nabla f(0,0)=(0,0),
\]

while

\[
\nabla g(0,0)=(1,0).
\]

Hence identical Hessian spectra do not determine whether the reference point is stationary.

## D8. Koopman finite-state example
Let the state set be {0,1} and define deterministic map

\[
T(0)=1,\qquad T(1)=0.
\]

For an observable h, define Koopman action

\[
(Uh)(x)=h(T(x)).
\]

On indicator basis

\[
\delta_0,\delta_1,
\]

we have

\[
U\delta_0=\delta_1,
\qquad
U\delta_1=\delta_0.
\]

Therefore the finite Koopman matrix is

\[
U=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Its characteristic polynomial is

\[
\lambda^2-1,
\]

so

\[
\boxed{\sigma(U)=\{1,-1\}}.
\]

This spectrum belongs to the observable-space operator U. It is not a Jacobian spectrum by definition.

## D9. Transition-local signatures
For a nonlinear transition map Phi and reference state z_t, a local diagnostic may use

\[
J_t=D\Phi(z_t).
\]

A sequence

\[
\sigma(J_t)
\]

is therefore a state/time-indexed diagnostic. Comparing J_t and J_{t+1} without recording z_t,z_{t+1}, the estimation method, and the measurement window discards part of the object being measured.

## D10. Mechanistic significance requires a functional bridge
Let s(A) be any spectral signature and y(A) a functional output under a declared interface. D4 constructs A and B with identical eigenvalue and singular-value multisets but different y(A)=||Ae1|| and y(B)=||Be1||.

Therefore equality of those spectral signatures does not identify functional equivalence.

Conversely, a correlation between s(A) and y(A) over a dataset is still observational evidence. To claim functional necessity or mechanism, one needs a separately typed intervention such as ablation, substitution, controlled perturbation, recovery, or another justified functional test.

## D11. Empirical limits
For empirical or learned spectral diagnostics, report at least:
- finite precision;
- conditioning/non-normality;
- finite sample or time window;
- truncation/rank choice;
- operator-estimation procedure;
- uncertainty or replay tolerance.

A numerical eigendecomposition is not automatically an exact property of an underlying infinite-dimensional or nonlinear system.
