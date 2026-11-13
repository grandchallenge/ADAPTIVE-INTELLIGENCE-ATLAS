#!/usr/bin/env python3
"""Reusable GRU and cognitive probe/repair mechanics for OWI-EC-004.

Core mechanics are shared by full-information and on-policy task-cost tests.
Probe replays a 3-step recurrent suffix from a trusted checkpoint, exposes
an observed-vs-replayed discrepancy, and caches the replay for correction.
"""
import argparse
import json
import time
from dataclasses import dataclass,asdict
from statistics import mean
import torch
from torch import nn
from torch.nn import functional as F
from torch.distributions import Categorical

@dataclass
class Cfg:
    h:int=12
    length:int=9
    suffix:int=3
    batch:int=192
    pretrain:int=380
    joint:int=1250
    eval_n:int=6000
    p_fault:float=0.8
    sigma:float=2.5
    lambda_compute:float=0.035
    policy_overhead:float=0.005
    entropy:float=0.0006

class Core(nn.Module):
    def __init__(self,h):
        super().__init__()
        self.branches=nn.ModuleList([nn.GRU(1,h,batch_first=True) for _ in range(2)])
        self.heads=nn.ModuleList([nn.Linear(h,1) for _ in range(2)])
    def forward_clean(self,x):
        outputs=[]
        for c in range(2):
            o,_=self.branches[c](x[:,:,c:c+1]);outputs.append(self.heads[c](o[:,-1]).squeeze(1))
        return torch.stack(outputs,1)

class Actor(nn.Module):
    def __init__(self, h, active=True, feature='rich'):
        super().__init__()
        self.active=active
        self.feature=feature
        self.fdim=4 if feature=='summary' else 2*h+6
        self.first=nn.Sequential(nn.Linear(self.fdim,20),nn.Tanh(),nn.Linear(20,3)) if active else None
        self.second=nn.Sequential(nn.Linear(self.fdim+(2 if active else 0),20),nn.Tanh(),nn.Linear(20,4))
    def features(self,hidden,checkpoint,logits):
        parts=[]
        for c in range(2):
            parts += [torch.tanh(logits[:,c:c+1]/4.0),hidden[c].norm(dim=1,keepdim=True)/float(hidden[c].shape[1])**0.5]
        if self.feature=='rich':
            for c in range(2):
                parts += [hidden[c],(hidden[c]-checkpoint[c]).norm(dim=1,keepdim=True)/float(hidden[c].shape[1])**0.5]
        return torch.cat(parts,dim=1)


def sample_data(n,cfg,rng):
    x=(2*torch.randint(0,2,(n,cfg.length,2),generator=rng)-1).float()
    y=(x.sum(dim=1)>0).float()
    return x,y


def corrupted(core,x,cfg,rng,kind='gaussian',p_fault=None):
    """Return actual corrupted rollout, checkpoint, trusted replays, evaluator-only labels."""
    n=len(x); prefix=cfg.length-cfg.suffix
    p=cfg.p_fault if p_fault is None else p_fault
    fault=torch.multinomial(torch.tensor([1-p,p/2,p/2]),n,replacement=True,generator=rng)
    corrupted_states=[]; clean_states=[]; checkpoints=[]
    for c,gru in enumerate(core.branches):
        _,h0=gru(x[:,:prefix,c:c+1]); check=h0.squeeze(0)
        _,hclean=gru(x[:,prefix:,c:c+1],h0)
        _,hone=gru(x[:,prefix:prefix+1,c:c+1],h0)
        perturb=(fault==c+1).unsqueeze(1)
        w=hone.squeeze(0)
        if kind=='gaussian':
            affected=w+cfg.sigma*torch.randn(w.shape,generator=rng)
        elif kind=='dropout':
            affected=w*(torch.rand(w.shape,generator=rng)>0.85).float()
        elif kind=='signflip':
            affected=-w
        elif kind=='roll':
            affected=w.roll(shifts=cfg.h//2,dims=1)
        elif kind=='small_noise':
            affected=w+0.6*torch.randn(w.shape,generator=rng)
        else: raise ValueError(kind)
        w=torch.where(perturb,affected,w)
        _,hbad=gru(x[:,prefix+1:,c:c+1],w.unsqueeze(0))
        checkpoints.append(check)
        corrupted_states.append(hbad.squeeze(0))
        clean_states.append(hclean.squeeze(0))
    return fault, corrupted_states,clean_states,checkpoints


def plan(core,actor,x,cfg,rng,kind='gaussian',training=True,signal_mode='normal',force_uniform_probe=False):
    n=len(x); fault,bad,clean,checkpoint=corrupted(core,x,cfg,rng,kind)
    raw=torch.stack([core.heads[c](bad[c]).squeeze(1) for c in range(2)],dim=1)
    cleaned=torch.stack([core.heads[c](clean[c]).squeeze(1) for c in range(2)],dim=1)
    z=actor.features(bad,checkpoint,raw)
    if signal_mode=='shuffle':
        z=z[torch.randperm(n,generator=rng)]
    if actor.active:
        p_logits=actor.first(z)
        if training:
            d=Categorical(logits=p_logits)
            if force_uniform_probe:
                p_choice=torch.randint(0,3,(n,),generator=rng)
                logp_probe=torch.zeros(n)
            else:
                p_choice=d.sample()
                logp_probe=d.log_prob(p_choice)
            entropy_probe=d.entropy()
        else:
            p_choice=p_logits.argmax(dim=1);logp_probe=None;entropy_probe=None
        probes=[]
        for c in range(2):
            residual=((clean[c]-bad[c]).pow(2).mean(dim=1,keepdim=True)+1e-8).sqrt()
            probe_value=torch.where((p_choice==c+1).unsqueeze(1),residual,torch.zeros_like(residual))
            if signal_mode=='zero_probe': probe_value=torch.zeros_like(probe_value)
            elif signal_mode=='shuffle': probe_value=probe_value[torch.randperm(n,generator=rng)]
            probes.append(probe_value)
        z=torch.cat((z,*probes),dim=1)
    else:
        p_choice=torch.zeros(n,dtype=torch.long);logp_probe=None;entropy_probe=None
    r_logits=actor.second(z)
    if training:
        d=Categorical(logits=r_logits);r_choice=d.sample();logp_repair=d.log_prob(r_choice);entropy_repair=d.entropy()
    else:
        r_choice=r_logits.argmax(dim=1);logp_repair=None;entropy_repair=None
    final=raw.clone()
    for c in range(2):
        final[:,c]=torch.where((r_choice & (1<<c)).bool(),cleaned[:,c],raw[:,c])
    # Each branch's trusted suffix is computed once if probed and/or repaired.
    # Policy itself is charged separately. These charges are *normalized compute
    # proxies*, not physically measured latency of this batched evaluator.
    spent=(p_choice==1).long()+(p_choice==2).long()
    spent=spent+(((r_choice&1)!=0)&(p_choice!=1)).long()+(((r_choice&2)!=0)&(p_choice!=2)).long()
    cost=cfg.lambda_compute*spent.float()+cfg.policy_overhead
    return dict(logits=final,raw_logits=raw,clean_logits=cleaned,cost=cost,spent=spent,probed=p_choice,
                repaired=r_choice,fault=fault,logp_probe=logp_probe,
                logp_repair=logp_repair,entropy_probe=entropy_probe,entropy_repair=entropy_repair)



def exact_expected_risk(core,actor,x,y,cfg,rng,uniform_probe=False, exploration=0.0, entropy_temp=0.0):
    """Differentiable expectation over all cognitive actions (NO fault labels).

    This is a *full-information training oracle*, not on-policy learning.
    Evaluate task loss under each repair candidate, optimize the policy on
    task loss plus cognitive cost directly. It cannot prove online discovery.
    """
    fault,bad,clean,checkpoint=corrupted(core,x,cfg,rng)
    raw=torch.stack([core.heads[c](bad[c]).squeeze(1) for c in range(2)],dim=1)
    replay=torch.stack([core.heads[c](clean[c]).squeeze(1) for c in range(2)],dim=1)
    losses=[]
    for a in range(4):
        updated=torch.stack([replay[:,c] if (a & (1<<c)) else raw[:,c] for c in range(2)],dim=1)
        losses.append(F.binary_cross_entropy_with_logits(updated,y,reduction='none').mean(dim=1))
    L=torch.stack(losses,dim=1)
    base=actor.features(bad,checkpoint,raw)
    probe_probs=actor.first(base).softmax(dim=1) if actor.active else None
    if probe_probs is not None and exploration:
        probe_probs=probe_probs*(1-exploration)+exploration/3
    values=[]
    for p in (range(3) if actor.active else (0,)):
        if actor.active:
            probe=[]
            for c in range(2):
                gap=((clean[c]-bad[c]).pow(2).mean(dim=1,keepdim=True)+1e-8).sqrt()
                probe.append(gap if p==c+1 else torch.zeros_like(gap))
            obs=torch.cat((base,*probe),dim=1)
        else: obs=base
        response_prob=actor.second(obs).softmax(dim=1)
        if exploration:
            response_prob=response_prob*(1-exploration)+exploration/4
        action_charges=[]
        for a in range(4):
            units=int(p!=0)+int((a&1)!=0 and p!=1)+int((a&2)!=0 and p!=2)
            action_charges.append(cfg.lambda_compute*units+cfg.policy_overhead)
        objective=L+torch.tensor(action_charges).unsqueeze(0)
        val=(response_prob*objective).sum(dim=1)
        if entropy_temp:
            val=val+entropy_temp*(response_prob*response_prob.clamp_min(1e-8).log()).sum(dim=1)
        values.append(val)
    V=torch.stack(values,dim=1)
    out=(V.mean(dim=1) if uniform_probe else (V*probe_probs).sum(dim=1)) if actor.active else V[:,0]
    if actor.active and (not uniform_probe) and entropy_temp:
        out=out+entropy_temp*(probe_probs*probe_probs.clamp_min(1e-8).log()).sum(dim=1)
    return out.mean()



def eval_model(core,actor,seed,cfg,kind,n=None,signal_mode='normal'):
    core.eval();actor.eval()
    rng=torch.Generator().manual_seed(seed+{'gaussian':9101,'dropout':9201,'signflip':9301,'roll':9401,'small_noise':9501}[kind])
    n=n or cfg.eval_n
    with torch.no_grad():
        x,y=sample_data(n,cfg,rng)
        out=plan(core,actor,x,cfg,rng,kind=kind,training=False,signal_mode=signal_mode)
        task=F.binary_cross_entropy_with_logits(out['logits'],y,reduction='none').mean(dim=1)
        error=((out['logits']>0).float()!=y).float().mean(dim=1)
        alt={}
        for a in range(4):
            z=out['raw_logits'].clone()
            for c in range(2):
                if a & (1<<c): z[:,c]=out['clean_logits'][:,c]
            alt[a]=(F.binary_cross_entropy_with_logits(z,y,reduction='none').mean(dim=1)+cfg.lambda_compute*(int(bool(a&1))+int(bool(a&2))))
        oracle=torch.stack([alt[a] for a in range(4)],dim=1).min(dim=1).values
        return {'objective':round((task+out['cost']).mean().item(),6),
                'none':round(alt[0].mean().item(),6),'fixed_A':round(alt[1].mean().item(),6),
                'fixed_B':round(alt[2].mean().item(),6),'fixed_both':round(alt[3].mean().item(),6),
                'oracle_omniscient':round(oracle.mean().item(),6),'task_bce':round(task.mean().item(),6),'bit_error':round(error.mean().item(),6),
                'compute_charge':round(out['cost'].mean().item(),6),
                'probe_rate':round((out['probed']!=0).float().mean().item(),6),
                'repair_rate':round((out['repaired']!=0).float().mean().item(),6),
                'avg_suffix_replays':round(out['spent'].float().mean().item(),6),
                'false_repair_clean':round((out['repaired'][out['fault']==0]!=0).float().mean().item(),6) if (out['fault']==0).any() else None}

