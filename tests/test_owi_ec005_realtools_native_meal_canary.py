#!/usr/bin/env python3
"""Native meal-label source-mutation arm contract tests."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"experiments"))
from owi_ec005_realtools_native_meal_canary import (
    selected_new_label,GOOD,BAD,ARMS
)

class NativeAllergenArms(unittest.TestCase):
    def test_public_correct_and_explicitly_misleading_label_separate(self):
        self.assertEqual(selected_new_label("correct_cashew"),"cashews (cross-contact)")
        self.assertEqual(selected_new_label("incorrect_peanut"),"peanuts")
        self.assertIsNone(selected_new_label("stop"))
        self.assertNotEqual(GOOD,BAD)
        self.assertEqual(set(ARMS),{"stop","correct_cashew","incorrect_peanut"})
    def test_invalid_oracle_arm_rejected(self):
        for arm in ("oracle","native_checker","private_state",None):
            with self.subTest(arm=arm):
                with self.assertRaises(ValueError):
                    selected_new_label(arm)
if __name__=="__main__":
    unittest.main()
