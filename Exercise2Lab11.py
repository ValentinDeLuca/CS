"""Write a program that asks the user to provide two strings, and then display (avoiding
repetition of characters in printing):
• the characters that appear in both strings;
• characters that appear in one string but not in the other;
• letters that do not appear in either string.
Tip: Turn a string into a set of characters"""

ALPHABET = set("abcdefghijklmnopqrstuvwxyz")

def ask_inputs():
    first = input("Introduce First String: ")
    second = input("Introduce Second String: ")
    return set(first), set(second)

def print_results(first, second):
    print(f"Union: {first.union(second)}")
    print(f"Difference first: {first.difference(second)}")
    print(f"Difference second: {second.difference(first)}")
    print(f"Neither: {ALPHABET.difference(first.union(second))}")

def main():
    first, second = ask_inputs()
    print_results(first, second)
    pass


if __name__ == "__main__":
    main()
