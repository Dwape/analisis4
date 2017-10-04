import csv
import matplotlib.pyplot as plt

def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return [result[column] for result in results]

altura = get_column("geo_pos.csv",0)
latitud = get_column("geo_pos.csv",1)

plt.figure("Altura/Latitud")
plt.xlabel("Altura(km)")
plt.ylabel("Latitud(km)")

plt.plot(altura,latitud)