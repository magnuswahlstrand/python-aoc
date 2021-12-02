from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")

toBinary = str.maketrans({
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1'
})


def parse_boarding_card(boarding_card: str):
    b = boarding_card.translate(toBinary)
    row = int(b[:7], 2)
    column = int(b[7:], 2)
    return row, column, (row * 8 + column)


def find_max_id(lines: List[str]):
    return max(parse_boarding_card(boarding_card)[2] for boarding_card in lines)


def part_1():
    return find_max_id(read_lines("input.txt"))


def part_2():
    lines = read_lines("input.txt")
    boarding_cards = set([parse_boarding_card(boarding_card)[2] for boarding_card in lines])
    mn = min(boarding_cards)
    mx = max(boarding_cards)
    for b in range(mn, mx + 1, 1):
        if b not in boarding_cards:
            return b

    raise ValueError("not found")


assert_test(find_max_id(test_input), 820, 1)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
