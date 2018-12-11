from operator import add, sub
from collections import namedtuple
import re


class Point:
    def __init__(self, initial_pos, vector):
        self.pos = [int(x) for x in initial_pos]
        self.vector = [int(x) for x in vector]

    def reverse(self):
        self.pos = list(map(sub, self.pos, self.vector))

    def travel(self):
        self.pos = list(map(add, self.pos, self.vector))

    def __repr__(self):
        return f'pos: {self.pos}, vector: {self.vector}'


test_input = '''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
'''


def find_line(points):
    subsequent_points = 0
    for point in points:
        for p in points:
            if point.pos[1] == p.pos[1] and abs(p.pos[0] - point.pos[0]) == 1:
                subsequent_points += 1
            if subsequent_points > 10:
                return True
    return False


def calculate_area(points):
    min_x = min(p.pos[0] for p in points)
    min_y = min(p.pos[1] for p in points)
    max_x = max(p.pos[0] for p in points)
    max_y = max(p.pos[1] for p in points)
    return (max_x - min_x) * (max_y - min_y)


def puzzle1(strings):
    points = []
    for string in strings:
        res = re.search(r'^position=<([^>]+)> velocity=<([^>]+)>$', string.strip())
        points.append(Point(res[1].split(','), res[2].split(',')))

    seconds_travelled = 0
    current_area = calculate_area(points)
    previous_area = current_area + 1
    while(current_area < previous_area):
        for point in points:
            point.travel()
        seconds_travelled += 1
        previous_area = current_area
        current_area = calculate_area(points)
    print(f"seconds travelled: {seconds_travelled-1}")

    for point in points:
        point.reverse()
    min_x = min(p.pos[0] for p in points)
    min_y = min(p.pos[1] for p in points)
    max_x = max(p.pos[0] for p in points)
    max_y = max(p.pos[1] for p in points)
    base_y = ['.'] * (max_y + 1 - min_y)
    matrix = [list(base_y) for _ in range(min_x, max_x + 1)]
    for point in points:
        matrix[point.pos[0] - min_x][point.pos[1] - min_y] = '#'

    for row in matrix:
        print(''.join(row))


puzzle1(test_input.splitlines())

with open('10.txt') as f:
    puzzle1(f.readlines())
