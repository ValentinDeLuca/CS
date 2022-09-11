"""ARTISTIC GYMNASTICS

Create a Python program that manages the scores of an artistic gymnastics competition. The information is contained in a file "scores.txt". Each line of the file has the following format (fields separated by space):

name, surname, sex, nation, the 5 scores assigned by the judges.

Make the following assumptions:

    The number of lines in the file is not known a priori
    The Name and Surname fields do not contain spaces
    The athlete's sex is encoded by an M or F character.
    The country abbreviation is always coded on 3 capital letters
    5 votes are always assigned for each athlete, separated by a space and the value may vary from a minimum of 0 to a maximum of 10.

The program must print:

    The name of the female winner. When calculating the total points, the maximum and the maximum score must always be DISCARDED minimum amon the 5 assigned. The final score is therefore given by the sum of the three remaining scores.
    The ranking of the top 3 nations, including both female and male athletes. For each nation the total score is calculated by adding the scores of all its athletes (M and F, and always discarding the highest and lowest scores of each athlete).

Example:

Yuri Chechi M ENG 9.3 8.9 9.7 9.7 9.8
Veronica Servente F ITA 9.0 9.0 9.0 9.2 9.5
Sabrina Vega F USA 8.4 8.7 8.5 8.6 9.0
Viktoria Komova F RUS 8.3 8.7 9.5 9.6 9.0
Rebecca Downie F GRB 8.2 8.9 8.9 8.6 9.3
Douglas F USA Cages 8.2 8.9 8.9 8.6 9.3
Hannah Whelan F GRB 8.0 8.0 8.0 8.0 8.0

the program output should be the following:

Female winner:
Veronica Servente, ITA - Score: 27.2

Overall nations ranking:
1) ITA - Total score: 55.9
2) USA - Final Score: 52.2
3) GRB - Final Score: 50.4
"""

FILENAME = "scores.txt"
OS_ERROR = "Error opening file"
GET_N_COUNTRIES_ERROR = "Unable to get top %d countries"
FEMALE = "F"
FEMALE_WINNER = "Female winner:\n%s, %s - Score: %g\n"
TOP_COUNTRIES = "Overall nations ranking: "
TOP_N_COUNTRY = "%d) %s - Total score: %.1f"
N = 3

def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OS_ERROR}: {problem}")
        exit(1)


def analise_data(lines):
    info_list = []
    for line in lines:
        items = line.split()
        info_list.append(
            [" ".join(items[0:2]), items[2], items[3], items[4:]])  # NAME&SURNAME, GENDER, COUNTRY,SCORES[]
        for i in range(len(info_list[-1][-1])):  # cast scores to float
            info_list[-1][-1][i] = float(info_list[-1][-1][i])
    return calculate_scores(info_list)


def calculate_scores(info_list):
    for i in range(len(info_list)):
        info_list[i][-1] = sum(sorted(info_list[i][-1])[1:-1])
    return info_list


def get_best_athlete_by_gender(gender, info_list):
    best_athlete = []
    best_score = 0
    for i in info_list:
        if i[1] == gender:
            if i[-1] > best_score:  # i[-1] -> score
                best_athlete = i
                best_score = i[-1]
    return best_athlete


def get_top_n_counties(n, info_list):
    countries_dict = make_countries_dict(info_list)
    try:
        return countries_dict[:n]
    except:
        print(GET_N_COUNTRIES_ERROR % n)
        exit(1)


def make_countries_dict(info_list):
    countries_dict = {}
    for i in info_list:
        try:
            countries_dict[i[2]] = countries_dict[i[2]] + i[-1]
        except KeyError:
            countries_dict[i[2]] = i[-1]
    return sorted(countries_dict.items(), key=lambda item: item[1], reverse=True)


def main():
    lines = open_file(FILENAME)
    info_list = analise_data(lines)
    best_female = get_best_athlete_by_gender(FEMALE, info_list)
    print(FEMALE_WINNER  % (best_female[0], best_female[1], best_female[-1]))
    top_three_countries = get_top_n_counties(N, info_list)
    for i, country in enumerate(top_three_countries):
        print(TOP_N_COUNTRY % (i, country[0], country[1]))


if __name__ == '__main__':
    main()
