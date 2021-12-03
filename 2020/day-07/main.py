import re
from typing import List

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")
test_input_2 = read_lines("input_test_2.txt")

outside_pattern = re.compile(r'^\w+ \w+')
inside_pattern = re.compile(r'(\d+) (\w+ \w+)')

from collections import defaultdict


def num_bags_containing_shiny_gold_bag(lines: List[str]):
    is_contained_by = defaultdict(list)
    for line in lines:
        m = re.search(outside_pattern, line)
        outer_bag = m.group()  # Will throw error if no match
        for match in re.findall(inside_pattern, line):
            is_contained_by[match[1]].append(outer_bag)

    seen = set()
    bags = ['shiny gold']
    i = 0
    while i < len(bags):
        for outer_bag in is_contained_by[bags[i]]:
            if outer_bag not in seen:
                bags.append(outer_bag)
            seen.add(outer_bag)
        i += 1
    return len(seen)


def count_bags(contains, bag):
    bags = contains[bag]
    if len(bags) == 0:
        return 1

    return sum(int(b[0]) * count_bags(contains, b[1]) for b in bags) + 1  # Count the bag itself


def num_bags_inside_shiny_gold_bag(lines: List[str]):
    contains = defaultdict(list)
    for line in lines:
        m = re.search(outside_pattern, line)
        outer_bag = m.group()  # Will throw error if no match
        for match in re.findall(inside_pattern, line):
            contains[outer_bag].append(match)

    return count_bags(contains, 'shiny gold') - 1  # Remove the outer bag itself


def part_1():
    return num_bags_containing_shiny_gold_bag(read_lines("input.txt"))


def part_2():
    return num_bags_inside_shiny_gold_bag(read_lines("input.txt"))


assert_test(num_bags_containing_shiny_gold_bag(test_input), 4, 1)
assert_test(num_bags_inside_shiny_gold_bag(test_input), 32, 2)
assert_test(num_bags_inside_shiny_gold_bag(test_input_2), 126, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
