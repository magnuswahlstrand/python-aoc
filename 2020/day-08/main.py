from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def perform_operation(current, acc, op, val):
    if op == 'nop':
        return current + 1, acc
    elif op == 'jmp':
        return current + val, acc
    elif op == 'acc':
        return current + 1, acc + val
    else:
        raise ValueError("unexpected operation", op)


def find_loop_inner(operations):
    visited = set()
    current, acc = 0, 0
    while current not in visited:
        visited.add(current)
        op, val = operations[current]
        current, acc = perform_operation(current, acc, op, val)
        if current == len(operations):
            return acc, True
    return acc, False


def find_loop(input: List[str]):
    operations = [(s[:3], int(s[3:])) for s in input]
    return find_loop_inner(operations)


def fix_loop(input: List[str]):
    operations = [(s[:3], int(s[3:])) for s in input]
    for i, op in enumerate(operations):

        if op[0] == 'acc':
            continue

        operations[i] = ('jmp', op[1]) if op[0] == 'nop' else ('nop', op[1])
        acc, end_found = find_loop_inner(operations)
        operations[i] = op
        if end_found:
            return acc


def part_1():
    return find_loop(read_lines("input.txt"))[0]


def part_2():
    return fix_loop(read_lines("input.txt"))


assert_test(find_loop(test_input)[0], 5, 1)
assert_test(fix_loop(test_input), 8, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
