from util import read_input


def count_increasing(input_file: str):
    lines = read_input(input_file)
    return sum([1 for (a, b) in zip(lines, lines[1:]) if int(b) > int(a)])

def count_increasing_average(input_file: str):
    lines = read_input(input_file)
    return sum([1 for (a, b) in zip(lines, lines[3:]) if int(b) > int(a)])


test_count = count_increasing("input_test.txt")
assert test_count == 7
print("result for day-1 test is:", test_count, "as expected")
test_count = count_increasing_average("input_test.txt")
assert test_count == 5
print("result for day-2 test is:", test_count, "as expected")

print("result for day-1:", count_increasing("input.txt"))
print("result for day-2:", count_increasing_average("input.txt"))

