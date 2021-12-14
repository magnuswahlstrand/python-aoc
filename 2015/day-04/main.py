import hashlib

from util import read_lines

test_input = read_lines("input_test.txt")
salt = 'yzbqklnj'


def find_hash_iter(salt, target_prefix):
    return next(
        i for i in range(1, 10000000) if hashlib.md5((salt + str(i)).encode()).hexdigest().startswith(target_prefix))


def part_1():
    return find_hash_iter(salt, "00000")


def part_2():
    return find_hash_iter(salt, "000000")


# assert_test(find_hash_iter(test_input), 198, 1)
# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
