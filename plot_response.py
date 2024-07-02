import matplotlib.pyplot as plt
import numpy as np

from passive_joint_function import get_passive_force

angle = np.arange(np.pi,-np.pi, -np.pi/180)
pos_force = list(map(get_passive_force, angle, np.zeros_like(angle)))
vel_force = list(map(get_passive_force, np.zeros_like(angle), angle))
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(angle,pos_force)
axs[0].grid()
axs[0].set_xlabel("Angle (radians)")
axs[0].set_ylabel("Force Applied")

axs[1].plot(angle,vel_force)
axs[1].grid()
axs[1].set_xlabel("Angle (radians)")
axs[1].set_ylabel("Force Applied")

plt.savefig("./gifs/response_plot.png")