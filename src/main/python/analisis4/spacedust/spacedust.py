import csv

from src.main.python.analisis4.spacedust.Lagrange import lagrange


def write_csv(begin, end):

    newLatitud = []
    for i in range(begin, end, -10):
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





altura = get_column("geo_pos.csv", 0)
latitud = get_column("geo_pos.csv", 1)
function = lagrange(altura[0:100], latitud[0:100])
write_csv(10000,9899)







