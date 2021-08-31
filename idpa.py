import numpy as np
from numpy.linalg import norm
import pandas as pd

data = pd.read_csv('Bewertung.csv').values.tolist()
filtered = []


def getFilteredValue(value):
    if value.isnumeric():
        return int(value)
    else:
        return 0


def cos_sim(a, b):
    return np.dot(a, b)/(norm(a)*norm(b))


def fixed_formula(sims, n, ratings, i):
    counter = 0
    for y in range(n):
        counter += sims[y] * ratings[y][i]
    denominator = 0
    for y in range(n):
        counter += sims[y]
    return counter/denominator


for row in data:
    filtered_row = [
        row[1],
        getFilteredValue(row[3]),
        getFilteredValue(row[4]),
        getFilteredValue(row[5]),
        getFilteredValue(row[6]),
        getFilteredValue(row[7]),
        getFilteredValue(row[8]),
        getFilteredValue(row[9]),
        getFilteredValue(row[11]),
        getFilteredValue(row[12]),
        getFilteredValue(row[13]),
        getFilteredValue(row[14]),
        getFilteredValue(row[15])
    ]
    if str(filtered_row).count('0') <= 5:
        filtered.append(filtered_row)
        print(filtered_row)
print("Length: "+str(len(filtered)))

ratings = []
print("\n")
for row in filtered:
    int_row = row[1:]
    dataPoints = []
    for rating in int_row:
        if rating > 0:
            dataPoints.append(rating)
    mean = sum(int_row) / len(dataPoints)
    meaned_el = []
    meaned_el.append(row[0])
    for rating in int_row:
        if rating > 0:
            meaned_el.append(rating-mean)
        else:
            meaned_el.append(0)
    ratings.append(meaned_el)
    print(meaned_el)
print("Length: "+str(len(ratings)))


for person in ratings:
    print()
    print(person[0])
    print()
    sims = []
    for compare in ratings:
        if compare is person:
            continue
        sims.append(str(cos_sim(person[1:], compare[1:])) + " " + compare[0])
    for i in range(4):
        print(max(sims))
        sims.remove(max(sims))
    for i in range(1):
        print(min(sims))
        sims.remove(min(sims))
