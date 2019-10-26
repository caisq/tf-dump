import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

plt.figure(figsize=[10, 3.5])

ax = plt.subplot(1, 2, 1)
x = np.arange(-10, 10, 0.1)
y = tf.nn.sigmoid(x)
plt.plot(x, y)
plt.xlim([-10, 10])
plt.xlabel('x')
plt.title('sigmoid(x)')
plt.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax = plt.subplot(1, 2, 2)
y = tf.nn.relu(x)
plt.plot(x, y)
plt.xlim([-10, 10])
plt.xlabel('x')
plt.title('relu(x)')
plt.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.savefig('Figure_3_2.png', dpi=600)
plt.show()

