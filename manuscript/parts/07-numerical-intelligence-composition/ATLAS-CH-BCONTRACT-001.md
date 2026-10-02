# Boundary Contracts
<!-- ATLAS-CH-BCONTRACT-001 -->

**Epistemic status:** mathematical exposition built from standard sensitivity/conditioning and automatic-differentiation machinery, local-to-global compatibility ideas, exact toy derivations, and a source-bounded GCL project connection.  
**Primary figure:** \`ATLAS-FIG-BCONTRACT-001\`  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-BCONTRACT-001-DERIVATIONS.md\`  
**Computational witness:** \`mathematics/computational-witnesses/ATLAS-CW-BCONTRACT-001.md\`

## 1. Composition fails at boundaries

A complex learned system is rarely one undivided map.

It is assembled from components:

\[
x
\xrightarrow{f}
y
\xrightarrow{g}
z.
\]

The dimensions may match. The program may run. The result can still be wrong.

The reason is simple: a boundary carries more than shape.

It carries meaning.

It carries admissible geometry.

It carries perturbations and gradients.

It carries numerical error.

It may also carry hidden assumptions about scale, normalization, units, support, precision, or invariants.

The central question of this chapter is therefore:

> What must one component expose at its boundary so that another component can use it without reopening the entire interior?

The Atlas answer is a **boundary contract**.

A boundary contract is not merely a software API and not automatically a certificate. It is a structured statement of obligations that a composition depends on.

## 2. The engineered flange

The useful allegory is an **engineered flange**.

Two physical machines may have matching bolt patterns and still be unsafe to connect. One side may expect pressure the other cannot tolerate. A load may arrive along the wrong axis. Two fluids may be chemically incompatible. The dimensions fit while the interface semantics fail.

The correspondence is:

- bolt geometry ↔ shape/type compatibility;
- working medium ↔ semantic interpretation;
- load direction ↔ perturbation direction;
- rated load ↔ sensitivity bound;
- tolerance ↔ numerical/error budget;
- alignment constraint ↔ geometric invariant.

The limit is important.

A learned component is not a steel flange. Its behavior can depend on state, data, adaptation, and training history. It need not obey fixed constitutive laws.

The flange is useful only for one lesson:

> compatibility is a bundle of obligations, not one matching dimension.

Once that point is clear, the mathematics should take over.

## 3. A provisional contract object

Let

\[
f:\mathcal X\to\mathcal Y.
\]

The Atlas uses the provisional explanatory object

\[
\boxed{
C_f=
(\mathcal X,\mathcal Y,\Sigma,\mathcal I,\mathcal S,\mathcal E).
}
\]

Its fields are:

\[
\mathcal X
=
\text{admissible input domain},
\]

\[
\mathcal Y
=
\text{admissible output domain},
\]

\[
\Sigma
=
\text{semantic declaration},
\]

\[
\mathcal I
=
\text{invariants and geometric obligations},
\]

\[
\mathcal S
=
\text{sensitivity and perturbation behavior},
\]

\[
\mathcal E
=
\text{numerical error and precision obligations}.
\]

This tuple is not proposed as a universal standard.

It is a disciplined way to ask what must cross a boundary besides bytes and dimensions.

## 4. Interface signature versus boundary contract

An interface signature might say:

\[
f:\mathbb R^{768}\to\mathbb R^{768}.
\]

That is useful.

It tells us what shapes can be connected.

It does not tell us whether the output is:

- normalized;
- centered;
- a probability vector;
- a logit vector;
- an embedding whose norm carries confidence;
- an embedding whose norm is intentionally discarded;
- an element of a quotient class;
- valid only in a bounded operating region.

A boundary contract adds these obligations explicitly.

The distinction can be written schematically as

\[
\boxed{
\text{signature}
\subset
\text{contract information}.
}
\]

A signature can be part of a contract.

It is not the whole contract.

## 5. Shape-compatible, semantically incompatible

Consider

\[
f_{\rm dir}(x)
=
\frac{x}{\|x\|_2},
\qquad
x\neq0.
\]

The output is a unit vector.

Suppose its intended semantics are:

> direction only; amplitude has been intentionally discarded.

Now define

\[
g_{\rm mag}(y)
=
\|y\|_2,
\]

and suppose the downstream component interprets magnitude as meaningful amplitude.

The tensor shapes compose perfectly:

\[
\mathbb R^2
\to
\mathbb R^2
\to
\mathbb R.
\]

Take

\[
x=(3,4).
\]

Its amplitude is

\[
\|x\|_2=5.
\]

But

\[
g_{\rm mag}(f_{\rm dir}(x))
=
1.
\]

The software connection is legal.

The semantic connection is not.

This is the simplest reason a boundary contract must carry meaning, not only type.

## 6. Four obligation classes

The Atlas separates four classes because they fail in different ways.

### 6.1 Semantic obligations

A semantic obligation answers:

> What does this state mean?

Examples include:

- probability versus logit;
- displacement versus absolute position;
- direction versus magnitude-bearing vector;
- uncertainty estimate versus raw score;
- local coordinate versus globally identified state.

Semantic mismatch can survive every shape check.

### 6.2 Geometric obligations

A geometric obligation answers:

> What states are admissible, and what equivalences matter?

Examples include:

\[
\|x\|=1,
\]

\[
X^\top X=I,
\]

simplex constraints,

quotient identifications,

positivity,

sparsity,

or a known gauge freedom.

The Geometry chapter showed that ambient coordinates and admissible states need not be the same object.

A boundary that forgets this distinction can hand a downstream component an invalid state even when every tensor dimension is correct.

### 6.3 Differential obligations

A differential obligation answers:

> How do perturbations and gradients cross this boundary?

For a differentiable map

\[
y=f(x),
\]

the local derivative is

\[
J_f(x).
\]

Rather than materializing the full Jacobian, we often probe it through

\[
J_f(x)v
\]

and

\[
J_f(x)^\top u.
\]

These are Jacobian-vector products and vector-Jacobian products. Automatic differentiation provides efficient machinery for computing them in many practical systems [@BaydinEtAl2018].

Differential obligations can include:

- directional gain;
- dominant singular value estimates;
- gradient transfer conventions;
- null directions;
- sensitivity to selected subspaces.

### 6.4 Numerical obligations

A numerical obligation answers:

> What error and conditioning assumptions are being passed across the boundary?

It may include:

- dtype or precision;
- scaling convention;
- absolute or relative error budget;
- conditioning estimate;
- tolerance;
- solver residual;
- stopping criterion;
- stability region.

Numerical analysis has long distinguished problem conditioning from algorithmic stability [@Higham2002].

A composition can fail because the mathematics is badly conditioned, because an implementation is unstable, or because an interface discards the information needed to tell which happened.

## 7. The chain rule is the first composition law

Let

\[
y=f(x),
\]

and

\[
z=g(y).
\]

Then

\[
z=(g\circ f)(x).
\]

Locally,

\[
\boxed{
J_{g\circ f}(x)
=
J_g(f(x))J_f(x).
}
\]

This elementary identity is one of the most useful facts in the chapter.

It tells us that local perturbation behavior composes multiplicatively.

If

\[
\delta x
\]

is a small input perturbation, then

\[
\delta z
\approx
J_gJ_f\,\delta x.
\]

Using the induced \(2\)-norm,

\[
\|J_gJ_f\|_2
\le
\|J_g\|_2\|J_f\|_2.
\]

This is a local bound.

It is not automatically a global theorem.

## 8. An exact two-module witness

Take

\[
A=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
\]

Let

\[
f(x)=Ax,
\]

and

\[
g(y)=By.
\]

Then

\[
C=BA
=
\begin{pmatrix}
2&1/2\\
0&1
\end{pmatrix}.
\]

The composed local sensitivity is exactly the matrix \(C\).

For

\[
v=
\begin{pmatrix}
1\\
-1
\end{pmatrix},
\]

the forward directional sensitivity is

\[
Cv
=
\begin{pmatrix}
3/2\\
-1
\end{pmatrix}.
\]

For

\[
u=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\]

the reverse sensitivity is

\[
C^\top u
=
\begin{pmatrix}
2\\
3/2
\end{pmatrix}.
\]

The same boundary can therefore be probed in the forward direction through a JVP and in the reverse direction through a VJP.

## 9. Exact local amplification

For this \(C\),

\[
C^\top C
=
\begin{pmatrix}
4&1\\
1&5/4
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_\pm
=
\frac{21\pm\sqrt{185}}8.
\]

Therefore

\[
\boxed{
\|C\|_2
=
\sqrt{
\frac{21+\sqrt{185}}8
}
\approx
2.079707626949502.
}
\]

This number has a precise meaning.

Among unit perturbations, there is a direction whose local output perturbation is amplified by about \(2.08\).

It does **not** mean:

- every perturbation grows by \(2.08\);
- every state has the same Jacobian;
- the nonlinear system is globally \(2.08\)-Lipschitz;
- the composition is unsafe.

A sensitivity number is useful only when its scope remains attached to it.

## 10. The boundary figure

![A schematic upstream-to-downstream boundary contract listing semantic, geometric, differential, and numerical obligations beside the exact image of the unit perturbation circle under C equals [[2,1/2],[0,1]].](../../figures/masters/ATLAS-FIG-BCONTRACT-001.png)

The left panel is schematic.

It names the obligation classes and shows forward JVP and reverse VJP channels.

The right panel is literal for the toy system.

The dashed circle is the set of unit perturbations.

The solid ellipse is its image under

\[
C.
\]

The longest radius is the dominant singular value,

\[
2.0797\ldots
\]

The figure deliberately keeps the schematic contract language beside an exact local sensitivity object.

One should not be mistaken for the other.

## 11. Power iteration as a boundary probe

If the full Jacobian is too large to form, one may estimate a dominant singular value using repeated applications of

\[
J
\]

and

\[
J^\top.
\]

For the toy map,

\[
M=C^\top C.
\]

Power iteration uses

\[
v_{k+1}
=
\frac{Mv_k}{\|Mv_k\|_2}.
\]

The Rayleigh quotient

\[
\mu_k
=
\frac{v_k^\top Mv_k}{v_k^\top v_k}
\]

approaches the dominant eigenvalue under standard convergence conditions.

Then

\[
\sqrt{\mu_k}
\]

approaches the dominant singular value of \(C\).

Starting from the normalized direction proportional to \((1,1)\), the witness gives

\[
1.9039433,
\]

\[
2.0701070,
\]

\[
2.0792647,
\]

\[
2.0796874,
\]

\[
2.0797067,
\]

and then agreement with the exact value to the displayed precision.

This is a good use of a probe because the answer is known independently.

## 12. Estimation is not certification

Power iteration has assumptions.

Its convergence depends on the spectrum and the starting vector.

A finite iteration gives an estimate, not an oracle.

In a nonlinear component, the Jacobian may also change with the operating point.

Therefore a contract should not silently transform

> we measured a large singular direction near this state

into

> the component has a proven global gain bound.

The first can be strong local evidence.

The second requires a much stronger argument.

This is where numerical conditioning discipline matters [@Higham2002].

## 13. Separator variables

Large systems often cannot expose their entire internal state at every interface.

They summarize.

Let

\[
s(y)
\]

be a low-dimensional boundary summary.

This can be valuable.

It can also erase exactly the information the next component needs.

Suppose

\[
s(y)=y_1.
\]

Take

\[
y=(0,1),
\qquad
y'=(0,2).
\]

Then

\[
s(y)=s(y')=0.
\]

But if downstream behavior depends on

\[
h(y)=y_2,
\]

then

\[
h(y)\neq h(y').
\]

The separator has identified two states that are operationally different.

A low-order interface is therefore justified only relative to a property:

> sufficient for what?

That question cannot be skipped.

## 14. Local-to-global reasoning

Boundary contracts are local objects.

They describe what neighboring components may assume about each other.

This naturally recalls local-to-global mathematics.

Sheaf theory provides a formal language for compatible local data and gluing [@Curry2013Sheaves]. That language is useful because it teaches the right kind of question:

> if local pieces agree on overlaps, under what conditions do they assemble into a coherent global object?

The Atlas does not claim that learned-system contracts are automatically sheaves.

Nor does local compatibility automatically yield:

- global stability;
- global safety;
- global optimality;
- absence of feedback loops;
- preservation of a system-level invariant.

The sheaf connection is a lens on compatibility.

It is not a free global theorem.

## 15. Individually acceptable pieces can fail together

Suppose two components each have a finite local gain bound.

That does not settle the behavior of a large feedback system containing them.

The problem can arise from:

- gain multiplication;
- incompatible semantics;
- hidden state;
- delay;
- approximation error;
- non-normal coupling;
- feedback;
- state-dependent regime changes.

The chapter’s local contract object is deliberately not named a certificate.

It is an interface statement.

Whether the interface obligations are sufficient for a stronger global property must be proved or tested separately.

## 16. Public GCL project state

The Atlas design connects this chapter to the GCL MODULUS research programme.

That connection must remain source-bounded.

The current public repository

\`grandchallenge/MODULUS\`

was inspected at commit

\`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`.

It contains typed contract machinery, including the public file

\`modulus/online/contracts.py\`,

which defines a \`RegretContract\` and associated geometry, feedback, comparator, loss, guarantee, constraint, and telemetry fields.

That is real public project state.

However, the remembered research names

- \`BoundaryContract\`;
- \`SeparatorCompiler\`;
- \`Modula\`

were not found in the inspected public tree or searchable commit history.

The chapter therefore does **not** claim that those named extensions are implemented in current public MODULUS.

This is an example of the source discipline the Atlas will later formalize: project memory can motivate a question without being promoted into documentary evidence.

## 17. The GCL working slogan, properly bounded

The Atlas specification preserves the working slogan:

> “Modula tells the optimizer how to move. Boundary contracts tell the system how to compose.”

It is useful rhetorically because it distinguishes two scales:

- an update rule governs motion;
- an interface contract governs composition.

But the slogan is not a theorem.

The present chapter establishes only the bounded mathematical pieces developed above:

- semantic obligations;
- geometric obligations;
- JVP/VJP sensitivity;
- numerical conditioning;
- separator sufficiency questions;
- local composition bounds.

The stronger programme remains research.

## 18. Six failure modes

### 18.1 Shape without meaning

Dimensions match while semantic interpretation differs.

### 18.2 Geometry without preservation

The downstream component receives a state outside its admissible set.

### 18.3 Local sensitivity without global scope

A Jacobian norm measured at one state is treated as a global bound.

### 18.4 Compressed boundary without sufficiency

A separator erases state that changes downstream behavior.

### 18.5 Numerical tolerance without conditioning

An absolute tolerance is quoted without regard to problem scaling or conditioning.

### 18.6 Contract without support

An obligation is written down but not measured, derived, proved, or otherwise supported.

A contract is only as strong as the obligations it records and the evidence behind them.

## 19. What a mature contract might carry

A future machine-readable boundary contract could record, for example:

- object identity;
- input/output semantic types;
- shape and dtype;
- manifold or invariant constraints;
- units or scale conventions;
- local sensitivity probes;
- norm conventions;
- uncertainty or error budget;
- approximation method;
- separator variables;
- operating region;
- failure conditions;
- evidence identity;
- version identity.

The list is intentionally not canonical.

Different components need different obligations.

The purpose is to make hidden assumptions inspectable.

## 20. Atlas connections

**Geometry.**  
A boundary can carry admissible state geometry, not merely coordinates.

**Numerical intelligence.**  
Conditioning, residuals, and error budgets become interface obligations.

**Automatic differentiation.**  
JVPs and VJPs provide practical directional probes [@BaydinEtAl2018].

**Composition Without Catastrophe.**  
The next step is to ask when local contracts are sufficient for system-level reasoning.

**Governed adaptation.**  
A self-changing component should not silently invalidate the contract under which other components depend on it.

The recurring Atlas shift is:

\[
\boxed{
\text{architecture as connected modules}
\longrightarrow
\text{architecture as composition of explicit contracts}.
}
\]

## 21. Closing view

The most dangerous interface assumptions are often the ones nobody wrote down.

A boundary contract makes them objects.

What does the state mean?

What geometry is valid?

What perturbations are amplified?

What numerical error is being inherited?

What summary has been retained, and what has been discarded?

The flange is only an allegory.

The contract is the object.

And a local contract is not the end of the argument.

It is the beginning of a compositional one.

## References used in this chapter

- [@BaydinEtAl2018]
- [@Higham2002]
- [@Curry2013Sheaves]

See \`sources/source-locks/ATLAS-CH-BCONTRACT-001.yaml\` for exact source identities, public GCL project-state boundaries, and claim scope.
