# SHIFT-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-SHIFT-001
- implementation issue: #263
- protected baseline: 01a4c2c7d526df385bb8b2ab58046c3c476e3629
- branch: work/shift-263

## Hard prerequisite

UNCERTAINTY-001:
- manuscript e6714d0505a96e2bfdc431b4ec60d50b0044efa6
- source lock b9f38d496efe2d704b759510cf171d5a3e83a2c8
- AUDIT-054 132a0df9a603ec88811312d193971100549648a4

## New primary sources
- Sugiyama, Krauledat & Müller 2007, JMLR 8:985--1005
- Madry et al. 2018, ICLR

## Implementation artifacts
- specification b0d7a0a85e56c065b8977ba523b75601366ffc6f
- derivations b12d6ef827f8095c8599c7dcc610e223ae2c769d
- witness 4bf2a0b95d8e1ade101b00c9aa15afb4ee1dd77b
- manuscript 064b7f05068eb212eacbb64228e51b6069d2728f
- source lock 5c96c8b3efc459308db680dada19ebc767209634
- bibliography ed8976909306cde1ef6a92de5383c1cd61600484
- Chapter Ledger 94ae4b045410a8fe1e2dce84d160b78a0f163629
- Source Register 540d7ff9a0e0e2668ca5444a4a42456b22c94d4a

## Exact changed-law witness
- X in {a,b}, Y(a)=1, Y(b)=0
- P_X=(1/2,1/2)
- Q_X=(3/4,1/4)
- unchanged predictor score s(a)=s(b)=1/2
- source calibration gap = 0
- deployment calibration gap = 1/4
- source Brier risk = deployment Brier risk = 1/4
- exact importance weights w(a)=3/2, w(b)=1/2

## Benign marginal-shift control
- X in {u,v}, exact predictor f(u)=0, f(v)=1
- P_X=(1/2,1/2)
- Q_X=(9/10,1/10)
- TV(P_X,Q_X)=2/5
- source and deployment 0/1 risk both 0

## Conditional-shift control
- unchanged X marginal
- reversed conditional labels under Q
- source-perfect predictor has Q-risk 1
- X-density ratio is identically 1 and cannot repair conditional shift

## Adversarial separation
- clean two-point classifier risk = 0
- declared perturbation set permits opposite input with original label retained
- adversarial risk = 1
- adversarial robustness is perturbation-set relative

## Durable boundaries
- P-law guarantees do not silently transfer to Q;
- covariate shift and conditional shift are distinct;
- shift detection is not task-failure detection;
- importance weighting requires target support inside source support for ordinary density-ratio correction;
- calibration, coverage, selective risk, predictive risk, adversarial risk, and structural sensitivity remain distinct;
- average-case deployment shift is not worst-case adversarial perturbation;
- changed predictive statistics do not identify a structural mechanism.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
