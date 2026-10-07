# SPECTRALDIAG-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-SPECTRALDIAG-001
- implementation issue: #267
- protected baseline: 7d2da2ceb970bbba7c43a387ce2ce74f8035e8cf
- branch: work/spectraldiag-267

## Hard prerequisites

NONNORMAL-001:
- manuscript a8b4cde747df1a986eeca1439203b08512a1471c
- source lock f8c868af0fc35b73d9acadbdf6d952b03c1d89e9
- AUDIT-001 f13b7ac01f7b10dfadd64da6f31c45832344c082

MECHDIAG-001:
- ledger manuscript 4682d5b4abc77c40aa27fd5144d6909250add86f
- source lock 94362bbe21c5f7f29123e461cc749e617bc117c7
- AUDIT-047 960e75262c69c0fdb24cc3d33813b250879f25eb
- mature reader companion 8275d106f3960eb21e385b3d9130b3cb7686fec0
- audit source-scope packet fe3a99a8a162dc2d364ff2db2674d737a1fdeb20

## New primary source
- Igor Mezić (2005), *Spectral Properties of Dynamical Systems, Model Reduction and Decompositions*, Nonlinear Dynamics 41:309--325, DOI 10.1007/s11071-005-2824-x.
- authority is limited to the Koopman observable-operator spectral viewpoint.

## Implementation artifacts at validated pre-receipt head c535f7c78cdde871dc264e1aa4116118ef30bcc0
- specification 14263bc6909db5189b0324b2f2e5aa28d29411bc
- derivation packet f65e3bdef065a71b72db189539392175ed840728
- computational witness c86ee1cf38368f9f92cfa718dbc1c3527d1e077a
- reader manuscript fa985357911a2024a4070175c0b6a5f414740994
- source lock 461ec864d22c14040444c0760d9aea7b05997125
- Chapter Ledger a8f29d878863f8b14ddf5f57259829b1aea1c16c
- Source Register 6b91b10e46bf4a90a77ba93807120c09b817c60b
- bibliography acecefea7c71b895f204cd4458d7ee4aa5bd326c

## Exact finite controls

### Equal eigenvalues / unequal response
D=diag(1/2,1/2), N=[[1/2,2],[0,1/2]].
Both eigenvalue multisets are {1/2,1/2}.
For e2=(0,1):
- ||D e2||_2^2 = 1/4;
- ||N e2||_2^2 = 17/4.

### Equal eigenvalue and singular-value multisets / unequal interface response
A=diag(2,1/2), B=diag(1/2,2).
Both eigenvalue and singular-value multisets are {2,1/2}.
For e1=(1,0):
- ||A e1||_2 = 2;
- ||B e1||_2 = 1/2;
- fixed-interface norm change = 3/2 despite zero multiset drift.

### Same local Jacobian / different nonlinear map
F(x)=x/2 and G(x)=x/2+x^2.
- F'(0)=G'(0)=1/2;
- F(1/2)=1/4;
- G(1/2)=1/2.

### Same Hessian spectrum / different stationarity
f(x,y)=x^2+y^2 and g(x,y)=x^2+y^2+x.
Both Hessians are 2I with spectrum {2,2}, but
- grad f(0,0)=(0,0);
- grad g(0,0)=(1,0).

### Finite Koopman witness
For the two-state swap T(0)=1, T(1)=0, the indicator-observable Koopman matrix is [[0,1],[1,0]].
- U^2=I;
- trace(U)=0;
- det(U)=-1;
- eigenvalues {1,-1}.

## Durable boundaries
- every spectrum is attached to an explicitly named operator/object and reference state/time when local;
- eigenvalues, singular values, pseudospectra/resolvent diagnostics, Jacobian spectra, Hessian spectra, and Koopman spectra are distinct objects;
- equal global spectral summaries do not determine relative-position/interface behavior;
- local Jacobian spectra do not determine global nonlinear maps;
- Hessian spectra do not determine gradients or stationarity;
- empirical Koopman matrices are finite approximations whose relation to an underlying operator needs separate approximation theory;
- spectral correlation/predictive utility is not functional necessity;
- mechanistic significance requires intervention, ablation, substitution, recovery, or an equivalently typed functional test;
- empirical spectral estimates remain subject to sampling, truncation, conditioning, finite precision, and operator-estimation error.

## Validation gate
The pre-receipt implementation head c535f7c78cdde871dc264e1aa4116118ef30bcc0 passed canonical repository validation and independent exact witness replay. The final receipt-bearing head must be revalidated before PR creation. Merge additionally requires exact-head GitHub Actions success and a fresh post-draft audit.
