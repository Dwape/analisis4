import csv

def get_column(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return [result[column] for result in results]

altura = get_column("geo_pos.csv", 0)
latitud = get_column("geo_pos.csv", 1)

out = csv.writer(open("myfile.csv", "w"), delimiter="\n")
csv = []
for i in range(0, len(altura)-1):
    csv.append(altura[i] + "," + latitud[i])

out.writerow(csv)


