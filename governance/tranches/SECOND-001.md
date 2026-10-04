# SECOND-001 — Curvature and Second-Order Structure

## Identity

- chapter: ATLAS-CH-SECOND-001
- implementation issue: #163
- protected baseline: 8fbae32144f94e497203b311cc0a824f8cd8a486
- work branch: work/atlas-163
- hard prerequisites:
  - ATLAS-CH-OPTBASE-001
  - ATLAS-CH-GEOM-001

## Exact prerequisite binds

OPTBASE:
- manuscript: 42df47c50c2d6d26da65a58b230040e2663f901f
- source lock: fa610d3d763cc1a7e76ee4b83e85ce2c965c2825
- AUDIT-012: 28929ba6b4a16a3cef4a871fd9253d76e8a93634

GEOM:
- manuscript: f8e406f24a01bd852996e11118e04427ff549f35
- source lock: d75e8bcf5a5920eca6b09cb8bb181182c7827b5c
- AUDIT-001: f13b7ac01f7b10dfadd64da6f31c45832344c082

## External source set

- Nocedal and Wright (2006), Numerical Optimization.
- Amari (1998), Natural Gradient Works Efficiently in Learning.
- Pearlmutter (1994), Fast Exact Multiplication by the Hessian.
- Parikh and Boyd (2014), Proximal Algorithms.

## Exact witness set

Positive-definite quadratic:
- H=diag(1,4)
- b=(1,1)^T
- x0=0
- Newton step=(1,1/4)^T
- objective 0 -> -5/8
- directional derivative=-5/4

Indefinite control:
- f(x,y)=1/2(x^2-y^2)
- z0=(0,1)^T
- g=(0,-1)^T
- H=diag(1,-1)
- raw Newton step=(0,-1)^T
- g^T p_N=1 > 0
- objective -1/2 -> 0

Trust-region control:
- radius Delta=1
- exact model minimizer p_TR=(0,1)^T
- model change=-3/2
- objective at new point=-2

Metric witness:
- G=diag(1,4)
- g=(1,1)^T
- Euclidean direction=(-1,-1)^T
- metric direction=(-1,-1/4)^T

Hessian-vector witness:
- v=(2,-1)^T
- Hv=(2,-4)^T

Secant witness:
- s=(1,2)^T
- y=Hs=(1,8)^T

Proximal witness:
- threshold alpha*lambda=1
- prox(3)=2
- prox(-3)=-2
- prox(1/2)=0

## Durable boundaries

- Hessian != Fisher information in general.
- Natural gradient != Newton in general.
- Indefinite Newton can be ascent.
- Quasi-Newton approximation != exact Hessian.
- Trust region != step clipping.
- HVP access != explicit Hessian formation.
- Proximal operator != gradient clipping.
- Positive local curvature != global convexity.
- Exact local quadratic model != global optimum.

## Artifact set

- sources/source-locks/ATLAS-CH-SECOND-001.yaml
- sources/bibliography.bib
- manuscript/specifications/ATLAS-CH-SECOND-001.md
- mathematics/derivations/ATLAS-CH-SECOND-001-DERIVATIONS.md
- mathematics/computational-witnesses/ATLAS-CW-SECOND-001.md
- manuscript/parts/05-optimization/ATLAS-CH-SECOND-001.md
- governance/CHAPTER_LEDGER.yaml
- governance/SOURCE_REGISTER.yaml
- this receipt

## Remaining gates

Canonical validation, implementation merge, bounded post-draft audit, in-scope repairs, audit validation/merge, issue closure, fresh frontier recomputation, handoff update, and controller reset.
