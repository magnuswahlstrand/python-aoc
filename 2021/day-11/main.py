from itertools import product
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def neighbors(o, size):
    x1, y1 = max(o[0] - 1, 0), max(o[1] - 1, 0)
    x2, y2 = min(o[0] + 2, size), min(o[1] + 2, size)
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (x, y) != o:
                yield x, y


def count_flashes(lines: List[str]):
    return simulate_octopus(lines)[0]


def simulate_octopus(lines, run_until_sync=False):
    steps = 1000 if run_until_sync else 100

    octo_map = [list(map(int, line)) for line in lines]
    size = len(octo_map)
    coords = list(product(range(size), repeat=2))

    # First increase
    count = 0
    for step in range(steps):
        flashing = []
        for c in coords:
            octo_map[c[1]][c[0]] += 1
            if octo_map[c[1]][c[0]] > 9:
                flashing.append(c)

        # Then flash & spread
        while len(flashing) > 0:
            count += len(flashing)
            next_round = []
            for o in flashing:
                for n in neighbors(o, size=size):
                    octo_map[n[1]][n[0]] += 1
                    if octo_map[n[1]][n[0]] == 10:
                        next_round.append(n)
            flashing = next_round

        # Finally change 9s to 0
        for c in coords:
            if octo_map[c[1]][c[0]] > 9:
                octo_map[c[1]][c[0]] = 0

        if run_until_sync:
            s = sum(sum(row) for row in octo_map)
            print("sum", s, step)
            if s == 0:
                return -1, step + 1
    return count, -1


def find_sync(lines: List[str]):
    return simulate_octopus(lines, run_until_sync=True)[1]


def part_1():
    return count_flashes(read_lines('input.txt'))


def part_2():
    return find_sync(read_lines('input.txt'))


assert_test(count_flashes(test_input), 1656, 1)
assert_test(find_sync(test_input), 195, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
