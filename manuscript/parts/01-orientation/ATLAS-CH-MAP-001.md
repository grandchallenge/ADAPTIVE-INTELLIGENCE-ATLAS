# How to Read a Mathematical Atlas
<!-- ATLAS-CH-MAP-001 -->

**Epistemic status:** Atlas Documentary Synthesis  
**Specification:** manuscript/specifications/ATLAS-CH-MAP-001.md  
**Documentary packet:** mathematics/derivations/ATLAS-CH-MAP-001-DOCUMENTARY.md  
**Source lock:** sources/source-locks/ATLAS-CH-MAP-001.yaml

## 1. Begin with a question {#an-atlas-is-not-a-road}

Why can a matrix be asymptotically stable and still amplify a perturbation? This is the kind of question an atlas should help the reader answer. It suggests where to start, which mathematical tools illuminate the difficulty, and which conclusions are not justified.

A textbook can take a single road from definitions to theorems. An atlas provides more than one useful route: it gives landmarks, several scales of description, and honest boundaries. Its reading order is flexible, but the hypotheses on which a result depends are not.

Consider the exact matrix from **Normality, Pseudospectra, and Transient Growth** (ATLAS-CH-NONNORMAL-001):

\[
A=\begin{pmatrix}4/5&4\\0&4/5\end{pmatrix}.
\]

Both eigenvalues are \(4/5\), so \(\rho(A)=4/5<1\). Since the eigenvalues lie inside the unit disk, \(A^n\to0\) as \(n\to\infty\). Does every individual application of \(A\) therefore shrink a vector?

Use the simplest possible test. For the unit vector \(e_2=(0,1)^\top\),

\[
Ae_2=(4,4/5)^\top,\qquad
\|Ae_2\|_2=\sqrt{16+16/25}>1.
\]

Thus \(\|A\|_2\geq\|Ae_2\|_2>1\). Asymptotic eigenvalue stability and finite-step amplification are compatible. Neither calculation invalidates the other: they answer different mathematical questions.

**How to travel through this example.** The chapter **Linear Maps and Decompositions** (ATLAS-CH-LINALG-001) supplies eigenvalues, singular values, and the induced norm. **Normality, Pseudospectra, and Transient Growth** supplies the exact powers of this triangular matrix, a normal comparison, and a pseudospectral interpretation. Its **ATLAS-FIG-PSPECTRUM-001** plate makes the competing descriptions visible. A reader who wishes to connect that mathematics to neural-network optimization must then consult the relevant dynamical model and empirical evidence. The matrix proves no claim about how frequently real training runs become unstable.

This is an opinionated route: operator norms are more revealing than eigenvalues *for the finite-time amplification question*. It does not imply that operator norms are always the best coordinates, or that a systems-level theory is required to answer every question.

## 2. Many maps, stable coordinates {#map-and-territory}

A mathematical landscape can be mapped through objects, operations, questions, and dependencies. Geography offers a useful analogy only up to a point: a map legend explains how to read a mark; it does not turn a conjecture into a theorem.

A reader may begin at the full Atlas, move to one Part or chapter, and then descend to a precise statement and its proof, derivation, or computational witness. The reverse journey is equally valuable: begin with a calculation, ask which mathematical concept it illustrates, and trace its uses elsewhere.

[]{#read-at-several-resolutions}[]{#stable-identity}

We maintain stable chapter and object identifiers because book order may change. A reference such as ATLAS-CH-NONNORMAL-001 is a coordinate, not an ordinal promise. This matters whenever a new chapter, an improved explanation, or an updated figure changes the physical pages without changing the identity of the mathematical object.

## 3. Paths and prerequisites are different {#the-map-is-not-the-dependency-graph}

A **hard dependency** grants a downstream chapter permission to use an explicitly established upstream object. If \(A\) supplies a theorem needed by \(B\), the arrow \(A\to B\) must identify the precise result and its assumptions.

A **soft cross-link** merely says that two regions illuminate one another. The reader may travel between them, but neither chapter acquires proof authority by proximity.

[]{#hard-dependency}[]{#soft-cross-link}[]{#narrative-is-not-mathematical-authority}

For our matrix example, the definition of an induced operator norm is a mathematical prerequisite. The visual comparison with a later discussion of optimizer transients may be a useful connection, but it is not evidence that an optimizer exhibits this same matrix mechanism.

Neither the table of contents nor the dependency graph alone tells a complete mathematical story. One organizes reading; the other records what may be assumed. The Atlas retains both so that readers can explore without silently importing unproved statements.

## 4. A claim needs its own legend {#the-legend-epistemic-labels}

A mathematical book contains definitions, established results, local derivations, exact computations, empirical observations, interpretations, conjectures, and open problems. They may look equally polished on the page while carrying very different obligations.

The eleven canonical status labels in **Claims, Evidence, and Computational Witnesses** (ATLAS-CH-EVIDENCE-001) also cover GCL project provenance, programme context, and institutional review. They are **not eleven steps on a confidence ladder**. A statement can simultaneously be a derivation, have a computational witness, cite a public source, and carry a separately documented review status. None of these labels by itself authorizes an implication outside the support's scope.

[]{#definition}[]{#established-result}[]{#atlas-derivation}[]{#computational-witness}[]{#observation-and-interpretation}[]{#gcl-project-evidence-and-programme-context}[]{#conjecture-and-open-problem}[]{#institutional-status}[]{#presentation-creates-no-epistemic-status}[]{#proof-derivation-and-witness}[]{#replay-is-not-truth}

Here is how to use the distinction. For the matrix above, the claim \(\rho(A)<1\) but \(\|A\|_2>1\) is justified by a short exact calculation. It is not justified *because a figure has been reproduced* or because a repository recorded successful CI. A plotted finite-horizon curve can illustrate further behavior, but any claim about a real training system would require different assumptions and observations.

An exact finite computation can disprove a proposed universal claim by exhibiting a valid counterexample. Exhaustively checking finitely many examples does not, without an additional argument, prove a universal statement about all possible inputs. The Evidence chapter supplies complete claim-support packets for both kinds of inference.

## 5. Figures are mathematical statements too {#figures-have-representation-classes}

A well-chosen figure can make an operator, trajectory, or geometric constraint more intelligible than a page of unmotivated notation. It still needs a declared interpretation.

[]{#exact-figures}[]{#data-derived-figures}[]{#schematic-figures}

The Atlas distinguishes three figure types. An **exact** figure draws an explicitly defined relation or construction. A **data-derived** figure displays computed or measured values with finite precision, parameters, and a stated method. A **schematic** figure represents a conceptual correspondence, not measured metric distance or causal strength. The image and its caption must make these distinctions clear.

Return to the pseudospectrum plate. Its finite matrix and comparison have exact mathematical definitions; rendering, sampling, color, and resolution remain presentational choices. Readers should be able to follow the figure to the formulas and, where appropriate, its computational witness. A visually striking contour is a guide toward understanding, not an independent proof.

## 6. A source trail is not a theorem {#the-source-lock}

Mathematical derivations, cited authority, and reproducible computation answer different questions. The Atlas keeps exact source locks, derivation packets, computational witnesses, and bounded audits so readers can reconstruct what supported a claim at a particular revision.

[]{#documentary-provenance}[]{#audits}

A source lock identifies what was used and what that source can legitimately support. A replay shows what procedure ran in a declared environment; it does not by itself establish that the model is correct, the mathematics is sound, another party replicated it independently, or a certifying body approved it. An audit asks whether specific claims, assumptions, figures, or sources withstand scrutiny. Its disposition applies only to its declared scope.

These records are valuable, but the introductory chapter need not reproduce the entire institutional procedure. When more detail is needed, follow the chapter's source lock, Evidence chapter, or technical records. Readers should encounter the mathematics before its administrative history, not have to read a ledger to understand a matrix.

## 7. Choose a route suited to the question {#six-ways-through-the-atlas}

The Atlas provides six useful reading patterns. None is privileged for all purposes.

[]{#route-a-linear-foundations}[]{#route-b-dependency-first}[]{#route-c-concepttheme}[]{#route-d-research-frontier}[]{#route-e-proofreplay}[]{#route-f-visualatlas-plate}[]{#choosing-a-route}[]{#how-to-read-a-keystone}[]{#how-to-read-a-frontier-chapter}[]{#allegory-as-a-bounded-instrument}[]{#what-changed-in-our-picture}

| Your objective | Starting point | Follow next | Boundary to remember |
|---|---|---|---|
| Learn a mathematical region | Foundations and illustrative examples | The book's suggested sequence | Editorial order is not prerequisite authority |
| Reconstruct one result | Target theorem or chapter | Hard dependencies back to needed definitions | Every hypothesis still matters |
| Compare a mathematical concept | Operator, geometry, memory, or dynamics theme | Soft links with local prerequisites | Similar language need not imply identical objects |
| Investigate open terrain | Open problem, conjecture, or programme chapter | Established results, assumptions, and failures | Research direction is not completed theorem |
| Replay or audit a computation | Exact claim or witness | Derivation, source, environment, and results | Repeatability is not automatically proof |
| Learn visually | Figure or mathematical plate | Legend, formulas, and scope | Schematic marks are not measurements |

Keystone chapters are high-leverage because many later chapters depend on them; that makes mathematical scrutiny more important, not less. Frontier chapters are best read in reverse: begin by asking what is already established and what remains uncertain. Metaphor or allegory can help motivate either journey, but its job ends where a mathematical definition, derivation, or limitation must take over.

## 8. A compact reader's practice {#a-compact-reader-protocol}

Five reading errors recur across mathematical subjects: confusing chapter order with prerequisites, promoting a soft cross-link into a theorem, treating every exact computation as an unrestricted proof, mistaking replay for independent certification, and reading the geometry of a schematic plate as measured data.

[]{#five-reading-errors-to-avoid}[]{#chapter-order-treated-as-dependency-order}[]{#soft-cross-link-treated-as-prerequisite}[]{#exact-computation-treated-as-proof-automatically}[]{#replay-treated-as-certification}[]{#schematic-figure-treated-as-measured-geometry}

When entering an unfamiliar chapter, ask three linked questions. **What problem is being illuminated?** Identify the central object and try a small example before following additional notation. **What exactly is established?** Check hypotheses, proof or computation, and boundaries; note where a source supplies prior authority. **Where can I go next?** Follow true prerequisites for rigor and soft connections for insight, keeping the two visibly distinct.

This reader's practice is deliberately shorter than a governance checklist. The detailed Evidence chapter explains how to populate a claim-support record when reconstruction or adjudication is necessary. The purpose here is to give the reader enough confidence to begin exploring.

## 9. Closing view {#closing-view-1}

A useful atlas need not reduce its subject to one thesis. Its mathematical commitments are more concrete: important questions should lead to revealing examples, definitions should make the right structures visible, proofs should respect their hypotheses, and connections should disclose their limitations.

The non-normal matrix supplies a small demonstration of what this book should repeatedly accomplish. A familiar description was true but incomplete for the question. An alternative viewpoint produced a direct, exact calculation and a better route through the subject.

The territory will remain larger than the book. Its purpose is to give readers clearer mathematics and the freedom to navigate among honest, overlapping maps.


## References used in this chapter {#references-used-in-this-chapter-1}

This chapter is a documentary synthesis of project-internal canonical objects.

Primary locked sources:

- `governance/ATLAS_MAP.md`;
- `governance/DEPENDENCY_GRAPH.md`;
- `governance/CHAPTER_COMPOSITION_PROTOCOL.md`;
- `governance/EPISTEMIC_STATUS.yaml`;
- `governance/ATLAS_EDITORIAL_PROFILE.md`;
- `governance/FIGURE_REGISTER.yaml`;
- `governance/SOURCE_REGISTER.yaml`.

See `sources/source-locks/ATLAS-CH-MAP-001.yaml` for exact Git blob identities and declared authority.

