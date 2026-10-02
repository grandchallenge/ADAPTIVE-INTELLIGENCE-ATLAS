# KEYSTONE-003 — Attention + Optimizer-State Dynamics Manuscript Pair

## Status

**Tranche state:** implemented on branch pending merge validation.

## Objective

Produce the second style-setting keystone pair:

- \`ATLAS-CH-ATTNOP-001\` — Attention as an Operator;
- \`ATLAS-CH-OPTDYN-001\` — Optimizer-State Dynamics.

## Baseline

- AUDIT-001 merge: \`01a8203e7e4ddd02828ec6415b918b4a9dde4951\`;
- work issue: \`#7\`.

## Source locks

### Attention

- Vaswani et al., *Attention Is All You Need* (NeurIPS 2017);
- Tsai et al., *Transformer Dissection: An Unified Understanding for Transformer’s Attention via the Lens of Kernel*, DOI \`10.18653/v1/D19-1443\`;
- Katharopoulos et al., *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention*, ICML 2020.

### Optimizer-State Dynamics

- Polyak, *Some Methods of Speeding up the Convergence of Iteration Methods*, DOI \`10.1016/0041-5553(64)90137-5\`;
- Sutskever et al., *On the importance of initialization and momentum in deep learning*, ICML 2013;
- Kingma and Ba, *Adam: A Method for Stochastic Optimization*, ICLR 2015 / arXiv:1412.6980;
- Lessard, Recht, Packard, *Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints*, DOI \`10.1137/15M1009597\`.

Exact metadata and claim scope are stored in the source-lock manifests.

## Atlas-owned derivations

Attention packet establishes:

- standard score/operator/value decomposition;
- fixed-operator linearity in values;
- row-stochasticity;
- a concrete proof that the full self-attention map is nonlinear in hidden state;
- permutation equivariance before positional asymmetry;
- masking as operator-support restriction;
- softmax-row sensitivity;
- feature-map reassociation for linear attention.

Optimizer packet establishes:

- augmented momentum state;
- exact block/state Jacobian on a scalar quadratic;
- characteristic polynomial and stability dependence on \((\eta,\beta,h)\);
- exact stable non-normal example;
- exact fourth-step gain \(\|J^4\|_2\approx2.610090585959495\);
- fixed-point versus time-varying Jacobian-product distinction.

## Wolfram witnesses

Runtime:

- Wolfram Language \`15.0.1 for Linux x86 (64-bit) (July 2, 2026)\`;
- system ID \`Linux-x86-64\`.

### ATLAS-FIG-ATTNOP-001

- source: \`figures/wolfram/ATLAS-FIG-ATTNOP-001.wl\`;
- output: \`figures/masters/ATLAS-FIG-ATTNOP-001.png\`;
- Git blob: \`2ba96f6f30311c117f27c0717961145ce9cbb0cd\`.

Independent replay in this tranche verified:

- softmax row sums \(=1\) to numerical precision;
- fixed-\(A\) linearity residual \(=0\);
- first-query perturbation
  \[
  \Delta A_{1,:}\approx(-0.08124593,0.02683053,0.05441540).
  \]

### ATLAS-FIG-OPTDYN-001

- source: \`figures/wolfram/ATLAS-FIG-OPTDYN-001.wl\`;
- output: \`figures/masters/ATLAS-FIG-OPTDYN-001.png\`;
- Git blob: \`fa8e5231cb6451c026a0ccd7beecdfcff330c98d\`.

For

\[
J=
\begin{pmatrix}
0.9&-0.09\\
1&0.9
\end{pmatrix},
\]

independent replay verified:

- eigenvalues \(0.9\pm0.3i\);
- spectral radius \(\sqrt{0.9}\approx0.9486832981\);
- non-normality;
- peak \(2\)-norm gain \(2.610090585959495\) at step \(4\) over \(n=0,\ldots,20\).

## Manuscript drafts

- \`manuscript/parts/05-attention-sequence-position/ATLAS-CH-ATTNOP-001.md\`;
- \`manuscript/parts/06-optimization-geometry-dynamics/ATLAS-CH-OPTDYN-001.md\`.

Both follow the Atlas pattern:

problem → bounded allegory → formal object → exact derivation → computational witness → figure → interpretation → failure boundary → downstream handoff.

## Repair during tranche

An earlier partial write had interpreted TeX backslashes as JavaScript escape characters in several Markdown files. The affected Attention manuscript, both derivation packets, and both witness receipts were rewritten with clean TeX.

CI is strengthened to reject hidden C0 control characters and tabs in Atlas-authored Markdown, making this failure class durable rather than merely repaired locally.

## Promotion state

Both ledger nodes are promoted from \`specification-ready\` to \`draft-v0.1\`.

This indicates a complete first manuscript pass with bound sources, derivations, figure/witness provenance, and replay. It does not imply mathematical certification or publication readiness.

## Next phase after merge

Run a bounded mathematical/editorial audit of the pair, checking:

1. algebra and numerical replay;
2. citation closure;
3. notation against the lexicon and prior keystones;
4. figure semantics and accessibility;
5. distinction between operator structure and causal interpretation;
6. distinction between local optimizer-state mechanism and frontier-training prevalence.

Only after audit should the Atlas move to Boundary Contracts + Replayable Evidence Objects.
