from collections import defaultdict
from typing import List

from util import assert_test

test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")
test_input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split("\n")

test_input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split("\n")

input = """zi-end
XR-start
zk-zi
TS-zk
zw-vl
zk-zw
end-po
ws-zw
TS-ws
po-TS
po-YH
po-xk
zi-ws
zk-end
zi-XR
XR-zk
vl-TS
start-zw
vl-start
XR-zw
XR-vl
XR-ws""".split("\n")


def setup(lines):
    d = defaultdict(list)
    for start, finish in [p.split('-', maxsplit=2) for p in lines]:
        if start != 'start':
            d[finish].append(start)
        if finish != 'start':
            d[start].append(finish)
    return d


def find_paths(d, node, small_visited):
    if node == 'end':
        return [['end']]

    paths = []
    for n in d[node]:
        if n.islower() and n in small_visited:
            continue

        new_visited = [n, *small_visited] if n.islower() else small_visited[:]
        for p in find_paths(d, n, new_visited):
            paths.append([node] + p)

    return paths


def find_paths_v2(d, node, small_visited):
    if node == 'end':
        return [['end']]

    paths = []
    for n in d[node]:
        double_visit_consumed = next((v for v in small_visited.values() if v > 1), 0) != 0

        if n.islower() and (double_visit_consumed and small_visited[n] > 0):
            continue

        new_visited = small_visited.copy()
        if n.islower():
            new_visited[n] += 1

        for p in find_paths_v2(d, n, new_visited):
            paths.append([node] + p)

    return paths


def count_paths(lines: List[str]):
    d = setup(lines)
    ps = find_paths(d, 'start', ['start'])
    return len(ps)


# Inspired by https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/ho8w7hx/?utm_source=share&utm_medium=web2x&context=3
def alt_part_1(lines: List[str], can_repeat=False):
    d = defaultdict(set)
    for a, b in [p.split('-', maxsplit=2) for p in lines]:
        d[a].add(b)
        d[b].add(a)

    return alt_count_paths(d, ('start',), can_repeat)


def alt_count_paths(graph, path, can_repeat):
    if path[-1] == "end":
        return 1

    paths = 0
    for nxt in graph[path[-1]]:
        if not (nxt.islower() and nxt in path):
            paths += alt_count_paths(graph, path + (nxt,), can_repeat)
        elif can_repeat and nxt != 'start':
            paths += alt_count_paths(graph, path + (nxt,), False)

    return paths


def count_paths_v2(lines: List[str]):
    d = setup(lines)
    visited = defaultdict(int)
    ps = find_paths_v2(d, 'start', visited)
    return len(ps)


def part_1():
    return alt_part_1(input)


def part_2():
    return alt_part_1(input, True)


# assert_test(count_paths(test_input), 10, 1)
# assert_test(count_paths(test_input_2), 19, 1)
# assert_test(count_paths(test_input_3), 226, 1)
# assert_test(count_paths_v2(test_input), 36, 2)
# assert_test(count_paths_v2(test_input_2), 103, 2)
# assert_test(count_paths_v2(test_input_3), 3509, 2)
# print("result for day-1:", part_1())
# print("result for day-2:", part_2())

assert_test(alt_part_1(test_input), 10, 1)
assert_test(alt_part_1(test_input_2), 19, 1)
assert_test(alt_part_1(test_input_3), 226, 1)
# print("result for day-1:", part_1())

assert_test(alt_part_1(test_input, can_repeat=True), 36, 2)
assert_test(alt_part_1(test_input_2, can_repeat=True), 103, 2)
assert_test(alt_part_1(test_input_3, can_repeat=True), 3509, 2)
print("result for day-2:", part_2())
