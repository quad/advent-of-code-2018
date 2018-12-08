from copy import deepcopy
from collections import namedtuple, defaultdict


test_input = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''

Coordinate = namedtuple('Coordinate', ['x', 'y'])


def is_closest(coord, matrices, x, y):
    distances = []
    for c, other in matrices.items():
        if c != coord:
            distances.append(other[x][y])
    if matrices[coord][x][y] < min(distances):
        return True
    return False


def is_infinite(coord, coord_matrices):
    size_x = len(coord_matrices[coord])
    size_y = len(coord_matrices[coord][0])
    for x in [0, size_x - 1]:
        for y in range(size_y):
            if is_closest(coord, coord_matrices, x, y):
                print("x", coord)
                print(x, y)
                return True
    for x in range(size_x):
        for y in [0, size_y - 1]:
            if is_closest(coord, coord_matrices, x, y):
                print('y', coord)
                print(x, y)
                return True
    return False


def get_coords(strings):
    coords = []
    for string in strings:
        coord = string.strip().split(', ')
        coords.append(Coordinate(int(coord[0]), int(coord[1])))
    return coords


def generate_matrices(coords):
    min_x = min(c.x for c in coords)
    min_y = min(c.y for c in coords)
    max_x = max(c.x for c in coords)
    max_y = max(c.y for c in coords)
    base_y = [0] * (max_y - min_y + 1)
    base_matrix = [list(base_y) for _ in range(max_x - min_x + 1)]
    print(len(base_matrix))
    print(len(base_y))
    coord_matrices = {}
    adjusted_coords = []
    for coord in coords:
        adjusted_coords.append(Coordinate(coord.x - min_x, coord.y - min_y))

    for coord in adjusted_coords:
        matrix = deepcopy(base_matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = abs(x - coord.x) + abs(y - coord.y)
        coord_matrices[coord] = matrix
    return coord_matrices


def puzzle1(strings):
    coord_matrices = generate_matrices(get_coords(strings))
    coords = list(coord_matrices.keys())
    for coord in list(coords):
        if is_infinite(coord, coord_matrices):
            coords.remove(coord)

    captured_area = defaultdict(int)
    for coord in coords:
        print(coord)
        matrix = coord_matrices[coord]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if is_closest(coord, coord_matrices, x, y):
                    captured_area[coord] += 1
    print(captured_area)
    areas = list(captured_area.values())
    areas.sort()
    return(areas.pop())


def puzzle2(strings, threshold):
    coord_matrices = generate_matrices(get_coords(strings))
    coords = list(coord_matrices.keys())
    sum_matrix = coord_matrices[coords[0]]
    del(coord_matrices[coords[0]])
    for coord, matrix in coord_matrices.items():
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                sum_matrix[x][y] += matrix[x][y]
    area = 0
    for row in sum_matrix:
        for val in row:
            if val < threshold:
                area += 1
    return "area is " + str(area)


print(puzzle1(test_input.splitlines()))
print(puzzle2(test_input.splitlines(), 32))
with open('6.txt') as f:
    print(puzzle2(f.readlines(), 10000))
with open('6.txt') as f:
    print(puzzle1(f.readlines()))
