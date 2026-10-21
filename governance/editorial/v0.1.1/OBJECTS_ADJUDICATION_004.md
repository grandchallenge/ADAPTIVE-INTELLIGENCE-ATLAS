# ATLAS #405: fourth chapter editorial acceptance

Decision: ACCEPT OBJECTS for the corrected-edition editorial scope only.
Current full 80-row ledger is 4/80 ACCEPTED: THESIS, MAP, OBJECTS,
EVIDENCE. All remaining 76 are UNVERIFIED. No formal mathematical
certification, whole-book PDF/UA acceptance, or publication warrant.

## Corrected substantive issue

ER-P1-06: the original 19 numbered short sections broke four formal roles,
three category errors and the downstream reading guide into unrelated
fragments. Current source groups them into six connected main sections
and two intentional subordinate headings. The current reader first learns
role versus shape, then four mathematical roles, then three worked category
errors (same matrix data/operation; numerical step/evolution; tensor
shape/semantic contract), then state-dependent role changes and the four
questions the reader should ask. The source preserves all 23 original
mathematical display expressions byte-identically under comparison against
the previous workbench source revision.

ER-P1-07: mathematical precision on true continuous two-sided real-time
autonomous flows, nonnegative-time semiflows and open-domain local flows
is preserved exactly; composition alone never licenses continuity or
differentiability. Independent exact rational counterchecks include
the normalization of (3,4), reducing magnitude 5 to 1, and the
difference of 1/4 between two Euler steps and one doubled step for a
specific linear scalar right-hand side.

Canonical source and documentary packet Git blobs are respectively
bc39d74e16ba29568aeb777563c3a52d3c0ba3cc and
885eba4f66630fe6620e48a5282ed9759fd8f0ac. Three original pinned
OBJECTS source-lock Git object identities matched. Supporting document
contains four restored MathJax mathematical displays, rendered in a
two-page PDF.

## GCL role provenance

Producer issue #423 returned authenticated RESULT/1
a0423e5cf0f04b2fb2c3d0e91a814e81 on original workbench head
761c277051e71df5345e7bf1852c3356a1c77345, with corrected producer
commit 5295418f21bdf628a42ebe53b2f3dde448ec57d7.

Separate critical role issue #424 returned authenticated RESULT/1
a0424e5cf0f04b2fb2c3d0e91a814e82 on corrected exact producer
commit 5295418f21bdf628a42ebe53b2f3dde448ec57d7.
The critic checked the full source, exact mathematical expressions,
three historic authorities, actual print and MathJax presentation,
formal domain/regularity caveats, and previously accepted chapters.
The same authenticated GitHub identity records independent accountable
role passes; no distinct physical reviewer or GitHub account required
for GCL operational editorial admission.

## Reproduced outputs and earlier chapter preservation

Full-book canonical RC2 TeX SHA256:
054afe9d09e81503f85348e07178d7f523a9c68e00f5368a0dc90dd0b3fc922a.
Actual 1424-page three-pass PDF SHA256:
08da9052e506d545572876dc332684c82d869e67db4f897b3ccb09b46a321a0b.
Full-book MathJax HTML SHA256:
675673c46c719f51385b36a3ef4c34d2643462b32851bdab9a582738337d7f20.
OBJECTS principal reading pages: 83–93. Page 94 contains a running
header but no substantive chapter text; this is a separately
noted P2 print-layout item, not evidence of a missing argument.
All original 2971 LaTeX labels and 18 figures/semantic alt descriptions
survive. There are 5883 unique HTML anchors; legacy OBJECTS, downstream
State and Closing view identifiers remain usable.

Current manuscript source-tree identity is authoritative in the machine
ledger; its stable SHA is dfc2ae27b3d9e97bb36d29949706709ac396c331.
Original source and figure tree IDs remain unchanged.

Previously accepted THESIS source, MAP source, and EVIDENCE source
Git identities remain unchanged. Their actual new-render PDF sections
69–76, 77–82, and 95–107 and the relevant HTML anchors were rechecked.
The three EVIDENCE tables still contain 12, 7 and 7 rows. Their historical
producer/critic receipts and earlier artifact digests are not overwritten;
the complete ledger contains distinct current-render revalidation records
bound to the current critic run #424.

Required tests: six OBJECTS structural/math invariants, six 4/80
acceptance invariants, six historic MAP documentary regressions,
and six THESIS source/scope/anchor tests all pass locally. They are
wired through the protected validate workflow. This decision is
effective in the editable ATLAS workbench only after the protected
correction PR passes CI and merges.

Remaining work: full corrected-edition editorial acceptance of the
other 76 chapters, print/accessibility release checks, and separate
authorized publication of v0.1.1. The public v0.1.0 remains unchanged.
