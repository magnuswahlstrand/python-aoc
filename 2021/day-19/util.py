from typing import List


def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read()


def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def assert_test(actual, expected, day):
    if actual == expected:
        print(f"test result for day-{day} is: {actual} as expected")
    else:
        print(f"ERROR: test result for day-{day} not as expected. {actual} != {expected}")


def print_grid(grid, pos_highlight=[], val_highlight=[]):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c in val_highlight:
                print(f'\x1b[6;30;42m{c}\x1b[0m', end='')
            elif (x, y) in pos_highlight:
                print(f'\x1b[6;30;42m{c}\x1b[0m', end='')
            else:
                print(c, end='')
        print()


def neighbors(o, size):
    x1, y1 = max(o[0] - 1, 0), max(o[1] - 1, 0)
    x2, y2 = min(o[0] + 2, size[0]), min(o[1] + 2, size[1])
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (x, y) != o:
                yield x, y


def neighbors_manhattan(o, size):
    for c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x, y = o[0] + c[0], o[1] + c[1]
        if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
            continue

        yield x, y


### Candidates

import numpy as np


# https://www.cs.helsinki.fi/group/goa/mallinnus/3dtransf/3drot.html
def rot_z(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (-y, x, z)

    # x' = x*cos q - y*sin q
    # y' = x*sin q + y*cos q
    # z' = z
    return np.array((x, y, z))


def rot_x(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (x, -z, y)

    # y' = y*cos q - z*sin q
    # z' = y*sin q + z*cos q
    # x' = x
    return np.array((x, y, z))


def rot_y(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (z, y, -x)

    # z' = z*cos q - x*sin q
    # x' = z*sin q + x*cos q
    # y' = y
    return np.array((x, y, z))
