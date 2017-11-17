import matplotlib.pyplot as plt


def graph2dHeatMap(array):
    plt.imshow(array, cmap='hot', interpolation='nearest')
    plt.show()

def graph(array):
    import plotly.plotly as py
    import plotly.graph_objs as go


    data = [array]
    py.iplot(data, filename='basic-heatmap')