from collections import deque
from itertools import islice
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def is_valid_number(current_numbers, new_number):
    for i, c in enumerate(current_numbers):
        for c2 in islice(current_numbers, i + 1, None):
            if c + c2 == new_number:
                return True
    return False


def find_first_invalid_number(lines: List[str], preamble_size=25):
    current_numbers = deque((int(s) for s in lines[:preamble_size]), preamble_size)
    for incoming_number in (int(s) for s in lines[preamble_size:]):
        if is_valid_number(current_numbers, incoming_number):
            current_numbers.append(incoming_number)
        else:
            return incoming_number


def find_summing_numbers(lines: List[str], preamble_size=25):
    target_number = find_first_invalid_number(lines, preamble_size)
    l = [int(s) for s in lines]

    # Increase numbers until we are equal to or above the target

    start = 0
    while True:
        sum = 0
        index = start
        while sum < target_number:
            sum += l[index]
            index += 1

        if sum == target_number:
            return min(l[start:index]) + max(l[start:index])
        else:
            start += 1


def part_1():
    return find_first_invalid_number(read_lines('input.txt'))


def part_2():
    return find_summing_numbers(read_lines('input.txt'))


assert_test(find_first_invalid_number(test_input, 5), 127, 1)
assert_test(find_summing_numbers(test_input, 5), 62, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
