# NEURALKRYLOV-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-NEURALKRYLOV-001
- implementation issue: #255
- protected baseline: c9d5c61bf611327a1ed054206c5d8e778559e28a
- branch: work/neuralkrylov-255

## Hard prerequisites

KRYLOV-001:
- manuscript 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock adbe97c750ed79d09462a5e867e5beb772ad72e2
- AUDIT-039 03660b0dbd1d0604e943d0d09c7b52c6605b256c

TRANSPORT-001:
- manuscript 0a81b39a457384f7a265bbac2955ea282217bc3f
- source lock 55fcd80bc3d94e3b270ddcf28873242ba21f823f
- AUDIT-053 060d0b9dc320cd16fdcfe10b87484a3bbfda4c75

## Source decision
- no new external academic source added;
- classical Krylov/preconditioning authority is inherited through audited KRYLOV-001;
- representation-map/local-Jacobian authority is inherited through audited TRANSPORT-001;
- new finite positive/control witnesses are Atlas-owned exact linear algebra.

## Implementation artifacts
- specification 6ac203b25f1155b3eaed4b063af8fa559b69ce2d
- derivations afe1798ce77b74b79478d79553bd72323da8545b
- witness 02e383c1ff0237199be5ac757c4aebdd4cb8e011
- manuscript d2740a2d47c004dc48a0dc97ae0ebbb43d60707b
- source lock f030acac3c8269ab6c3a4856c1ec53cc75cedee9
- Chapter Ledger 2149fa3ae83e57fd46391e6b36a0af3931da5af0
- Source Register 536349056012148899077b9d0d1f0badd18dd684

## Exact positive witness
- A=diag(1,4), b=(1,1)
- fixed left preconditioner M=diag(1,2)
- B=M^{-1}A=diag(1,2)
- c=M^{-1}b=(1,1/2)
- exact solution x*=(1,1/4)
- K1(B,c)=span{c}
- best K1 transformed-residual scalar alpha=3/4
- x1=(3/4,3/8)
- transformed residual squared = 1/8
- original residual squared = 5/16
- true error squared = 5/64
- K2(B,c)=R^2 because det[c,Bc]=1/2
- x*=(3/2)c-(1/2)Bc
- exact K2 residual/error = 0

## Metric firewall
- downstream readout w=(1,2)
- w^T x*=3/2
- w^T x1=3/2
- x1 nevertheless has nonzero residual and true error
- therefore exact downstream readout does not imply exact solve

## Low-dimension failure control
- B_bad=diag(1,10)
- c_bad=(1,1)
- K1=span{c_bad}
- best scalar alpha_bad=11/101
- residual=(90/101,-9/101)
- residual squared=81/101
- low subspace dimension alone is not a convergence certificate

## Durable boundaries
- every Krylov construction must name its linear operator;
- local Jacobian/surrogate operator is not the global nonlinear representation map;
- fixed-left, right, flexible, learned, state-dependent, and nonlinear preconditioners are different semantics;
- transformed residual, original residual, true solve error, representation quality, and task quality are distinct;
- classical Krylov convergence does not transfer to learned nonlinear transport by analogy;
- exact-arithmetic basis identities do not imply finite-precision orthogonality;
- restart/truncation can discard useful directions.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact rational witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
