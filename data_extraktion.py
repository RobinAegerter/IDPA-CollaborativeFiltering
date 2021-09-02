import pandas as pd


def getFilteredValue(value):
    if value.isnumeric():
        return int(value)
    else:
        return 0


def get(path):
    data = pd.read_csv(path).values.tolist()

    filtered = []
    for row in data:
        filtered_row = [row[1]]
        for i in range(3, len(row)):
            filtered_row.append(getFilteredValue(row[i]))
        if str(filtered_row).count('0') <= 5:
            filtered.append(filtered_row)
            print(filtered_row)
    print(f'Length: {len(filtered)}\n')
    return filtered
