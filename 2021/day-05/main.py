import re
from collections import defaultdict, namedtuple
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")

pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')


def setup(lines):
    d = defaultdict(lambda: 0)
    Range = namedtuple('Range', 'x1 y1 x2 y2 dx dy')
    # Setup
    ranges = []
    for line in lines:
        for match in re.findall(pattern, line):
            c = [int(x) for x in match]
            dx = 1 if c[0] <= c[2] else -1
            dy = 1 if c[1] <= c[3] else -1
            ranges.append(Range(c[0], c[1], c[2], c[3], dx, dy))

    return d, ranges


def find_ridges(lines: List[str], count_diagonal=False):
    d, ranges = setup(lines)

    # Calc
    for r in ranges:
        if r.x1 == r.x2:
            for y in range(r.y1, r.y2 + r.dy, r.dy):
                d[(r.x1, y)] += 1
        elif r.y1 == r.y2:
            for x in range(r.x1, r.x2 + r.dx, r.dx):
                d[(x, r.y1)] += 1
        elif count_diagonal:
            for v in range(0, abs(r.x1 - r.x2) + 1):
                d[(r.x1 + v * r.dx, r.y1 + v * r.dy)] += 1

    return sum(v > 1 for v in d.values())


def print_map(d):
    for y in range(0, 10):
        for x in range(0, 10):
            v = d[(x, y)]
            if v > 0:
                print(v, end='')
            else:
                print('.', end='')
        print()


def part_1():
    return find_ridges(read_lines('input.txt'))


def part_2():
    return find_ridges(read_lines('input.txt'), count_diagonal=True)


assert_test(find_ridges(test_input), 5, 1)
assert_test(find_ridges(test_input, True), 12, 1)
# assert_test(life_support_rating(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
