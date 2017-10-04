import csv
import numpy as np

from src.main.python.analisis4.spacedust.Lagrange import lagrange


def evaluate_Points(begin, end, function, distance):
    newLatitud = np.empty([int((begin - end) / distance) + 1])
    j = 0
    for i in range(begin, end - 1, -distance):
        newLatitud[j] = function(i)
        j += 1
        print(i)
        print(function(i))
    return newLatitud


def write_csv(begin, end, newLatitud, distance):
    out = csv.writer(open("myfile.csv", "a"), delimiter="\n")
    write = []
    for i in range(0, begin-end, distance):
        write.append(str(i+end) + "," + str(newLatitud[int((begin-end - i) / distance)]))

    out.writerow(write)


def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return np.asarray([result[column] for result in results])


def getXPoints(size, distance):
    xPoints = []
    for i in range(0, size, distance):
        xPoints[i] = i
    return xPoints


#def calculateLagrange(x1, x2, distance):
#    altura = get_column("geo_pos.csv", 0)
#    latitud = get_column("geo_pos.csv", 1)
#    function = lagrange(altura[x1:x2+1], latitud[x1:x2+1])
#    return  evaluate_Points(int(altura[x1]), int(altura[x2]), function, distance)


def main():
    distance = 10
    yPoints = np.empty([int(10000/distance)])
    altura = get_column("geo_pos.csv", 0)
    latitud = get_column("geo_pos.csv", 1)

    function1 = lagrange(altura[0:50 + 1], latitud[0:50 + 1])
    yPoint1 = evaluate_Points(int(altura[0]), int(altura[50]), function1, distance)

    function2 = lagrange(altura[50:94+1], latitud[50:94+1])
    yPoint2 = evaluate_Points(int(altura[50]), int(altura[94]), function2, distance)

    yPoint3 = evaluate_Points(int(altura[94]), 0, function2, distance)

    yPoints = np.append(yPoint1, yPoint2, axis=0)
    yPoints = np.append(yPoints, yPoint3, axis=0)

    write_csv(10000, 0, yPoints, distance)

main()







