from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def operate(v, x, op):
    # print(v, op, x)
    if op == '+':
        ret = v + x
    elif op == '*':
        ret = v * x

    return ret


def eval_expr(line: str) -> (int, int):
    current = 0
    i = 0

    op = '+'
    while i < len(line):
        c = line[i]
        if c == '(':
            res, l = eval_expr(line[i + 1:])
            i += l
            current = operate(current, res, op)
        elif c == " ":
            pass
        elif '0' <= c <= '9':
            current = operate(current, int(c), op)
        elif c == '+' or c == '*':
            op = c
        elif c == ")":
            return current, i + 1
        i += 1

    return current, i


def e(stack) -> int:
    i = 0
    while i < len(stack):
        # print(stack[i])
        if stack[i] == '+':
            stack.pop(i)  # Remove +
            # print("ab", stack[i - 1])
            stack[i - 1] += stack.pop(i)
            # print("ab", stack[i - 1])
        else:
            i += 1

    p = 1
    for s in stack[::2]:
        p *= s
    return p


def eval_expr_v2(line: str) -> (int, int):
    i = 0
    stack = []
    while i < len(line):
        c = line[i]
        if c == '(':
            res, l = eval_expr_v2(line[i + 1:])
            i += l
            stack.append(res)
        elif c == ")":
            # EVAL HERE

            return e(stack), i + 1
        elif '0' <= c <= '9':
            stack.append(int(c))
        elif c == '+' or c == '*':
            stack.append(c)
        i += 1

    return e(stack), i


def foobar(lines: List[str]):
    return sum(eval_expr(line)[0] for line in lines)


def foobar_v2(lines: List[str]):
    return sum(eval_expr_v2(line.replace(' ', ''))[0] for line in lines)


def part_1():
    return foobar(read_lines('input.txt'))


def part_2():
    return foobar_v2(read_lines('input.txt'))


assert_test(foobar(test_input), 26 + 437 + 12240 + 13632, 1)
assert_test(foobar_v2(test_input), 46 + 1445 + 669060 + 23340, 2)

print("result for day-1:", part_1())
print("result for day-2:", part_2())
