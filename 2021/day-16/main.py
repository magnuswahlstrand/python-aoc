import binascii
from typing import List

import numpy as np

from util import read_lines, assert_test, read_input

test_input = read_lines("input_test.txt")


def print_bytes(bs):
    print(to_bin(bs))


def to_bin(bs):
    return bin(int.from_bytes(bs, "big"))[2:].zfill(len(bs) * 8)


def read_bytes(bs: str, num_bytes, i):
    return bs[i:i + num_bytes], i + num_bytes


def read_bytes_int(bs: str, num_bytes, i):
    read_bs, i = read_bytes(bs, num_bytes, i)
    return int(read_bs, 2), i


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


def parse_packet(h):
    i = 0
    _ver, i = read_bytes_int(h, 3, i)
    _type, i = read_bytes_int(h, 3, i)

    if _type == 4:
        val = ""
        while True:
            prefix, i = read_bytes(h, 1, i)
            v, i = read_bytes(h, 4, i)
            val += v
            if prefix == '0':
                return int(val, 2), i, _ver
    else:
        len_type, i = read_bytes(h, 1, i)
        sum_ver = _ver
        vals = []

        if len_type == '0':
            length, i = read_bytes_int(h, 15, i)
            target = i + length
            while i < target:
                i, sum_ver, v = parse_packet_and_step(h, i, sum_ver)
                vals.append(v)
        else:
            length, i = read_bytes_int(h, 11, i)
            for _ in range(length):
                i, sum_ver, v = parse_packet_and_step(h, i, sum_ver)
                vals.append(v)

        return op(_type, vals), i, sum_ver


def parse_packet_and_step(h, i, sum_ver):
    v, j, _ver = parse_packet(h[i:])
    i += j
    sum_ver += _ver
    return i, sum_ver, v


def calc_sum_versions(input: str):
    h = to_bin(binascii.unhexlify(input))
    val, i, vers = parse_packet(h)
    return vers


def calc_everything(input: str):
    h = to_bin(binascii.unhexlify(input))
    val, i, vers = parse_packet(h)
    return val


def part_1():
    return calc_sum_versions(read_input('input.txt'))


def part_2():
    return calc_everything(read_input('input.txt'))


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

# assert_test(foobar_v2(test_input), 230, 2)
print("result for day-1:", part_1())
print("result for day-2:", part_2())
