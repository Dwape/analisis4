import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def graph2d(x_values, y_values, x_axis, y_axis):
    plt.plot(x_values, y_values)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()


def graph3d(x_values, y_values, z_values):
    """Two options:
    1. z_values don't need to be calculated with the new values of x and y np.meshgrid(x, y). If that
    is the case, z_values that were calculated previously can be used.
    2. z_values need to be calculated with the new values of x and y. Then, Lagrange could be applied
    with np.meshgrid(x, y) and z_values to get new z_values"""

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    #x_values, y_values = np.meshgrid(x_values, y_values)

    # Plot the surface.
    surf = ax.plot_surface(x_values, y_values, z_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


