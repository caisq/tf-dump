import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 1e-4)
bce_true = - np.log(x + 1e-6)
bce_false = - np.log(1.0 - x + 1e-6)

plt.figure()
plt.plot(x, bce_true, 'k-', linewidth=2)
plt.plot(x, bce_false, 'b--', linewidth=2)
plt.xlim([0, 1])
plt.ylim([0, 14])
plt.grid(True)
plt.xlabel('probability')
plt.ylabel('binary cross entropy')
plt.legend(['trueLabel = 1', 'trueLabel = 0'])

plt.savefig('Figure_3_8.png', dpi=600)
plt.show()
