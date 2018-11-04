import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10*np.pi, 50000, endpoint=True)
y1 = np.sin(0.7*x1)*np.sin(6*x1)*np.sin(20*x1)*np.cos(100*x1)

transformed = np.fft.fft(y1)

plt.figure(1)
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
plt.sca(ax1)
plt.plot(x1, y1)

plt.sca(ax2)
plt.plot(transformed)

plt.show()
