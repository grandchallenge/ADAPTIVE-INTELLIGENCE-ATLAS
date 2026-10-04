# OPTIONALITY-001 — Optionality and Correction Capacity

## Identity

- chapter: `ATLAS-CH-OPTIONALITY-001`
- issue: #129
- baseline: `39f419abb72c941e041f92f2834229f9968da006`
- branch: `work/optionality-001`
- hard prerequisite:
  - `ATLAS-CH-REGRET-001`

Exact prerequisite binds:

- REGRET manuscript: `56d6039348cbb13814325a4cfb3256177ab39a56`
- AUDIT-026: `6af3c12f71f0731f0e3f3d0fef2389d6a9bc0d95`
- REGRET source lock: `52d85475fd6796ce5397b3255774bed2040e5a47`

## Core optionality objects

- viable continuation set `V_h(s)`;
- consequence equivalence `~_s`;
- functional option quotient `O_h(s)`;
- optional finite count `N_h(s)=|O_h(s)|`;
- extended-real correction cost `k_h(s,theta)`;
- post-evidence conditional correction indicator `C_{h,epsilon}(s,theta)`;
- ex-ante tolerance-indexed correction capacity `CC_{h,epsilon}(s;b)`;
- horizon-relative recoverability `Rec_h(s;B)`.

## Exact witness

Two environments:

`Theta={L,R}`

with symmetric prior.

The declared stage-0 action set is `{P,C_L,C_R}`. The learner comparison is preserve versus commit-left; the symmetric `C_R` action exists so the clairvoyant environment-informed comparator `C_theta` is well typed.

Preserve policy:

- immediate cost `1/2`;
- future actions `{L,R}`;
- return `1/2` in both environments;
- Bayes regret `1/2`;
- functional option count `2`;
- zero-tolerance ex-ante correction capacity `1`;
- information gain `1 bit`.

Commit-left policy:

- no immediate cost;
- future action `{L}`;
- returns `1` in L and `0` in R;
- Bayes regret `1/2`;
- functional option count `1`;
- zero-tolerance ex-ante correction capacity `1/2`;
- information gain `1 bit`.

Thus prior value, Bayes regret, and information gain tie while correction capacity differs.

Worst-case regret is `1/2` versus `1`; the tranche does not claim optionality is invisible to every risk criterion.

## Counterexamples

1. Preservation cost `c>1/2` makes the higher-optionality policy lower expected value.
2. Duplicate action aliases increase raw action count without increasing functional options.
3. Perfect information does not restore an action that an earlier commitment made infeasible.

## Source boundary

External precedents:

- Arrow–Fisher (1974): uncertainty, irreversibility, and preservation value;
- Aubin (1991), original Birkhäuser Boston print identity: viability/state constraints;
- Klyubin–Polani–Nehaniv (2008): empowerment and the options-open interpretation.

Atlas-owned:

- functional option quotient;
- correction cost;
- tolerance-indexed correction capacity;
- witness and counterexamples.

## Durable distinctions

- expected value versus future feasible-action structure;
- optionality versus uncertainty aversion;
- recoverability versus delay;
- raw action labels versus consequence classes;
- information gain versus correction capacity;
- bad stochastic outcome versus irreversibility;
- regret versus opportunity damage;
- policy options versus environment branches;
- hard infeasibility versus finite correction cost;
- optionality objective/constraint/diagnostic versus universal anti-commitment rule.

## Durable artifacts

- `sources/source-locks/ATLAS-CH-OPTIONALITY-001.yaml`;
- `manuscript/specifications/ATLAS-CH-OPTIONALITY-001.md`;
- `mathematics/derivations/ATLAS-CH-OPTIONALITY-001-DERIVATIONS.md`;
- `mathematics/computational-witnesses/ATLAS-CW-OPTIONALITY-001.md`;
- `manuscript/parts/11-decision-making/ATLAS-CH-OPTIONALITY-001.md`;
- Chapter Ledger promotion;
- Source Register entry;
- bibliography closure.

## Remaining gates

Validate, repair all in-scope defects, open and merge implementation PR, instantiate bounded post-draft audit, repair audit defects, validate and merge audit, verify issue closure, recompute dependency-legal frontier, and reset controller.
