"""Fail-closed markdown mathematical notation and source identity, ATLAS #405."""
import json,re,subprocess,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'mathematics/derivations/ATLAS-CH-MAP-001-DOCUMENTARY.md'
LEDGER=ROOT/'governance/editorial/v0.1.1/CHAPTER_ACCEPTANCE_EVIDENCE_080.json'

def validate_documentary(s):
    # Portable GitHub/Pandoc math: exactly seven complete standalone $$ display blocks.
    if re.search(r'(?m)^\s*\[\s*$',s) or re.search(r'(?m)^\s*\]\s*$',s):
        raise ValueError('naked square bracket delimiter')
    if any(x.strip()=='$$' for x in s.splitlines()) is False:
        raise ValueError('missing display math')
    if len(re.findall(r'(?m)^\$\$$',s))!=14:
        raise ValueError('math delimiters not paired')
    blocks=re.findall(r'(?ms)^\$\$\n(.*?)^\$\$$',s)
    if len(blocks)!=7 or any(not v.strip() or '\n\n' in v for v in blocks):
        raise ValueError('display math has blank paragraph or malformed delimiter')
    if s.count(r'\not\Rightarrow')!=2 or s.count(r'\neq')!=1:
        raise ValueError('lost nonpromotion/source-authority glyphs')
    if re.search(r'(?m)^otRightarrow$',s) or re.search(r'(?m)^eq$',s):
        raise ValueError('broken mathematical operator')
    if r'\text{presentation}' not in s or r'\text{replay}' not in s or r'\text{citation}' not in s:
        raise ValueError('lost claim-domain context')
    return blocks

class MAPDocumentaryMath(unittest.TestCase):
    def test_actual_doc_notation(self):
        b=validate_documentary(PATH.read_text())
        self.assertEqual(len(b),7)
        self.assertIn(r'\text{citation}', ''.join(b))
    def test_no_raw_brackets(self):
        with self.assertRaises(ValueError):validate_documentary(PATH.read_text().replace('$$','[',1))
    def test_no_broken_nonimplication(self):
        with self.assertRaises(ValueError):validate_documentary(PATH.read_text().replace(r'\not\Rightarrow','otRightarrow',1))
    def test_no_accidental_broken_inequality(self):
        with self.assertRaises(ValueError):validate_documentary(PATH.read_text().replace(r'\neq','eq',1))
    def test_no_internal_paragraph_break(self):
        with self.assertRaises(ValueError):validate_documentary(PATH.read_text().replace(r'\text{replay}', '\\text{replay}\n\n',1))
    def test_canonical_map_not_rewritten(self):
        d=json.loads(LEDGER.read_text())
        row=next(x for x in d['chapters'] if x['chapter_id']=='ATLAS-CH-MAP-001')
        actual=subprocess.check_output(['git','hash-object',str(ROOT/row['source_path'])],text=True).strip()
        self.assertEqual(actual,row['source_blob_sha1'])
        self.assertEqual(actual,'d4073139ad9cad95fa25415a4e74a5ff733b1475')
        self.assertEqual(d['accepted_count'],7)

if __name__=='__main__': unittest.main()
