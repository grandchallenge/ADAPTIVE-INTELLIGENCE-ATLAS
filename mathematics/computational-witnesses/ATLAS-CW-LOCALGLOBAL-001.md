# ATLAS-CW-LOCALGLOBAL-001 — Exact Finite Gluing and Obstruction Witness

**Chapter:** ATLAS-CH-LOCALGLOBAL-001  
**Witness class:** exact finite linear-algebra computation  
**Purpose:** separate global-to-local injectivity, compatible-family existence, unique gluing, and explicit overlap obstruction.

## Domain and cover

Let:

`X={a,b,c}`.

Use the cover:

`U={a,b}`;

`V={b,c}`;

`W=U intersect V={b}`.

For every subset `S`, define:

`F(S)=R^S`.

Restrictions forget coordinates outside the smaller set.

## Global-to-local map

Identify:

`F(X)=R^3`;

`F(U) direct-sum F(V)=R^4`.

Define:

`R(x,y,z)=(x,y,y,z)`.

The map R is injective.

Therefore one pair of local restrictions can come from at most one global section.

## Overlap discrepancy

Define:

`Delta(u_a,u_b,v_b,v_c)=u_b-v_b`.

Then local data are compatible exactly when:

`Delta=0`.

## Exactness

The image of R is:

`{(x,y,y,z)}`.

The kernel of Delta is:

`{(u_a,u_b,v_b,v_c):u_b=v_b}`.

Therefore:

`im(R)=ker(Delta)`.

Thus every compatible local pair has a global glue, and injectivity of R makes that glue unique.

## Compatible family

Take:

`s_U=(1,2)`;

`s_V=(2,4)`.

Then:

`Delta=2-2=0`.

The unique global glue is:

`s=(1,2,4)`.

## Incompatible family

Take:

`q_U=(1,2)`;

`q_V=(3,4)`.

Then:

`Delta=2-3=-1`.

Because the discrepancy is nonzero, the pair is not in the image of R.

No global function on X restricts to both local sections.

## Matrix form

Using column vectors:

`R =
[[1,0,0],
 [0,1,0],
 [0,1,0],
 [0,0,1]]`.

`Delta =
[0,1,-1,0]`.

Then:

`Delta R=0`.

Also:

`rank(R)=3`;

`dim ker(Delta)=3`.

Therefore:

`im(R)=ker(Delta)`.

## Claim boundary

This witness proves only the exact finite function-sheaf statements above.

It does not prove that every presheaf has the gluing property, that every engineering compatibility problem is a sheaf, that approximate disagreement has a canonical repair, or that a global section implies factual truth, semantic adequacy, numerical stability, or system correctness.
