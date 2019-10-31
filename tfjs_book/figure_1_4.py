import numpy as np
import matplotlib.pyplot as plt

N_POINTS = 300

xys = 2 * (np.random.rand(N_POINTS, 2) - 0.5)
xys = np.concatenate([xys, np.array([[-0.695, 0.85]])], axis=0)

radii = np.sqrt(xys[:, 0] * xys[:, 0] + xys[:, 1] * xys[:, 1])
print(radii)

xys = xys[np.logical_and(radii > 0.3, radii < 0.7), :]
print(xys.shape)

angles = np.arctan2(xys[:, 1], xys[:, 0])

is_white = np.logical_or(
    np.logical_and(angles > 0, angles < np.pi * 3 / 4),
    np.logical_and(angles < 0, angles > - np.pi * 3 / 4))
xys_white = xys[is_white, :]
xys_black = xys[np.logical_not(is_white), :]

plt.figure(figsize=[12, 9])
ax = plt.subplot(2, 2, 1)
plt.plot(xys_white[:, 0],  xys_white[:, 1],
         'ko', markerfacecolor='w')
plt.plot(xys_black[:, 0],  xys_black[:, 1],
         'ko', markerfacecolor='k')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('A')

#
angles_white = np.rad2deg(np.arctan2(xys_white[:, 1], xys_white[:, 0]))
angles_black = np.rad2deg(np.arctan2(xys_black[:, 1], xys_black[:, 0]))
radius_white = np.sqrt(xys_white[:, 1] ** 2 + xys_white[:, 0] ** 2)
radius_black = np.sqrt(xys_black[:, 1] ** 2 + xys_black[:, 0] ** 2)
ax = plt.subplot(2, 2, 2)
plt.plot(angles_white, radius_white, 'ko', markerfacecolor='w')
plt.plot(angles_black, radius_black, 'ko', markerfacecolor='k')
ax.axvline(x=135, linestyle='--', color='k')
ax.axvline(x=-135, linestyle='--', color='k')
plt.xlim([-180, 180])
plt.ylim([0, np.sqrt(2.0)])
plt.xlabel('Angle (degrees)')
plt.ylabel('Radius')
plt.title('B')

#
ax = plt.subplot(2, 2, 3)
plt.plot(np.abs(angles_white) - 135, np.zeros_like(radius_white),
         'ko', markerfacecolor='w')
plt.plot(np.abs(angles_black) - 135, np.zeros_like(radius_black),
         'ko', markerfacecolor='k')
ax.axvline(x=0, linestyle='--', color='k')
plt.xlim([-135, 45])
plt.ylim([-0.1, 0.1])
plt.yticks([0])
plt.xlabel('abs(Angle) - 135')
plt.title('C')
ax.set_position([0.125, 0.3, 0.5, 0.1])

plt.savefig('Figure_1_4.png', dpi=300)
plt.show()