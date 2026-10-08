import base64
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("semantic_alt",ROOT/"tools/editorial_export_figure_alts.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class SemanticAltTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.figs=mod.tex_figures(mod.TEX.read_text())
        chunks=[]
        for dg,(ident,_,path) in cls.figs.items():
            img=base64.b64encode((ROOT/path).read_bytes()).decode("ascii")
            chunks.append(f'<figure>\n<img role="img" src="data:image/png;base64,{img}" alt="ordinary caption" />\n<figcaption>ordinary caption</figcaption></figure>')
        cls.html="\n".join(chunks)

    def test_complete_semantic_coverage_and_image_binding(self):
        out=mod.rewrite_document(self.html,self.figs)
        self.assertEqual(out.count("alt="),18)
        self.assertNotIn('alt="ordinary caption"',out)
        mod.rewrite_document(out,self.figs,verify=True)

    def test_missing_image_is_rejected(self):
        with self.assertRaises(ValueError):
            mod.rewrite_document(self.html.split("</figure>",1)[1],self.figs)

    def test_duplicate_image_is_rejected(self):
        with self.assertRaises(ValueError):
            mod.rewrite_document(self.html+self.html,self.figs)

    def test_caption_is_not_accepted_as_semantic_alt(self):
        with self.assertRaises(ValueError):
            mod.rewrite_document(self.html,self.figs,verify=True)

    def test_source_figures_are_distinct_and_mathematically_specific(self):
        self.assertEqual(len(self.figs),18)
        self.assertEqual(len({v[0] for v in self.figs.values()}),18)
        self.assertTrue(all(len(v[1])>=65 for v in self.figs.values()))
        for word in ["0.1887", "183/100", "2-norm"]:
            self.assertTrue(any(word in v[1] for v in self.figs.values()))

if __name__=="__main__":
    unittest.main()
