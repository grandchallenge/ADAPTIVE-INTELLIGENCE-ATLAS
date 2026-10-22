# ATLAS 405, corrected-edition NONNORMAL chapter admission

Decision: ACCEPT NONNORMAL only for chapter-level editorial scope. The
complete 80-row mutable corrected-edition acceptance ledger advances
from 5 to 6. The other 74 chapters remain UNVERIFIED. This decision
does not certify a theorem, PDF/UA access, or public publication.

## Findings closed

(1) Normal matrices and the field of eigenvectors. A real normal
rotation may have no real eigenvectors and requires complex unitary
diagonalization. The edited text no longer implies a real orthogonal
eigenbasis for all real normal matrices. Real symmetric matrices do
admit a real orthogonal eigenbasis.

(2) Parameters and degenerate cases. The real triangular singular
value formula assumes a real a and K>0; the pseudospectral resolvent
convention takes epsilon>0. A^0 and A^1 are treated separately from
the valid n>=2 nilpotent-binomial power formula. The exact rational
unit tests independently replay cases with a=0.

(3) Pseudospectral-boundary derivation. Squaring gives an extraneous
root, r²=epsilon(epsilon-K). At the singular-value boundary,
r²=sigma_max sigma_min >=epsilon² excludes that root when K>0.
The correct circle has radius sqrt(epsilon(epsilon+K)).
An independent critic also obtained this result directly from
sigma_min=(sqrt(K²+4r²)-K)/2, avoiding the squaring step.

The Wolfram witness and the documentary derivation are unchanged;
neither the witness nor source bibliography licenses claims about
the cause of instability in a deployed machine-learning system.

## Authenticated accountable GCL roles

Producer issue #432, run a0432e5cf0f04b2fb2c3d0e91a814e83,
RESULT/1: https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/432#issuecomment-6337852408

Separate GCL critic issue #433,
run a0433e5cf0f04b2fb2c3d0e91a814e85,
RESULT/1: https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/433#issuecomment-6337906653

Both roles are accountable under different actual controller grants, while
using the same authenticated GitHub transport account permitted by GCL
editorial governance. The source head checked by the critic is
8f163c07a095aac6e3e07d1157981745970ae79b.

## Source, rendering and reproducibility

Corrected NONNORMAL chapter Git blob:
c25d2fe874eae5933c55b43919bda3cab8733345.
Unchanged derivation blob:
9bcdc4cf0a9297407d50ea71077a7ecf5fdb3ecc.
Unchanged computational witness blob:
43e53119709db23cea2aca5cf49397a92763c4d2.
All four source-lock entries are cited bibliographic records, not
invented pinned-Git source attestations.

Recomposed TeX SHA256:
29bfa30b565d74849c4598685b46133e16294b4c812b8ead26bcc8c27777c858.
Triple-pass native 1426-page PDF SHA256:
a9710b643e5cc744ecfffde045964bd18f185d8a261f6e38a8114a57f8689f58.
Full HTML SHA256:
e45bb3afcb4d212b5db22441197bf883324e3e2d10bde0d943749d78c36b9ed6.

Nonnormality chapter physical PDF pages 125-136; the figure is on
page 130, 1100 by 418 embedded pixels at 230.4 effective DPI,
source figure SHA256:
98e7228b577c1dea820ee94b8ad71d1da51114068f0d0f0495f861013635c6be.
All 2971 historical LaTeX labels and 18 figures and alt descriptions
are preserved. All twelve NONNORMAL pages pass selectable-text and
edge-margin checks.

The previous five accepted chapter Git blobs remain unchanged.
Current-render revalidation covers THESIS pages 69-76, MAP 77-82,
OBJECTS 83-93, EVIDENCE 95-107 and LINALG 109-123 and corresponding
MathJax HTML chapter anchors. Earlier critic issue receipts and prior
PDF/HTML digests are retained, not replaced or retroactively updated.
The full source-tree identities for manuscript, source locks and figures
are checked against Git HEAD in shallow-checkout CI.

Five fresh source/mathematical tests, seven acceptance-ledger tests and
six historic MAP tests pass locally. This decision is only operationally
admitted after native protected PR validation and a merge into editable
PR #320. Immutable public v0.1.0 and protected main remain untouched.
