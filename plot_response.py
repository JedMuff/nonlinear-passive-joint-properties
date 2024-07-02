import matplotlib.pyplot as plt
import numpy as np

def plot_response(func, ax):

    x = np.arange(np.pi/2,-np.pi/2, -np.pi/180)
    y = list(map(func,x))

    ax.plot(x,y)
    ax.grid()
    ax.xlabel("Angle (radians)")
    ax.ylabel("Force Applied")
