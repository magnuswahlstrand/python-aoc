from collections import defaultdict

from util import read_input, assert_test

test_input = read_input("input_test.txt")

moves = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}


def count_houses(_input: str):
    d = defaultdict(int)
    c = (0, 0)
    d[c] += 1
    for v in _input:
        m = moves[v]
        c = (c[0] + m[0], c[1] + m[1])
        d[c] += 1

    return len(d.keys())


def count_houses_v2(_input: str):
    d = defaultdict(int)
    c = (0, 0)
    d[c] += 1
    for v in _input[::2]:
        m = moves[v]
        c = (c[0] + m[0], c[1] + m[1])
        d[c] += 1

    c = (0, 0)
    d[c] += 1
    for v in _input[1::2]:
        m = moves[v]
        c = (c[0] + m[0], c[1] + m[1])
        d[c] += 1

    return len(d.keys())


def part_1():
    return count_houses(read_input('input.txt'))


def part_2():
    return count_houses_v2(read_input('input.txt'))


assert_test(count_houses(test_input), 2, 1)
# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
