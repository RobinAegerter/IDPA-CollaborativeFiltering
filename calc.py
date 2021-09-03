from numpy import dot
from numpy.linalg import norm


def cos_sim(x, y):
    return dot(x, y)/(norm(x)*norm(y))


def fixed_formula(similarities, n, ratings, i):

    valid_keys = []
    valid_ratings = []
    for key in similarities:
        for rating in ratings:
            if rating[0] is key and rating[i] is not None:
                valid_keys.append(key)
                valid_ratings.append(rating[i])
                n -= 1
        if n <= 0 or similarities[key] < 0:
            break
    counter = 0
    for i in range(len(valid_keys)):
        counter += similarities[valid_keys[i]] * valid_ratings[i]
    denominator = 0
    for rating in valid_ratings:
        denominator += rating
    return counter/denominator
