import heapq
from collections import defaultdict
from typing import List

from util import read_lines, neighbors_manhattan, assert_test

test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split('\n')


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def repeat_world(world, times=5):
    new_world = []
    for j in range(times):
        for row in world:
            new_world.append([(c + i + j - 1) % 9 + 1 for i in range(times) for c in row])
    return new_world


def path_to_goal(lines: List[str], repeat=False):
    world = [[int(c) for c in line] for line in lines]
    if repeat:
        world = repeat_world(world)

    d = {}
    for y, row in enumerate(world):
        for x, c in enumerate(row):
            d[x, y] = world[y][x]

    start = (0, 0)
    dims = len(world[0]), len(world)
    goal = len(world[0]) - 1, len(world) - 1

    h = lambda v: (abs(v[0] - goal[0]) + abs(v[1] - goal[1]))

    came_from = {}

    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = h(start)

    open_set = PriorityQueue()
    open_set.push(start, f_score[start])
    seen = set()

    i = 0
    while len(open_set) > 0:
        i += 1
        current = open_set.pop()

        if current == goal:
            path = reconstruct_path(came_from, current)
            return sum(d[n] for n in path if n is not start)

        for n in neighbors_manhattan(current, dims):

            tentative_gscore = g_score[current] + d[n]
            if tentative_gscore < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_gscore
                f_score[n] = tentative_gscore + h(n)

                if n not in seen:
                    open_set.push(n, f_score[n])
                    seen.add(n)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def __len__(self):
        return len(self._queue)

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def part_1():
    return path_to_goal(read_lines('input.txt'))


def part_2():
    return path_to_goal(read_lines('input.txt'), repeat=True)


assert_test(path_to_goal(test_input), 40, 1)
assert_test(path_to_goal(test_input, repeat=True), 315, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
