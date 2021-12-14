from tabulate import tabulate


def table(movies, raitngs, title):
    print(
        f'\n{title}\n\n{tabulate(raitngs, headers=movies, tablefmt="presto", numalign="center",floatfmt=".3f")}\n')


def user_similarities(user, sims, neighborhood):
    i = 0
    similarities = []
    for sim in sims:
        if sim is user:
            continue
        similarities.append([sims[sim], sim])
        i += 1
        if i >= (neighborhood+neighborhood/1.5):
            break
    print(f'\n{user}\n\n{tabulate(similarities,tablefmt="plain", numalign="decimal",floatfmt=".5f")}')

