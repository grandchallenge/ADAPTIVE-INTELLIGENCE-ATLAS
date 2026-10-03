# Discretization, Stability, and Splitting
<!-- ATLAS-CH-NUMERICS-001 -->

**Epistemic status:** Established Numerical Analysis + Atlas Derivation + Atlas Interpretation  
**Specification:** manuscript/specifications/ATLAS-CH-NUMERICS-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-NUMERICS-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-NUMERICS-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-NUMERICS-001.yaml

## 1. The computation that runs is not the exact flow

The Dynamics chapter gave us an exact evolution law.

For

\[
\dot x=f(x),
\]

the exact time-\(h\) flow is

\[
\Phi_h.
\]

A computer usually does not apply \(\Phi_h\) exactly.

It applies an update rule

\[
\Psi_h.
\]

That distinction is the beginning of numerical analysis:

\[
\boxed{
\text{mathematical evolution}
\neq
\text{numerical evolution}
}
\]

unless equality has been proved.

A numerical method does not merely produce an approximate answer.

It creates its own discrete dynamical system.

That system can have:

- different stability;
- different fixed points;
- different invariants;
- different long-time geometry;
- different failure modes.

This is why numerical analysis becomes a language for neural computation.

A layer, solver step, optimizer step, or routing update is not merely “close to” an abstract process.

It is the process the machine actually executes.

## 2. Road versus stepping stones

A useful allegory is a road and stepping stones.

The exact flow is the road.

A numerical method lays down stones.

The correspondence is:

- exact flow:
  the continuous route prescribed by the differential equation;
- numerical update:
  the rule for choosing the next stone;
- step size:
  spacing between stones;
- local error:
  how far one new stone misses the road when starting exactly on it;
- global error:
  how far repeated stepping drifts after many steps;
- stability region:
  the set of mode/step combinations for which repeated stepping behaves acceptably.

The limit matters.

A numerical method is not merely a lower-resolution drawing of the road.

The stepping-stone sequence is a different discrete system.

It can leave the road entirely.

## 3. One-step methods

Suppose

\[
x_n
\]

approximates the exact state at time

\[
t_n.
\]

A one-step method has form

\[
\boxed{
x_{n+1}
=
\Psi_h(x_n).
}
\]

The exact sampled state satisfies

\[
x(t_{n+1})
=
\Phi_h(x(t_n)).
\]

The two maps have different roles:

\[
\Phi_h:
\text{exact transport},
\]

\[
\Psi_h:
\text{implemented update}.
\]

The purpose of analysis is to understand when repeated use of \(\Psi_h\) reproduces the aspects of \(\Phi_h\) we care about.

## 4. Explicit Euler

Taylor expansion gives

\[
x(t+h)
=
x(t)
+
h f(x(t))
+
O(h^2).
\]

Dropping the remainder yields

\[
\boxed{
x_{n+1}
=
x_n+h f(x_n).
}
\]

This is explicit Euler.

Its appeal is obvious:

- one vector-field evaluation;
- no equation solve;
- simple memory footprint;
- simple interpretation.

Its weaknesses are equally important:

- first-order accuracy;
- restricted stability region;
- poor behavior on stiff systems;
- no generic preservation of geometric structure.

Simple does not mean benign.

## 5. Implicit Euler

Implicit Euler uses

\[
\boxed{
x_{n+1}
=
x_n+h f(x_{n+1}).
}
\]

Now the unknown future state appears inside the vector field.

Each step can require solving an equation.

This is more expensive.

It also changes the stability geometry dramatically.

The trade is characteristic of numerical computation:

> more work per step can buy qualitatively different admissible step sizes.

Implicit does not mean automatically more accurate.

It means the method is defined by a different update relation.

## 6. Local error

Let

\[
y_n=x(t_n)
\]

be the exact sampled state.

Insert the exact state into the numerical rule.

Define the one-step defect:

\[
d_{n+1}
=
\Phi_h(y_n)
-
\Psi_h(y_n).
\]

If

\[
\|d_{n+1}\|
\le
K h^{p+1},
\]

we say the local defect is order

\[
O(h^{p+1}).
\]

This asks:

> If we start one step exactly on the true trajectory, how much does the numerical rule miss after that one step?

It does not yet answer how errors accumulate.

## 7. Global error

The global error is

\[
e_n
=
y_n-x_n.
\]

Now previous numerical mistakes feed into later steps.

Suppose the numerical map obeys

\[
\|\Psi_h(u)-\Psi_h(v)\|
\le
(1+Ch)\|u-v\|.
\]

Then

\[
\|e_{n+1}\|
\le
K h^{p+1}
+
(1+Ch)\|e_n\|.
\]

Over a fixed interval

\[
nh\le T,
\]

a discrete Grönwall estimate yields

\[
\|e_n\|
=
O(h^p)
\]

under the declared regularity and stability assumptions.

This is the standard reason a local defect of order \(p+1\) can produce global order \(p\).

The statement is conditional.

Consistency by itself is not a universal convergence theorem.

## 8. The scalar test equation

A large fraction of numerical stability theory begins with

\[
\boxed{
y'=\lambda y.
}
\]

The exact solution over one step is

\[
y(t+h)
=
e^{h\lambda}y(t).
\]

Define

\[
z=h\lambda.
\]

Then the exact amplification factor is

\[
R_{\rm exact}(z)=e^z.
\]

A numerical method applied to this equation has form

\[
y_{n+1}
=
R(z)y_n.
\]

This scalar function

\[
R(z)
\]

compresses the method's linear amplification behavior.

## 9. Absolute stability

For a mode that should decay, we want repeated numerical amplification not to grow.

Absolute stability requires

\[
\boxed{
|R(z)|<1.
}
\]

The set of \(z\) satisfying this condition is the method's absolute-stability region.

This is not the same concept as Lyapunov stability of a nonlinear dynamical system.

It is a property of the numerical method applied to the scalar test equation.

The word "stability" must carry its qualifier.

## 10. Explicit Euler amplification

For explicit Euler,

\[
y_{n+1}
=
y_n+h\lambda y_n.
\]

Therefore

\[
\boxed{
R_E(z)=1+z.
}
\]

Absolute stability requires

\[
|1+z|<1.
\]

Geometrically this is the disk centered at

\[
-1
\]

with radius

\[
1.
\]

On the negative real axis:

\[
-2<z<0.
\]

If

\[
\lambda<0,
\]

we obtain

\[
\boxed{
0<h<\frac{2}{|\lambda|}.
}
\]

A perfectly stable continuous decay mode can therefore become an unstable discrete mode if the step is too large.

## 11. Implicit Euler amplification

Implicit Euler gives

\[
y_{n+1}
=
y_n+h\lambda y_{n+1}.
\]

Thus

\[
(1-z)y_{n+1}=y_n,
\]

so

\[
\boxed{
R_I(z)
=
\frac{1}{1-z}.
}
\]

Let

\[
z=x+iy
\]

with

\[
x<0.
\]

Then

\[
|1-z|^2
=
(1-x)^2+y^2
>
1.
\]

Hence

\[
|R_I(z)|<1.
\]

The entire open left half-plane is absolutely stable.

Implicit Euler is A-stable.

## 12. The stability geometry is computational geometry

The stability region is not decoration.

It tells us which combinations of:

- system eigenvalue;
- step size;
- numerical rule;

produce decaying numerical modes.

The same continuous mode

\[
\lambda
\]

can be harmless for one method and disastrous for another.

This is why "the system is stable" is not enough when the computation uses discrete steps.

We must ask:

> stable under which update?

![A three-panel numerical plate showing Euler absolute-stability geometry, the stiff fast-mode behavior at h=0.03, and log-log local splitting defects for Lie and Strang compositions.](../../figures/masters/ATLAS-FIG-NUMERICS-001.png)

## 13. Consistency of explicit Euler

The exact scalar amplification is

\[
e^z
=
1+z+\frac{z^2}{2}
+\frac{z^3}{6}
+\cdots.
\]

Explicit Euler uses

\[
1+z.
\]

Therefore

\[
e^z-(1+z)
=
\frac{z^2}{2}
+
O(z^3).
\]

With

\[
z=h\lambda,
\]

the one-step amplification defect is

\[
O(h^2).
\]

Under the standard finite-time stability assumptions, explicit Euler is globally first order.

This is an accuracy statement.

It says nothing by itself about whether a chosen step lies inside the stability region.

## 14. Stability and accuracy are different questions

Suppose a method is stable.

It can still be inaccurate.

Suppose a method is high order.

It can still be unstable at the chosen step size.

Two separate questions are therefore required:

1. Does the numerical mode remain controlled?
2. Does it approximate the correct mode well enough?

The stiff calibration system makes the difference visible.

## 15. A stiff two-timescale system

Consider

\[
\dot x
=
\begin{pmatrix}
-1&0\\
0&-100
\end{pmatrix}
x.
\]

The exact modes decay as

\[
e^{-t}
\]

and

\[
e^{-100t}.
\]

The system contains two very different timescales:

\[
\tau_{\rm slow}=1,
\]

and

\[
\tau_{\rm fast}=0.01.
\]

The fast mode disappears quickly.

Yet it can dictate the step size of an explicit method.

## 16. Explicit Euler on the stiff system

The modal amplification factors are

\[
R_{\rm slow}=1-h,
\]

and

\[
R_{\rm fast}=1-100h.
\]

The fast mode requires

\[
|1-100h|<1.
\]

Therefore

\[
0<h<0.02.
\]

Now choose

\[
h=0.03.
\]

The slow mode gives

\[
R_{\rm slow}=0.97.
\]

That looks harmless.

The fast mode gives

\[
\boxed{
R_{\rm fast}=-2.
}
\]

The exact fast mode decays by

\[
e^{-3}
\approx
0.049787.
\]

The numerical fast mode doubles in magnitude and flips sign.

The computation invents instability.

## 17. Implicit Euler on the same system

At

\[
h=0.03,
\]

implicit Euler gives

\[
R_{\rm slow}
=
\frac{1}{1.03}
\approx
0.970874,
\]

and

\[
\boxed{
R_{\rm fast}
=
\frac14.
}
\]

The fast mode now decays numerically.

The step is stable.

But the exact fast amplification is

\[
e^{-3}
\approx
0.049787.
\]

The numerical factor

\[
0.25
\]

is much larger.

The fast transient is heavily misrepresented.

This is the chapter's simplest demonstration that:

\[
\boxed{
\text{stable}
\neq
\text{accurate}.
}
\]

## 18. What stiffness means here

Stiffness is not simply:

> one derivative is large.

The useful numerical idea is that the dynamics contain fast stable modes that impose severe explicit stability restrictions even when the behavior of interest evolves much more slowly [@HairerWanner1996].

The problem is relational:

- a system;
- a method;
- a tolerance;
- a timescale of interest.

Different formal definitions of stiffness exist.

The Atlas will state the operational context rather than pretend one scalar captures every case.

## 19. Implicitness is not free

Implicit Euler's larger stability region comes at a price.

For nonlinear \(f\), each step solves

\[
x_{n+1}
-
h f(x_{n+1})
=
x_n.
\]

This can require:

- Newton iterations;
- Jacobian solves;
- preconditioners;
- stopping criteria.

The update can therefore be more stable and more expensive.

This trade will reappear later in:

- implicit neural layers;
- equilibrium models;
- learned solvers;
- Krylov acceleration.

Numerical structure and systems cost are inseparable.

## 20. Structure preservation

Accuracy at one short horizon is not the only objective.

A numerical method can also be judged by whether it preserves important structure.

Possible targets include:

- invariants;
- monotonicity;
- reversibility;
- positivity;
- symplectic form;
- constraints;
- conserved mass.

The Dynamics chapter introduced exact Hamiltonian structure.

Numerics now asks what a discrete update does to it.

## 21. Explicit Euler on the harmonic oscillator

For

\[
\dot q=p,
\qquad
\dot p=-q,
\]

explicit Euler gives

\[
\begin{pmatrix}
q_{n+1}\\
p_{n+1}
\end{pmatrix}
=
M_E
\begin{pmatrix}
q_n\\
p_n
\end{pmatrix},
\]

with

\[
M_E
=
\begin{pmatrix}
1&h\\
-h&1
\end{pmatrix}.
\]

Its determinant is

\[
\boxed{
\det M_E=1+h^2.
}
\]

For any nonzero \(h\),

\[
\det M_E>1.
\]

The exact oscillator flow preserves phase-space area.

Explicit Euler expands it.

## 22. Symplectic Euler

Use the update order

\[
p_{n+1}
=
p_n-hq_n,
\]

then

\[
q_{n+1}
=
q_n+h p_{n+1}.
\]

The update matrix is

\[
M_{SE}
=
\begin{pmatrix}
1-h^2&h\\
-h&1
\end{pmatrix}.
\]

Its determinant is

\[
1.
\]

More strongly, with

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

the exact witness gives

\[
\boxed{
M_{SE}^\top J M_{SE}=J.
}
\]

The discrete map is symplectic.

## 23. Symplectic does not mean exact-energy conserving

Start from

\[
(q_0,p_0)=(1,0).
\]

One symplectic-Euler step gives

\[
p_1=-h,
\]

\[
q_1=1-h^2.
\]

The exact oscillator energy begins at

\[
H_0=\frac12.
\]

After the step,

\[
H_1
=
\frac12
\left[
(1-h^2)^2+h^2
\right].
\]

Therefore

\[
H_1-H_0
=
\frac12(-h^2+h^4).
\]

This is generically nonzero.

So:

\[
\boxed{
\text{symplectic}
\not\Rightarrow
\text{exact energy preservation}.
}
\]

The preserved structure is the symplectic form.

That can still matter enormously for long-time behavior [@HairerLubichWanner2006].

## 24. Splitting a difficult generator

Suppose an evolution law decomposes into two parts:

\[
A+B.
\]

Maybe:

- each part is easier to solve;
- each part preserves a different structure;
- each part is sparse;
- each part acts on different variables.

The exact linear flow is

\[
e^{h(A+B)}.
\]

If

\[
e^{hA}
\]

and

\[
e^{hB}
\]

are individually easy, composition becomes attractive.

This is operator splitting.

## 25. Lie-Trotter splitting

The simplest composition is

\[
\boxed{
\Psi_h^{LT}
=
e^{hA}e^{hB}.
}
\]

If

\[
A
\]

and

\[
B
\]

commute,

\[
[A,B]=0,
\]

then

\[
\boxed{
e^{h(A+B)}
=
e^{hA}e^{hB}.
}
\]

The split step is exact.

If the operators do not commute, order matters.

## 26. The commutator

Define

\[
\boxed{
[A,B]
=
AB-BA.
}
\]

The commutator measures the failure of interchangeability.

If

\[
[A,B]=0,
\]

then applying \(A\) then \(B\) agrees with applying \(B\) then \(A\) at the relevant algebraic level.

If

\[
[A,B]\neq0,
\]

composition order leaves a trace.

That trace becomes the leading splitting error.

This will later connect numerical splitting to Atlas diagnostics of coupled modules and operators.

## 27. Exact noncommuting witness

Take

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

and

\[
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Both satisfy

\[
A^2=B^2=0.
\]

Their commutator is

\[
\boxed{
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
}
\]

The components are as simple as possible.

Their composition is not.

## 28. Lie defect

Because the matrices are nilpotent,

\[
e^{hA}=I+hA,
\]

and

\[
e^{hB}=I+hB.
\]

Therefore

\[
e^{hA}e^{hB}
=
I+h(A+B)+h^2AB.
\]

The exact flow expands as

\[
e^{h(A+B)}
=
I+h(A+B)
+
\frac{h^2}{2}(A+B)^2
+
O(h^3).
\]

Since

\[
(A+B)^2=AB+BA,
\]

the leading difference is

\[
\boxed{
e^{hA}e^{hB}
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3).
}
\]

The commutator is not merely a diagnostic metaphor.

It appears directly in the composition error.

## 29. Strang splitting

A symmetric composition is

\[
\boxed{
\Psi_h^S
=
e^{hA/2}
e^{hB}
e^{hA/2}.
}
\]

For the exact witness, symbolic expansion gives no \(O(h^2)\) defect.

The leading defect begins at

\[
O(h^3).
\]

The computational witness gives

\[
\Psi_h^S-e^{h(A+B)}
=
h^3
\begin{pmatrix}
0&1/12\\
-1/6&0
\end{pmatrix}
+
O(h^4).
\]

Under the standard repeated-step assumptions, this yields second-order global accuracy.

Symmetry has canceled the leading asymmetric error.

## 30. Why splitting is useful

Splitting lets us combine subflows whose individual properties we understand.

Examples can include:

- transport plus reaction;
- kinetic plus potential flow;
- local plus communication operators;
- reversible plus dissipative pieces;
- sparse computational modules.

But composition is not free.

When operators do not commute, the order matters.

The split method approximates the combined generator rather than simply reproducing it.

## 31. Adaptive step size

A fixed step size assumes one resolution works everywhere.

That can be wasteful or unsafe.

Adaptive methods estimate local error and adjust \(h\).

A generic loop is:

1. propose a step;
2. estimate local defect;
3. accept or reject;
4. enlarge or shrink \(h\);
5. continue.

This is numerical resource allocation.

Later Atlas chapters will ask whether computational depth can be controlled in the same spirit.

The present chapter does not yet define a learned depth policy.

## 32. Numerical depth

If each layer behaves like a step,

\[
x_{k+1}
=
\Psi_{h_k}(x_k),
\]

then depth is not merely architecture size.

It is also the number of updates used to approximate or realize a transformation.

This viewpoint suggests questions such as:

- Is a region dynamically easy enough for a large step?
- Does instability require smaller steps?
- Can local error estimate computational depth?
- Can two operators be split to reduce per-step complexity?

These are Atlas interpretations.

The numerical mathematics itself remains the standard substrate.

## 33. Residual blocks as steps

A residual block has form

\[
x_{k+1}
=
x_k+F_k(x_k).
\]

If we write

\[
F_k(x)
=
h f_k(x),
\]

the update resembles explicit Euler.

That resemblance is useful.

It is not an identity with one autonomous ODE unless stronger structure is present.

The layer function can vary with \(k\).

Normalization, attention, routing, and learned parameters can all change the interpretation.

The correct statement is often:

> the block admits an integrator lens.

Not:

> the block is literally Euler integration of a fixed ODE.

## 34. Stability regions as architectural warnings

Suppose a learned update has a local linear mode with eigenvalue

\[
\lambda.
\]

A residual coefficient or effective step size can place

\[
h\lambda
\]

inside or outside a method-like stability region.

This can provide a useful diagnostic.

It does not automatically prove that the nonlinear architecture is governed by the scalar test equation.

The scalar analysis is a local warning system.

The full model requires its own argument.

## 35. Stiffness as computational imbalance

Stiffness offers another useful Atlas lens.

If one part of the state evolves on a very fast stable timescale while another evolves slowly, an explicit architecture may be forced to use many small steps because of the fast component.

Possible responses include:

- implicit updates;
- preconditioning;
- splitting;
- multiscale treatment;
- adaptive stepping;
- reparameterization.

This is exactly why the Atlas places numerical analysis upstream of adaptive depth and Neural Krylov Transport.

## 36. Step size is part of the algorithm

A numerical method is not fully specified by the update family alone.

The step size matters.

For explicit Euler on

\[
y'=\lambda y,
\]

the same method can be:

- stable;
- unstable;
- accurate;
- inaccurate;

depending on

\[
h\lambda.
\]

This is a useful antidote to method labels.

Saying "we use Euler" is not enough.

Saying "we use residual updates" is not enough.

Scale matters.

## 37. Stability terminology must remain qualified

The Atlas will use at least three distinct notions.

### Dynamical stability

A property of the underlying system.

### Absolute stability

A property of a numerical method applied to the scalar test equation.

### Algorithmic or backward stability

A property of how numerical perturbations affect a computation and whether the computed result corresponds to a nearby problem [@Higham2002].

These concepts interact.

They are not interchangeable.

## 38. Five failure modes

### Exact flow conflated with update rule

A discretization is treated as if it inherits every property of the continuous system.

### Stable conflated with accurate

An implicit method damps the right mode but at the wrong rate.

### High order conflated with safe step size

Formal accuracy is used outside the method's stability regime.

### Determinant one conflated with symplecticity

Volume preservation is treated as sufficient geometric structure in arbitrary dimension.

### Splitting order ignored

Noncommuting subflows are rearranged as though composition order were irrelevant.

## 39. Atlas connections

**Dynamics.**  
Numerics starts from exact flow and asks what computation preserves.

**Adaptive depth.**  
Step-size control becomes a prototype for computational-depth control.

**Split operators.**  
Lie-Trotter and Strang provide the mathematical substrate for SPINDLE-style computation.

**Krylov methods.**  
Implicit solves can become computational bottlenecks that iterative subspace methods accelerate.

**Optimization.**  
Learning rates act partly like step sizes in discrete parameter dynamics.

**Architecture as dynamics.**  
Residual blocks invite integrator interpretations, subject to explicit assumptions.

**Boundary contracts.**  
Separately discretized components must compose without invalidating their guarantees.

**Neural transport.**  
Representation updates can be studied as approximate transport under constrained numerical rules.

## 40. What changed in our picture?

Dynamics taught us to ask:

> What evolution law does the system follow?

Numerics adds a second question:

> What evolution law does the computer actually execute?

Those are not always the same.

The gap is not merely error in the everyday sense.

It has structure.

It has:

- order;
- stability regions;
- stiffness;
- geometry;
- commutators;
- step-size dependence.

Once computation is viewed this way, architectural depth stops being only a count of layers.

It can also become a numerical design variable.

That is the bridge to the chapters ahead.

## References used in this chapter

- [@Butcher2016]
- [@HairerNorsettWanner1993]
- [@HairerWanner1996]
- [@HairerLubichWanner2006]
- [@Higham2002]

See \`sources/source-locks/ATLAS-CH-NUMERICS-001.yaml\` for exact source roles and claim scope.
