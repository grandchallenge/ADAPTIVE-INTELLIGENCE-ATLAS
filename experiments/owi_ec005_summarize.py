#!/usr/bin/env python3
"""Descriptive, fail-closed five-seed audit of OWI-EC-005 results.

A green schema/replay audit is not scientific acceptance. A positive claim
requires advantage on matched passive and fixed policies, information
ablations, a held-out intervention and repeated seeds.
"""
import argparse
import json
import math
import statistics
from pathlib import Path


def summarize(folder, seeds):
    if len(seeds) < 5 or len(set(seeds)) != len(seeds):
        raise ValueError("need five distinct seed identities")
    records = [json.loads((folder / f"seed{s}_results.json").read_text())
               for s in seeds]
    for seed, rec in zip(seeds, records):
        if rec["seed"] != seed or rec["counterfactual_training"]:
            raise ValueError("seed/provenance or outcome-only invariant broken")
        for mode in ("active", "passive", "fixed_both"):
            if mode not in rec["results"]:
                raise ValueError(f"missing {mode}: seed {seed}")
            for kind in ("gaussian", "dropout", "signflip", "roll",
                         "persistent", "coupled", "checkpoint", "length13",
                         "parity"):
                data = rec["results"][mode][kind]
                if not (math.isfinite(data["objective"])
                        and math.isfinite(data["elapsed_seconds_batch"])
                        and data["executed_dense_macs"]["total"] >= 0):
                    raise ValueError(f"invalid datum {seed} {mode} {kind}")
        for kind in ("zero_probe", "shuffle_probe"):
            if kind not in rec["results"]["active"]:
                raise ValueError(f"missing {kind} ablation: seed {seed}")

    def measure(condition, comparator, kind):
        diffs = [r["results"][comparator][kind]["objective"] -
                 r["results"][condition][kind]["objective"] for r in records]
        m = statistics.mean(diffs)
        sd = statistics.stdev(diffs)
        # t critical 95% for five seeds; descriptive only.
        critical = 2.776 if len(diffs) == 5 else None
        interval = None if critical is None else [
            m - critical * sd / math.sqrt(len(diffs)),
            m + critical * sd / math.sqrt(len(diffs))]
        return {"paired_improvement": m, "per_seed": diffs, "positive_seeds":
                sum(d > 0 for d in diffs), "descriptive_95_interval": interval}

    kinds = ("gaussian", "dropout", "signflip", "roll", "small_noise",
             "persistent", "coupled", "checkpoint", "length13", "parity")
    comparisons = {kind: {
        "versus_passive": measure("active", "passive", kind),
        "versus_fixed_both": measure("active", "fixed_both", kind)}
        for kind in kinds}
    ablations = {name: [r["results"]["active"][name]["objective"] -
                         r["results"]["active"]["gaussian"]["objective"]
                         for r in records]
                 for name in ("zero_probe", "shuffle_probe")}
    all_seed_gaussian = all(
        comparisons["gaussian"]["versus_passive"]["per_seed"][i] > 0 and
        comparisons["gaussian"]["versus_fixed_both"]["per_seed"][i] > 0
        for i in range(len(seeds)))
    heldout = [k for k in ("dropout", "signflip", "roll", "small_noise",
                           "persistent", "coupled", "checkpoint")
               if all(comparisons[k][vs]["positive_seeds"] == len(seeds)
                      for vs in ("versus_passive", "versus_fixed_both"))]
    survives_ablation = (
        all(v > 0 for v in ablations["zero_probe"]) and
        all(v > 0 for v in ablations["shuffle_probe"]))
    status = ("BOUNDED_POSITIVE_CANDIDATE_REQUIRES_REVIEW"
              if all_seed_gaussian and heldout and survives_ablation
              else "NEGATIVE_OR_INSUFFICIENT_EVIDENCE")
    return {
        "research": "OWI-EC-005", "seeds": seeds,
        "disposition": status,
        "acceptance_conditions": {
            "in_distribution_all_seed_advantage": all_seed_gaussian,
            "heldout_mechanisms_all_seed_advantage": heldout,
            "probe_information_ablation_all_seed_degradation": survives_ablation,
            "measured_hardware_energy_or_true_flops": False,
            "new_task_semantics_validated": False,
        },
        "comparisons": comparisons, "ablations_vs_normal": ablations,
        "mean_gaussian": {
            mode: statistics.mean(
                r["results"][mode]["gaussian"]["objective"] for r in records)
            for mode in ("active", "passive", "fixed_both")},
        "mean_actual_conditional_replays": {
            mode: statistics.mean(
                r["results"][mode]["gaussian"]["replay_per_example"]
                for r in records) for mode in ("active", "passive", "fixed_both")},
        "mean_executed_dense_macs_per_example": {
            mode: statistics.mean(
                r["results"][mode]["gaussian"]["executed_dense_macs"]["total"] /
                r["results"][mode]["gaussian"]["n_examples"] for r in records)
            for mode in ("active", "passive", "fixed_both")},
        "ec004_archived_comparison_not_matched": {
            "full_info_active_summary": 0.053109,
            "full_info_passive_summary": 0.064680,
            "full_info_fixed_both": 0.0717,
            "ec004_onpolicy_failure": 0.077686,
            "warning": "Archival numbers, different execution and evaluation; "
                       "not a matched EC005 comparison"},
        "limitations": [
            "frozen task GRU: no end-to-end co-learning inference",
            "parity is a zero-shot task-semantic shift, not adapted-task learning",
            "dense-MAC estimates are execution counted, not profiled hardware FLOPs",
            "batch CPU latency includes Python selection/index dispatch",
            "RSS is high-water process memory, not isolated per-intervention allocation",
            "no off-policy estimator: current behavior-policy likelihood is optimized",
            "no scientific promotion from green CI without review",
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", default="build/owi_ec005")
    ap.add_argument("--seeds", default="1,2,3,4,5")
    ap.add_argument("--output", default="build/owi_ec005/summary.json")
    args = ap.parse_args()
    folder = Path(args.folder)
    result = summarize(folder, [int(s) for s in args.seeds.split(",")])
    dest = Path(args.output)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"disposition": result["disposition"],
                      "mean_gaussian": result["mean_gaussian"],
                      "heldout": result["acceptance_conditions"][
                          "heldout_mechanisms_all_seed_advantage"]}, indent=2))


if __name__ == "__main__":
    main()
