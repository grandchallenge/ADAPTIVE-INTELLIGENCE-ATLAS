# ATLAS-CW-MINCURR-001 — Exact Minimal Teaching-Basis Witness

**Chapter:** ATLAS-CH-MINCURR-001  
**Purpose:** exact replay of relative teaching-set minimality and the high-progress/non-basis control.

## W1. Concept class

Probe set:

\[
Q=\{q_1,q_2\}.
\]

Concept class:

\[
H=\{h_{00},h_{01},h_{10},h_{11}\},
\]

with each concept represented by its ordered outputs on \((q_1,q_2)\).

Target:

\[
h^\star=h_{11}=(1,1).
\]

## W2. Teaching examples

\[
e_1=(q_1,1),
\qquad
e_2=(q_2,1).
\]

For any finite set \(T\) of labeled experiences, restrict to \(T_Q=\{(q,y)\in T:q\in Q\}\). The **target-relative** version space is:

\[
V_H(T)=\{h\in H:\forall(q,y)\in T_Q,\ h(q)=y\}.
\]

This explicitly matches the replay code below, which skips auxiliary probes outside \(Q\); it is not an assertion that such experiences are globally uninformative.

## W3. Exact basis

For:

\[
T^\star=\{e_1,e_2\},
\]

\[
\boxed{
V_H(T^\star)=\{h_{11}\}.
}
\]

So the declared exact reconstructor uniquely recovers the target.

## W4. Strict-smaller candidates

\[
V_H(\varnothing)
=
\{h_{00},h_{01},h_{10},h_{11}\},
\]

\[
V_H(\{e_1\})
=
\{h_{10},h_{11}\},
\]

\[
V_H(\{e_2\})
=
\{h_{01},h_{11}\}.
\]

All strict smaller subsets have version-space size greater than one.

Therefore:

\[
\boxed{
|T^\star|=2
}
\]

is the exact minimum for the declared witness.

## W5. High-progress/non-basis control

Introduce auxiliary experience:

\[
e_3=(z,1),
\qquad
z\notin Q.
\]

Freeze progress scores:

\[
p(e_1)=1,
\qquad
p(e_2)=1,
\qquad
p(e_3)=5.
\]

Because \(z\) is outside the target probe family:

\[
\boxed{
V_H(\{e_3\})=H.
}
\]

Thus the highest-progress experience reduces target ambiguity by zero.

Yet \(e_1\) or \(e_2\) each reduce the version space from four hypotheses to two.

Hence:

\[
\boxed{
\text{highest progress}
\not\Rightarrow
\text{minimal target-basis membership}.
}
\]

## W6. Minimal exact replay code

    from itertools import combinations

    H = {
        "h00": {"q1": 0, "q2": 0},
        "h01": {"q1": 0, "q2": 1},
        "h10": {"q1": 1, "q2": 0},
        "h11": {"q1": 1, "q2": 1},
    }

    target = "h11"

    e1 = ("q1", 1)
    e2 = ("q2", 1)
    e3 = ("z", 1)

    def version_space(examples):
        out = []
        for name, h in H.items():
            ok = True
            for q, y in examples:
                # Auxiliary experiences outside the declared target probe
                # family impose no target-class constraint.
                if q not in ("q1", "q2"):
                    continue
                if h[q] != y:
                    ok = False
                    break
            if ok:
                out.append(name)
        return tuple(out)

    assert version_space(()) == ("h00", "h01", "h10", "h11")
    assert version_space((e1,)) == ("h10", "h11")
    assert version_space((e2,)) == ("h01", "h11")
    assert version_space((e1, e2)) == ("h11",)

    basis = (e1, e2)

    # Every strict smaller subset fails unique target reconstruction.
    for r in range(len(basis)):
        for subset in combinations(basis, r):
            assert len(version_space(subset)) > 1

    assert len(version_space(basis)) == 1
    assert version_space(basis)[0] == target

    progress = {e1: 1, e2: 1, e3: 5}

    assert progress[e3] > progress[e1]
    assert progress[e3] > progress[e2]
    assert version_space((e3,)) == ("h00", "h01", "h10", "h11")

    print("MINCURR_EXACT_WITNESS_OK")

## Claim boundary

This witness proves only relative teaching-set minimality under the declared finite concept class and exact consistency-based reconstruction rule.

It does not establish:

- a universal minimal curriculum;
- a universal reasoning basis;
- that high learning progress is unimportant;
- that the target learner of a real neural system behaves like version-space elimination;
- that later behavioural expression proves early-mechanism persistence.
