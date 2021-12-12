from typing import List

from util import read_lines

test_input = read_lines("input_test.txt")


def wrapping_paper(lines: List[str]):
    return sum(2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l) for line in lines for (l, w, h) in
               [map(int, line.split('x'))])


def ribbon(lines: List[str]):
    return sum(2 * sum(sorted((l, w, h))[:2]) + w * l * h for line in lines for (l, w, h) in
               [map(int, line.split('x'))])


def part_1():
    return wrapping_paper(read_lines('input.txt'))


def part_2():
    return ribbon(read_lines('input.txt'))


# assert_test(foobar(test_input), 198, 1)
# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
