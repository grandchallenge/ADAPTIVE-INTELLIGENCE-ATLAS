# Derivations — ATLAS-CH-GOVADAPT-001

## Scope

This packet formalizes the Atlas governed-adaptation construction.

It does not prove that the construction is uniquely correct, that process conformance implies substantive safety, or that one correction-capacity floor is universally optimal.

## 1. Protected state and candidate revision

Let

\[
g=(r,x,E,A,P,C,L),
\]

where \(r\) is protected revision identity, \(x\) operative state, \(E\) canonical evidence, \(A\) authority relation, \(P\) promotion state, \(C\) certification state, and \(L\) transition history.

A candidate revision is

\[
q=(id,r_{parent},\Delta,\hat r).
\]

The parent identity must match the protected revision unless an explicit rebase/revalidation transition exists.

## 2. Typed authority

For actor \(a\), define separate predicates:

\[
Auth_{prop}(a,q),
\quad
Auth_{exec}(a,q),
\quad
Auth_{promote}(a,\hat r),
\quad
Auth_{recover}(a,\hat r,r_\star),
\quad
Auth_{cert}(a,\hat r).
\]

No implication among them is automatic.

## 3. Evidence binding

For evidence

\[
e=(id,target,claim,payload,provenance),
\]

define

\[
Binds(e,r)=\mathbf 1\{target(e)=r\}.
\]

For required evidence family \(E_q^\star\),

\[
EvidenceOK(E,q)
=
\prod_{e\in E_q^\star} Binds(e,\hat r).
\]

If any required object targets a different revision, the exact-target evidence gate fails.

## 4. Repair invalidates exact-target validation

Suppose validation object \(e_1\) targets revision \(r_1\).

A repair creates \(r_2\neq r_1\).

Then

\[
Binds(e_1,r_2)=0.
\]

Fresh replay can produce \(e_2\) with

\[
Binds(e_2,r_2)=1.
\]

This is the exact-head replay rule.

## 5. Correction-capacity inheritance

From OPTIONALITY, use:

\[
C_{h,\epsilon}(x,\theta)\in\{0,1\},
\]

and

\[
CC_{h,\epsilon}(x;b)
=
\mathbb E_{\theta\sim b}
[
C_{h,\epsilon}(x,\theta)
].
\]

GOVADAPT does not redefine this inherited quantity.

It constrains which correction paths count as feasible by requiring that the path also be governance-authorized.

## 6. Authorized recovery path

Let a governed transition path be

\[
\gamma=(g_0\to g_1\to\cdots\to g_m),
\qquad
m\le h.
\]

Define \(AuthPath(\gamma)=1\) iff every edge is permitted by the authority contract in force for that edge.

For declared target consequence class \([r_\star]\), define

\[
RecAuth_h(g,[r_\star])=1
\]

iff an authorized path of length at most \(h\) reaches the declared target class.

A stored prior artifact can exist while

\[
RecAuth_h=0.
\]

## 7. Governance admissibility

Let the required conditions be:

- parent identity;
- exact-target evidence;
- applicable execution authority;
- any declared separation predicate;
- immediate invariant;
- correction-capacity floor.

Define

\[
Adm(g,q)
=
ParentOK
\cdot EvidenceOK
\cdot AuthorityOK
\cdot Sep
\cdot Inv
\cdot
\mathbf 1\{CC_{h,\epsilon}\ge\kappa\}.
\]

This Boolean product is a declared Atlas gate.

A different programme may legitimately choose a different gate.

## 8. Execution is not promotion

Execution:

\[
g\xrightarrow{execute(q)}g_q.
\]

Promotion requires a separate predicate and transition:

\[
g_q\xrightarrow{promote}g^+.
\]

Certification remains a separate coordinate.

## 9. Finite equal-utility witness

Let

\[
\Theta=\{N,D\},
\qquad
b(N)=b(D)=1/2.
\]

Two candidate revisions satisfy:

\[
\Delta U(A)=\Delta U(B)=1.
\]

Both pass the same parent, provenance, execution-authority, and immediate-invariant checks.

Only the future correction structure differs.

For candidate A:

\[
C_{h,0}(x_A,N)=1,
\qquad
C_{h,0}(x_A,D)=1.
\]

Hence

\[
CC_{h,0}(x_A;b)
=
\frac12(1)+\frac12(1)
=
1.
\]

For candidate B:

\[
C_{h,0}(x_B,N)=1,
\qquad
C_{h,0}(x_B,D)=0.
\]

Hence

\[
CC_{h,0}(x_B;b)
=
\frac12(1)+\frac12(0)
=
\frac12.
\]

## 10. Utility-only gate cannot distinguish

Define

\[
G_U(q)=\mathbf 1\{\Delta U(q)\ge1\}.
\]

Then

\[
G_U(A)=G_U(B)=1.
\]

## 11. Correction-aware gate separates

Set

\[
\kappa=1
\]

and define

\[
G_C(q)
=
G_U(q)
\cdot
\mathbf 1\{CC_{h,0}(x_q;b)\ge1\}.
\]

Then

\[
G_C(A)=1,
\qquad
G_C(B)=0.
\]

This separation comes entirely from the declared correction-capacity floor.

It does not prove that \(\kappa=1\) is generally optimal.

## 12. Raw action labels are insufficient

Suppose both post-revision states expose:

\[
\{continue,rollback\}.
\]

If the rollback label in one state lacks authority or cannot reach the target consequence class, raw action count is equal while governed recovery differs.

Therefore:

\[
\text{raw action count}
\not\Rightarrow
\text{correction capacity}.
\]

## 13. Backup versus recovery

A stored baseline artifact gives a candidate restoration object.

Recoverability additionally requires, as applicable:

- compatible state;
- authority;
- available dependencies;
- restorable external resources;
- bounded transition path;
- acceptable correction cost.

Thus:

\[
\text{backup exists}
\not\Rightarrow
RecAuth_h=1.
\]

## 14. Safety without liveness

Suppose every candidate fails a required gate.

The canonical state may remain:

\[
g_0\to g_0\to g_0\to\cdots.
\]

The invariant can remain true at every step while no adaptation is promoted.

Hence safety does not imply liveness.

## 15. Intervention precedents

Corrigibility literature studies cooperation with corrective intervention [@SoaresEtAl2015Corrigibility].

Safe interruptibility provides a formal treatment of interruption incentives in a specific reinforcement-learning setting [@OrseauArmstrong2016].

The Off-Switch Game studies incentives around preserving a human intervention channel under objective uncertainty [@HadfieldMenellEtAl2017OffSwitch].

These motivate the intervention dimension but do not imply the Atlas gate.

## 16. Governing-policy boundary

Authority over operative state \(x\) does not automatically imply authority over the authority relation \(A\).

A candidate that changes \(A\) belongs to a different transition class and must satisfy the governing process for policy change.

## 17. Claim boundary

The derivations establish:

- typed authority separation;
- exact-target evidence rebinding;
- authorized-path recoverability;
- a finite correction-capacity-aware gate;
- the equal-immediate-utility witness;
- backup/recovery non-equivalence;
- safety/liveness separation.

They do not establish universal safety, universal optimality, complete corrigibility, or substantive correctness from governance conformance.
