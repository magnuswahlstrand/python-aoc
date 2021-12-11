from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")


def count_1_4_7_8s(lines: List[str]):
    return sum(sum(True for n in o if len(n) in (2, 3, 4, 7)) for o in
               (output.split() for _, output in (line.split(" | ", maxsplit=2) for line in lines)))


d = {i: set(s) for i, s in enumerate([
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
])}

intersections = {n: [len(set(d[n]).intersection(d[n2])) for n2 in (1, 4, 7, 8)] for n in range(10)}


def intersections_with_known(s, known):
    return [len(set(s).intersection(k)) for k in known]


def calc_entry(line: str):
    displays, output = line.split(" | ", maxsplit=2)

    # Sort segments dcbef --> bcdef
    displays_text_sorted = [''.join(sorted(s)) for s in displays.split()]
    output_text_sorted = [''.join(sorted(o)) for o in output.split()]

    # By length of display
    displays_text_sorted.sort(key=len)
    n1, n7, n4, *rest, n8 = displays_text_sorted

    # Now we have 4 known numbers
    known = [set(n) for n in (n1, n4, n7, n8)]

    found = {n1: 1, n4: 4, n7: 7, n8: 8}
    for n in [0, 2, 3, 5, 6, 9]:
        f = next(r for r in rest if intersections_with_known(r, known) == intersections[n])
        found[f] = n

    return int(''.join(map(str, (found[o] for o in output_text_sorted))))


def count_sums(input):
    return sum(calc_entry(line) for line in input)


def part_1():
    return count_1_4_7_8s(read_lines('input.txt'))


def part_2():
    return count_sums(read_lines('input.txt'))


assert_test(count_1_4_7_8s(test_input), 26, 1)
assert calc_entry("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf") == 5353
assert_test(count_sums(test_input), 61229, 1)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
