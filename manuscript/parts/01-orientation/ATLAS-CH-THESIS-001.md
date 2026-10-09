# A Mathematical Atlas, by Choice
<!-- ATLAS-CH-THESIS-001 -->

**Epistemic status:** Atlas Synthesis  
**Specification:** manuscript/specifications/ATLAS-CH-THESIS-001.md  
**Documentary packet:** mathematics/derivations/ATLAS-CH-THESIS-001-DERIVATIONS.md  
**Source lock:** sources/source-locks/ATLAS-CH-THESIS-001.yaml

## 1. Why make an atlas?

A textbook may build a theory from its foundations. A survey may inventory a field. An atlas has a different task: reveal the shape of a mathematical landscape, give the reader several navigable routes, and identify where the maps overlap or remain incomplete.

This book explores mathematical structures used to describe systems that represent, transform, learn, remember, coordinate, and adapt. It is deliberately **selective and opinionated**. We often prefer operators to bare parameter counts, dynamics to static layer diagrams, geometry to unconstrained coordinates, and explicit interfaces to treating a deployed model as an isolated function.

These are editorial preferences, not a single proposition that the remaining chapters must prove.

For example, eigenvalues inside the unit disk do not preclude finite-time amplification by powers of a non-normal matrix. Operator norms tell us something eigenvalues alone do not. The value of the second viewpoint comes from the question it illuminates and the mathematics that establishes the answer, not from its place in a universal theory of intelligence.

We will sometimes study individual models, sometimes composed systems, and sometimes a purely mathematical object without insisting on an AI analogy. One may follow different mathematical maps of the same territory. Each map should be judged by what it helps the reader understand and by the limits of its assumptions.

**The ambition is to make the mathematics visible without making it smaller.**

## 2. An atlas, not a catalogue

A catalogue tells us what objects exist.

An atlas tells us how a territory is charted.

It contains:

- coordinate systems;
- local maps;
- overlaps;
- landmarks;
- routes;
- scales;
- boundaries;
- regions that remain poorly mapped.

This book is organized in the second way.

A chapter on geometry does not exist merely because manifolds are mathematically important.

It exists because later chapters need a language for legal motion in constrained state spaces.

A chapter on non-normality does not exist merely because pseudospectra are elegant.

It exists because asymptotic eigenvalue stability can miss finite-horizon amplification.

A chapter on replayable evidence does not exist merely because provenance is administratively desirable.

It exists because an adaptive research system must know which claim is supported by which reconstructable path.

The atlas allegory has a limit.

A research programme is not static geography.

The territory can change when new algorithms, new evidence, or new forms of computation appear.

The map therefore has to be versioned.

## 3. The recurring shifts

These changes of viewpoint guide the book's editorial selection. They are routes to mathematical questions, not new discoveries or mandatory steps in a unified proof.

### 3.1 Vectors to operators

A vector tells us where we are in a representation space.

An operator tells us how states are transformed.

Many modern mechanisms become clearer when the transformation is treated as the central object rather than the stored vector alone.

Attention is one example.

Relative position may also be better understood as an operator acting on representation space rather than as an appended coordinate.

### 3.2 Layers to flows

A stack of layers is a discrete sequence.

The same stack can sometimes be interpreted as an approximation to an evolution law.

That viewpoint introduces questions of:

- stability;
- step size;
- reversibility;
- stiffness;
- splitting;
- error control.

Depth can then be studied partly as computational time.

This does not mean every network is literally a discretized differential equation.

It means numerical dynamics can reveal structure that layer counting alone hides.

### 3.3 Parameters to geometry

Parameter values live in spaces with constraints, symmetries, scales, and equivalences.

If a state or parameter is constrained to a sphere, Stiefel manifold, simplex, quotient space, or other structured domain, the geometry changes what constitutes a legal or meaningful update.

The Geometry keystone develops this point formally.

### 3.4 Routing to decision making

A router does more than compute a score.

It allocates scarce computation under uncertainty and capacity constraints.

That opens the door to online decision theory, regret, optionality, and coordination costs.

### 3.5 Context to compiled memory access

A context window is one memory surface.

It is not the only one.

An adaptive system can combine:

- parametric memory;
- external retrieval;
- associative stores;
- symbolic records;
- shared institutional memory;
- compiled context.

The Atlas therefore treats memory as infrastructure as well as model anatomy.

### 3.6 Agents to distributed systems

Once multiple models, tools, memories, humans, and validators interact, the relevant object is no longer a lone agent.

It is a coordinated system.

Questions of concurrency, communication, provenance, shared state, failure isolation, and authority become mathematically and operationally relevant.

### 3.7 Training to dynamical identification

An optimizer has state.

A model has state.

The data stream and scheduler can have state.

The combined training process can therefore be studied as a dynamical system rather than only as repeated minimization of a scalar loss.

### 3.8 Interpretability to intervention

Description is weaker than controlled substitution.

If a proposed internal object is said to matter, the stronger question is whether changing, replacing, suppressing, or preserving it changes behavior in the predicted way.

The Atlas therefore treats intervention and substitution as important diagnostic standards.

### 3.9 Architecture to composition of contracts

A system can fail even when every tensor shape matches.

Composition requires assumptions about meaning, geometry, perturbations, and numerical behavior.

The Boundary Contracts keystone develops this as an interface problem.

### 3.10 Result to evidence object

A research conclusion is not only a sentence.

It is supported by sources, methods, environments, artifacts, observations, interpretations, and review state.

The Replayable Evidence Objects keystone turns that support path into an explicit object.

## 4. A provisional system decomposition

For one systems-oriented route, we may use the provisional explanatory decomposition

\[
\mathcal A
=
(\mathcal S,\mathcal O,\mathcal D,\mathcal M,\mathcal I,\mathcal E,\mathcal G).
\]

Here:

\[
\mathcal S
=
\text{states},
\]

\[
\mathcal O
=
\text{operators},
\]

\[
\mathcal D
=
\text{dynamics},
\]

\[
\mathcal M
=
\text{memory},
\]

\[
\mathcal I
=
\text{interfaces},
\]

\[
\mathcal E
=
\text{evidence},
\]

and

\[
\mathcal G
=
\text{governance}.
\]

This tuple is neither a universal ontology nor a theorem. It is one map legend. Later chapters may use other coordinates for different questions without proving those coordinates equivalent.

Later chapters will refine each term and, where necessary, expose the places where the decomposition becomes inadequate.

## 5. Choose the boundary to fit the question

Consider a retrieval-augmented system.

Its answer can depend on:

- the model weights;
- the tokenizer;
- the query transformation;
- the retrieval index;
- the current contents of the index;
- ranking;
- context compilation;
- tool outputs;
- runtime policies.

If we ask only what is stored in the model parameters, we have chosen a system boundary that excludes part of the causal machinery.

The same issue appears in agent systems.

A planner that calls a solver and writes to shared memory cannot be understood entirely by inspecting the planner weights.

Capability is partly distributed over the arrangement.

For that question, a broader unit of analysis may be useful:

\[
\boxed{
\text{model}
\subseteq
\text{adaptive computational system}.
}
\]

The inclusion can be strict. But an individual model may be the right boundary for a particular mathematical claim. The distinction is about useful explanation, not a compulsory systems ontology.

## 6. What makes a chosen viewpoint worthwhile?

An opinionated atlas owes readers reasons rather than allegiance. A perspective earns its place by clarifying a concrete problem, exposing a useful invariant, resolving an apparent paradox, improving a calculation, or revealing a precise connection to another subject.

For each preferred lens, ask: What question does it answer? What small example reveals the need for it? Which theorem, calculation, or witness makes the insight exact? When would a competing lens work better?

Not every neural network is a discretized differential equation. Not every question about intelligent computation needs governance or persistent memory. Not every geometric analogy supports a theorem. The Atlas should show these limitations as openly as its successful connections.

## 7. Description versus programme

Some claims in the Atlas are descriptive.

For example:

- attention uses state-dependent mixing operators;
- momentum introduces optimizer state;
- a source hash identifies bytes;
- a Jacobian describes local differential sensitivity.

Other claims are programme-level.

For example:

- intelligent systems should externalize more world knowledge into governed shared memory;
- adaptive depth should be treated as numerical error control;
- boundary contracts should become first-class architectural objects;
- research systems should preserve replayable evidence objects.

The second class is not smuggled into the first.

A research programme can be useful before it becomes established theory.

It must still be labeled correctly.

## 8. Dependencies and connections are different maps

The hard dependency graph records exactly which definitions and results later chapters may assume. Soft cross-links reveal possible routes through the terrain. Neither graph is a proof that the whole subject reduces to one sequence.

The keystone chapters were written early to test a durable mathematical composition method. The remaining chapters extend the coverage. That production history does not itself validate an overall theory of adaptive intelligence.

## 9. What the chapters should give the reader

A mature chapter should make a worthwhile mathematical object intelligible. It should motivate its definitions, develop the needed mathematics, supply an example or figure when useful, and state clearly what has been established.

Geometry should explain how constraints change admissible motion. Operator theory should distinguish asymptotic eigenvalue claims from finite-horizon behavior. Numerical analysis should reveal when a time-stepping algorithm fails to respect a continuous law. Memory and coordination chapters should expose what they add to a particular system-level task. Scientific-method chapters should make the support for claims inspectable.

None is required to establish a single Adaptive-System Thesis. Incomplete GCL investigations can be included as expressly unfinished terrain rather than evidence forced into a conclusion.

## 10. The map ahead

The immediate next chapter introduces four recurring roles:

- states;
- operators;
- flows;
- interfaces.

After that, the mathematical substrate develops:

- linear maps;
- probability and information;
- geometry;
- dynamics;
- numerical analysis;
- local-to-global reasoning.

Only then does the Atlas move deeply into representation, architecture, optimization, memory, routing, agents, and governed adaptation.

One useful itinerary is:

\[
\boxed{
\text{geometry}
\to
\text{operators}
\to
\text{dynamics}
\to
\text{optimization}
\to
\text{composition}
\to
\text{memory}
\to
\text{coordination}
\to
\text{diagnostics}
\to
\text{governed adaptation}.
}
\]

This is a route through the atlas, not a deduction or an obligatory reading order.

## 11. Closing view

The Atlas is not neutral about which mathematical viewpoints are enlightening. It is equally unwilling to confuse its selection with a universal result.

The concluding chapters will revisit connections and unresolved boundaries rather than manufacture a theorem that all chapters were written to support.

An atlas succeeds when readers leave better equipped to recognize an important mathematical structure, ask a sharper question, choose the right formal tool, and know where an argument stops. That is the standard by which this book should be judged.

## References used in this chapter

This chapter is Atlas synthesis. Its load-bearing documentary sources are the source inventory, Atlas Map, Editorial Profile, and Chapter Composition Protocol bound in sources/source-locks/ATLAS-CH-THESIS-001.yaml. External mathematical claims are deferred to the downstream chapters that source them directly.
