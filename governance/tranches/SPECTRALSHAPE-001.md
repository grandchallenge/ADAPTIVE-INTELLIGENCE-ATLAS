# SPECTRALSHAPE-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-SPECTRALSHAPE-001
- implementation issue: #272
- protected baseline: c17966203c5a3d7c5bbb629caa2d3b2ae87d81e0
- branch: work/spectralshape-272

## Hard prerequisites

MATRIXOPT-001:
- manuscript ac860c93b99ee33d8213bf05845b3670061fba53
- source lock f4fb1797bc93a8f038ddb06e6d3139ab6367ffcb
- AUDIT-046 5f87902c5e30d45149df70d6c0b86a320c9c142a

NONNORMAL-001:
- manuscript a8b4cde747df1a986eeca1439203b08512a1471c
- source lock f8c868af0fc35b73d9acadbdf6d952b03c1d89e9
- AUDIT-001 f13b7ac01f7b10dfadd64da6f31c45832344c082

## Source decision
- no new external academic source added;
- SVD/polar/update-geometry authority is inherited through audited MATRIXOPT-001;
- non-normal transient/pseudospectral authority is inherited through audited NONNORMAL-001;
- all new finite shaping/control witnesses are Atlas-owned exact linear algebra.

## Implementation artifacts
- specification 913618031f1532e01635a20210c17e9563b4b7e6
- derivations 7516af5e01f310d75a1a444a6313d28123744010
- witness a50e364a9554db3b3b31ae59e9ad4e52376ee484
- manuscript f2a6b57d4e3a09c9398c80af2d36e7d53e77793e
- source lock 5b24e3184e612d2771eab370c66073a56d3ba3b8
- Chapter Ledger 52368e21da96630a428d2f8fba41251ea7e1f07f
- Source Register a20765eaacf2b2b4c570bd3657f41fc77ee3ee9d

## Exact shaping witness
- G=diag(4,1), singular values (4,1), kappa2=4
- scalar normalization -> diag(1,1/4), kappa2=4
- upper clipping sigma->min(sigma,2) -> diag(2,1), kappa2=2
- polar flattening -> I2, kappa2=1
- explicit non-flat target spectrum (3,2) -> diag(3,2), kappa2=3/2

## Non-normal control
- A=[[1/2,2],[0,1/2]]
- N=(1/2)I2
- shared eigenvalues {1/2,1/2}
- probe e2=(0,1)
- ||A e2||^2=17/4
- ||N e2||^2=1/4
- at epsilon=1/4, inherited exact pseudospectral radii are 3/4 and 1/4

## Durable boundaries
- scalar normalization changes scale, not generally conditioning;
- clipping/conditioning and polar flattening are distinct maps;
- flat spectrum is one possible target, not a universal optimum;
- instantaneous update spectra are not optimizer-state dynamics;
- eigenvalue shape alone does not control non-normal transient/pseudospectral behavior;
- improved update condition number does not by itself prove faster nonlinear convergence or better task quality.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
