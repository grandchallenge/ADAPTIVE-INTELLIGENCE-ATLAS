# Chapter Specification — ATLAS-CH-MINCURR-001

## Identity

**Title:** Minimal Curricula and Reasoning Bases  
**Part:** Tokenization, Data, and Curriculum  
**Status target:** draft-v0.1  
**Implementation issue:** #251  
**Protected baseline:** 3981c7de350e2eb284eb0f3753c09321c173d436

## Hard prerequisites

### ATLAS-CH-PROGRESSSEARCH-001 / AUDIT-049

May inherit:

- explicit experience-space search;
- progress estimates with declared observation contract;
- exploration/coverage state;
- delayed-credit and finite-horizon semantics;
- generalization-state evidence as non-oracular feedback;
- exact exploit-only and immediate-greedy failure witnesses.

May not inherit minimality, reconstructability, or a transferable reasoning basis.

### ATLAS-CH-RESIDUAL-001 / AUDIT-006

May inherit:

- task-relative capability sufficiency;
- invariance/sufficiency separation;
- leastness relative to declared descriptor and post-processing classes;
- semantic versus operational reconstruction boundaries.

May not inherit existence, uniqueness, finite-dimensionality, or efficient computability of a universal minimal basis.

Exact identities and source scope are frozen in:

sources/source-locks/ATLAS-CH-MINCURR-001.yaml

## New primary sources

- Goldman and Kearns (1995): classical teaching complexity / teaching dimension.
- Zhu (2015): machine teaching as optimal training-set design for a specified learner/target.

## Chapter contract

Ask for the smallest admissible early experience/mechanism basis from which a declared later capability can be reconstructed.

The chapter must distinguish:

1. experience-space search;
2. current learning-progress signal;
3. target capability family;
4. admissible teaching/example language;
5. reconstruction rule;
6. minimality relative to that declaration;
7. acquisition;
8. persistence;
9. accessibility;
10. behavioural expression.

No implication may be silently promoted across these levels.

## Finite target-capability witness

Let the probe set be:

\[
Q=\{q_1,q_2\}.
\]

Let the admissible concept class be:

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

The target capability is therefore the ordered response pair:

\[
(1,1).
\]

## Teaching examples

Use the target-consistent labeled examples:

\[
e_1=(q_1,1),
\qquad
e_2=(q_2,1).
\]

For any teaching set \(T\), define version space:

\[
V_H(T)
=
\{h\in H:\text{$h$ is consistent with every example in }T\}.
\]

The declared reconstructor succeeds exactly when:

\[
|V_H(T)|=1.
\]

If unique, it returns the sole consistent hypothesis.

This is the admissible reconstruction rule for the witness.

## Exact two-example basis

For:

\[
T^\star=\{e_1,e_2\},
\]

we have:

\[
V_H(T^\star)=\{h_{11}\}.
\]

Therefore \(T^\star\) reconstructs the declared target exactly.

## Strict-smaller failure

The strict target-consistent subsets are:

\[
\varnothing,
\qquad
\{e_1\},
\qquad
\{e_2\}.
\]

Their version spaces are:

\[
V_H(\varnothing)
=
\{h_{00},h_{01},h_{10},h_{11}\},
\]

\[
V_H(\{e_1\})
=
\{h_{10},h_{11}\},
\]

\[
V_H(\{e_2\})
=
\{h_{01},h_{11}\}.
\]

Each has size greater than one.

Hence no strict smaller target-consistent subset reconstructs \(h^\star\).

Therefore:

\[
\boxed{
T^\star
\text{ is minimal for the declared }(H,h^\star,Q,\text{reconstructor}).
}
\]

## Minimal does not mean universal

This result is not:

\[
\text{universal minimal curriculum}.
\]

Change:

- concept class;
- probe family;
- learner;
- example language;
- reconstruction rule;
- allowed side information;

and the minimum can change.

Minimality is declaration-relative.

## Teaching-dimension connection

The witness is an exact finite instance of the teaching-set idea: examples are chosen to uniquely identify the target relative to a concept class.

The chapter may use teaching-dimension language only within this relative formalism.

## Machine-teaching connection

The same witness can be read as a tiny machine-teaching problem:

- learner/reconstructor fixed;
- target fixed;
- teacher chooses examples;
- objective includes minimum teaching-set size subject to exact target recovery.

The chapter must not imply that this learner model describes arbitrary neural training.

## High-progress/non-basis control

Introduce an auxiliary experience:

\[
e_3=(z,1),
\]

where \(z\notin Q\).

The target concept class \(H\) has no target-capability coordinate at \(z\).

Freeze progress scores:

\[
p(e_1)=1,
\qquad
p(e_2)=1,
\qquad
p(e_3)=5.
\]

Thus:

\[
e_3
\]

has the highest current progress score.

But observing \(e_3\) alone imposes no constraint on \(H\):

\[
V_H(\{e_3\})
=
H.
\]

So:

\[
|V_H(\{e_3\})|=4.
\]

Therefore the highest-progress region does not belong to the minimal target-identifying basis.

## Search versus basis

The witness establishes:

\[
\boxed{
\text{high learning progress}
\not\Rightarrow
\text{membership in a minimal reconstructive basis}.
}
\]

PROGRESSSEARCH decides where experience may be valuable next.

MINCURR asks which experiences are necessary/sufficient for a declared reconstruction objective.

These are different optimization problems.

## Basis versus sequence

A minimal set does not automatically prescribe an order.

For \(T^\star\), both sequences:

\[
(e_1,e_2)
\]

and:

\[
(e_2,e_1)
\]

identify the target after both examples.

If acquisition dynamics make order matter, that is an added learner-dependent structure.

Set minimality and sequence optimality must remain distinct.

## Minimal teaching set need not be unique

The exact witness happens to have a unique target-consistent size-two set because \(Q\) has only two target probes.

In other concept classes, multiple minimal teaching sets may exist.

Therefore:

\[
\boxed{
\text{minimal size}
\not\Rightarrow
\text{unique basis}.
}
\]

## Reasoning-basis interpretation

A reasoning basis is a declared collection of portable operations/constraints sufficient to reconstruct a capability family under an admissible composition class.

The finite teaching witness supplies the structural pattern:

- sufficiency;
- strict-smaller failure;
- declared reconstruction map;
- relative minimality.

It does not establish that real neural reasoning decomposes into two discrete symbolic operations.

## Mechanism evidence ladder

The chapter must keep four levels distinct.

### A0 — acquisition evidence

Evidence that mechanism/operation \(m\) is formed or used during an early learning interval.

This may come from:

- intervention;
- representation probe;
- mechanistic readout;
- training-local behavior.

It is time-local evidence.

### A1 — persistence evidence

Evidence that the same declared mechanism \(m\) remains present at later state \(t_1\).

Early acquisition does not establish persistence.

### A2 — accessibility evidence

Evidence that the persistent mechanism can be:

- decoded;
- invoked;
- recovered;
- causally accessed

through a declared admissible interface.

Persistence does not guarantee accessibility.

### A3 — behavioural expression

Evidence that the later system expresses the declared capability on the probe family.

Behavioural expression does not prove which earlier mechanism persisted or caused it.

## Non-implications

The manuscript must explicitly reject:

\[
\text{acquisition}
\not\Rightarrow
\text{persistence},
\]

\[
\text{persistence}
\not\Rightarrow
\text{accessibility},
\]

\[
\text{accessibility}
\not\Rightarrow
\text{expression in every context},
\]

and:

\[
\text{later behavioural expression}
\not\Rightarrow
\text{persistence/causality of an earlier mechanism}.
\]

## Persistence identity problem

To claim the same mechanism persists, a study needs an identity criterion.

Examples can include:

- invariant functional signature;
- matched causal intervention;
- aligned mechanistic subspace;
- declared reconstruction relation.

Similarity of two aggregate behaviors is not enough.

## Accessibility is interface-relative

A latent operation can be present but inaccessible to:

- the current prompt;
- the current policy;
- the current readout;
- the current controller.

Therefore accessibility must specify the allowed interface/intervention class.

## Behavioural suppression

A persistent and accessible mechanism can fail to express behavior because:

- another mechanism dominates;
- the context does not trigger it;
- routing suppresses it;
- downstream control changes.

Thus absence of expression is not by itself absence of mechanism.

## Behavioural recovery

Conversely, later behavior can reappear via:

- original persistent mechanism;
- relearning;
- alternate mechanism;
- compensating route.

Therefore behavioural recovery alone cannot identify mechanism persistence.

## Minimal curriculum objective

For general declared learner \(L\), target \(\theta^\star\), admissible experience family \(\mathcal E\), and cost \(c(T)\), a machine-teaching-style problem can be written:

\[
\min_{T\subseteq\mathcal E}
c(T)
\]

subject to:

\[
L(T)=\theta^\star
\]

or a declared capability-equivalence condition.

The exact witness uses:

\[
c(T)=|T|
\]

and exact unique identification.

## Reconstruction-relative alternative

When exact model identity is unnecessary, require only declared capability reconstruction:

\[
B(L(T),q)=B^\star(q)
\quad
\forall q\in\mathcal Q.
\]

This follows the RESIDUAL discipline: sufficient capability can be weaker than full state identity.

Minimality must say which of these objectives is intended.

## Generalization boundary

A curriculum minimal for:

\[
\mathcal Q
\]

need not be minimal or sufficient for a larger probe family:

\[
\mathcal Q'.
\]

Therefore broad later capability cannot be inferred from a narrow witness without expanding the declared probe family.

## Search-control requirement

Any empirical claim that high-progress experiences reveal the minimal basis should include controls where:

- high-progress experience is auxiliary/irrelevant to target reconstruction;
- low-progress experience is nevertheless necessary for reconstruction;
- search score and version-space reduction disagree.

The exact \(e_3\) witness supplies the first such control.

## Required exact replay

The computational witness must enumerate all subsets of:

\[
\{e_1,e_2\}
\]

and verify:

- target reconstruction succeeds only on \(T^\star\);
- every strict smaller subset leaves version-space size \(>1\).

It must separately verify:

\[
p(e_3)>p(e_1),p(e_2)
\]

while:

\[
V_H(\{e_3\})=H.
\]

## Required non-implications

The manuscript must reject:

\[
\text{highest progress}
\not\Rightarrow
\text{minimal-basis membership},
\]

\[
\text{minimal for one capability family}
\not\Rightarrow
\text{universal minimality},
\]

\[
\text{minimal set}
\not\Rightarrow
\text{optimal sequence},
\]

\[
\text{later success}
\not\Rightarrow
\text{early-mechanism persistence},
\]

and:

\[
\text{behavioural equivalence}
\not\Rightarrow
\text{mechanistic identity}.
\]

## Reader outcomes

A reader should be able to:

1. distinguish experience search from minimal reconstructive basis selection;
2. define a version-space teaching criterion;
3. reproduce the exact two-bit minimality proof;
4. show why every strict smaller teaching set fails;
5. reproduce the high-progress/non-basis control;
6. state why minimality is learner/capability/example-class relative;
7. distinguish set minimality from sequence optimization;
8. distinguish acquisition, persistence, accessibility, and expression;
9. explain why later behavior cannot prove early mechanism persistence;
10. connect teaching-set minimality to the broader Residual/reconstructability programme without claiming a universal basis.

## Required artifacts

- source lock;
- bibliography entries;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## References

- [@GoldmanKearns1995Teaching]
- [@Zhu2015MachineTeaching]

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-MINCURR-001.yaml
