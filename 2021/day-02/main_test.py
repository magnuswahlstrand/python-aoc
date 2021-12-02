from main import parse_instructions
from util import read_lines

test_input = read_lines('input_test.txt')

assert list(parse_instructions(test_input))[0] == (5, 0)
assert list(parse_instructions(test_input))[1] == (0, 5)
