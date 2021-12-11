from typing import List

import numpy as np
import scipy.ndimage.filters as filters

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")

footprint = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])


def find_minima(lines: List[str]):
    data = np.array([[int(col) for col in row] for row in lines])
    data_min = filters.minimum_filter(data, footprint=footprint, mode='mirror')
    minima = (data < data_min)
    return ((data + 1) * minima).sum(), minima, data


def find_minima_part_1(lines: List[str]):
    res, _, _ = find_minima(lines)
    return res


neighbor_directions = np.array([(1, 0), (-1, 0), (0, 1), (0, -1)])


def get_neighbors(current, bounds):
    return (tuple(n) for n in np.array(current) + neighbor_directions if all(n >= (0, 0)) and all(n < bounds))


def find_basin(lines: List[str]):
    _, minima, data = find_minima(lines)
    res = np.where(minima)
    minima_points = np.array(list(zip(res[0], res[1])))

    basin_sizes = []
    for m in minima_points:

        seen = set([tuple(m)])
        remaining = [tuple(m)]
        while len(remaining) > 0:
            current = remaining.pop()
            neighbors = list(n for n in get_neighbors(current, data.shape) if data[n] != 9 and n not in seen)
            remaining.extend(neighbors)
            seen.update(neighbors)

        basin_sizes.append(len(seen))

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def part_1():
    return find_minima_part_1(read_lines('input.txt'))


def part_2():
    return find_basin(read_lines('input.txt'))


assert_test(find_minima_part_1(test_input), 15, 1)
assert_test(find_basin(test_input), 1134, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
