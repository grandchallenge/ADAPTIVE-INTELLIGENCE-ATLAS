# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Handoff date:** 2026-10-04  
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`  
**Controller branch:** `state/atlas-controller`  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml`  
**Current main:** `356273124481084c6c4d7f9a0d5fae59fe4405cb`

This file exists so a fresh session can resume the Atlas composition programme without reconstructing state from chat history.

## 1. Mandatory restart sequence

On every fresh session or interruption:

1. Read `governance/ACTIVE_TRANSACTION.yaml` from branch `state/atlas-controller`.
2. Read this handoff file.
3. Fetch the current `main` SHA.
4. If `main` still equals the controller's recorded `baseline_commit`, execute the controller's `next_action`.
5. If `main` has advanced, recompute the dependency-legal frontier from `governance/CHAPTER_LEDGER.yaml` before instantiating new work.
6. Do not reconstruct live execution state from conversational memory when repository state is available.

## 2. Execution protocol

The Atlas uses transaction-mode execution.

For one bounded chapter tranche, carry the work through the full real boundary:

- create issue;
- create work branch from recorded baseline;
- lock exact prerequisites and external sources;
- write chapter specification;
- write formal/derivation or documentary packet;
- add a computational witness only when it materially clarifies the claim;
- write the full manuscript prose;
- update Chapter Ledger;
- update Source Register;
- write tranche receipt;
- open implementation PR;
- run repository validation;
- repair all in-scope defects until green;
- merge implementation PR;
- instantiate bounded post-draft audit;
- repair every in-scope audit defect;
- write audit record;
- open audit PR;
- validate and merge;
- verify issues closed/completed;
- recompute the dependency-legal frontier;
- return controller to `idle-ready` with the new baseline and next action.

Legitimate stop conditions are only:

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.

Do not hand back merely because an intermediate step completed.

## 3. Working style

Execute in short durable bursts.

Checkpoint live state to `governance/ACTIVE_TRANSACTION.yaml` whenever the transaction crosses a real phase boundary.

Avoid progress-only handbacks. A user message such as `next`, `resume`, `continue`, `proceed`, or `make it so` means: read the durable controller and continue the recorded transaction.

## 4. Current state

The controller will be reset to:

- state: `idle-ready`;
- baseline/main: `356273124481084c6c4d7f9a0d5fae59fe4405cb`;
- next target: `ATLAS-CH-COMPRESS-001`;
- title: **Compression and Description Length**;
- reason: after SECOND-001 audit closure, the dependency-legal frontier has no count-2 leader. The top tier is a count-1 tie, and deterministic ordering selects COMPRESS-001 first.

Current frontier, recomputed from the live post-AUDIT-041 Chapter Ledger:

1. `ATLAS-CH-COMPRESS-001` — downstream architecture count 1; direct consumer `ATLAS-CH-COMPINTEL-001`.
2. Other count-1 entries include `ATLAS-CH-FRONTIER-001`, `ATLAS-CH-HARDWARE-001`, `ATLAS-CH-MANOPT-001`, `ATLAS-CH-MATRIXOPT-001`, `ATLAS-CH-MECHDIAG-001`, `ATLAS-CH-POLITY-001`, `ATLAS-CH-PROGRESSSEARCH-001`, `ATLAS-CH-ROUTERDYN-001`, `ATLAS-CH-RPO-001`, `ATLAS-CH-TOKEN-001`, `ATLAS-CH-TRANSPORT-001`, and `ATLAS-CH-UNCERTAINTY-001`.

SECOND-001 is now audited `draft-v0.1`. Its direct consumer `ATLAS-CH-MATRIXOPT-001` is newly dependency-legal.

## 5. Immediately preceding completed tranches

### SECOND-001 — Curvature and Second-Order Structure

- implementation issue: #163, closed completed;
- implementation PR: #164;
- implementation merge: `62e341cc87130dc1b937da4f126bdc0b9eb9d17a`;
- audit: `AUDIT-041`;
- audit issue: #165, closed completed;
- audit PR: #166;
- audit merge / current main: `356273124481084c6c4d7f9a0d5fae59fe4405cb`.

Core exact objects:

- local quadratic model `f(x)+g^T p + 1/2 p^T H p`;
- Newton equation `Hp=-g`;
- positive-definite descent identity `g^T p_N=-g^T H^{-1}g<0`;
- explicit indefinite-curvature counterexample where raw Newton is ascent;
- trust-region model with radius `Delta`;
- Hessian-vector products without explicit Hessian formation;
- Fisher metric and natural-gradient distinction;
- quasi-Newton secant relation `B s=y`;
- proximal operator and soft-threshold witness.

Exact witnesses:

- SPD quadratic: `H=diag(1,4)`, `b=(1,1)^T`, Newton step `(1,1/4)^T`, objective `0 -> -5/8`;
- indefinite control: `f(x,y)=1/2(x^2-y^2)` at `(0,1)`, raw Newton direction has `g^T p_N=1>0` and raises the objective to `0`;
- trust-region radius `1` selects `p=(0,1)^T` and lowers the objective to `-2`;
- metric witness: `G=diag(1,4)`, Euclidean direction `(-1,-1)^T`, metric direction `(-1,-1/4)^T`;
- proximal threshold `1`: `3->2`, `-3->-2`, `1/2->0`.

AUDIT-041 found no mathematical or prose reversal. It repaired one source-metadata omission by adding the canonical Parikh–Boyd DOI `10.1561/2400000003` and publisher locator.

Load-bearing boundary: local second-order structure does not by itself establish global convexity, global optimality, or universal optimizer superiority.


### POSGEOM-001 — The Geometry of Position

- implementation issue: #159, closed completed;
- implementation PR: #160;
- implementation merge: `26c51843b13a0ab58ba0f16cd0c2e365a60d1180`;
- audit: `AUDIT-040`;
- audit issue: #161, closed completed;
- audit PR: #162;
- audit merge / current main: `8fbae32144f94e497203b311cc0a824f8cd8a486`.

Core exact objects:

- 2D rotation block `R(phi)`;
- position-indexed family `R_m(omega)=R(m omega)`;
- exact identity `R_m^T R_n=R((n-m)omega)`;
- transformed score identity `(R_m q)^T(R_n k)=q^T R((n-m)omega)k`;
- block-diagonal multi-frequency extension;
- coordinate-wise direct-product multidimensional extension;
- explicit separation between positional algebra and model-level long-context behavior.

Exact witness:

- `theta=pi/6`, `q=k=(1,0)^T`;
- same-offset pairs `(0,2)` and `(3,5)` both score `1/2`;
- different-offset pair `(1,4)` scores `0`;
- generic-vector replay with `q=(1,2)^T`, `k=(3,-1)^T`, `m=2`, `n=5` gives `7` in both direct and relative forms.

Non-orthogonal control:

- `S_m=diag(2^m,1)`;
- same-offset pair `(0,2)` scores `4`;
- same-offset pair `(3,5)` scores `256`;
- therefore equal relative displacement alone does not determine the transformed inner product without the required transform-family structure.

Long-context boundary:

- Position Interpolation and YaRN are treated as paper-scoped context-extension methods;
- exact continuation of the positional formula is not promoted into a universal theorem of retrieval quality, calibration, optimization stability, or arbitrary-length generalization.

Implementation CI initially caught a serialization defect: LaTeX backslash escapes in the manuscript had produced control characters. The manuscript was rewritten through raw-string serialization, all POSGEOM artifacts were rescanned byte-clean, and exact repaired head `ddea383a6c1ffa1a89ed8892d3c900e28940d804` passed canonical validation.

AUDIT-040 found no further mathematical, source-scope, prose, or repository repair.

Load-bearing boundary: `formula extrapolates` does not imply `trained model generalizes`.


### KRYLOV-001 — Krylov Subspaces and Iterative Solves

- implementation issue: #155, closed completed;
- implementation PR: #156;
- implementation merge: `4fb9bbd05c3f48e3b69a72eaee171487576b5c48`;
- audit: `AUDIT-039`;
- audit issue: #157, closed completed;
- audit PR: #158;
- audit merge / current main: `df99382bf263423fea72bcf75d2d222c19112031`.

Core classical objects:

- `K_m(A,r_0)=span{r_0,Ar_0,...,A^(m-1)r_0}`;
- Arnoldi relation `A V_m = V_(m+1) Hbar_m`;
- symmetric/Hermitian Lanczos three-term specialization;
- Galerkin residual orthogonality;
- minimum-residual least-squares projection;
- residual/error relation `A e_m=r_m`;
- left/right preconditioning as changes of effective operator;
- matrix-free operator-vector access;
- finite-precision orthogonality/restart boundary.

Exact witness:

- `A=diag(1,2,4)`, `b=(1,1,1)^T`, `x_0=0`;
- `V=[b,Ab]`;
- reduced matrix `[[7,21],[21,73]]`;
- reduced RHS `[3,7]^T`;
- coefficients `[36/35,-1/5]^T`;
- `x_2=[29/35,22/35,8/35]^T`;
- `r_2=[6,-9,3]^T/35`;
- `V^T r_2=0`;
- `||r_2||_2^2=18/175`;
- Lanczos replay gives `alpha_1=7/3`, `beta_1=sqrt(14)/3`, `alpha_2=59/21`, `beta_2=3sqrt(3)/7`.

Conditioning control:

- `A_c=diag(1,100,10000)`;
- one-step SPD Galerkin/CG coefficient `1/3367`;
- Euclidean residual norm squared increases from `3` to `19602/3367`;
- energy-error norm squared decreases from `10101/10000` to `33980067/33670000`.

AUDIT-039 found no mathematical reversal. It canonicalized the artifact placement after a recoverable connector-filter workaround, restored the canonical reader title and exact source-lock reference, removed temporary duplicate artifacts, added the transaction receipt, and restored implementation issue metadata.

Load-bearing boundary: classical Krylov structure does not by itself establish rapid convergence for arbitrary operators, Euclidean error from residual alone, or convergence guarantees for learned nonlinear Neural Krylov Transport.


### GOVADAPT-001 — Governed Adaptation

- implementation issue: #149, closed completed;
- implementation PR: #150;
- implementation merge: `c0db4e60ba1fb9d3f2d7ac4469ca40bb5a761784`;
- audit: `AUDIT-038`;
- audit issue: #151, closed completed;
- audit PR: #153;
- audit merge / current main: `574de4e65b42d4c090467b8a43fe2e534653b6e9`.

Core governed-adaptation objects:

- protected state `g=(r,x,E,A,P,C,L)`;
- candidate revision bound to an exact parent and exact candidate identity;
- separate proposal, execution, promotion, recovery, and certification authority;
- exact-target evidence binding and fresh replay after identity-changing repair;
- authorized recovery-path semantics distinct from stored rollback artifacts;
- inherited correction-capacity semantics from OPTIONALITY;
- fail-closed safety versus liveness.

Exact witness:

- one common protected baseline state `x_0`;
- two candidate post-revision states `x_A` and `x_B`;
- equal immediate utility increments from the same baseline;
- `CC_{h,0}(x_A;b)=1`;
- `CC_{h,0}(x_B;b)=1/2`;
- an immediate-utility-only gate cannot distinguish the candidates;
- a declared correction-capacity floor can distinguish them;
- equal raw command counts do not imply equal governed recoverability.

AUDIT-038 repaired three precision defects:

1. corrected the Corrigibility bibliography/source-lock author order;
2. restored the inherited correction-capacity type by applying it to post-revision states rather than candidate labels;
3. made equal immediate utility explicitly relative to one common protected reference state.

Load-bearing boundary: governance conformance establishes satisfaction of a declared authority/evidence process; it does not by itself establish substantive truth, universal safety, complete corrigibility, or universally optimal adaptation.


### CURRICULUM-001 — Curriculum Learning

- implementation issue: #145, closed completed;
- implementation PR: #146;
- implementation merge: `4c28148b2e9d09bf5f5ea3241e49141aeaa33d7f`;
- audit: `AUDIT-037`;
- audit issue: #147, closed completed;
- audit PR: #148;
- audit merge / current main: `ae2ce726fa4f24fc52289a1f2e6bbbaff9232d11`.

Core curriculum objects:

- model state `theta_t`, optimizer state `u_t`, curriculum state `c_t`;
- controller observation `z_t`;
- open-loop schedule versus closed-loop state-aware policy;
- declared difficulty score and competence threshold;
- oriented finite-difference learning-progress signal;
- sample selection versus mixture reweighting;
- explicit post-update controller feedback;
- curriculum-effect separation from compute, exposure, and optimizer confounds.

Exact witness:

- state `s=(e,h) in {0,1,2}^2`;
- repeatable experience types `E` and `H`;
- static ranking `d(E)=1<2=d(H)`;
- toy controller has full state observation `z=s`;
- at `(0,0)`, rewards are `R(E)=1, R(H)=0`;
- at `(2,0)`, rewards are `R(E)=0, R(H)=1`;
- therefore no state-independent deterministic first action is one-step progress-optimal for both states;
- from `(2,0)`, fixed `E,H` gives cumulative toy progress 1, while state-aware `H,H` gives 2 under an equal two-transition budget.

AUDIT-037 repaired three precision defects:

1. defined the controller-visible post-update feedback symbol;
2. made progress orientation explicit for higher- versus lower-is-better metrics;
3. declared full toy-state observability and repeatable action semantics.

Load-bearing boundary: learning-progress signals can control a curriculum without proving acquisition, persistence, accessibility, internal mechanism identity, or long-horizon curriculum optimality.


### SPLIT-001 — Split-Operator Networks

- implementation issue: #141, closed completed;
- implementation PR: #142;
- implementation merge: `2776a2d77fff39e90bd58a866b0275d946909fa9`;
- audit: `AUDIT-036`;
- audit issue: #143, closed completed;
- audit PR: #144;
- audit merge / current main: `c1122f3b6a6cb0170e77f5fe340a7bec402618ce`.

Core exact reference objects:

- product-labeled Lie compositions `S_AB(h)=exp(hA)exp(hB)` and `S_BA(h)=exp(hB)exp(hA)`;
- explicit column-vector rule that products act right-to-left;
- commutator `[A,B]=AB-BA`;
- Strang composition `exp(hA/2)exp(hB)exp(hA/2)`;
- learned submaps `Psi_A(H)=H+F_A(N_A(H))` and `Psi_B(H)=H+F_B(N_B(H))`;
- additive versus sequential residual composition;
- shared/autonomous versus layer-varying/nonautonomous semantics;
- explicit splitting-versus-learning error taxonomy.

Exact witness:

- `A=[[0,1],[0,0]]`, `B=[[0,0],[1,0]]`;
- `A^2=B^2=0`;
- `[A,B]=diag(1,-1)`;
- `S_AB-S_BA=h^2[A,B]` exactly;
- `S_AB-exp(h(A+B))=(h^2/2)[A,B]+O(h^3)`;
- reversing product order flips the leading commutator sign;
- the declared Strang witness has local defect `O(h^3)`;
- the diagonal commuting control has exact order independence;
- at `h=1/2`, Lie Frobenius error is approximately `0.1793148493970293`, while the Strang witness error is approximately `0.02370487546729764`.

AUDIT-036 repaired four precision defects:

1. separated matrix-product labels from chronological execution order;
2. required an explicit step-parameterized learned-map family before neural half-step/Strang language is meaningful;
3. distinguished the derivative of the nonlinear composition defect from a same-state Jacobian commutator diagnostic;
4. repaired malformed inline TeX introduced during the implementation write.

Load-bearing boundary: arbitrary learned neural blocks do not inherit exact-flow, Strang-order, reversibility, symplecticity, or convergence claims merely from a split-operator analogy.


### GSD-001 — Executable Generalization-State Dynamics Programme

- planning issue: #139;
- programme PR: #140;
- protected merge / current main: `b87bad6229896174e6c872994d6a0f4878e2e1d5`;
- human plan: `governance/research-agenda/GSD-001_RESEARCH_PROGRAMME.md`;
- machine-readable WP index: `governance/research-agenda/GSD-001_WORK_PACKAGE_INDEX.yaml`.

Execution is gated. The immediate research tranche is only `GSD-WP00` through `GSD-WP03`: evaluator fidelity, 1B checkpoint harness, transition catalogue, and adversarial transition validation.

Later work is conditional:
- recovery/Residual, K-DIAGNOSTICS, and CPS require a confirmed soft-margin transition;
- curriculum control requires a supported data-window attribution;
- Muon/MODULUS and nGPT/RUNT comparisons require a controlled state regime;
- OLMo3-32B and post-training confirmation require held-out predictive value at smaller scale.

The programme keeps capacity allocation as a hypothesis and treats negative gates as compute-saving scientific results.

### RESEARCHSM-001 — Research as a State Machine

- implementation issue: #136;
- implementation PR: #137;
- implementation merge: `a796eb3ae822c3bf998b27de94db7213646d2c59`;
- audit: `AUDIT-035`;
- audit issue/PR: #138;
- audit merge / current main: `8fa6a51dfdb7a51c5d5975ea0f2e84c252cbdd39`.

Core research-state objects:

- bounded work package `W=(id,Q,B,S,D,R,A,Z)`;
- product research state `x=(q,E,U,J,P,C,L)`;
- typed guarded transitions;
- canonical-state/history separation;
- exact-identity duplicate relation;
- canonically idempotent retry and advancement;
- separate programme-disposition and certification coordinates;
- explicit actor-separation predicates;
- typed failure/recovery classes.

Exact witness:

- first capture of `(17,A)` creates one canonical evidence identity;
- exact retry leaves the canonical evidence count at one;
- distinct result `(17,B)` raises the preserved count to two;
- advancement vector `(1,1,1,1,0)` evaluates to `0`;
- advancement vector `(1,1,1,1,1)` evaluates to `1`;
- missing-check vector `(1,1,0,1,1)` evaluates to `0`;
- exact repeated advancement has one canonical set-insertion effect;
- same-actor separation predicate gives `Sep(A,A)=0`;
- a fail-closed execution can preserve every declared safety invariant while never reaching advancement.

Pinned public GCL evidence:

- lifecycle controller blob `91dca167b4b9c2dd15be41fb1996211752120f27`;
- Frontier Advancement Gate blob `4145981b5ba85527c49b83a3440b0632db9924ca`;
- Controlled Epistemic Interface blob `33164987c3f5484863ab31606034060e72b7148a`;
- all pinned at `grandchallenge/MATH-PROGRAMME@fdd7a3fe3df7b2d699753347080c1cbc2127e02d`.

AUDIT-035 repaired a substantive implementation incompleteness:

1. completed the manuscript beyond the retry witness with advancement, actor separation, certification, safety/liveness, recovery, public-case-study, failure-mode, and GOVADAPT sections;
2. completed the computational witness with the required Boolean gate, idempotent advancement, same-actor separation failure, and safety-without-liveness execution;
3. completed the formal packet with explicit advancement/certification state, recovery classes, and public GCL lifecycle mapping.

Load-bearing boundary: workflow conformance does not establish mathematical truth, actor-label difference does not prove epistemic independence, and fail-closed safety does not imply eventual progress.

### AGENDA-GSD-001 — Generalization-State Dynamics

- governing issue: #133;
- implementation PR: #134;
- protected merge / current main: `889193744d0ae1bdd6ae6bd0d6328becbc5b3eaf`;
- motivating source: arXiv:2609.33150v1;
- durable agenda artifact: `governance/research-agenda/AGENDA-GSD-001.md`.

Durable rule:

**Do not infer monotone mechanism improvement from smooth loss, more training, or endpoint benchmarks. Treat checkpoints as potentially distinct computational states, and separate acquisition, persistence, accessibility, and behavioural expression.**

The integration sharpened future architecture contracts for CPS, Curriculum, Learning Progress as Search, Minimal Curricula/Reasoning Bases, Mechanistic Intervention, and Spectral/Operator Diagnostics. It did not change the 80-chapter dependency graph.

Claim firewall:

- capacity allocation remains a hypothesis;
- behavioural change does not by itself prove mechanism change;
- no scalar diagnostic is presumed universal;
- recovery evidence is conditional on a declared intervention class.

### OPTIONALITY-001 — Optionality and Correction Capacity

- implementation merge: `7eb2d23b77b612ed86db7ba50df6177f58df7bdf`;
- audit: `AUDIT-034`;
- audit PR: #132;
- audit merge: `b625a34280567345fb2829c6aff184561bd11757`.

The audited chapter distinguishes present value, future feasible-action sets, recoverability, and ex-ante correction capacity, with explicit conditional viable sets and comparator semantics.


### OPTIONALITY-001 — Optionality and Correction Capacity

- implementation issue: #129;
- implementation PR: #130;
- implementation merge: `7eb2d23b77b612ed86db7ba50df6177f58df7bdf`;
- audit: `AUDIT-034`;
- audit issue: #131;
- audit PR: #132;
- audit merge / current main: `b625a34280567345fb2829c6aff184561bd11757`.

Durable optionality objects:

- viable continuation set `V_h(s)`;
- consequence quotient `O_h(s)=V_h(s)/~_s`;
- conditional post-evidence viable set `V_h(s;theta)`;
- extended-real correction cost `k_h(s,theta)`;
- conditional correction indicator `C_{h,epsilon}(s,theta)`;
- ex-ante correction capacity `CC_{h,epsilon}(s;b)=E_b[C_{h,epsilon}(s,theta)]`;
- horizon-relative recoverability.

Exact witness:

- environment `Theta={L,R}`, symmetric prior;
- declared stage-0 action set `{P,C_L,C_R}`;
- preserve and commit-left both have prior expected return `1/2`;
- both have Bayesian regret `1/2` against the explicitly clairvoyant `C_theta` comparator;
- worst-case regret is `1/2` versus `1`;
- functional option count is `2` versus `1`;
- zero-tolerance ex-ante correction capacity is `1` versus `1/2`;
- both branches acquire exactly one bit of information.

AUDIT-034 repaired three precision defects without changing the arithmetic:

1. `C_R` and the clairvoyant comparator action class are now explicitly declared;
2. post-evidence conditional correction feasibility is distinct from the pre-evidence belief-weighted `CC`;
3. the Aubin source lock now binds the original 1991 Birkhäuser Boston print identity, ISBN `9780817635718`.

Load-bearing boundary: optionality is an explicit objective, constraint, or diagnostic; it is not a universal injunction against commitment and does not imply safety, robustness, or low regret.

### MOE-001 — Mixture-of-Experts Systems

- implementation PR: #127;
- implementation merge: `5090ed112ee086450387a8465772ec9a2358c410`;
- audit: `AUDIT-033`;
- audit issue/PR: #128;
- audit merge / current main: `39f419abb72c941e041f92f2834229f9968da006`.

Core routing objects:

- router probabilities `p_{i,e}`;
- preferred top-k route `P_i`;
- accepted dispatch `a_{i,e}`;
- expert token load `n_e`;
- router probability mass `m_e`;
- expert capacity `C`;
- overflow policy;
- expert/device placement.

Exact witness:

- six tokens, three experts, top-1, capacity 2;
- naive preferred loads `(3,2,1)`;
- rerouting t3 from overloaded E1 to available E3 yields accepted loads `(2,2,2)`;
- router probability mass remains `(47/20,2,33/20)`, normalized to `(47/120,1/3,11/40)`;
- count imbalance is `0`, probability-mass imbalance is `49/7200`;
- toy utility totals remain unequal at `(8,4,2)`;
- drop-overflow instead gives loads `(2,2,1)`, drop rate `1/6`, and expert arithmetic `5c` instead of `6c`.

Load-bearing distinctions:

- router probability versus preferred route versus accepted dispatch;
- capacity/overflow semantics versus router preference;
- accepted-count balance versus probability-mass balance;
- traffic balance versus expert usefulness/specialization;
- preferred-router concentration versus accepted-load concentration;
- expert underuse versus functional redundancy versus capacity overload;
- auxiliary balance objective versus task objective;
- expert arithmetic versus communication/system cost.

AUDIT-033 repairs:

- made top-k explicitly a preferred route before capacity/overflow;
- separated preferred-router concentration from accepted-load concentration because capacity can mask collapsed preferences;
- replaced ambiguous `capacity collapse` language with `capacity overload`.

### LOCALGLOBAL-001 — Local-to-Global Mathematics

- implementation PR: #125;
- implementation merge: `ca04c7f4dc854c0d5176f2d66c422475ebc0907e`;
- audit: `AUDIT-032`;
- audit issue/PR: #126;
- audit merge / current main: `a15170c608c5b83048ce2310e68e527e041438cb`.

Central local-to-global structure:

- section spaces `F(U)`;
- restriction maps `rho^U_V:F(U)->F(V)`;
- matching families on overlaps;
- gluing existence and uniqueness;
- finite discrepancy/obstruction maps.

Exact witness:

- `X={a,b,c}`, `U={a,b}`, `V={b,c}`;
- global-to-local map `R(x,y,z)=(x,y,y,z)`;
- overlap discrepancy `Delta(u_a,u_b,v_b,v_c)=u_b-v_b`;
- `R` injective and `im(R)=ker(Delta)`;
- local sections `(1,2)` and `(2,4)` glue uniquely to `(1,2,4)`;
- local sections `(1,2)` and `(3,4)` have discrepancy `-1` and cannot glue.

Load-bearing distinctions:

- graph/cover incidence versus data and maps carried over it;
- presheaf restriction structure versus sheaf unique gluing;
- gluing existence versus uniqueness;
- exact compatibility versus approximate fusion;
- global consistency versus factual truth or semantic adequacy.

AUDIT-032 repairs:

- changed the general discrepancy target to one component per pair `i<j`, removing redundant ordered/diagonal overlap terms;
- replaced the witness's `xor` placeholder with direct-sum terminology.

### EXTMEM-001 — The External-Memory Thesis

- implementation PR: #122;
- implementation merge: `c775a398062736c372f13f65dd2bb7349c2796c7`;
- audit: `AUDIT-031`;
- audit issue: #123;
- audit PR: #124;
- audit merge / current main: `ed3f07a2531c520e0fad43f072340f8099448098`.

Central placement descriptor:

`Place(k)=(V,P,S,D,R,L,H,A,G)`

for volatility, provenance/audit need, sharing scope, deletion/supersession need, retrievability, latency, availability/failure tolerance, access control/privacy, and value of parametric generalization/compression.

Load-bearing distinctions:

- parametric knowledge versus explicit external records;
- external locus versus persistent lifetime;
- storage correctness versus retrieval/use correctness;
- record-local update versus systems cost;
- provenance visibility versus factual correctness;
- authoritative update versus consumer freshness;
- shared store versus synchronized effective memory;
- externalization versus later consolidation into parameters.

Exact witness:

- initial parametric state `theta=(1,1)` represents `A=2,B=0`;
- updating only A to 4 while preserving B requires `theta'=(2,2)`;
- naive one-coordinate edit `(2,1)` yields `A=3,B=1`;
- versioned external memory marks A/v1 superseded and A/v2 current while B is unchanged;
- latest read returns A=4, while a stale snapshot still returns A=2.

AUDIT-031 repairs:

- split latency and availability/failure tolerance into separate placement coordinates;
- preserved the inherited distinction between external locus and persistent lifetime;
- made the witness's supersession state explicit so only one A version is current.

### DATA-001 — Data Quality, Mixtures, and Contamination

- implementation PR: #119;
- implementation merge: `703e763cac01d224eec87aeeca43d5f1acf9c58c`;
- audit: `AUDIT-030`;
- audit issue: #120;
- audit PR: #121;
- audit merge / current main: `7604f00fe257ade14adf01718bda0b8f9aa8feb9`.

Central data object:

`D=(R,S,P,Phi,Delta,mu,E)`

for records, sources/domains, provenance/lineage, processing pipeline, duplicate/overlap predicates, sampling measure, and evaluation boundary.

Load-bearing distinctions:

- exact duplication versus near duplication versus semantic redundancy;
- raw corpus proportions versus post-filter/dedup proportions versus training sampling weights;
- synthetic provenance versus quality judgment;
- detected overlap versus memorization versus causal benchmark-score effects;
- unweighted item contamination rate versus weighted evaluation measures;
- publication date versus actual pre-cutoff content availability.

Exact witness:

- exact overlap rate `1/3`;
- near-overlap rate `2/3` at token-Jaccard threshold `3/4`;
- raw training count `5`;
- exact-dedup representatives `4`;
- near-duplicate graph clusters `3`;
- raw domain proportions `(2/5,1/5,1/5,1/5)`;
- exact-dedup proportions `(1/4,1/4,1/4,1/4)`;
- declared training weights `(1/2,1/4,1/8,1/8)`.

AUDIT-030 repairs:

- named the chapter's contamination-rate formula as the unweighted item rate and required explicit weights for weighted evaluation;
- required a declared counting unit before corpus/mixture proportions are interpreted;
- repaired the temporal boundary so post-cutoff benchmark publication alone is not treated as proof that the content did not exist earlier.

### BOUNDARYPROBE-001 — Boundary Probes

- implementation PR: #116;
- implementation merge: `a6ef32bbd43347907833b0812cb776162ade01c6`;
- audit: `AUDIT-029`;
- audit issue: #117;
- audit PR: #118;
- audit merge / current main: `53583191c96a9657bbb247d683c25ee9f7bedacf`.

Central probe objects:

- JVP: `J_F(x)v`;
- VJP under the declared Euclidean coordinate convention: `J_F(x)^T w`;
- local Euclidean gain: `sigma_max(J_F(x))`;
- power iteration on `J^T J`;
- boundary-probe contract `B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`.

Exact witness:

- nonlinear map `F(x1,x2)=(x1^2+x2,x1+2x2)` at `x0=(1,1)`;
- exact Jacobian `[[2,1],[1,2]]`;
- singular values `3,1`;
- JVP `(3,3)`, VJP `(4,5)`, exact pairing value `9`;
- exact nonlinear remainder `(epsilon^2,0)`;
- mixed-start Rayleigh values `365/41`, `29525/3281` approach `9`;
- weak-eigenspace initialization remains at Rayleigh value `1` despite true singular norm `3`.

AUDIT-029 repairs:

- made the Euclidean coordinate/inner-product convention explicit for `J^T w`;
- separated a finite monitoring estimate `hat sigma <= tau` from the stronger true-norm claim `||J||_2 <= tau`;
- aligned the Griewank–Walther bibliography record with the locked second-edition SIAM source identity.

### SPARSE-001 — Conditional Computation

- implementation PR: #114;
- implementation merge: `817cc0267c48235c50024a26f5473e1b4de0f935`;
- audit: `AUDIT-028`;
- audit PR: #115;
- audit merge / current main: `c82f61da1ca457b9670273669c04fe3fd5459652`.

Central sparsity/conditional-computation object:

`S=(P,A,T,B,D,R)`

for parameter sparsity, activation sparsity, token sparsity, block/module sparsity, conditional depth, and routing.

Load-bearing distinctions:

- static sparsity versus input/state-dependent conditional execution;
- hard skipped work versus soft gating;
- router cost versus executed-path cost;
- average versus peak/tail compute;
- total capacity versus active per-input work;
- arithmetic operations versus launches, memory traffic, energy, communication, latency, and throughput;
- training graph versus inference graph;
- efficiency versus task-quality preservation.

Exact witness:

- fixed resource pair `(40,1)`;
- conditional average `(55/2,15/4)`;
- average arithmetic reduction `5/16=31.25%`;
- unchanged peak arithmetic `40`;
- compute-dominated toy cost favors conditional execution;
- launch-dominated toy cost favors fixed execution.

AUDIT-028 repairs:

- aligned the primitive resource vector to `C=(F,K,M,E)`, keeping latency/throughput as hardware-dependent modeled or measured outputs;
- aligned the Roofline manuscript title with the locked CACM source identity.

### RETRIEVAL-001 — Retrieval and Associative Access

- implementation PR: #112;
- implementation merge: `e675cf95bb4a8df788bc96aed0b786b21d9fcb96`;
- audit: `AUDIT-027`;
- audit PR: #113;
- audit merge / current main: `98e146cbd150625ecac4a5f1416da221ec7abff3`.

Central retrieval contract:

`Retr=(D,Q,F,s,pi,k,O)`.

Load-bearing distinctions:

- exact-key, symbolic, sparse, dense/vector, hybrid, and multi-index access remain distinct;
- ranking score is not calibrated relevance probability;
- top-k is an ordered truncation, not a completeness theorem;
- exact nearest-neighbor and ANN semantics remain distinct;
- logical record identity and index-entry identity remain separate;
- retrieval rank does not create provenance or authority;
- retrieval-contract correctness, task relevance, and downstream usefulness are separate evaluation layers.

Exact witness:

- exact-key `id=B` -> B;
- symbolic `year>=2024` -> `{A,C}`;
- vector ranking -> `C,A,B`;
- paper-filter then rank top-1 -> A;
- rank top-1 then paper-filter -> empty.

AUDIT-027 repairs:

- renamed the complete retrieval tuple from `R` to `Retr` to preserve the MEMTAX read-path coordinate;
- made top-k an ordered list with a separate selected-set view.

### REGRET-001 — Regret

- implementation PR: #110;
- implementation merge:
  `915911dfd5b6b6daf7084edd75e2341d7a727d10`;
- audit:
  `AUDIT-026`;
- audit PR: #111;
- audit merge / current main:
  `e1709bc5744a260c0a1eec5234d5ac4cb261b3b7`.

Central regret contract:

- horizon `T`;
- environment `theta` or class `Theta`;
- admissible policy class `Pi`;
- reward/loss convention;
- comparator;
- expectation/prior convention.

Load-bearing distinctions:

- pathwise mean-benchmark regret versus expected/pseudo-regret;
- Bayesian regret versus worst-case/minimax regret;
- fixed versus dynamic comparator classes;
- cumulative regret versus simple/final recommendation regret;
- sublinear cumulative regret versus zero/bounded regret;
- regret guarantees versus safety, fairness, calibration, robustness, tail risk, recoverability, and optionality.

Exact witnesses:

- two-round Bernoulli example: pseudo-regret `1`, while pathwise regret takes `3/2`, `1/2`, or `-1/2` and has expectation `1`;
- one-step two-environment example: minimax policy uses `q=1/2` with regret `1/2`, while prior `9/10,1/10` makes `q=1` Bayes-optimal with Bayes regret `1/10` and worst-case regret `1`;
- one fixed learner trajectory has regret `0` against the best fixed action and `1` against an unrestricted dynamic comparator;
- one exploration sequence has cumulative regret `1` and simple regret `0`.

AUDIT-026 repairs:

- bound Bayesian/minimax optimization to an explicit admissible policy class `Pi`;
- replaced the general comparator-class `max` with `sup`, while preserving the finite witness maximum.

### FORMAL-001 — Formal Methods and Machine-Checkable Claims

- implementation PR: #107;
- implementation merge:
  `ea4b586d2b2c4a2e664345613ec7300c5e18ffda`;
- audit:
  `AUDIT-025`;
- audit PR: #108;
- audit merge / current main:
  `f94a18010d969f80ddb96663bec02e449f4eb5eb`;
- duplicate audit issue #109 was closed as duplicate after a connector retry partially succeeded.

Central formal-support object set:

`F=(R,S,M,P,K,I,W)`

for requirement, formal specification, model/semantics, checked support object, checker/kernel, implementation, and deployed world.

Typed support relations:

- `Formalizes(S,R)`;
- `Interprets(M,S)`;
- `Checks(K,P,S,M)`;
- `Conforms(I,M)`;
- `AssumptionsHold(W,M)`.

Load-bearing doctrine:

- proof of a formal statement does not automatically prove adequacy of the human requirement;
- a proved model does not automatically imply implementation conformance;
- a machine-checked theorem remains conditional on its logic, axioms, definitions, trust base, and assumptions;
- finite successful tests are not universal proofs without a completeness bridge;
- replayability and formal proof are complementary, non-equivalent support routes;
- theorem checking and institutional certification remain distinct states.

Exact witness:

- specification `x_0=0`, `SpecStep(x)=x+2`, invariant `Even(x)`;
- induction proves every specified reachable state is even;
- implementation tests `0->2->4->6` pass;
- divergent implementation then maps `6->7`, violating both conformance and the invariant.

AUDIT-025 repairs:

- removed a mutable Lean `latest` documentation URL from the load-bearing source/citation chain because it did not satisfy the inherited immutable-identity discipline;
- replaced the misleading linear claim stack with the typed support graph above.

### CONTINUAL-001 — Continual Learning and Forgetting

- implementation PR: #105;
- implementation merge:
  `b726917e1b40d37ce0f0459035ef9b7e07e0fa6b`;
- audit:
  `AUDIT-024`;
- audit PR: #106;
- audit merge / current main:
  `c257c8400a329cb127ac322cf8bfb70d4693b10c`.

Central evaluation object:

- performance-through-time score `R_{i,j}`;
- encountered-context lower triangle for retention/forgetting;
- optional full matrix plus untrained/reference baseline for forward-transfer claims;
- per-context endpoint forgetting
  `F_j=max(0,max_{k=j,...,T-1}R_{k,j}-R_{T,j})`;
- average and worst-context summaries only when scores are commensurate or explicitly normalized.

Mechanism distinctions:

- replay restores earlier evidence to optimization;
- EWC adds a Fisher-weighted local quadratic parameter penalty;
- GEM uses episodic-memory gradients to constrain first-order update directions;
- parameter isolation prevents direct overwrite by changing the writable-capacity/routing contract.

Exact witness:

`L_A(w)=(1/2)(w+1)^2`,
`L_B(w)=(1/2)(w-1)^2`.

Sequential B-only training raises old-task loss from `0` to `2`.

For

`J_lambda=L_B+(lambda/2)(w+1)^2`,

`w_lambda=(1-lambda)/(1+lambda)`.

At `lambda=1`, both task losses are `1/2`.

Equal-weight replay reaches the same point only because the old task loss is exactly the chosen quadratic penalty. Two isolated task-selected parameters reach zero/zero only by adding capacity and routing.

AUDIT-024 repairs:

- bounded forgetting aggregation to `T>=2` and commensurate/normalized cross-context score scales;
- separated lower-triangular retention evaluation from forward-transfer evaluation, which requires future-context scores plus a baseline.

### NETNUM-001 — Networks as Numerical Schemes

- implementation PR: #103;
- implementation merge:
  `e7c0cda1a96f23e78120c02f66511488612a4035`;
- audit:
  `AUDIT-023`;
- audit PR: #104;
- audit merge / current main:
  `8a08c5db5322f027dd9214618f21ed88ce9255c0`.

Central numerical-network interface:

- residual map `x_{k+1}=x_k+F_k(x_k)`;
- declared continuous reference `dx/dt=f(t,x)`;
- Euler bridge `F_k(x)=h_k f(t_k,x)`;
- local defect relative to exact flow;
- global error over a declared refinement family;
- forward numerical stability separated from training/optimization stability;
- residual scale separated from numerical step size;
- invertibility separated from computational reconstruction and time reversibility.

Exact witness:

for `x'=-x`, explicit Euler gives `x_{k+1}=(1-h)x_k`.

- non-growth interval: `0<=h<=2`;
- strict-decay interval: `0<h<2`;
- `h=3` gives unstable factor `-2`;
- at `T=1`, `N=2,4,8` give exact rational values `1/4`, `81/256`, and `5764801/16777216`;
- at `h=1/2`, the forward map is invertible but forward-plus-negative-step Euler returns only `3/4`, not the identity.

AUDIT-023 repair:

the scalar stability wording was tightened to preserve the NUMERICS-001 distinction between closed non-growth and strict asymptotic decay. No numerical result changed.

### EXPLORE-001 — Exploration and Information Value

- implementation PR: #101;
- implementation merge:
  `2de8b7b6fd30f47e066eb475bbd282583926b681`;
- audit:
  `AUDIT-022`;
- audit PR: #102;
- audit merge / current main:
  `58da49a2f2969de687cbfd247e488997e57b05d6`.

Central Bayesian exploration structure:

- latent parameter `Theta`;
- belief `b_t(theta)`;
- observation law `p(y|theta,a)`;
- immediate reward `r(theta,a,y)`;
- constrained action set `C_t(b)`;
- finite-horizon Bayes value `V_t(b)`;
- information gain `IG_b(a)=I_b(Theta;Y|a)`;
- one-step value of information `VoI_b(a)`.

Load-bearing doctrine:

- exploration is purposeful information acquisition, not random action;
- epistemic uncertainty is distinct from outcome stochasticity;
- information gain is distinct from decision value;
- an action can have lower immediate expected reward and higher total finite-horizon value;
- UCB/optimism, posterior sampling, and information-directed sampling are distinct mechanisms;
- bandit feedback is a strict simplification of general MDP exploration;
- safe/constrained exploration requires an explicit constraint and guarantee semantics.

Exact witness:

a two-step Bayesian bandit with prior `P(theta=1)=2/5` gives:

- known-first total value `1`;
- informative-action-first total value `11/10`;
- immediate exploration cost `1/10`;
- future value of information `1/5`;
- net advantage `1/10`.

AUDIT-022 repairs:

- made the one-step reward notation consistent by introducing expected payoff `bar r`;
- repaired one malformed notation delimiter;
- narrowed the Moldovan–Abbeel description to the source-supported ergodicity-based safety formulation.

### EXPERIMENT-001 — Experiments as Arguments

- implementation issue: #96, closed completed;
- implementation PR: #97;
- implementation merge:
  `0e441ea8725a7527f138bf0b11b202a737b0dec8`;
- audit issue: #98, closed completed;
- audit:
  `AUDIT-021`;
- audit PR: #99;
- audit merge / current main:
  `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`.

Central experiment object:

`E=(q,theta,U,A,Z,Y,g,V,rho,Omega)`

with:

- bounded claim;
- estimand;
- units/population/sample frame;
- intervention/assignment rule;
- nuisance structure;
- outcome;
- estimator/comparison rule;
- variation/uncertainty description;
- stopping/tuning/selection/reporting rule;
- interpretation scope.

Load-bearing doctrine:

- a run is not yet an experimental argument;
- hypothesis is distinct from estimand;
- intervention is distinct from observational association;
- a baseline is any comparator, while an ablation is a structured intervention on a component;
- seed variance is conditional run-to-run variation, not a substitute for data/population/implementation uncertainty;
- effect magnitude is distinct from statistical significance;
- reproducibility is distinct from replication and from validity;
- benchmark superiority does not by itself identify mechanism;
- selection and stopping are part of the design and may not be erased from the report.

Exact witness:

a deterministic 20-unit two-stratum construction has individual treatment effect +1 everywhere, yet confounded assignment yields a naive aggregate contrast of -7 while both within-stratum contrasts and the equal-stratum standardized contrast are +1.

AUDIT-021 repair:

the original stopping/selection coordinate `tau` collided with the audited Evidence chapter's `tau` epistemic-class coordinate. The chapter now uses `rho` throughout. No mathematical claim changed.

### RLBASE-001 — Reinforcement Learning and Control

- implementation merge:
  `39932c4067bd3d3f85a4d223586875cd2063e3b7`;
- audit:
  `AUDIT-017`;
- audit merge / resulting main:
  `015bc4dc465bde59105530cda2ad6d2d3500ab0e`.

Load-bearing content:

- finite discounted MDP object;
- Bellman expectation and optimality equations;
- dynamic programming versus sampled TD/Q-learning;
- policy-gradient boundary;
- model-based/Dyna boundary;
- POMDP belief-state boundary;
- exact rational two-state policy-improvement witness.

### DEPTH-001 — Depth as Computational Time

- implementation merge:
  `4ef01e5c1d88a09e107a8ca95ed7fc9fb9766855`;
- audit:
  `AUDIT-018`;
- audit merge:
  `9a00ed8fc6b0ca160a9b7e1fb4deef7c078f69cf`.

Load-bearing content:

- fixed, recurrent, adaptive, equilibrium, and conditional depth;
- separation of architectural, parameter, and execution depth;
- exact contraction witness
  `x_{k+1}=(x_k+2)/2`;
- stopping depth
  `tau(epsilon)=ceil(log_2(2/epsilon))`;
- explicit `criterion_met` versus `budget_exhausted`;
- heterogeneous compute resources represented separately unless scalarization is declared.

### MEMTAX-001 — A Taxonomy of Machine Memory

- implementation merge:
  `cd78611a76ba58a27644c37425a55c466090613b`;
- audit:
  `AUDIT-019`;
- audit merge:
  `ffca5ab3dbc75ef0b3ce0ff5afe13d86f32ae75e`.

Central taxonomy:

`M=(L,W,R,T,A,U,P,S)`

with:

- locus;
- write path;
- read path;
- lifetime;
- addressability;
- mutability;
- provenance;
- sharing/synchronization.

Six overlapping roles:

- parametric;
- working;
- episodic;
- semantic;
- associative;
- external.

Important audit repair:

**external memory is a locus property; persistence is the independent lifetime coordinate T.**

Exact witness:

one immutable three-record store supports exact-key, nearest-neighbor associative, and recency/episodic reads solely by changing the read contract.

### EVIDEX-001 — Evidence Exchange and Zero-Context Work

- implementation merge:
  `dceb03af6b0c253b66a1c04a00f2285acd899c73`;
- audit:
  `AUDIT-020`;
- audit merge / current main:
  `55085755626d60d2981a7cf17a6af7cbac60f9fc`.

Central dispatch object:

`D=(delta,Q,B,Sigma,C,Lambda,Gamma,rho)`

Central return object:

`R=(delta,chi,K,Pi,V,Delta)`

Load-bearing doctrine:

- zero-context work is **compiled context**, not absence of context;
- zero-context sufficiency constrains the **normative authorized task contract**, not worker psychology;
- hidden conversation state may not supply an authorized premise, permission, source, success criterion, or return requirement;
- provenance does not imply truth;
- durable identity does not imply authority;
- receipt != acceptance != promotion != certification;
- `independent_blind` is an information-flow declaration, not proof of statistical or institutional independence;
- synthesis requires an explicit logical composition rule;
- only the explicit pointwise proposition schema automatically supports union of domains.

Exact witness:

two different `inputs.txt` versions share the same pathname.

Pathname-only provenance leaves two source candidates.

Exact v1 SHA-256 selects one candidate and replay reproduces `result=5`.

## 6. Existing key prerequisite chapters

The following are already at `draft-v0.1` and audited where applicable:

- `ATLAS-CH-EVIDENCE-001` — Claims, Evidence, and Computational Witnesses;
- `ATLAS-CH-AGENTS-001` — From Models to Agents;
- `ATLAS-CH-COORD-001` — Coordination Architectures;
- `ATLAS-CH-REPLAY-001` — Replayable Evidence Objects;
- `ATLAS-CH-RLBASE-001`;
- `ATLAS-CH-DEPTH-001`;
- `ATLAS-CH-MEMTAX-001`;
- `ATLAS-CH-RETRIEVAL-001`;
- `ATLAS-CH-CONTINUAL-001`.

Do not treat already-drafted downstream chapters as hidden prerequisite authority unless the Chapter Ledger explicitly declares them as dependencies.

## 7. Next tranche — COMPRESS-001

Stable ID:

`ATLAS-CH-COMPRESS-001`

Title:

**Compression and Description Length**

Declared hard dependencies:

- `ATLAS-CH-INFO-001`;
- `ATLAS-CH-REP-001`.

Atlas contract:

> Develop MDL, pruning, quantization, distillation, low rank, weight sharing, and structured transforms.

The next session should instantiate this tranche from current main only if the controller remains `idle-ready` and main still equals the recorded baseline.

A sound intellectual spine should distinguish at least:

1. coding length from parameter count;
2. lossless from lossy compression;
3. model compression from data compression;
4. pruning from quantization;
5. low-rank factorization from unstructured sparsity;
6. weight sharing from parameter deletion;
7. knowledge distillation from literal parameter compression;
8. MDL/model selection from ad hoc size minimization;
9. compression ratio from retained task quality;
10. descriptive compactness from mechanistic or semantic understanding.

The finite witness should be selected only after source locking. It should include an exact toy coding/parameter example where two representations have equal predictive behavior but different description lengths, plus a control showing that aggressive compression can destroy the relevant function.

Direct consumer:

- `ATLAS-CH-COMPINTEL-001`.

## 8. Durable restart instruction for a fresh chat

A fresh session can be started with only:

> Resume the Adaptive Intelligence Atlas. Read `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` branch `state/atlas-controller`, `governance/ACTIVE_TRANSACTION.yaml` first, then `governance/CURRENT_HANDOFF.md`. Follow the recorded recovery rule and continue the bounded transaction through its real completion boundary. Work in short durable bursts; do not reconstruct state from chat.

No other chat history should be required.

## 9. Invariants that must remain true

- `ACTIVE_TRANSACTION.yaml` is the live recovery authority.
- Main must never be assumed unchanged; verify it.
- Chapter eligibility comes from the current Chapter Ledger.
- A chapter may consume only declared hard prerequisites plus explicitly source-locked external/public project evidence.
- Every strengthened claim requires strengthened support.
- Computational witnesses prove only their declared finite/bounded claims.
- Audit repairs must repair the manuscript/formal/source artifacts, not merely document defects.
- Validation must be green before merge.
- After completion, recompute the frontier and checkpoint `idle-ready`.

This handoff is a recovery aid. If it ever conflicts with the live controller or current repository state, the live controller plus current `main` and Chapter Ledger take precedence.
