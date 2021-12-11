import re
from typing import List

from util import read_input, assert_test

test_input = read_input("input_test.txt")
test_input_2 = read_input("input_test_2.txt")


def parse_rule(rule_raw: str) -> List:
    l = []
    for r in rule_raw.split(' '):
        if r.startswith("\""):
            return r[1]
        else:
            l.append(r)
    return l


def setup(_input):
    rules, messages = _input.split('\n\n', maxsplit=2)
    d = {}
    for rule in rules.split('\n'):
        ns, r = rule.split(": ", maxsplit=2)
        d[ns] = parse_rule(r)
    return d, messages


def eval_rule(key, rules, v2=False):
    if key == '8' or key == '11':
        pass

    if key == '|':
        return '|'

    if isinstance(rules[key], str) and rules[key][0] != '|':
        return rules[key]

    res = ''.join(eval_rule(r, rules, v2) for r in rules[key])
    return f'({res})'


def count_valid_message(_input: str, replace=False):
    d, messages = setup(_input)

    if replace:
        r42 = eval_rule('42', d, replace)
        r31 = eval_rule('31', d, replace)
        d['8'] = f"{r42}+"
        v = f"({r42}{r31}|{r42}{r42}{r31}{r31}|{r42}{r42}{r42}{r31}{r31}{r31}|{r42}{r42}{r42}{r42}{r31}{r31}{r31}{r31})"
        d['11'] = v

    pattern = eval_rule('0', d, replace)
    r = re.compile(f'^{pattern}$')
    print(f'^{pattern}$')

    return len([message for message in messages.split('\n') if r.match(message) is not None])


def part_1():
    return count_valid_message(read_input('input.txt'))


def part_2():
    return count_valid_message(read_input('input.txt'), replace=True)


assert_test(count_valid_message(test_input), 2, 1)
assert_test(count_valid_message(test_input_2, replace=True), 12, 1)

print("result for day-1:", part_1())
print("result for day-2:", part_2())
