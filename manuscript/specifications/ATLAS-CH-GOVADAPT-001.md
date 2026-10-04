# Chapter Specification — ATLAS-CH-GOVADAPT-001

## Identity

**Title:** Governed Adaptation  
**Part:** Scientific Method and Governed Adaptation  
**Status:** specification-ready.  
**Epistemic class:** audited Optionality/Research-State-Machine prerequisites + bounded intervention literature + Atlas synthesis.

## Chapter contract

Ask how an adaptive system may change its operative state while preserving correction capacity, exact provenance, bounded authority, explicit recovery paths, evidence identity, and separation between execution, promotion, and certification.

## Hard prerequisites

- ATLAS-CH-OPTIONALITY-001;
- ATLAS-CH-RESEARCHSM-001.

May inherit from OPTIONALITY:

- viable continuation sets;
- conditional correction cost;
- conditional correction indicator;
- ex-ante correction capacity;
- horizon-relative recoverability.

May inherit from RESEARCHSM:

- bounded work packages;
- typed canonical state;
- canonical/history separation;
- exact-identity idempotence;
- guarded advancement;
- separate certification;
- actor-separation predicates;
- fail-closed safety versus liveness;
- typed recovery;
- exact-target evidence.

## Governed state

Let the protected adaptive state be

\[
g=(r,x,E,A,P,C,L),
\]

where \(r\) is exact revision identity, \(x\) operative state, \(E\) canonical evidence, \(A\) authority relation, \(P\) promotion state, \(C\) certification state, and \(L\) append-only transition history.

A candidate revision is

\[
q=(id,r_{parent},\Delta,\hat r).
\]

## Authority separation

Define separate predicates for proposal, execution, promotion, recovery, and certification authority.

No implication among these predicates is automatic.

## Exact-target evidence

For evidence object \(e=(id,target,claim,payload,provenance)\), define

\[
Binds(e,r)\iff target(e)=r.
\]

Evidence for one exact revision is not silently reusable for a materially different revision.

## Governed execution gate

Let \(Inv(x)\) be the declared invariant and \(Sep(q)\) any required actor-separation predicate.

Let the correction-capacity floor be \(\kappa\in[0,1]\).

Define

\[
Adm(g,q)
=
ParentOK
\land EvidenceOK
\land AuthorityOK
\land Sep
\land Inv
\land
\bigl(CC_{h,\epsilon}(x_q;b)\ge\kappa\bigr).
\]

This is an Atlas governance construction, not a universal theorem.

## Execution, promotion, certification

Execution creates a candidate state.

Promotion is a separate transition.

Certification, when present, is another separate transition.

## Governed recovery

A stored rollback artifact is not yet recoverability.

For target revision/consequence class \(r_\star\), governed recovery requires an authorized path of bounded length to the declared target.

## Finite witness

Let hidden future condition be

\[
\Theta=\{N,D\},
\qquad
b(N)=b(D)=1/2.
\]

Two candidates \(A\) and \(B\) produce post-revision operative states \(x_A\) and \(x_B\) from the same protected baseline \(x_0\).

Their immediate utility increments are explicitly baseline-relative:

\[
U(x_A)-U(x_0)
=
U(x_B)-U(x_0)
=
1.
\]

Candidate A preserves an authorized recovery path if a defect is later discovered.

Candidate B does not.

Thus:

\[
CC_{h,0}(x_A;b)=1,
\qquad
CC_{h,0}(x_B;b)=1/2.
\]

A utility-only threshold ties them.

A declared gate requiring \(CC_{h,0}\ge1\) admits A and rejects B.

The witness proves only this finite separation.

## Intervention literature

Use:

- Soares et al. (2015) for corrective-intervention/corrigibility desiderata;
- Orseau and Armstrong (2016) for safe interruptibility in their RL setting;
- Hadfield-Menell et al. (2017) for off-switch incentives under objective uncertainty.

Do not collapse these concepts into Atlas correction capacity.

## Safety versus liveness

A fail-closed gate can preserve an invariant while refusing every candidate.

Therefore safety does not imply eventual adaptation.

## Failure boundaries

Include:

- executable is not authorized;
- authorized is not beneficial;
- beneficial is not certified;
- rollback artifact is not recoverability;
- raw option count is not correction capacity;
- stale evidence is not exact-target evidence;
- intervention-channel preservation is not complete alignment;
- fail-closed safety is not liveness;
- process conformance is not substantive truth;
- authority over operative state does not automatically include authority over the governing policy.

## Downstream handoff

Direct consumer:

- ATLAS-CH-FRONTIER-001.

## Sources

- [@SoaresEtAl2015Corrigibility]
- [@OrseauArmstrong2016]
- [@HadfieldMenellEtAl2017OffSwitch]

Source lock:

sources/source-locks/ATLAS-CH-GOVADAPT-001.yaml

## Acceptance

The draft must define a governed state and candidate revision, separate authority roles, bind evidence to exact target identity, distinguish rollback artifacts from recovery, incorporate correction-capacity semantics, derive the equal-utility witness, preserve the safety/liveness boundary, and include the full governed artifact/audit lifecycle.
