#!/usr/bin/env python3
"""OWI-EC-005W exact ORIGINAL TRAIN professional-review row710 PUBLIC-only preflight.

Full 159MB source digest and class/env partition checked first; no original
environment class is executed, hidden state/checker/skills are not opened,
and no DEV or sealed TEST public prompts/method declarations are exported.
"""
from __future__ import annotations
import json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_intake import public_view
from owi_ec005_realtools_split import partition

ROW=710
SOURCE="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
FAMILY="a739046b13061603e09af000ceed469840dfecba0068db2e1919454b18394b0c"
PROMPT="97bca760aa53e15f281b71771a6b63a1ba294c1ce3123f9632b114cbf12d6d36"
READ_PREFIX=("get_","list_","check_","find_")
def public_preflight():
    lock=json.loads(Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json").read_text())
    if lock.get("sha256")!=SOURCE:raise ValueError("original full source bytes lock changed")
    rows=audit_source(lock)
    split=partition(rows,seed=4611)
    train={x["row_index"]:x for x in split["partitions"]["train"]}
    if ROW not in train or train[ROW]["environment_id_sha256"]!=FAMILY or train[ROW]["public_prompt_sha256"]!=PROMPT:
        raise ValueError("original professional-review task or connected TRAIN family changed")
    task=public_view(rows[ROW])
    public_tools=[]
    for tool in rows[ROW]["extra_info"]["environment"]["tools"]:
        f=tool.get("function",{}) if isinstance(tool,dict) else {}
        name=f.get("name")
        if not isinstance(name,str):raise ValueError("original tool function name malformed")
        if name.startswith(READ_PREFIX):
            public_tools.append({"name":name,"parameters":f.get("parameters",{}),
                                 "description":str(f.get("description",""))[:480]})
    return {"contract":"OWI-EC005W-ORIGINAL-REVIEW-TRAIN-ROW710-PUBLIC-PREFLIGHT/1",
            "original_complete_source_sha256":SOURCE,
            "original_train_row":ROW,
            "original_train_connected_family_sha256":FAMILY,
            "original_public_user_prompt_sha256":PROMPT,
            "original_public_user_instructions":[m["content"] for m in task["messages"] if m["role"]=="user"],
            "original_declared_public_read_methods":public_tools,
            "no_original_source_code_or_private_checker_executed":True,
            "no_development_or_sealed_test_task_export":True}
if __name__=="__main__":
    print("OWI_EC005W_ORIGINAL_REVIEW_PUBLIC_PREFLIGHT",json.dumps(public_preflight(),sort_keys=True))
