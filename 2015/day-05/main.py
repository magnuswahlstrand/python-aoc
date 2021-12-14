from collections import Counter
from typing import List

from util import read_lines

test_input = read_lines("input_test.txt")

forbidden = (('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y'))


def is_nice(line):
    c = Counter(line)
    vowels = sum(v for (k, v) in c.items() if k in "aeiou")
    if vowels < 3:
        return False

    if any(pair in forbidden for pair in zip(line[:-1], line[1:])):
        return False

    if not any(pair[0] == pair[1] for pair in zip(line[:-1], line[1:])):
        return False

    return True


def is_nice_v2(line):
    if not any(pair[0] == pair[1] for pair in zip(line[:-2], line[2:])):
        return False

    if not any((line[i:i + 2] in line[0:i]) or (line[i:i + 2] in line[i + 2:]) for i in range(len(line)-1)):
        return False

    return True


def count_nice(lines: List[str], is_nice_func=is_nice):
    return sum(is_nice_func(line) for line in lines)


def part_1():
    return count_nice(read_lines('input.txt'))


def part_2():
    return count_nice(read_lines('input.txt'), is_nice_v2)


assert is_nice("ugknbfddgicrmopn")
assert is_nice("aaa")
assert not is_nice("jchzalrnumimnmhp")
assert not is_nice("haegwjzuvuyypxyu")
assert not is_nice("dvszwmarrgswjxmb")

assert is_nice_v2("qjhvhtzxzqqjkmpb")
assert is_nice_v2("xxyxx")
assert not is_nice_v2("uurcxstgmygtbstg")
assert not is_nice_v2("ieodomkazucvgmuy")
assert not is_nice_v2("xxx")

print("result for day-1:", part_1())
print("result for day-2:", part_2())
