#!/usr/bin/env python3
"""Neural sequence-dynamics introspection pilot.

Actual trained GRU states; hidden-state interventions and a learned
randomized-action Q self-estimator. No access to injected fault labels at decision time.
This is a bounded synthetic research witness, not proof of sapience.
"""
import argparse
import json
import time
from dataclasses import asdict, dataclass

import torch
from torch import nn
import torch.nn.functional as F


class Branch(nn.Module):
    def __init__(self, hidden=14):
        super().__init__()
        self.gru = nn.GRU(1, hidden, batch_first=True)
        self.head = nn.Linear(hidden, 1)

    def forward(self, x):
        trace, _ = self.gru(x)
        return trace, self.head(trace[:, -1]).squeeze(1)


class Core(nn.Module):
    def __init__(self, hidden=14):
        super().__init__()
        self.branches = nn.ModuleList([Branch(hidden), Branch(hidden)])

    def forward(self, x):
        traces, logits = [], []
        for c, b in enumerate(self.branches):
            t, y = b(x[:, :, c:c+1])
            traces.append(t)
            logits.append(y)
        return traces, torch.stack(logits, dim=1)


class QModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(input_dim, 64), nn.SiLU(),
                                 nn.Linear(64, 64), nn.SiLU(), nn.Linear(64, 4))

    def forward(self, x):
        return self.net(x)


@dataclass
class Settings:
    hidden: int = 14
    sequence_length: int = 7
    core_steps: int = 330
    q_steps: int = 650
    q_train: int = 22000
    test: int = 7000
    batch: int = 256
    corruption_sigma: float = 2.3
    corruption_probability: float = 0.8
    repair_cost: float = 0.035
    dynamics_probe_cost: float = 0.008
    dynamics_steps: int = 750


def examples(n, cfg, rng):
    x = torch.randint(0, 2, (n, cfg.sequence_length, 2), generator=rng).float() * 2 - 1
    y = (x.sum(dim=1) > 0).float()
    return x, y


def train_core(seed, cfg):
    torch.manual_seed(seed)
    rng = torch.Generator().manual_seed(seed + 300)
    core = Core(cfg.hidden)
    opt = torch.optim.Adam(core.parameters(), lr=0.012)
    core.train()
    for step in range(cfg.core_steps):
        x,y = examples(cfg.batch, cfg, rng)
        _, logits = core(x)
        loss = F.binary_cross_entropy_with_logits(logits, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
    core.eval()
    x,y = examples(4096, cfg, rng)
    with torch.no_grad():
        _, logits = core(x)
        accuracy = ((logits>0).float() == y).float().mean().item()
    return core, accuracy


def corrupt(hidden, kind, rng, sigma):
    if kind == 'gaussian':
        return hidden + sigma * torch.randn(hidden.shape, generator=rng)
    if kind == 'dropout':
        mask = (torch.rand(hidden.shape, generator=rng) >= 0.85).float()
        return hidden * mask
    if kind == 'signflip':
        return -hidden
    if kind == 'permutation':
        return hidden.roll(shifts=hidden.shape[-1]//2, dims=-1)
    raise ValueError('Unknown fault mechanism '+kind)


def train_dynamics(core, seed, cfg):
    # Self-supervised, label-free next-state identification of the *frozen* GRU.
    torch.manual_seed(seed + 700)
    rng = torch.Generator().manual_seed(seed + 970)
    x, _ = examples(14000, cfg, rng)
    with torch.no_grad():
        traces, _ = core(x)
    models = []
    for c in range(2):
        f = torch.cat((traces[c][:, -2, :], x[:, -1, c:c+1]), dim=1)
        target = traces[c][:, -1, :].detach()
        model = nn.Linear(cfg.hidden+1, cfg.hidden)
        opt = torch.optim.Adam(model.parameters(), lr=0.01)
        for _ in range(cfg.dynamics_steps):
            idx = torch.randint(0,len(f),(cfg.batch,),generator=rng)
            loss = F.mse_loss(model(f[idx]), target[idx])
            opt.zero_grad()
            loss.backward()
            opt.step()
        model.eval()
        models.append(model)
    return models


def make_batch(core, n, cfg, rng, fault_kind='gaussian', dynamics=None):
    x, y = examples(n, cfg, rng)
    with torch.no_grad():
        traces, clean_logits = core(x)
        finals = [t[:, -1].clone() for t in traces]
        previous = [t[:, -2].clone() for t in traces]
        injected = torch.multinomial(
            torch.tensor([1.0-cfg.corruption_probability, cfg.corruption_probability/2, cfg.corruption_probability/2]),
            n, replacement=True, generator=rng) # 0 clean, 1 branch0, 2 branch1
        changed = [f.clone() for f in finals]
        for channel in range(2):
            idx = injected == channel + 1
            if idx.any():
                changed[channel][idx] = corrupt(finals[channel][idx], fault_kind, rng, cfg.corruption_sigma)
        corrupt_logits = torch.stack([core.branches[c].head(changed[c]).squeeze(1) for c in range(2)],dim=1)
        # Telemetry is internal, and contains no injected fault ID, target or clean final state.
        state_parts = []
        for c in range(2):
            state_parts += [changed[c], previous[c], corrupt_logits[:, c:c+1],
                            changed[c].norm(dim=1,keepdim=True),
                            (changed[c] - previous[c]).norm(dim=1, keepdim=True)]
        features = torch.cat(state_parts, dim=1)
        if dynamics is not None:
            residuals = []
            for c in range(2):
                f = torch.cat((previous[c], x[:, -1, c:c+1]), dim=1)
                predicted = dynamics[c](f)
                residuals.append(((predicted-changed[c])**2).mean(dim=1,keepdim=True).sqrt())
            features = torch.cat((features, *residuals), dim=1)
        # Physically replay the trusted last recurrent step for each possible repair.
        # These outcomes are available to the evaluator, never to the policy before action.
        repair_logits = []
        for c in range(2):
            replay, _ = core.branches[c].gru(
                x[:, -1:, c:c+1], previous[c].unsqueeze(0).contiguous())
            repaired = core.branches[c].head(replay[:, 0, :]).squeeze(1)
            if not torch.allclose(repaired, clean_logits[:, c], atol=1e-5, rtol=1e-5):
                raise AssertionError('Replayed corrective neural transition does not match the clean core')
            repair_logits.append(repaired)
        # Hidden potential outcomes are evaluated, but only one randomized action
        # outcome is disclosed during Q-model training.
        costs = torch.tensor([0.0, cfg.repair_cost, cfg.repair_cost, 2*cfg.repair_cost])
        outcomes = []
        for action in range(4):
            amended = corrupt_logits.clone()
            for channel in range(2):
                if action & (1 << channel):
                    amended[:, channel] = repair_logits[channel] # actually re-executed trusted GRU transition
            err = ((amended > 0).float() != y).float().mean(dim=1)
            outcomes.append(err + costs[action])
        return features.detach(), torch.stack(outcomes,dim=1).detach(), injected.detach(), corrupt_logits.detach(), clean_logits.detach()


def selected_features(feat, cfg, mode):
    if mode == 'full':
        return feat[:, :2*(2*cfg.hidden+3)]
    if mode == 'logits':
        h = cfg.hidden
        return feat[:, [2*h, 4*h+3]]
    if mode == 'dynamics':
        h = cfg.hidden
        return feat[:, [2*h, 4*h+3, 4*h+6, 4*h+7]]
    raise ValueError('Unknown feature mode: '+mode)


def train_q(core, seed, cfg, mode='full', dynamics=None):
    torch.manual_seed(seed + 99)
    rng = torch.Generator().manual_seed(seed + 1200)
    feat,outcomes,_,_,_ = make_batch(core, cfg.q_train, cfg,rng,dynamics=dynamics)
    feat = selected_features(feat,cfg,mode)
    # Randomized action logging: the learner observes one potential outcome per episode.
    actions = torch.randint(0,4,(len(feat),),generator=rng)
    observed = outcomes[torch.arange(len(feat)),actions]
    q = QModel(feat.shape[1])
    opt = torch.optim.AdamW(q.parameters(),lr=0.002,weight_decay=0.0001)
    q.train()
    for step in range(cfg.q_steps):
        idx = torch.randint(0,len(feat),(cfg.batch,),generator=rng)
        pred = q(feat[idx]).gather(1,actions[idx,None]).squeeze(1)
        loss = F.mse_loss(pred,observed[idx])
        opt.zero_grad()
        loss.backward()
        opt.step()
    q.eval()
    return q


def risk(outcomes, chosen):
    return outcomes.gather(1,chosen[:,None]).mean().item()


def eval_kind(core,q,q_logits,q_dynamics,dynamics,seed,cfg,kind):
    rng = torch.Generator().manual_seed(seed + {'gaussian':4001,'dropout':4501,'signflip':5001,'permutation':5501}[kind])
    with torch.no_grad():
        feat, outcomes, faults, raw, clean = make_batch(core,cfg.test,cfg,rng,kind,dynamics=dynamics)
        scores = q(selected_features(feat,cfg,'full'))
        logits_scores=q_logits(selected_features(feat,cfg,'logits'))
        logits_policy=logits_scores.argmin(1)
        dynamics_scores = q_dynamics(selected_features(feat,cfg,'dynamics'))
        dynamics_policy = dynamics_scores.argmin(1)
        policy = scores.argmin(1)
        oracle = outcomes.argmin(1)
        n = len(feat)
        shuffled = q(selected_features(feat[torch.randperm(n,generator=rng)],cfg,'full')).argmin(1)
        # Task-score-only causal proxy: no hidden states or temporal telemetry; learned Q on two logits not supplied.
        margins = raw.abs()
        proxy = torch.where(margins[:,0]<margins[:,1],torch.ones(n,dtype=torch.long),torch.full((n,),2,dtype=torch.long))
        random_actions = torch.randint(0,4,(n,),generator=rng)
        result={
            'none':risk(outcomes,torch.zeros(n,dtype=torch.long)),
            'fixed_A':risk(outcomes,torch.ones(n,dtype=torch.long)),
            'fixed_B':risk(outcomes,torch.full((n,),2,dtype=torch.long)),
            'repair_both':risk(outcomes,torch.full((n,),3,dtype=torch.long)),
            'oracle':risk(outcomes,oracle),
            'learned':risk(outcomes,policy),
            'logits_only_learned':risk(outcomes,logits_policy),
            'learned_dynamics_probe':risk(outcomes,dynamics_policy)+cfg.dynamics_probe_cost,
            'unnecessary_repair_given_clean':float((policy[faults==0]>0).float().mean()),
            'shuffled':risk(outcomes,shuffled),
            'low_margin_proxy':risk(outcomes,proxy),
            'random_actions':risk(outcomes,random_actions),
            'chosen_repair_rate':float((policy>0).float().mean()),
            'q_mse_full_counterfactual':F.mse_loss(scores,outcomes).item(),
            'causal_action_agreement':(policy==oracle).float().mean().item(),
            'fault_rate':float((faults>0).float().mean()),
            'actual_corrupt_error':float(((raw>0)!=(clean>0)).float().mean()),
        }
        return result


def run(seed,cfg):
    t=time.monotonic()
    core, clean_acc = train_core(seed,cfg)
    q=train_q(core,seed,cfg,mode='full')
    q_logits=train_q(core,seed,cfg,mode='logits')
    dynamics=train_dynamics(core,seed,cfg)
    q_dynamics=train_q(core,seed,cfg,mode='dynamics',dynamics=dynamics)
    data={k:eval_kind(core,q,q_logits,q_dynamics,dynamics,seed,cfg,k) for k in ('gaussian','dropout','signflip','permutation')}
    return {'seed':seed,'core_clean_accuracy':clean_acc,'seconds':round(time.monotonic()-t,2), 'conditions':data}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seeds',default='1,2,3')
    ap.add_argument('--core-steps',type=int,default=330)
    ap.add_argument('--q-steps',type=int,default=650)
    ap.add_argument('--q-train',type=int,default=22000)
    ap.add_argument('--test',type=int,default=7000)
    ap.add_argument('--output',default='')
    ap.add_argument('--wandb-project',default='')
    args=ap.parse_args()
    torch.set_num_threads(1)
    cfg=Settings(core_steps=args.core_steps,q_steps=args.q_steps,q_train=args.q_train,test=args.test)
    seeds=[int(s) for s in args.seeds.split(',')]
    records=[]
    for seed in seeds:
        item=run(seed,cfg)
        records.append(item)
        print('SEED',seed,'clean acc',item['core_clean_accuracy'],'elapsed',item['seconds'],'gaussian',item['conditions']['gaussian'], flush=True)
        if args.wandb_project:
            import wandb
            with wandb.init(project=args.wandb_project,config={**asdict(cfg),'seed':seed}):
                for kind,stats in item['conditions'].items():
                    wandb.log({kind+'/'+k:v for k,v in stats.items()})
    result={'experiment':'neural-OWI-pilot','torch':torch.__version__,'device':'cpu','configuration':asdict(cfg),'runs':records}
    if args.output:
        with open(args.output,'w') as file:
            json.dump(result,file,indent=2)
    print('FINISHED',len(records),'SEEDS',flush=True)


if __name__=='__main__':
    main()
