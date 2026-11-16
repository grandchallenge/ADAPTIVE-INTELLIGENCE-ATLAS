#!/usr/bin/env python3
"""OWI-EC-005V: exact original TRAIN hotel row236 PUBLIC task/schema preflight.

No original class executes here; no source-private initial state, verifier,
DEV/TEST prompt or tool response is inspected, exported or logged. All original
159MB raw source bytes are locked before train partition/source selection.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
from owi_ec005_realtools_family_survey import audit_source
from owi_ec005_realtools_intake import public_view, canonical
from owi_ec005_realtools_split import partition

ROW=236
EXPECT_CORPUS="3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a"
EXPECT_FAMILY="fd0d8974e2af1954f04775ff85b3bc002a4c6bc14b35c5883a28555d8adaa4df"
EXPECT_PUBLIC_PROMPT="25d2be96389844fe56ff7490182876380bc2b0e153ee3da53598dc265b24708d"
LOCK=Path("governance/research/OWI_EC005_TOOL_SOURCE_LOCK.json")
def preflight():
    lock=json.loads(LOCK.read_text())
    if lock.get("sha256")!=EXPECT_CORPUS:
        raise ValueError("original 2550 task source lock mismatch")
    rows=audit_source(lock)
    split=partition(rows,seed=4611)
    train={x["row_index"]:x for x in split["partitions"]["train"]}
    if ROW not in train or train[ROW]["environment_id_sha256"]!=EXPECT_FAMILY or train[ROW]["public_prompt_sha256"]!=EXPECT_PUBLIC_PROMPT:
        raise ValueError("original source TRAIN row/public task/family identity mismatch")
    task=public_view(rows[ROW])
    if task.keys()!={"messages"}:raise ValueError("source private leaked into public")
    env=rows[ROW]["extra_info"]["environment"]
    methods=[]
    for tool in env["tools"]:
        f=tool.get("function",{})
        if not isinstance(f.get("name"),str):raise ValueError("original public schema malformed")
        if f["name"] in {"check_room_availability_over_date_range","get_booking_info",
                         "get_room_info","list_available_rooms","list_bookings_by_guest",
                         "list_active_bookings_for_room","get_room_amenities",
                         "list_available_rooms_by_type","list_all_room_types"}:
            methods.append({"name":f["name"],
                            "parameters":f.get("parameters"),
                            "description":str(f.get("description",""))[:400]})
    return {"contract":"OWI-EC005V-ORIGINAL-TRAIN-HOTEL-ROW236-PUBLIC-PREFLIGHT/1",
            "corpus_sha256":EXPECT_CORPUS,"original_train_row":ROW,
            "original_train_family_sha256":EXPECT_FAMILY,
            "original_public_prompt_sha256":EXPECT_PUBLIC_PROMPT,
            "user_instructions":[x["content"] for x in task["messages"] if x["role"]=="user"],
            "relevant_original_declared_PUBLIC_tools":methods,
            "no_original_source_private_state_or_checker_read_executed":True,
            "source_dev_sealed_test_public_tasks_not_exported":True}
if __name__=="__main__":
    print("OWI_EC005V_ORIGINAL_HOTEL_PUBLIC_PREFLIGHT",json.dumps(preflight(),sort_keys=True))
