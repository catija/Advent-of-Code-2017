# Code for spiral matrix from https://stackoverflow.com/a/36889800/4548692
NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction


def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2  # start near the center
    dx, dy = NORTH  # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count  # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
                    matrix[new_y][new_x] is None):  # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix  # nowhere to go


def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_" * width if el is None else fmt.format(el) for el in row))


def find_target(target, matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == target:
                print("Done!")
                return i, j
    return -1, -1


m = spiral(605, 605)
t = 361527
a, b = find_target(t, m)
c, d = find_target(1, m)
print("Target coordinates = ({},{})".format(a, b))
print("Target coordinates = ({},{})".format(c, d))
distance = abs(c - a) + abs(d - b)
print("Distance between {} and 1 is {}!".format(t, distance))
