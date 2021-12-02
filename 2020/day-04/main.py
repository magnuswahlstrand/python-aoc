import re

from util import read_input, assert_test

test_input = read_input("input_test.txt")
test_input_2 = read_input("input_test_2.txt")


def has_necessary_keys(p: dict):
    return 'byr' in p and \
           'iyr' in p and \
           'eyr' in p and \
           'hgt' in p and \
           'hcl' in p and \
           'ecl' in p and \
           'pid' in p


def is_valid(passport_str: str):
    p = dict(p.split(":")[:2] for p in passport_str.split())
    return has_necessary_keys(p)


def between(val: str, low: str, high: str):
    return low <= val <= high


rgbPattern = re.compile(r"^#[0-9a-f]{6}$")
idPattern = re.compile(r"^[0-9]{9}$")


def is_valid_2(passport_str: str):
    p = dict(p.split(":")[:2] for p in passport_str.split())

    if not has_necessary_keys(p):
        return False

    if not between(p['byr'], "1920", "2002"):
        return False

    if not between(p['iyr'], "2010", "2020"):
        return False

    if not between(p['eyr'], "2020", "2030"):
        return False

    if p['hgt'].endswith("cm") and between(p['hgt'][:-2], "150", "193"):
        pass
    elif p['hgt'].endswith("in") and between(p['hgt'][:-2], "59", "76"):
        pass
    else:
        return False

    if not rgbPattern.match(p['hcl']):
        return False

    if p['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not idPattern.match(p['pid']):
        return False

    return True


def count_valid_passports(input: str, validate_func=is_valid):
    return sum(validate_func(passport) for passport in input.split('\n\n'))


def part_1():
    return count_valid_passports(read_input("input.txt"))


def part_2():
    return count_valid_passports(read_input("input.txt"), is_valid_2)


assert_test(count_valid_passports(test_input), 2, 1)
assert_test(count_valid_passports(test_input_2, is_valid_2), 4, 2)

print("result for day-1:", part_1())
print("result for day-2:", part_2())
