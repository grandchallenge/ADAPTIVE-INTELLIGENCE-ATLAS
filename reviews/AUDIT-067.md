# AUDIT-067 — Spectral and Operator Diagnostics

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-SPECTRALDIAG-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #267
- implementation PR: #268
- exact validated implementation head: 8d4dd2a78ae5f3b6f49984562ec27f8d8da779c7
- implementation GitHub Actions run: 37556698565
- implementation merge / audited protected baseline: d7ac9862600874baf24128186ef23aa5e2cbb6af
- audit issue: #270
- audit branch: audit/a270
- chapter: ATLAS-CH-SPECTRALDIAG-001

Protected implementation artifact identities:

- specification: 14263bc6909db5189b0324b2f2e5aa28d29411bc
- derivation packet: f65e3bdef065a71b72db189539392175ed840728
- computational witness: c86ee1cf38368f9f92cfa718dbc1c3527d1e077a
- reader manuscript: fa985357911a2024a4070175c0b6a5f414740994
- source lock: 461ec864d22c14040444c0760d9aea7b05997125
- bibliography: acecefea7c71b895f204cd4458d7ee4aa5bd326c
- Chapter Ledger: a8f29d878863f8b14ddf5f57259829b1aea1c16c
- Source Register: 6b91b10e46bf4a90a77ba93807120c09b817c60b
- transaction receipt: 488800440c4c49758da57643ff3725024a6ac42e

A controller checkpoint lag occurred after the implementation merge: PR #268 had already merged the exact validated implementation head while ACTIVE_TRANSACTION.yaml still recorded the pre-merge CI-green state. Protected main and the PR history showed that the merge itself was exact. The controller was repaired before the audit was instantiated.

## 1. NONNORMAL prerequisite

PASS.

Exact identities:

- manuscript a8b4cde747df1a986eeca1439203b08512a1471c;
- source lock f8c868af0fc35b73d9acadbdf6d952b03c1d89e9;
- AUDIT-001 f13b7ac01f7b10dfadd64da6f31c45832344c082.

The chapter inherits the correct boundary: eigenvalues need not determine finite-horizon amplification for non-normal operators, and pseudospectral/resolvent diagnostics remain descriptive operator diagnostics rather than neural-mechanism explanations.

## 2. MECHDIAG prerequisite packet

PASS.

Exact identities:

- ledger-selected manuscript 4682d5b4abc77c40aa27fd5144d6909250add86f;
- source lock 94362bbe21c5f7f29123e461cc749e617bc117c7;
- AUDIT-047 960e75262c69c0fdb24cc3d33813b250879f25eb;
- mature reader companion 8275d106f3960eb21e385b3d9130b3cb7686fec0;
- audit source-scope packet fe3a99a8a162dc2d364ff2db2674d737a1fdeb20.

The implementation correctly inherits readability-versus-function, intervention typing, redundancy cautions, and the requirement for functional evidence before mechanistic promotion.

## 3. New source scope

PASS.

The chapter adds exactly one new external academic authority:

- Igor Mezić (2005), *Spectral Properties of Dynamical Systems, Model Reduction and Decompositions*, Nonlinear Dynamics 41:309–325, DOI 10.1007/s11071-005-2824-x.

Its authority is used only for the Koopman observable-operator spectral viewpoint.

No pseudospectral, mechanistic-diagnostic, Jacobian, Hessian, or neural-causal theorem is attributed to this source.

## 4. Object identity discipline

PASS.

Every spectral quantity is attached to a declared object:

- matrix/operator eigenvalues;
- singular values;
- resolvent/pseudospectrum;
- Jacobian at a declared state;
- Hessian at a declared point;
- finite Koopman operator on a declared observable space.

The chapter does not treat “the spectrum” as a single untyped object.

## 5. Equal eigenvalues / unequal response control

PASS.

For:

D = diag(1/2,1/2)

and

N = [[1/2,2],[0,1/2]],

both eigenvalue multisets are {1/2,1/2}.

For e2=(0,1):

- ||D e2||_2^2 = 1/4;
- ||N e2||_2^2 = 17/4.

Thus equal eigenvalues do not determine finite-step response.

Independent audit replay agrees.

## 6. Equal eigenvalue and singular-value multisets / unequal interface response

PASS.

For:

A = diag(2,1/2)

and

B = diag(1/2,2),

both eigenvalue multisets and singular-value multisets are {2,1/2}.

For fixed interface vector e1=(1,0):

- ||A e1||_2 = 2;
- ||B e1||_2 = 1/2.

The interface-response difference is therefore 3/2 despite zero drift in those global multisets.

The chapter correctly concludes that global spectral summaries do not determine fixed-interface behavior.

## 7. Local Jacobian / nonlinear-map control

PASS.

For:

F(x)=x/2

and

G(x)=x/2+x^2,

the local derivatives at zero satisfy:

F'(0)=G'(0)=1/2.

But at x=1/2:

- F(1/2)=1/4;
- G(1/2)=1/2.

Thus identical local Jacobian spectra at one reference point do not determine the global nonlinear map.

## 8. Hessian spectrum / stationarity control

PASS.

For:

f(x,y)=x^2+y^2

and

g(x,y)=x^2+y^2+x,

both Hessians are 2I and therefore have spectrum {2,2}.

At (0,0):

- grad f=(0,0);
- grad g=(1,0).

Hence Hessian spectrum does not determine gradient or stationarity.

## 9. Finite Koopman witness

PASS.

For the two-state swap T(0)=1, T(1)=0, the indicator-observable Koopman matrix is:

U=[[0,1],[1,0]].

Exactly:

- U^2=I;
- trace(U)=0;
- det(U)=-1;
- eigenvalues are {1,-1}.

The chapter correctly types this as a finite observable-space representation and does not claim a finite empirical Koopman matrix automatically equals an infinite-dimensional Koopman operator.

## 10. Pseudospectral boundary

PASS.

The chapter inherits pseudospectral/resolvent authority from NONNORMAL-001 and does not collapse pseudospectral sensitivity into eigenvalue drift, singular-value drift, or mechanistic evidence.

## 11. Local/global boundary

PASS.

Jacobian and Hessian spectra are explicitly reference-point dependent.

Transition-local signatures are kept distinct from global operator summaries.

No local spectrum is silently promoted to a global dynamical theorem.

## 12. Descriptive versus predictive versus functional versus causal claims

PASS.

The manuscript separates:

- descriptive diagnostic quality;
- predictive utility;
- functional necessity;
- causal/mechanistic significance.

Spectral correlation alone is not treated as intervention evidence.

## 13. Functional-evidence gate

PASS.

Any mechanistic interpretation of a spectral signature is required to be paired with an intervention, ablation, substitution, recovery test, or equivalently typed functional experiment.

This matches the MECHDIAG evidence boundary.

## 14. Estimation and numerical limits

PASS.

The chapter records that empirical spectra are affected by:

- sampling;
- finite observation windows;
- truncation;
- operator estimation error;
- conditioning;
- finite precision.

No empirical spectral estimate is presented as exact merely because the underlying mathematical object has an exact spectrum.

## 15. Transaction-receipt provenance

PASS.

Every implementation artifact identity recorded in governance/tranches/SPECTRALDIAG-001.md matches the exact protected implementation merge d7ac9862600874baf24128186ef23aa5e2cbb6af.

The protected receipt is blob 488800440c4c49758da57643ff3725024a6ac42e.

## 16. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- SPECTRALDIAG status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- hard dependencies remain NONNORMAL-001 and MECHDIAG-001;
- the mature MECHDIAG documentary packet is bound;
- the SPECTRALDIAG source lock is registered;
- Mezić 2005 resolves through the bibliography;
- no governed figure is introduced;
- exact implementation head passed GitHub Actions run 37556698565;
- protected implementation merge passed canonical repository validation;
- independent audit replay returned SPECTRALDIAG_AUDIT_WITNESS_OK.

## Final disposition

AUDIT-067 passes with no repair.

The durable SPECTRALDIAG rule is:

**spectral and operator diagnostics are typed measurements of explicitly declared objects. Equal eigenvalue or singular-value summaries need not imply equal dynamics or interface behavior, local spectra do not determine global nonlinear behavior, and spectral correlation does not become mechanistic evidence without a separately typed functional test.**
