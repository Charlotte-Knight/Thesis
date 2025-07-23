import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import mplhep
mplhep.style.use("CMS")
import scipy.interpolate as spi

#increase font size
plt.rcParams.update({'font.size': 30})

x = np.array([0, 0, 1, 1, 0.5])
y = np.array([0, 1, 0, 1, 0.5])
z = np.array([-2, 0, -2, -2, -0.5])

# Make data
X = np.arange(0, 1, 0.001)
Y = np.arange(0, 1, 0.001)
X, Y = np.meshgrid(X, Y)

linear_interp = spi.griddata((x, y), z, (X, Y), method='linear')
cubic_interp = spi.griddata((x, y), z, (X, Y), method='cubic')

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, linear_interp, rcount=50, ccount=50, linewidth=1.5)
ax.scatter(x, y, z, color='r', s=100)
ax.view_init(20, -30)
plt.draw()
fig.savefig("interp_toy_linear.pdf")
plt.clf()

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, cubic_interp, rcount=50, ccount=50, linewidth=1.5)
ax.scatter(x, y, z, color='r', s=100)
ax.view_init(20, -30)
plt.draw()
fig.savefig("interp_toy_cubic.pdf")
plt.clf()