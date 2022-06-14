"""Write a program that counts the occurrences of each word in a text file,whose
name is entered by keyboard. Assume that the file contains only alphabetical or
spacing characters. B) Next, improve the program so that it displays the 100 most
common words (in case of parity at position 100, it does not matter which words are
printed)."""
FILE_NAME = "../../text.txt"

def file_open(name_of_file):
    words_in_file = []
    try:
        with open(name_of_file, "r")as file:
            lines = file.read().splitlines()
            for line in lines:
                words_in_file = words_in_file + line.split()
    except OSError as problem:
        print(f"Error Opening File: {problem}")
        exit(1)
    return words_in_file
def input_words():
    word_dict = dict()
    words = input("Words to find: ").split()
    for word in words:
        word_dict[word] = 0
    return word_dict

def analyze(words_in_file, words_to_find):
    for word in words_in_file:
        if word in words_to_find:
            words_to_find[word] = words_to_find[word] + 1
    return words_to_find

def top_one_hundred(words_in_file):
    word_count = {}
    for word in words_in_file:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    sorted_dict = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(100):
        print(f"{sorted_dict[i]}")
    return 1

def main():
    choice = int(input("1: Search for Words\n2: Top 100\n->>"))
    if choice == 1:
        print(analyze(file_open(FILE_NAME), input_words()))
    elif choice == 2:
        top_one_hundred(file_open(FILE_NAME))


if __name__ == "__main__":
    main()
