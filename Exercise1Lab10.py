"""Write a program that reads the input.txt text file. Each line read must be written to
the output file.txt preceded by the line number, inserted as a comment between
characters /* and */. For example, if the input file.txt were as follows:
Society in every state is a blessing, but
government, even in its best state, is but a
necessary evil; in its worst state an intolerable
one: for when we suffer, or are exposed to the
same miseries by a government, which we might
expect in a country without government, our
calamity is heightened by reflecting that we
furnish the means by which we suffer.
The output.txt file generated would be:
/*1*/Society in every state is a blessing, but
/*2*/government, even in its best state, is but a
/*3*/necessary evil; in its worst state an intolerable
/*4*/one: for when we suffer, or are exposed to the
/*5*/same miseries by a government, which we might
/*6*/expect in a country without government, our
/*7*/calamity is heightened by reflecting that we
/*8*/furnish the means by which we suffer."""
FILENAME = "input.txt"
FILENAME_OUTPUT = "output.txt"
OSERROR = "OSError Opening file: "
def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def write_output_file(lines):
    try:
        with open(FILENAME_OUTPUT, "w") as output:
            for i, line in enumerate(lines):
                output.write(f"/*{i+1}*/{line}")
                if i < len(lines)-1:
                    output.write("\n")
    except OSError as problem:
        print(f"{OSERROR}{problem}")
    exit(1)


def main():
    write_output_file(open_file(FILENAME))


if __name__ == '__main__':
    main()
