from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")
test_input_2 = read_lines("input_test_2.txt")

memPattern = r'\d+'


def find_sum(lines: List[str]):
    one_mask, zero_mask = 0, 0
    register = {}
    for line in lines:
        left, right = line.split(" = ", maxsplit=2)
        if left == 'mask':
            one_mask = sum(1 << (35 - i) for i, v in enumerate(right) if v == '1')
            zero_mask = sum(1 << (35 - i) for i, v in enumerate(right) if v != '0')
        else:
            pos = int(left[4:-1])
            register[pos] = (int(right) | one_mask) & zero_mask

    return sum(register.values())


def find_permutations(mask: str, index: int, addr: str):
    if index == len(mask):
        return [0]

    out = []
    if mask[index] == 'X':
        current = 1 << (len(mask) - index - 1)
        for r in find_permutations(mask, index + 1, addr):
            out.append(current + r)
            out.append(r)
    elif mask[index] == '1':
        current = 1 << (len(mask) - index - 1)
        for r in find_permutations(mask, index + 1, addr):
            out.append(current + r)
    elif mask[index] == '0':
        current = int(addr[index]) << (len(mask) - index - 1)
        for r in find_permutations(mask, index + 1, addr):
            out.append(current + r)

    return out


def find_sum_v2(lines: List[str]):
    register = {}
    for line in lines:
        left, right = line.split(" = ", maxsplit=2)
        if left == 'mask':
            mask = right
        else:

            pos = int(left[4:-1])
            addr = bin(pos)[2:].zfill(36)
            permutations = find_permutations(mask, 0, addr)
            for p in permutations:
                register[p] = int(right)

    return sum(register.values())


def part_1():
    return find_sum(read_lines('input.txt'))


def part_2():
    return find_sum_v2(read_lines('input.txt'))


assert_test(find_sum(test_input), 165, 1)
assert_test(find_sum_v2(test_input_2), 208, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
