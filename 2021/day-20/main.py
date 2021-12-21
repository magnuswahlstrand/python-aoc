from itertools import chain

import numpy as np

from util import *

test_input = read_input("input_test.txt")

bin_8_6 = (256, 128, 64)
bin_5_3 = (32, 16, 8)
bin_2_0 = (4, 2, 1)


def count_pixels(input: str, iterations=2):
    algorithm_raw, image_raw = input.split('\n\n')
    algorithm = [1 if a == '#' else 0 for a in algorithm_raw]
    image = np.pad(np.array([[1 if l == '#' else 0 for l in line] for line in image_raw.splitlines()], dtype=int),
                   iterations + 2)
    image_2 = np.zeros(image.shape, dtype=int)
    size = len(image)

    for i in range(iterations):
        for y in range(1, size - 1):
            for x in range(1, size - 1):
                a = sum(chain(image[y - 1, x - 1:x + 2] * bin_8_6,
                              image[y, x - 1:x + 2] * bin_5_3,
                              image[y + 1, x - 1:x + 2] * bin_2_0))
                image_2[y, x] = algorithm[a]
        image, image_2 = image_2, image

        # Clean up garbage at the edges, every two rounds
        if i % 2 == 1:
            image[0:2, :] = 0
            image[-2:, :] = 0
            image[:, 0:2] = 0
            # image[:, -2:] = 0 # This doesn't do anything
    print_grid(image)

    return np.count_nonzero(image)


def print_grid(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            print('#' if c == 1 else '.', end='')
        print()


def part_1():
    return count_pixels(read_input('input.txt'))


def part_2():
    return count_pixels(read_input('input.txt'), 50)


assert_test(count_pixels(test_input), 35, 1)
assert_test(count_pixels(test_input, 50), 3351, 2)
# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
