from util import assert_test

test_input = """.#.
..#
###"""

input = """.#.#.#..
..#....#
#####..#
#####..#
#####..#
###..#.#
#..##.##
#.#.####"""

import numpy as np


def foo(_input: str):
    start = np.array([[1 if c == '#' else 0 for c in line] for line in _input.split('\n')])
    s = np.array((1, *start.shape)) + 10 * 2
    m = np.zeros(s)

    c1 = 10 + round(start.shape[0] / 2)
    c2 = c1 + start.shape[0]
    m[10, c1:c2, c1:c2] = start

    n = m.copy()
    print(np.sum(m))
    for _ in range(6):
        for z in range(len(m)):
            for y in range(len(m[0])):
                for x in range(len(m[0, 0])):
                    t = (z, y, x)
                    i = np.array(t)
                    z1, y1, x1, z2, y2, x2 = *(i - 1).clip(min=0), *(i + 2)
                    current = m[t]
                    neighbors = np.count_nonzero(m[z1:z2, y1:y2, x1:x2]) - current

                    if current == 1 and (neighbors == 2 or neighbors == 3):
                        n[t] = 1
                    elif current == 0 and neighbors == 3:
                        n[t] = 1
                    else:
                        n[t] = 0
        m, n = n, m
        print(np.sum(m))

    return np.sum(m)


def foo2(_input: str):
    start = np.array([[1 if c == '#' else 0 for c in line] for line in _input.split('\n')])
    s = np.array((1, 1, *start.shape)) + 10 * 2
    m = np.zeros(s)

    c1 = 10 + round(start.shape[0] / 2)
    c2 = c1 + start.shape[0]

    m[10, 10, c1:c2, c1:c2] = start

    n = m.copy()
    print(np.sum(m))
    for _ in range(6):
        for w in range(len(m)):
            for z in range(len(m[0])):
                for y in range(len(m[0, 0])):
                    for x in range(len(m[0, 0, 0])):
                        t = (w, z, y, x)
                        i = np.array(t)
                        w1, z1, y1, x1, w2, z2, y2, x2 = *(i - 1).clip(min=0), *(i + 2)

                        current = m[t]
                        neighbors = np.count_nonzero(m[w1:w2, z1:z2, y1:y2, x1:x2]) - current

                        if current == 1 and (neighbors == 2 or neighbors == 3):
                            n[t] = 1
                        elif current == 0 and neighbors == 3:
                            n[t] = 1
                        else:
                            n[t] = 0
        m, n = n, m
        print(np.sum(m))

    return np.sum(m)


def part_1():
    return foo(input)


def part_2():
    return foo2(input)


assert_test(foo(test_input), 112, 1)
assert_test(foo2(test_input), 848, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
