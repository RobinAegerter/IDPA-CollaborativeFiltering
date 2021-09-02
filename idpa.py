import data_extraktion
import format_data
import printer


def main():
    data = data_extraktion.get('./Bewertung.csv')
    data = format_data.normalize(data)
    for user in data:
        similarities = format_data.get_all_simularties_of_user(user, data)
        printer.user_similarities(user[0], similarities)


if __name__ == '__main__':
    main()
