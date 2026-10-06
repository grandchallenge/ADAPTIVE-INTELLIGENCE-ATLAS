# AUDIT-063 — Minimal Curricula and Reasoning Bases

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-MINCURR-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, bibliography, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #251
- implementation PR: #252
- exact validated implementation head: 1a1974edd3b077c6ef37503b6c6f21237f8e952c
- implementation GitHub Actions run: 37544743541
- implementation merge / audited protected baseline: f4ef49601bf2c306918f75a2e0abfc242379935e
- audit issue: #253
- audit branch: audit/a253
- chapter: ATLAS-CH-MINCURR-001

Protected implementation artifact identities:

- specification: a90bf935ef124bc9a748123d2ba67474049a5314
- derivation packet: b49724dba87f9cf58a59ac611b781665b57dbc95
- computational witness: 8d7142ed8f457a7a8647904b6e4c8e04e4b20ed7
- reader manuscript: 01a5491100430fe8bf56793e6e1b557ba91dc652
- source lock: e7cb725448a35b31fa879528dc01b02a72d052ca
- bibliography: c95dbd1d1e3ddd0e3b99e067ce3dd654bf8201da
- Chapter Ledger: a8d40ef1f4144def1c6e5cbd363d9837186b50f0
- Source Register: 2b4ba80c4d8ccbf68804ab54b99b926204a387d5
- transaction receipt: 90a8635137ed5fd761387c93faa780fbf95b4459

The implementation required one non-mathematical repair before validation: the reader manuscript reference heading was changed to the repository-required protocol marker. The receipt was refreshed to the repaired manuscript blob before PR creation.

## 1. Hard prerequisites

PASS.

PROGRESSSEARCH-001 is bound exactly:
- manuscript 30e988200933dbba8ad53f069acacf131b0944ee
- source lock 6e593b0d17e4a80d5790a6ea6d580f3b4530686a
- AUDIT-049 647a8b0ca273ff8c8bebaaa97073a9b198e8bee4

RESIDUAL-001 is bound exactly:
- manuscript 02b0886a87e1e17c749e15349e14f43674c3d1ff
- source lock 6e6a25c4b4e01475e68a6c616eefb6ba7b039341
- AUDIT-006 b24ef782bedfe76a4c52d832562a0dd29d2a64a9

The chapter preserves the inherited boundary that search utility does not establish reconstructive minimality and that leastness is relative to declared capability, example/descriptor, and reconstruction classes.

## 2. New source scope

PASS.

The source lock adds only:
- Goldman and Kearns (1995), DOI 10.1006/jcss.1995.1003
- Zhu (2015), DOI 10.1609/aaai.v29i1.9761

Their use is narrow: classical target-identifying teaching-set / teaching-dimension framing, and machine teaching as training-set design relative to a specified learner and target. Neither source is used as authority for neural mechanism persistence, universal curriculum minimality, or a universal reasoning basis.

## 3. Bibliography integrity

PASS.

The bibliography contains the two new keys GoldmanKearns1995Teaching and Zhu2015MachineTeaching, and the manuscript/source lock use them consistently.

## 4. Exact concept-class witness

PASS.

The declared probe set is Q={q1,q2}. The concept class is H={h00,h01,h10,h11}, with target h*=h11. The teaching examples are e1=(q1,1) and e2=(q2,1).

The version-space definition is explicit and the exact reconstructor succeeds only when the version space is singleton.

## 5. Sufficiency of the two-example basis

PASS.

For T*={e1,e2}, the version space is exactly {h11}. Thus the target is uniquely reconstructed.

Independent audit replay agrees.

## 6. Strict-smaller failure

PASS.

The strict subsets are empty, {e1}, and {e2}. Their version spaces are respectively H, {h10,h11}, and {h01,h11}. Every strict smaller candidate therefore has cardinality greater than one.

Hence the minimum teaching-set size is exactly 2.

## 7. Relative minimality boundary

PASS.

The chapter explicitly scopes the result to the declared concept/capability class, target, example language, learner/reconstructor, and side information. It does not promote the finite witness to a universal minimal curriculum.

## 8. High-progress/non-basis control

PASS.

The auxiliary experience e3=(z,1), with z outside Q, has frozen progress score 5 while e1 and e2 each have score 1. Because e3 lies outside the target probe family, V_H({e3})=H.

Thus the highest-progress experience leaves target ambiguity unchanged and is not in T*.

Independent replay agrees.

## 9. Search versus reconstructive value

PASS.

The chapter correctly distinguishes current learning-progress/search value from target-identification/reconstructive necessity. It does not conclude that high progress is unimportant; it concludes only that progress ranking and minimal-basis membership are different objectives.

## 10. Set versus sequence

PASS.

Under the declared order-insensitive reconstructor, both orderings of e1 and e2 yield the same final teaching set. The manuscript correctly rejects the implication from minimal set to unique optimal sequence.

## 11. Capability versus model identity

PASS.

The chapter allows a weaker capability-relative reconstruction criterion and explicitly links it to the audited Residual discipline. It does not silently require full internal-state reconstruction when the target is capability equivalence.

## 12. Acquisition/persistence/accessibility/expression ladder

PASS.

The chapter separates acquisition evidence, persistence evidence, accessibility evidence, and behavioural expression.

It explicitly blocks promotion from acquisition to persistence, persistence to accessibility, accessibility to expression in every context, and later expression to persistence or causality of a particular early mechanism.

No empirical mechanism-persistence claim is made.

## 13. Mechanism identity boundary

PASS.

The manuscript requires a declared identity criterion for longitudinal persistence claims, such as matched functional signature, causal intervention effect, aligned mechanistic subspace, or declared reconstruction relation. Aggregate behavioral similarity alone is not accepted as mechanism identity.

## 14. Transaction-receipt provenance

PASS.

Every implementation artifact identity in governance/tranches/MINCURR-001.md matches the exact protected implementation merge. The repaired manuscript identity is correctly reflected in the receipt.

## 15. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:
- MINCURR status is draft-v0.1
- canonical specification/manuscript/derivation/source-lock/witness paths are populated
- hard dependencies remain PROGRESSSEARCH-001 and RESIDUAL-001
- the MINCURR source lock is registered
- both new bibliography keys resolve
- no governed figure is introduced
- exact implementation head passed GitHub Actions run 37544743541
- protected implementation merge passed canonical repository validation
- independent audit replay returned MINCURR_AUDIT_WITNESS_OK

## Final disposition

AUDIT-063 passes with no repair.

The durable MINCURR rule is:

**search value, reconstructive necessity, mechanism persistence, mechanism accessibility, and behavioural expression are distinct objects. A basis is minimal only relative to a declared capability and reconstruction contract, and later behavior cannot by itself certify which early mechanism survived or caused it.**
