from collections import defaultdict
from typing import List

from util import assert_test

input = [6, 4, 12, 1, 20, 0, 16]


def find_number_on_turn(starting_number: List[str], max_turn=2020):
    seen = set(starting_number[:-1])
    previous_to_last_time = defaultdict(int)

    turn = 0
    for i, n in enumerate(starting_number):
        turn += 1
        previous_to_last_time[n] = turn

    previous = starting_number[-1]
    while turn < max_turn:
        turn += 1
        v = previous_to_last_time[previous]
        if v == 0:
            new = 0
        else:
            new = turn - 1 - v

        # Update for last round
        previous_to_last_time[previous] = turn - 1
        previous = new
        if turn % 3000000 == 0:
            print(turn)

    return new


def part_1():
    return find_number_on_turn(input)


def part_2():
    return find_number_on_turn(input, 30000000)


assert_test(find_number_on_turn([0, 3, 6]), 436, 1)
assert_test(find_number_on_turn([1, 3, 2]), 1, 1)
assert_test(find_number_on_turn([2, 1, 3]), 10, 1)
assert_test(find_number_on_turn([1, 2, 3]), 27, 1)
assert_test(find_number_on_turn([2, 3, 1]), 78, 1)
assert_test(find_number_on_turn([3, 2, 1]), 438, 1)
assert_test(find_number_on_turn([3, 1, 2]), 1836, 1)
print("result for day-1:", part_1())
# assert_test(find_number_on_turn([0, 3, 6], 30000000), 175594, 1)
print("result for day-2:", part_2())
