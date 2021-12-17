from collections import namedtuple

import numpy as np

from util import assert_test

test_input = "target area: x=20..30, y=-10..-5"
_input = "target area: x=96..125, y=-144..-98"

Target = namedtuple("Target", "x_min x_max y_min y_max")


def parse_target(target_raw):
    t = [[int(x) for x in p.split('..')] for p in target_raw[15:].split(', y=')]
    return Target(*t[0], *t[1])


def find_max_y(target_raw: str):
    target = parse_target(target_raw)
    for vy in range(300, -10, -1):
        ok, res = sweep_x(vy, target)
        if ok:
            return res[3]


def count_all_v(target_raw: str):
    target = parse_target(target_raw)
    count = 0
    for vy in range(300, target.y_min - 1, -1):
        c = len(sweep_x_v2(vy, target))
        count += c

    return count


def sweep_x(vy, target):
    results = []
    for vx in range(1, 100):
        p = np.array((0, 0))
        v = np.array((vx, vy))
        maxy = p[1]
        for i in range(200):
            p += v
            maxy = max(maxy, p[1])
            drag = (-1 if v[0] > 0 else 1) if v[0] != 0 else 0
            v += (drag, -1)

            left_of = p[0] < target.x_min
            right_of = p[0] > target.x_max
            above = p[1] > target.y_max
            below = p[1] < target.y_min
            if right_of:
                if above:
                    return False, -1
                else:
                    break

            if below:
                break

            if not above and not left_of:
                return True, (vx, vy, i, maxy)

            results.append((vx, vy))

    return False, 1


def sweep_x_v2(vy, target):
    results = []
    for vx in range(1, target.x_max + 1):
        p = np.array((0, 0))
        v = np.array((vx, vy))
        for i in range(600):
            p += v
            drag = (-1 if v[0] > 0 else 1) if v[0] != 0 else 0
            v += (drag, -1)

            left_of = p[0] < target.x_min
            right_of = p[0] > target.x_max
            above = p[1] > target.y_max
            below = p[1] < target.y_min
            if right_of:
                if above:
                    return results
                else:
                    break

            if below:
                break

            if not above and not left_of:
                results.append((vx, vy))
                break

    return results


def part_1():
    return find_max_y(_input)


def part_2():
    return count_all_v(_input)


assert_test(find_max_y(test_input), 45, 1)
assert_test(count_all_v(test_input), 112, 1)
# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())  # 244, 2283 too low
