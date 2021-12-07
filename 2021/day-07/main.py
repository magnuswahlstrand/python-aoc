from collections import namedtuple
from statistics import median

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def eval_pos(crabs, x):
    return CrabPosition(sum(abs(c - x) for c in crabs), x)


def eval_pos_v2(crabs, x):
    return CrabPosition(sum(int(n * (n + 1) / 2) for n in (abs(c - x) for c in crabs)), x)


CrabPosition = namedtuple("CrabPosition", "energy x")


def find_horizontal_position_v2(input: str):
    crabs = tuple(map(int, input.split(",")))
    x = int(median(crabs))  # Good starting point

    left, right, current = eval_pos_v2(crabs, x - 1), eval_pos_v2(crabs, x + 1), eval_pos_v2(crabs, x)
    direction, next = (1, right) if left > right else (-1, left)
    while next.energy < current.energy:
        current = next
        next = eval_pos_v2(crabs, current.x + direction)

    return eval_pos_v2(crabs, current.x).energy


def find_horizontal_position(input: str):
    crabs = tuple(map(int, input.split(",")))
    x = int(median(crabs))
    return eval_pos(crabs, x).energy


def part_1():
    return find_horizontal_position(read_lines('input.txt')[0])


def part_2():
    return find_horizontal_position_v2(read_lines('input.txt')[0])


assert_test(find_horizontal_position(test_input[0]), 37, 1)
assert_test(find_horizontal_position_v2(test_input[0]), 168, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
