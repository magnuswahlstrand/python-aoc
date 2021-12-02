from functools import reduce
from typing import List

from util import read_lines, assert_test


def to_coordinates(instruction: str, amount: str):
    a = int(amount)
    if instruction == 'forward':
        return a, 0
    elif instruction == 'down':
        return 0, a
    elif instruction == 'up':
        return 0, -a
    else:
        raise ValueError(f"unexpected instruction {instruction}")


def part_1():
    return calculate_product("input.txt")

def part_2():
    return calculate_product_v2("input.txt")


def parse_instructions(lines: List[str]):
    return (to_coordinates(*line.split()) for line in lines)


def calculate_product(filename: str):
    lines = read_lines(filename)
    instructions = parse_instructions(lines)
    final_coords = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), instructions)
    return final_coords[0] * final_coords[1]


def calculate_product_v2(filename: str):
    lines = read_lines(filename)
    instructions = parse_instructions(lines)
    x, y, aim = 0, 0, 0
    for i in instructions:
        aim += i[1]
        x += i[0]
        y += aim * i[0]

    return x * y


assert_test(calculate_product('input_test.txt'), 150, 1)
assert_test(calculate_product_v2('input_test.txt'), 900, 1)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
