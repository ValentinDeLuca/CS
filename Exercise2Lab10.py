"""Write a program that reads all the lines of a text file (input.txt), reverses the order and
writes them in another file (output.txt). For example, if the input.txt file contains
these lines:
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.
then the output file.txt will contain:
The lamb was sure to go.
And everywhere that Mary went
Its fleece was white as snow
Mary had a little lamb"""

FILENAME = "input.txt"
FILENAME_OUTPUT = "output_reversed.txt"
OSERROR = "OSError Opening File: "
def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def reverse_file(lines):
    reversed_lines = ""
    for i, line in enumerate(lines[::-1]):
        reversed_lines = reversed_lines + line
        if i < len(lines[::-1])-1:
            reversed_lines = reversed_lines + "\n"
    return reversed_lines

def write_output_file(line):
    try:
        with open(FILENAME_OUTPUT, "w") as output_file:
            output_file.write(line)
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def main():
    write_output_file(reverse_file(open_file(FILENAME)))

if __name__ == '__main__':
    main()
