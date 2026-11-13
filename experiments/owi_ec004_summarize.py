#!/usr/bin/env python3
"""Summarize OWI-EC-004 finite-seed evidence and compute-only sensitivity.

This reports descriptive intervals; it is not a prospective significance test.
"""
import argparse
import json
import math
from pathlib import Path
from statistics import mean,stdev

MODES=('active_rich','passive_rich','active_summary','passive_summary')
KINDS=('gaussian','dropout','signflip','roll','small_noise')
T95_4=2.7764451051977987


def interval(xs):
    mu=mean(xs)
    return dict(mean=mu,interval_95pct_student_t=[mu-T95_4*stdev(xs)/math.sqrt(len(xs)),mu+T95_4*stdev(xs)/math.sqrt(len(xs))])


def summarize(folder,seeds,online=True):
    rows={(seed,mode):json.loads((folder/f'seed{seed}_{mode}.json').read_text())
          for seed in seeds for mode in MODES}
    summary={}
    for kind in KINDS:
        summary[kind]={}
        for mode in MODES:
            metrics=[rows[seed,mode]['conditions'][kind] for seed in seeds]
            summary[kind][mode]={k:mean(x[k] for x in metrics) for k in ('objective','none','fixed_both','oracle_omniscient','bit_error','compute_charge','probe_rate','avg_suffix_replays')}
            if mode.startswith('active'):
                summary[kind][mode].update({k:mean(x[k] for x in metrics) for k in ('zero_probe_information_objective','shuffled_all_telemetry_objective')})
    comparisons={}
    for name,act,base in (
        ('summary_active_minus_passive','active_summary','passive_summary'),
        ('rich_active_minus_passive','active_rich','passive_rich')):
        ds=[rows[s,act]['conditions']['gaussian']['objective']-rows[s,base]['conditions']['gaussian']['objective'] for s in seeds]
        comparisons[name]=interval(ds)
    diff=[rows[s,'active_summary']['conditions']['gaussian']['zero_probe_information_objective']-rows[s,'active_summary']['conditions']['gaussian']['objective'] for s in seeds]
    comparisons['summary_probe_information_value']=interval(diff)
    # Matrix-multiply counts, NOT full FLOPs/latency. GRU suffix: 3 timesteps,
    # 3 gates, hidden=12, input=1, plus 12-wide output linear head.
    h=12
    replay_mac=3*3*h*(h+1)+h
    ctrl_mac={'active_rich':1380,'passive_rich':680,'active_summary':340,'passive_summary':160}
    sensitivity={mode:summary['gaussian'][mode]['objective']-0.005+0.035*mac/replay_mac for mode,mac in ctrl_mac.items()}
    result={'seeds':seeds,'n_models':len(seeds)*len(MODES),'models':MODES,'kinds':KINDS,
            'summary':summary,'comparisons':comparisons,
            'mac_sensitivity':{'replay_suffix_mac':replay_mac,'controller_dense_mac':ctrl_mac,'mac_adjusted_objective':sensitivity,
                               'warning':'Sensitivity only; MACs omit nonlinear ops, memory traffic, vectorization and actual wall latency.'},
            'claim_boundary':'Full-information task+compute optimization, not learned from on-policy outcomes alone; probe semantics and trusted checkpoints pre-engineered; no sapience inference.'}
    if online:
        records=[json.loads((folder/f'seed{s}_active_summary_onpolicy.json').read_text()) for s in seeds]
        result['onpolicy']={'mean_objective':mean(r['results']['gaussian']['objective'] for r in records),
                            'mean_fixed_both':mean(r['results']['gaussian']['fixed_both'] for r in records),
                            'runs':[{k:r[k] for k in ('seed','mode','onpolicy_steps')}|
                                    { 'objective':r['results']['gaussian']['objective'],'fixed_both':r['results']['gaussian']['fixed_both']} for r in records]}
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--folder',default='build/owi_ec004')
    p.add_argument('--seeds',default='1,2,3,4,5')
    p.add_argument('--no-onpolicy',action='store_true')
    p.add_argument('--output',default='')
    p.add_argument('--check',action='store_true')
    a=p.parse_args();seeds=[int(x) for x in a.seeds.split(',')]
    if len(seeds)<2: raise SystemExit('Use at least two seeds for descriptive CI')
    result=summarize(Path(a.folder),seeds,online=not a.no_onpolicy)
    if a.check:
        for s in seeds:
            ar=json.loads((Path(a.folder)/f'seed{s}_active_summary.json').read_text())['conditions']['gaussian']
            pas=json.loads((Path(a.folder)/f'seed{s}_passive_summary.json').read_text())['conditions']['gaussian']
            assert ar['objective']<pas['objective'],(s,ar,pas)
            assert ar['objective']<ar['fixed_both']
            assert ar['objective']<ar['zero_probe_information_objective']
            assert ar['objective']<ar['shuffled_all_telemetry_objective']
        print('PASS five-seed active-probe gain and information ablations')
    if a.output:Path(a.output).write_text(json.dumps(result,indent=2))
    print(json.dumps({'seeds':seeds,'gaussian_mean_losses':{k:round(v['objective'],6) for k,v in result['summary']['gaussian'].items()},'paired_differences':result['comparisons'],'onpolicy':result.get('onpolicy'),'MAC_adjusted_objectives':result['mac_sensitivity']['mac_adjusted_objective']},indent=2))

if __name__=='__main__':main()
