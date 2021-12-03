import operator
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def power_consumption(numbers: List[str]):
    most_common = list(
        sum(line[x] == "1" for line in numbers) >= ((len(numbers) + 1) / 2) for x in range(len(numbers[0])))
    gamma = ["1" if s else "0" for s in most_common]
    epsilon = ["0" if s else "1" for s in most_common]
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def life_support_rating(numbers: List[str]):
    number_length = len(numbers[0])
    return find_best_match(numbers, number_length) * find_best_match(numbers, number_length, op=operator.not_)


def noop(x):
    return x


def find_best_match(numbers: List[str], number_length, op=noop):
    for x in range(number_length):
        count_numbers = int((len(numbers) + 1) / 2)
        one_is_most_common = "".join(number[x] for number in numbers).count("1") >= count_numbers
        required_digit = "1" if op(one_is_most_common) else "0"

        numbers = [number for number in numbers if number[x] == required_digit]

        if len(numbers) == 1:
            return int(numbers[0], 2)

    raise Exception("something went wrong")


def part_1():
    return power_consumption(read_lines("input.txt"))


def part_2():
    return life_support_rating(read_lines("input.txt"))


assert_test(power_consumption(test_input), 198, 1)
assert_test(life_support_rating(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
