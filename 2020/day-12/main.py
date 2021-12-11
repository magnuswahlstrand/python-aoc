import re

import numpy as np

from util import read_input, assert_test

test_input = read_input("input_test.txt")

directions = {
    'N': np.array((0, -1)),
    'S': np.array((0, 1)),
    'E': np.array((1, 0)),
    'W': np.array((-1, 0)),
}

rotations = {
    (1, 0): np.array((0, 1)),
    (0, 1): np.array((-1, 0)),
    (-1, 0): np.array((0, -1)),
    (0, -1): np.array((1, 0)),
}


def ship_distance(_input: str):
    pos = np.array((0, 0))
    dir = np.array((1, 0))
    for c, val in ((c, int(d)) for c, d in re.findall(r'([NSEWLRF])(\d+)', _input)):
        if c in directions:
            pos += directions[c] * val
        elif c == 'F':
            pos += dir * val
        elif c == 'R' or c == 'L':
            deg = val if c == 'R' else 360 - val
            for v in range(int(deg / 90)):
                dir = np.array((-dir[1], dir[0]))

    return sum(pos)


def waypoint_distance(_input: str):
    waypoint = np.array((10, -1))
    ship = np.array((0, 0))
    for c, val in ((c, int(d)) for c, d in re.findall(r'([NSEWLRF])(\d+)', _input)):
        if c in directions:
            waypoint += directions[c] * val
        elif c == 'F':
            ship += waypoint * val
        elif c == 'R' or c == 'L':
            deg = val if c == 'R' else 360 - val
            for v in range(int(deg / 90)):
                waypoint = np.array((-waypoint[1], waypoint[0]))

    return sum(ship)


def part_1():
    return ship_distance(read_input('input.txt'))


def part_2():
    return waypoint_distance(read_input('input.txt'))


assert_test(ship_distance(test_input), 25, 1)
assert_test(waypoint_distance(test_input), 286, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
