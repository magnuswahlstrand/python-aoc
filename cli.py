import os
import sys
from distutils.dir_util import copy_tree

import requests

args = sys.argv[1:]
print(args)


def setup_day(year, day, add_test=False):
    if 'AOC_SESSION' not in os.environ:
        print('please set AOC_SESSION')
        sys.exit(1)

    session = os.environ['AOC_SESSION']

    # Copy template
    padded_day = day.zfill(2)
    fr_dir = './template'
    to_dir = f'./{year}/day-{padded_day}'
    print(f'copying template from "{fr_dir}" to "{to_dir}"')
    copy_tree(fr_dir, to_dir)

    # Download input
    print('download input')
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    with requests.get(url, stream=True, cookies={'session': session}) as r:
        r.raise_for_status()
        with open(to_dir + "/input.txt", 'w') as f:
            f.write(r.text.strip())

    # Add test
    if add_test:
        print('add test')
        contents = []
        print('please enter test input')
        while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
        with open(to_dir + "/input_test.txt", 'w') as f:
            f.write('\n'.join(contents))


if args[0] == 'setup':
    add_test = False
    if len(args) > 3 and args[3] == 'test':
        add_test = True

    setup_day(args[1], args[2], add_test)

print('done')
