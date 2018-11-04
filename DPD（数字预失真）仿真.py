import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(20, 40, 500, endpoint=True)
y1 = np.linspace(2, 2, 500, endpoint=True)

plt.figure(1)
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
plt.sca(ax1)

o_sin = np.sin(4*x1)+2
t_sin = np.sqrt(20*o_sin)
n_sin = 0.1*t_sin*t_sin-2
#n_sin = 2*o_sin-2
plt.plot(x1, o_sin)
plt.plot(x1, n_sin)
plt.plot(x1, y1)
#plt.plot(x1, 2*o_sin-2, color='red')

plt.sca(ax2)
z_sin = 0.1*x1*x1
y = 2*np.sqrt(20*x1)

plt.plot(x1, z_sin)
plt.plot(x1, 2*x1)
plt.plot(x1, y)

plt.xlim(20, 60)
plt.ylim(40, 60)

plt.show()
