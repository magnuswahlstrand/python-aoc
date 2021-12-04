from util import read_input, assert_test

test_input = read_input("input_test.txt")


class Board:

    def __init__(self, id):
        self.id = id
        self.cols = [0] * 5
        self.rows = [0] * 5
        self.numbers = {}
        self.marked = set()
        self.has_bingo = False

    def __repr__(self):
        return f"Board({self.id})"

    def mark_number(self, number):
        c, r = self.numbers[number]
        self.cols[c] += 1
        self.rows[r] += 1
        self.marked.add(number)
        self.has_bingo = self.cols[c] == 5 or self.rows[r] == 5

    def sum_remaining(self):
        return sum(int(key) for key in self.numbers.keys() if key not in self.marked)


def setup(input):
    section_1, *rest = input.split('\n\n')
    numbers = section_1.split(',')
    boards = []
    for i, b in enumerate(rest):
        board = Board(i)
        for r, row in enumerate(b.split('\n')):
            for c, number in enumerate(row.split()):
                board.numbers[number] = (c, r)
        boards.append(board)
    return numbers, boards


def find_bingo(input: str):
    numbers, boards = setup(input)

    for number in numbers:
        for board in boards:
            if number in board.numbers:
                board.mark_number(number)
                if board.has_bingo:
                    return int(number) * board.sum_remaining()


def find_last_bingo(input: str):
    numbers, boards = setup(input)

    remaining_boards = len(boards)
    for number in numbers:
        for board in boards:
            if board.has_bingo:
                continue

            if number in board.numbers:
                1
                if board.has_bingo:
                    remaining_boards -= 1

            if remaining_boards == 0:
                return int(number) * board.sum_remaining()


def part_1():
    return find_bingo(read_input('input.txt'))


def part_2():
    return find_last_bingo(read_input('input.txt'))


assert_test(find_bingo(test_input), 4512, 1)
assert_test(find_last_bingo(test_input), 1924, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
