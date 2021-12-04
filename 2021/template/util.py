from typing import List


def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read()


def read_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def assert_test(actual, expected, day):
    if actual == expected:
        print(f"test result for day-{day} is: {actual} as expected")
    else:
        print(f"ERROR: test result for day-{day} not as expected. {actual} != {expected}")
