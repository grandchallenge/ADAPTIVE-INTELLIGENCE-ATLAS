# GOVADAPT-001 — Governed Adaptation

## Identity

- chapter: ATLAS-CH-GOVADAPT-001
- issue: #149
- baseline: ae2ce726fa4f24fc52289a1f2e6bbbaff9232d11
- branch: work/atlas-149
- hard prerequisites:
  - ATLAS-CH-OPTIONALITY-001
  - ATLAS-CH-RESEARCHSM-001

Exact prerequisite binds:

- OPTIONALITY manuscript: a202d82ad9f2242fd17117cf6faa6eaa30227369
- AUDIT-034: 43abd668155904debaf7687a05e93a0ea7d60fa5
- OPTIONALITY source lock: 631afbcc9bfa1a2382ef109d701d523cafbbf0d1
- RESEARCHSM manuscript: fca394ca7fe69561730ea5b13076974f22fe73e9
- AUDIT-035: 8251b54ffb5644a41d7404d0e33e717f384d5c12
- RESEARCHSM source lock: c507c236fb8993b1e5e4df400c92ce490ff42dde

## External source set

- Soares et al. (2015), Corrigibility;
- Orseau and Armstrong (2016), Safely Interruptible Agents;
- Hadfield-Menell et al. (2017), The Off-Switch Game.

External claims are restricted to the intervention/corrigibility results documented by those sources.

## Core objects

- protected state g=(r,x,E,A,P,C,L);
- candidate revision q=(id,r_parent,Delta,r_hat);
- separate proposal/execution/promotion/recovery/certification authority;
- exact-target evidence predicate;
- authorized recovery-path predicate;
- correction-capacity floor;
- fail-closed safety versus liveness.

## Exact witness

Hidden future condition:

[
Theta={N,D},
qquad
b(N)=b(D)=1/2.
]

Equal immediate utility:

[
Delta U(A)=Delta U(B)=1.
]

Correction capacities:

[
CC_{h,0}(x_A;b)=1,
qquad
CC_{h,0}(x_B;b)=1/2.
]

An immediate-utility threshold admits both.

A declared correction-aware gate with (kappa=1) admits A and rejects B.

## Durable distinctions

- capability versus authority;
- execution versus promotion;
- promotion versus certification;
- stored rollback artifact versus governed recoverability;
- action labels versus functional correction paths;
- evidence history versus exact-target validation;
- safety versus liveness;
- process conformance versus substantive truth;
- operative-state authority versus governance-policy-change authority;
- intervention-channel preservation versus complete corrigibility.

## Artifact set

- sources/source-locks/ATLAS-CH-GOVADAPT-001.yaml
- sources/bibliography.bib
- manuscript/specifications/ATLAS-CH-GOVADAPT-001.md
- mathematics/derivations/ATLAS-CH-GOVADAPT-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-GOVADAPT-001.md
- manuscript/parts/14-scientific-method-governed-adaptation/ATLAS-CH-GOVADAPT-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- this tranche receipt

## Remaining gates

Repository validation, implementation PR, exact-head green CI, protected merge, bounded post-draft audit, in-scope repairs, audit validation/merge, issue closure, frontier recomputation, and controller reset.
