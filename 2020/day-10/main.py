from collections import namedtuple
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")

Charger = namedtuple('Charger', 'val index')


def jolt_difference_product(lines: List[str]):
    chargers = setup(lines)

    ones, threes = 0, 0
    for i in range(len(chargers) - 1):
        diff = chargers[i + 1].val - chargers[i].val
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    return ones * threes


def jolt_arrangements(lines: List[str]):
    chargers = setup(lines)
    cache = {chargers[-1]: 1}
    return total_combinations(chargers, chargers[0], cache)


def total_combinations(chargers, current, cache):
    if current.val in cache:
        return cache[current.val]

    # Only look at the next 3 chargers, and select those that are valid
    connections = [c for c in chargers[current.index + 1:current.index + 4] if c.val <= current.val + 3]

    s = sum(total_combinations(chargers, c, cache) for c in connections)
    cache[current.val] = s
    return s


def setup(lines):
    chargers = sorted(int(s) for s in lines + [0])
    chargers.append(chargers[-1] + 3)
    return [Charger(c, i) for i, c in enumerate(chargers)]


def part_1():
    return jolt_difference_product(read_lines('input.txt'))


def part_2():
    return jolt_arrangements(read_lines('input.txt'))


assert_test(jolt_difference_product(test_input), 220, 1)
assert_test(jolt_arrangements(test_input), 19208, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
