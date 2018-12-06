import re
from collections import namedtuple

ElfSquare = namedtuple('ElfSquare', ['id', 'coords', 'size'])


def add_to_matrix(source_matrix, coords, size):
    cur_x = len(source_matrix)
    cur_y = len(source_matrix[0])
    if cur_x < coords[0] + size[0]:
        for _ in range(coords[0] + size[0] - cur_x):
            source_matrix.append([0] * cur_y)

    if cur_y < coords[1] + size[1]:
        for row in range(len(source_matrix)):
            pad_len = range(coords[1] + size[1] - cur_y)
            if row >= cur_x:
                pad_len = range(coords[1] + size[1] - 1)
            for _ in pad_len:
                source_matrix[row].append(0)

    for row in range(coords[0], coords[0] + size[0]):
        for col in range(coords[1], coords[1] + size[1]):
            if row >= coords[0] and col >= coords[1]:
                source_matrix[row][col] += 1


def parse_cut(string):
    res = re.search(r'^#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)', string)
    if not res:
        return None
    return ElfSquare(res[1], [int(res[2]), int(res[3])], [int(res[4]), int(res[5])])


def puzzle1(strings):
    matrix = [[0]]
    elf_squares = []
    for string in strings:
        elf_square = parse_cut(string)
        elf_squares.append(elf_square)
        if not elf_square:
            continue
        add_to_matrix(matrix, elf_square.coords, elf_square.size)

    count = 0
    for row in matrix:
        for val in row:
            if val > 1:
                count += 1
    print(count)


def puzzle2(strings):
    matrix = [[0]]
    elf_squares = []
    for string in strings:
        elf_square = parse_cut(string)
        elf_squares.append(elf_square)
        if not elf_square:
            continue
        add_to_matrix(matrix, elf_square.coords, elf_square.size)

    print("done compiling matrix")
    for square in elf_squares:
        matches = True
        for col in matrix[square.coords[0]:square.coords[0] + square.size[0]]:
            in_square = col[square.coords[1]:square.coords[1] + square.size[1]]
            if sum(in_square) != len(in_square):
                matches = False
                break
        if matches:
            print(square.id)


#strings = '''
##1 @ 1,3: 4x4
##2 @ 3,1: 4x4
##3 @ 5,5: 2x2
#'''
#puzzle1(strings.splitlines())

with open('3.txt') as f:
    puzzle2(f.readlines())
