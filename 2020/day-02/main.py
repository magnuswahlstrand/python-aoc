import re

regex = re.compile(r'(\d+)-(\d+) (\w+): (\w+)')


def parse_passports(lines: str):
    return re.findall(regex, lines)


def is_valid(lower_str: str, upper_str: str, c: str, passport: str):
    count = passport.count(c)
    return int(lower_str) <= count <= int(upper_str)


def is_valid_v2(idx_1: str, idx_2: str, c: str, passport: str):
    # Either one of these must be true
    return (passport[int(idx_1) - 1] == c) != (passport[int(idx_2) - 1] == c)


def count_valid_passports(filename: str, validator_func=is_valid):
    input = read_input(filename)
    return len([passport for passport in parse_passports(input) if validator_func(*passport)])


def read_input(filename: str):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    day_1 = count_valid_passports("input.txt")
    day_2 = count_valid_passports("input.txt", is_valid_v2)
    print(f"result for day 1 is: {day_1}")
    print(f"result for day 2 is: {day_2}")
