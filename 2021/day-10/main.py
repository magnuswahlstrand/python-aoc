from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")

lefties = set("[({<")
righties = set(")]>}")

mirror = {
    ")": "(",
    "]": "[",
    ">": "<",
    "}": "{",
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}

score = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def find_first_invalid(line: str):
    stack = []
    for c in line:
        if c in lefties:
            stack.append(c)
        else:
            if stack[-1] == mirror[c]:
                # print("ok", stack.pop())
                stack.pop()
            else:
                # print("error!", c)
                return c
    if len(stack) != 0:
        return ""

    return ""


def return_remaining_stack(line: str):
    stack = []
    for c in line:
        if c in lefties:
            stack.append(c)
        else:
            if stack[-1] == mirror[c]:
                # print("ok", stack.pop())
                stack.pop()
            else:
                return -1
                # print("error!", c)
    if len(stack) != 0:
        return stack


def score_lines(lines: List[str]):
    return sum(score[find_first_invalid(line)] for line in lines)


score_v2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def score_lines_v2(lines: List[str]):
    autocomplete_lines = [list(reversed([mirror[s] for s in stack])) for stack in
                          (return_remaining_stack(line) for line in lines) if stack != -1]

    score = []
    for stack in autocomplete_lines:
        s = 0
        for c in stack:
            s = 5 * s + score_v2[c]
        score.append(s)

    score.sort()
    return score[int(len(score) / 2)]


def part_1():
    return score_lines(read_lines('input.txt'))


def part_2():
    return score_lines_v2(read_lines('input.txt'))


assert find_first_invalid('{([(<{}[<>[]}>{[]{[(<()>') == '}'
assert find_first_invalid('[[<[([]))<([[{}[[()]]]') == ')'
assert find_first_invalid('[{[{({}]{}}([{[{{{}}([]') == ']'
assert find_first_invalid('{([<><>])}') == ''

assert_test(score_lines(test_input), 26397, 1)
assert_test(score_lines_v2(test_input), 288957, 1)
print("result for day-1:", part_1())

print("result for day-2:", part_2())
