# Composition Without Catastrophe
<!-- ATLAS-CH-COMPOSE-001 -->

**Epistemic status:** audited Boundary Contracts + audited Split-Operator Networks + Atlas-owned exact composition synthesis.  
**Specification:** manuscript/specifications/ATLAS-CH-COMPOSE-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-COMPOSE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-COMPOSE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-COMPOSE-001.yaml

A system can be built from components that are individually reasonable and still fail as a whole.

That is not paradoxical.

The reason is that composition introduces new questions.

A component can satisfy its own input/output contract while a downstream component assumes something different.

Two maps can each have modest local sensitivity while their product violates a system budget.

The same two transformations can be safe in one order and unsafe in another.

A local certificate can be correct and still be irrelevant outside its operating region.

The governing rule of this chapter is:

\[
\boxed{
\text{component validity}
+
\text{component validity}
\not\Rightarrow
\text{system validity}.
}
\]

The missing object is the composition argument.

## 1. Components do not compose by optimism

Suppose

\[
x\xrightarrow{f}y\xrightarrow{g}z.
\]

A naive implementation view asks:

> do the tensor shapes match?

A stronger contract view asks:

- does \(y\) mean what \(g\) expects?
- is \(y\) inside the operating region required by \(g\)?
- are invariants preserved?
- are perturbation and error budgets compatible?
- does ordering matter?
- what happens to upstream error after downstream amplification?

These are different questions.

Passing one does not answer the others.

The audited Boundary Contracts chapter supplied the interface language.

The audited Split-Operator Networks chapter supplied the order/noncommutativity language.

COMPOSE puts them together.

## 2. A composition has obligations of its own

Write a provisional boundary contract for \(f\) as

\[
C_f
=
(\mathcal X,\mathcal Y,\Sigma_f,\mathcal I_f,\mathcal S_f,\mathcal E_f).
\]

Write one for \(g\) as

\[
C_g
=
(\mathcal Y,\mathcal Z,\Sigma_g,\mathcal I_g,\mathcal S_g,\mathcal E_g).
\]

The shared symbol \(\mathcal Y\) is not enough.

The connecting boundary also has to satisfy:

- semantic compatibility;
- domain compatibility;
- invariant compatibility;
- sensitivity assumptions;
- numerical/error accounting.

This chapter uses the explanatory notation

\[
C_f\triangleright C_g
\]

to mean that the exported guarantees of \(f\) satisfy the imported assumptions of \(g\) for the declared composition.

This is Atlas notation.

It is not proposed as a universal contract standard.

## 3. The first composition law is the chain rule

At a differentiable operating point,

\[
J_{g\circ f}(x)
=
J_g(f(x))J_f(x).
\]

Therefore

\[
\|J_{g\circ f}(x)\|_2
\le
\|J_g(f(x))\|_2
\|J_f(x)\|_2.
\]

This statement is elementary.

Its implications are not.

The local sensitivities multiply in an upper bound.

So a downstream stage can amplify upstream perturbation.

But the product bound can also be very loose.

The actual alignment of the singular directions matters.

This is already enough to show why component-local sensitivity numbers are not a system certificate.

## 4. The exact two-component witness

Take

\[
A=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix}.
\]

Both components have the same operator norm:

\[
\boxed{
\|A\|_2=\|B\|_2=\frac32.
}
\]

Suppose each component has a valid local contract allowing gain up to

\[
\frac32.
\]

Now impose a system-level gain budget

\[
\tau=2.
\]

Each component passes its local test.

The composition still has work to do.

## 5. Chronological order matters

For column vectors, chronological \(A\) then \(B\) is represented by

\[
BA.
\]

Compute:

\[
BA
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

This is an orthogonal swap.

Therefore

\[
\boxed{
\|BA\|_2=1.
}
\]

The system gain budget passes:

\[
1<2.
\]

Now reverse the chronology.

Chronological \(B\) then \(A\) is

\[
AB.
\]

Compute:

\[
AB
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}.
\]

Its singular values are

\[
\frac94,
\qquad
\frac49.
\]

Therefore

\[
\boxed{
\|AB\|_2=\frac94.
}
\]

Now the system gain budget fails:

\[
\frac94>2.
\]

Same components.

Same component-local contracts.

Different order.

Different system disposition.

## 6. Product order is not chronological prose

The notation matters.

For column-vector states, matrix products act right-to-left.

So:

- chronological \(A\) then \(B\) corresponds to \(BA\);
- chronological \(B\) then \(A\) corresponds to \(AB\).

This distinction was already repaired and frozen in the audited Split-Operator chapter.

COMPOSE inherits it without ambiguity.

## 7. The pair is genuinely noncommuting

The difference is

\[
[A,B]
=
AB-BA.
\]

Exactly,

\[
[A,B]
=
\begin{pmatrix}
0&5/4\\
-5/9&0
\end{pmatrix}
\ne0.
\]

So the order effect is not a naming artifact.

The transformations genuinely do not commute.

This is the finite-dimensional version of a general warning:

> when operations do not commute, ordering is part of the system.

## 8. The product norm bound can be loose

The component norms give the generic upper bound

\[
\|BA\|_2
\le
\|B\|_2\|A\|_2
=
\frac94.
\]

But the exact composition is

\[
\|BA\|_2=1.
\]

The upper bound overestimates the actual gain.

For the reverse product,

\[
\|AB\|_2=\frac94,
\]

so the same generic bound is attained exactly.

This gives a useful pair of facts:

\[
\boxed{
\text{component norm ceilings provide a bound, not the exact composition.}
}
\]

and

\[
\boxed{
\text{relative alignment can make the bound either loose or sharp.}
}
\]

## 9. A commuting control

Now use

\[
A_c=
\operatorname{diag}(3/2,2/3),
\]

\[
B_c=
\operatorname{diag}(2/3,3/2).
\]

Each still has operator norm

\[
\frac32.
\]

But now

\[
[A_c,B_c]=0,
\]

and

\[
A_cB_c
=
B_cA_c
=
I.
\]

Therefore either order has gain

\[
\boxed{1.}
\]

This is the matched control.

The local component norm ceilings are unchanged.

What changed is the relationship between the transformations.

## 10. The lesson of the control

The witness and control have the same individual gain ceilings.

They do not have the same composition.

Therefore a component-local statement such as

\[
\|J_f\|\le L_f
\]

does not contain enough information to reconstruct the exact composed gain.

The interaction matters.

That interaction can involve:

- singular-vector alignment;
- cancellation;
- amplification;
- noncommutativity;
- invariant mismatch;
- domain escape.

The contract needs to say which of these matter for the downstream obligation.

## 11. Error budgets also compose

Gain is only one failure mode.

Approximation error is another.

Suppose \(\widehat f\) approximates \(f\) and \(\widehat g\) approximates \(g\).

Assume:

\[
\|\widehat f(x)-f(x)\|
\le
\varepsilon_f,
\]

and, on the connecting region,

\[
\|\widehat g(y)-g(y)\|
\le
\varepsilon_g.
\]

Suppose the true downstream map has Lipschitz bound

\[
\|g(y_1)-g(y_2)\|
\le
L_g\|y_1-y_2\|.
\]

Then:

\[
\begin{aligned}
\|\widehat g(\widehat f(x))-g(f(x))\|
&\le
\|\widehat g(\widehat f(x))-g(\widehat f(x))\|\\
&\quad+
\|g(\widehat f(x))-g(f(x))\|\\
&\le
\varepsilon_g+L_g\varepsilon_f.
\end{aligned}
\]

So

\[
\boxed{
E_{g\circ f}
\le
\varepsilon_g+L_g\varepsilon_f.
}
\]

The downstream stage amplifies the upstream error.

## 12. The connecting domain is load-bearing

The previous derivation quietly used an important assumption:

\[
\widehat f(x)
\]

must remain inside the region where the downstream bounds apply.

If upstream approximation error pushes the state outside that domain, then:

- the downstream Lipschitz bound may no longer hold;
- the downstream implementation error bound may no longer hold;
- the semantic interpretation may no longer be valid;
- an invariant may be violated.

This is exactly why a boundary contract needs more than a scalar error budget.

## 13. A finite error-budget failure

Take the scalar maps

\[
f(x)=x,
\]

\[
g(y)=\frac32y.
\]

Suppose the local implementation errors satisfy

\[
|\widehat f(x)-f(x)|
\le
\frac1{10},
\]

and

\[
|\widehat g(y)-g(y)|
\le
\frac1{10}.
\]

The downstream gain is

\[
L_g=\frac32.
\]

The derived composition guarantee is

\[
E
\le
\frac1{10}
+
\frac32\frac1{10}
=
\frac14.
\]

Suppose the system requirement is

\[
E\le\frac15.
\]

Each component-local error ceiling is only

\[
\frac1{10}.
\]

Yet the derived system guarantee is

\[
\frac14>\frac15.
\]

The local budgets pass individually. **The upper bound alone would show only that the system budget cannot yet be certified.** It would not prove that a particular implementation violates the requirement.

For this witness, we can exhibit an implementation attaining that bound. Choose

\[
\widehat f(x)=x+\frac1{10},
\qquad
\widehat g(y)=\frac32y+\frac1{10}.
\]

Each component has actual error exactly \(1/10\), on all real inputs, so the local contracts are satisfied. But

\[
\begin{aligned}
\widehat g(\widehat f(x))-g(f(x))
&=\frac32\left(x+\frac1{10}\right)+\frac1{10}-\frac32x\\
&=\frac14
>\frac15.
\end{aligned}
\]

Thus **this explicit composition actually fails** the system error requirement. The separate statement that the generic upper bound is insufficient for certification remains true when no particular implementations are supplied.

## 14. This is not the same as noncommutativity

The scalar error-budget witness has no interesting order effect.

Its failure comes from amplification and accumulation.

The matrix witness has a strong order effect.

Its failure comes from noncommutativity and alignment.

These are different failure mechanisms.

They should not be collapsed into one generic word such as instability.

## 15. Longer chains

Suppose a chain has stages

\[
f_1,f_2,\ldots,f_n.
\]

Let local approximation error at stage \(k\) be bounded by

\[
\varepsilon_k,
\]

and let the downstream true map at stage \(k\) have gain bound

\[
L_k
\]

on the connecting region.

If

\[
E_k
\le
L_kE_{k-1}+\varepsilon_k,
\]

with

\[
E_0=0,
\]

then induction gives

\[
\boxed{
E_n
\le
\sum_{j=1}^{n}
\varepsilon_j
\prod_{k=j+1}^{n}L_k.
}
\]

The formula makes one point visible:

> upstream error is weighted by every downstream gain that follows it.

## 16. Uniform local budgets can still grow badly

If every stage has

\[
L_k=L
\]

and

\[
\varepsilon_k=\varepsilon,
\]

then

\[
E_n
\le
\varepsilon
\sum_{r=0}^{n-1}L^r.
\]

If

\[
L=1,
\]

this becomes

\[
E_n\le n\varepsilon.
\]

If

\[
L>1,
\]

the worst-case bound grows geometrically:

\[
E_n
\le
\varepsilon
\frac{L^n-1}{L-1}.
\]

This does not mean the worst case is attained.

It means a local budget cannot be interpreted independently of chain depth and downstream gains.

## 17. Four levels of certificate

It helps to separate four evidence objects.

### Component certificate

A statement about one component.

For example:

\[
\|J_f(x_0)\|_2\le L_f.
\]

### Interface compatibility certificate

A statement that the upstream output satisfies the downstream assumptions.

For example:

\[
f(x_0)\in D_g.
\]

### Composition certificate

A derived statement about the combined map.

For example:

\[
\|J_g(f(x_0))J_f(x_0)\|
\le
L_gL_f.
\]

### System-level guarantee

A statement about the full reachable behavior of the assembled system.

For example:

> every reachable state satisfies the declared safety property.

These are not the same evidence level.

## 18. Local does not mean global

A local Jacobian bound at one point,

\[
\|J_f(x_0)\|\le L,
\]

does not imply that \(f\) is globally \(L\)-Lipschitz.

The derivative can be larger elsewhere.

The operating region can change.

The system can leave the region.

A global conclusion requires a bound over the relevant region and assumptions that connect those local bounds into a global result.

The audited Boundary Contracts chapter already enforced this firewall.

COMPOSE keeps it.

## 19. Interface compatibility is not system safety

Suppose every adjacent pair of modules is interface-compatible.

That can still be insufficient for a full system guarantee.

Why?

Because a global property can depend on:

- long-horizon accumulation;
- loops and feedback;
- reachable-state geometry;
- interaction between distant modules;
- stochasticity;
- adaptation;
- distribution shift;
- stateful memory.

Local compatibility is useful.

It is not magical.

## 20. Shape compatibility is the weakest case

The simplest failure is inherited from Boundary Contracts.

An upstream module can output a normalized direction.

A downstream module can interpret vector magnitude as meaningful amplitude.

The shapes match.

The semantics do not.

The software graph composes.

The intended mathematical object does not.

This is the most basic reason the contract must carry meaning.

## 21. Invariants can fail at the boundary

Suppose a downstream component assumes

\[
\|y\|=1.
\]

If the upstream component guarantees this exactly, the invariant composes.

If it guarantees only

\[
|\|y\|-1|\le\delta,
\]

the downstream theorem may or may not survive.

That depends on the downstream assumptions.

The phrase approximately normalized is not a complete contract.

It needs a tolerance and a theorem that knows what to do with that tolerance.

## 22. Semantic mismatch and numerical error can interact

A system can have both:

- a semantic mismatch;
- a numerical error budget.

A small numerical error does not repair a wrong semantic interpretation.

Likewise, semantically aligned modules can still violate a numerical budget.

The obligation classes remain separate because the remedies are different.

## 23. Order can change what the next module sees

In the exact matrix witness, \(B\) acts on a state already transformed by \(A\), or vice versa.

That is the point.

Sequential composition is not a bag of independent ingredients.

The second stage sees the result of the first.

This is why order is architectural information.

The Split-Operator chapter made the same point using exact flows and commutators [@McLachlanQuispel2002].

COMPOSE turns it into a contract-level system-budget question.

## 24. Classical splitting results stay bounded

The existence of an exact matrix witness does not make an arbitrary learned network an exact split flow.

A learned block can include:

- normalization;
- masking;
- stochasticity;
- routing;
- parameter variation;
- data-dependent control flow.

Classical Lie or Strang order only transfers when the required mathematical assumptions are actually established [@McLachlanQuispel2002; @HairerLubichWanner2006].

The chapter uses the mathematics as a reference system, not as a free theorem generator.

## 25. JVP/VJP probes remain local evidence

Boundary Contracts inherited JVP and VJP machinery [@BaydinEtAl2018].

These probes are useful for testing:

- directional gain;
- gradient transfer;
- dominant local sensitivity;
- interface alignment.

They still report local differential behavior.

A successful local probe does not certify a whole state space.

This is an evidence boundary, not a criticism of the probe.

## 26. Conditioning remains a separate question

A large observed error can come from:

- an ill-conditioned problem;
- an unstable implementation;
- upstream approximation error;
- downstream amplification;
- interface mismatch.

Numerical analysis keeps conditioning and algorithmic stability distinct [@Higham2002].

COMPOSE should do the same.

The goal is not merely to detect failure.

It is to identify which obligation failed.

## 27. Feedback changes the problem

So far the chapter has mostly discussed feed-forward composition:

\[
x\to f(x)\to g(f(x)).
\]

Now suppose the composed output is fed back:

\[
x_{t+1}
=
(g\circ f)(x_t).
\]

A one-pass composition certificate does not automatically answer:

- whether trajectories remain bounded;
- whether they converge;
- whether transient growth occurs;
- whether invariant sets survive;
- whether noise accumulates.

These are dynamical questions.

COMPOSE marks the boundary and stops.

A full closed-loop theorem would require additional dependencies and source authority.

## 28. Repeated local validity can still miss reachability

A component may be certified on an operating region

\[
D.
\]

If the composed system leaves \(D\), the certificate has expired.

This creates a subtle failure mode:

1. every local theorem is correct;
2. every theorem is scoped;
3. the assembled trajectory exits the scope;
4. the system becomes uncertified.

Nothing contradictory happened.

The composition argument failed to prove reachability containment.

## 29. Budget accounting should be explicit

A system contract should say which budget is being composed.

Examples include:

- perturbation gain;
- absolute numerical error;
- relative error;
- probability mass leakage;
- constraint violation;
- latency;
- memory;
- energy;
- uncertainty;
- privacy loss.

Different budgets obey different composition laws.

COMPOSE derives only the laws it states.

It does not assume every budget adds or multiplies in the same way.

## 30. Conservative bounds are not failures

The product norm bound

\[
\|J_gJ_f\|
\le
\|J_g\|\|J_f\|
\]

can be loose.

That does not make it wrong.

A conservative bound may still be useful for screening.

But if the conservative bound violates a threshold, one should not immediately conclude that the real composition violates it.

The exact \(BA\) witness demonstrates this:

\[
\|B\|\|A\|=\frac94,
\]

while

\[
\|BA\|=1.
\]

The right conclusion is:

> the coarse certificate is inconclusive for that threshold.

## 31. Tightness can be order-dependent

The reverse product \(AB\) reaches the full product bound:

\[
\|AB\|
=
\|A\|\|B\|
=
\frac94.
\]

So a conservative certificate can be loose in one ordering and exact in another.

That is a useful diagnostic fact.

It means a system designer should not treat component-local norm ceilings as a complete description of compositional geometry.

## 32. A practical composition protocol

For every boundary \(f\to g\), record:

1. operating domain;
2. semantic meaning of the connecting state;
3. invariants;
4. local sensitivity evidence;
5. numerical/error budget;
6. precision/unit convention;
7. downstream assumptions.

Then for the composition:

1. verify interface compatibility;
2. derive the composition rule for the relevant budget;
3. test order if operations may not commute;
4. compare the derived bound with the system budget;
5. check whether the composed state remains in the region where the local contracts apply;
6. use an exact or higher-fidelity computation when a conservative bound is inconclusive.

## 33. A practical order test

When two modules may be reordered, compare:

\[
g\circ f
\]

with

\[
f\circ g.
\]

Possible diagnostics include:

- exact finite witness;
- output difference;
- commutator in a declared linear reference model;
- Jacobian commutator as a local diagnostic;
- task-level difference.

Do not silently identify a same-state Jacobian commutator with the derivative of the full nonlinear composition defect.

That distinction is inherited from the audited Split chapter.

## 34. A practical error test

For a two-stage approximation, report:

\[
\varepsilon_f,
\qquad
\varepsilon_g,
\qquad
L_g,
\]

and the derived composition budget:

\[
\varepsilon_g+L_g\varepsilon_f.
\]

Also report the connecting domain on which those quantities are valid.

Without the domain, the number is incomplete.

## 35. A practical chain test

For a long chain, report the recurrence:

\[
E_k\le L_kE_{k-1}+\varepsilon_k.
\]

Do not only report the individual \(\varepsilon_k\).

The downstream gains determine how strongly early errors matter.

This is the composition analogue of keeping provenance attached to evidence.

## 36. What counts as catastrophe here?

The title is broader than any one metric.

A catastrophe can mean:

- a violated numerical tolerance;
- a broken invariant;
- a semantic mismatch;
- a system gain over budget;
- a state leaving the certified region;
- order-dependent behavior not represented in the design;
- accumulated error beyond specification.

The chapter does not define a universal catastrophe metric.

It requires the system-level obligation to be declared.

## 37. What this chapter proves

The exact finite witness proves:

\[
\|A\|=\|B\|=\frac32,
\]

\[
\|BA\|=1,
\]

\[
\|AB\|=\frac94.
\]

It proves that the same components pass a gain budget of \(2\) in one order and fail it in the reverse order.

The commuting control proves:

\[
A_cB_c=B_cA_c=I.
\]

The error derivation proves, under its assumptions:

\[
E_{g\circ f}
\le
\varepsilon_g+L_g\varepsilon_f.
\]

The chain derivation proves, under its assumptions:

\[
E_n
\le
\sum_{j=1}^{n}
\varepsilon_j
\prod_{k=j+1}^{n}L_k.
\]

These are the load-bearing results.

## 38. What this chapter does not prove

It does not prove:

\[
\text{all local contracts pass}
\Rightarrow
\text{global safety}.
\]

It does not prove that learned neural modules are exact flows.

It does not prove that a local Jacobian bound is a global Lipschitz theorem.

It does not prove that commuting linearizations imply globally commuting nonlinear maps.

It does not prove long-horizon stability.

It does not prove a universal contract calculus.

## 39. Non-implications

The chapter therefore rejects:

\[
\text{component contracts pass}
\not\Rightarrow
\text{system contract passes},
\]

\[
\|J_f(x_0)\|\le L
\not\Rightarrow
\text{global }L\text{-Lipschitz},
\]

\[
\|J_gJ_f\|\le\|J_g\|\|J_f\|
\not\Rightarrow
\text{tight estimate},
\]

\[
[A,B]=0\text{ in a reference model}
\not\Rightarrow
\text{learned modules commute globally},
\]

\[
\text{local error budget}
\not\Rightarrow
\text{long-horizon stability},
\]

and

\[
\text{interface compatibility}
\not\Rightarrow
\text{closed-loop safety}.
\]

## 40. Atlas connections

**Boundary Contracts.**  
COMPOSE consumes the obligation language and asks whether the guarantees actually survive assembly.

**Split-Operator Networks.**  
COMPOSE consumes order/noncommutativity discipline and turns it into explicit system-budget tests.

**Adaptive depth.**  
A variable-depth system changes the number of times local gain/error budgets compose.

**Routing and sparse systems.**  
Different routes induce different composition chains and therefore different contract obligations.

**Agents and tools.**  
A tool interface can be type-correct while semantically or numerically incompatible with the agent's assumptions.

**Governed adaptation.**  
A self-changing system must know which local contract changes invalidate downstream composition arguments.

## 41. Closing view

A component can be correct.

Another component can be correct.

Their composition can still be wrong.

Sometimes the problem is semantic.

Sometimes it is numerical.

Sometimes an error budget accumulates.

Sometimes a noncommuting order turns a harmless composition into an amplifying one.

Sometimes every local statement remains true while the system simply leaves the region where those statements apply.

The correct response is not to distrust modularity.

It is to make composition explicit. **A claim of safe composition requires a justified bridge from the local guarantees to the stated system-level obligation.** That bridge may require interface assumptions, error control, stability bounds, or a domain invariant. When the bridge is absent, local validity remains local.

## References used in this chapter

Inherited through audited prerequisites:

- [@Higham2002]
- [@BaydinEtAl2018]
- [@McLachlanQuispel2002]
- [@HairerLubichWanner2006]

Exact source identities and claim boundaries are recorded in sources/source-locks/ATLAS-CH-COMPOSE-001.yaml.
