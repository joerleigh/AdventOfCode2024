#! python3
import argparse
import os.path


def run_day(day, part, use_sample):
    suffix = '_sample' if use_sample else ''
    filename = f'inputs/day_{day}_{part}{suffix}.txt'
    if not os.path.isfile(filename):
        filename = f'inputs/day_{day}{suffix}.txt'

    modulename = f'day_{day}'
    day_module = __import__(modulename)

    print(f'day {day}, part {part}')
    with open(filename) as file:
        if part == 1:
            day_module.part_one(file)
        elif part == 2:
            day_module.part_two(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an Advent of Code 2024 day')
    parser.add_argument('day', type=int)
    parser.add_argument('part', type=int)
    parser.add_argument('-s', '--sample', action='store_true')
    args = parser.parse_args()

    run_day(args.day, args.part, args.sample)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
