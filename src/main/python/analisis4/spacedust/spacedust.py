import csv
import numpy as np

from src.main.python.analisis4.spacedust.Lagrange import lagrange


def write_csv(begin, end, function):
    newLatitud = []
    for i in range(begin, end-1, -10):
        newLatitud.append(function(i))
        print(i)
        print(function(i))
    out = csv.writer(open("myfile.csv", "w"), delimiter="\n")
    write = []
    for i in range(0, begin-end, 10):
        write.append(str(i+end) + "," + str(newLatitud[int(i / 10) - 1]))

    out.writerow(write)


def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return [result[column] for result in results]


def calculateLagrange(x1, x2):
    altura = get_column("geo_pos.csv", 0)
    latitud = get_column("geo_pos.csv", 1)
    function = lagrange(altura[x1:x2], latitud[x1:x2])
    write_csv(int(altura[x1]),  int(altura[x2]), function)


calculateLagrange(0, 50)





