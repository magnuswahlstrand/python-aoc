import copy
from itertools import product
from typing import List

from util import assert_test, read_lines

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split()


def next_state(c, n):
    if c == 'L' and n == 0:
        return '#', 1
    if c == '#' and n >= 4:
        return 'L', 1
    return c, 0


def find_neighbors(board, coords, height, width):
    neighbors = {}
    for c in coords:
        x1, x2, y1, y2 = max(0, c[0] - 1), min(width - 1, c[0] + 1), max(0, c[1] - 1), min(height - 1, c[1] + 1)
        neighbors[c] = [n for n in product(range(x1, x2 + 1), range(y1, y2 + 1)) if n != c and board[n[1]][n[0]] != '.']
    return neighbors


def find_neighbors_v2(board, coords, height, width):
    neighbors = {}
    dirs = list(n for n in product(range(-1, 2), range(-1, 2)) if n != (0, 0))
    for c in coords:
        ns = []
        for d in dirs:
            x, y = (c[0] + d[0], c[1] + d[1])
            while 0 <= x < width and 0 <= y < height:
                if board[y][x] == 'L':
                    ns.append((x, y))
                    break
                x += d[0]
                y += d[1]
        neighbors[c] = ns
    return neighbors


def count_stable_seats(lines: List[str], neighbor_func=find_neighbors, tolerance=4):
    board = [list(line) for line in lines]
    width, height = len(board[0]), len(board)
    coords = tuple(product(range(width), range(height)))

    neighbors = neighbor_func(board, coords, height, width)
    return step_state_machine(board, coords, neighbors, tolerance)


def step_state_machine(board, coords, neighbors, tolerance):
    board2 = copy.deepcopy(board)  # Just need the right dimensions

    # Initialize to something greater than 0
    i = 0
    num_updates = 1
    while num_updates > 0:
        i += 1
        num_updates = 0
        for c in coords:
            current = board[c[1]][c[0]]
            if current == '.':
                pass

            count = sum(board[n[1]][n[0]] == '#' for n in neighbors[c])

            if current == 'L' and count == 0:
                board2[c[1]][c[0]] = '#'
                num_updates += 1
            elif current == '#' and count >= tolerance:
                board2[c[1]][c[0]] = 'L'
                num_updates += 1
            else:
                board2[c[1]][c[0]] = current

        board, board2 = board2, board

    return sum(row.count('#') for row in board)


def print_board(board):
    for row in board:
        for r in row:
            print(r, end='')
        print()


def part_1():
    return count_stable_seats(read_lines('input.txt'))


def part_2():
    return count_stable_seats(read_lines('input.txt'), neighbor_func=find_neighbors_v2, tolerance=5)


assert_test(count_stable_seats(test_input), 37, 1)
assert_test(count_stable_seats(test_input, neighbor_func=find_neighbors_v2, tolerance=5), 26, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
