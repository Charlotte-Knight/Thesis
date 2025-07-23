import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import mplhep
mplhep.style.use("CMS")
#plt.xkcd()

#increase font size
plt.rcParams.update({'font.size': 30})

# Make data
X = np.arange(-1.1, 1.1, 0.1)
Y = np.arange(-1.1, 1.1, 0.1)
X, Y = np.meshgrid(X, Y)

# Plot the surface
Z = (X**2 + Y**2) / 1.1
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min(), vmax=Z.max(), cmap=cm.Blues_r)
ax.set_xticks([-1, 1])
ax.set_yticks([-1, 1])
ax.set_zticks([])

ax.set_xlabel(r"$C_i$")
ax.set_ylabel(r"$C_j$")
ax.set_zlabel("NLL")
fig.savefig("pca_toy_a.pdf")
plt.clf()

# Plot the surface
Z = X**2 + Y**2 + 2*X*Y
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min(), vmax=Z.max(), cmap=cm.Blues_r)
ax.set_xticks([-1, 1])
ax.set_yticks([-1, 1])
ax.set_zticks([])

ax.set_xlabel(r"$C_i$")
ax.set_ylabel(r"$C_j$")
ax.set_zlabel("NLL")
fig.savefig("pca_toy_b.pdf")