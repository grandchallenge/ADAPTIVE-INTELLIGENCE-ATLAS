# ATLAS-CH-COMPOSE-001 — Derivation Packet

## Scope

This packet derives exact finite composition witnesses and bounded local error-propagation statements for ATLAS-CH-COMPOSE-001.

It does not establish a universal contract calculus, a global nonlinear safety theorem, a closed-loop stability theorem, or a neural splitting theorem.

## D1. Local Jacobian composition

For differentiable

\[
f:\mathcal X\to\mathcal Y,
\qquad
g:\mathcal Y\to\mathcal Z,
\]

the chain rule gives

\[
J_{g\circ f}(x)
=
J_g(f(x))J_f(x).
\]

For the induced Euclidean operator norm,

\[
\|J_{g\circ f}(x)\|_2
\le
\|J_g(f(x))\|_2
\|J_f(x)\|_2.
\]

This is a local upper bound at the declared operating point.

It can be strict.

## D2. Exact order-sensitive pair

Let

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

Since

\[
A^\top A=
\begin{pmatrix}
9/4&0\\
0&4/9
\end{pmatrix},
\]

the singular values of \(A\) are

\[
3/2,\quad 2/3.
\]

Hence

\[
\|A\|_2=\frac32.
\]

Likewise,

\[
B^\top B
=
\begin{pmatrix}
4/9&0\\
0&9/4
\end{pmatrix},
\]

so

\[
\|B\|_2=\frac32.
\]

Each component therefore satisfies the local gain ceiling

\[
L_{\rm component}=\frac32.
\]

## D3. Chronological A then B

For column vectors, chronological \(A\) then \(B\) means

\[
x\mapsto Ax\mapsto BAx.
\]

Compute

\[
BA
=
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix}
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

This is an orthogonal permutation matrix.

Therefore

\[
(BA)^\top(BA)=I,
\]

and

\[
\boxed{\|BA\|_2=1.}
\]

For the declared system gain budget

\[
\tau=2,
\]

this order passes:

\[
1<2.
\]

## D4. Chronological B then A

Reverse the chronology:

\[
x\mapsto Bx\mapsto ABx.
\]

Compute

\[
AB
=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix}
\begin{pmatrix}
0&3/2\\
2/3&0
\end{pmatrix}
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}.
\]

Then

\[
(AB)^\top(AB)
=
\begin{pmatrix}
16/81&0\\
0&81/16
\end{pmatrix}.
\]

Thus the singular values are

\[
9/4,\quad 4/9.
\]

Hence

\[
\boxed{\|AB\|_2=\frac94.}
\]

The system gain budget fails:

\[
\frac94>2.
\]

The same two components and the same local component gain bounds therefore lead to opposite system dispositions under reversed order.

## D5. Exact commutator

Compute

\[
[A,B]
=
AB-BA.
\]

Using the previous products,

\[
[A,B]
=
\begin{pmatrix}
0&9/4\\
4/9&0
\end{pmatrix}
-
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
=
\begin{pmatrix}
0&5/4\\
-5/9&0
\end{pmatrix}.
\]

Therefore

\[
[A,B]\ne0.
\]

The exact finite witness is genuinely noncommuting.

## D6. Product-norm upper bound is loose

The generic local norm product gives

\[
\|BA\|_2
\le
\|B\|_2\|A\|_2
=
\frac94.
\]

But the exact value is

\[
\|BA\|_2=1.
\]

Thus the product bound can overestimate the true gain by a factor

\[
\frac94.
\]

For the reverse order,

\[
\|AB\|_2=\frac94
=
\|A\|_2\|B\|_2.
\]

So the same component norms can yield either a maximally aligned product or a strongly cancelling/compensating product.

Component-local norm ceilings do not determine the exact composition.

## D7. Commuting compatible control

Let

\[
A_c=
\begin{pmatrix}
3/2&0\\
0&2/3
\end{pmatrix},
\]

\[
B_c=
\begin{pmatrix}
2/3&0\\
0&3/2
\end{pmatrix}.
\]

Both are diagonal, so

\[
[A_c,B_c]=0.
\]

Their product is

\[
A_cB_c
=
B_cA_c
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
=
I.
\]

Both components again satisfy

\[
\|A_c\|_2=\|B_c\|_2=\frac32.
\]

But either chronology gives

\[
\boxed{\|A_cB_c\|_2=1.}
\]

This is a compatible commuting control with the same individual gain ceiling.

## D8. Two-stage approximation error

Let \(\widehat f,\widehat g\) approximate \(f,g\).

Assume for the declared input \(x\):

\[
\|\widehat f(x)-f(x)\|
\le
\varepsilon_f.
\]

Assume both \(\widehat f(x)\) and \(f(x)\) lie in a connecting domain \(D_g\).

Assume on \(D_g\):

\[
\|\widehat g(y)-g(y)\|
\le
\varepsilon_g
\]

and

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

Therefore

\[
\boxed{
E_{g\circ f}
\le
\varepsilon_g+L_g\varepsilon_f.
}
\]

The connecting-domain condition is essential.

Without it, the downstream bounds may not apply to the perturbed upstream output.

## D9. Exact scalar error-budget witness

Let

\[
f(x)=x,
\qquad
g(y)=\frac32 y.
\]

Suppose

\[
|\widehat f(x)-f(x)|
\le
\frac1{10},
\]

and for the connecting domain,

\[
|\widehat g(y)-g(y)|
\le
\frac1{10}.
\]

Since \(g\) is globally linear,

\[
L_g=\frac32.
\]

Thus

\[
E
\le
\frac1{10}
+
\frac32\cdot\frac1{10}
=
\frac1{10}+\frac3{20}
=
\frac5{20}
=
\frac14.
\]

If the system-level error requirement is

\[
E\le\frac15,
\]

then

\[
\frac14>\frac15.
\]

Both component-local error ceilings are \(1/10\), yet the guaranteed system error exceeds the declared system budget.

This is a budget-composition failure, not an order/noncommutativity failure.

## D10. n-stage error recurrence

Let the true chain be

\[
F_n=f_n\circ\cdots\circ f_1
\]

and the approximate chain

\[
\widehat F_n
=
\widehat f_n\circ\cdots\circ\widehat f_1.
\]

Assume recursively that on declared connecting domains,

\[
E_k
=
\|\widehat F_k(x)-F_k(x)\|
\]

satisfies

\[
E_k
\le
L_k E_{k-1}+\varepsilon_k,
\]

with

\[
E_0=0.
\]

For \(n=1\),

\[
E_1\le\varepsilon_1.
\]

Assume

\[
E_{n-1}
\le
\sum_{j=1}^{n-1}
\varepsilon_j
\prod_{k=j+1}^{n-1}L_k.
\]

Then

\[
\begin{aligned}
E_n
&\le
L_nE_{n-1}+\varepsilon_n\\
&\le
L_n
\sum_{j=1}^{n-1}
\varepsilon_j
\prod_{k=j+1}^{n-1}L_k
+
\varepsilon_n\\
&=
\sum_{j=1}^{n-1}
\varepsilon_j
\prod_{k=j+1}^{n}L_k
+
\varepsilon_n.
\end{aligned}
\]

Writing the last term with the empty product \(1\),

\[
\boxed{
E_n
\le
\sum_{j=1}^{n}
\varepsilon_j
\prod_{k=j+1}^{n}L_k.
}
\]

This makes downstream amplification explicit.

## D11. Equal local ceilings do not imply equal global error

Suppose every stage has

\[
L_k=L
\]

and

\[
\varepsilon_k=\varepsilon.
\]

Then the recurrence gives

\[
E_n
\le
\varepsilon
\sum_{r=0}^{n-1}L^r.
\]

If \(L\ne1\),

\[
E_n
\le
\varepsilon
\frac{L^n-1}{L-1}.
\]

If \(L=1\),

\[
E_n\le n\varepsilon.
\]

Thus even a uniform local error budget can accumulate linearly or geometrically in the derived worst-case bound.

This does not establish that the worst case is attained.

## D12. Contract compatibility is not shape compatibility

Let an upstream component export a normalized direction:

\[
f_{\rm dir}(x)
=
\frac{x}{\|x\|}.
\]

Let a downstream component interpret norm as amplitude.

Shapes match.

Semantics do not.

This inherited BCONTRACT witness establishes:

\[
\text{shape compatibility}
\not\Rightarrow
\text{semantic compatibility}.
\]

COMPOSE inherits the lesson but does not duplicate the prerequisite proof as new authority.

## D13. Local certificate hierarchy

Define four evidence levels.

### Component-local statement

Example:

\[
\|J_f(x_0)\|_2\le L_f.
\]

### Interface statement

Example:

\[
f(x_0)\in D_g
\]

and the semantics/invariants required by \(g\) hold.

### Derived composition statement

Example:

\[
\|J_g(f(x_0))J_f(x_0)\|_2
\le
L_gL_f.
\]

### System-level statement

Example:

\[
\text{all reachable states satisfy a declared safety property}.
\]

The first three do not imply the fourth without additional assumptions.

## D14. Local Jacobian bound is not a global Lipschitz theorem

A bound at one point,

\[
\|J_f(x_0)\|\le L,
\]

contains no information about the derivative far from \(x_0\).

Therefore it cannot by itself imply

\[
\|f(x)-f(y)\|
\le
L\|x-y\|
\]

for all \(x,y\).

A global conclusion needs a bound over the relevant region plus sufficient regularity and path/connectivity assumptions.

This is a scope statement, not a negative theorem about every possible route to global control.

## D15. Interface compatibility is not closed-loop stability

Suppose \(f\) and \(g\) compose correctly for one pass.

If the system iterates

\[
x_{t+1}
=
(g\circ f)(x_t),
\]

long-horizon behavior depends on repeated application.

One-pass interface compatibility does not alone determine:

- boundedness;
- convergence;
- transient growth;
- invariant-set preservation;
- stochastic robustness.

Those require additional dynamical assumptions.

COMPOSE records this as a boundary and does not import a new stability theorem.

## D16. Durable propositions

1. The chain rule makes local differential obligations compose by matrix multiplication.
2. Operator-norm component ceilings provide a valid product upper bound but not the exact composite gain.
3. Two individually valid components can satisfy or violate the same system gain budget depending only on order.
4. The exact \(A,B\) witness has component norms \(3/2\), forward chronology \(A\to B\) gain \(1\), reverse chronology \(B\to A\) gain \(9/4\).
5. The exact commuting control has the same component norms and gain \(1\) in either order.
6. Approximation errors compose as \(\varepsilon_g+L_g\varepsilon_f\) under explicit connecting-domain assumptions.
7. In an \(n\)-stage chain, upstream errors are weighted by downstream gain products.
8. Individually acceptable local error budgets can exceed a stricter system-level budget after composition.
9. Local/interface/composition certificates are distinct from system-level global guarantees.
10. No result in this packet proves universal compositional safety for learned systems.
