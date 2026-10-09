# Atlas Map v0.2

**Status:** dependency-refined architecture  
**Parts:** 14  
**Chapter contracts:** 80  
**Hard dependency semantics:** `governance/DEPENDENCY_GRAPH.md` / `.yaml`

The map records purpose and hard dependency, not final chapter numbering. Stable IDs survive reordering. Soft cross-links and dependency-role annotations live in the dependency-graph supplement.

## Part 1 — Orientation: What Adaptive Intelligence Is
`ATLAS-PART-ORIENTATION`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-THESIS-001` | A Mathematical Atlas, by Choice | Explain the selective mathematical viewpoints of an opinionated atlas without requiring one grand theorem. | — |
| `ATLAS-CH-MAP-001` | How to Read a Mathematical Atlas | Explain the multi-resolution reading strategy, epistemic labels, figures, computational witnesses, and dependency paths. | `ATLAS-CH-THESIS-001` |
| `ATLAS-CH-OBJECTS-001` | States, Operators, Flows, and Interfaces | Introduce the four recurring object types used across the book and why confusing them causes conceptual errors. | `ATLAS-CH-THESIS-001` |
| `ATLAS-CH-EVIDENCE-001` | Claims, Evidence, and Computational Witnesses | Establish the Atlas distinction among theorem, observation, computation, interpretation, conjecture, and programme. | `ATLAS-CH-MAP-001` |

## Part 2 — Mathematical Substrate
`ATLAS-PART-MATH`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-LINALG-001` | Linear Maps and Decompositions | Develop bases, projections, eigendecompositions, SVD, low-rank approximation, pseudoinverses, and operator norms as transformation language. | `ATLAS-CH-OBJECTS-001` |
| `ATLAS-CH-NONNORMAL-001` | Normality, Pseudospectra, and Transient Growth | Show why eigenvalues alone can fail to predict short-horizon behavior and develop non-normal amplification. | `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-KRYLOV-001` | Krylov Subspaces and Iterative Solves | Develop Arnoldi, Lanczos, residual-driven subspaces, and the logic of solving large problems through informative directions. | `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-INFO-001` | Probability, Information, and Statistical Structure | Introduce conditional probability, concentration, entropy, KL divergence, mutual information, exponential families, and sufficient statistics. | `ATLAS-CH-OBJECTS-001` |
| `ATLAS-CH-GEOM-001` | Geometry of Constrained State Spaces | Develop manifolds, tangent spaces, geodesics, exponential maps, retractions, spheres, Stiefel and Grassmann manifolds. | `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-DYN-001` | Flows, Stability, and Bifurcation | Develop ODEs, fixed points, Lyapunov ideas, linearization, bifurcations, Hamiltonian and symplectic viewpoints. | `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-NUMERICS-001` | Discretization, Stability, and Splitting | Develop consistency, stability, convergence, explicit/implicit schemes, stiffness, Lie–Trotter and Strang splitting. | `ATLAS-CH-DYN-001` |
| `ATLAS-CH-LOCALGLOBAL-001` | Local-to-Global Mathematics | Introduce graphs, sheaves, compatibility, gluing, and compositional viewpoints only to the degree needed later. | `ATLAS-CH-OBJECTS-001` |

## Part 3 — Representation Geometry
`ATLAS-PART-REP`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-REP-001` | Representations and Invariants | Develop embeddings, latent representations, invariance, equivariance, identifiability, superposition, sparsity, and feature dictionaries. | `ATLAS-CH-INFO-001`, `ATLAS-CH-GEOM-001` |
| `ATLAS-CH-NORMREP-001` | Normalized and Hyperspherical Representations | Study unit-norm states, angular versus radial information, SLERP, tangent updates, and normalized architectures. | `ATLAS-CH-GEOM-001`, `ATLAS-CH-REP-001` |
| `ATLAS-CH-QUOTIENT-001` | Equivalence and Quotient Geometry | Treat redundant parameterizations as equivalence classes and ask whether quotienting simplifies learning landscapes. | `ATLAS-CH-GEOM-001`, `ATLAS-CH-REP-001` |
| `ATLAS-CH-RESIDUAL-001` | The Residual | Formulate the search for minimal transferable computational structure that survives changes of representation and parameterization. | `ATLAS-CH-QUOTIENT-001` |
| `ATLAS-CH-TRANSFER-001` | Reconstruction and Transfer | Connect minimal representations, transfer learning, bottlenecks, reconstruction, and capability recovery. | `ATLAS-CH-RESIDUAL-001`, `ATLAS-CH-INFO-001` |

## Part 4 — Neural Computation as Dynamics
`ATLAS-PART-ARCH`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-ARCHHIST-001` | From Layered Networks to Residual Systems | Use MLPs, CNNs, RNNs, encoder–decoders, and residual networks to expose the transition from static composition to dynamical interpretation. | `ATLAS-CH-DYN-001` |
| `ATLAS-CH-TRANSFORMER-001` | The Transformer as Baseline Object | Present conventional Transformer anatomy precisely enough to support later reinterpretation. | `ATLAS-CH-ARCHHIST-001` |
| `ATLAS-CH-DEPTH-001` | Depth as Computational Time | Develop recurrent depth, adaptive depth, deep equilibrium, and conditional computation through the lens of computational time. | `ATLAS-CH-NUMERICS-001`, `ATLAS-CH-ARCHHIST-001` |
| `ATLAS-CH-SPLIT-001` | Split-Operator Networks | Apply operator splitting to neural computation and analyze ordering, commutators, and splitting error. | `ATLAS-CH-NUMERICS-001`, `ATLAS-CH-TRANSFORMER-001` |
| `ATLAS-CH-TRANSPORT-001` | Representation as Transport | Synthesize geometry, residual computation, and constrained motion into a transport view of representation updates. | `ATLAS-CH-NORMREP-001`, `ATLAS-CH-SPLIT-001` |

## Part 5 — Attention, Sequence, and Position
`ATLAS-PART-ATTN`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-ATTNOP-001` | Attention as an Operator | Develop queries, keys, values, kernels, softmax, sparse attention, and operator interpretations. | `ATLAS-CH-TRANSFORMER-001`, `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-ATTNAPPROX-001` | Approximate and Structured Attention | Study FAVOR+, random features, structured projections, entmax, sparsity, and approximation tradeoffs. | `ATLAS-CH-ATTNOP-001`, `ATLAS-CH-KRYLOV-001` |
| `ATLAS-CH-POSGEOM-001` | The Geometry of Position | Develop sinusoidal encodings, RoPE, block rotations, long-context extrapolation, and multidimensional position. | `ATLAS-CH-ATTNOP-001`, `ATLAS-CH-GEOM-001` |
| `ATLAS-CH-RPO-001` | Relative-Position Operators | Move from positional vectors to low-dimensional operators, frequency modes, DC components, and head-specific specialization. | `ATLAS-CH-POSGEOM-001`, `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-LATENTTIME-001` | Latent Clocks | Treat time as an inferred variable using dynamic time warping, multimodal alignment, and asynchronous sequence structure. | `ATLAS-CH-RPO-001`, `ATLAS-CH-DYN-001` |

## Part 6 — Optimization as Geometry and Dynamics
`ATLAS-PART-OPT`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-OPTBASE-001` | First-Order Optimization | Develop SGD, momentum, Adam-family methods, schedules, clipping, initialization, and weight decay as baseline machinery. | `ATLAS-CH-DYN-001` |
| `ATLAS-CH-SECOND-001` | Curvature and Second-Order Structure | Develop Hessians, Fisher information, natural gradient, quasi-Newton methods, trust regions, and proximal ideas. | `ATLAS-CH-OPTBASE-001`, `ATLAS-CH-GEOM-001` |
| `ATLAS-CH-MATRIXOPT-001` | Matrix-Aware Optimization | Study Shampoo, polar factors, orthogonalized updates, Muon-like methods, and square versus rectangular geometry. | `ATLAS-CH-LINALG-001`, `ATLAS-CH-SECOND-001` |
| `ATLAS-CH-MANOPT-001` | Optimization on Manifolds | Develop tangent gradients, retractions, constrained motion, and sphere/Stiefel optimization. | `ATLAS-CH-GEOM-001`, `ATLAS-CH-OPTBASE-001` |
| `ATLAS-CH-SPECTRALSHAPE-001` | Spectral Shaping | Distinguish normalization, flattening, conditioning, and intentional spectral shaping of updates. | `ATLAS-CH-MATRIXOPT-001`, `ATLAS-CH-NONNORMAL-001` |
| `ATLAS-CH-OPTDYN-001` | Optimizer-State Dynamics | Analyze the coupled model–optimizer state, non-normal transients, learning-rate boundaries, and state Jacobians. | `ATLAS-CH-NONNORMAL-001`, `ATLAS-CH-OPTBASE-001` |
| `ATLAS-CH-CPS-001` | Coupling-Phase Spectroscopy | Develop optimizer-state Jacobian probes and dynamical signatures of phase and generalization-state transitions, including transition-local prediction tests. | `ATLAS-CH-OPTDYN-001` |
| `ATLAS-CH-VARIOPT-001` | Variational and Divergence-Derived Optimization | Develop divergences as geometry, discrete Lagrangians, symplectic updates, and MODULUS-style derivation of update rules. | `ATLAS-CH-NUMERICS-001`, `ATLAS-CH-MANOPT-001` |

## Part 7 — Numerical Intelligence and Composition
`ATLAS-PART-NUMINT`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-NETNUM-001` | Networks as Numerical Schemes | Recast residual networks as discretizations and distinguish local error, global error, stability, and reversibility. | `ATLAS-CH-NUMERICS-001`, `ATLAS-CH-ARCHHIST-001` |
| `ATLAS-CH-ADAPTDEPTH-001` | Adaptive Depth as Error Control | Connect learned stopping and adaptive compute to local error estimation and adaptive time stepping. | `ATLAS-CH-DEPTH-001`, `ATLAS-CH-NETNUM-001` |
| `ATLAS-CH-NEURALKRYLOV-001` | Neural Krylov Transport | Explore short-horizon preconditioned solves as representation computation. | `ATLAS-CH-KRYLOV-001`, `ATLAS-CH-TRANSPORT-001` |
| `ATLAS-CH-BOUNDARYPROBE-001` | Boundary Probes | Develop JVPs, VJPs, power iteration, sensitivity, and interface conditions for learned components. | `ATLAS-CH-LINALG-001`, `ATLAS-CH-NETNUM-001` |
| `ATLAS-CH-BCONTRACT-001` | Boundary Contracts | Define semantic and numerical interface contracts for composition, including low-order separator variables and sensitivity obligations. | `ATLAS-CH-BOUNDARYPROBE-001`, `ATLAS-CH-LOCALGLOBAL-001` |
| `ATLAS-CH-COMPOSE-001` | Composition Without Catastrophe | Study noncommutativity, error propagation, local certificates, and how separately valid pieces can fail together. | `ATLAS-CH-BCONTRACT-001`, `ATLAS-CH-SPLIT-001` |

## Part 8 — Sparse and Conditional Computation
`ATLAS-PART-SPARSE`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-SPARSE-001` | Conditional Computation | Develop sparsity, dynamic computation, token selection, conditional depth, and hardware implications. | `ATLAS-CH-DEPTH-001` |
| `ATLAS-CH-MOE-001` | Mixture-of-Experts Systems | Develop routing, capacity, load balancing, specialization, collapse, and expert parallelism. | `ATLAS-CH-SPARSE-001`, `ATLAS-CH-TRANSFORMER-001` |
| `ATLAS-CH-ROUTERDYN-001` | Router Dynamics and Diagnostics | Study churn, specialization, commutators, temporal instability, and spectral router diagnostics. | `ATLAS-CH-MOE-001`, `ATLAS-CH-OPTDYN-001` |
| `ATLAS-CH-REGRETROUTE-001` | Routing as Online Decision Making | Reframe routing through bandits, regret, optionality, and correction capacity. | `ATLAS-CH-ROUTERDYN-001` |

## Part 9 — Memory Beyond the Weights
`ATLAS-PART-MEM`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-MEMTAX-001` | A Taxonomy of Machine Memory | Distinguish parametric, working, episodic, semantic, associative, and external memory. | `ATLAS-CH-REP-001` |
| `ATLAS-CH-RETRIEVAL-001` | Retrieval and Associative Access | Develop vector, symbolic, hybrid, multi-index, and key–value retrieval. | `ATLAS-CH-MEMTAX-001`, `ATLAS-CH-ATTNOP-001` |
| `ATLAS-CH-CONTINUAL-001` | Continual Learning and Forgetting | Study replay, consolidation, EWC, parameter isolation, and catastrophic forgetting. | `ATLAS-CH-MEMTAX-001`, `ATLAS-CH-OPTBASE-001` |
| `ATLAS-CH-EXTMEM-001` | The External-Memory Thesis | Argue and test which knowledge should leave parameters and enter persistent shared memory. | `ATLAS-CH-RETRIEVAL-001`, `ATLAS-CH-CONTINUAL-001` |
| `ATLAS-CH-CONTEXTCOMP-001` | Context Compilation | Treat prompts as compiled working sets assembled from persistent, typed, provenance-aware memory. | `ATLAS-CH-EXTMEM-001` |

## Part 10 — Tokenization, Data, and Curriculum
`ATLAS-PART-DATA`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-TOKEN-001` | Tokenization and Representation Boundaries | Develop bytes, characters, subwords, BPE, unigram methods, morphology, fertility, and multilingual effects. | `ATLAS-CH-INFO-001`, `ATLAS-CH-REP-001` |
| `ATLAS-CH-TOKENCOMP-001` | Tokenization as Compression and Interface | Connect vocabulary design to description length, compute, interoperability, and tokenizer lingua francas. | `ATLAS-CH-TOKEN-001` |
| `ATLAS-CH-DATA-001` | Data Quality, Mixtures, and Contamination | Develop deduplication, quality, synthetic data, mixture weighting, contamination, and benchmark pathology. | `ATLAS-CH-EVIDENCE-001` |
| `ATLAS-CH-CURRICULUM-001` | Curriculum Learning | Study ordering, difficulty, competence, automatic curriculum construction, and state-aware data selection without assuming monotone training progress. | `ATLAS-CH-DATA-001`, `ATLAS-CH-OPTBASE-001` |
| `ATLAS-CH-PROGRESSSEARCH-001` | Learning Progress as a Search Operator | Treat learning progress and declared generalization-state evidence as feedback for choosing the next experience and searching experience space. | `ATLAS-CH-CURRICULUM-001` |
| `ATLAS-CH-MINCURR-001` | Minimal Curricula and Reasoning Bases | Ask for the smallest early mechanisms and reasoning operations from which broad later capability can be reconstructed, distinguishing acquisition, persistence, accessibility, and behavioural expression. | `ATLAS-CH-PROGRESSSEARCH-001`, `ATLAS-CH-RESIDUAL-001` |

## Part 11 — Decision Making Under Uncertainty
`ATLAS-PART-DECISION`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-RLBASE-001` | Reinforcement Learning and Control | Develop MDPs, POMDPs, Bellman equations, dynamic programming, policy methods, and model-based RL. | `ATLAS-CH-DYN-001`, `ATLAS-CH-INFO-001` |
| `ATLAS-CH-EXPLORE-001` | Exploration and Information Value | Develop bandits, exploration–exploitation, information gain, value of information, and safe exploration. | `ATLAS-CH-RLBASE-001` |
| `ATLAS-CH-REGRET-001` | Regret | Develop Bayesian and minimax regret and clarify what regret controls do and do not imply. | `ATLAS-CH-EXPLORE-001` |
| `ATLAS-CH-OPTIONALITY-001` | Optionality and Correction Capacity | Formalize the value of preserving future viable actions and recoverability under uncertainty. | `ATLAS-CH-REGRET-001` |
| `ATLAS-CH-JOINTUNC-001` | Joint Uncertainty Propagation | Treat transition, reward, observation, and future-value uncertainty jointly rather than by naive independent summation. | `ATLAS-CH-RLBASE-001`, `ATLAS-CH-INFO-001` |

## Part 12 — Diagnostics, Robustness, and Compression
`ATLAS-PART-DIAG`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-UNCERTAINTY-001` | Uncertainty and Calibration | Develop aleatoric/epistemic uncertainty, ensembles, Bayesian approximations, conformal prediction, calibration, and abstention. | `ATLAS-CH-INFO-001` |
| `ATLAS-CH-SHIFT-001` | Distribution Shift and Robustness | Develop covariate shift, concept drift, adversarial robustness, robust optimization, and structural sensitivity. | `ATLAS-CH-UNCERTAINTY-001` |
| `ATLAS-CH-MECHDIAG-001` | Mechanistic Intervention | Develop probes, ablations, activation patching, causal interventions, circuits, counterfactual substitution, and recovery tests that distinguish lost mechanisms from suppressed or inaccessible ones. | `ATLAS-CH-EVIDENCE-001`, `ATLAS-CH-TRANSFORMER-001` |
| `ATLAS-CH-SPECTRALDIAG-001` | Spectral and Operator Diagnostics | Develop singular spectra, Jacobian/Hessian spectra, pseudospectra, Koopman views, relative-position diagnostics, spectral drift, and transition-local signatures without assuming a universal scalar diagnostic. | `ATLAS-CH-NONNORMAL-001`, `ATLAS-CH-MECHDIAG-001` |
| `ATLAS-CH-COMPRESS-001` | Compression and Description Length | Develop MDL, pruning, quantization, distillation, low rank, weight sharing, and structured transforms. | `ATLAS-CH-INFO-001`, `ATLAS-CH-REP-001` |
| `ATLAS-CH-COMPINTEL-001` | Compression as Discovery and Intelligence Probe | Examine compression as discovery of reusable computation and as an empirical probe of predictive structure. | `ATLAS-CH-COMPRESS-001`, `ATLAS-CH-RESIDUAL-001` |

## Part 13 — Agents, Systems, and Hardware
`ATLAS-PART-POLITY`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-AGENTS-001` | From Models to Agents | Develop tool use, planning, search, reflection, decomposition, and bounded delegation. | `ATLAS-CH-THESIS-001` |
| `ATLAS-CH-COORD-001` | Coordination Architectures | Develop blackboards, tuple spaces, rendezvous, shared state, message passing, event-driven systems, and transactions. | `ATLAS-CH-AGENTS-001` |
| `ATLAS-CH-EVIDEX-001` | Evidence Exchange and Zero-Context Work | Treat agent outputs as candidate evidence and develop provenance, handoffs, replay, and zero-context work packets. | `ATLAS-CH-COORD-001`, `ATLAS-CH-EVIDENCE-001` |
| `ATLAS-CH-POLITY-001` | The Computational Polity | Develop intelligence as a coordinated system of models, memory, tools, humans, validators, and governance. | `ATLAS-CH-COORD-001`, `ATLAS-CH-EXTMEM-001` |
| `ATLAS-CH-HARDWARE-001` | The Machine Under the Mathematics | Develop GPUs, memory hierarchy, tensor cores, arithmetic intensity, precision, kernels, and bandwidth. | `ATLAS-CH-LINALG-001` |
| `ATLAS-CH-SYSTEMS-001` | Scaling, Parallelism, and Serving | Develop data/tensor/pipeline/expert parallelism, collectives, KV caches, batching, throughput, latency, profiling, and benchmark methodology. | `ATLAS-CH-HARDWARE-001`, `ATLAS-CH-MOE-001` |

## Part 14 — Scientific Method, Governed Adaptation, and Frontier Synthesis
`ATLAS-PART-GOV`

| Stable ID | Chapter | Contract | Depends on |
|---|---|---|---|
| `ATLAS-CH-EXPERIMENT-001` | Experiments as Arguments | Develop falsifiability, baselines, controls, ablations, counterfactuals, effect sizes, seeds, and reproducibility. | `ATLAS-CH-EVIDENCE-001` |
| `ATLAS-CH-REPLAY-001` | Replayable Evidence Objects | Develop source locking, environment pinning, exact replay, artifact capture, and semantic bridges. | `ATLAS-CH-EXPERIMENT-001`, `ATLAS-CH-EVIDEX-001` |
| `ATLAS-CH-FORMAL-001` | Formal Methods and Machine-Checkable Claims | Develop specifications, invariants, contracts, proof assistants, Lean, and the limits of formal certification. | `ATLAS-CH-REPLAY-001` |
| `ATLAS-CH-RESEARCHSM-001` | Research as a State Machine | Develop Forge → Solve → Cert, bounded work packages, independent actors, idempotence, and promotion gates. | `ATLAS-CH-REPLAY-001`, `ATLAS-CH-FORMAL-001` |
| `ATLAS-CH-GOVADAPT-001` | Governed Adaptation | Ask how systems can change themselves while preserving correction capacity, provenance, and bounded authority. | `ATLAS-CH-OPTIONALITY-001`, `ATLAS-CH-RESEARCHSM-001` |
| `ATLAS-CH-FRONTIER-001` | Frontier Questions of Adaptive Intelligence | Collect the Atlas research programme: geometry-derived optimization, operator-valued position, adaptive depth, shared memory, minimal curricula, residual structure, benign nonconvexity, and boundary contracts. | `ATLAS-CH-GOVADAPT-001`, `ATLAS-CH-RESIDUAL-001`, `ATLAS-CH-BCONTRACT-001` |
| `ATLAS-CH-SYNTHESIS-001` | Connections, Boundaries, and Open Terrain | Cross-reference important mathematical connections, alternate routes and unresolved territory without universal architecture claims. | `ATLAS-CH-FRONTIER-001`, `ATLAS-CH-POLITY-001` |

## Keystone chapter set

- `ATLAS-CH-ATTNOP-001`
- `ATLAS-CH-BCONTRACT-001`
- `ATLAS-CH-GEOM-001`
- `ATLAS-CH-NONNORMAL-001`
- `ATLAS-CH-OPTDYN-001`
- `ATLAS-CH-REPLAY-001`

## Architecture rule

Changes that alter Part-level intent, remove a keystone dependency, or change the governing conceptual spine require an ADR. Ordinary chapter refinement does not.
