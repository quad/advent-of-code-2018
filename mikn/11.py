from operator import itemgetter
import numpy
import math


def puzzle1(grid_serial, size_x=300, size_y=300, print_coord=None):
    matrix = numpy.empty(shape=(size_x,size_y), dtype=numpy.int8)
    for x in range(size_x):
        for y in range(size_y):
            rack_id = x + 1 + 10
            if print_coord and x == print_coord[0] - 1 and y == print_coord[1] - 1:
                print(print_coord)
                print(rack_id)
                power = rack_id * (y + 1)
                print(power)
                power = power + grid_serial
                print(power)
                power = power * rack_id
                print(power)
                power = math.floor(power / 100) % 10
                print(power)
                power = power - 5
                print(power)
                print("calc")
                print(math.floor(((rack_id * (y + 1) + grid_serial) * rack_id) / 100) % 10 - 5)
            # MATH
            matrix[x,y] = (math.floor(((rack_id * (y + 1) + grid_serial) * rack_id) / 100) % 10 - 5)
    #highest_value = (0, 0, 0, 0)
    highest_value = []
    for size in range(1, 300):
        print('current size: {size}'.format(size=size))
        sums = []
        for x in range(size_x - size):
            for y in range(size_y - size):
                 sums.append((x + 1, y + 1, numpy.sum(matrix[x:x+size,y:y+size])))
        sums.sort(key=itemgetter(2))
        high_score = (size, sums.pop())
        print(high_score)
        highest_value.append(high_score)
    highest_value.sort(key=itemgetter(1))
    if print_coord:
        x = print_coord[0] - 2
        y = print_coord[1] - 2
        pass
    print(highest_value)


#puzzle1(8, print_coord=(3, 5))
#puzzle1(18, print_coord=(33, 45))
#puzzle1(18, print_coord=(33, 45))
#puzzle1(57, print_coord=(122, 79))
#puzzle1(39, print_coord=(217, 196))
#puzzle1(71, print_coord=(101, 153))
puzzle1(1955, size_x=300, size_y=300)
