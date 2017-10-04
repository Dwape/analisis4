import csv
import numpy as np

from src.main.python.analisis4.spacedust.Lagrange import lagrange

def evaluate_Points(begin, end, function):
    newLatitud = np.empty([int((begin - end) / 10) + 1])
    j = 0
    for i in range(begin, end - 1, -10):
        newLatitud[j] = function(i)
        j += 1
        print(i)
        print(function(i))
    return newLatitud



def write_csv(begin, end, newLatitud):
    out = csv.writer(open("myfile.csv", "a"), delimiter="\n")
    write = []
    for i in range(0, begin-end, 10):
        write.append(str(i+end) + "," + str(newLatitud[int((begin-end - i) / 10)]))

    out.writerow(write)


def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return np.asarray([result[column] for result in results])

def getXPoints(size, distance):
    xPoints = []
    for i in range(0, size, distance):
        xPoints[i] = i
    return xPoints

def calculateLagrange(x1, x2):
    altura = get_column("geo_pos.csv", 0)
    latitud = get_column("geo_pos.csv", 1)
    function = lagrange(altura[x1:x2+1], latitud[x1:x2+1])
    newLatitud = evaluate_Points(altura[x1], altura[x2], function)
    write_csv(int(altura[x1]),  int(altura[x2]), newLatitud)

calculateLagrange(50,94)
calculateLagrange(0, 50)







