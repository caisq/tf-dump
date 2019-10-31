import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[8, 6])

x = np.arange(-6.25, 6.25, 0.1)
y = tf.math.atan(x)
plt.plot(x, y)
plt.xlim([-6.25, 6.25])
plt.xlabel('x')
plt.xlabel('atan(x)')
plt.title('atan')
plt.grid(True)
ax = fig.axes[0]
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.savefig('Figure_A_5.png', dpi=600)
plt.show()

