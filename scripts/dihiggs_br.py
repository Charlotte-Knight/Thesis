import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import itertools
import mplhep
mplhep.style.use("CMS")

br = {
    r"$bb$": 5.824e-1,
    r"$WW$": 2.137e-1,
    r"$gg$": 8.187e-2,
    r"$\tau\tau$": 6.272e-2,
    r"$cc$": 2.891e-2,
    r"$ZZ$": 2.619e-2,
    r"$\gamma\gamma$": 2.27e-3,
}

labels, values = zip(*list(br.items())[::-1])
x = np.arange(len(labels))
bin_edges = np.arange(len(labels)+1)

xs = []
ys = []
brs = []

plt.figure(figsize=(10, 8))

for i, j in itertools.combinations_with_replacement(x, 2):
  xs.append(j+0.5)
  ys.append(i+0.5)
  f = 1 if i == j else 2
  brs.append(f * values[i] * values[j])
  print(labels[i], labels[j], f * values[i] * values[j])

for i, j, br in zip(xs, ys, brs):
  if br > 0.001:
    if f"{br:.2g}" == "0.01":
      plt.text(i, j, "0.010", ha="center", va="center", color="black", fontsize=18)
    else:
      plt.text(i, j, f"{br:.2g}", ha="center", va="center", color="black", fontsize=18)
  else:
    plt.text(i, j, f"{br:.1e}", ha="center", va="center", color="white", fontsize=18)
  # else:
  #   plt.text(i, j, f"<\n{br:.4f}", ha="center", va="center", color="black", fontsize=18)

plt.hist2d(xs, ys, weights=brs, bins=bin_edges, norm=matplotlib.colors.LogNorm())
plt.colorbar()#.set_label("HH branching ratio")
plt.title("HH branching fractions")

plt.xticks(x+0.5, labels)
plt.yticks(x+0.5, labels)

plt.minorticks_off()
plt.gca().tick_params(axis='x', which='major', top=False)
plt.gca().tick_params(axis='y', which='major', right=False)


plt.tight_layout()
plt.savefig("Figures/Dihiggs/dihiggs_br.pdf")