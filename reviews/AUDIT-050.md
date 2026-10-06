# AUDIT-050 — Router Dynamics and Diagnostics

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-ROUTERDYN-001 remains at \`draft-v0.1\`.

No mathematical, witness, source-scope, provenance, reader-maturity, specialization, spectral, commutator, or downstream-boundary defect requiring repair was found.

This audit does not promote the chapter to publication-ready, certified, or final-copy status.

## Audited implementation

- implementation issue: #199
- implementation PR: #200
- exact green implementation head: \`3c3f22044102f10386e5d3bc850ac2bc32b6c709\`
- implementation merge: \`70cf75f3f4a67dec75267766934ce5f96c7fac49\`
- audit issue: #201
- audit branch: \`audit/routerdyn-201\`
- chapter: \`ATLAS-CH-ROUTERDYN-001\`

Implementation artifact identities:

- specification: \`0202b1acc7afb398de1b4cb5da5eaae90e660d3d\`
- manuscript: \`4c3c4b22d7f6a564b255a251ba646d11dbbc29a4\`
- derivation: \`abe764147698626022f4222df02e762f2b0394e9\`
- witness: \`a105d8b12b73514dd846faad82e965e1d4b5a2c8\`
- source lock: \`27aca5556b902c679132780e4f74ba8822420762\`
- Chapter Ledger: \`109a98c2a697b97596314bc12503755b51d5374c\`
- Source Register: \`fd449da001f1fdbbb36f6045d2b833030c11189d\`
- bibliography: \`5a11a24448d81242265333ac724d97b451442013\`

## 1. Hard prerequisites

PASS.

Mixture-of-Experts exact binds:

- manuscript: \`5281e3bc0721681c630c56057cf478311e96662d\`
- source lock: \`75d5b04a90794b7543c70414ec9e2be59c9af7ed\`
- AUDIT-033: \`261e63f7853c359460bd76302ddfaeed576892cb\`

Optimizer-State Dynamics exact binds:

- manuscript: \`59b03c10b7f4b917cc8a0cb4d6893e12c1993c8c\`
- source lock: \`0b0cb1dd109a7708bd2a5238116bd225c69fb185\`
- AUDIT-002: \`4671995f0cd7465a5df2bb60431244f482e5e3c9\`

## 2. External source scope

PASS.

The source lock uses ST-MoE only for its reported sparse-model stability/router-logit work and source-specific specialization observations.

Expert Choice is used only for routing-rule dependence of utilization and specialization concerns.

Neither source is promoted to a universal theory of router dynamics.

## 3. Typed temporal observables

PASS.

The chapter keeps separate:

- router probability drift;
- preferred-route churn;
- accepted-dispatch churn;
- accepted-load drift.

The maps from probability to preference to accepted dispatch to load are not treated as invertible.

## 4. Load-versus-churn witness

PASS.

Independent replay gives:

- load before: \((2,2)\);
- load after: \((2,2)\);
- load drift: \(0\);
- route churn: \(1\).

Therefore stable load does not imply stable token routing.

## 5. Transition-operator spectral boundary

PASS.

The stable transition matrix and total-swap transition matrix both have singular values \((1,1)\), while their token-level dynamics differ maximally.

The chapter therefore correctly blocks the inference that equal singular spectra imply equal routing dynamics.

The empirical one-step transition operator is not silently promoted to a stationary Markov model.

## 6. Probability-drift witness

PASS.

Independent replay gives:

- preferred routes unchanged;
- preferred-route churn: \(0\);
- average probability drift: \(0.3\).

Thus zero route churn does not imply static router probabilities.

## 7. Specialization boundary

PASS.

Specialization is defined relative to a declared token/task category system and accepted dispatch.

Balanced or concentrated load is not equated with semantic specialization.

A specialization score is not promoted to causal importance.

## 8. Augmented-state and commutator boundary

PASS.

The chapter keeps router-plus-optimizer memory inside the declared dynamical state and uses local Jacobians only as local objects.

Independent replay gives the commutator

\[
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

with Frobenius norm \(\sqrt2\).

Both one-step maps have eigenvalues \((1,1)\), so their individual eigenvalue multisets do not encode the displayed order sensitivity.

A nonzero commutator is not claimed to identify a causal mechanism.

## 9. Spectral diagnostics

PASS.

The manuscript keeps operator identity attached to every spectral statistic.

Expert-transition spectra, local router-state Jacobian spectra, and finite-horizon Jacobian-product gains are not collapsed into one generic "router spectrum."

No universal scalar router-health score is claimed.

## 10. Churn interpretation

PASS.

The chapter explicitly states that high churn need not be harmful and low churn need not be beneficial.

Capacity/overflow semantics, changing data, interchangeable experts, and router-margin changes remain alternative explanations.

## 11. Bibliography and provenance

PASS.

The declared keys resolve:

- \`ZophEtAl2022STMoE\`;
- \`ZhouEtAl2022ExpertChoice\`.

The Source Register contains \`ATLAS-SRC-ROUTERDYN-LOCK-001\`.

The Chapter Ledger binds specification, reader, derivation, source lock, and witness paths.

## 12. Reader maturity

PASS.

The reader contains:

- the opening diagnostic obstruction;
- four temporal observable classes;
- exact finite witnesses;
- empirical transition operators;
- taxonomy-relative specialization;
- augmented-state dynamics;
- commutator and spectral diagnostics;
- interpretation/failure boundaries;
- a direct REGRETROUTE handoff;
- epistemic status, references, and source-lock pointer.

## 13. REGRETROUTE handoff

PASS.

ATLAS-CH-REGRETROUTE-001 may inherit the temporal diagnostics and exact counterexamples.

ROUTERDYN does not pre-claim regret, online comparison classes, optionality, correction capacity, or reward timing.

## Final audit boundary

The durable separations are:

- stable load != stable routing;
- zero route churn != zero probability drift;
- equal singular spectra != equal routing dynamics;
- nonzero commutator != identified causal mechanism.

No repair is required.

The next legitimate operation is exact-head canonical validation of this audit record, audit merge, final main validation, frontier recomputation, issue closure, and controller/handoff reset.
