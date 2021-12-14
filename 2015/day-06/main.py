import re
from typing import List

import numpy as np

from util import read_lines

test_input = read_lines("input_test.txt")


def to_action(line):
    p = re.split(r' |,', line)
    return p[1], int(p[-5]), int(p[-4]), int(p[-2])+1, int(p[-1])+1


def count_lights(lines: List[str]):
    lights = np.zeros((1000, 1000), np.int32)
    for line in lines:
        action, x1, y1, x2, y2 = to_action(line)
        if action == 'on':
            lights[x1:x2, y1:y2] = 1
        elif action == 'off':
            lights[x1:x2, y1:y2] = 0
        else:
            lights[x1:x2, y1:y2] = 1 - lights[x1:x2, y1:y2]

    return np.sum(lights)


def count_lights_v2(lines: List[str]):
    lights = np.zeros((1000, 1000), np.int32)
    for line in lines:
        action, x1, y1, x2, y2 = to_action(line)
        if action == 'on':
            lights[x1:x2, y1:y2] += 1
        elif action == 'off':
            lights[x1:x2, y1:y2] = (lights[x1:x2, y1:y2]-1).clip(min=0)
        else:
            lights[x1:x2, y1:y2] += 2

    return np.sum(lights)


def part_1():
    return count_lights(read_lines('input.txt'))


def part_2():
    return count_lights_v2(read_lines('input.txt'))


print("result for day-1:", part_1())
print("result for day-2:", part_2())
