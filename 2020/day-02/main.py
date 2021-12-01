import re

regex = re.compile(r'(\d+)-(\d+) (\w+): (\w+)')


def parse_passports(lines: str):
    return re.findall(regex, lines)


def is_valid(lower_str: str, upper_str: str, c: str, passport: str):
    count = passport.count(c)
    return int(lower_str) <= count <= int(upper_str)


def count_valid_passports(filename: str):
    input = read_input(filename)
    return len([passport for passport in parse_passports(input) if is_valid(*passport)])


def read_input(filename: str):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    day_1 = count_valid_passports("input.txt")
    # day_2 = find_product_day2(input.input, 2020)
    print(f"result for day 1 is: {day_1}")
    # print(f"result for day 2 is: {day_2}")
