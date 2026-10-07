# ATLAS-CH-SPECTRALDIAG-001 — Chapter Specification

## Title
Spectral and Operator Diagnostics

## Contract
Develop singular spectra, Jacobian/Hessian spectra, pseudospectra, Koopman views, relative-position diagnostics, spectral drift, and transition-local signatures without assuming a universal scalar diagnostic.

## Hard prerequisites
- ATLAS-CH-NONNORMAL-001
- ATLAS-CH-MECHDIAG-001, including the mature reader companion and AUDIT-047 source-scope packet

## Required objects
Every diagnostic must name the object to which it applies:
- matrix/operator A;
- Jacobian J_F(z0);
- Hessian H_L(theta0);
- empirical transition matrix/operator;
- Koopman operator U acting on a declared observable space;
- a finite estimated/truncated surrogate, when that is all that exists.

## Mandatory distinctions
1. eigenvalue spectrum versus singular-value spectrum;
2. spectrum versus pseudospectrum/resolvent growth;
3. global linear operator versus local Jacobian;
4. Hessian spectrum versus gradient/stationarity;
5. operator-intrinsic summaries versus relative-position/interface diagnostics;
6. global summary versus transition-local signature;
7. descriptive correlation versus predictive utility;
8. predictive utility versus functional necessity;
9. functional necessity versus causal mechanism.

## Exact witnesses
### W1 — equal eigenvalues, unequal finite response
Compare D=(1/2)I with N=[[1/2,2],[0,1/2]]. Both have eigenvalues {1/2,1/2}, but for e2=(0,1), ||D e2||_2=1/2 while ||N e2||_2=sqrt(17)/2>1.

### W2 — equal eigenvalues and singular values, unequal interface response
Compare A=diag(2,1/2) and B=diag(1/2,2). They have the same eigenvalue multiset and singular-value multiset {2,1/2}. With fixed interface vector e1, ||A e1||=2 while ||B e1||=1/2.

### W3 — same local Jacobian spectrum, different nonlinear map
F(x)=x/2 and G(x)=x/2+x^2 have the same Jacobian value 1/2 at x0=0, but F(1/2)=1/4 while G(1/2)=1/2.

### W4 — same Hessian spectrum, different stationarity
f(x,y)=x^2+y^2 and g(x,y)=x^2+y^2+x have Hessian 2I at the origin, but grad f(0,0)=0 and grad g(0,0)=(1,0).

### W5 — finite Koopman example
For the two-state deterministic swap T(0)=1, T(1)=0 and indicator-observable basis (1_{0},1_{1}), the Koopman matrix is [[0,1],[1,0]] with eigenvalues {1,-1}. This is an operator on observables, not the scalar derivative/Jacobian of a Euclidean state map.

## Mechanistic firewall
A spectral signature may be descriptive or predictive. Mechanistic significance requires a separately typed functional test such as intervention, ablation, substitution, recovery, or another justified causal/functional experiment.

## Empirical limitations
State finite precision, conditioning, sampling, truncation, finite-window effects, and operator-estimation error for empirical spectra or learned Koopman approximations.

## Acceptance criteria
- all hard prerequisite blobs exact;
- source lock complete and minimal;
- exact witnesses replay independently;
- reader manuscript includes protocol reference section and claim boundaries;
- Chapter Ledger promoted to draft-v0.1;
- Source Register and bibliography resolve;
- canonical repository validation green;
- exact-head GitHub Actions green;
- post-draft audit merged before controller reset.
