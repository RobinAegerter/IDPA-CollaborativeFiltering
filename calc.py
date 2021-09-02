from numpy import dot
from numpy.linalg import norm


def cos_sim(x, y):
    return dot(x, y)/(norm(x)*norm(y))


def fixed_formula(similarities, n, ratings, i):
    counter = 0
    for y in range(n):
        counter += similarities[y] * ratings[y][i]
    denominator = 0
    for y in range(n):
        counter += similarities[y]
    return counter/denominator


def get_all_simularties_of_user(user, data):
    similarities = []
    for compared_user in data:
        if compared_user is user:
            continue
        similarities.append(cos_sim(user[1:], compared_user[1:]))
    return similarities
