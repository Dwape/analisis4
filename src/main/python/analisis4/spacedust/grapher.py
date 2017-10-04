import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def graph2d(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()


def graph3d(x_values, y_values, z_values):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    #X = np.arange(-5, 5, 0.25)
    #Y = np.arange(-5, 5, 0.25)
    x_values, y_values = np.meshgrid(x_values, y_values)
    #R = np.sqrt(X ** 2 + Y ** 2)
    #Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(x_values, y_values, z_values, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


x_val = np.array([1, 2, 3, 4, 5])
y_val = np.array([0, 0.69315, 1.09861, 1.38629, 1.60944])
z_val = np.array([1, 2, 3, 4, 5])

#graph3d(x_val, y_val, z_val)
graph2d(x_val, y_val)
