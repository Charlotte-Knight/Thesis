import matplotlib.pyplot as plt
# change default font size
import numpy as np
import scipy.stats as sps
plt.xkcd()
plt.rcParams.update({'font.size': 18})

x = np.linspace(0, 10, 1000)

MZ = 1
WZ = 0.05

MH = 0.125
WH = 0.01

MN = 9
WN = 0.1

Z = sps.rel_breitwigner.pdf(x, rho=MZ/WZ, scale=WZ)
H = 0.1 * sps.rel_breitwigner.pdf(x, rho=MH/WH, scale=WH)
SM = Z #+H
NP = SM + sps.rel_breitwigner.pdf(x, rho=MN/WN, scale=WN)

f, ax = plt.subplots()

plt.plot(x, SM, label="SM")
plt.plot(x, NP, label="SM + NP")

#plt.ylim(bottom=-8.5)
plt.text(0.23, -0.1, r"$E < E_\text{LHC}$", transform=ax.transAxes)
plt.text(0.70, -0.1, r"$E > E_\text{LHC}$", transform=ax.transAxes)
plt.text(0.40, 0.30, "EFT", fontsize=30, transform=ax.transAxes)
plt.axvline(6, linestyle="--", color="k")
ax.set_xlabel(r"$E$ [TeV]", loc="right")

plt.ylabel("Rate [a.u.]")
plt.yscale("log")
#plt.xscale("log")
plt.legend()

plt.gca().axes.get_xaxis().set_visible(False)
#plt.xticks([])
#plt.xlabel("E")

plt.tight_layout()
plt.savefig("Figures/EFT/xkcd.pdf")