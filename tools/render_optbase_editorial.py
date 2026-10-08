#!/usr/bin/env python3
"""Atlas candidate v0.1.1: exact-input OPTBASE plate, deterministic local render.

This is a Matplotlib editorial derivative, NOT a Wolfram generator replay.
The immutable v0.1.0 Wolfram master and source/manifests remain unchanged.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.ticker import MultipleLocator

ROOT=Path(__file__).resolve().parent.parent
OUTPUT=ROOT/"figures/derivatives/ATLAS-FIG-OPTBASE-001-v0.1.1.png"
MODEL={
 "a_range":(Fraction(0),Fraction(3)),
 "strict_stability":(Fraction(0),Fraction(2)),
 "gradient":(Fraction(3),Fraction(4)),
 "threshold":Fraction(2),
 "clipped":(Fraction(6,5),Fraction(8,5)),
 "coupled":Fraction(183,100),
 "decoupled":Fraction(181,100)
}
assert MODEL["gradient"][0]**2+MODEL["gradient"][1]**2==25
assert MODEL["clipped"]==(MODEL["threshold"]/5*MODEL["gradient"][0],MODEL["threshold"]/5*MODEL["gradient"][1])
assert MODEL["clipped"][0]**2+MODEL["clipped"][1]**2==4
assert MODEL["coupled"]-MODEL["decoupled"]==Fraction(1,50)
assert abs(1-0)==1 and abs(1-1)==0 and abs(1-2)==1

plt.rcParams.update({
 "font.family":"DejaVu Sans", "font.size":10.5,"mathtext.fontset":"dejavusans",
 "axes.titlesize":12, "axes.labelsize":10, "figure.facecolor":"white",
 "axes.spines.top":False, "axes.spines.right":False,
})
fig,axes=plt.subplots(1,3,figsize=(15.3,4.4),layout="constrained",width_ratios=[1,1.05,1.0])
a=np.linspace(0,3,601)
ax=axes[0]
ax.axvspan(0,2,color="0.93",zorder=0)
ax.plot(a,np.abs(1-a),color="0.1",lw=2.3)
ax.axhline(1,color="0.45",ls="--",lw=1.2)
ax.axvline(2,color="0.45",ls=":",lw=1.2)
ax.plot([0,2],[1,1],ls="",marker="o",mfc="white",mec="0.2",ms=6)
ax.set(xlim=(-.06,3.12),ylim=(-.05,2.2),xlabel=r"$a=\eta\lambda$",ylabel=r"$|1-\eta\lambda|$",title="A. Quadratic GD amplification")
ax.text(1.0,.19,r"$0<a<2$: convergence",ha="center",fontsize=10)
ax.annotate("boundary",xy=(2,1),xytext=(2.25,1.3),arrowprops=dict(arrowstyle="->",color="0.3"),fontsize=9)

ax=axes[1]
ax.add_patch(Circle((0,0),2,fill=False,edgecolor="0.5",lw=1.7,linestyle="--"))
ax.annotate("",xy=(3,4),xytext=(0,0),arrowprops=dict(arrowstyle="->",lw=2,color="0.05"))
ax.annotate("",xy=(1.2,1.6),xytext=(0,0),arrowprops=dict(arrowstyle="->",lw=2.5,color="0.48"))
ax.plot([3,1.2],[4,1.6],"o",color="0.05",ms=5)
ax.annotate(r"$g=(3,4),\ \|g\|=5$",xy=(3,4),xytext=(-2.2,4.55),fontsize=10,arrowprops=dict(arrowstyle="-",color="0.5"))
ax.annotate(r"$g_{\rm clip}=(6/5,8/5)$",xy=(1.2,1.6),xytext=(-2.2,3.3),fontsize=9.8,arrowprops=dict(arrowstyle="-",color="0.5"))
ax.text(-2.5,-2.8,r"$\tau=2,\quad \|g_{\rm clip}\|=2$",fontsize=10)
ax.set(xlim=(-3,5),ylim=(-3.2,5.25),xlabel=r"$g_1$",ylabel=r"$g_2$",title="B. Global norm clipping")
ax.set_aspect("equal",adjustable="box")
ax.axhline(0,color="0.7",lw=.7);ax.axvline(0,color="0.7",lw=.7)

ax=axes[2]
x0=float(MODEL["decoupled"]);x1=float(MODEL["coupled"])
ax.set_xlim(1.795,1.845)
ax.set_ylim(-.8,.9)
ax.plot([x0,x1],[0,0],color="0.3",lw=2)
ax.scatter([x0,x1],[0,0],marker="o",s=62,facecolors=["white","0.2"],edgecolors="0.2",zorder=4)
ax.annotate(r"$181/100$",xy=(x0,0),xytext=(x0-.003,.4),ha="right",fontsize=11,arrowprops=dict(arrowstyle="->",color="0.4"))
ax.annotate(r"$183/100$",xy=(x1,0),xytext=(x1+.003,-.43),ha="left",fontsize=11,arrowprops=dict(arrowstyle="->",color="0.4"))
ax.text(1.82,.71,r"$\Delta\theta = 1/50$",ha="center",fontsize=11)
ax.text(1.804,-.65,"Decoupled",fontsize=10,ha="left")
ax.text(1.843,.57,"Coupled",fontsize=10,ha="right")
ax.xaxis.set_major_locator(MultipleLocator(.01))
ax.set(xlabel=r"next $\theta$",yticks=[],title="C. Adaptive decay differs")
ax.spines["left"].set_visible(False)
fig.suptitle("Optimization: stability, clipping, and decay",fontsize=14.5,fontweight="bold")
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(OUTPUT,dpi=160,facecolor="white",bbox_inches="tight",pad_inches=.15)
plt.close(fig)
from PIL import Image
with Image.open(OUTPUT) as im:
    w,h=im.size
assert 1.5<w/h<6.5,(w,h)
print("OPTBASE_DERIVATIVE",str(OUTPUT),"PIXELS",w,h,"SHA256",hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),"MATPLOTLIB",matplotlib.__version__)
