from collections import defaultdict
from itertools import permutations, combinations

from util import *

test_input_0 = """--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1"""

test_input_1 = """--- scanner 0 ---
0,2,1
4,1,1
3,3,1

--- scanner 1 ---
-1,-1,0
-5,0,0
-2,1,0"""


def find_offset(scanner_coords, scanner_2, limit=12):
    set_1_coords = set(tuple(s) for s in scanner_coords)
    for s1 in set_1_coords:
        # Start with a coordinate
        for i, direction in enumerate(scanner_2):
            for s2 in direction:
                offset = s2 - s1
                # if offset[0] != -68 or offset[1] != 1246 or offset[2] != 43:
                #     continue
                # print("offset", ','.join(str(s) for s in offset))
                s = sum(tuple(o) in set_1_coords for o in (direction - offset))
                if s >= limit:
                    return True, offset, i

    return False, [], -1


def match_scanners(input_: str):
    scanners = parse_scanners_v2(input_)

    # for i, set_1 in enumerate(scanners):
    #
    #     for j, scn in enumerate(scanners):
    #         if j <= i:
    #             continue
    #         # print(f"find matches between {i}-{j}")
    #
    #         found, offset, index = find_offset(set_1[0], scn)
    #         if found:
    #             print(f"matches {i}-{j}: {offset} at {index}")

    seen = set()
    coords = defaultdict(int)

    todo = []
    # seen.add(0)
    # todo = [(0, scanners[0][0], (0, 0, 0))]
    update_seen_todo_and_coords(coords, 0, scanners[0][0], seen, todo, (0, 0, 0))
    while len(todo) > 0:
        i, current_set, current_offset = todo.pop()
        for j, scn in enumerate(scanners):
            if j in seen:
                continue

            found, offset, index = find_offset(current_set, scn)
            if found:
                total_offset = (current_offset + offset)
                update_seen_todo_and_coords(coords, j, scn[index], seen, todo, total_offset)

                print(f"matches {i}-{j}: {total_offset} at {index}")

    return len(coords.keys())


def update_seen_todo_and_coords(coords, j, scn_slice, seen, todo, total_offset):
    todo.append((j, scn_slice, total_offset))
    seen.add(j)
    for coord in scn_slice - total_offset:
        coords[tuple(coord)] += 1


def parse_scanners_v2(input_):
    scanners_raw = input_.split('\n\n')
    scanners = []
    perm = list(permutations((0, 1, 2)))
    for s in scanners_raw:
        scn = np.array([c.split(',') for c in s.splitlines()[1:]]).astype(int)
        scanner = []
        for p in perm:
            for flip_x in [1, -1]:
                for flip_y in [1, -1]:
                    for flip_z in [1, -1]:
                        scanner.append(np.array([(flip_x * s[p[0]], flip_y * s[p[1]], flip_z * s[p[2]]) for s in scn]))
        scanners.append(scanner)
    return scanners


def part_1():
    return match_scanners(read_input('input.txt'))


def print_s(s):
    for line in s:
        print(','.join([str(n) for n in line]))
    print()


#
# scanners = parse_scanners_v2(test_scanner_rotations)
# # for dir in scanners[0]:
# #     print_s(dir)
#
# print(find_offset(scanners[0], scanners[1]))
# print(find_offset(scanners[0], scanners[2]))
# print(find_offset(scanners[0], scanners[3]))
# print(find_offset(scanners[0], scanners[4]))

# assert_test(match_scanners(test_input), 79, 1)
# assert_test(match_scanners(test_input_1), 198, 1)
# assert_test(foobar_v2(test_input), 230, 2)

# print("result for day-1:", part_1())

# OUTPUT FROM PART 1. PART 1 TAKES MAYBE 5 MIN TO RUN :D
# matches 0-0: [0 0 0]]
# matches 0-11: [1384   51   28] at 12
# matches 0-12: [-1068    28   -46] at 27
# matches 0-24: [    6 -1158     3] at 38
# matches 24-3: [-1079 -1050   -25] at 5
# matches 24-13: [  115 -2420   -57] at 35
# matches 24-15: [   54 -1154  1091] at 38
# matches 24-26: [   86 -1126 -1316] at 3
# matches 26-5: [  130 -2317 -1215] at 41
# matches 5-25: [ 1211 -2280 -1298] at 6
# matches 25-22: [ 1247 -2338    35] at 6
# matches 22-8: [ 1348 -3620   -92] at 30
# matches 8-6: [ 1211 -4725    29] at 20
# matches 8-16: [ 1208 -3526  1199] at 23
# matches 6-21: [ 2498 -4808   -99] at 10
# matches 3-20: [-2229 -1227     1] at 24
# matches 20-18: [-2225   113  -122] at 18
# matches 18-7: [-2256  1265   -80] at 9
# matches 7-2: [-2379  1302  1231] at 37
# matches 7-9: [-1057  1345    11] at 44
# matches 12-27: [-1070   154  1168] at 47
# matches 11-1: [2459  -20   28] at 42
# matches 11-23: [1324 1197  -69] at 32
# matches 23-14: [1369 2427 -131] at 15
# matches 23-17: [1203 1282 1192] at 17
# matches 1-10: [ 2423    82 -1293] at 47
# matches 1-19: [ 2423 -1137  -148] at 29
# matches 19-4: [ 3670 -1047    -5] at 3
output_from_day_1 = [[0, 0, 0],
                     [1384, 51, 28],
                     [-1068, 28, -46],
                     [6, -1158, 3],
                     [-1079, -1050, -25],
                     [115, -2420, -57],
                     [54, -1154, 1091],
                     [86, -1126, -1316],
                     [130, -2317, -1215],
                     [1211, -2280, -1298],
                     [1247, -2338, 35],
                     [1348, -3620, -92],
                     [1211, -4725, 29],
                     [1208, -3526, 1199],
                     [2498, -4808, -99],
                     [-2229, -1227, 1],
                     [-2225, 113, -122],
                     [-2256, 1265, -80],
                     [-2379, 1302, 1231],
                     [-1057, 1345, 11],
                     [-1070, 154, 1168],
                     [2459, -20, 28],
                     [1324, 1197, -69],
                     [1369, 2427, -131],
                     [1203, 1282, 1192],
                     [2423, 82, -1293],
                     [2423, -1137, -148],
                     [3670, -1047, -5]]


def part_2():
    return max(sum(abs(np.array(a) - np.array(b))) for a, b in combinations(output_from_day_1, 2))


print("result for day-2:", part_2())
