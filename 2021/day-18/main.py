from __future__ import annotations

import copy
import json
import math
from itertools import combinations

from util import read_lines, assert_test

test_input = read_lines("input_test.txt")
test_input_0 = read_lines("input_test_0.txt")


class Node:
    def __init__(self, data):
        if isinstance(data, int):
            self.left = None
            self.right = None
            self.data = data
            return
        self.left = data[0] if isinstance(data[0], Node) else Node(data[0])
        self.right = data[1] if isinstance(data[1], Node) else Node(data[1])
        self.data = None

    def find_depth(self, depth, current_depth=0) -> Node:
        if self.data is not None:
            return None

        if depth == current_depth:
            return self

        n = self.left.find_depth(depth, current_depth + 1)
        if n:
            return n

        return self.right.find_depth(depth, current_depth + 1)

    def __iter__(self):
        if self.data is not None:
            yield self
        else:
            yield from self.left
            yield from self.right

    def __repr__(self):
        if self.data is not None:
            return str(self.data)
        return f'[{self.left},{self.right}]'

    def collapse(self):
        self.left = None
        self.right = None
        self.data = 0

    def split(self):

        self.left = Node(int(math.floor(self.data / 2)))
        self.right = Node(int(math.ceil(self.data / 2)))
        self.data = None

    def __add__(self, other):
        if not isinstance(other, Node):
            raise ValueError("unexpected type", type(other))
        return Node([self, other])

    def magnitude(self):
        if self.data is not None:
            return self.data

        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def explode(root: Node):
    found = root.find_depth(4)
    if found is None:
        return False

    leaves = [leaf for leaf in root]
    i = leaves.index(found.left)
    if i - 1 >= 0:
        leaves[i - 1].data += leaves[i].data
    if i + 2 < len(leaves):
        leaves[i + 2].data += leaves[i + 1].data
    found.collapse()
    return True


def split(root: Node):
    found = next((leaf for leaf in root if leaf.data and leaf.data >= 10), None)
    if found is None:
        return False

    found.split()
    return True


def reduce(root: Node):
    print('before', root)
    for i in range(1000):
        # print(root)

        if explode(root):
            # print('explode  ', end='')
            continue

        if split(root):
            # print('split    ', end='')
            continue

        break
    print('the end')
    print(root)


def reduce_and_add(ls):
    print('start')
    root = Node(ls[0])
    reduce(root)
    for l in ls[1:]:
        root += Node(l)
        reduce(root)
    return root


def assert_explode(ls, expected):
    n = Node(ls)
    explode(n)
    assert repr(n) == expected, repr(n)


assert_explode([[[[[9, 8], 1], 2], 3], 4], "[[[[0,9],2],3],4]")
assert_explode([7, [6, [5, [4, [3, 2]]]]], "[7,[6,[5,[7,0]]]]")
assert_explode([[6, [5, [4, [3, 2]]]], 1], "[[6,[5,[7,0]]],3]")
assert_explode([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
assert_explode([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

# Test addition
added = repr(Node([1, 1]) + Node([2, 2]) + Node([3, 3]) + Node([4, 4]))
assert added == "[[[[1,1],[2,2]],[3,3]],[4,4]]"

# Small testcase
root = Node([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]) + Node([1, 1])
reduce(root)
assert repr(root) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", root

# TC 3
ls = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
root = reduce_and_add(ls)
assert repr(root) == "[[[[3,0],[5,3]],[4,4]],[5,5]]", repr(root)

# TC 5

ls = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
root = reduce_and_add(ls)
assert repr(root) == "[[[[5,0],[7,4]],[5,5]],[6,6]]", repr(root)

# TC 4
assert Node([[1, 2], [[3, 4], 5]]).magnitude() == 143
assert Node([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).magnitude() == 1137
assert Node([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]).magnitude() == 3488

# Test split
n = Node([[[[0, 7], 4], [16, [0, 13]]], [1, 1]])
split(n)
assert repr(n) == "[[[[0,7],4],[[8,8],[0,13]]],[1,1]]", repr(n)


def get_magnitude(ls_raw):
    ls = [json.loads(line) for line in ls_raw]
    return reduce_and_add(ls).magnitude()


def get_highest_magnitude(ls_raw):
    ls = [json.loads(line) for line in ls_raw]
    combs = list(combinations(ls, 2))

    mags = []
    print(len(combs))
    for c in combs:
        c2 = copy.deepcopy(c)
        c3 = list(reversed(copy.deepcopy(c)))
        mags.append(reduce_and_add(c2).magnitude())
        mags.append(reduce_and_add(c3).magnitude())

    return max(mags)


def part_1():
    return get_magnitude(read_lines('input.txt'))


def part_2():
    return get_highest_magnitude(read_lines('input.txt'))


assert_test(get_magnitude(test_input), 4140, 1)
assert_test(get_highest_magnitude(test_input), 3993, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
