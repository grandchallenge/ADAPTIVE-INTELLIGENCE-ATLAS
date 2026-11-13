#!/usr/bin/env python3
"""Stage-based joint objective training for reproducible endogenous control pilot.

No fault-ID or self-model-target supervision: only task loss and normalized replay costs.
The actor phase uses full counterfactual outcome enumeration. This is a strong
full-information-training assumption, not demonstrated online exploration.
"""
import argparse
import json
import os
import time
from dataclasses import asdict
from pathlib import Path
import torch
from torch.nn import functional as F
from owi_ec004_core import Cfg,Core,Actor,sample_data,exact_expected_risk,eval_model


def train_base(seed,cfg,n):
    torch.manual_seed(seed)
    rng=torch.Generator().manual_seed(seed+101)
    core=Core(cfg.h)
    opt=torch.optim.Adam(core.parameters(),lr=0.013)
    for t in range(n):
        x,y=sample_data(cfg.batch,cfg,rng)
        loss=F.binary_cross_entropy_with_logits(core.forward_clean(x),y)
        opt.zero_grad();loss.backward();opt.step()
    with torch.no_grad():
        x,y=sample_data(4096,cfg,rng)
        accuracy=((core.forward_clean(x)>0).float()==y).float().mean().item()
    return core,accuracy


def train_controller(core,seed,cfg,active,feature,steps=500):
    # Frozen-core policy identification using task outcomes, not fault annotations.
    torch.manual_seed(seed+5)
    rng=torch.Generator().manual_seed(seed+103)
    actor=Actor(cfg.h,active,feature)
    for p in core.parameters():p.requires_grad_(False)
    opt=torch.optim.Adam(actor.parameters(),lr=0.002)
    phases=[]
    for step in range(steps):
        x,y=sample_data(cfg.batch,cfg,rng)
        entropy_temperature=(0.13 if step < steps//3 else (0.06 if step < (2*steps)//3 else 0.015))
        value=exact_expected_risk(core,actor,x,y,cfg,rng,
             uniform_probe=(active and step < steps//2),
             exploration=0.04 if step < int(steps*0.8) else 0.0,
             entropy_temp=entropy_temperature)
        opt.zero_grad();value.backward();torch.nn.utils.clip_grad_norm_(actor.parameters(),3.0);opt.step()
        if (step+1)%100==0:phases.append((step+1,round(value.detach().item(),5)))
    for p in core.parameters():p.requires_grad_(True)
    return actor,phases


def fine_tune(core,actor,seed,cfg,steps=100):
    torch.manual_seed(seed+6)
    rng=torch.Generator().manual_seed(seed+104)
    opt=torch.optim.Adam([{'params':core.parameters(),'lr':0.0005}, {'params':actor.parameters(),'lr':0.0008}])
    for step in range(steps):
        x,y=sample_data(cfg.batch,cfg,rng)
        v=exact_expected_risk(core,actor,x,y,cfg,rng,exploration=0.01,entropy_temp=0.005)
        opt.zero_grad();v.backward();torch.nn.utils.clip_grad_norm_(list(core.parameters())+list(actor.parameters()),3.0);opt.step()
    return float(v.detach())


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',choices=['pretrain','actor','joint','eval'],required=True)
    parser.add_argument('--seed',type=int,default=1)
    parser.add_argument('--mode',choices=['active_rich','passive_rich','active_summary','passive_summary'],default='active_rich')
    parser.add_argument('--folder',default='build/owi_ec004')
    parser.add_argument('--pretrain',type=int,default=250)
    parser.add_argument('--actor-steps',type=int,default=1200)
    parser.add_argument('--joint-steps',type=int,default=100)
    parser.add_argument('--eval',type=int,default=4000)
    parser.add_argument('--lambda-compute',type=float,default=0.035)
    parser.add_argument('--overhead',type=float,default=0.005)
    parser.add_argument('--wandb-project',default='',help='optional explicit W&B evaluation logging')
    args=parser.parse_args()
    torch.set_num_threads(1)
    cfg=Cfg(pretrain=args.pretrain,joint=args.joint_steps,eval_n=args.eval,lambda_compute=args.lambda_compute,policy_overhead=args.overhead)
    folder=Path(args.folder);folder.mkdir(parents=True,exist_ok=True)
    prefix=folder / ('seed'+str(args.seed))
    path=folder / ('seed'+str(args.seed)+'_'+args.mode+'.pt')
    active=args.mode.startswith('active')
    feature='summary' if 'summary' in args.mode else 'rich'
    started=time.monotonic()
    if args.stage=='pretrain':
        core,acc=train_base(args.seed,cfg,args.pretrain)
        torch.save({'core':core.state_dict(),'accuracy':acc,'cfg':asdict(cfg)},str(prefix)+'_core.pt')
        print('BASE_TRAINED',args.seed,'acc',acc,'seconds',time.monotonic()-started,flush=True)
    elif args.stage=='actor':
        state=torch.load(str(prefix)+'_core.pt',weights_only=True)
        core=Core(cfg.h);core.load_state_dict(state['core']);core.eval()
        actor,curve=train_controller(core,args.seed,cfg,active,feature,args.actor_steps)
        torch.save({'core':core.state_dict(),'actor':actor.state_dict(),'curve':curve,'pretrain_accuracy':state['accuracy'],'cfg':asdict(cfg)},path)
        print('ACTOR_TRAINED',args.mode,curve,'seconds',time.monotonic()-started,flush=True)
    elif args.stage=='joint':
        state=torch.load(path,weights_only=True)
        core=Core(cfg.h);core.load_state_dict(state['core'])
        actor=Actor(cfg.h,active,feature);actor.load_state_dict(state['actor'])
        final=fine_tune(core,actor,args.seed,cfg,args.joint_steps)
        state.update({'core':core.state_dict(),'actor':actor.state_dict(),'joint_last_objective':final})
        torch.save(state,path)
        print('JOINT_FINETUNED',args.mode,'last_loss',final,'seconds',time.monotonic()-started,flush=True)
    else:
        state=torch.load(path,weights_only=True)
        core=Core(cfg.h);core.load_state_dict(state['core']);core.eval()
        actor=Actor(cfg.h,active,feature);actor.load_state_dict(state['actor']);actor.eval()
        conditions={kind:eval_model(core,actor,args.seed,cfg,kind) for kind in ('gaussian','dropout','signflip','roll','small_noise')}
        if active:
            for kind in conditions:
                conditions[kind]['zero_probe_information_objective']=eval_model(core,actor,args.seed,cfg,kind,signal_mode='zero_probe')['objective']
                conditions[kind]['shuffled_all_telemetry_objective']=eval_model(core,actor,args.seed,cfg,kind,signal_mode='shuffle')['objective']
        result={'seed':args.seed,'mode':args.mode,'pretrain_accuracy':state['pretrain_accuracy'],
                'actor_curve':state['curve'],'joint_last_objective':state.get('joint_last_objective'),
                'conditions':conditions,'cfg':asdict(cfg),'training':'full information expected task risk, no diagnostic labels'}
        with open(folder / ('seed'+str(args.seed)+'_'+args.mode+'.json'),'w') as f:json.dump(result,f,indent=2)
        if args.wandb_project:
            import wandb
            with wandb.init(project=args.wandb_project,config={'seed':args.seed,'mode':args.mode,**asdict(cfg)}):
                wandb.log({f'{kind}/{k}':v for kind,rec in conditions.items() for k,v in rec.items() if isinstance(v,(int,float))})
        print('EVALUATED',args.seed,args.mode,'gaussian',conditions['gaussian'],'signflip',conditions['signflip'],'seconds',time.monotonic()-started,flush=True)

if __name__=='__main__':
    main()
    os._exit(0)
