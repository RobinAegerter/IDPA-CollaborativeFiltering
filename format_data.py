import calc


def normalize(data):
    ratings = []
    for row in data:
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
    print(f'Length: {len(ratings)}\n')
    return ratings


def get_all_simularties_of_user(user, data):
    similarities = []
    for compared_user in data:
        if compared_user is user:
            continue
        similarities.append(calc.cos_sim(user[1:], compared_user[1:]))
    return similarities
