
"""Complete the program of the previous exercise so that it finds a way out of the maze
from any point. Build a new dictionary whose keys are the positions of the corridors
and whose values are all equal to the string "?". Then scan the keys to that dictionary.
For each key that is at the
edge of the maze (i.e. represents an exit),replace the "?" with a value ("N", "E", "S",
or "W") indicating the direction of the exit path. At this point, repeat the scan of the
keys whose value has remained "?" and check if they have at least one adjacent
whose value is not "?", using the first dictionary to locate the adjacents. Found one of
such adjacent, replace the string "?" with the direction of the adjacent. If you fail to
make any of these substitutions during one of these scans, stop the algorithm.
Finally, visualize the labyrinth thus obtained: in each corridor position there will be
the direction that leads most quickly to an exit. For example,:
*N*******
*NWW*?*S*
*N*****S*
*N*S*EES*
*N*S***S*
*NWW*EES*
*****N*S*
*EEEEN*S*
*******S*
"""
from pprint import pprint

"""Write a program that reads a text file(maze.txt) containing the image of a labyrinth,
such as the following, in which the asterisks are impassable walls and the spaces are
passable corridors.
Generate a dictionary whose keys are tuples of the type (row, column) of corridor
locations and whose values are sets of adjacent corridor locations. In the labyrinth
example presented here, (1, 1) (blue square) has as adjacent corridors {(1, 2), (0, 1),
(2, 1)}. View the dictionary.
"""

FILENAME = "maze.txt"
OSERROR = "OSError Opening File: "
CORRIDOR = " "
WALL = "*"
UNDEFINED = "?"

NEWS = "NEWS"
NORTH = "N"
EAST = "E"
WEST = "W"
SOUTH = "S"

def open_file(filename):
    try:
        with open(filename) as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
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
    if 1+row < len(matrix) and matrix[1+row][col] == CORRIDOR:
        result.add((1+row, col))
    if 1+col < len(matrix[row]) and matrix[row][1+col] == CORRIDOR:
        result.add((row, 1+col))
    if row-1 > -1 and matrix[row-1][col] == CORRIDOR:
        result.add((row-1, col))
    if col-1 > -1 and matrix[row][col-1] == CORRIDOR:
        result.add((row, col-1))
    if result == set():
        return None
    return result

# ---------------------------------------------------------------------------------------------------------------------#

def corridors_to_undefined(matrix, corridors):
    for corridor in corridors:
        matrix[corridor[0]][corridor[1]] = UNDEFINED

def insert_fastest_way_out(matrix, corridors):
    for i in range(len(matrix)):
        if i == 0 or i == len(matrix)-1:
            for j in range(len(matrix[i])):
                if matrix[i][j] == UNDEFINED:
                    if i == 0:
                        # Exit from Up
                        matrix[i][j] = NORTH
                        spread(matrix, corridors, i+1, j)
                    elif i == len(matrix)-1:
                        # Exit from Down
                        matrix[i][j] = SOUTH
                        spread(matrix, corridors, i-1, j)
        else:
            if matrix[i][0] == UNDEFINED:
                # Exit from Left
                matrix[i][0] = WEST
                spread(matrix, corridors, i, 1)
            if matrix[i][len(matrix[i])-1] == UNDEFINED:
                # Exit from Right
                matrix[i][len(matrix[i])-1] = EAST
                spread(matrix, corridors, i, len(matrix[i])-2)

def spread(matrix, corridors, i, j):
    news = NEWS                  # Where does it come from
    if matrix[i-1][j] in news:     # -North
        matrix[i][j] = NORTH
    elif matrix[i][j+1] in news:   # -East
        matrix[i][j] = EAST
    elif matrix[i][j-1] in news:   # -West
        matrix[i][j] = WEST
    elif matrix[i+1][j] in news:   # -South
        matrix[i][j] = SOUTH
    for corridor in corridors[(i, j)]: # Iterate through neighbours Key: (i, j) Value: {(i+1, j+1), (j, i+1)}
        if matrix[corridor[0]][corridor[1]] == UNDEFINED:   # If any of them is still unknown, keep spreading
            spread(matrix, corridors, corridor[0], corridor[1])

def main():
    data = open_file(FILENAME)
    matrix = lines_to_matrix(data)
    corridors = get_corridors_from_matrix(matrix)
    corridors_to_undefined(matrix, corridors)
    insert_fastest_way_out(matrix, corridors)
    pprint(matrix)


if __name__ == '__main__':
    main()
