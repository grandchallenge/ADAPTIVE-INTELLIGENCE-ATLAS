# UNCERTAINTY-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-UNCERTAINTY-001
- title: Uncertainty and Calibration
- implementation issue: #215
- branch: work/uncertainty-215
- protected baseline: 1fa80bdae8e5219cc7e90b481914b66e3af8c3aa
- controller branch: state/atlas-controller

## Hard prerequisite binding

### INFO-001

- manuscript: 0fca10cbc7476c5b729ee15dfad0dec563665821
- source lock: ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

## Implementation artifact blobs

- specification: efa855b00af94780f08f9267ed6357ec847374c9
- derivation packet: 997cba9eb0c8f48d06c1155c5e17f7db74c964ae
- computational witness: 01f8fff254fb0a458935c716ce07da389a4a33ef
- reader manuscript: 4ae2ae94cdb39dacfe4c900144159ef65b9f1a34
- source lock: b9f38d496efe2d704b759510cf171d5a3e83a2c8
- Chapter Ledger: 4c854cfd4f7e19db3399d78c95cb90a99a4da9eb
- Source Register: ae7b98bb7b758631c202f004c444180dcfbb5401
- bibliography: afafee05f9fd71932e067e34a061e970c1685f90

## Durable mathematical substrate

The tranche establishes:

1. population binary calibration as E[Y|S]=S;
2. an exact calibrated-but-uninformative versus calibrated-and-sharp witness;
3. predictive entropy as distinct from an aleatoric/epistemic decomposition;
4. an exact same-predictive-law witness with opposite conditional/model-information decomposition;
5. source-scoped MC-dropout semantics;
6. source-scoped deep-ensemble semantics;
7. finite-sample conformal marginal coverage through exchangeable ranks;
8. an exact n=4, alpha=0.2 rank witness with coverage 4/5 under no ties;
9. selective coverage and selective risk as separate from calibration;
10. an exact five-example risk/coverage witness;
11. explicit distribution-shift boundaries for all distribution-relative guarantees.

## Exact witnesses

### Same predictive entropy, different decomposition

Model A:

- Y ~ Bernoulli(1/2);
- Theta fixed;
- H(Y)=1 bit;
- E[H(Y|Theta)]=1 bit;
- I(Y;Theta)=0.

Model B:

- Theta ~ Bernoulli(1/2);
- Y=Theta;
- predictive Y ~ Bernoulli(1/2);
- H(Y)=1 bit;
- E[H(Y|Theta)]=0;
- I(Y;Theta)=1 bit.

Thus identical predictive entropy does not identify epistemic/model uncertainty.

### Calibration versus sharpness

For equally likely X=a,b with conditional positive probabilities 0.9 and 0.1:

- constant predictor S0=0.5 is calibrated and has Brier risk 0.25;
- conditional predictor S1=(0.9,0.1) is calibrated and has Brier risk 0.09.

Thus calibration does not determine sharpness or proper-score performance.

### Conformal rank witness

For n=4 and alpha=0.2:

- k=ceil(5*0.8)=4;
- under exchangeability and no ties, future rank is uniform on 1..5;
- coverage occurs for ranks 1..4;
- marginal coverage is exactly 4/5.

### Selective prediction witness

Error indicators: (0,0,0,1,1).

- accept all: coverage=1, selective risk=2/5;
- accept first three: coverage=3/5, selective risk=0.

Lower selective risk is conditional on lower coverage.

## Claim boundaries

This transaction does not establish that:

- confidence equals calibration;
- calibration implies sharpness or high accuracy;
- predictive entropy equals epistemic uncertainty;
- the aleatoric/epistemic split exhausts all uncertainty;
- dropout samples are exact posterior samples in arbitrary networks;
- ensemble members are posterior samples by definition;
- conformal marginal coverage implies arbitrary conditional coverage;
- conformal coverage is probability calibration;
- abstention calibrates probabilities;
- in-distribution guarantees survive distribution shift.

## Downstream handoff

Direct consumer: ATLAS-CH-SHIFT-001.

SHIFT may inherit the uncertainty objects, calibration definitions, exact finite witnesses, and exchangeability/risk-coverage boundaries. It must independently establish every shifted-distribution, covariate-shift, concept-drift, adversarial, robustness, and structural-sensitivity statement.

## Validation state

Implementation remains unmerged until canonical Linux validation and exact-head GitHub validation both pass, followed by implementation merge, mandatory post-draft audit, final main validation, frontier recomputation, issue closure, and controller/handoff reset.
