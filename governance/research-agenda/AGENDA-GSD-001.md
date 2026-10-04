# AGENDA-GSD-001 — Generalization-State Dynamics

**Status:** Active GCL research-agenda decision  
**Date:** 2026-10-03  
**Governing issue:** #133  
**Scope:** Pre-training dynamics, checkpoint selection, curriculum control, mechanistic diagnostics, capability reconstruction, and optimizer/architecture comparisons  
**Primary external source:** Jiaxin Wen, Zhengxuan Wu, Dawn Song, Lijie Chen, *Generalization Dynamics of LM Pre-training*, arXiv:2609.33150v1, submitted 2026-09-27.  
**Exact source URI:** https://arxiv.org/abs/2609.33150v1

## 1. Decision

GCL will treat generalization behaviour during training as a potentially non-monotone state variable rather than as a quantity that can be inferred from smooth training loss, terminal-checkpoint performance, or ordinary benchmark trajectories alone.

For work that makes claims about learned mechanisms, GCL will distinguish four questions:

1. **acquisition** — was a transferable computation learned at all?
2. **persistence** — does the relevant computational substrate remain present across later training?
3. **accessibility/control** — can the computation still be recruited under a declared prompt, routing condition, intervention, or small continuation update?
4. **behavioural expression** — does the computation dominate the model's observed answer under the declared evaluation?

A failure of behavioural expression is not by itself evidence that the computation was never learned or has been erased.

This decision changes research priorities and evaluation contracts. It does not establish a universal theory of why generalization states change.

## 2. Evidence motivating the decision

Wen et al. report abrupt reversals between more-generalizing and more-pattern-matching behaviour across nearby language-model pre-training checkpoints while conventional loss and benchmark trajectories remain comparatively smooth. They call the phenomenon **mode-hopping**.

The paper also reports that checkpoint choice can materially affect later post-training generalization, and presents a preliminary experiment in which data selected from windows associated with a target behavioural mode can stabilize that mode during continued pre-training.

These observations are sufficient to reject a GCL default assumption of monotone mechanism improvement from loss or endpoint capability alone.

They are not sufficient to establish the authors' proposed capacity-allocation explanation as fact.

## 3. Claim firewall

The following remain hypotheses or open questions:

- capacity competition between shallow and generalizable circuits as the universal cause of mode-hopping;
- every behavioural fluctuation corresponding to a distinct internal computational mechanism;
- one scalar statistic diagnosing a model's generalization state;
- intermediate checkpoints being generally superior to final checkpoints;
- data selection demonstrated on one probe generalizing to arbitrary capabilities;
- state changes being reversible or irreversible without intervention evidence.

## 4. Research object

For a checkpoint or training state theta_t, use a structured generalization-state descriptor when useful:

\[
\mathcal G(\theta_t)=
\bigl(
G_{\mathrm{beh}},
G_{\mathrm{mech}},
G_{\mathrm{geom}},
G_{\mathrm{opt}},
G_{\mathrm{route}}
\bigr).
\]

The coordinates denote declared behavioural, mechanistic, representational/geometric, optimizer-state, and routing/selection observations.

This is a research interface, not a claim that these coordinates are complete, independent, or uniquely identifiable.

## 5. Required experimental distinctions

### State trajectory, not endpoint-only evaluation

Experiments concerning training progress should sample enough checkpoints to detect reversals, occupancy, and path dependence when technically feasible. Terminal checkpoint comparisons remain useful, but cannot by themselves establish monotone mechanism formation.

### Behaviour versus mechanism

A behavioural transition does not prove a mechanistic transition. Mechanistic claims require intervention, localization, causal substitution, or other evidence capable of distinguishing substrate loss, substrate persistence with changed competition, changed routing/control, changed representation with functionally equivalent computation, and evaluation artefact.

### Recovery as evidence

Where a previously expressed capability disappears, measure whether it can be restored by a bounded intervention class Delta.

A useful quantity is the declared recovery cost

\[
R_{\Delta}(\theta,q)=
\inf_{\delta\in\Delta}
C(\delta)
\]

subject to restoration of the target capability on probe q.

The intervention class and cost C must be stated. Low recovery cost is evidence only relative to that intervention contract.

### Occupancy and transition rate

For a declared regime G, useful comparative diagnostics include

\[
O_G=\frac{1}{T}\sum_t \mathbf 1[\theta_t\in G]
\]

and a transition count or rate computed over declared checkpoint spacing.

These are not universal measures of intelligence.

### Hysteresis and path dependence

When feasible, compare trajectories such as G → P → G with trajectories reaching a nominally similar final training distribution through a different history. Persistent differences are evidence of path dependence and should be analyzed with the Atlas dynamics and optimizer-state machinery rather than collapsed into endpoint score variance.

## 6. Agenda consequences

### Minimal Curricula and Reasoning Bases

Strengthen the target to:

> What is the smallest curriculum or experience-selection policy that acquires transferable computations, preserves their accessibility, and keeps them competitively expressible?

Failure to express a reasoning operation must be classified among at least: not acquired; acquired then structurally lost; persistent but inaccessible; accessible but behaviourally suppressed; unresolved.

### Learning Progress as a Search Operator

Treat learning progress together with generalization-state evidence as feedback for experience selection:

\[
\theta_t
\rightarrow
\text{probe state}
\rightarrow
\text{select experience/data}
\rightarrow
\theta_{t+1}.
\]

Test whether state-aware curriculum control improves desirable-regime occupancy or recovery without relying on one behavioural probe as a universal controller.

### CPS and optimizer-state dynamics

Use dense checkpoint windows around reproducible G → P and P → G transitions to test whether optimizer-state Jacobians, non-normal amplification, or related dynamical signatures change before, during, or after behavioural transitions.

Prospective or held-out transition prediction is preferred to retrospective best-layer selection.

### Mechanistic and spectral diagnostics

Mechanistic Intervention should ask whether an apparently lost computation can be restored by activation patching, path/head interventions, routing changes, or other bounded causal substitutions.

Spectral and operator diagnostics should search for structured transition signatures, but no scalar effective-rank, Fisher, sharpness, gradient-similarity, or spectral statistic should be promoted as a universal generalization indicator without independent evidence.

### The Residual

Treat suppressed capability as a reconstruction problem:

> What minimal structure survives a behavioural disappearance and remains sufficient to reconstruct the prior capability?

Recovery cost, invariant subspaces, transferable operators, or related objects may provide operational approximations.

### Architecture and optimizer comparisons

When the question concerns transferable computation, report not only terminal loss/capability but state stability where feasible. Candidate comparison quantities include desirable-state occupancy, transition frequency, recovery cost, hysteresis, and post-training transfer from selected checkpoints.

For nGPT/RUNT, Muon-like methods, manifold optimization, MODULUS-derived updates, and related work, this creates a falsifiable question: do different geometries or update laws change the stability or recoverability of transferable computational regimes?

### Optionality bridge

There is a plausible but exploratory connection to Optionality and Correction Capacity. An update that improves immediate fit while making a transferable regime difficult to recover may reduce future correction capacity. This is not yet an OPRM theorem or standard.

## 7. First bounded experimental tranche

1. Select an open model family with sufficiently dense public checkpoints.
2. Define several adversarial generalization probes with soft and hard score semantics.
3. Locate at least one reproducible G → P or P → G transition.
4. Run transition-local behavioural, optimizer-state, representation/operator, mechanistic-intervention, and recovery diagnostics.
5. Test whether the transition can be predicted before the behavioural change.
6. Test whether the suppressed mode is recoverable with a small declared intervention.
7. Compare an alternative curriculum, optimizer, or architecture only after the baseline transition is reproducible.
8. Test for hysteresis if the training-control surface permits it.

The tranche succeeds even if it falsifies a GCL mechanism hypothesis.

## 8. Programme interfaces

This agenda decision informs, but does not replace:

- ATLAS-CH-RESIDUAL-001;
- ATLAS-CH-OPTDYN-001;
- ATLAS-CH-CPS-001;
- ATLAS-CH-CURRICULUM-001;
- ATLAS-CH-PROGRESSSEARCH-001;
- ATLAS-CH-MINCURR-001;
- ATLAS-CH-MECHDIAG-001;
- ATLAS-CH-SPECTRALDIAG-001;
- ATLAS-CH-OPTIONALITY-001.

No new hard dependency is introduced. The Atlas remains an 80-chapter architecture.

## 9. Executable programme

The implementation plan for this agenda is:

- `governance/research-agenda/GSD-001_RESEARCH_PROGRAMME.md`
- `governance/research-agenda/GSD-001_WORK_PACKAGE_INDEX.yaml`

The programme uses gated escalation: evaluator fidelity and cheap checkpoint sweeps first; transition validation and recovery/mechanistic tests second; curriculum control third; optimizer/architecture comparisons fourth; OLMo3-32B and post-training confirmation only after held-out predictive value is established.

## 9. Durable rule

> **Do not infer monotone mechanism improvement from smooth loss, more training, or endpoint benchmarks. Treat checkpoints as potentially distinct computational states, and separate acquisition, persistence, accessibility, and expression.**

This rule is methodological. It does not certify any mechanistic explanation of the motivating paper.
