from typing import List

from util import read_lines, assert_test

test_input_0 = ["3"]
test_input = read_lines("input_test.txt")


def count_fish(lines: List[str], total_days=18):
    d = {}
    # Fish in input is between [1..5]
    for fish_type in range(1, 7):
        fish_heap = [(fish_type, total_days)]

        n = 0
        while n < len(fish_heap):

            fish_counter, fish_total_days = fish_heap[n]
            for day in range(0, fish_total_days):

                if fish_counter == 0:
                    fish_counter += 7
                    # Spawn a new fish
                    fish_heap.append((8, fish_total_days - day - 1))

                fish_counter -= 1
            n += 1
        d[fish_type] = n

    return sum(d[int(f)] for f in lines[0].split(","))


def count_fish_v2(lines: List[str], total_days=18):
    window = (1, 1, 1, 1, 1, 1, 1, 1, 1)
    for n in range(total_days):
        window = (*window[1:], window[0] + window[2])

    reversed_window = tuple(reversed(window))
    return sum(reversed_window[int(f)] for f in lines[0].split(","))


def part_1():
    return count_fish(read_lines('input.txt'), total_days=80)


def part_2():
    return count_fish_v2(read_lines('input.txt'), total_days=256)


assert_test(count_fish_v2(test_input_0, total_days=18), 5, 2)
assert_test(count_fish_v2(test_input, total_days=18), 26, 2)
assert_test(count_fish_v2(test_input, total_days=80), 5934, 2)
assert_test(count_fish_v2(test_input, total_days=256), 26984457539, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
