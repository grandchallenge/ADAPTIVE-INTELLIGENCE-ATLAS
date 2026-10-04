# CURRICULUM-001 — Curriculum Learning

## Identity

- chapter: ATLAS-CH-CURRICULUM-001
- issue: #145
- baseline: c1122f3b6a6cb0170e77f5fe340a7bec402618ce
- branch: work/curriculum-001
- hard prerequisites:
  - ATLAS-CH-DATA-001
  - ATLAS-CH-OPTBASE-001

Exact prerequisite binds:

- DATA manuscript: e4cb245419ad3601aa82ac33129660673ab1622c
- AUDIT-030: 740b1340ac969bd330a995b9dca2129f4317a541
- DATA source lock: 701f5504e77342fad29fb4c54eb2926a0c4c90b9
- OPTBASE manuscript: 42df47c50c2d6d26da65a58b230040e2663f901f
- AUDIT-012: 28929ba6b4a16a3cef4a871fd9253d76e8a93634
- OPTBASE source lock: fa610d3d763cc1a7e76ee4b83e85ce2c965c2825

Project-local context bind:

- GSD agenda: 0f31202a928d8e2cb5e3290d84b32344033c2f19

## External source set

- Bengio et al. (ICML 2009): curriculum-learning formulation;
- Graves et al. (ICML 2017): automated stochastic syllabus selection from learning-progress signals;
- Platanios et al. (NAACL-HLT 2019): difficulty/competence-based scheduling.

All empirical claims remain scoped to the cited studies.

## Core objects

- learner state \((\theta_t,u_t)\);
- curriculum state \(c_t\);
- curriculum observation \(z_t\);
- curriculum policy \(\pi_t(a\mid z_t,c_t)\);
- data-selection kernel \(Q(x\mid a)\);
- difficulty score \(d(x)\);
- competence threshold \(q_t\);
- learning-progress signal \(LP_t(r)\);
- open-loop versus closed-loop control;
- selection versus reweighting.

## Exact witness

State:

\[
s=(e,h)\in\{0,1,2\}^2.
\]

Actions:

\[
E,H.
\]

Static ranking:

\[
d(E)=1<2=d(H).
\]

At \(s_A=(0,0)\):

\[
R(E)=1,\qquad R(H)=0.
\]

At \(s_B=(2,0)\):

\[
R(E)=0,\qquad R(H)=1.
\]

Therefore no state-independent deterministic first action is one-step progress-optimal for both states.

Two-step equal-transition comparison from \(s_B\):

- fixed \(E,H\): cumulative toy progress 1;
- state-aware \(H,H\): cumulative toy progress 2.

The witness is finite and synthetic. It is not a neural training result.

## Durable distinctions

- curriculum policy versus optimizer;
- model state versus optimizer state versus curriculum state;
- open-loop schedule versus closed-loop state-aware policy;
- static difficulty versus state-dependent utility;
- competence threshold versus proved competence;
- learning-progress signal versus mechanism evidence;
- sample selection versus mixture reweighting;
- curriculum gain versus dose/compute/recipe confounding;
- immediate progress versus long-horizon search value;
- deterministic syllabus versus stochastic syllabus.

## Artifact set

- sources/source-locks/ATLAS-CH-CURRICULUM-001.yaml
- sources/bibliography.bib
- manuscript/specifications/ATLAS-CH-CURRICULUM-001.md
- mathematics/derivations/ATLAS-CH-CURRICULUM-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-CURRICULUM-001.md
- manuscript/parts/10-tokenization-data-curriculum/ATLAS-CH-CURRICULUM-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- this tranche receipt

## Remaining gates

Repository validation, implementation PR, exact-head green CI, protected merge, bounded post-draft audit, in-scope repairs, audit validation/merge, issue closure, frontier recomputation, and controller reset.
