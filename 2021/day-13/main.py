import numpy as np

from util import assert_test, read_input

test_input = read_input("input_test.txt")


def print_world_v2(world):
    for row in world.transpose():
        for c in row:
            print("#" if c > 0 else ' ', end='')
        print()


def count_after_first_fold(_input: str, max_folds=1, should_print=False):
    # Setup
    c_raw, folds = _input.split('\n\n')
    coords = [tuple(int(v) for v in line.split(',')) for line in c_raw.split('\n')]
    dim = np.max(coords, 0) + (1, 1)
    world = np.zeros(dim)
    for c in coords:
        world[c] = 1

    # Folding time
    for f in folds.split('\n')[:max_folds]:
        txt, num = f.split("=")
        n = int(num)
        if txt[-1] == 'y':
            world = world[:, 0:n] + np.fliplr(world[:, n + 1:])
        elif txt[-1] == 'x':
            world = world[0:n, :] + np.flipud(world[n + 1:, :])

    if should_print:
        print_world_v2(world)

    return np.count_nonzero(world)


def part_1():
    return count_after_first_fold(read_input('input.txt'))


def part_2():
    return count_after_first_fold(read_input('input.txt'), None, True)


assert_test(count_after_first_fold(test_input), 17, 1)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
