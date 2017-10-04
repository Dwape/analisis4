import csv
import numpy as np

from src.main.python.analisis4.spacedust.Lagrange import lagrange
from src.main.python.analisis4.spacedust.grapher import graph3d, graph2d


def evaluate_Points(begin, end, function, distance):
    new_latitud = np.empty([int((begin - end) / distance) + 1])
    j = 0
    for i in range(begin, end - 1, -distance):
        new_latitud[j] = function(i)
        j += 1
        print(i)
        print(function(i))
    return new_latitud

def write_csv3d(begin, end, newLatitud, newLongitud, distance, filename):
    out = csv.writer(open(filename, "w"), delimiter="\n")
    write = []
    for i in range(0, begin-end+1, distance):
        write.append(str(i+end) + "," + str(newLatitud[int((begin-end - i) / distance)]) + "," + str(newLongitud[int((begin-end - i )/ distance)]))

    out.writerow(write)


def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    array = []
    for result in results:
        if len(result) > 0:
            array.append(float(result[column]))
    return array

# np.asarray([result[column] for result in results])


def getZPoints(size, distance):
    xPoints = np.empty([size])
    for i in range(0, size+1, distance):
        xPoints[i] = i
    return xPoints


def file_writer():
    distance = 1
    y_points = np.empty([int(10000 / distance)])
    x_points = np.empty([int(10000 / distance)])
    altura = get_column("geo_pos.csv", 0)
    latitud = get_column("geo_pos.csv", 1)
    longitud = get_column("geo_pos.csv", 2)

    function_y1 = lagrange(altura[0:51], latitud[0:51])
    y_point1 = evaluate_Points(int(altura[0]), int(altura[50]), function_y1, distance)
    y_point1 = np.delete(y_point1, len(y_point1)-1)

    function_x1 = lagrange(altura[0:51], longitud[0:51])
    x_point1 = evaluate_Points(int(altura[0]), int(altura[50]), function_x1, distance)
    x_point1 = np.delete(x_point1, len(x_point1) - 1)

    function_y2 = lagrange(altura[50:91], latitud[50:91])
    y_point2 = evaluate_Points(int(altura[50]), int(altura[90]), function_y2, distance)
    y_point2 = np.delete(y_point2, len(y_point2) - 1)

    function_x2 = lagrange(altura[50:91], longitud[50:95])
    x_point2 = evaluate_Points(int(altura[50]), int(altura[94]), function_x2, distance)
    x_point2 = np.delete(x_point2, len(x_point2) - 1)

    function_y3 = lagrange(altura[90:95], latitud[90:95])
    y_point3 = evaluate_Points(int(altura[90]), int(altura[94]), function_y3, distance)
    y_point3 = np.delete(y_point3, len(y_point3) - 1)

    function_x3 = lagrange(altura[90:95], longitud[90:95])
    x_point3 = evaluate_Points(int(altura[90]), int(altura[94]), function_x3, distance)
    x_point3 = np.delete(x_point3, len(x_point3) - 1)

    y_point4 = evaluate_Points(int(altura[94]), 0, function_y3, distance)
    x_point4 = evaluate_Points(int(altura[94]), 0, function_x3, distance)

    y_points = np.append(y_point1, y_point2, axis=0)
    y_points = np.append(y_points, y_point3, axis=0)
    y_points = np.append(y_points, y_point4, axis=0)
    x_points = np.append(x_point1, x_point2, axis=0)
    x_points = np.append(x_points, x_point3, axis=0)
    x_points = np.append(x_points, x_point4, axis=0)

    write_csv3d(10000, 0, y_points, x_points, distance, "interpolated10.csv")



def create_graph_3d():
    altura = get_column("interpolated10.csv", 0)
    latitud = get_column("interpolated10.csv", 1)
    longitud = get_column("interpolated10.csv", 2)

    graph3d(longitud, latitud, altura, "Longitud", "Latitud", "Altura")

def create_graph_2d(column, name):
    altura = get_column("interpolated10.csv", 0)
    axisY = get_column("interpolated10.csv", column)

    graph2d(axisY, altura, name, "Altura")

#file_writer()
create_graph_2d(1, "Latitud")
create_graph_2d(2, "Longitud")
create_graph_3d()







