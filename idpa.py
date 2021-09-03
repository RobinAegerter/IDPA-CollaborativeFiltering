import data_extraktion
import format_data
import printer
from copy import copy, deepcopy


def main():
    data = data_extraktion.get_ratings('./Bewertung.csv')
    movies = data_extraktion.get_movies('./Bewertung.csv')
    data = format_data.normalize(data)
    for user in data:
        similarities = format_data.get_all_simularties_of_user(
            deepcopy(user), deepcopy(data))
        printer.user_similarities(user[0], similarities)
    for user in data:
        format_data.get_empty_ratings(user, movies)


if __name__ == '__main__':
    main()
