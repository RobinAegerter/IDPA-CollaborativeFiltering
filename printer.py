

def user_similarities(user, sims):
    print(f'\n{user}\n')
    for sim in sims:
        if sim is user:
            continue
        print(f'{sim}: {sims[sim]}')
