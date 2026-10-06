# Chapter Specification — ATLAS-CH-COMPOSE-001

## Identity

**Title:** Composition Without Catastrophe  
**Part:** Numerical Intelligence and Composition  
**Status target:** draft-v0.1  
**Implementation issue:** #231  
**Protected baseline:** eab85ed47695e1c3ae19f69e85b194c48a576a31

## Hard prerequisites

- ATLAS-CH-BCONTRACT-001 / AUDIT-003;
- ATLAS-CH-SPLIT-001 / AUDIT-036.

Exact prerequisite identities and claim boundaries are frozen in:

sources/source-locks/ATLAS-CH-COMPOSE-001.yaml

No new external source authority is required for the core chapter.

## Chapter contract

Explain why separately valid components can still form an invalid system.

The chapter must separate four distinct failure surfaces:

1. **interface incompatibility** — downstream assumptions do not match upstream guarantees;
2. **budget accumulation** — locally acceptable sensitivity/error bounds exceed a system-level budget after composition;
3. **order dependence** — the same components produce different behavior when noncommuting order changes;
4. **certificate scope failure** — a local or operating-region certificate is silently promoted into a global safety claim.

The chapter must not imply:

\[
\text{all local contracts pass}
\Rightarrow
\text{global system contract passes}.
\]

A composition theorem requires an explicit composition rule and assumptions.

## Core objects

Let

\[
f:\mathcal X\to\mathcal Y,
\qquad
g:\mathcal Y\to\mathcal Z.
\]

Write local boundary contracts schematically as

\[
C_f=(\mathcal X,\mathcal Y,\Sigma_f,\mathcal I_f,\mathcal S_f,\mathcal E_f),
\]

\[
C_g=(\mathcal Y,\mathcal Z,\Sigma_g,\mathcal I_g,\mathcal S_g,\mathcal E_g).
\]

The connecting boundary is valid only if the guarantees exported by \(f\) satisfy the assumptions imported by \(g\).

Shape compatibility alone is insufficient.

## Contract compatibility relation

For the specific composition \(g\circ f\), introduce the explanatory relation

\[
C_f \triangleright C_g
\]

to mean:

- \(f(\mathcal X_{\rm op})\) lies inside the operating domain required by \(g\);
- semantic declarations agree on the meaning of the connecting state;
- required invariants are preserved or explicitly restored;
- sensitivity assumptions used by downstream bounds hold on the connecting region;
- numerical/error budgets are represented in compatible units and norms.

This symbol is Atlas explanatory notation, not a universal standard.

## Local derivative composition

At a declared differentiable operating point,

\[
J_{g\circ f}(x)
=
J_g(f(x))J_f(x).
\]

Therefore

\[
\|J_{g\circ f}(x)\|_2
\le
\|J_g(f(x))\|_2\,
\|J_f(x)\|_2.
\]

This is a local upper bound.

It may be loose.

It is not automatically a global nonlinear Lipschitz or safety theorem.

## Exact order-sensitive failure witness

Use

\[
A=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix}.
\]

Define linear components

\[
f_A(x)=Ax,
\qquad
f_B(x)=Bx.
\]

Each local gain contract is satisfied with

\[
\|A\|_2=\|B\|_2=\frac32.
\]

Set a system-level gain budget

\[
\tau=2.
\]

For column-vector states, chronological \(A\) then \(B\) is

\[
B A.
\]

Exactly,

\[
BA
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

so

\[
\boxed{\|BA\|_2=1<2.}
\]

Reverse the chronological order: \(B\) then \(A\), represented by

\[
AB.
\]

Exactly,

\[
AB
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}.
\]

For a matrix

\[
M=
\begin{pmatrix}
0&a\\
b&0
\end{pmatrix},
\]

its singular values are \(|a|\) and \(|b|\).

Hence

\[
\boxed{\|AB\|_2=\frac94>2.}
\]

Therefore the same two components, each satisfying the same individual gain contract, pass the system budget in one order and violate it in the reverse order.

The noncommutator is

\[
[A,B]
=
AB-BA
=
\begin{pmatrix}
0&5/4\\
-5/9&0
\end{pmatrix}
\ne0.
\]

This is an exact finite witness.

## Compatible commuting control

Use

\[
A_c=
\operatorname{diag}(3/2,2/3),
\]

\[
B_c=
\operatorname{diag}(2/3,3/2).
\]

Then

\[
[A_c,B_c]=0,
\]

and

\[
A_cB_c=B_cA_c=I.
\]

Each component again has

\[
\|A_c\|_2=\|B_c\|_2=\frac32,
\]

but either order yields

\[
\boxed{\|A_cB_c\|_2=1<2.}
\]

This control shows that identical component-level norm ceilings do not determine the actual composition; alignment and ordering matter.

## Local error propagation

Let \(\widehat f,\widehat g\) approximate \(f,g\).

Assume on a declared connecting domain:

\[
\|\widehat f(x)-f(x)\|
\le
\varepsilon_f,
\]

\[
\|\widehat g(y)-g(y)\|
\le
\varepsilon_g,
\]

and \(g\) is Lipschitz there with constant \(L_g\):

\[
\|g(y_1)-g(y_2)\|
\le
L_g\|y_1-y_2\|.
\]

Then

\[
\begin{aligned}
\|\widehat g(\widehat f(x))-g(f(x))\|
&\le
\|\widehat g(\widehat f(x))-g(\widehat f(x))\|\\
&\quad+
\|g(\widehat f(x))-g(f(x))\|\\
&\le
\varepsilon_g+L_g\varepsilon_f.
\end{aligned}
\]

Thus

\[
\boxed{
E_{g\circ f}
\le
\varepsilon_g+L_g\varepsilon_f.
}
\]

The connecting-domain assumption is load-bearing: \(\widehat f(x)\) must remain inside the domain where the downstream error and Lipschitz bounds apply.

## Chain error recurrence

For a chain \(f_1,\ldots,f_n\), suppose

\[
E_k
\le
L_kE_{k-1}+\varepsilon_k,
\qquad
E_0=0.
\]

Then by induction,

\[
\boxed{
E_n
\le
\sum_{j=1}^{n}
\varepsilon_j
\prod_{k=j+1}^{n}L_k.
}
\]

The empty product is \(1\).

This formula makes downstream amplification of upstream error explicit.

It remains scoped to the declared domains and constants.

## Exact finite error-budget witness

Choose two scalar stages:

\[
f(x)=x,
\qquad
g(y)=\frac32 y.
\]

Let implementation errors satisfy

\[
|\widehat f(x)-f(x)|\le\frac1{10},
\]

\[
|\widehat g(y)-g(y)|\le\frac1{10}.
\]

With

\[
L_g=\frac32,
\]

the composition guarantee is

\[
E
\le
\frac1{10}
+
\frac32\frac1{10}
=
\frac14.
\]

If a system requirement is

\[
E\le\frac15,
\]

both component-local error budgets may be individually acceptable at \(1/10\), while the derived composition budget fails:

\[
\frac14>\frac15.
\]

This is a separate failure mode from noncommutativity.

## Certificate hierarchy

The chapter must distinguish:

### Component certificate

A statement about one component on a declared operating region.

Example:

\[
\|J_f(x)\|_2\le L_f.
\]

### Interface compatibility certificate

A statement that the upstream guarantees satisfy the downstream assumptions at one boundary.

### Composition certificate

A derived statement about the composed map under explicit assumptions.

Example:

\[
\|J_gJ_f\|_2\le L_gL_f.
\]

### System-level guarantee

A property required of the complete chain.

This may involve global state reachability, distribution shift, invariants, stochasticity, feedback, adaptation, or long-horizon behavior that local certificates do not cover.

No level automatically promotes to the next.

## Local versus global

A local statement such as

\[
\|J_f(x_0)\|_2\le L
\]

does not imply

\[
\|f(x)-f(y)\|
\le
L\|x-y\|
\]

for all \(x,y\).

A global Lipschitz conclusion requires a bound over the relevant connecting region plus regularity assumptions sufficient to integrate the local bound.

Likewise, a finite collection of locally compatible interfaces does not automatically establish global closed-loop safety.

## Composition and order

The SPLIT prerequisite supplies the exact rule that order can matter when operations do not commute.

COMPOSE must preserve right-to-left matrix action for column vectors:

- chronological \(A\) then \(B\) corresponds to \(BA\);
- chronological \(B\) then \(A\) corresponds to \(AB\).

Product subscripts must not be used as ambiguous chronological labels.

## Error types must remain separate

The chapter must not collapse:

- interface semantic mismatch;
- numerical approximation error;
- local sensitivity amplification;
- splitting/order error;
- optimization error;
- modeling error;
- finite-precision error;
- stochastic variation;
- distribution shift.

Several may coexist.

One bound does not subsume the others.

## Feedback boundary

If the output of a composition is fed back into its input, a one-pass contract does not automatically control repeated iteration.

For a linear closed-loop map \(x_{t+1}=Mx_t\), one-step norm information and long-horizon behavior are different objects.

The chapter may mention this as a boundary but must not import a full stability theory without a new dependency/source route.

## Reader outcomes

A reader should be able to:

1. explain why local component validity is not sufficient for system validity;
2. derive the product-norm local gain bound;
3. reproduce the exact \(A,B\) order-sensitive witness;
4. reproduce the commuting control;
5. derive the two-stage error bound;
6. derive the \(n\)-stage error recurrence;
7. distinguish component, interface, composition, and system-level certificates;
8. identify which assumptions are operating-region dependent;
9. distinguish order/noncommutativity failure from error-budget accumulation;
10. state why no global safety theorem follows from the chapter.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{component contracts pass}
\not\Rightarrow
\text{system contract passes};
\]

\[
\|J_f(x_0)\|\le L
\not\Rightarrow
\text{global }L\text{-Lipschitz};
\]

\[
\|J_gJ_f\|\le\|J_g\|\|J_f\|
\not\Rightarrow
\text{tight composition estimate};
\]

\[
[A,B]=0\text{ in one reference model}
\not\Rightarrow
\text{learned modules commute globally};
\]

\[
\text{local error budget}
\not\Rightarrow
\text{long-horizon stability};
\]

\[
\text{interface compatibility}
\not\Rightarrow
\text{closed-loop safety}.
\]

## Required artifacts

- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- source lock;
- Chapter Ledger promotion;
- Source Register entry;
- tranche receipt;
- mandatory post-draft audit.

## Downstream handoff

COMPOSE should provide reusable language for:

- systems composition;
- mechanistic intervention pipelines;
- adaptive-depth chains;
- routing and sparse systems;
- agents and tool interfaces;
- governed adaptation;
- synthesis chapters.

Downstream chapters may inherit:

- explicit connecting-domain assumptions;
- system-budget composition discipline;
- order-sensitive witnesses;
- local versus global certificate hierarchy.

They may not inherit a universal global safety theorem.

## Source boundary

Inherited external references only:

- [@Higham2002]
- [@BaydinEtAl2018]
- [@McLachlanQuispel2002]
- [@HairerLubichWanner2006]

All external authority is inherited through the audited prerequisites.

Source lock:

sources/source-locks/ATLAS-CH-COMPOSE-001.yaml
