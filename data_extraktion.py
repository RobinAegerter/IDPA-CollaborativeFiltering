import pandas as pd


def get_filtered_value(value):
    if value.isnumeric():
        return int(value)
    else:
        return 0


def get_ratings(path):
    data = pd.read_csv(path).values.tolist()
    filtered = []
    for row in data:
        filtered_row = [row[1]]
        for i in range(3, len(row)):
            filtered_row.append(get_filtered_value(row[i]))
        if str(filtered_row).count('0') <= 13:
            filtered.append(filtered_row)
    return filtered


def get_movies(path):
    data = pd.read_csv(path).keys()
    movies = ["Names"]
    for i in range(3, len(data)):
        movies.append(data[i][16:-26])
    return movies
