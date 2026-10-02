# Normality, Pseudospectra, and Transient Growth
<!-- ATLAS-CH-NONNORMAL-001 -->

**Epistemic status:** mathematical exposition with source-locked standard results and Atlas-owned finite-dimensional derivations.  
**Norm convention:** spectral/operator (2)-norm unless explicitly stated otherwise.  
**Primary figure:** `ATLAS-FIG-PSPECTRUM-001`  
**Derivation packet:** `mathematics/derivations/ATLAS-CH-NONNORMAL-001-DERIVATIONS.md`

## 1. The eigenvalue story can be true and still be incomplete

A standard stability instinct is to inspect eigenvalues.

For the discrete linear system

[
x_{t+1}=Ax_t,
]

if every eigenvalue of (A) lies strictly inside the unit disk, then (A^t	o0) under the usual finite-dimensional hypotheses. The asymptotic statement is correct.

It does not follow that every disturbance shrinks monotonically on the way to zero.

That gap between eventual decay and finite-time behavior is the subject of this chapter.

The smallest useful counterexample fits in a (2	imes2) matrix. The lesson scales far beyond it.

Consider

[
A=
egin{pmatrix}
a & K\
0 & a
end{pmatrix},
qquad
|a|<1.
]

Both eigenvalues equal (a). If the eigenvalue plot were all we saw, the system would appear almost boring: one stable point, repeated twice.

Yet for large enough (K), the matrix can strongly amplify some inputs before its asymptotic decay wins.

The matrix is **non-normal**.

That word is not a synonym for unstable. It identifies a geometric property of the operator that determines how safely eigenvalue intuition can be converted into statements about finite-time amplification.

## 2. Normality

A complex matrix (A) is normal when

[
A^*A=AA^*,
]

where (A^*) denotes the conjugate transpose.

Real symmetric matrices are normal. Orthogonal and unitary matrices are normal. More generally, a finite-dimensional matrix is normal exactly when it can be diagonalized by a unitary change of basis.

Thus

[
A=ULambda U^*
]

with (U) unitary.

For such a matrix,

[
A^k=ULambda^kU^*,
]

and the spectral (2)-norm obeys

[
|A^k|_2
=
|Lambda^k|_2
=
max_i|lambda_i|^k
=
ho(A)^k.
]

For a normal matrix, the eigenvalue picture and the (2)-norm growth picture align perfectly.

If (ho(A)<1), then every power decays monotonically in operator norm.

This is one reason normal operators are so pleasant: their eigenvectors form an orthonormal basis, so modal directions do not interfere geometrically.

## 3. Non-normality is about geometry between directions

A matrix can be diagonalizable without being normal.

Suppose

[
A=VLambda V^{-1}
]

with a non-unitary eigenvector matrix (V). Then

[
A^k
=
VLambda^kV^{-1},
]

and therefore

[
|A^k|_2
le
|V|_2,
|V^{-1}|_2,
|Lambda^k|_2.
]

Writing

[
kappa_2(V)=|V|_2|V^{-1}|_2,
]

we obtain

[
|A^k|_2
le
kappa_2(V)ho(A)^k
]

when the eigenvalues are ordered by magnitude.

The factor (kappa_2(V)) is absent in the normal case because a unitary (V) has condition number one.

This gives the first geometric clue: if eigenvectors become nearly linearly dependent, a state can be represented as a large cancellation among modal components. The modes may each decay while the cancellation changes in a way that temporarily increases the physical norm.

The useful allegory is a harbor with aligned currents.

Imagine two currents that eventually carry every floating object toward calm water. If the currents point in nearly the same geometric direction, motion can be transferred between them so that the observable displacement grows before the long-term decay dominates.

The correspondence is:

- asymptotic modal decay ↔ eigenvalues inside the unit disk;
- nearly aligned modal directions ↔ non-orthogonal eigenvectors or generalized directions;
- temporary surge ↔ transient growth of (|A^k|).

The limit of the allegory is equally important. A matrix is not literally a fluid, and non-normality is not identical to hydrodynamic energy transfer. Fluid mechanics is historically important here because it provided striking applications of pseudospectral and transient-growth analysis [@ReddySchmidHenningson1993; @TrefethenEtAl1993]. The mathematics is more general.

## 4. An exact two-dimensional example

Return to

[
A=
egin{pmatrix}
a & K\
0 & a
end{pmatrix}.
]

Write

[
A=aI+KN,
qquad
N=
egin{pmatrix}
0&1\
0&0
end{pmatrix}.
]

Since (N^2=0),

[
A^n
=
a^nI
+
n a^{n-1}KN.
]

Therefore

[
oxed{
A^n=
egin{pmatrix}
a^n & nKa^{n-1}\
0 & a^n
end{pmatrix}.
}
]

The eigenvalues remain (a). The spectral radius of every power is

[
ho(A^n)=|a|^n.
]

But the off-diagonal term is

[
nKa^{n-1}.
]

For (|a|<1), this term eventually decays. Before it decays, the factor (nK) can make it large.

This is transient amplification in its simplest exact form.

## 5. The operator norm says what the eigenvalue plot does not

For

[
B=
egin{pmatrix}
p&q\
0&p
end{pmatrix},
]

we compute

[
B^	op B
=
egin{pmatrix}
p^2&pq\
pq&p^2+q^2
end{pmatrix}.
]

Its eigenvalues are

[
lambda_{pm}
=
rac{
2p^2+q^2
pm
|q|sqrt{4p^2+q^2}
}{2}.
]

Thus

[
|B|_2
=
sqrt{lambda_+}.
]

Substituting

[
p=a^n,qquad q=nKa^{n-1},
]

gives an exact expression for (|A^n|_2).

The formula looks more complicated than the spectral radius because finite-time gain depends on singular geometry, not eigenvalues alone.

This is a recurring theme in the Atlas:

> eigenvalues describe invariant modal rates; singular values describe worst-case instantaneous or finite-horizon amplification.

Neither replaces the other.

## 6. Same eigenvalues, different behavior

The Atlas witness fixes

[
a=rac45,qquad K=4.
]

Then

[
A=
egin{pmatrix}
4/5&4\
0&4/5
end{pmatrix}.
]

Compare it with the normal matrix

[
N_0=rac45 I.
]

The two matrices have exactly the same eigenvalue multiset:

[
{0.8,0.8}.
]

For the normal matrix,

[
|N_0^n|_2=(0.8)^n.
]

It decays immediately.

For the non-normal matrix, an exact Wolfram evaluation of the derived norm over (n=0,dots,40) gives

[
max |A^n|_2
=
8.2124290544ldots
]

at

[
n=4.
]

The system whose eigenvalues suggest simple decay amplifies some input by more than a factor of eight before decaying.

That is not a numerical accident. It follows from the exact power formula.

## 7. The first Atlas plate

![Two-panel comparison: the non-normal matrix has large finite-horizon 2-norm amplification while the matched normal matrix decays; its epsilon-pseudospectral circles are also much larger despite identical eigenvalues.](../../figures/masters/ATLAS-FIG-PSPECTRUM-001.png)

The left panel compares finite-horizon (2)-norm gain for the non-normal (A) and the matched normal matrix (N_0).

The right panel compares their (arepsilon)-pseudospectral boundaries.

The figure is generated by Wolfram Language 15.0.1 from the source-controlled file

`figures/wolfram/ATLAS-FIG-PSPECTRUM-001.wl`.

The curves and circles are not hand-drawn explanatory art. They are derived from the exact matrices stated above. Panel layout and annotation are editorial; the mathematics is literal.

## 8. From spectrum to pseudospectrum

The spectrum asks:

> for which (z) is (zI-A) singular?

The pseudospectrum asks a more graded question:

> for which (z) is (zI-A) nearly singular?

For the spectral (2)-norm, one convenient finite-dimensional definition is

[
Lambda_arepsilon(A)
=
left{
zinmathbb C:
sigma_{min}(zI-A)learepsilon
ight}.
]

Outside the spectrum,

[
|(zI-A)^{-1}|_2
=
rac{1}{sigma_{min}(zI-A)},
]

so equivalently

[
Lambda_arepsilon(A)
=
left{
z:
|(zI-A)^{-1}|_2gearepsilon^{-1}
ight}
cupsigma(A).
]

A further equivalent characterization says that (z) belongs to the (arepsilon)-pseudospectrum exactly when it is an eigenvalue of some perturbed matrix (A+E) with (|E|_2learepsilon). This perturbation formulation is standard in the pseudospectra literature [@TrefethenEmbree2005; @ReddySchmidHenningson1993].

The pseudospectrum therefore measures more than where the eigenvalues are. It reveals how sensitive spectral behavior is to perturbation and how large the resolvent can become away from the exact spectrum.

## 9. An exact pseudospectrum, not a numerical contour

For our matrix,

[
zI-A
=
egin{pmatrix}
z-a&-K\
0&z-a
end{pmatrix}.
]

Let

[
r=|z-a|.
]

The squared singular values are

[
sigma_{pm}^2
=
rac{
2r^2+K^2
pm
Ksqrt{K^2+4r^2}
}{2},
qquad K>0.
]

On the (arepsilon)-pseudospectral boundary,

[
sigma_{min}=arepsilon.
]

The product of the two singular values is the magnitude of the determinant:

[
sigma_{max}sigma_{min}
=
|det(zI-A)|
=
r^2.
]

Thus

[
sigma_{max}
=
rac{r^2}{arepsilon}.
]

The sum of the squared singular values is

[
sigma_{max}^2+sigma_{min}^2
=
2r^2+K^2.
]

Substitution gives

[
rac{r^4}{arepsilon^2}
+
arepsilon^2
=
2r^2+K^2.
]

Rearranging,

[
(r^2-arepsilon^2)^2
=
K^2arepsilon^2.
]

Because (sigma_{max}gesigma_{min}) implies (r^2gearepsilon^2), the relevant branch is

[
oxed{
r^2=arepsilon(arepsilon+K).
}
]

Therefore

[
oxed{
Lambda_arepsilon(A)
=
left{
z:
|z-a|
le
sqrt{arepsilon(arepsilon+K)}
ight}.
}
]

For the normal comparison

[
N_0=aI,
]

we have simply

[
oxed{
Lambda_arepsilon(N_0)
=
{z:|z-a|learepsilon}.
}
]

The eigenvalue plot is identical. The pseudospectral neighborhoods are not.

For small (arepsilon),

[
sqrt{arepsilon(arepsilon+K)}
sim
sqrt{Karepsilon},
]

which is much larger than (arepsilon) when (K) is large.

This is why the right panel of the figure opens dramatically around the non-normal operator.

## 10. What “nearly singular” buys us

The resolvent

[
(zI-A)^{-1}
]

acts as a frequency-like or response-like object in many linear problems. If its norm is large, a small forcing or perturbation can produce a large response.

Pseudospectra map those regions of large resolvent norm.

This is one reason the subject became influential in hydrodynamic stability. Classical eigenvalue analysis could predict modal decay while experiments and simulations exhibited strong finite-time amplification. Pseudospectral analysis made the missing sensitivity visible [@TrefethenEtAl1993].

The lesson should not be overgeneralized. The Atlas does not infer from this history that every transient in a learning system is a pseudospectral phenomenon. The correct transfer is methodological:

> if a system is non-normal, finite-time amplification and perturbation sensitivity require tools beyond an eigenvalue plot.

## 11. Spectral radius, norm, and horizon

Three quantities answer different questions.

### Spectral radius

[
ho(A)=max_i|lambda_i|.
]

It is central to asymptotic power behavior.

### One-step operator norm

[
|A|_2=sigma_{max}(A).
]

It measures the largest one-step amplification of Euclidean norm.

### Finite-horizon gain

[
G(k)=|A^k|_2.
]

It measures the largest amplification over exactly (k) repeated steps.

For a normal matrix these quantities align unusually well:

[
G(k)=ho(A)^k.
]

For a non-normal matrix, they can separate dramatically.

That separation is the phenomenon, not a pathology in the mathematics.

## 12. Diagonalizable does not mean harmless

The Jordan-like example is defective when (K
eq0): it has only one eigenvector. It is useful because the derivation is exact.

But non-normal transient growth does not require defectiveness.

A diagonalizable matrix

[
A=VLambda V^{-1}
]

can still have nearly parallel eigenvectors and a large (kappa_2(V)). In that case, modal coordinates are badly conditioned. Large intermediate cancellations can occur even though every modal coefficient decays according to (Lambda^k).

Thus the deeper contrast is not

[
	ext{diagonalizable}
quad	ext{versus}quad
	ext{non-diagonalizable}.
]

It is closer to

[
	ext{orthogonal modal geometry}
quad	ext{versus}quad
	ext{non-orthogonal modal geometry}.
]

Normality provides the cleanest finite-dimensional boundary for that distinction.

## 13. Pseudospectra are norm-dependent

The Atlas fixes the spectral (2)-norm in this chapter.

That choice is not invisible.

For a different induced norm, the numerical shape and size of the pseudospectrum can change. Statements about “large pseudospectra” should therefore specify the norm.

Likewise, transient gain depends on the norm used to measure state magnitude.

In applications, Euclidean energy may be natural, but not always. A physically or statistically meaningful metric can induce a different operator norm.

This is not a technical footnote. It connects directly back to the previous chapter: geometry determines what a magnitude means.

## 14. A useful finite-time question

Suppose a system is asymptotically stable.

The question

> Does it converge?

may be too weak for an adaptive system.

We may instead need to ask:

> Before it converges, how much can it amplify perturbations?

For training dynamics, routing systems, recurrent computation, or iterative numerical methods, a large transient can be operationally decisive even if the asymptotic fixed point is stable.

Finite precision can saturate. Nonlinearities can activate. A downstream subsystem can leave its valid regime. An optimizer can enter a region from which the local linearization no longer applies.

None of those consequences are contained in the linear theory alone. But the linear transient can be the event that exposes them.

## 15. Bridge to optimizer-state dynamics

Later we will treat an optimizer and its internal state as a coupled dynamical system.

A local update may be written

[
z_{t+1}=F_t(z_t),
]

with local Jacobian

[
J_t=D F_t(z_t).
]

Over (k) steps, perturbations are propagated by

[
J_{t+k-1}cdots J_t.
]

Even if each local spectrum appears benign, non-normal geometry and time variation can create finite-horizon amplification.

This chapter supplies the mathematics needed to formulate that possibility.

It does not yet establish that any particular optimizer exhibits the mechanism. That requires an optimizer-specific model or measurement. The later chapter on Optimizer-State Dynamics will make that transition explicitly.

## 16. Five statements we will not make

### “Non-normal means unstable.”

False. The Atlas example is asymptotically stable.

### “Spectral radius below one means every perturbation shrinks immediately.”

False for non-normal matrices.

### “A large pseudospectrum proves transient growth of a particular magnitude.”

Not by itself. Pseudospectra provide sensitivity and growth information through precise bounds and relationships, but the statement being made must specify the relevant theorem, norm, and horizon [@TrefethenEmbree2005].

### “A transient spike proves eventual divergence.”

False. Transient amplification and asymptotic instability are different phenomena.

### “Eigenvalues are useless.”

False. The point is insufficiency, not irrelevance.

The spectrum remains an essential invariant. Pseudospectra and singular-value growth answer questions that the spectrum alone does not.

## 17. What the Wolfram witness establishes

The rendered plate is a computational witness for one exact system.

It establishes:

1. (A) and (N_0) have the same eigenvalues;
2. their finite-horizon (2)-norm gains differ strongly;
3. the non-normal example reaches gain (8.2124290544ldots) at (n=4) over the inspected range;
4. the plotted pseudospectral circles follow the exact analytic radii
   [
   sqrt{arepsilon(arepsilon+K)}
   ]
   for (A) and
   [
   arepsilon
   ]
   for (N_0).

Wolfram Language 15.0.1 independently verified the symbolic matrix power and the boundary substitution recorded in the derivation packet.

The witness does not establish prevalence in machine learning.

## 18. Atlas connections

**Spectral shaping.**  
An optimizer or architecture can alter singular geometry without merely moving eigenvalues.

**Optimizer-State Dynamics.**  
The coupled state Jacobian may exhibit transient amplification invisible to a parameter-only analysis.

**Router Dynamics.**  
A routing system can have stable-looking average behavior while perturbations amplify over short horizons.

**Spectral Diagnostics.**  
Pseudospectra, singular values, effective rank, and ordinary eigenvalues become complementary probes rather than competing doctrines.

**Numerical stability.**  
Iteration stability is a finite-horizon computational question as well as an asymptotic one.

The conceptual shift is:

[
	ext{Where are the eigenvalues?}
]

becomes

[
	ext{What can this operator do to perturbations over the horizon that matters?}
]

## 19. Closing view

The spectrum is a set of points.

The pseudospectrum is a landscape of sensitivity around those points.

For normal operators, that landscape hugs the spectrum tightly and eigenvalue intuition is unusually trustworthy. For non-normal operators, the landscape can swell outward, revealing directions in which small perturbations or finite-time propagation become unexpectedly large.

Our (2	imes2) example is intentionally small enough that nothing is hidden behind simulation. Its eigenvalues are stable. Its powers are exact. Its singular values are exact. Its pseudospectral circles are exact.

And still, the naive story fails.

That is the utility of a good counterexample: it does not merely contradict an intuition. It tells us which extra object must enter the mathematics.

Here, that object is the geometry of the operator beyond its eigenvalues.

## References used in this chapter

- [@HornJohnson2012]
- [@TrefethenEmbree2005]
- [@ReddySchmidHenningson1993]
- [@TrefethenEtAl1993]

See `sources/source-locks/ATLAS-CH-NONNORMAL-001.yaml` for exact source identities and claim scope.
