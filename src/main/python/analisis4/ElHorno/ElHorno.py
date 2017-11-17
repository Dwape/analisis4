import csv
import numpy as np


def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    array = []
    for result in results:
        if len(result) > 0:
            array.append(float(result[column]))
    return array

