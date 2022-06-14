"""A scattered array is a sequence of numbers, most of which are zero. An efficient way
to store a scattered array is a dictionary, in which the keys are the locations where
there are non-zero values, and the values are the corresponding values in the
sequence. For example, the sequence 0 0 0 0 0 0 4 0 0 0 2 9 would be represented by
the dictionary {5:4, 9:2, 10:9}. Write a function, sparseArraySum, whose arguments
are two such dictionaries, a and b, and which returns a scattered array that is the
sum vector : its value at position i is the sum of the values of a and b at position i.
The dictionaries of the calling program should not be changed."""

WORM1 = [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 9]
WORM2 = [0, 0, 0, 0, 2, 3, 0, 0, 2, 0, 6]

""" Worms are long  and thin -> arrays
    Butterflies are large and complex -> dictionaries
    Monarchs are the upper class of butterflies -> two butterflies combined
    a worm goes through a Cocoon to turn into a Butterfly -> cocoon(worm) 
    a butterfly _devolves_ to turn into a worm -> devolve(butterfly) """

# Disclaimer: Worms don't turn into butterflies. Silkworms do. For simplicity they're called worms.

def cocoon(worm):
    butterfly = {}
    for i, number in enumerate(worm):
        if number > 0 or number < 0:
            butterfly[i] = number
    return butterfly


def sparceArraySum(butterfly1, butterfly2):
    monarch = {}
    enhance(monarch, butterfly1)
    enhance(monarch, butterfly2)
    return dict(sorted(monarch.items()))

def enhance(monarch, butterfly):
    for key in butterfly.keys():
        if key in monarch:
            monarch[key] = monarch[key] + butterfly[key]
        else:
            monarch[key] = butterfly[key]
    return monarch.items()


def devolve(butterfly):
    worm = []
    for i in butterfly:
        worm = worm + [0]*(i-len(worm))
        worm.append(butterfly[i])
    return worm


def main():
    worm1, worm2 = cocoon(WORM1), cocoon(WORM2)
    monarch = sparceArraySum(worm1, worm2)
    print(monarch)
    print(devolve(monarch))


if __name__ == '__main__':
    main()
