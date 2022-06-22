"""Write a program that searches for a given word in the contents of a group of files.
The program first asks for the list of files (to be placed on a single line, separated by
commas and the word to be searched. The names of the files will be stored in a list
(files),the word to be searched is stored in a variable.
You must display all lines that contain the word, regardless it is uppercase or
lowercase, each line preceded by the name of the file in which it is located. For
example, if the word was "ring", and the list contain:
book.txt, address.txt, homework.py
then the program may display the following:
book.txt: There is only one Lord of the Ring, only one who can bend
it to his will
book.txt: The ring has awoken; it’s heard its masters call.
address.txt: Kris Kringle, North Pole
address.txt: Homer Simpson, Springfield
homework.py: string = "text"
The search word is entered by the user and the words containing the search word are
also valid (eg. ring and growl)."""
FILENAME_FILES = "files.txt"
FILENAME = "words.txt"
OSERROR = "OSError Opening File: "
def find_word_in_lines(word, filename):
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)
    for line in lines:
        for chunk in range(len(line)-len(word)):
            if line[chunk:chunk + len(word)].lower() == word:
                print(f"{filename}: {line}")

def main():
    files = input("Insert the name of the files separated by a comma: ").split(",")
    word = input("Insert the word you're looking for: ")
    for file in files:
        find_word_in_lines(word, file)


if __name__ == '__main__':
    main()
