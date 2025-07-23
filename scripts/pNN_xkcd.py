import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

for mX in [300, 350, 400]:
  plt.figure(figsize=(5, 5))
  plt.xkcd()
  x = np.linspace(100, 500, 400)
  y_bkg = sps.crystalball.pdf(-x, 1.5, 1.1, -200, 50)
  y_sig = 0.5*sps.crystalball.pdf(-x, 1.5, 1.1, -mX, 25)
  # y_bkg = sps.norm.pdf(x, 200, 50)
  # y_sig = sps.norm.pdf(x, 300, 50)

  alpha = 0.5 if mX == 350 else 1
 
  plt.plot(x, y_bkg, label='Background', zorder=3)
  plt.plot(x, y_sig, label=r'$m_X=%d\,$GeV'%mX, zorder=3, alpha=alpha)
  plt.legend(ncol=2, loc="upper center")
  plt.ylim(top=plt.ylim()[1]*1.2)

  #turn off y-axis
  plt.gca().axes.get_yaxis().set_visible(False)
  plt.xlabel(r"$m_{\gamma\gamma\tau\tau}$ [GeV]")
  plt.axvline(mX-25, color='black', linestyle='--', alpha=alpha)
  plt.axvline(mX+50, color='black', linestyle='--', alpha=alpha)

  plt.tight_layout()
  plt.savefig(f"Figures/Dihiggs/categorisation/pNN_intution_mX{mX}.pdf")
  plt.clf()