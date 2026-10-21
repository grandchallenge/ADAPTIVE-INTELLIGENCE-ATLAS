# States, Operators, Flows, and Interfaces
<!-- ATLAS-CH-OBJECTS-001 -->

**Epistemic status:** Atlas Synthesis  
**Specification:** manuscript/specifications/ATLAS-CH-OBJECTS-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-OBJECTS-001-DERIVATIONS.md  
**Source lock:** sources/source-locks/ATLAS-CH-OBJECTS-001.yaml

## 1. Roles are not storage shapes {#the-same-tensor-can-be-four-different-things}

Suppose a program contains a square array

\[
A\in\mathbb R^{n\times n}.
\]

What is it?

It might be:

- a covariance state;
- a learned parameter;
- a linear operator;
- an adjacency matrix;
- a metric tensor in coordinates;
- an attention score matrix;
- an evidence artifact.

The shape does not answer the question.

The Atlas therefore begins with a discipline:

> identify an object by the role it plays in the argument, not only by the container used to store it.

Four roles recur throughout this book:

\[
\boxed{
\text{state},
\quad
\text{operator},
\quad
\text{flow},
\quad
\text{interface}.
}
\]

These are explanatory categories.

They are not a universal ontology.

[]{#noun-verb-motion-handshake} **A first analogy.**

A useful first analogy is grammatical.

A **state** behaves like a noun: something has a value.

An **operator** behaves like a verb: something is done to a state.

A **flow** behaves like unfolding motion: transformations accumulate through an evolution parameter.

An **interface** behaves like a handshake: two objects agree on what may cross a boundary.

The analogy is useful because it catches category errors.

It also fails quickly.

A mathematical state can itself encode an operator.

An operator can be state-dependent.

A family of operators may fail to satisfy the exact algebraic law required of a true flow.

An interface can be learned or adaptive.

Natural-language grammar is therefore only an entry point.

The mathematics determines the object.

The analogy serves only to orient the question. The four mathematical roles below decide which inference is legitimate; neither a tensor shape nor a grammatical label can do so.


## 2. Four mathematical roles {#state}

A role is specified by what an object means and how it participates in a claim. The same stored object may play different roles in different arguments.

### State

A state is an information-bearing value

\[
x\in\mathcal X.
\]

The state space \(\mathcal X\) may be:

- Euclidean;
- discrete;
- probabilistic;
- constrained;
- manifold-valued;
- a product space;
- a space of functions;
- a structured record.

A state answers:

> What information is currently instantiated?

Examples include:

- a hidden activation;
- an optimizer momentum buffer;
- a memory record;
- a probability distribution;
- a graph;
- a model checkpoint;
- a tuple-space configuration.

The word “state” is deliberately broader than “vector.”

[]{#operator} **Operator.**

An operator is a transformation

\[
F:\mathcal X\to\mathcal Y.
\]

It answers:

> What transformation is being applied?

A linear operator has the special form

\[
F(x)=Ax.
\]

But many operators in the Atlas are nonlinear or state-dependent.

Examples include:

- attention;
- normalization;
- a retrieval rule;
- an optimizer update;
- a solver step;
- a routing map;
- a projection or retraction.

A matrix is not automatically an operator.

It becomes an operator when the model assigns it a transformation role.

[]{#flow-and-dynamics} **Flow and dynamics.**

On a topological state space \(\mathcal X\), a **continuous global autonomous flow** is a jointly continuous map

\[
\Phi:\mathbb R\times\mathcal X\to\mathcal X,
\qquad (t,x)\mapsto\Phi_t(x),
\]

such that \(\Phi_0=\mathrm{id}_{\mathcal X}\) and

\[
\Phi_{t+s}=\Phi_t\circ\Phi_s
\qquad (t,s\in\mathbb R).
\]

When the evolution parameter is restricted to nonnegative times, a jointly continuous action of \([0,\infty)\) satisfying the analogous laws is a **continuous semiflow**. A **local flow** has a suitable open time-state domain of definition and satisfies the composition law only where the relevant trajectories and times are defined. Neither a local flow nor a semiflow automatically extends to a global two-sided flow.

The algebraic identity and composition laws **alone** define a group or semigroup action; they do not imply continuity or differentiability. For flows arising from a differentiable ODE, additional regularity and existence/uniqueness hypotheses justify the claimed smoothness and domain.

If a differential equation

\[
\dot x=f(x)
\]

has a well-defined evolution, \(\Phi_t(x_0)\) denotes the state after time \(t\).

This gives a new kind of object.

A single operator says:

> transform this state once.

A flow says:

> here is how transformations accumulate across an evolution parameter.

This distinction becomes central when network depth is treated as computational time.

[]{#interface} **Interface.**

Suppose

\[
F:\mathcal X\to\mathcal Y
\]

feeds

\[
G:\mathcal Y\to\mathcal Z.
\]

At minimum, the codomain of \(F\) must be admissible input for \(G\).

Software type systems often check part of this requirement.

But a meaningful interface can also depend on:

- units;
- scale;
- normalization;
- geometric constraints;
- semantic interpretation;
- uncertainty;
- precision;
- differential sensitivity.

An interface therefore answers:

> What is another component allowed to assume about what crosses this boundary?

The Boundary Contracts chapter later turns this question into a formal programme.

A state can be an input to a map, an operator can depend on a state, and an interface can govern a family of maps. These are related roles, not four mutually exclusive data types.


## 3. Three category errors, worked through {#first-category-error-array-equals-role}

**Stored array versus transformation.** The same matrix can encode observed structure or act on another state; the relevant choice belongs to the mathematical statement.

Let

\[
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix}.
\]

If \(A\) is a covariance matrix, it is a state describing second-order structure.

If \(A\) acts by

\[
x\mapsto Ax,
\]

it is a linear operator.

The stored entries are identical.

The semantics are different.

This distinction becomes important later when the Atlas moves from vectors to operators.

Without role discipline, the phrase “the representation matrix” can hide whether we mean data, a transformation, or a coordinate encoding of something basis-independent.

[]{#second-category-error-one-step-equals-dynamics} **One numerical step versus an evolution.**

Consider a residual update

\[
x_{k+1}
=
x_k+h f(x_k).
\]

One update map is

\[
F_h(x)=x+h f(x).
\]

The depth-indexed computation is the sequence

\[
x_0,
x_1,
x_2,
\ldots
\]

generated by repeated application.

These are not the same object.

The single-step operator can be locally well behaved while repeated application has different long-horizon behavior.

Later chapters on numerical intelligence and non-normality make this distinction quantitative.

[]{#flow-like-is-weaker-than-flow} **An interpretation is not an exact flow.**

Neural networks often invite continuous-time language.

That language can be useful.

It must be scoped.

If layer \(k\) uses a different transformation from layer \(k+1\), the depth-indexed family need not satisfy

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s
\]

for one autonomous flow.

The safer statement may be:

> the architecture admits a dynamical or integrator interpretation.

That is weaker than claiming an exact continuous-time flow.

The Atlas will use the stronger word only when the stronger structure is present.

[]{#third-category-error-matching-shape-equals-composability} **Compatible shape versus meaningful composition.**

Let \(F:\mathbb R^2\setminus\{0\}\to\mathbb R^2\) be the normalization map

\[
F(x)
=
\frac{x}{\|x\|_2},
\qquad x\ne 0.
\]

It returns direction only; it is not defined at the zero vector.

Let

\[
G(y)
=
\|y\|_2
\]

interpret magnitude as meaningful amplitude.

The shapes match.

The semantics do not.

For

\[
x=(3,4),
\]

the original magnitude is \(5\), but

\[
G(F(x))=1.
\]

The interface failed before any matrix multiplication failed.

[]{#interfaces-are-not-interiors} **Contract versus implementation.**

A contract can describe:

- accepted inputs;
- guarantees;
- error bounds;
- invariants;
- provenance.

It does not need to expose the full internal mechanism.

This separation is important for modular intelligence.

If every component must know every other component's interior, composition does not scale.

But abstraction has a price.

A contract can omit something the downstream system actually needs.

The problem is therefore not:

> hide as much as possible.

It is:

> expose enough for the property the composition is supposed to preserve.

In all three examples the entries or dimensions alone pass an impoverished check. The error comes from a hidden assumption about role, time, domain, or preserved quantity.


## 4. Roles can change across a computation {#state-dependent-operators}

The four roles are not rigid boxes.

Attention provides a useful example.

For fixed queries and keys, the normalized attention matrix \(A\) acts linearly on values:

\[
V\mapsto AV.
\]

But in the full layer,

\[
A=A(X)
\]

depends on the current state \(X\).

The operator itself is state-dependent.

This is not a contradiction.

It is exactly why role language is useful.

We can distinguish:

- the current state;
- the operator instantiated from that state;
- the transformation applied to another part of the state.

[]{#operator-valued-state} **Operator-valued state.**

Sometimes a state contains an object that later acts as an operator.

An optimizer state may contain a preconditioner.

A memory system may store a learned routing matrix.

A hypernetwork may emit weights that define another map.

The same mathematical object can therefore change role across a pipeline.

The rule is not:

> every object has one eternal category.

The rule is:

> state the role being used in the present argument.

[]{#evidence-is-another-object-class} **Evidence is not the operator it records.**

Later in the Atlas, evidence records become explicit.

An evidence object may describe an operator:

- which source defined it;
- which code implemented it;
- which run exercised it;
- which output was observed.

The evidence record is not the operator.

Confusing those categories produces a different kind of error.

A green replay tells us that an evidence path reconstructed under its declared conditions.

It does not transform the evidence record into the mathematical object it describes.

The relevant question is not whether a stored matrix, activation, or record has one permanent classification. It is which transformation, claim, or contract is being asserted at this point in the argument.


## 5. Four questions for a reader {#the-four-questions}

The roles provide a compact diagnostic, rather than a second list of object types:

| Role | Question to ask |
|---|---|
| State | What information is instantiated? |
| []{#operator-1} Operator | What transformation acts, on which domain? |
| []{#flow} Flow | How do transformations compose over a declared evolution parameter? |
| []{#interface-1} Interface | What may another component assume at the boundary? |

Not every question needs every role; the point is to expose the assumption needed for the next deduction.

[]{#why-this-vocabulary-matters} **Why this vocabulary matters.**

The rest of the Atlas repeatedly changes levels of description.

Linear algebra moves between coordinates and operators.

Geometry distinguishes ambient coordinates from admissible states.

Attention distinguishes scores from mixing operators.

Optimization adds optimizer state to model state.

Numerical analysis distinguishes one update from accumulated dynamics.

Memory distinguishes stored content from retrieval operators.

Composition distinguishes component interiors from boundary obligations.

Scientific method distinguishes claims from their evidence paths.

Without a small amount of object discipline, these chapters would reuse the same words for incompatible roles.


## 6. Where the distinctions lead {#handoff-to-linear-algebra}

The next mathematical chapter specializes the operator role.

For finite-dimensional linear maps, bases turn operators into matrices.

That creates a powerful computational language:

- projections;
- eigendecompositions;
- singular values;
- pseudoinverses;
- norms;
- conditioning;
- low-rank structure.

The important point is already in place:

\[
\boxed{
\text{matrix coordinates}
\neq
\text{operator role by definition}.
}
\]

Linear algebra will now make that distinction precise.

[]{#handoff-to-information} **Information-bearing states.**

Probability introduces another kind of state.

A distribution is an information-bearing mathematical object.

Entropy, KL divergence, and mutual information are functionals of such states.

Again, storage format is secondary.

What matters is the declared probability model and the operation being performed on it.

### Closing view

The first conceptual discipline of the Atlas is simple:

Do not ask only what shape an object has.

Ask what role it plays.

A state is what is instantiated.

An operator transforms.

A flow organizes transformation through evolution.

An interface states what composition may assume.

These distinctions are not the final theory.

They are the grammar that lets the rest of the book say what kind of thing it is talking about.

The next chapters use the four roles to decide what is being defined, computed, composed and evidenced. Their theorems must still supply their own assumptions and sources.


## References used in this chapter

This chapter is Atlas synthesis. Its project-local vocabulary is bound through sources/source-locks/ATLAS-CH-OBJECTS-001.yaml to the source inventory, Mathematical Lexicon, and Atlas Map. Standard mathematical instances are developed and externally sourced in downstream chapters.
