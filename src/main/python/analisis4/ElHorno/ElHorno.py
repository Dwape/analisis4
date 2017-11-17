import csv
from src.main.python.analisis4.ElHorno.RungeKutta import runge_kutta, temperature_function
from src.main.python.analisis4.ElHorno.Grapher import graph2dHeatMap, graph

def get_column_csv(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    array = []
    for result in results:
        if len(result) > 0:
            array.append(float(result[column]))
    return array


def write_csv(array, filename):
    out = csv.writer(open(filename, "w"), delimiter=",")
    write = []
    for i in range(0, len(array)):
        out.writerow(array[i])

    out.writerow(write)


def get_row(array, i):
    row = str(array[i][0])
    for j in range(1, len(array[i])):
        row = row + ", " + str(array[i][j])
    return row


def calculate_temp(h, current_t,  t, array):
    new_array = []
    new_array.append(array[0])
    for i in range(1, len(array)-1):
        sub_array = []
        sub_array.append(array[i][0])
        for j in range(1, len(array[i])-1):
            sub_array.append(calculate_one_place(array, i, j, h, current_t, t))
        sub_array.append(array[i][len(array[i])-1])
        new_array.append(sub_array)
    new_array.append(array[len(array)-1])
    return new_array


def calculate_one_place(array, i, j, h, current_t, t):
    medium = 0
    for k in range(i-1, i+2):
        medium += array[k][j-1]
        medium += array[k][j+1]
    medium += array[i-1][j]
    medium += array[i+1][j]
    medium = medium/8
    result = runge_kutta(temperature_function, h, t, array[i][j], current_t, medium)
    return result


def calculate(h, t):
    current_t = 0
    array = []
    for i in range(0, 21):
        array.append(get_column_csv("temperaturas_horno.csv", i))

    for i in range(0, 10):
        array = calculate_temp(h, current_t+t, current_t, array)
        current_t += t
        print("Finished " + str(current_t))
        write_csv(array, "Results/temperatura" + str(current_t) + ".csv")
        graph2dHeatMap(array)
        #graph(array)

calculate(0.01, 100)

