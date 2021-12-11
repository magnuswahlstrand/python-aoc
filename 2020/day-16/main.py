import re

from util import read_input, assert_test

test_input = read_input("input_test.txt")
test_input_2 = read_input("input_test_2.txt")


def is_valid_field(field, rules):
    for rule in rules:
        if rule[0] <= field <= rule[1] or rule[2] <= field <= rule[3]:
            return True

    return False


def scanning_error_rate(_input: str):
    rules_raw, _, nearby = _input.split("\n\n", maxsplit=3)

    rules = [list(map(int, re.findall(r'(\d+)', r))) for r in rules_raw.split('\n')]
    sum = 0
    for ticket in nearby.split('\n')[1:]:
        fields = map(int, ticket.split(','))
        for field in fields:
            if not is_valid_field(field, rules):
                sum += field

    return sum


def rule_valid_for_field(field, rule):
    return rule[0] <= field <= rule[1] or rule[2] <= field <= rule[3]


def your_ticket_value(_input: str):
    rules_raw, yours, nearby = _input.split("\n\n", maxsplit=3)
    your_ticket_value = list(map(int, yours.split('\n')[1].split(',')))

    rules = [list(map(int, re.findall(r'(\d+)', r))) for r in rules_raw.split('\n')]
    valid_tickets = [your_ticket_value]
    for ticket_raw in nearby.split('\n')[1:]:
        ticket = list(map(int, ticket_raw.split(',')))
        if is_valid_ticket(ticket, rules):
            valid_tickets.append(ticket)

    departure_rule_indices = [i for i, line in enumerate(rules_raw.split('\n')) if line.startswith("departure")]

    num_rules = len(rules)
    rule_matches = {}
    for i, rule in enumerate(rules):
        matches = []
        for n in range(num_rules):
            if all(rule_valid_for_field(ticket[n], rule) for ticket in valid_tickets):
                matches.append(n)

        rule_matches[i] = set(matches)

    product = 1
    while len(rule_matches) > 0:
        rule_index, val = next((k, r) for k, r in rule_matches.items() if len(r) == 1)
        value = val.pop()

        if rule_index in departure_rule_indices:
            product *= your_ticket_value[value]

        del rule_matches[rule_index]
        for rule_match in rule_matches.values():
            rule_match.discard(value)

    return product


def is_valid_ticket(fields, rules):
    for field in fields:
        if not is_valid_field(field, rules):
            return False
    return True


def part_1():
    return scanning_error_rate(read_input('input.txt'))


def part_2():
    return your_ticket_value(read_input('input.txt'))


assert_test(scanning_error_rate(test_input), 71, 1)
print("result for day-1:", part_1())
print("result for day-2:", part_2())

print(rule_valid_for_field(40, (36, 269, 275, 973)))
