# Neural Krylov Transport
<!-- ATLAS-CH-NEURALKRYLOV-001 -->

**Epistemic status:** audited classical Krylov/numerical-linear-algebra substrate + audited representation-transport substrate + Atlas-owned exact finite local-solve witnesses.  
**Specification:** manuscript/specifications/ATLAS-CH-NEURALKRYLOV-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-NEURALKRYLOV-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-NEURALKRYLOV-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-NEURALKRYLOV-001.yaml

A deep model already transports representations through a sequence of maps.

Sometimes a useful local computation can be posed as a linear correction problem:

\[
A_z\delta_z=b_z.
\]

That raises a natural question:

> can a model use a few operator-generated directions to compute a better representation correction without forming or solving a large dense system?

Classical Krylov methods provide one mathematical language for that question.

But the analogy is useful only if its boundaries remain visible.

The governing rule is:

\[
\boxed{
\text{declare the linear operator first; inherit no nonlinear convergence theorem by analogy.}
}
\]

## 1. What comes from classical Krylov theory

Krylov Subspaces and Iterative Solves already supplies:

- operator-generated trial spaces;
- Arnoldi/Lanczos vocabulary;
- projection and residual criteria;
- conditioning boundaries;
- left/right preconditioning semantics;
- matrix-free operator access;
- restart and finite-precision cautions.

Those objects remain classical linear algebra.

NEURALKRYLOV does not redefine them.

## 2. What comes from representation transport

Representation as Transport already gives a separate interface:

\[
z_{k+1}=\Phi_k(z_k).
\]

A representation is a state.

A stage is a declared map.

A local Jacobian can describe differential behavior near a base point.

But the Jacobian is not the global nonlinear map.

NEURALKRYLOV joins these two languages only through a declared local linear problem.

## 3. The local-solve interface

At state \(z\), suppose we define:

\[
A_z\delta_z=b_z.
\]

The operator \(A_z\) might be:

- a local Jacobian-derived map;
- a normal-equation operator;
- a Hessian-like approximation;
- a learned linear surrogate;
- another explicitly declared linear operator.

Nothing in the phrase “Neural Krylov” identifies \(A_z\) automatically.

The operator must be named.

## 4. The representation update is separate

Once an approximate correction:

\[
\delta_z^{(m)}
\]

has been computed, a representation block might apply:

\[
z^+=\Phi(z,\delta_z^{(m)}).
\]

The local solve and the representation update are different maps.

A good local solve does not automatically imply:

- a good representation;
- a stable global trajectory;
- a better task score.

Those are separate tests.

## 5. A fixed left-preconditioned exact witness

Use the local system:

\[
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

The exact solution is:

\[
x^\star=
\begin{pmatrix}
1\\1/4
\end{pmatrix}.
\]

Introduce fixed left preconditioner:

\[
M=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix}.
\]

Then:

\[
M^{-1}A=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\]

and:

\[
M^{-1}b=
\begin{pmatrix}
1\\1/2
\end{pmatrix}.
\]

Write:

\[
B=M^{-1}A,
\qquad
c=M^{-1}b.
\]

## 6. Why the preconditioner matters

The Krylov process now sees:

\[
Bx=c.
\]

That is not merely “the same system with faster convergence.”

It is a transformed system with a transformed residual.

The original residual remains:

\[
r=b-Ax.
\]

The transformed residual is:

\[
\widehat r=c-Bx=M^{-1}r.
\]

These are different numerical objects.

## 7. One operator-generated direction

With:

\[
x_0=0,
\]

the first Krylov space is:

\[
\mathcal K_1(B,c)=\operatorname{span}\{c\}.
\]

So every candidate has form:

\[
x=\alpha c.
\]

The best transformed-residual coefficient is:

\[
\boxed{
\alpha=\frac34.
}
\]

Hence:

\[
x_1=
\begin{pmatrix}
3/4\\
3/8
\end{pmatrix}.
\]

## 8. The transformed residual is nonzero

For \(x_1\):

\[
\widehat r_1
=
\begin{pmatrix}
1/4\\
-1/4
\end{pmatrix}.
\]

Thus:

\[
\boxed{
\|\widehat r_1\|_2^2=\frac18.
}
\]

The best one-dimensional trial-space point is still not the exact solve.

## 9. The original residual is different

The original-system residual is:

\[
r_1
=
\begin{pmatrix}
1/4\\
-1/2
\end{pmatrix}.
\]

Thus:

\[
\boxed{
\|r_1\|_2^2=\frac5{16}.
}
\]

The same iterate has two different residual norms depending on which system we evaluate.

This is not a contradiction.

It is preconditioning semantics.

## 10. The true error is another object

The true error is:

\[
e_1=x^\star-x_1
=
\begin{pmatrix}
1/4\\
-1/8
\end{pmatrix}.
\]

Hence:

\[
\boxed{
\|e_1\|_2^2=\frac5{64}.
}
\]

Now we already have three different quantities:

\[
\frac18,
\qquad
\frac5{16},
\qquad
\frac5{64}.
\]

They answer different questions.

## 11. One more direction changes everything in this toy

Compute:

\[
Bc=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

The two generated directions are:

\[
c=
\begin{pmatrix}
1\\1/2
\end{pmatrix},
\qquad
Bc=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Their determinant is:

\[
\boxed{\frac12}.
\]

Therefore:

\[
\boxed{
\mathcal K_2(B,c)=\mathbb R^2.
}
\]

## 12. The exact solution is in the second Krylov space

Indeed:

\[
\boxed{
x^\star
=
\frac32c-\frac12Bc.
}
\]

So an exact residual-minimizing solve in \(\mathcal K_2\) can recover:

\[
x^\star.
\]

Then:

\[
\widehat r_2=0,
\qquad
r_2=0,
\qquad
e_2=0.
\]

## 13. What the positive witness actually shows

It shows one finite fact:

> for this declared operator, right-hand side, and preconditioner, one generated direction is insufficient while two are sufficient.

That is a useful architecture motif.

It is not:

- a rate theorem;
- a dimension-independent guarantee;
- evidence that every neural representation has a two-step Krylov structure.

## 14. Short horizon can be computationally meaningful

The representation-computation idea is not necessarily to solve a large system to machine precision.

It may instead be:

- generate a few directions;
- project a local problem;
- obtain a useful correction;
- stop because compute is bounded.

This makes horizon \(m\) an architectural resource.

But “small \(m\)” is not itself a quality certificate.

## 15. A low-dimensional failure control

Consider:

\[
B_{\rm bad}
=
\begin{pmatrix}
1&0\\
0&10
\end{pmatrix},
\qquad
c_{\rm bad}
=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Again:

\[
\mathcal K_1
=
\operatorname{span}\{c_{\rm bad}\}.
\]

The trial space is one-dimensional.

## 16. The best one-dimensional residual can still be poor

The exact minimum-residual scalar is:

\[
\alpha_{\rm bad}
=
\frac{11}{101}.
\]

The residual becomes:

\[
r_{\rm bad}
=
\begin{pmatrix}
90/101\\
-9/101
\end{pmatrix}.
\]

Therefore:

\[
\boxed{
\|r_{\rm bad}\|_2^2
=
\frac{81}{101}.
}
\]

That is large.

## 17. Dimension is not convergence

Both positive and bad controls use a one-dimensional first trial space.

One gives a moderate approximation.

The other leaves a large residual.

Thus:

\[
\boxed{
\text{small trial-space dimension}
\not\Rightarrow
\text{small residual}.
}
\]

The operator geometry matters.

## 18. Conditioning and spectral structure still matter

KRYLOV already established that convergence can depend on:

- spectrum;
- field of values;
- non-normality;
- right-hand side;
- polynomial approximation;
- preconditioning;
- finite precision.

A neural implementation does not make those dependencies disappear.

It may change the operator.

Then the analysis must change with it.

## 19. Task quality can disagree with solve quality

Now define downstream readout:

\[
w=
\begin{pmatrix}
1\\2
\end{pmatrix}.
\]

For the exact solution:

\[
w^\top x^\star=\frac32.
\]

For the non-exact one-step iterate:

\[
w^\top x_1=\frac32.
\]

So:

\[
\boxed{
w^\top x_1=w^\top x^\star.
}
\]

## 20. Yet the one-step solve is still wrong

At the same time:

\[
r_1\neq0,
\]

and:

\[
e_1\neq0.
\]

So the downstream scalar is exact even though the local solve is not.

Therefore:

\[
\boxed{
\text{exact task readout}
\not\Rightarrow
\text{exact solve}.
}
\]

This is a minimal but important metric firewall.

## 21. The converse also needs proof

A smaller residual does not automatically imply a better task metric.

A downstream task may:

- ignore the corrected direction;
- amplify a tiny error direction;
- saturate;
- threshold;
- use a nonlinear readout.

Therefore solve quality and task quality must be evaluated separately.

## 22. Representation quality is another layer

Suppose \(x\) becomes a representation correction.

One can measure:

- Euclidean correction error;
- angular error;
- constraint violation;
- retained information;
- probe separability;
- downstream task score.

None equals:

\[
\|b-Ax\|
\]

by definition.

A chapter that reports only residual has not yet measured representation quality.

## 23. The local Jacobian bridge

Suppose a representation map is:

\[
z^+=\Phi(z).
\]

At base point \(z_0\), a local differential object is:

\[
J_\Phi(z_0).
\]

A local correction operator might be declared as:

\[
A_{z_0}=I-J_\Phi(z_0).
\]

Then a Krylov method can be built for \(A_{z_0}\).

But that is a Krylov problem for a local linear operator.

It is not a Krylov method for the entire nonlinear \(\Phi\).

## 24. Local Jacobian is not global transport

If the representation moves to \(z_1\), then:

\[
J_\Phi(z_1)
\]

can differ from:

\[
J_\Phi(z_0).
\]

If the operator changes at each stage, a sequence of generated directions is not automatically:

\[
r,Ar,A^2r,\ldots
\]

for one fixed \(A\).

The classical object has changed.

## 25. Learned preconditioners make the distinction sharper

Suppose:

\[
M=M_\theta(z).
\]

Then the preconditioner may depend on:

- state;
- layer;
- input;
- training parameters.

A learned preconditioner can be a useful architecture.

But it is not automatically the fixed linear \(M\) of classical theory.

Any guarantee must match the actual semantics.

## 26. Fixed left versus right versus flexible

The exact witness is fixed left preconditioning:

\[
M^{-1}Ax=M^{-1}b.
\]

Right preconditioning would instead change variables.

Flexible preconditioning can use different preconditioners across iterations.

Nonlinear preconditioning changes the mathematical problem further.

The word “preconditioned” is insufficient without the type.

## 27. Matrix-free access fits the architecture

A neural system may never materialize:

\[
A_z.
\]

It may expose only:

\[
v\mapsto A_zv.
\]

For Jacobian-derived operators, this can be implemented by JVP/VJP-style primitives.

That is compatible with classical operator-action semantics.

But the operator is still conceptually defined.

## 28. Matrix-free does not mean operator-free

The fact that a matrix is not explicitly stored does not license an undefined operator.

For every Krylov claim, one should be able to answer:

> what map is being applied to the vector?

Without that answer, the subspace claim is underspecified.

## 29. Residual and error need conditioning

For an invertible linear problem:

\[
Ae=r.
\]

Therefore:

\[
e=A^{-1}r.
\]

Bounds such as:

\[
\|e\|
\le
\|A^{-1}\|\|r\|
\]

depend on the operator.

Residual is observable from \(A,b,x\).

True error requires the exact solution or a certificate.

They are not interchangeable.

## 30. Preconditioned residual adds another layer

Under left preconditioning:

\[
\widehat r=M^{-1}r.
\]

A solver can minimize:

\[
\|\widehat r\|
\]

while the application ultimately cares about:

\[
\|r\|.
\]

Sometimes this is exactly the intended geometry.

Sometimes it is not.

The distinction should be explicit.

## 31. Finite precision still exists inside neural systems

If a block explicitly constructs orthogonal or nearly orthogonal operator-generated directions, finite precision matters.

Possible failures include:

- loss of orthogonality;
- direction collapse;
- residual-estimate drift;
- numerical dependence.

A learned implementation is still numerical computation.

## 32. Restarting and truncation are architectural choices

A bounded-compute Neural Krylov block may stop after \(m\) directions.

It may also restart.

This controls:

- memory;
- latency;
- operator calls.

But it can throw away useful subspace information.

The exact positive witness already shows:

\[
m=1
\]

misses the exact solution, while:

\[
m=2
\]

captures it.

## 33. A Neural Krylov block as an interface

A bounded block can be specified as:

1. receive \(z\);
2. define \(A_z\);
3. define \(b_z\);
4. define preconditioner \(M_z\), if used;
5. generate at most \(m\) directions;
6. solve or project in the trial space;
7. return correction \(\delta_z^{(m)}\);
8. update representation;
9. expose diagnostics.

This is a precise architecture description.

## 34. Diagnostics should remain plural

A serious implementation should report, where available:

- transformed residual;
- original residual;
- estimated/known solve error;
- representation change;
- constraint violation;
- downstream task metric;
- operator/preconditioner condition diagnostics.

One scalar should not impersonate all of them.

## 35. The right empirical question

The most useful empirical question is not:

> does this architecture “look like Krylov”?

It is:

> for the exact operator and preconditioner declared by the architecture, what does the short generated subspace buy us relative to a matched compute baseline?

That question can be falsified.

## 36. The right theoretical question

For a learned architecture, the theoretical burden is:

- identify the operator family;
- identify whether it is fixed or state-dependent;
- identify the projection criterion;
- identify the preconditioner class;
- control nonlinearity/state drift;
- state finite-precision assumptions;
- connect solve quality to representation/task quality only with an explicit theorem.

Without these, classical convergence is only an analogy.

## 37. Non-implications

NEURALKRYLOV rejects:

\[
\text{low subspace dimension}
\not\Rightarrow
\text{small residual},
\]

\[
\text{small residual}
\not\Rightarrow
\text{small true error without conditioning information},
\]

\[
\text{small solve error}
\not\Rightarrow
\text{good representation/task quality},
\]

\[
\text{exact task readout}
\not\Rightarrow
\text{exact solve},
\]

\[
\text{local Jacobian Krylov step}
\not\Rightarrow
\text{global nonlinear convergence},
\]

\[
\text{representation transport}
\not\Rightarrow
\text{Krylov convergence theorem},
\]

and:

\[
\text{learned preconditioner}
\not\Rightarrow
\text{fixed-linear preconditioner guarantees}.
\]

## 38. Atlas connections

**Krylov Subspaces and Iterative Solves.**  
Supplies the exact linear-algebra vocabulary and limits.

**Representation as Transport.**  
Supplies the state-map/local-Jacobian interface while blocking ODE/geodesic/Krylov overclaims.

**Adaptive depth.**  
A future controller can treat horizon \(m\) as adaptive compute, but must justify its stopping signal.

**Boundary probes.**  
JVP/VJP and sensitivity machinery can expose matrix-free local operator actions.

**Systems.**  
Short-horizon iterative representation computation creates explicit operator-call, memory, and latency tradeoffs.

## 39. Closing view

Neural Krylov Transport is not the claim that neural networks secretly run GMRES.

Its **disciplined architecture pattern** begins with a declared local linear operator, constructs a few operator-generated directions, applies a declared projection, and uses the result for a declared representation update. This is a sequence of typed operations, not an algebraic sum or a general convergence theorem.

The finite witness shows why this can matter.

One direction leaves nonzero residual and error.

Two directions recover the exact local solution.

A separate one-dimensional control remains poor.

And an exact downstream readout can coexist with a non-exact solve.

So the durable lesson is not “Krylov always works.”

**Short-horizon operator-generated computation can be useful, but its guarantees depend on the declared operator, metric, preconditioner, and interface.** This chapter's exact finite witnesses demonstrate that restricted statement; they do not establish a general convergence theorem for a learned nonlinear transport mechanism.

## References used in this chapter

No new external academic authority is added.

Classical numerical-linear-algebra authority is inherited through audited ATLAS-CH-KRYLOV-001.

Representation-transport authority is inherited through audited ATLAS-CH-TRANSPORT-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-NEURALKRYLOV-001.yaml
