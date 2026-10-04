# AUDIT-040 — The Geometry of Position

## Disposition

**PASS**

ATLAS-CH-POSGEOM-001 is fit to remain at \`draft-v0.1\`.

No mathematical, source-scope, prose, or repository repair is required by this audit.

## Audited implementation

- implementation issue: #159
- implementation PR: #160
- implementation merge: \`26c51843b13a0ab58ba0f16cd0c2e365a60d1180\`
- audit issue: #161
- audit branch: \`audit/posgeom-161\`
- chapter: \`ATLAS-CH-POSGEOM-001\`

Exact merged artifact identities:

- specification: \`5ad12ea20e32919f44921ae32914dd963a2c848f\`
- derivation packet: \`bf6aabc1c99a68ee21128e6a29e0f3fceefc62c2\`
- computational witness: \`c013246c849d48a08b7bdf9aabc66ebac193accc\`
- manuscript: \`841bc96c696e58fb7914c851c7c13f2e5d076b53\`
- source lock: \`a94a592d68a5f6ddadf450127dde0e261acf429f\`
- bibliography: \`47e9d77a567aa93aad4e00be768d2901e65666f3\`
- Chapter Ledger: \`4322c3ad314904cfeb9a0ed7f56a2bd6cf1c0ee7\`
- Source Register: \`a285da0fc538a20435895cbdc8dbe5f363db06c4\`
- tranche receipt: \`1125350b6129fb377fa0a96e8a618cbb53311357\`

## 1. Hard prerequisites

PASS.

The chapter binds both audited prerequisites at the protected implementation baseline.

### Attention as an Operator

- manuscript: \`d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c\`
- source lock: \`4af4e53230776daaf0be825cffd1263957ed97c8\`
- AUDIT-002: \`4671995f0cd7465a5df2bb60431244f482e5e3c9\`

The inherited interface is limited to query/key/value and score/operator notation, plus permutation equivariance in the absence of positional asymmetry.

### Geometry

- manuscript: \`f8e406f24a01bd852996e11118e04427ff549f35\`
- source lock: \`d75e8bcf5a5920eca6b09cb8bb181182c7827b5c\`
- AUDIT-001: \`f13b7ac01f7b10dfadd64da6f31c45832344c082\`

The inherited interface is limited to rotations, orthogonality, and exact geometric/invariance discipline.

## 2. External source identity

PASS.

Independent source review confirms the chapter's four external roles.

### Vaswani et al. (2017)

The original Transformer source presents fixed sinusoidal positional encodings as additive features and states the motivation that a fixed offset can be represented by a linear function of the sinusoidal encoding.

The chapter correctly treats the paper's extrapolation language as motivation rather than a universal theorem.

### Su et al. (2021)

RoFormer introduces RoPE as position-dependent rotations and explicitly describes the resulting relative-position dependence in self-attention.

The chapter's exact block-rotation algebra is consistent with that mechanism.

### Chen et al. (2023)

Position Interpolation linearly downscales input position indices to fit the original context range and reports long-context extension with limited fine-tuning under the paper's experiments.

The chapter correctly scopes the paper's theoretical interpolation-versus-extrapolation comparison to the method's stated setting.

### Peng et al. (2023)

YaRN is correctly used as a primary empirical context-extension reference.

The chapter does not promote its reported long-context results into a universal guarantee.

## 3. Additive sinusoid versus rotary mechanism

PASS.

The chapter explicitly separates:

- additive sinusoidal position features;
- multiplicative/block-rotational transformation of query/key coordinates.

The shared use of sine/cosine structure is not used to collapse the two mechanisms.

## 4. Exact rotary identity

PASS.

For

\[
R(\phi)=
\begin{pmatrix}
\cos\phi&-\sin\phi\\
\sin\phi&\cos\phi
\end{pmatrix},
\]

the derivation uses

\[
R(\phi)^\top=R(-\phi),
\]

hence

\[
R(m\omega)^\top R(n\omega)
=
R((n-m)\omega).
\]

Therefore

\[
(R_m q)^\top(R_n k)
=
q^\top R((n-m)\omega)k.
\]

The sign convention is internally consistent.

## 5. Same-offset witness

PASS.

With

\[
\theta=\pi/6,
\qquad
q=k=(1,0)^\top,
\]

the pairs \((0,2)\) and \((3,5)\) both have relative offset 2 and both give

\[
\cos(2\theta)=\cos(\pi/3)=1/2.
\]

The different-offset pair \((1,4)\) has offset 3 and gives

\[
\cos(3\theta)=\cos(\pi/2)=0.
\]

## 6. Generic-vector replay

PASS.

For

\[
q=(1,2)^\top,
\qquad
k=(3,-1)^\top,
\qquad
m=2,
\qquad
n=5,
\qquad
\theta=\pi/6,
\]

the relative phase is \(\pi/2\).

Then

\[
R(\pi/2)k=(1,3)^\top
\]

and

\[
q^\top R(\pi/2)k=7.
\]

The direct transformed inner product gives the same value.

## 7. Non-orthogonal control

PASS.

For

\[
S_m=\operatorname{diag}(2^m,1)
\]

and \(q=k=(1,0)^\top\),

\[
(S_mq)^\top(S_nk)=2^{m+n}.
\]

Thus:

- \((0,2)\) gives \(4\);
- \((3,5)\) gives \(256\).

The relative offset is equal while the score differs.

This is a valid bounded counterexample to the idea that arbitrary position-dependent transforms inherit relative-only dependence.

## 8. Multi-frequency extension

PASS.

The chapter uses block-diagonal rotations.

Because the transpose/product identity holds independently per block, the full block-diagonal operator satisfies the same relative-offset closure.

No cross-block mixing claim is made.

## 9. Common-translation boundary

PASS.

For a common shift \(c\),

\[
(n+c)-(m+c)=n-m,
\]

so the rotary query-key contribution is unchanged.

The chapter explicitly avoids promoting this into full-model translation invariance.

That qualification is load-bearing because masking, boundaries, content placement, and other operations can break the symmetry.

## 10. Multidimensional construction

PASS.

For coordinate \(p=(u,v)\), the chapter defines a direct-product positional action

\[
R_p=
\operatorname{diag}
(R(u\omega_x),R(v\omega_y)).
\]

Then pairwise relative structure depends on the coordinate displacement.

The witness with offsets \((2,3)\), frequencies \((\pi/2,\pi/3)\), and resulting relative operator \(-I_4\) is exact.

The text correctly presents this as one explicit construction rather than a theorem that every multidimensional positional system must factor this way.

## 11. Position Interpolation

PASS.

The chapter represents the interpolation map schematically as

\[
m\mapsto mL/L'
\]

for original scale \(L\) and target scale \(L'>L\).

This captures the source's linear index downscaling.

The text states clearly that this is a method-level intervention, not a guarantee of model quality.

## 12. Long-context epistemic boundary

PASS.

The chapter makes the central distinction:

\[
\text{formula extrapolates}
\neq
\text{trained model generalizes}.
\]

That distinction is consistent across the source lock, specification, derivation packet, witness, and manuscript.

Exact continuation of the positional formula is not used as evidence for arbitrary-length retrieval, calibration, optimization stability, or task quality.

## 13. Frequency scaling versus index scaling

PASS.

The chapter notes that both interventions alter phases but are operationally distinct.

It does not claim equivalence in a full multi-frequency trained model.

## 14. Mask interaction

PASS.

The chapter separates:

- score geometry for an admissible query-key pair;
- support constraints imposed by masking.

This remains consistent with the audited Attention prerequisite.

## 15. Downstream RPO boundary

PASS.

RPO may inherit:

- block-rotation notation;
- exact relative-offset identity;
- multi-frequency decomposition;
- multidimensional product construction;
- algebra-versus-generalization boundary.

RPO must independently establish:

- low-dimensional relative-position operator structure;
- frequency-mode decomposition beyond the ordinary RoPE block statement;
- DC components;
- head specialization.

No downstream theorem is smuggled upstream.

## 16. Repository integrity

PASS.

The implementation passed canonical validation after one mechanical serialization repair.

The repair replaced an incorrectly escaped manuscript payload with raw-string serialization.

A post-repair scan found no remaining control characters in the chapter artifacts.

The canonical artifact paths in the Chapter Ledger exist.

The source lock is registered.

The manuscript contains:

- an epistemic-status marker;
- a References section;
- the exact source-lock path.

The computational witness contains a Claim boundary.

No governed figure is required.

## Final disposition

AUDIT-040 passes without further repair.

The durable layer is:

**additive-versus-rotary positional distinction + exact block-rotation relative-position identity + multi-frequency and multidimensional product structure + explicit non-orthogonal control + exact algebra versus empirical long-context generalization boundary.**
