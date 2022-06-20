"""Write a program that reads the data from the text file 1 rawdata_2014.txt and inserts
it into a dictionary whose keys are names of nations and whose values are annual per
capita incomes. Note that in the file the fields are separated by a tab character '\t'.
Then, the program must ask the user to provide country names, to display the
corresponding values. The program ends when the user writes quit. [P8.17]
Update: at the address https://www.cia.gov/the-world-factbook/field/real-gdp-percapita/country-comparison you can
download (button "Download Data") the similar data, updated to 2021, in CSV format. We suggest you try to solve the same
exercise by working on the CSV file."""

FILENAME = "import.txt"


def create_data_base_from_file(filename):
    try:
        with open(filename, "r") as file:
            return read_data(file.read().splitlines(), filename.split(".")[-1])
    except OSError as problem:
        print(f"OSError opening file: {problem}")
        exit(1)

def read_data(lines, extension):
    data_base, items, key_index, value_index = {}, [], 0, 0
    if extension == "csv":
        lines = lines[1:] # [1:] to remove first line with keys
    for line in lines:
        if extension == "csv":
            items = line.split('","')
            items[0] = items[0].lstrip('"') # .lstrip('"') to remove first extra "
            key_index, value_index = 0, 2
        elif extension == "txt":
            items = line.split('\t')    # split by \t
            key_index, value_index = 1, 2
        key, value = items[key_index], items[value_index].replace(" ", "")
        data_base[key] = value
    return data_base

def main():
    data_base = create_data_base_from_file(FILENAME)
    while True:
        user_input = input("Enter the name of a country to display it's value ['Quit' to exit]: ")
        if user_input.lower() == "quit":
            break
        else:
            try:
                print(f"{user_input}: {data_base[user_input]}")
            except KeyError:
                print("This is not a country! Try again")


if __name__ == '__main__':
    main()
