"""The administrative manager of a hotel records sales in a text file. Each line contains
the following 4 information, separated by "semicolon" characters: the customer's
name, the service sold (for example, dinner, conference, accommodation, and so on),
the amount paid and the date of the event. Write a program that reads such a text file and displays the total amount
related to each type of service, reporting an error if the file does not exist or if its format is incorrect (verifying
that there are 4 fields per line and that the price is float). [P7. 29]"""
FILENAME = "sales.txt"
OSERROR = "ORError Opening File: "
INVALID_FILE_ERROR = "Invalid fields per line."
def open_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)
    return lines

def lines_to_dict(lines):
    amount_per_service = {}
    for line in lines:
        items = line.split(";")
        if len(items) == 4:
            items[2] = money_to_int(items[2])
            if items[1] in amount_per_service:
                amount_per_service[items[1]] = amount_per_service[items[1]] + items[2]
            else:
                amount_per_service[items[1]] = items[2]
        else:
            print(INVALID_FILE_ERROR)
            exit(1)
    return amount_per_service

def money_to_int(item):
    return float(item[1:])

def main():
    services = lines_to_dict(open_file(FILENAME))
    for service in services:
        print(f"{service}: ${services[service]}")


if __name__ == '__main__':
    main()
