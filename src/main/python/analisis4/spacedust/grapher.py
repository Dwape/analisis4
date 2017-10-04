import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl


def graph2d(x_values, y_values, x_axis, y_axis):
    """Graphs a curve in 2D, with the values passed as parameters."""
    plt.plot(x_values, y_values)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()


def graph3d(x_values, y_values, z_values, x_axis, y_axis, z_axis):
    """Graphs a parametric curve with the values passed as parameters."""
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(x_values, y_values, z_values, label='parametric curve')
    ax.legend()

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_zlabel(z_axis)

    plt.show()




