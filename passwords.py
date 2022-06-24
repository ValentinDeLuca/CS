"""Randomly Generates a password containing Aa numbers and symbols
Calls wordcount.py to plot a graph of the most repeated characters"""
import random
import wordcount

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BETA = ALPHA.lower()
NUM = "0123456789"
SYM = "\ !@#$%^&*()_+=-[]{};':,./<>?|`~\""
ALL = ALPHA + BETA + NUM + SYM

OUTPUT_FILENAME = "password.txt"


def main():
    password_len = ask_for_n()
    top_len = len(ALL)
    generated_pass = ""
    for i in range(password_len):
        generated_pass = generated_pass + ALL[random.randint(0, top_len-1)]
    with open(OUTPUT_FILENAME, "w") as file:
        file.write(generated_pass)
    count_words(OUTPUT_FILENAME, password_len)

def ask_for_n():
    try:
        n = int(input("Insert Password Len: "))
        if n > 0:
            return n
        else:
            print("This is not a valid number. Try again!")
            return ask_for_n()
    except:
        print("This is not a valid number. Try again!")
        return ask_for_n()
def count_words(filename, n):
    wordcount.main(filename, n)


if __name__ == '__main__':
    main()
