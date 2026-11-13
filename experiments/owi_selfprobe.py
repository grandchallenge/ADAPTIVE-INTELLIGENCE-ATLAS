#!/usr/bin/env python3
"""Finite, randomized, action-conditional witness for endogenous epistemic control.

Pure Python standard library; not a demonstration of neural sapience.
"""
import argparse
import json
import math
import random
from collections import defaultdict
from statistics import mean

ACTIONS = ('none', 'retrieve', 'recompute')
STATES = ('evidence', 'compute')
PROBE_COST = 0.09
REPAIR_COST = 0.03
P_PROBE_CORRECT = 0.95


def symptom(z, rng, flipped=False):
    u = rng.random()
    if u < 0.20:
        return '?'
    correct = z if u < 0.90 else STATES[1 - STATES.index(z)]
    return STATES[1 - STATES.index(correct)] if flipped else correct


def probe(z, rng):
    return z if rng.random() < P_PROBE_CORRECT else STATES[1 - STATES.index(z)]


def loss_probability(z, action):
    return 0.1 if (z == 'evidence' and action == 'retrieve') or (z == 'compute' and action == 'recompute') else 0.8


def action_cost(action):
    return REPAIR_COST if action != 'none' else 0.0


def train(n, rng):
    totals = defaultdict(lambda: [0.0, 0])
    probes = defaultdict(int)
    for _ in range(n):
        z = STATES[rng.randrange(2)]
        s = symptom(z, rng)
        inspected = rng.random() < 0.5
        p = probe(z, rng) if inspected else '-'
        a = ACTIONS[rng.randrange(3)]  # intervention randomized *after* traces
        y = float(rng.random() < loss_probability(z, a))
        record = totals[(s, p, a)]
        record[0] += y
        record[1] += 1
        if inspected:
            probes[(s, p)] += 1
    return totals, probes


def qhat(totals, s, p, action):
    x, n = totals[(s, p, action)]
    if not n:
        raise ValueError('No support for intervention at state ' + str((s, p, action)))
    return x / n + action_cost(action)


def best(totals, s, p):
    return min(ACTIONS, key=lambda a: (qhat(totals, s, p, a), ACTIONS.index(a)))


def probe_preference(totals, probes, s):
    baseline = qhat(totals, s, '-', best(totals, s, '-'))
    n = sum(probes[(s, p)] for p in STATES)
    if not n:
        raise ValueError('No randomized probe samples for ' + s)
    with_probe = PROBE_COST + sum(
        probes[(s, p)] / n * qhat(totals, s, p, best(totals, s, p))
        for p in STATES
    )
    return with_probe < baseline, baseline - with_probe


def oracle_mean(s, p, a):
    # For transparent scoring only. These hidden-state posteriors are not used by learner.
    prior = {'evidence': 0.875, 'compute': 0.125, '?': 0.5}[s]
    if p != '-':
        w_e = P_PROBE_CORRECT if p == 'evidence' else 1 - P_PROBE_CORRECT
        w_c = 1 - P_PROBE_CORRECT if p == 'evidence' else P_PROBE_CORRECT
        prior = prior * w_e / (prior * w_e + (1 - prior) * w_c)
    return (prior * loss_probability('evidence', a)
            + (1 - prior) * loss_probability('compute', a)
            + action_cost(a))


def sup_error(totals):
    return max(abs(qhat(totals, s, p, a) - oracle_mean(s, p, a))
               for s in (*STATES, '?') for p in ('-', *STATES) for a in ACTIONS)


def sample_eval(totals, probes, n, rng, flipped=False):
    outcomes = defaultdict(float)
    decisions = defaultdict(int)
    for _ in range(n):
        z = STATES[rng.randrange(2)]
        s = symptom(z, rng, flipped)
        baseline_s = symptom(STATES[rng.randrange(2)], rng)  # independent, same-marginal diagnostic
        y = rng.random()  # paired loss-noise across all policies in this trial
        for policy in ('none', 'fixed', 'passive', 'active', 'shuffled'):
            do_probe = False
            if policy == 'none':
                a = 'none'
            elif policy == 'fixed':
                a = 'retrieve'
            elif policy == 'shuffled':
                a = best(totals, baseline_s, '-')
            elif policy == 'passive':
                a = best(totals, s, '-')
            else:
                do_probe, _ = probe_preference(totals, probes, s)
                p = probe(z, rng) if do_probe else '-'
                a = best(totals, s, p)
                decisions['probed_' + s] += int(do_probe)
                decisions['count_' + s] += 1
            outcomes[policy] += float(y < loss_probability(z, a)) + action_cost(a) + (PROBE_COST if do_probe else 0)
    return {k: v / n for k, v in outcomes.items()}, dict(decisions)


def run(seed, train_size, test_size):
    totals, probes = train(train_size, random.Random(seed))
    risks, decisions = sample_eval(totals, probes, test_size, random.Random(seed + 100000))
    shifted, _ = sample_eval(totals, probes, test_size, random.Random(seed + 200000), flipped=True)
    cells = [totals[(s, p, a)][1] for s in (*STATES, '?') for p in ('-', *STATES) for a in ACTIONS]
    n_min = min(cells)
    # A 95% union bound: 2.5% each for response means and probe outcome laws.
    min_probe = min(sum(probes[(s, p)] for p in STATES) for s in (*STATES, '?'))
    epsilon = math.sqrt(math.log(2 * len(cells) / 0.025) / (2 * n_min))
    kappa = math.sqrt(math.log(2 * 3 / 0.025) / (2 * min_probe))
    regret_bound = 2 * (epsilon + 1.03 * kappa)
    return {'seed': seed, 'train': train_size, 'eval': test_size, 'risk': risks,
            'shifted_passive_risk': shifted['passive'], 'sup_q_error': sup_error(totals),
            'hoeffding_95pct_epsilon': epsilon, 'probe_tv_95pct_kappa': kappa,
            'greedy_95pct_regret_bound': regret_bound,
            'guaranteed_gain_vs_fixed_if_positive': 0.255 - regret_bound,
            'min_cell': n_min, 'min_probe': min_probe,
            'probe_by_signal': {s: probe_preference(totals, probes, s)[0] for s in (*STATES, '?')},
            'active_probe_counts': decisions}


def self_test():
    assert abs(oracle_mean('evidence', '-', 'retrieve') - 0.2175) < 1e-12
    assert abs(oracle_mean('?', '-', 'retrieve') - 0.48) < 1e-12
    assert abs(0.8 * 0.2175 + 0.2 * 0.48 - 0.27) < 1e-12
    assert abs(0.8 * 0.2175 + 0.2 * (0.95 * 0.1 + 0.05 * 0.8 + 0.03 + PROBE_COST) - 0.225) < 1e-12
    r = run(seed=19, train_size=40000, test_size=70000)
    assert r['probe_by_signal'] == {'evidence': False, 'compute': False, '?': True}
    assert abs(r['risk']['active'] - 0.225) < 0.02, r
    assert r['risk']['active'] < r['risk']['passive'] < r['risk']['fixed']
    assert r['risk']['shuffled'] > r['risk']['active']
    assert r['shifted_passive_risk'] > r['risk']['fixed']
    print('SELF-TEST PASS: oracle, learned probe policy, controls, and held-out shift')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seeds', default='1,2,3,4,5', help='comma-separated independent seeds')
    ap.add_argument('--train', type=int, default=40000)
    ap.add_argument('--eval', type=int, default=70000)
    ap.add_argument('--output', help='optional JSON output filepath')
    ap.add_argument('--wandb-project', help='optional explicit W&B logging; requires wandb installed')
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.train < 200 or args.eval < 200:
        ap.error('--train and --eval must be >= 200')
    seeds = [int(s.strip()) for s in args.seeds.split(',') if s.strip()]
    if not seeds:
        ap.error('At least one seed required')
    wandb = None
    if args.wandb_project:
        try:
            import wandb
        except ImportError as e:
            raise SystemExit('Install wandb to enable --wandb-project') from e
    results = []
    for seed in seeds:
        item = run(seed, args.train, args.eval)
        results.append(item)
        if wandb:
            wb = wandb.init(project=args.wandb_project, config={'seed': seed, 'train': args.train, 'eval': args.eval}, reinit=True)
            wandb.log({**{'risk/' + k: v for k, v in item['risk'].items()}, 'model/sup_q_error': item['sup_q_error']})
            wb.finish()
    summary = {'risk_mean': {a: mean(r['risk'][a] for r in results) for a in ('none', 'fixed', 'passive', 'active', 'shuffled')},
               'shifted_passive_mean': mean(r['shifted_passive_risk'] for r in results),
               'sup_q_error_mean': mean(r['sup_q_error'] for r in results),
               'analytic_risk': {'fixed': 0.48, 'passive': 0.27, 'active': 0.225},
               'claim_boundary': 'synthetic finite partially observable causal-control witness; not a neural-emergence result'}
    result = {'summary': summary, 'runs': results}
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, sort_keys=True)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
