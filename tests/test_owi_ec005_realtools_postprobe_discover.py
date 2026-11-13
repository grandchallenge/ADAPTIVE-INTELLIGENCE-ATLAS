#!/usr/bin/env python3
"""Evidence-boundary tests for public-only natural task variant selection."""
import json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_postprobe_discover import survey
from owi_ec005_realtools_split import partition
from owi_ec005_realtools_intake import DatasetBoundaryError
from test_owi_ec005_realtools_family_survey import fixture

class NaturalVariantTest(unittest.TestCase):
    def test_never_export_hidden_source_or_heldout_family_prompts(self):
        rows=fixture()
        part=partition(rows,seed=4611)
        anchors=[v["row_index"] for v in part["partitions"]["train"]][:2]
        result=survey(rows,anchors=tuple(anchors),limit=1)
        self.assertEqual({r["index"] for r in result},set(anchors))
        exported=json.dumps(result)
        for forbidden in ("SECRET_CHECK_","SECRET_SKILL_","DO_NOT_SHOW_",
                          "class Fixture"):
            self.assertNotIn(forbidden,exported)
        test_index=part["partitions"]["test"][0]["row_index"]
        with self.assertRaises(DatasetBoundaryError):
            survey(rows,anchors=(test_index,),limit=1)

    def test_invalid_scope_fails(self):
        rows=fixture()
        with self.assertRaises(DatasetBoundaryError):
            survey(rows,anchors=(0,0),limit=1)
        with self.assertRaises(DatasetBoundaryError):
            survey(rows,anchors=(0,),limit=99)

if __name__=="__main__":
    unittest.main()
