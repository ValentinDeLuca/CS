"""Write a "censor" program, which reads a file (bad_words.txt) containing a list of
"bad words" (such as "sex", "drugs", "C++" and so on), one per line, inserting them
into a set. Then read another text file: the program must rewrite the second file
read, generating a third in which all the letters of each swear word (including those
in the sub-words containing swear words) have been replaced by a number of
asterisks equal to its length."""

FILENAME = "text.txt"
FILENAME_BAD_WORDS = "badwords.txt"
FILENAME_OUTPUT = f"censored_{FILENAME}"
ERROR_OPENING_FILE = "OSError Opening file: "


def open_file_return_lines():
    try:
        with open(FILENAME, "r") as text:
            return text.read().splitlines()
    except OSError as problem:
        print(ERROR_OPENING_FILE + f"{problem}")


def open_bad_file_return_lines():
    try:
        with open(FILENAME_BAD_WORDS, "r") as bads:
            return set(bads.read().splitlines())
    except OSError as problem:
        print(ERROR_OPENING_FILE + f"{problem}")
        exit(1)


def replace_bad_word(editing, word, bad_word):
    if bad_word in word:  # replace the contained bad word in the current word
        editing = word.replace(bad_word, "*" * len(bad_word))
    return editing


def replace_in_line(palabras, bad_words):
    final = ""
    for palabra in palabras:  # iterate through every word in phrase
        editing = palabra
        for bad in bad_words:  # search for each bad word on the current word
            editing = replace_bad_word(editing, palabra, bad)
        final = final + editing + " "
    return final


def full_edit(lines, bad_words):
    final_text = ""
    for line in lines:
        final_text = final_text + replace_in_line(line.split(), bad_words) + "\n"
    return final_text


def write_new_file(output):
    try:
        with open(FILENAME_OUTPUT, "w") as otp_file:
            otp_file.write(output)
        return otp_file
    except OSError as problem:
        print(ERROR_OPENING_FILE + f"{problem}")


def main():
    lines = open_file_return_lines()
    bad_words = open_bad_file_return_lines()
    censored_text = full_edit(lines, bad_words)
    write_new_file(censored_text)
    exit(0)


if __name__ == '__main__':
    main()
