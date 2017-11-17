import matplotlib.pyplot as plt


def graph2dHeatMap(array):
    plt.imshow(array, cmap='hot', interpolation='nearest')
    plt.show()