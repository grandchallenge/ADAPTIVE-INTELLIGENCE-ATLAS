# EXPLORE-001 — Exploration and Information Value

## Identity

- chapter: `ATLAS-CH-EXPLORE-001`;
- implementation issue: #101;
- drafting baseline: `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`;
- work branch: `work/explore-001`;
- hard prerequisite:
  - `ATLAS-CH-RLBASE-001` at audited `draft-v0.1`.

## Objective

Promote EXPLORE-001 from architecture to a complete `draft-v0.1` chapter that treats exploration as purposeful information acquisition under sequential decision uncertainty.

## Source lock

The tranche binds:

- audited RLBASE manuscript blob `a99f78b788b97bc1bb3346ca1f1b97802c0f84db`;
- RLBASE audit blob `8b7a1f9b61c15ab9c2c010ea538e25c11a7ed1cc`;
- Auer–Cesa-Bianchi–Fischer (2002);
- Thompson (1933);
- Russo–Van Roy (2014);
- Howard (1966);
- Moldovan–Abbeel (2012).

No downstream Regret or Optionality manuscript is used as prerequisite authority.

## Formal spine

The chapter separates:

- immediate reward;
- epistemic uncertainty;
- information gain;
- decision value of information;
- exploration cost;
- continuation value;
- admissible constrained action set.

For one-step future decision value:

`VoI_b(a)=E_Y[max_{a'}E[r(theta,a')|Y,a]]-max_{a'}E[r(theta,a')]`.

## Exact witness

Two-step Bayesian bandit:

- known action reward: `1/2`;
- unknown action reward: `theta in {0,1}`;
- prior `P(theta=1)=2/5`;
- unknown action reveals `theta`.

Exact values:

- known-first total: `1`;
- unknown-first total: `11/10`;
- immediate exploration cost: `1/10`;
- future value of information: `1/5`;
- net exploration advantage: `1/10`.

## Durable artifacts

- `sources/source-locks/ATLAS-CH-EXPLORE-001.yaml`;
- `manuscript/specifications/ATLAS-CH-EXPLORE-001.md`;
- `mathematics/derivations/ATLAS-CH-EXPLORE-001-DERIVATIONS.md`;
- `mathematics/computational-witnesses/ATLAS-CW-EXPLORE-001.md`;
- `manuscript/parts/11-decision-making/ATLAS-CH-EXPLORE-001.md`;
- Chapter Ledger promotion;
- Source Register entry;
- bibliography entries.

## Tranche state

Implementation artifacts complete on the work branch.

Repository validation, implementation merge, and bounded post-draft audit remain part of this transaction.
