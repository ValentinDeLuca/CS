OSERROR = "OSError Opening File: "
def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def count_characters(text):
    aux = text
    count = {}
    words = set(aux)
    for word in words:
        count[word] = text.count(word)
    return count

def make_graph(data_base, n): # Receives the number for each character:
    top = list(data_base.values())[0]
    lower = list(data_base.values())[-1]
    asterisc = "■"
    for character in data_base:
        print(f"{character}:{asterisc*(1+((data_base[character] - lower) * 100 // top))} {round((100 * data_base[character]) / n, 2)}%")

def main(filename, n):
    text = open_file(filename)
    dict_characters = dict(sorted(count_characters(text).items(), key=lambda x: x[1], reverse=True))
    make_graph(dict_characters, n)
