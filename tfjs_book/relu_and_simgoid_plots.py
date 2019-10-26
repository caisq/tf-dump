import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.figure(figsize=[10, 3.5])

ax = plt.subplot(position=[0.1, 0.15, 0.35, 0.7])
x = np.arange(-10, 10, 0.1)
y = tf.nn.sigmoid(x)
plt.plot(x, y)
plt.xlim([-10, 10])
plt.xlabel('x')
plt.title('sigmoid(x)')
plt.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax = plt.subplot(position=[0.55, 0.15, 0.35, 0.7])
y = tf.nn.relu(x)
plt.xlim([-10, 10])
plt.xlabel('x')
plt.title('relu(x)')
plt.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x, y)

plt.savefig('Figure_3_2.png', dpi=600)
plt.show()

