import data_extraktion
import format_data
import printer
from copy import deepcopy

NEIGHBORHOOD = 7


def main():
    data = data_extraktion.get_ratings('./ratings.csv')
    movies = data_extraktion.get_movies('./ratings.csv')
    printer.table(movies, data, "Filtered Data")
    data = format_data.normalize(data)
    printer.table(movies, data, "Normalized Data")
    for user in data:
        similarities = format_data.get_all_simularties_of_user(
            deepcopy(user), deepcopy(data))
        printer.user_similarities(user[0], similarities, NEIGHBORHOOD)
        format_data.get_empty_ratings(
            user, movies, similarities, data, NEIGHBORHOOD)


if __name__ == '__main__':
    main()
