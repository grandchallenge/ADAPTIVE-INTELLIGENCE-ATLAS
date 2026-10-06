# MINCURR-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-MINCURR-001
- implementation issue: #251
- protected baseline: 3981c7de350e2eb284eb0f3753c09321c173d436
- branch: work/mincurr-251

## Hard prerequisites

PROGRESSSEARCH-001:
- manuscript 30e988200933dbba8ad53f069acacf131b0944ee
- source lock 6e593b0d17e4a80d5790a6ea6d580f3b4530686a
- AUDIT-049 647a8b0ca273ff8c8bebaaa97073a9b198e8bee4

RESIDUAL-001:
- manuscript 02b0886a87e1e17c749e15349e14f43674c3d1ff
- source lock 6e6a25c4b4e01475e68a6c616eefb6ba7b039341
- AUDIT-006 b24ef782bedfe76a4c52d832562a0dd29d2a64a9

## New primary sources
- Goldman & Kearns 1995, DOI 10.1006/jcss.1995.1003
- Zhu 2015, DOI 10.1609/aaai.v29i1.9761

## Implementation artifacts
- specification a90bf935ef124bc9a748123d2ba67474049a5314
- derivations b49724dba87f9cf58a59ac611b781665b57dbc95
- witness 8d7142ed8f457a7a8647904b6e4c8e04e4b20ed7
- manuscript 01a5491100430fe8bf56793e6e1b557ba91dc652
- source lock e7cb725448a35b31fa879528dc01b02a72d052ca
- bibliography c95dbd1d1e3ddd0e3b99e067ce3dd654bf8201da
- Chapter Ledger a8d40ef1f4144def1c6e5cbd363d9837186b50f0
- Source Register 2b4ba80c4d8ccbf68804ab54b99b926204a387d5

## Exact minimal teaching witness
- concept class H={h00,h01,h10,h11} over probes q1,q2
- target h*=h11
- e1=(q1,1)
- e2=(q2,1)
- T*={e1,e2}
- V_H(T*)={h11}
- V_H(empty)=H
- V_H({e1})={h10,h11}
- V_H({e2})={h01,h11}
- exact minimum teaching-set size: 2

## High-progress/non-basis control
- auxiliary e3=(z,1), z outside target probe family
- p(e1)=1
- p(e2)=1
- p(e3)=5
- V_H({e3})=H
- therefore the highest-progress region does not reduce target ambiguity and is not in T*

## Mechanism-evidence ladder
- acquisition: evidence mechanism formed/used early
- persistence: evidence same declared mechanism remains later
- accessibility: evidence mechanism can be decoded/invoked/recovered under a declared interface
- behavioural expression: evidence later system produces target behavior
- no implication is promoted across these levels without separate evidence

## Durable boundaries
- minimality is relative to target/capability class, admissible examples, learner/reconstructor, and side information;
- minimal set does not imply unique optimal sequence;
- high progress does not imply minimal-basis membership;
- later behavior does not prove early-mechanism persistence;
- behavioral equivalence does not prove mechanistic identity.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
