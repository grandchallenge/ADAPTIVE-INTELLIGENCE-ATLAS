#!/usr/bin/env python3
"""Outcome-only on-policy REINFORCE comparator for OWI-EC-004.

Unlike full-info training, only sampled action outcomes update the policy.
Fault identity and unchosen action outcomes are not used as policy targets.
"""
import sys,torch, argparse,json,os,time
from pathlib import Path
from torch import nn
from torch.nn import functional as F
from owi_ec004_core import Core,Actor,Cfg,sample_data,plan,eval_model


def train(seed,mode,steps,folder):
    cfg=Cfg(pretrain=250,joint=0,eval_n=4000)
    state=torch.load(folder/f'seed{seed}_core.pt',weights_only=True)
    core=Core(cfg.h);core.load_state_dict(state['core']);core.eval()
    for p in core.parameters():p.requires_grad_(False)
    feature='summary' if 'summary' in mode else 'rich'
    actor=Actor(cfg.h,mode.startswith('active'),feature)
    torch.manual_seed(seed+722)
    rng=torch.Generator().manual_seed(seed+723)
    optim=torch.optim.Adam(actor.parameters(),lr=0.0015)
    baseline=0.4
    curve=[]
    for t in range(steps):
        x,y=sample_data(cfg.batch,cfg,rng)
        out=plan(core,actor,x,cfg,rng,training=True,
                 force_uniform_probe=(actor.active and t<steps//2))
        task=F.binary_cross_entropy_with_logits(out['logits'],y,reduction='none').mean(1)
        total=task+out['cost']
        lp=out['logp_repair']
        entropy=out['entropy_repair']
        if actor.active:
            lp=lp+out['logp_probe']
            entropy=entropy+out['entropy_probe']
        reg=(0.04 if t<steps//3 else (0.015 if t<2*steps//3 else 0.004))
        # On-policy policy-gradient from sampled task cost, NOT alternate-action costs.
        loss=((total.detach()-baseline)*lp).mean()-reg*entropy.mean()
        optim.zero_grad();loss.backward();nn.utils.clip_grad_norm_(actor.parameters(),3.0);optim.step()
        baseline=0.99*baseline+0.01*total.detach().mean().item()
        if (t+1)%300==0:curve.append({'step':t+1,'sample_loss':round(total.detach().mean().item(),5),'probe_rate':round(float((out['probed']!=0).float().mean()),4),'repair_rate':round(float((out['repaired']!=0).float().mean()),4)})
    return core,actor,curve


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seed',type=int,default=1)
    ap.add_argument('--mode',choices=['active_summary','passive_summary'],default='active_summary')
    ap.add_argument('--steps',type=int,default=1800)
    ap.add_argument('--folder',default='build/owi_ec004')
    a=ap.parse_args();torch.set_num_threads(1)
    folder=Path(a.folder)
    t0=time.monotonic()
    core,actor,curve=train(a.seed,a.mode,a.steps,folder)
    results={k:eval_model(core,actor,a.seed,Cfg(),k) for k in ('gaussian','signflip','roll','small_noise')}
    record={'seed':a.seed,'mode':a.mode,'onpolicy_steps':a.steps,'training':'on-policy sampled action outcome only','curve':curve,'results':results,'duration_s':round(time.monotonic()-t0,2)}
    dest=folder/f'seed{a.seed}_{a.mode}_onpolicy.json'
    with open(dest,'w') as f:json.dump(record,f,indent=2)
    print('ONPOLICY',a.seed,a.mode,record['duration_s'],curve,results['gaussian'],flush=True)

if __name__=='__main__':
    main()
    os._exit(0)
