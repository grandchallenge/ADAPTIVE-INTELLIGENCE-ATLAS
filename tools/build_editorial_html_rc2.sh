#!/usr/bin/env bash
# Corrected-edition HTML candidate only. Does not publish or modify v0.1.0.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
OUT="${1:-$ROOT/build/editorial-candidate/v0.1.1}"
mkdir -p "$OUT"
PANDOC="$(python3 -c 'import pypandoc; print(pypandoc.get_pandoc_path())')"
python3 tools/build_editorial_candidate_rc2.py --check
python3 tools/release_tex_for_html.py --output "$OUT/atlas-rc2-html-input.tex"
"$PANDOC" "$OUT/atlas-rc2-html-input.tex" --from=latex --to=html5 --standalone --toc --number-sections --mathjax --embed-resources --resource-path=. -o "$OUT/atlas-v0.1.1.html"
python3 tools/editorial_export_figure_alts.py --html "$OUT/atlas-v0.1.1.html" --write
python3 tools/editorial_export_figure_alts.py --html "$OUT/atlas-v0.1.1.html" --verify
sha256sum "$OUT/atlas-v0.1.1.html"
