import time
from collections import namedtuple
from functools import lru_cache

from util import *

test_input = read_lines("input_test.txt")


class Player:
    def __init__(self, index, position):
        self.index = index
        self.score = 0
        self.pos = position

    def __repr__(self):
        return f'p{self.index}(space={self.pos},score={self.score})'


def roll_die(v):
    v = v % 100 + 1
    return v, v


def deterministic_die(lines: List[str]):
    p = Player(0, int(lines[0][-1:]))
    q = Player(1, int(lines[1][-1:]))

    d, v = 0, 0
    while p.score < 1000 and q.score < 1000:
        v, v1 = roll_die(v)
        v, v2 = roll_die(v)
        v, v3 = roll_die(v)
        d += 3

        p.pos = (p.pos + v1 + v2 + v3 - 1) % 10 + 1
        p.score += p.pos

        p, q = q, p

    return p.score * d


possible_dice_rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

UpdatedState = namedtuple('UpdatedState', "updated_pos updated_score")


def dirac_die(lines: List[str]):
    c_pos = int(lines[0][-1:])
    o_pos = int(lines[1][-1:])
    return max(play_game(c_pos, 0, o_pos, 0))


def next_player_state(c_pos, c_score):
    for roll, multiplier in possible_dice_rolls.items():
        updated_pos = (c_pos + roll - 1) % 10 + 1
        updated_score = c_score + updated_pos
        yield multiplier, UpdatedState(updated_pos, updated_score)


@lru_cache(maxsize=None)
def play_game(c_pos, c_score, o_pos, o_score):
    if o_score >= 21:
        return 0, 1  # Other player won

    c_sum, o_sum = 0, 0
    for multiplier, c in next_player_state(c_pos, c_score):
        result = play_game(o_pos, o_score, c.updated_pos, c.updated_score)
        c_sum += multiplier * result[1]
        o_sum += multiplier * result[0]

    return c_sum, o_sum


def part_1():
    return deterministic_die(read_lines('input.txt'))


def part_2():
    return dirac_die(read_lines('input.txt'))


assert_test(deterministic_die(test_input), 739785, 1)
# assert_test(dirac_die(test_input), 444356092776315, 2)
print("result for day-1:", part_1())

start = time.time()
print("result for day-2:", part_2())
end = time.time()
print(end - start)
