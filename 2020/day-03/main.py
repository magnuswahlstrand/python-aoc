from typing import List

from util import read_input

test_input = read_input("input_test.txt")


def coordinates(height, x_step, y_step):
    return ((x, y) for x, y in zip(range(0, height * x_step, x_step), range(0, height, y_step)))


def count_trees(input: List[str], x_step=3, y_step=1):
    map_height = len(input)
    xys = coordinates(map_height, x_step, y_step)

    map_width = len(input[0])
    return sum(input[y][x % map_width] == "#" for x, y in xys)


def count_multiple_trees(input):
    return count_trees(input, 1, 1) * count_trees(input, 3, 1) * \
           count_trees(input, 5, 1) * count_trees(input, 7, 1) * \
           count_trees(input, 1, 2)


def part_1():
    return count_trees(read_input("input.txt"))


def part_2():
    return count_multiple_trees(read_input("input.txt"))


test_count = count_trees(test_input)
assert test_count == 7
print("result for day-1 test is:", test_count, "as expected")

test_count2 = count_multiple_trees(test_input)
assert test_count2 == 336
print("result for day-2 test is:", test_count2, "as expected")

print("result for day-1:", part_1())
print("result for day-2:", part_2())
