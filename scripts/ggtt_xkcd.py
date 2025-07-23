import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

x = np.linspace(100, 180, 200)
y_non_res_bkg = np.exp(-x/30)
y_res_bkg = 0.003*np.exp(-(x-125)**2/1.5**2)
y_bkg = y_res_bkg + y_non_res_bkg
y_sig = 0.010*np.exp(-(x-125)**2/1.5**2)

plt.title(r"$\mathrm{X} \to \mathrm{HH}$ and $\mathrm{X} \to \mathrm{Y}(\tau\tau)\mathrm{H}(\gamma\gamma)$")
plt.plot(x, y_non_res_bkg, label='Nonresonant background', zorder=3)
plt.plot(x, y_res_bkg+y_non_res_bkg, label='+ single higgs', zorder=2)
plt.plot(x, y_bkg+y_sig, label='+ signal', zorder=1)
plt.legend()

#turn off y-axis
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel("$m_{\gamma\gamma}$ [GeV]")

plt.tight_layout()
plt.savefig("Figures/Dihiggs/introduction/xhh.pdf")
plt.clf()

"""-------------------------------------------"""

x = np.linspace(100, 1000, 2000)
y_non_res_bkg = np.exp(-x/100)
y_res_bkg = 0.04*np.exp(-(x-125)**2/1.5**2)
y_bkg = y_res_bkg + y_non_res_bkg
y_sig = 0.06*np.exp(-(x-400)**2/(1.5*3)**2)

plt.title(r"High-mass $\mathrm{X} \to \mathrm{Y}(\gamma\gamma)\mathrm{H}(\tau\tau)$")
plt.plot(x, y_non_res_bkg, label='Nonresonant background', zorder=3)
plt.plot(x, y_res_bkg+y_non_res_bkg, label='+ single higgs', zorder=2)
plt.plot(x, y_bkg+y_sig, label='+ signal', zorder=1)
plt.legend()

#turn off y-axis
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel("$m_{\gamma\gamma}$ [GeV]")

# set x tick at 100
plt.xticks([100*i for i in range(1, 11)])

plt.tight_layout()
plt.savefig("Figures/Dihiggs/introduction/xyh_high_mass.pdf")
plt.clf()

"""-------------------------------------------"""

x = np.linspace(65, 150, 200)
y_non_res_bkg = np.exp(-x/30)
y_res_bkg = 0.01*np.exp(-(x-125)**2/1.5**2)
y_dy_bkg = 0.005*np.exp(-(x-90)**2/1.5**2)
y_bkg = y_res_bkg + y_non_res_bkg + y_dy_bkg
y_sig = 0.03*np.exp(-(x-80)**2/(1)**2)

plt.title(r"Low-mass $\mathrm{X} \to \mathrm{Y}(\gamma\gamma)\mathrm{H}(\tau\tau)$")
plt.plot(x, y_non_res_bkg, label='Nonresonant background', zorder=4)
plt.plot(x, y_res_bkg+y_non_res_bkg, label='+ single higgs', zorder=3)
plt.plot(x, y_res_bkg+y_non_res_bkg+y_dy_bkg, label='+ DY background', zorder=2, color="#d62728")
plt.plot(x, y_bkg+y_sig, label='+ signal', zorder=1, color="#2ca02c")
plt.legend()

#turn off y-axis
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlabel("$m_{\gamma\gamma}$ [GeV]")

plt.xticks([65, 80, 100, 120, 140, 150])


plt.tight_layout()
plt.savefig("Figures/Dihiggs/introduction/xyh_low_mass.pdf")