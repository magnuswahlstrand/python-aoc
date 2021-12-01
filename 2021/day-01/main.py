from util import read_input


def count_increasing(input_file: str, distance: int = 1):
    lines = read_input(input_file)
    return sum(int(b) > int(a) for (a, b) in zip(lines, lines[distance:]))


def part_1():
    return count_increasing("input.txt")


def part_2():
    return count_increasing("input.txt", 3)


test_count = count_increasing("input_test.txt")
assert test_count == 7
print("result for day-1 test is:", test_count, "as expected")

test_count2 = count_increasing("input_test.txt", 3)
assert test_count2 == 5
print("result for day-2 test is:", test_count2, "as expected")

print()
print("result for day-1:", part_1())
print("result for day-2:", part_2())
