from collections import Counter

from util import read_input, assert_test

test_input = read_input("input_test.txt")
test_input_2 = read_input("input_test_2.txt")


class Node:
    def __init__(self, val, next):
        self.data = val
        self.next = next

    def __str__(self):
        return self.data

    # Maybe a bit overkill
    def __add__(self, other):
        return str(self) + str(other)

    def __iter__(self):
        n = self

        yield str(n)
        while n.next:
            n = n.next
            yield str(n)


def run_simulation(insertions, steps, template):
    n = None
    for t in reversed(template):
        n = Node(t, n)
    first = n
    # print(''.join(first))
    for _ in range(steps):
        n = first
        while n.next:
            n.next = Node(insertions[n + n.next], n.next)
            n = n.next.next
        # print(''.join(first))
    polymer = ''.join(first)
    return Counter(polymer), polymer


def count_polymer(_input: str, steps=10):
    template, ins = _input.split('\n\n', maxsplit=2)
    insertions = {line[0:2]: line[6] for line in ins.split('\n')}

    count, _ = run_simulation(insertions, steps, template)
    cmn = count.most_common()
    return cmn[0][1] - cmn[-1][1]


def generate_pairs(template: str):
    return [a + b for (a, b) in zip(template[:-1], template[1:])]


def count_polymer_v2(_input: str, steps=10):
    template, ins = _input.split('\n\n', maxsplit=2)
    insertions = {line[0:2]: line[6] for line in ins.split('\n')}

    counter_dict = {}
    seen = set()
    remaining_pairs = generate_pairs(template)
    while len(remaining_pairs) > 0:
        p = remaining_pairs.pop()
        seen.add(p)

        count, resulting_polymer = run_simulation(insertions, 5, p)
        pairs = generate_pairs(resulting_polymer)
        for pair in pairs:
            if pair not in seen:
                remaining_pairs.append(pair)

        counter_dict[p] = Counter(pairs)

    c = Counter(generate_pairs(template))
    for s in range(5, steps + 1, 5):
        c = count_after_5(counter_dict, c)

    c2 = Counter(template)
    for k, v in c.items():
        c2[k[0]] += v
        c2[k[1]] += v

    cmn = c2.most_common()
    return (cmn[0][1] - cmn[-1][1]) / 2


def count_polymer_v3(_input: str, steps=10):
    template, ins = _input.split('\n\n', maxsplit=2)
    insertions = {line[0:2]: line[6] for line in ins.split('\n')}

    c = Counter(generate_pairs(template))
    for s in range(steps):
        c_out = Counter()
        for pair, count in c.items():
            new = pair[0] + insertions[pair] + pair[1]
            c_out.update({new[:2]: count})
            c_out.update({new[1:]: count})
        c = c_out

    c2 = Counter(template)
    for k, v in c.items():
        c2[k[0]] += v
        c2[k[1]] += v

    cmn = c2.most_common()
    return (cmn[0][1] - cmn[-1][1]) / 2


def count_after_5(per_iteration_dict, c_in):
    c_out = Counter()
    for pair, count in c_in.items():
        c_out.update({k: count * v for k, v in per_iteration_dict[pair].items()})
    return c_out


def part_1():
    return count_polymer(read_input('input.txt'))


def part_2():
    return count_polymer_v3(read_input('input.txt'), 40)


assert_test(count_polymer(test_input, 10), 1588, 1)
assert_test(count_polymer_v2(test_input, 10), 1588, 1)
assert_test(count_polymer_v2(test_input_2, 10), 517, 2)
assert_test(count_polymer_v3(test_input_2, 10), 517, 2)

print("result for day-1:", part_1())
print("result for day-2:", part_2())
