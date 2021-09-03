
def get_extreme_str(xtr, sims):
    value = xtr(sims, key=sims.get)
    return f'{value}: {sims[value]}'


def user_similarities(user, sims):
    maxi = get_extreme_str(max, sims)
    mini = get_extreme_str(min, sims)
    print(f'\n{user}\n \n{maxi}\n{mini}')
