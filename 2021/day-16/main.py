import binascii
from io import StringIO
from typing import List

import numpy as np

from util import read_lines, assert_test, read_input


def to_bin(bs):
    return bin(int.from_bytes(bs, "big"))[2:].zfill(len(bs) * 8)


def op(ver: str, vals: List[int]):
    if ver == 0:
        return sum(vals)
    elif ver == 1:
        return np.prod(vals)
    elif ver == 2:
        return min(vals)
    elif ver == 3:
        return max(vals)
    elif ver == 5:
        return 1 if vals[0] > vals[1] else 0
    elif ver == 6:
        return 1 if vals[0] < vals[1] else 0
    elif ver == 7:
        return 1 if vals[0] == vals[1] else 0

    raise ValueError("unexpected version", ver)


def parse_packet(h: StringIO):
    _ver = int(h.read(3), 2)
    _type = int(h.read(3), 2)
    global ver_total
    ver_total += _ver

    if _type == 4:
        val = ""
        while True:
            prefix = h.read(1)
            val += h.read(4)
            if prefix == '0':
                return int(val, 2)
    else:
        len_type = h.read(1)
        if len_type == '0':
            length = int(h.read(15), 2)
            target = h.tell() + length
            vals = []
            while h.tell() < target:
                v = parse_packet(h)
                vals.append(v)
        else:
            length = int(h.read(11), 2)
            vals = [parse_packet(h) for _ in range(length)]

        return op(_type, vals)


def calc_sum_versions(input: str):
    global ver_total
    ver_total = 0
    h = to_bin(binascii.unhexlify(input))
    parse_packet(StringIO(h))
    return ver_total


def calc_everything(input: str):
    h = to_bin(binascii.unhexlify(input))
    return parse_packet(StringIO(h))


def part_1():
    return calc_sum_versions(read_input('input.txt'))


def part_2():
    return calc_everything(read_input('input.txt'))


test_input = read_lines("input_test.txt")

assert to_bin(binascii.unhexlify("D2FE28")) == "110100101111111000101000"

assert_test(calc_sum_versions("8A004A801A8002F478"), 16, 1)
assert_test(calc_sum_versions("620080001611562C8802118E34"), 12, 1)
assert_test(calc_sum_versions("C0015000016115A2E0802F182340"), 23, 1)
assert_test(calc_sum_versions("A0016C880162017C3686B18A3D4780"), 31, 1)
print()
assert_test(calc_everything("C200B40A82"), 3, 2)
assert_test(calc_everything("04005AC33890"), 54, 2)
assert_test(calc_everything("880086C3E88112"), 7, 2)
assert_test(calc_everything("CE00C43D881120"), 9, 2)
assert_test(calc_everything("D8005AC2A8F0"), 1, 2)
assert_test(calc_everything("F600BC2D8F"), 0, 2)
assert_test(calc_everything("9C005AC2F8F0"), 0, 2)
assert_test(calc_everything("9C0141080250320F1802104A08"), 1, 2)

print("result for day-1:", part_1())
print("result for day-2:", part_2())

# Rewritten to use StringIO, inspired by mrphlip
# https://github.com/mrphlip/aoc/blob/master/2021/16.py
