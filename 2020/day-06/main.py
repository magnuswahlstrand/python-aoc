from collections import Counter
from typing import List

from util import read_input, assert_test

test_input = read_input("input_test.txt")


def sum_of_yes_per_group(input: List[str]):
    return sum([len(set(group.replace('\n', ''))) for group in input.split('\n\n')])


def sum_of_identical_yes_per_group(input: List[str]):
    # Wow, this is stupid :D
    return sum((len([c for c in count if c == max_count])
                for (count, max_count) in
                ((Counter(group.replace('\n', '')).values(), len(group.split()))
                 for group in input.split('\n\n'))))


def part_1():
    return sum_of_yes_per_group(read_input("input.txt"))


def part_2():
    return sum_of_identical_yes_per_group(read_input("input.txt"))


assert_test(sum_of_yes_per_group(test_input), 11, 1)
assert_test(sum_of_identical_yes_per_group(test_input), 6, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
