#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
VERSION="0.1.0-rc.1"
export SOURCE_DATE_EPOCH=1791331200
export TZ=UTC
PANDOC="$(python3 -c 'import pypandoc; print(pypandoc.get_pandoc_path())')"
python3 tools/assemble_manuscript.py --output /tmp/atlas-rc.md --manifest /tmp/atlas-rc-manifest.json --check
python3 tools/release_prepare_markdown.py
"$PANDOC" /tmp/atlas-rc-release-clean.md --from=markdown+tex_math_dollars+tex_math_single_backslash+citations+raw_attribute --to=latex --standalone --top-level-division=chapter --toc --number-sections --citeproc --bibliography=sources/bibliography.bib --resource-path=. -V documentclass=book -H tools/release_header.tex -o "manuscript/latex/atlas-v${VERSION}.tex"
cp "manuscript/latex/atlas-v${VERSION}.tex" /tmp/atlas-rc-canonical.tex
rm -rf /tmp/atlas-pdf-det
mkdir -p /tmp/atlas-pdf-det "build/release-candidate/v${VERSION}"
for pass in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/atlas-pdf-det /tmp/atlas-rc-canonical.tex > "/tmp/atlas-det${pass}.log" 2>&1
done
cp /tmp/atlas-pdf-det/atlas-rc-canonical.pdf "build/release-candidate/v${VERSION}/atlas-v${VERSION}.pdf"
python3 tools/release_tex_for_html.py
"$PANDOC" /tmp/atlas-rc-html-input.tex --from=latex --to=html5 --standalone --toc --number-sections --mathjax --embed-resources --resource-path=. -o /tmp/atlas-rc.html
python3 tools/release_add_alt.py
cp /tmp/atlas-rc.html "build/release-candidate/v${VERSION}/atlas-v${VERSION}.html"
python3 tools/write_release_manifest.py
python3 tools/check_release_candidate.py
echo "OK: built release candidate v${VERSION}"
