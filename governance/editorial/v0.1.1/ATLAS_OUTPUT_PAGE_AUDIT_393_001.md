# Atlas source-less output-active PDF warning audit

Status: DIAGNOSTIC ONLY — no print or chapter acceptance.

Exact head: 225b9fc6200d3e45d11af9ad9d4115f39d9bd003

PDF SHA256: 77324fa8d269ad82f85ae11368515db757ddc4e97eff1ababecde0ba780b05d7

Log SHA256: 0e5455ceeb41865641ee91909d15bb7be73fa95030467d8852ae64e4a6d996f2

PDF pages: 1426. TeX output-active warnings: 172. Shipout tokens: 1330. Worst width: 108.22955pt.

## Warning candidate-page neighborhoods

| Rank | Excess width pt | Before shipout | After shipout | Candidate pages |
|---:|---:|---:|---:|---|
| 1 | 108.22955 | 1002 | 1003 | 1002,1003 |
| 2 | 107.39584 | 1178 | 1179 | 1178,1179 |
| 3 | 100.79817 | 384 | 385 | 384,385 |
| 4 | 87.95473 | 1218 | 1219 | 1218,1219 |
| 5 | 86.70445 | 180 | 181 | 180,181 |
| 6 | 83.64711 | 342 | 343 | 342,343 |
| 7 | 76.42503 | 564 | 565 | 564,565 |
| 8 | 71.21547 | 1066 | 1067 | 1066,1067 |
| 9 | 70.38564 | 818 | 819 | 818,819 |
| 10 | 65.03793 | 1102 | 1103 | 1102,1103 |
| 11 | 62.53775 | 574 | 575 | 574,575 |
| 12 | 61.15096 | 1073 | 1074 | 1073,1074 |
| 13 | 61.15096 | 1075 | 1076 | 1075,1076 |
| 14 | 61.15096 | 1077 | 1078 | 1077,1078 |
| 15 | 61.15096 | 1079 | 1081 | 1079,1081 |
| 16 | 60.45415 | 1174 | 1175 | 1174,1175 |
| 17 | 58.57732 | 518 | 519 | 518,519 |
| 18 | 57.53809 | 894 | 895 | 894,895 |
| 19 | 54.62184 | 22 | 23 | 22,23 |
| 20 | 54.06592 | 1016 | 1017 | 1016,1017 |
| 21 | 53.92740 | 998 | 999 | 998,999 |
| 22 | 53.71960 | 162 | 163 | 162,163 |
| 23 | 53.37207 | 1012 | 1013 | 1012,1013 |
| 24 | 49.55196 | 120 | 121 | 120,121 |
| 25 | 49.20396 | 710 | 711 | 710,711 |

The before/after shipout pair is not a proven individual page or TeX source line. This source-less attribution remains uncertain.

## Independent PDF geometry

Text spans outside the PDF page box: 0 (pages: 0). Spans within 18pt of a physical edge: 0 (not necessarily clipped). Pages with extracted image blocks: 18.

Eight or fewer candidate pages were rasterized as samples for a human/critical agent reader; this does not establish all-page visual quality.

The complete  warning inventory and span examples are in the companion JSON. Remaining: inspect actual renders and caption/figure layout, diagnose print margins, mathematical fidelity, reading order and chapter-level quality. No inference of complete acceptance or public publication is warranted.


## Separate critical-role inspection of exact page renderings

The [sample-page image artifact from run 37915527684](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/37915527684) contains eight real rasterizations of this exact PDF, SHA-256 `77324fa8d269ad82f85ae11368515db757ddc4e97eff1ababecde0ba780b05d7`. During a distinct visual inspection, **PDF physical page 1178** (printed page **1110**, Chapter 67, *Compression as Discovery and Intelligence Probe*) exhibits an actual running-head collision: the page number **1110** touches the beginning of **CHAPTER 67**, instead of occupying a separate reserved header region. Physical page 1179 shows a short section running head and separately positioned page number, corroborating that the problem depends on header width. Physical page 1002 and physical page 1218 were sampled and did not show that specific collision.

This directly **refutes** an overly broad inference from the preceding geometry result. The value **0 spans outside the page media box** does not establish that the page is correctly composed: two text objects can visibly collide entirely *within* the page. The `\output` warnings therefore include a genuine **print-layout concern**, at least in the observed sample; none of the unexamined pages is certified as good. An exact-source running-head/page-number separation and truncation or short-mark repair is now the smallest warranted successor, followed by three-pass PDF and visual samples of both long and short header pages.

**Disposition:** bounded diagnosis COMPLETE; global page-head typography and 172 output-routine warnings NOT yet resolved. Do not close the remaining physical print-quality frontier on this diagnostic alone.
