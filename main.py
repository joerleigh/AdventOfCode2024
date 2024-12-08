#! python3
import argparse

from aoc import run_day

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an Advent of Code 2024 day')
    parser.add_argument('day', type=int)
    parser.add_argument('part', type=int)
    parser.add_argument('-s', '--sample', action='store_true')
    args = parser.parse_args()

    print(run_day(args.day, args.part, args.sample))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
