# Governed Adaptation

**Epistemic status:** audited Optionality and Research-State-Machine prerequisites + bounded corrigibility/interruptibility literature + Atlas synthesis.

Adaptive systems change.

Parameters move. Policies update. Data mixtures shift. Components are replaced. New evidence arrives. Research programmes advance from one protected state to another.

The difficult question is not whether change is possible. It is:

> **When a system is allowed to change, what must remain true so that later correction, provenance, and bounded authority are not silently destroyed by the change itself?**

This chapter calls that problem **governed adaptation**.

The central distinction is:

\[
\boxed{
\text{can change}
\neq
\text{authorized to change}
\neq
\text{safe to promote}
}
\]

The audited Optionality chapter supplies a language for correction capacity and recoverability.

The audited Research as a State Machine chapter supplies typed states, guarded transitions, exact identity, idempotence, authority separation, and fail-closed promotion.

The present chapter composes those ideas into an adaptation contract.

## 1. Adaptation as a governed transition

Let the current protected state be

\[
g=(r,x,E,A,P,C,L).
\]

Here:

- \(r\) is the exact protected revision identity;
- \(x\) is the operative state;
- \(E\) is canonical evidence;
- \(A\) is the authority relation;
- \(P\) is promotion/programme state;
- \(C\) is certification state;
- \(L\) is durable history.

A candidate revision is

\[
q=(id,r_{parent},\Delta,\hat r).
\]

The candidate declares which protected parent it assumes, what bounded change it proposes, and which exact result identity it produces.

If the parent changed, the proposal may already be stale.

## 2. Authority is typed

A common governance error is to collapse every form of permission into one word.

The Atlas keeps at least five relations separate:

- proposal authority;
- execution authority;
- promotion authority;
- recovery authority;
- certification authority.

These can belong to the same actor under one policy. They are still different relations.

A contributor who may propose a change does not thereby own canonical promotion.

An executor who can stage a revision does not thereby certify it.

A recovery operator does not thereby acquire policy-writing authority.

## 3. Execution is not promotion

A candidate can be executed in a staging state:

\[
g\xrightarrow{execute(q)}g_q.
\]

This creates a candidate state.

Promotion is separate:

\[
g_q\xrightarrow{promote}g^+.
\]

This separation creates a place to ask:

- Did the exact candidate pass its required checks?
- Are those checks bound to this revision?
- Were the relevant actors authorized?
- Is a recovery path still available?
- Did a repair invalidate earlier evidence?
- Is certification required or merely promotion?

The Research-State-Machine prerequisite already established that successful execution is not sufficient for promotion.

Governed adaptation applies that rule to changing systems.

## 4. Evidence belongs to exact targets

Let an evidence object be

\[
e=(id,target,claim,payload,provenance).
\]

Define:

\[
Binds(e,r)
\iff
target(e)=r.
\]

Suppose revision \(r_1\) passes validation.

A repair then produces:

\[
r_2\neq r_1.
\]

The old validation remains historical evidence.

It is not exact-target evidence for \(r_2\).

\[
Binds(e_{r_1},r_2)=0.
\]

The practical rule is simple:

> **After a material revision changes exact identity, replay the load-bearing evidence on the new exact target.**

This protects against validating one object and promoting another.

## 5. Canonical state and history

Adaptation can overwrite the evidence needed to understand the change.

A governed system therefore separates:

- canonical current state;
- append-only transition history;
- evidence objects;
- interpretation;
- review;
- promotion;
- certification.

A new revision should not erase the identity of its predecessor merely because the predecessor is no longer current.

History answers: how did we get here?

Canonical state answers: what is protected now?

Those are different questions.

## 6. Correction capacity enters the gate

Optionality introduced conditional correction feasibility:

\[
C_{h,\epsilon}(x,\theta)
\]

and ex-ante correction capacity:

\[
CC_{h,\epsilon}(x;b)
=
\mathbb E_{\theta\sim b}
[
C_{h,\epsilon}(x,\theta)
].
\]

Governed adaptation can use this as one explicit admissibility condition.

For a declared floor \(\kappa\), require:

\[
CC_{h,\epsilon}(x_q;b)\ge\kappa.
\]

This does not say that preserving more optionality is always better.

It says something narrower:

> If the governing process declares preservation of specified correction paths to be a requirement, then candidate evaluation must measure those paths rather than assume they survived.

## 7. A finite admissibility gate

One possible gate is:

\[
Adm(g,q)
=
ParentOK
\cdot
EvidenceOK
\cdot
AuthorityOK
\cdot
Sep
\cdot
Inv
\cdot
\mathbf 1\{CC_{h,\epsilon}\ge\kappa\}.
\]

The factors mean:

- exact parent identity matches;
- required evidence binds to the candidate;
- required authority predicates hold;
- any declared separation relation holds;
- the declared invariant holds;
- the declared correction-capacity floor holds.

The product is Boolean.

If any required factor is zero, the candidate is not admissible under this particular gate.

The Atlas does not claim this factorization is universal.

Its value is that each reason for refusal is typed.

## 8. Equal immediate value, unequal correction capacity

Consider a deliberately small witness.

Let:

\[
\Theta=\{N,D\},
\]

where:

- \(N\): no later defect is discovered;
- \(D\): a later defect is discovered.

Use symmetric prior:

\[
b(N)=b(D)=1/2.
\]

Two candidates satisfy:

\[
\Delta U(A)=\Delta U(B)=1.
\]

Both pass the same immediate checks.

Only one preserves a governed recovery path.

### Candidate A

If \(N\) occurs, no correction is required.

If \(D\) occurs, an authorized recovery path returns to the accepted target.

Therefore:

\[
C_{h,0}(A,N)=1,
\qquad
C_{h,0}(A,D)=1.
\]

Hence:

\[
CC_{h,0}(A;b)=1.
\]

### Candidate B

If \(N\) occurs, no correction is required.

If \(D\) occurs, the declared correction target is unreachable within the authorized horizon.

Therefore:

\[
C_{h,0}(B,N)=1,
\qquad
C_{h,0}(B,D)=0.
\]

Hence:

\[
CC_{h,0}(B;b)=1/2.
\]

Immediate value ties.

Correction capacity does not.

## 9. Why a utility-only gate misses the difference

Define:

\[
G_U(q)=\mathbf 1\{\Delta U(q)\ge1\}.
\]

Then:

\[
G_U(A)=G_U(B)=1.
\]

Now declare:

\[
\kappa=1
\]

and define:

\[
G_C(q)
=
G_U(q)
\mathbf 1\{CC_{h,0}(q;b)\ge1\}.
\]

Then:

\[
G_C(A)=1,
\qquad
G_C(B)=0.
\]

The witness establishes only this finite separation.

It does not tell us that every real system should use \(\kappa=1\).

It tells us that an objective containing only immediate value can omit a property the governing process may care about.

## 10. Raw action count is not enough

Suppose both candidate states expose two commands:

- continue;
- rollback.

A superficial option count says both states have two actions.

But suppose rollback in one state:

- lacks authority;
- points to an incompatible artifact;
- cannot restore external state;
- exceeds the permitted horizon;
- or fails the declared target semantics.

Then the labels are present while the functional correction path is absent.

This is why Optionality treats functional consequences and correction feasibility separately from raw action count.

## 11. A backup is not recovery

“We have a backup” is an artifact statement.

“We can recover” is a transition claim.

Recovery can fail because:

- the backup is corrupt;
- dependencies changed;
- external data cannot be restored;
- credentials expired;
- migrations were one-way;
- the recovery actor lacks authority;
- restored bytes do not recreate the declared consequence class.

For target class \([r_\star]\), define governed recovery by:

\[
RecAuth_h(g,[r_\star])=1
\]

only when an authorized path of length at most \(h\) reaches the declared target class.

## 12. Corrigibility and intervention precedents

Corrigibility was introduced as a problem of cooperation with corrective intervention despite incentives that can make capable agents resist shutdown or preference modification [@SoaresEtAl2015Corrigibility].

Orseau and Armstrong study safe interruptibility in reinforcement learning, asking how intervention can occur without training the agent to seek or avoid interruption [@OrseauArmstrong2016].

Hadfield-Menell and colleagues analyze an off-switch game in which an agent's incentive to preserve human intervention depends on uncertainty about the underlying objective and on treating human action as informative [@HadfieldMenellEtAl2017OffSwitch].

These are important precedents.

They are not interchangeable.

The Atlas keeps separate:

- corrigibility;
- interruptibility;
- human intervention-channel preservation;
- rollback;
- correction capacity;
- governance authority.

The literature motivates the intervention problem. It does not imply the Atlas gate.

## 13. Preserving correction can have cost

Optionality already established that preserving more options is not universally optimal.

The same warning applies here.

A recovery path can impose:

- storage cost;
- compatibility burden;
- slower migrations;
- operational complexity;
- delayed optimization.

Governed adaptation can therefore treat correction capacity as:

- an objective;
- a constraint;
- or a diagnostic.

It is not an unconditional command to preserve every possible past state.

## 14. Bounded authority

Authority to alter operative state \(x\) does not automatically include authority to alter the authority relation \(A\).

If a candidate changes the governance policy itself, that is a different transition class.

The system needs whatever authority the governing process assigns to policy change.

Thus:

\[
\boxed{
\text{authority over system state}
\neq
\text{authority over the rule that grants authority}
}
\]

Without this distinction, bounded delegation becomes unrestricted delegation by implication.

## 15. Safety is not liveness

A strict gate can refuse unsupported candidates.

That is a safety property.

But a gate can also refuse everything forever.

Consider:

\[
g_0\to g_0\to g_0\to\cdots.
\]

The invariant remains true.

No candidate advances.

Therefore:

\[
\text{fail-closed safety}
\not\Rightarrow
\text{eventual progress}.
\]

A programme claiming eventual adaptation needs a separate liveness argument.

## 16. Governance conformance is not substantive truth

Suppose a candidate:

- has exact provenance;
- passes all required checks;
- has proper authority;
- preserves the declared recovery path;
- receives promotion.

What has been shown?

That the declared governance contract was satisfied.

What has not automatically been shown?

- that a scientific hypothesis is true;
- that the system is globally safer;
- that every objective improved;
- that the evidence was complete;
- that no undeclared failure mode exists.

Process integrity matters because it lets us state exactly what was established.

## 17. Repairs invalidate exact-target evidence

A common operational pattern is:

1. candidate \(r_1\) is tested;
2. test fails;
3. candidate is repaired to \(r_2\);
4. someone remembers that “validation already ran.”

That is insufficient.

The correct sequence is:

1. bind evidence to \(r_1\);
2. repair to \(r_2\);
3. treat \(r_1\)'s exact-target validation as stale for promotion of \(r_2\);
4. replay on \(r_2\);
5. promote only if the new exact target passes.

This closes the identity gap between evidence and mutation.

## 18. Recovery must name a target

“Return to normal” is not a formal recovery target.

A governed recovery should name:

- target revision or consequence class;
- maximum horizon;
- authority;
- acceptable cost or tolerance;
- evidence required after restoration.

A rollback can restore bytes while failing to restore behavior.

It can restore behavior while failing to restore external state.

It can restore a previous revision while invalidating later evidence.

Recovery semantics belong in the transition system.

## 19. State-relative authority

Authority can be state-relative.

Permission granted for one bounded candidate should not silently cover a materially different object.

If the candidate's parent, scope, target identity, or governing policy changes materially, the applicable authority contract should be re-evaluated.

This is the governance analogue of exact-target evidence.

## 20. Why this matters for adaptive intelligence

An adaptive system that cannot preserve correction channels can become more capable while becoming harder to steer.

A research programme that cannot preserve provenance can become more productive while becoming less auditable.

A deployment pipeline that cannot preserve exact-target evidence can become faster while losing the ability to say what was actually validated.

Governed adaptation is the attempt to preserve the infrastructure of correction while permitting change.

It is not anti-adaptation.

It is a theory of admissible change under declared constraints.

## 21. Failure modes

### 21.1 Capability as authority

A system can perform an action and therefore treats itself as permitted to perform it.

This confuses mechanism with governance.

### 21.2 Promotion by execution

A candidate runs successfully and is treated as canonical.

This skips the promotion gate.

### 21.3 Stale green evidence

A repaired candidate inherits validation from its predecessor.

This violates exact-target binding.

### 21.4 Cosmetic rollback

A rollback command exists but cannot restore the declared target.

This confuses interface with recoverability.

### 21.5 Option counting

A system counts command labels rather than functional correction paths.

### 21.6 Corrigibility by naming

An intervention channel exists and the system is therefore called corrigible.

The stronger property has not been established.

### 21.7 Safety without progress

A fail-closed system never violates the gate but also never advances.

### 21.8 Governance as truth

A compliant process outcome is treated as proof that a scientific or empirical claim is correct.

### 21.9 Unbounded delegation

Authority over operative state is interpreted as authority over the governance contract.

### 21.10 Recovery without revalidation

A prior revision is restored but its current environment and dependencies are not rechecked.

## 22. Downstream handoff

Frontier Questions of Adaptive Intelligence may assume:

- governed adaptation is a typed transition problem;
- authority is separated by role;
- candidate evidence binds to exact target identity;
- authorized recovery paths are distinct from stored backups;
- correction capacity can be an explicit gate dimension;
- immediate value can tie while correction capacity differs;
- fail-closed safety does not imply liveness;
- intervention precedents do not collapse into a universal theorem.

FRONTIER must independently determine which unresolved questions deserve programme priority.

## 23. Epistemic status

Established prerequisite layer:

- viable continuation and correction-capacity semantics;
- typed governed states and guarded transitions;
- exact identity, idempotence, recovery classes, and authority separation.

External precedent layer:

- corrective intervention/corrigibility problem [@SoaresEtAl2015Corrigibility];
- safe interruptibility in a declared RL setting [@OrseauArmstrong2016];
- off-switch incentive analysis under objective uncertainty [@HadfieldMenellEtAl2017OffSwitch].

Atlas-owned synthesis:

- governed adaptive state;
- authority separation;
- exact-target adaptation gate;
- authorized recovery-path semantics;
- correction-capacity gate composition;
- equal-immediate-value finite witness.

Not established here:

- universal safety;
- universal adaptation optimality;
- complete corrigibility;
- universal rollback feasibility;
- substantive truth from governance conformance.

## References used in this chapter

- [@SoaresEtAl2015Corrigibility] — corrigibility and corrective intervention.
- [@OrseauArmstrong2016] — safe interruptibility in reinforcement learning.
- [@HadfieldMenellEtAl2017OffSwitch] — incentives around preserving a human off-switch.

Exact provenance and authority boundaries are locked in:

sources/source-locks/ATLAS-CH-GOVADAPT-001.yaml
