"""Write a program that reads a text file(maze.txt) containing the image of a labyrinth,
such as the following, in which the asterisks are impassable walls and the spaces are
passable corridors.
Generate a dictionary whose keys are tuples of the type (row, column) of corridor
locations and whose values are sets of adjacent corridor locations. In the labyrinth
example presented here, (1, 1) (blue square) has as adjacent corridors {(1, 2), (0, 1),
(2, 1)}. View the dictionary.
"""
from pprint import pprint

FILENAME = "maze.txt"
CORRIDOR = " "
WALL = "*"


def open_file(filename):
    try:
        with open(filename) as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"OSError opening file: {problem}")
        exit(0)


def lines_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append(list(line))
    return matrix


def get_corridors_from_matrix(matrix):
    corridors = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == CORRIDOR:
                corridors[(i, j)] = get_neighbour_corridors(matrix, i, j)
    return corridors


def get_neighbour_corridors(matrix, row, col):
    result = set()
    if 1 + row < len(matrix) and matrix[1 + row][col] == CORRIDOR:
        result.add((1 + row, col))
    if 1 + col < len(matrix[row]) and matrix[row][1 + col] == CORRIDOR:
        result.add((row, 1 + col))
    if row - 1 > -1 and matrix[row - 1][col] == CORRIDOR:
        result.add((row - 1, col))
    if col - 1 > -1 and matrix[row][col - 1] == CORRIDOR:
        result.add((row, col - 1))
    if result == set():
        return None
    return result


def main():
    data = open_file(FILENAME)
    matrix = lines_to_matrix(data)
    print(get_corridors_from_matrix(matrix))
    pprint(matrix)


if __name__ == '__main__':
    main()
