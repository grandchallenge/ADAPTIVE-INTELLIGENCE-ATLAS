# ATLAS-CH-MINCURR-001 — Derivation Packet

## Scope

This packet proves the exact finite minimal-teaching witness and the high-progress/non-basis control for MINCURR-001.

It does not prove universal curriculum minimality or neural mechanism persistence.

## D1. Concept class

Let:

\[
Q=\{q_1,q_2\}.
\]

Define:

\[
H=\{h_{00},h_{01},h_{10},h_{11}\},
\]

with:

\[
h_{ab}(q_1)=a,
\qquad
h_{ab}(q_2)=b.
\]

Target:

\[
h^\star=h_{11}.
\]

## D2. Version space

For a finite set \(T\) of labeled experiences, write \(T_Q=\{(q,y)\in T:q\in Q\}\). Define the target-relative version space:

\[
V_H(T)
=
\{h\in H:\forall(q,y)\in T_Q,\ h(q)=y\}.
\]

Only probes in the declared domain \(Q\) constrain hypotheses in \(H\). Auxiliary experiences outside \(Q\) are ignored **for this target-identification test**, not asserted to be unhelpful for other learning goals.

The declared exact reconstructor succeeds iff:

\[
|V_H(T)|=1.
\]

If unique, it returns that sole hypothesis.

## D3. Candidate teaching basis

Use:

\[
e_1=(q_1,1),
\qquad
e_2=(q_2,1).
\]

Define:

\[
T^\star=\{e_1,e_2\}.
\]

Consistency with \(e_1\) removes \(h_{00},h_{01}\).

Consistency with \(e_2\) removes \(h_{00},h_{10}\).

Both constraints together leave only:

\[
\boxed{
V_H(T^\star)=\{h_{11}\}.
}
\]

Therefore \(T^\star\) reconstructs the target exactly.

## D4. Empty-set failure

With no examples:

\[
V_H(\varnothing)=H.
\]

Thus:

\[
|V_H(\varnothing)|=4>1.
\]

The empty set does not reconstruct the target uniquely.

## D5. First singleton failure

For:

\[
T_1=\{e_1\},
\]

the hypotheses consistent with \(q_1\mapsto1\) are:

\[
h_{10},h_{11}.
\]

Hence:

\[
\boxed{
V_H(T_1)=\{h_{10},h_{11}\}.
}
\]

Thus:

\[
|V_H(T_1)|=2>1.
\]

## D6. Second singleton failure

For:

\[
T_2=\{e_2\},
\]

the hypotheses consistent with \(q_2\mapsto1\) are:

\[
h_{01},h_{11}.
\]

Hence:

\[
\boxed{
V_H(T_2)=\{h_{01},h_{11}\}.
}
\]

Again:

\[
|V_H(T_2)|=2>1.
\]

## D7. Relative minimality theorem

The strict subsets of \(T^\star\) are exactly:

\[
\varnothing,
\{e_1\},
\{e_2\}.
\]

All three have version-space size greater than one.

Meanwhile:

\[
|V_H(T^\star)|=1.
\]

Therefore:

\[
\boxed{
T^\star
\text{ is inclusion-minimal and cardinality-minimal among target-consistent subsets of }\{e_1,e_2\}.
}
\]

This theorem is relative to:

- \(H\);
- \(h^\star\);
- example language \(\{e_1,e_2\}\);
- the exact consistency-based reconstructor.

## D8. Minimum size

No size-zero or size-one target-consistent teaching set identifies \(h^\star\).

A size-two set does.

Thus the minimum size is:

\[
\boxed{2}.
\]

## D9. Minimality is not universality

If side information reduced the concept class to:

\[
\{h_{10},h_{11}\},
\]

then:

\[
\{e_2\}
\]

would identify \(h_{11}\).

If the probe family changed, the minimum could also change.

Therefore:

\[
\boxed{
\text{minimality is relative to the declared problem}.
}
\]

## D10. High-progress auxiliary experience

Introduce auxiliary experience:

\[
e_3=(z,1),
\]

with:

\[
z\notin Q.
\]

Since hypotheses in \(H\) are defined only on \(Q\), \(e_3\) imposes no target-class constraint.

Therefore:

\[
\boxed{
V_H(\{e_3\})=H.
}
\]

So:

\[
|V_H(\{e_3\})|=4.
\]

## D11. Freeze progress scores

Let:

\[
p(e_1)=1,
\qquad
p(e_2)=1,
\qquad
p(e_3)=5.
\]

Then:

\[
\boxed{
p(e_3)>p(e_1)=p(e_2).
}
\]

An exploit-only current-progress search would prefer \(e_3\).

But:

\[
e_3\notin T^\star
\]

and:

\[
V_H(\{e_3\})=H.
\]

Hence:

\[
\boxed{
\text{highest current progress}
\not\Rightarrow
\text{minimal-basis membership}.
}
\]

## D12. Progress and target information are different objectives

Define target ambiguity:

\[
A(T)=|V_H(T)|.
\]

Then:

\[
A(\{e_3\})=4,
\]

while:

\[
A(\{e_1\})=2,
\qquad
A(\{e_2\})=2.
\]

Thus the highest-progress experience produces zero reduction in target ambiguity:

\[
4-4=0.
\]

Each lower-progress target example reduces ambiguity by two hypotheses.

Therefore current learning progress and target-identification value can be ordered differently.

## D13. Set versus sequence

Both ordered curricula:

\[
(e_1,e_2)
\]

and:

\[
(e_2,e_1)
\]

end with the same teaching set \(T^\star\).

Under the declared order-insensitive consistency reconstructor, both identify \(h^\star\).

Thus:

\[
\boxed{
\text{minimal set}
\not\Rightarrow
\text{unique optimal order}.
}
\]

A sequence claim requires a learner whose update dynamics depend on order.

## D14. Capability-relative reconstruction

Exact concept identity is stronger than necessary in many settings.

Let declared behavior be:

\[
B(h,q)
\]

on probe family \(\mathcal Q\).

A weaker reconstruction criterion is:

\[
B(\widehat h,q)=B(h^\star,q)
\quad
\forall q\in\mathcal Q.
\]

Two internal hypotheses can then be equivalent for the declared capability.

This is the direct bridge to the RESIDUAL programme.

Minimality must specify whether it targets:

- exact model identity;
- capability-equivalence;
- another declared reconstruction relation.

## D15. Acquisition, persistence, accessibility, expression

Let:

\[
A_0(m)
\]

denote evidence that mechanism \(m\) was acquired during an early interval.

Let:

\[
P_1(m)
\]

denote evidence that the same declared mechanism persists later.

Let:

\[
X_1(m,\mathcal I)
\]

denote evidence that it is accessible through admissible interface class \(\mathcal I\).

Let:

\[
E_1(B,\mathcal Q)
\]

denote later behavioural expression of capability \(B\) on probes \(\mathcal Q\).

These are distinct predicates.

## D16. Acquisition does not imply persistence

Evidence at time \(t_0\):

\[
A_0(m)=1
\]

does not logically imply:

\[
P_1(m)=1.
\]

The mechanism may be overwritten, transformed beyond the identity criterion, or replaced.

A persistence claim needs longitudinal evidence.

## D17. Persistence does not imply accessibility

Even if:

\[
P_1(m)=1,
\]

the mechanism can be inaccessible to a declared interface.

Therefore:

\[
\boxed{
P_1(m)
\not\Rightarrow
X_1(m,\mathcal I).
}
\]

## D18. Accessibility does not force expression

Even if the mechanism is recoverable or causally invocable:

\[
X_1(m,\mathcal I)=1,
\]

normal behavior can fail to express it because of routing, context, competition, or downstream control.

Thus:

\[
\boxed{
X_1
\not\Rightarrow
E_1
}
\]

without context assumptions.

## D19. Expression does not identify persistence

Later behavior can arise through:

- the original persistent mechanism;
- relearning;
- a compensating route;
- a distinct mechanism.

Therefore:

\[
\boxed{
E_1
\not\Rightarrow
P_1(m)
}
\]

for a specific early mechanism \(m\).

This is an epistemic non-implication, not a statement that persistence never occurs.

## D20. Evidence-ladder consequence

A strong empirical claim that an early reasoning basis survives into later capability should separately establish:

1. acquisition;
2. longitudinal identity/persistence;
3. accessibility;
4. later expression or causal contribution.

Skipping a level changes the claim.

## Durable propositions

1. \(T^\star=\{(q_1,1),(q_2,1)\}\) uniquely identifies \(h_{11}\).
2. Every strict smaller target-consistent subset fails unique identification.
3. The minimum teaching-set size is exactly two for the declared witness.
4. High progress on \(e_3\) does not reduce the target version space.
5. Progress-search priority need not coincide with minimal-basis membership.
6. Minimality is relative to concept/capability class, example language, learner/reconstructor, and allowed side information.
7. Minimal set and optimal sequence are different questions.
8. Capability-equivalent reconstruction can be weaker than exact model identity.
9. Acquisition, persistence, accessibility, and behavioural expression are separate evidence predicates.
10. Later behavioral success does not identify which early mechanism persisted or caused it.

## Claim boundary

This packet proves only the declared finite teaching-set witness and its progress-control separation. It does not establish a universal minimal curriculum, a universal reasoning basis, or persistence of any real neural mechanism.
