
"""Magic boxes
Alice has 42 magic boxes.
Each box has infinite capacity, but can only store one type of objects. The type itself is not relevant, but once an
object has been inserted in a box, then only objects of that type can be added. For instance, after inserting an apple,
any number of apples can be added, even tons, but not a single banana.
If a magic box is emptied, it can be refilled with a new type of objects. For instance, after removing all the apples
from the box, a banana can be stored; and after that, any number of bananas, but not apples anymore.
Bob is handling Alice a sequence of objects; Alice should store them in the magic boxes according to previous notes. At
the same time, Carl is asking Alice for objects; Alice should take the object Carl is asking for from one box, and
handle it to him.
Write a program to simulate the behavior of Alice, Bob, and Carl. A text file named 'actions.txt' contains the actions
performed by Bob and Carl, one per line, in the form "Bob gives a OBJECT" or "Carl takes a OBJECT". The program should
check what happen, reporting a message if Alice is not able to respond correctly because either she can't store Bob's
object in a box, or she can't give Carl the requested object because it's not available.
The file is correct. Object names are a single word and are written in CAPITAL.
For instance (and assuming that Alice has only 2 boxes):

Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Bob gives a CHERRY
Generates an error, because Alice cannot store a CHERRY

Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Carl takes a CHERRY
Bob gives a CHERRY
Generates an error, because Alice cannot give a CHERRY

Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Carl takes a BANANA
Bob gives a CHERRY
Generates no errors, as the box with the first BANANA is emptied and can later store a CHERRY."""
# Files
FILENAME = "actions.txt"
READ_FILE = "r"
# N-boxes
NUMBER_OF_BOXES = 124 # breaks with 123
# Writes
BOXES_FILLED = " could not be added."
ITEM_MISSING = "Item could not be found"
GIVE_ACTION = "gives"
TAKE_ACTION = "take"
# Error messages
OSERROR = "OSError Opening File: "

def open_file(filename):
    try:
        with open(filename, READ_FILE) as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def analyze_data(lines):
    boxes = {}
    for line in lines:
        _, action, _, item = line.split()
        if action == TAKE_ACTION:
            if item in boxes:
                boxes[item] = boxes[item] - 1
                if boxes[item] <= 0:
                    del boxes[item]
            else:
                print(ITEM_MISSING)
                break
        elif action == GIVE_ACTION:
            if item in boxes:
                boxes[item] = boxes[item] + 1
            else:
                if len(boxes) + 1 > NUMBER_OF_BOXES:
                    print(f"{item}{BOXES_FILLED}")
                    break
                else:
                    boxes[item] = 1
    return boxes


def main():
    print(analyze_data(open_file(FILENAME)))


if __name__ == "__main__":
    main()
