import calc
import operator


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
                meaned_el.append(None)
        ratings.append(meaned_el)
        print(meaned_el)
    print(f'Length: {len(ratings)}\n')
    return ratings


def replace_none_with_zero(ratings):
    for i in range(len(ratings)):
        if ratings[i] is None:
            ratings[i] = 0
    return ratings


def get_all_simularties_of_user(user, data):
    user = replace_none_with_zero(user)
    similarities = {}
    for compared_user in data:
        compared_user = replace_none_with_zero(compared_user)
        similarities[compared_user[0]] = calc.cos_sim(
            user[1:], compared_user[1:])
    return dict(sorted(similarities.items(), key=operator.itemgetter(1), reverse=True))


def get_empty_ratings(user, movies, sims, data):
    print('Hasn\'t seen:')
    for i in range(len(user)):
        if user[i] is None:
            rating = calc.fixed_formula(sims, 4, data, i)
            print(f'    {movies[i]}: {rating}')
