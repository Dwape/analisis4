import csv
import numpy as np

from src.main.python.analisis4.spacedust.Lagrange import lagrange
from src.main.python.analisis4.spacedust.grapher import graph3d, graph2d


def evaluate_Points(begin, end, function, distance):
    newLatitud = np.empty([int((begin - end) / distance) + 1])
    j = 0
    for i in range(begin, end - 1, -distance):
        newLatitud[j] = function(i)
        j += 1
        print(i)
        print(function(i))
    return newLatitud


def write_csv2d(begin, end, newLatitud, distance, filename):
    out = csv.writer(open(filename, "w"), delimiter="\n")
    write = []
    for i in range(0, begin-end, distance):
        write.append(str(i+end) + "," + str(newLatitud[int((begin-end - i) / distance)]))

    out.writerow(write)

def write_csv3d(begin, end, newLatitud, newLongitud, distance, filename):
    out = csv.writer(open(filename, "w"), delimiter="\n")
    write = []
    for i in range(0, begin-end, distance):
        write.append(str(i+end) + "," + str(newLatitud[int((begin-end - i) / distance)]) + "," + str(newLongitud[int((begin-end - i )/ distance)]))

    out.writerow(write)

def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    array = []
    for result in results:
        if len(result) > 0:
            array.append(result[column])
    return array

# np.asarray([result[column] for result in results])


def getZPoints(size, distance):
    xPoints = np.empty([size])
    for i in range(0, size, distance):
        xPoints[i] = i
    return xPoints


#def calculateLagrange(x1, x2, distance):
#    altura = get_column("geo_pos.csv", 0)
#    latitud = get_column("geo_pos.csv", 1)
#    function = lagrange(altura[x1:x2+1], latitud[x1:x2+1])
#    return  evaluate_Points(int(altura[x1]), int(altura[x2]), function, distance)


def fileWriter():
    distance = 10
    yPoints = np.empty([int(10000 / distance)])
    xPoints = np.empty([int(10000 / distance)])
    altura = get_column("geo_pos.csv", 0)
    latitud = get_column("geo_pos.csv", 1)
    longitud = get_column("geo_pos.csv", 2)

    functionY1 = lagrange(altura[0:51], latitud[0:51])
    yPoint1 = evaluate_Points(int(altura[0]), int(altura[50]), functionY1, distance)
    yPoint1 = np.delete(yPoint1, len(yPoint1)-1)

    functionX1 = lagrange(altura[0:51], longitud[0:51])
    xPoint1 = evaluate_Points(int(altura[0]), int(altura[50]), functionX1, distance)
    xPoint1 = np.delete(xPoint1, len(xPoint1) - 1)

    functionY2 = lagrange(altura[50:95], latitud[50:95])
    yPoint2 = evaluate_Points(int(altura[50]), int(altura[94]), functionY2, distance)
    yPoint2 = np.delete(yPoint2, len(yPoint2) - 1)

    functionX2 = lagrange(altura[50:95], longitud[50:95])
    xPoint2 = evaluate_Points(int(altura[50]), int(altura[94]), functionX2, distance)
    xPoint2 = np.delete(xPoint2, len(xPoint2) - 1)

    yPoint3 = evaluate_Points(int(altura[94]), 0, functionY2, distance)
    xPoint3 = evaluate_Points(int(altura[94]), 0, functionX2, distance)

    yPoints = np.append(yPoint1, yPoint2, axis=0)
    yPoints = np.append(yPoints, yPoint3, axis=0)
    xPoints = np.append(xPoint1, xPoint2, axis=0)
    xPoints = np.append(xPoints, xPoint3, axis=0)


    write_csv3d(10000, 0, yPoints, xPoints, distance, "interpolated10.csv")



def createGraph3d():
    altura = get_column("interpolated10.csv", 0)
    latitud = get_column("interpolated10.csv", 1)
    longitud = get_column("interpolated10.csv", 2)

    graph3d(altura, latitud, longitud)

def createGraph2d(column, name):
    altura = get_column("interpolated10.csv", 0)
    axisY = get_column("interpolated10.csv", column)

    graph2d(axisY, altura, name, "Altura")

#fileWriter()
createGraph2d(1, "Latitud")
createGraph2d(2, "Longitud")
createGraph3d()







