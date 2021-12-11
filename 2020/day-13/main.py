from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def first_bus(lines: List[str]):
    ts = int(lines[0])
    buses = [int(b) for b in lines[1].split(',') if b != 'x']
    v = min(((b - ts % b), b) for b in buses)
    return v[0] * v[1]


# I had to look up my Go-solution for this one :D
def chinese_reminder_bus(lines):
    buses = [(int(b), i) for i, b in enumerate(lines[1].split(',')) if b != 'x']

    factor = 1
    timestamp = 0
    for bus, i in buses:
        while (timestamp + i) % bus != 0:
            timestamp += factor
        factor *= bus
    return timestamp


def part_1():
    return first_bus(read_lines('input.txt'))


def part_2():
    return chinese_reminder_bus(read_lines('input.txt'))


assert_test(first_bus(test_input), 295, 1)
assert_test(chinese_reminder_bus(test_input), 1068781, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
